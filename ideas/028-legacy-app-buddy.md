---
id: "028"
slug: legacy-app-buddy
name: Legacy App Buddy
one_liner: "A hotkey voice overlay that shows staff how to do tasks in old desktop business software and replays approved steps."
target_user: "Staff and ops managers at 10-200 person firms running legacy ERP, AS/400 or FoxPro-era desktop software"
form_factor: "desktop app"
lens: "Interaction shift"
frontier: false
competition: "WEAK DIRECT"
confidence: "LOW"
status: "developed"
signals: [HN-33, HN-34, LAND-04, RED-23]
scores:
  pain: 3
  evidence: 2
  ai_leverage: 4
  whitespace: 2
  novelty: 2
  why_now: 4
  solo_feasibility: 3
  distribution: 2
  wtp_economics: 2
  scale_defensibility: 2
total: 51.6
price_hypothesis: "$39 per seat per month, 5-seat minimum, one app playbook included"
model_cost_per_user_month: "$0.3 to $1"
gross_margin: "about 95% before support"
mvp_weeks: 8
deep_dive: false
red_team: false
---

# Legacy App Buddy

## 1. One-liner
A hotkey voice overlay that shows staff how to do tasks in old desktop business software and replays approved steps.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Daily friction and onboarding cost where knowledge lives "in someone's head", but no one quantifies it and firms live with it. |
| Evidence quality | 2 | 2 | Four signals, all indirect: a vendor-side comment, a family-business anecdote, a developer's alt-tab complaint, a new-hire training question. No one asks for this product. |
| AI leverage | 2 | 4 | Screen understanding, voice Q&A and adaptive replay are the product; human approval stays in the loop, so not a 5. |
| Whitespace | 2 | 2 | Five YC-listed no-API automation startups, an indie record-once tool on Product Hunt, and WalkMe and Whatfix on the guidance side. |
| Novelty of insight | 1 | 2 | The HeyClicky pattern pointed at old software is an obvious step; the playbook library is the twist. |
| Why now | 1 | 4 | Cheap screen understanding (about $0.0003 to $0.01 a screenshot) and hotkey voice agents only matured in 2026. |
| Solo feasibility | 2 | 3 | A guidance-only overlay is 8 weeks; reliable macros in old UIs (terminals, Win32 forms) and per-app playbooks are the hard parts. |
| Distribution | 2 | 2 | No store or marketplace; users are scattered small firms; consultants who maintain legacy apps are the only plausible channel. |
| Willingness to pay and unit economics | 2 | 2 | Margin is high, but nothing in the evidence states a price, and the nearest paid anchors are enterprise ($23K to $39K a year). |
| Scale and defensibility | 2 | 2 | Screen-aware assistants from Microsoft and Google cap it at 2; per-app playbooks are a real but small moat. |
| **Total** | | **51.6** | |

Confidence: LOW (the key belief, that free assistants cannot handle legacy screens, is untested). FRONTIER: no.

## 3. The problem
- Who: office and operations staff at small manufacturers, distributors and services firms whose core system is a 10 to 30 year old desktop or terminal application, plus the one person who knows it.
- Cost: execs "hate their legacy systems but can't really do anything about it" and want AI wrapped around the core system (HN-33); fixing a dead-vendor app needed a hex editor (HN-34); new hires ask "whoever is around" because the process knowledge is in heads (RED-23); people alt-tab between work apps and chat to copy context (LAND-04).
- Workarounds: a binder or wiki of screenshots, tribal knowledge, a consultant on call, RPA scripts that break when a screen changes, or doing it all by hand.
- Gap: a helper that sits next to the old app, understands its screens as pixels, and walks a person through a task.

## 4. Evidence
- **HN-33** (medium, 2026-05-26, HN, Launch HN: Minicor): "I've found that legacy system users (or at least the execs) are pretty excited about AI because they hate their legacy systems but can't really do anything about it (ERP changes are an extreme nightmare, and often no better system exists with all the capability they need). They want to wrap it in AI to automate stuff without changing out the core system." https://news.ycombinator.com/item?id=48284582 The commenter works with legacy-ERP manufacturers (vendor-side view).
- **RED-23** (medium, 2026-09-19, r/smallbusiness, 29 comments): "How do you handle training new hires when so much knowledge is just "in someone's head"?" (post title) https://www.reddit.com/r/smallbusiness/comments/1wktryv/
- **HN-34** (weak, 2025-11-05, Ask HN): "It's a foxpro application rewritten in '89 from an original dBase port from earlier in the 80s. I legit had to bust out radare2 and hexdump(analysis)/hex fiend(editing) in order to get the changes done because the original programmer passed away (RIP)." https://news.ycombinator.com/item?id=45824909
- **LAND-04** (medium, 2026-07-12, HN, maker of the Wisp overlay): "I built Wisp because I kept alt-tabbing between my editor/browser/docs and chat apps, copying context over, waiting for an answer, then copying the result back." https://news.ycombinator.com/item?id=48882687 A general overlay signal, not about legacy apps.
- Gap in the evidence: no one in these signals asks for a screen guide for an old app or states a price. The demand is inferred.
- New evidence (not in SIGNALS.md), supply-side: a YC-backed company, Pig, was reported to have "gave up and pivoted" from AI agents for Windows (TechCrunch headline, 2025-07-18), a caution on how hard reliable Windows automation is. https://techcrunch.com/2025/07/18/why-a-y-combinator-startup-tackling-ai-agents-for-windows-gave-up-and-pivoted (title only)

## 5. The product
- What it does: the user presses a hotkey inside the legacy app and says or types "how do I enter a credit memo?" The overlay captures that window only while the key is held, answers in one short step at a time, and points at the field or button. A manager records a task once (screen plus voice narration); the overlay turns it into a playbook for that app and version. For repeat tasks it can fill fields from a record the user selects, pausing for a confirmation tap before each save.
- Core AI loop: hotkey + question + window screenshot + app playbook -> model identifies the screen and next step -> spoken instruction plus a pointer highlight -> user acts -> next screenshot -> next step; recorded walkthrough -> model drafts a playbook (steps, fields, validations) -> manager edits.
- Interaction model: Windows tray app; hold-to-talk; capture only while held; no always-on recording; admin console for playbooks.
- Form factor: desktop app (Windows first; terminal emulators and Citrix windows are in scope because it reads pixels).
- Day in the life: a new order clerk at a 40-person distributor asks "customer wants net 45 on this order". The overlay says "Press F4 for terms", points at the terms field, and notes "Orders over $10,000 need a manager code in the next screen, as Dana recorded in March." Dana, the one expert, stops being the help desk.
- Safety lines: macros only with a confirmation before each save; no unattended runs in the MVP; screenshots processed under a no-retention setting; a per-app allow list.

## 6. Why the LLM is load-bearing
- Old UIs have no accessibility tree or API for many terminals and Win32 forms, so understanding a screen means reading pixels and text, which vision models now do for fractions of a cent.
- Turning a narrated recording into a readable playbook, and answering "how do I" in the user's words, is language work. Remove the model and you are left with a macro recorder, which exists.

## 7. The insight
- The generic hotkey assistant is now a lab feature, but a per-app, per-version playbook (what this firm's order screen means, which fields matter, what the manager recorded) turns a generic screen reader into something that onboards people. Honest caution: the concept note assumed legacy software is invisible to OS assistants; screen-aware assistants read pixels, so that belief needs a direct test (section 17).

## 8. Why now, and why this does not exist yet
- Why now: screenshot understanding costs about $0.0003 to $0.01 and hotkey voice agents (HeyClicky, YC Spring 2026) showed the pattern (`research/LANDSCAPE.md` sections 3 and 8).
- Why it partly exists: no-API automation startups (section 10) sell to developers and integrators, and digital adoption platforms sell to enterprises. A $39-a-seat guide for the clerk of a 40-person firm was not found, but that may be because buyers at that size do not buy software of this kind.

## 9. Inspiration and derivation
- Parents: HeyClicky and Clicky (hotkey, screen-aware, pointing), WalkMe and Whatfix (guided overlays on desktop apps), Minicor and Cyberdesk (self-healing automation of Windows apps).
- Changed: target user (the end clerk and small-firm ops manager, not developers or enterprise IT), core job (teach and guide first, automate second), business model (per-seat SMB pricing), channel (consultants who maintain the legacy app). Four of five changed.

## 10. Competition check
Queries run:
1. WebSearch: "AI assistant for legacy desktop software no API screen understanding guide users ERP green screen terminal AI copilot overlay Windows"
2. WebSearch (Product Hunt): "site:producthunt.com automate legacy desktop applications no API AI agent Windows ERP screen record once replay"
3. WebSearch (YC directory): "site:ycombinator.com/companies Windows desktop automation legacy software no API computer use agent manufacturing ERP"
4. WebSearch (digital adoption and RPA stores): "WalkMe OR Whatfix OR Pendo desktop application guidance legacy apps AI 2026 OR "Power Automate Desktop" OR UiPath Screen Agent legacy Windows apps small business pricing"
5. HN API: thread of Launch HN Minicor (item 48284582).

| Product | What it does | Price | How it differs |
|---|---|---|---|
| [Minicor](https://ycombinator.com/companies/minicor) (YC) | Managed, self-healing desktop automation for Windows apps with no APIs (EHRs, ERPs); built through a coding agent via MCP; exposes an API endpoint to trigger it | not stated | Sells automation as an API to builders, not guidance to staff |
| [Cyberdesk](https://www.ycombinator.com/companies/cyberdesk) (YC S25; [Launch HN](https://hn.svelte.dev/item/44901528)) | Computer-use agent for developers; follows memorized steps and falls back to a computer-use model on popups | not listed | Developer API for legacy Windows apps |
| [Pig](https://www.ycombinator.com/companies/pig), [Coasty](https://www.ycombinator.com/launches/RM5-coasty-the-computer-use-agent-that-doesn-t-break-on-real-software), [Zatanna](https://ycombinator.com/companies/zatanna), Nen (not YC) | Windows or ERP automation agents; Pig reportedly pivoted away ([TechCrunch](https://techcrunch.com/2025/07/18/why-a-y-combinator-startup-tackling-ai-agents-for-windows-gave-up-and-pivoted)) | n/a | A crowded YC cluster on the automation half |
| [DeskStride](https://www.producthunt.com/products/deskstride) (Product Hunt) | Windows and macOS app: record a task once, edit on a canvas, schedule or trigger; local-first, no code; finds elements by image or text | not stated | Closest small rival for the record-once half; no voice guidance |
| [WalkMe](https://www.walkme.com/walkme-desktop/) Workstation, [Whatfix](https://www.tfir.io/whatfix-for-desktop-and-mobile-applications-to-improve-employee-productivity/) | Guidance overlays for desktop and legacy apps | WalkMe median about $39,000 a year per a [competitor blog](https://trupeer.ai/blog/walkme-alternatives-honest-comparison) that cites an unverified Forrester report; Whatfix about $23K baseline per a [comparison post](https://www.glitter.io/blog/employee-training/best-whatfix-alternatives) quoting a critic [UNVERIFIED] | Enterprise-priced and implementation-heavy; the guidance half |
| Microsoft [Copilot Studio Computer Use](https://www.candede.com/articles/automating-legacy-systems-computer-use), [Amazon WorkSpaces AI agents](https://www.mindstudio.ai/blog/aws-workspaces-ai-agents-legacy-desktop-software) (preview May 2026), [Kognitos](https://www.kognitos.com/blog/ai-in-legacy-systems/), [Zoho RPA](https://www.zoho.com/rpa/windows-automation-software.html), ServiceNow AI Desktop Actions | Platform and RPA vendors drive Windows desktop apps through the UI | credits or enterprise | The platform risk for the macro half |
| Copilot Vision, Gemini Live and Magic Pointer (`research/LANDSCAPE.md` section 4) | Screen-aware voice help in any app, free or bundled | free to bundled | The platform risk for the guidance half |

Classification: **WEAK DIRECT**. For the exact job (a staff-facing, hotkey, voice guide plus approved replay for old desktop apps at small-firm prices) no direct product was found, but the automation half is crowded (five YC-listed companies, an indie tool, RPA vendors) and the guidance half is covered by enterprise vendors and by free screen-aware assistants.

Platform risk: high. Copilot Vision, Gemini Live with screen share and Copilot Studio Computer Use can already read and drive Windows apps; Microsoft owns the OS layer. The landscape lists generic screen overlays as a red zone. This caps Scale and defensibility at 2 and Whitespace at 3.

## 11. Business model
- Payer: the firm (ops manager or owner). Price: $39 per seat per month, 5-seat minimum, one app playbook included; $15 for read-only guidance seats. Anchors: HeyClicky $20 Pro and $100 Max; WalkMe and Whatfix at $23K to $39K a year [UNVERIFIED].
- Model cost per seat per month [ESTIMATE]: 60 guided questions, each 2,500 tokens in (screenshot plus cached playbook) and 200 to 300 out. 80% on Haiku 5.5 at 2,500 x $0.10/1M + 200 x $0.50/1M = $0.00035; 20% on Sonnet 5.5 at 2,500 x $2/1M + 300 x $10/1M = $0.008. Blended 60 x (0.8 x $0.00035 + 0.2 x $0.008) = 60 x $0.00188 = $0.11. Macros: 10 runs x 15 step checks x $0.00035 = $0.05. Speech: 20 minutes STT at $0.003 = $0.06 and 10 minutes TTS at $0.009 = $0.09. Total about $0.31, say $0.3 to $1 with margin for retries and long screens. Playbook drafting from a recorded walkthrough is a one-off of well under $1 per app.
- Gross margin [ESTIMATE]: ($39 - $0.31 - $1.43 Stripe) / $39 = 95% before support; onboarding and playbook support will dominate, so plan for 70% to 80% in year one.

## 12. Market size
- Buyers [ESTIMATE]: assume 1.0M US firms with 10 to 200 employees [ASSUMPTION; count not verified], of which 5% run a business-critical legacy desktop or terminal system = 50,000, averaging 8 seats.
- Revenue: 50,000 x 8 x $39 x 12 = $187M a year if all bought. At 3% penetration (1,500 firms) = 1,500 x 8 x $468 = $5.6M ARR.
- Reading: a decent niche, but entry depends on a channel that does not exist yet.

## 13. Go-to-market
- First 100: (1) consultants and VARs who maintain old ERPs (Sage, Epicor, Infor, AS/400 shops) as resellers of "ask the app" seats for their clients; recruit through LinkedIn and ERP user groups, about 20 firms via 10 partners; (2) Ask HN and Show HN threads like HN-34 where owners of old systems talk, about 20; (3) r/sysadmin, r/ERP and r/smallbusiness posts on onboarding new hires into old systems, with a free playbook generator for one task, about 30; (4) SEO on "train new employees on old ERP" and "AS/400 green screen cheat sheet", about 30.
- Growth loop: a playbook built for one app version is the starting point for the next firm on the same version (with the original owner's consent), and the consultant who sees it work installs it for every client.

## 14. Moat and scale path
- Moat: a library of per-app, per-version playbooks and screen maps; recorded firm-specific rules; consultant relationships. Smaller than a platform moat.
- Scale path: more app families, then unattended workflows with audit logs, then a developer API (closer to Minicor).

## 15. Solo feasibility
- MVP (8 weeks): Windows tray app with hold-to-talk, single-window capture, model call with a playbook, spoken step plus pointer overlay, playbook recorder, and confirmation-gated field fill. No unattended runs, no on-prem model.
- Running cost before revenue: about $50 to $120 a month (code signing, hosting, pilot usage under $5).
- Hardest risk: reliability of pointing and field fill in terminal and Win32 UIs, and customer trust with screens that hold payroll and customer data.

## 16. Pre-mortem
1. Copilot Vision or Gemini Live already guide users well enough on old screens, so firms see no reason to pay.
2. A wrong auto-fill posts bad data; one incident ends the pilot, and small firms cannot absorb support costs.
3. Firms with legacy systems buy through consultants and move slowly; the channel never forms.

## 17. Cheapest validation test
- What: first, run 5 legacy screens (a terminal ERP, a FoxPro-style app, an old Win32 order form) through Copilot Vision and Gemini Live and score their step guidance. Then run a Wizard-of-Oz session with 8 legacy-app users found via consultants and HN-style threads: a hotkey prototype using a vision model and a hand-written playbook.
- Cost: about $50. Duration: 3 weeks.
- Pass: free assistants complete under 40% of tasks, the prototype completes at least 70%, and at least 3 of 8 firms agree to pay $39 per seat for 5 seats. Fail: free assistants complete 60% or more, or fewer than 2 firms would pay.

## 18. Open questions
- Is the "legacy apps are invisible to OS assistants" belief true? The test above decides it; if false, kill.
- Which single app family first (for example QuickBooks Desktop, Sage 50 or 100, Epicor, an AS/400 package)? Pick by the size of its user group.
- Who buys: the ops manager, the consultant or the owner?
- How should screen privacy be handled for payroll and customer data (local blur, no retention)?
- Is the guidance product better as a feature for consultants than as a standalone company?
