# GrowthX System — UX Review & Open Questions
**Prepared by:** Danni  
**Date:** April 3, 2026  
**For:** Will (pull request review)

---

## Context

The goal of this system is to create one URL we can point everyone to — post-event attendees, potential clients, LinkedIn cold traffic, sales follow-up. The experience needs to work for all three, even though they arrive with very different levels of context.

The core intent: lead with so much value that people either want to support GrowthX, realize they need help and want to outsource to GrowthX, or trust GrowthX enough to bring them in for their company.

---

## Priority Changes

### 1. Add a Diagnostic Assessment at the Start (Before the Modules)

**The problem:** Right now the modules page says "Start anywhere" — which sounds generous but is actually paralyzing, especially for someone who just came from a LinkedIn ad with zero context. ~10.5 hours of potential content with no guided path is a lot to drop in front of a stranger.

**The proposal:** Two assessments, not one.

**Assessment A — "Find your starting point" (new, at the beginning)**
- 5–7 quick diagnostic questions
- Always routes everyone through Module 01 (the 15-min overview — "if you watch nothing else, watch this")
- Then gives personalized "go here next" based on their answers
- Tone: feels like a favour, not a test. "Before you dive in, let's figure out where you are."
- Output: shows them their gap so they feel the pain point before they start

**Assessment B — "Test your thinking" (existing 39 questions, stays at the end)**
- Keeps its current position as a comprehension check after going through the modules
- Now makes more sense sequentially: learn → test → see where you still have gaps

**Open question for Will:** Should Assessment A be *before* or *after* the gate? Putting it before the form lets people taste something before handing over their email, which might increase conversion. Putting it after keeps everything gated.

---

### 2. Cut the Gate Form from 5 Fields to 3

**Current fields:** First name, Work email, Company name, Role/Title, Company size

**Recommended:** Keep First name, Work email, Company name only.

**Cut Role/Title** — Can be inferred or enriched via Apollo/HubSpot after submission. Asking it upfront makes the form feel like a sales qualification screen.

**Cut Company size** — Can be looked up automatically via enrichment. Doesn't need to come from the user.

**The principle:** The gate should feel like an exchange of value, not an intake form. Three fields gets the information we actually need at this stage. The rest can be collected later, once they've experienced the content and trust is established.

---

### 3. Clean Up the Navigation for External Users

**The problem:** The global nav exposes "Hub" and "Inventory" to anyone who gets past the gate. Both are internal project tools — not user-facing content. Someone who just unlocked the system and starts exploring will hit dead ends or confusing internal pages.

**Recommended nav for external users (post-gate):**
- Modules
- Self-Assessments
- (Maybe) a "Book a call" or "Talk to us" link

**Hub and Inventory should only be visible internally** — either removed from the nav or conditionally shown.

---

### 4. The "Who Walks Through the Door" Problem

We're designing one URL for three different audiences:
- **Post-event attendees** — already warm, know GrowthX, want to go deeper
- **Potential clients** — moderate awareness, evaluating whether to engage
- **Cold LinkedIn/ad traffic** — zero context, just landed

We don't have a clear answer yet on whether to design for one primary audience or all three. Worth discussing. If it's cold traffic, the gate needs to come later and the value needs to come earlier. If it's post-event, the current approach probably works fine.

---

## Questions Still Open

1. **Does the diagnostic assessment gate or ungated?** (Before or after the form?)
2. **What does success look like for cold traffic?** Do they read one module? Do they book a call? Do they just opt in and enter a nurture sequence?
3. **Who maintains this long-term?** The HANDOFF.md notes several things still in progress (Module 01 hook video, CRM integration, Marcel's Notion prompt doc). What's the MVP we're shipping vs. what's phase 2?
4. **Should there be a "recommended path" for first-timers** vs. "browse freely" for returners? Right now it's one experience for everyone.

---

## What's Working Well (Keep As-Is)

- The design and visual system are clean — brand is consistent, Inter typeface, gold accents are cohesive
- The landing page copy is strong — the "without a system / what this teaches" split and the qualification checklist are doing good work
- The module structure (7 modules, each standing alone, with time estimates) is well thought out
- Dark/light mode toggle is a nice touch
- The progress bar on the assessments page is a good UX detail

---

## Copy Changes Made (Danni's Fork)

All changes are in `danni-sys/growthx-system` — open a PR to `williamproctor/growthx-system` to merge.

- **H1:** "How the team behind 4 unicorns thinks about AI-led growth."
- **Hero subhead:** "Not a course. Not a playbook. A system of thinking. The same one companies pay $10K–$60K/month to access."
- **"Why This Exists" H2:** "Tools change every quarter. Principles don't."
- **"Why This Exists" paragraph:** Rewritten around the principles-outlast-tools idea — grounded in 4 unicorns and a decade of work
- **Philosophy cards:** Replaced "Not a course / Not a playbook / Not theory" with three affirmative principles: Workflow before technology / Audience before algorithm / Systems, not sprints
- **Em dashes:** Removed from all visible copy (were flagged as AI tells)

---

## V1 Diagnostic Quiz Built

**File:** `quiz/index.html`

**What it does:** 5 questions that identify the user's primary gap and output a personalized 4-module starting path. Module 01 is always first. Routes to different module sequences based on whether their gap is visibility, content quality, strategy, or measurement.

**Where it should live — decision needed:**

- **Option A (before the gate):** Embed on the landing page before the form. User answers 5 questions, sees their gap, then fills out the form to unlock the full system. Higher investment before the gate = higher conversion. Recommended for cold traffic.
- **Option B (after the gate):** Redirect here immediately after form submission. The quiz becomes the first thing you see after unlocking. Simpler to implement. Good for post-event and warm audiences who don't need convincing.

For V1: Option B is faster to ship. Option A is the better long-term experience.

---

## Open Questions for Will + Marcel

**Copy:**
- [ ] Confirm: is "4 unicorns" the right claim, or should it be "the team behind HashiCorp, Scale AI, Deepgram, and ServiceTitan"? Named companies are more specific but may feel dated to some audiences.
- [ ] The two testimonials both end with "it changed how I see everything" — one should be replaced with something that covers a different angle (a specific result, a before/after, or a team application story). Can Marcel pull a better quote?
- [ ] The Marcel section headline ("Built by Marcel Santilli & the GrowthX team") is flat. Flag for V2.
- [ ] "How we think about growth in the age of AI" (What's Inside section) is generic — flag for V2.

**UX / functionality:**
- [ ] Cut the gate form from 5 fields to 3 (keep: first name, work email, company — cut: role, company size)
- [ ] **Nav exposes internal tools to external users** — the global nav currently shows "Hub" and "Inventory" to anyone who gets past the gate. Both are internal project tools. Post-gate nav should only show: Modules, Self-Assessments, and optionally a "Talk to us" CTA. Hub and Inventory should be removed or hidden from external-facing pages.
- [ ] **Quiz is built but not linked anywhere** — `quiz/index.html` exists and is fully functional. It needs to be connected to the user journey. Two options: (A) redirect here immediately after form submission as the first post-gate experience, or (B) embed it on the landing page before the form as a conversion mechanic. Recommend Option A for V1 — easiest to ship, Will just needs to update the form success state to redirect to `../quiz/index.html`.
- [ ] Decide: quiz before or after the gate?
- [ ] Wire the form to HubSpot or a webhook — currently logs to console only. Hard blocker before going live to real traffic.
- [ ] Module 01 gap: Marcel still needs to record the dedicated 15-min system overview

**Content:**
- [ ] The two duplicate testimonials — replace one
- [ ] Confirm exits claim before using it anywhere (DataGrid $200M, Prompt.fu/OpenAI are client exits, not Marcel's unicorn companies — different proof point)

---

## Feature Suggestion: Ask a Question (per module)

**What it is:** A short form at the bottom of each module page (after the assessment CTA) where users can submit a question to Marcel and the GrowthX team.

**Why it matters:**
- Every question is a content signal — what people are confused about after consuming a module
- Every submission is a qualified lead (they're already gated, re-asking email ties the question to a person)
- Questions can seed Circle posts, newsletter issues, or future module updates
- Makes Marcel feel accessible, which builds trust

**Recommended copy:**

> **Ask a question**
> Something didn't click, or curious how this applies to your situation? Ask Marcel and the team.

Fields: Name, Email, Your question
Button: "Send your question →"

**Recommended tool:** Tally.so (free) with their native Notion integration. Each submission creates a row in a Notion database with: Module, Name, Email, Question, Date, Status (New / Answered / Turned into content). Will needs to set up the Tally account and connect it to a Notion database. Takes about 30 minutes end-to-end.

**Where it lives:** Bottom of each module page (01–07), after the assessment CTA and before the resources section.

---

## Suggested Next Steps

- [ ] Will reviews this doc and Danni's fork
- [ ] Merge copy changes via PR
- [ ] Decide quiz placement (before or after gate)
- [ ] Cut form to 3 fields
- [ ] Fix nav for external users
- [ ] Wire form to CRM
- [ ] Marcel records Module 01 overview
- [ ] Will sets up Tally → Notion for the per-module question form
