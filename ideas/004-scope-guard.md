---
id: "004"
slug: scope-guard
name: Scope Guard
one_liner: "Turns client texts and site voice notes into priced change orders signed before the extra work starts."
target_user: "Small remodelers and trade contractors who work from signed estimates"
form_factor: "other"
lens: "Pain-first"
frontier: false
competition: "CROWDED"
confidence: "LOW"
status: "developed"
signals: [PRO-009, PRO-006, RED-39, PRO-031, PRO-010]
scores:
  pain: 3
  evidence: 2
  ai_leverage: 4
  whitespace: 2
  novelty: 3
  why_now: 3
  solo_feasibility: 3
  distribution: 3
  wtp_economics: 3
  scale_defensibility: 2
total: 55.8
price_hypothesis: "$39/month per contractor"
model_cost_per_user_month: "$2.00"
gross_margin: "95%"
mvp_weeks: 6
deep_dive: false
red_team: false
---

# Scope Guard

## 1. One-liner
Turns client texts and site voice notes into priced change orders signed before the extra work starts.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Given-away extras are a real margin leak, but the file has one direct signal (PRO-009) and no measured dollar loss. |
| Evidence quality | 2 | 2 | One medium signal on scope disputes; the rest are generic admin pain or tangential. New Reddit posts help but are not in the signal base. |
| AI leverage | 2 | 4 | Reading a messy thread against a signed scope and pricing the difference needs the model. |
| Whitespace | 2 | 2 | Handoff, Houzz Pro, JobTread, Foreman and several small tools already draft AI change orders; only passive thread capture is unserved and it is hard. |
| Novelty of insight | 1 | 3 | Capturing the change at the moment of the request is a useful twist, though others start from voice or text commands. |
| Why now | 1 | 3 | Models read threads and price from rate books cheaply, but this was possible in 2024. |
| Solo feasibility | 2 | 3 | About 6 weeks, with one hard risk: contractors' own SMS and WhatsApp cannot be read, so capture needs a job line. |
| Distribution | 2 | 3 | Contractor subreddits, Facebook groups and a GC-to-sub invite loop; every competitor also targets these. |
| Willingness to pay and unit economics | 2 | 3 | Contractors pay $39-150 a month for software (PRO-010) and margin is high, but incumbents bundle change orders. |
| Scale and defensibility | 2 | 2 | A feature inside project-management suites; a rate-book and ledger give light lock-in. |
| **Total** | | **55.8** | |

Confidence: LOW (key assumption untested). FRONTIER: no. **Recommendation: CROWDED; see section 18.**

## 3. The problem
- Who: small remodelers and trade contractors who sign a scoped estimate. Clients ask for extras on site, treat them as part of the job, and bristle when a change order appears (PRO-009).
- Cost [ESTIMATE]: two unbilled extras a month at $300 each [ASSUMPTION] is $600 a month, $7,200 a year, per contractor. The signal says "each one sounds small but the labor and materials add up fast".
- Frequency and workaround: every job. Today: a verbal yes, a text, a note, or "add it to the invoice later"; change orders are written at night (PRO-006, RED-39) or not at all. Homeowners distrust change orders too: a 2026 renovator noted that low bids leave out items that "hit me as change orders later" (new evidence below).

## 4. Evidence
- PRO-009 (medium, r/Contractor, 2026-07-09): "Each one sounds small but the labor and materials add up fast. When I brought up a change order they got defensive and said they figured it was all part of the job."
- PRO-006 (strong, r/Contractor, 2026-10-29): "I usually spend most of my day onsite then go home to spend more time on the computer doing admin task. I want to cut back on time spent doing much of these admin tasks."
- RED-39 (weak, HN, 2026-03-27, second-hand builder pitch): "My buddy runs a general contracting business. He's good at what he does, but he spends a lot of evenings on a laptop chasing invoices and scheduling follow-ups instead of hanging outwith his family and friends."
- PRO-031 (medium, LawnSite, 2026-10): a 5-truck landscaper needs contract language for price changes between quote and work; tangential, shows that post-signature price changes lack a standard mechanism.
- PRO-010 (medium, HN, 2026-03-06): a solo carpenter pays $39 to $150 a month for software built for 20-person firms (price anchor, no quote needed).
- New evidence (not in SIGNALS.md): r/Contractor, 2026-10-22, https://www.reddit.com/r/Contractor/comments/1xcsgau/ (51 comments): "I warned him the new windows might not fit the shutters and additional casing, if needed, would be a change order. He agreed, but now expects the casing for free."
- New evidence (not in SIGNALS.md): r/Contractor, 2026-10-17, https://www.reddit.com/r/Contractor/comments/1x8hhqu/ (44 comments, may be a marketing post): "We give two options with a price on each (fix it now, or button it up and quote it separately), and get the yes in a text so there's a record."
- New evidence (not in SIGNALS.md): Hacker News, 2026-01-12, https://news.ycombinator.com/item?id=46592657 (a homeowner's Show HN): "I realized that the "cheapest" quote was actually just leaving out expensive items (like debris removal and permits) that would have hit me as change orders later."

## 5. The product
- Outcome: when a client asks for something outside the signed estimate, the contractor gets a private nudge with a priced draft; one tap sends the client a link to sign before work starts. An extras ledger flows into the final invoice.
- Core AI loop: input (the signed estimate parsed into scope, exclusions and allowances; messages to a job line, forwarded screenshots, voice memos from the app) -> model work (decide whether a message is a scope change, which line it touches, price it from the contractor's labor rate, markup and material list, draft the change-order wording) -> output (nudge to the contractor; after approval an SMS link to a one-page change order with typed-name signature, timestamp, IP log and optional deposit) -> feedback (edits update the rate book and the "do not flag" rules).
- Interaction: each job gets a text number the contractor shares with the client ("text the job line"); the contractor reviews nudges by SMS or web. Not feasible [ASSUMPTION, platform policies not re-checked today]: silently reading a contractor's personal iMessage, SMS or WhatsApp on iOS.
- Form factor: SMS job line plus web app.
- Day in the life: Dana, a remodeler, has a $38,000 kitchen job. The client texts the job line: "can you also move the outlet by the window and add two more?" Scope Guard replies privately: "Not in the estimate. 3 outlets, 4 hours at $85 plus $60 materials with 20% markup = $495. Send?" Dana taps yes; the client signs on her phone within the hour and work proceeds.

## 6. Why the LLM is load-bearing
Clients write "while you're here, can you also..." in free text, photos and voice memos; the model must tell an extra from a clarification, map it to the estimate, and price it in the contractor's own terms. Without it you have a change-order form, which every project-management product already has. The value sits in detection and instant drafting, not in the form.

## 7. The insight
The change order dies at the moment of the request, because writing it later feels like an accusation. Capture it in the thread where the request happened, price it in under a minute, and the sign-off becomes routine instead of a confrontation. Honest note: Houzz Pro and Handoff already shorten drafting with voice or text commands; the claim that passive detection changes behavior more than a fast form is untested.

## 8. Why now, and why this does not exist yet
It does exist in parts, and nothing new was needed to build it. Models reading threads and rate books is a 2024 capability. Incumbents are shipping AI inside their suites in 2025-26 (Handoff raised $5.8M in June 2025; JobTread launched an AI connector on 2026-04-13; Houzz Pro advertises AI change orders). The unserved slice is detection from client messages for contractors who use no suite, and platform access makes that slice hard.

## 9. Inspiration and derivation
- Parents: Houzz Pro AI change orders, Handoff, ChangeVerdict (email versus contract baseline), the manual "get the yes in a text" habit.
- Changed: interaction model (the job line captures the request instead of a form the contractor opens), target user (shops with no project-management suite), business model (flat $39, not a suite upgrade), channel (contractor communities, GC-to-sub invites).

## 10. Competition check
- Queries run: (1) "AI change order generator contractors detect scope creep from text messages price extra work client signature remodeling"; (2) "site:producthunt.com change orders contractors AI scope change texts"; (3) "site:ycombinator.com/companies residential contractors remodeling construction change orders estimates AI"; (4) "Buildertrend JobTread AI features change orders 2026 AI assistant home builders remodelers". Also: Handoff change-order page read, news search on Handoff funding, Reddit archive pull (r/Contractor, r/Construction, r/Carpentry, 2026-08 to 2026-10), HN search. The App Store lookup script returned HTTP 403.
- [Handoff](https://www.handoff.ai/change-orders) (YC W20, [YC launch](https://www.ycombinator.com/launches/ORi-handoff-ai-agent-for-residential-contractors)): AI change orders that "work like mini-estimates", require client signatures, attach photos and collect payment; plan-based pricing, none shown. The page does not say it reads texts. Raised $5.8M (EIN Presswire and Commercial Observer headlines, 2025-06-03). Most direct competitor.
- [Houzz Pro](https://pro.houzz.com/for-pros/change-orders): change orders from a voice or text command and AI-generated line items (search snippet; price not seen).
- [JobTread](https://www.jobtread.com/features/change-orders): change orders and an [AI connector for Claude and ChatGPT](https://jobtread.com/product-updates/2026-04-13-job-tread-ai-connector) (2026-04-13); a competitor's page claims 10,000 customers. Buildertrend: client e-sign flows into the budget (third-party review); a search summary mentions an AI acquisition dated 2026-07-28 [UNVERIFIED, no source opened]. [Foreman](https://www.ycombinator.com/companies/foreman) (YC) offers AI project management for residential contractors including change orders.
- Small tools: ProBlu (field crews start change orders by text; listed by [Nomic](https://www.nomic.ai/compare/best-ai-for-change-order-management)), [ChangeVerdict](https://www.saashub.com/changeverdict) (forwarded change-request emails compared with the contract baseline), [ScopeGuard Pro](https://peerpush.com/p/scopeguard-zerb) (AI scope reviews, one-click approval), [StayInScope](https://www.hunted.space/product/stayinscope) (Product Hunt, freelancers), [BuildTools](https://www.buildtools.com/blog/2026-03-31-jobtread-vs-buildtools-modern-builder-software) and [Projul](https://projul.com/blog/construction-software-chatgpt-claude/). Vendor claims only.
- Indie builders keep arriving: r/Carpentry, 2026-10-20, ["Built a free 15-second mobile tool to kill verbal scope creep / on-site change order disputes"](https://www.reddit.com/r/Carpentry/comments/1xayhpb/) (title); two student research posts the same week ([r/Contractor](https://www.reddit.com/r/Contractor/comments/1xen90p/), [r/electricians](https://www.reddit.com/r/electricians/comments/1xen9q0/)).
- Classification: CROWDED. Several funded or popular products draft AI change orders. No product found watches a client message thread passively.
- Platform risk: high. Houzz Pro, Handoff and the suites sit where the contractor already works; Jobber or Housecall Pro could add change orders with AI. A general assistant can turn a pasted thread into a change order, but it cannot sit on the job line or run the sign-off.

## 11. Business model
- Payer: the contractor. Price hypothesis: $39 a month per contractor, anchored on the $39-150 a month a solo carpenter pays for software (PRO-010).
- Cost per active user per month [ESTIMATE], 3 live jobs, about 1,320 client and crew messages (20 a day x 3 jobs x 22 days [ASSUMPTION]): screening with Haiku 5.5 using a cached estimate (5,000 tokens x $0.01/1M) plus 600 new tokens (x $0.10/1M) and 80 output tokens (x $0.50/1M) = $0.00015 per call x 1,320 = $0.20; voice memos 30 x 1.5 minutes x $0.003 = $0.14; 6 change-order drafts on Sonnet 5.5 at 6,000 in + 1,000 out = $0.022 each = $0.13; SMS 6 orders x 5 messages x 1.2 x $0.01 [ASSUMPTION] = $0.36; job-line number $1.15 [ASSUMPTION]. Total about $2.00.
- Gross margin (39 - 2) / 39 = 95%.

## 12. Market size
Bottom-up [ESTIMATE, not verified]: 200,000 US small remodelers and trade contractors with 1-20 employees who sign scoped estimates. Sanity check: search summaries of Census County Business Patterns list 111,207 HVAC and plumbing establishments (2023) and 81,842 electrical establishments (2022), so 200,000 across all remodeling trades is conservative. At 2% penetration, 4,000 x $39 x 12 = $1.9M ARR.

## 13. Go-to-market
- First 100: answer change-order and scope-creep threads in r/Contractor and r/Carpentry (the October 2026 threads above are the entry points), publish a free change-order text template and calculator, and offer a 30-day free job line. SEO: "verbal change order", "client says it was included", "change order template remodeling".
- Loop: a GC who uses it invites subcontractors, who face the same scope creep from the GC; every client sign-off page carries a small "sent with Scope Guard" footer.

## 14. Moat and scale path
Weak. A rate book, an extras ledger and per-contractor "do not flag" rules create light lock-in. Scale path: estimates, invoices and deposits from the same job line. Platform risk caps it at 2.

## 15. Solo feasibility
- MVP in 6 weeks: job-line numbers with registration started on day 1, estimate PDF parser, message screening, change-order drafting from a rate book, signature page with audit trail, extras ledger, Stripe billing.
- Running cost before revenue: about $60-90 a month (numbers $10, hosting $20, models $10, SMS $20).
- Hardest risk: capture. Clients must text a new number; false nudges annoy and missed ones erode trust. Signature validity by state is a legal check, not a build risk.

## 16. Pre-mortem
1. Capture friction: clients do not use the job line, contractors do not change habits, and the product degrades to a change-order form.
2. Handoff, Houzz Pro and JobTread make drafting so fast that a $39 add-on has no reason to exist.
3. Nudge quality: too many false flags get muted, and one missed big extra ends trust.

## 17. Cheapest validation test
Give 10 contractors a job line for three weeks and run the screening by hand with model drafts. Cost about $100 and 15 hours. Pass: at least 3 real extras per contractor flagged, 50% or more judged correct by the contractor, $1,000 or more of extras documented across the pilot, and 5 of 10 say they would pay $39. Fail: clients do not use the line, or the contractors already capture extras in their suite.

## 18. Open questions
- Recommendation: kill the passive-capture version; keep only a job-line nudge for one-person shops with no suite, and only if the test passes. Handoff or Houzz Pro owns the rest.
- Do clients actually text a dedicated job number, or will they keep using the contractor's own phone?
- How much do Handoff and Houzz Pro charge for change orders, and do small shops use them?
- Is a typed-name signature with an audit trail enough for change orders in the contractor's state [UNVERIFIED]?
