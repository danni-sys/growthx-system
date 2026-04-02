# The GrowthX System

A free, gated lead magnet that teaches the mental models, frameworks, and first principles behind how GrowthX approaches AI-led growth — the same thinking applied to 60+ companies including Webflow, Ramp, and Lovable.

**Live site:** [williamproctor.github.io/growthx-system](https://williamproctor.github.io/growthx-system/)

## What this is

This is the complete prototype for an 8-module masterclass that GrowthX gives away in exchange for some information. It's not a course — it's a system. It teaches operators *how to think* about AI-led growth so they can leverage any tool to drive results.

The goal: generate qualified inbound leads for GrowthX by leading with extreme value.

## What's inside

| Page | Description |
|------|-------------|
| **[Landing Page](https://williamproctor.github.io/growthx-system/system/index.html)** | The public-facing lead capture page. Hero, social proof, 8-module overview, qualification section, and gated email form. |
| **[Content Inventory](https://williamproctor.github.io/growthx-system/inventory/index.html)** | Internal working tool. Maps each module against 105 vault assets. Includes source lists, gap analysis, and a clip map with 25 scored video sections ready for extraction. |
| **[Hub](https://williamproctor.github.io/growthx-system/)** | Project dashboard linking everything together. |

## The 8 modules

1. **The 15-Minute System Overview** — How GrowthX thinks about AI-led growth, in one watch
2. **AI Visibility Playbook** — What we learned from 1.1M observations across ChatGPT, Perplexity, Gemini & Google AI
3. **Content Strategy Framework** — Audience-first approach: knowledge graphs, topic mapping, context over prompts
4. **Content Quality System** — The quality principles AI rewards — editorial rigor, trust signals, the citation bar
5. **AEO Masterclass** — Answer Engine Optimization from first principles
6. **Starter Prompts & Artifacts** — The Shaping Loop, context artifacts, and prompt patterns that work
7. **Measurement & Monitoring** — PRAI framework, leading indicators, composite scoring
8. **Self-Assessments** — 39 scenario-based questions that test principles, not trivia

## What we're building toward

- [ ] Marcel records the 15-minute System Overview (Module 01 — the hook video)
- [ ] Cut 25 video clips from 11 source videos using the clip map scores and timestamps
- [ ] Package self-assessments as an interactive quiz component
- [ ] Wire the email form to a real backend (HubSpot, ConvertKit, or similar)
- [ ] Final copy review with Marcel and Danny
- [ ] Ship to production at a GrowthX-owned domain

## Tech

Static HTML/CSS/JS. No build step, no dependencies, no framework. Deploys automatically via GitHub Pages on push to `main`.

- **Design system:** `shared.css` — GrowthX brand palette (Burrito Beige, Metal Black, Karl the Fog), Inter typeface
- **Dark mode:** Toggle in the nav, persists via `localStorage`
- **Editing:** See [EDITING-GUIDE.md](EDITING-GUIDE.md) for how to change copy directly on GitHub
