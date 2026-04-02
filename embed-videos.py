#!/usr/bin/env python3
"""
Embed video tags into all module pages, replacing SVG play-button placeholders.

Usage:
    python embed-videos.py                  # Use local symlinked path
    python embed-videos.py --base-url https://cdn.example.com/clips

The script:
1. Creates a symlink from docs/growthx/videos/ → Content Vault/videos/clips/
2. Finds every inline-clip-body in modules/01-07.html
3. Replaces the SVG placeholder with a <video> tag pointing to the correct file
"""

import os
import re
import sys
import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MODULES_DIR = os.path.join(SCRIPT_DIR, "modules")
CLIPS_ROOT = os.path.join(SCRIPT_DIR, "..", "..", "Content Vault", "videos", "clips")
SYMLINK_PATH = os.path.join(SCRIPT_DIR, "videos")

CLIP_FILES = {}
for mod_dir in sorted(glob.glob(os.path.join(CLIPS_ROOT, "module-*"))):
    mod_num = os.path.basename(mod_dir).replace("module-", "")
    clips = sorted(f for f in os.listdir(mod_dir) if f.endswith(".mp4"))
    CLIP_FILES[mod_num] = clips

def create_symlink():
    target = os.path.relpath(CLIPS_ROOT, SCRIPT_DIR)
    if os.path.islink(SYMLINK_PATH):
        os.unlink(SYMLINK_PATH)
    elif os.path.exists(SYMLINK_PATH):
        print(f"  ⚠ {SYMLINK_PATH} exists and is not a symlink, skipping")
        return
    os.symlink(target, SYMLINK_PATH)
    print(f"  ✓ Symlink: videos/ → {target}")

def build_video_tag(base_url, mod_num, clip_filename):
    if base_url:
        src = f"{base_url.rstrip('/')}/module-{mod_num}/{clip_filename}"
    else:
        src = f"../videos/module-{mod_num}/{clip_filename}"

    return (
        f'<video controls preload="metadata" playsinline '
        f'style="width:100%;display:block;background:#000;">\n'
        f'        <source src="{src}" type="video/mp4">\n'
        f'      </video>'
    )

SVG_PLACEHOLDER = re.compile(
    r'<div class="inline-clip-body">\s*'
    r'<svg[^>]*>.*?</svg>\s*'
    r'</div>',
    re.DOTALL
)

VIDEO_EXISTING = re.compile(
    r'<div class="inline-clip-body">\s*'
    r'<video[^>]*>.*?</video>\s*'
    r'</div>',
    re.DOTALL
)

def patch_module(mod_num, base_url):
    filepath = os.path.join(MODULES_DIR, f"{mod_num}.html")
    if not os.path.exists(filepath):
        print(f"  ✗ {filepath} not found")
        return 0

    with open(filepath, "r") as f:
        html = f.read()

    clips = CLIP_FILES.get(mod_num, [])
    if not clips:
        print(f"  ✗ No clip files found for module-{mod_num}")
        return 0

    clip_idx = [0]
    replaced = [0]

    def replacer(match):
        idx = clip_idx[0]
        if idx >= len(clips):
            return match.group(0)
        tag = build_video_tag(base_url, mod_num, clips[idx])
        clip_idx[0] += 1
        replaced[0] += 1
        return f'<div class="inline-clip-body">\n      {tag}\n    </div>'

    html = SVG_PLACEHOLDER.sub(replacer, html)

    # Also replace existing video tags (for re-runs with different base URL)
    if replaced[0] == 0:
        clip_idx[0] = 0
        html = VIDEO_EXISTING.sub(replacer, html)

    with open(filepath, "w") as f:
        f.write(html)

    return replaced[0]

def main():
    base_url = None
    if "--base-url" in sys.argv:
        idx = sys.argv.index("--base-url")
        if idx + 1 < len(sys.argv):
            base_url = sys.argv[idx + 1]

    print("Embedding videos into module pages...\n")

    if not base_url:
        print("Step 1: Creating symlink for local serving")
        create_symlink()
    else:
        print(f"Step 1: Using CDN base URL: {base_url}")

    print("\nStep 2: Patching module HTML files")
    total = 0
    for mod_num in sorted(CLIP_FILES.keys()):
        count = patch_module(mod_num, base_url)
        total += count
        status = f"  ✓ Module {mod_num}: {count} clips embedded"
        if count == 0:
            status = f"  – Module {mod_num}: no placeholders found (already embedded?)"
        print(status)

    print(f"\nDone. {total} video tags embedded across {len(CLIP_FILES)} modules.")
    if not base_url:
        print("\nTo preview locally:")
        print(f"  cd {SCRIPT_DIR}")
        print("  python3 -m http.server 8080")
        print("  open http://localhost:8080/modules/01.html")

if __name__ == "__main__":
    main()
