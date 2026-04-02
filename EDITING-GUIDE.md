# Editing Guide

This repo contains the GrowthX System lead magnet — the landing page, content inventory, and supporting pages. Everything is static HTML/CSS/JS with no build step.

## How to edit copy

1. Go to the file on GitHub (links below)
2. Click the **pencil icon** (top-right of the file view) to open the editor
3. Make your changes to the text between HTML tags
4. Scroll down, add a short description of what you changed, and click **Commit changes**
5. Wait ~30 seconds for GitHub Pages to rebuild, then refresh the live URL

## File map

| What | File | What to edit |
|------|------|-------------|
| **Landing page** | `system/index.html` | Hero headline, subhead, module names/descriptions, stats, qualify lists, form labels, CTA text |
| **Content inventory** | `inventory/index.html` | Module assessments, source lists, clip map notes, action items |
| **Hub page** | `index.html` | Card titles, descriptions, status tags |

## Quick tips for editing HTML

- Text lives between tags like `<h1>text here</h1>` or `<p>text here</p>`
- Don't delete the tags themselves — just change the words between them
- `&amp;` means `&` — use `&amp;` if you need an ampersand
- If something breaks, check the commit history and revert

## Preview locally

Download/clone the repo and open any `.html` file directly in your browser. The dark mode toggle, navigation, and all styling work locally — no server needed.

## Live URL

Once GitHub Pages is enabled: `https://williamproctor.github.io/growthx-system/`

## Structure

```
index.html          ← Hub / project dashboard
shared.css          ← Design system (don't edit unless changing brand)
theme.js            ← Dark mode toggle (don't edit)
assets/             ← Logo SVG
system/index.html   ← Landing page
inventory/index.html ← Content inventory & clip map
```
