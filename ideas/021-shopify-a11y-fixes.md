---
id: "021"
slug: shopify-a11y-fixes
name: Shopify A11y Fixes
one_liner: "Shopify app that writes reviewable theme-code accessibility fixes and an evidence log for merchants facing EAA or ADA claims."
target_user: "Shopify merchants with roughly $250K+ revenue selling into the EU or US, especially after an ADA demand letter, plus agencies running 10+ stores"
form_factor: "plugin"
lens: "Forcing function"
frontier: false
competition: "CROWDED"
confidence: "MED"
status: "developed"
signals: [FORCE-20, FORCE-22, FORCE-23, FORCE-24, SVC-32]
scores:
  pain: 3
  evidence: 3
  ai_leverage: 3
  whitespace: 1
  novelty: 1
  why_now: 3
  solo_feasibility: 3
  distribution: 3
  wtp_economics: 3
  scale_defensibility: 2
total: 51.6
price_hypothesis: "$79/month per store, free public audit; agency plan $29/store/month for 10+ stores"
model_cost_per_user_month: "$0.85 model, $0.94 with compute"
gross_margin: "84%"
mvp_weeks: 8
deep_dive: false
red_team: false
---

# Shopify A11y Fixes

## 1. One-liner
Shopify app that writes reviewable theme-code accessibility fixes and an evidence log for merchants facing EAA or ADA claims.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Legal exposure is real (demand letters, EAA enforceable since 2025-06-28) but episodic; most merchants feel it only after a letter (FORCE-24). |
| Evidence quality | 2 | 3 | Four medium signals, two of them first-person Shopify merchants (FORCE-23, FORCE-24); no signal states a price paid. SVC-32 is public-sector, not Shopify. |
| AI leverage | 2 | 3 | Mapping a failing DOM node back to Liquid and writing a minimal patch, plus alt text, is model work; the scanning itself (axe-style rules) is deterministic. |
| Whitespace | 2 | 1 | Two Shopify apps already sell exactly this (Patrol from $200/month, TestParty from $599/month with a $4M seed), plus a long tail of widget apps. |
| Novelty of insight | 1 | 1 | "Fix the code, not an overlay" is both rivals' headline pitch. |
| Why now | 1 | 3 | EAA enforcement and coding-model quality are recent, but both rivals were already in market by 2024 to 2026 on the same logic. |
| Solo feasibility | 2 | 3 | Embedded app, scanner, theme diffs and approvals in about 8 weeks; theme-write access and breaking layouts are the risks. |
| Distribution | 2 | 3 | Shopify App Store and r/shopify are built-in channels, but the category is crowded and review counts of rivals (26 to 293) are hard to match. |
| Willingness to pay and unit economics | 2 | 3 | Clear payer with a legal reason; rivals show a $200 to $599 band; high margin, but churn after the one-off cleanup is likely. |
| Scale and defensibility | 2 | 2 | Shopify-only, easy to copy, Shopify or a funded rival can follow; a per-theme fix library and agency channel are the only moat candidates. |
| **Total** | | **51.6** | |

Confidence: MED. FRONTIER: no.

## 3. The problem
- Who: Shopify merchants (and the agencies that run their stores) who must meet WCAG 2.1/2.2 AA because of the EU's European Accessibility Act (enforceable by Member States since 2025-06-28, FORCE-20) or US ADA demand letters (FORCE-24).
- How often: a one-off cleanup, then continuous drift, because every new product image, theme update and installed app can reintroduce failures.
- What it costs: consultant or agency audits, a lawyer's response to a demand letter, and a compliance line that is "only defined by a judge during litigation" at the operator's expense (FORCE-22).
- Workaround today: install an overlay widget (lawyers warn it can mark the site as a target, FORCE-24), pay a managed service ($599/month at TestParty), hire a freelance developer, or do nothing.

## 4. Evidence
Five cited signals (full rows in `research/SIGNALS.md`):
- FORCE-24 (medium, 2026-08-19): "Main thing I learned is that I definitely wouldn’t just install an accessibility widget and assume the problem is handled. Wish I knew that before getting the letter." Shows: a merchant with a US demand letter who now distrusts widgets. https://www.reddit.com/r/shopify/comments/1vsom2f/
- FORCE-23 (medium, 2026-06-19): "Looking for a trusted recommendation that can help bring a site up to snuff. Hard to know from research what is inflated pricing or actually compliant." Shows: buyers cannot tell real compliance from inflated pricing, so proof of work matters. https://www.reddit.com/r/shopify/comments/1uagft9/
- FORCE-22 (medium, 2026-05-28): "The issue is that the EU framework combines broad principles, partial technical references, vague proportionality requirements, and evolving judicial interpretation. In practice, that means the exact compliance boundary is often only defined by a judge during litigation, and with the website operator funding the clarification process through lawyer and court fees." Shows: no safe harbor, so a logged, good-faith fix trail is the best defense. https://news.ycombinator.com/item?id=48304563
- FORCE-20 (medium, 2025-06-27): law-firm briefing that the EAA "can be enforced by Member States from 28 June 2025" and covers online shops. https://www.traverssmith.com/knowledge/knowledge-container/a-new-milestone-for-accessibility-the-european-accessibility-act-now-applies/
- SVC-32 (medium, 2026-04-23): law-firm alert on the DOJ ADA Title II rule: "Automated remediation tools aren't reliable enough yet" (sentence continues about complex educational and STEM content). Shows the limit of automation (public-sector context). https://www.duanemorris.com/alerts/doj_extends_ada_title_ii_digital_accessibility_deadlines_one_year_0426.html
- New evidence (not in SIGNALS.md), Shopify App Store reviews of TestParty as returned by a page fetch (small-model summary, not re-verified): 2026-07-24, The Sak: "Great app, great team, easy integration and puts your ADA lawsuit worries to bed." 2026-07-19, JOLYN: "Great team and automated workflow - much better than Accessibe, Userway, Level Access etc." https://apps.shopify.com/testparty. Shows paying demand for the code-fix model, and that it is already served.

## 5. The product
- Outcome: install, get a free audit of the storefront, review a batch of theme diffs and content fixes in a preview theme, publish, and keep a dated evidence log that you can hand to a lawyer or regulator.
- Core AI loop: input (rendered pages for about 25 templates, theme files via the Shopify theme API or a connected GitHub repo, product content and images) -> deterministic rule scan, then the model traces each failure to the Liquid/CSS/JS source, drafts a minimal patch (labels, focus order, contrast tokens, ARIA, form errors, heading levels) and writes alt text -> output (pull request or preview-theme diff, content updates queued for approval, before/after scan results, accessibility statement draft) -> feedback (accept or reject per diff; rejections train a per-theme fix library).
- Interaction model: embedded Shopify admin app with a weekly monitor and email alerts when a new product, theme update or app injection breaks a rule.
- Form factor: Shopify app (plugin) plus a public "scan any store URL" page.
- Day in the life: a skincare brand ($1.2M a year, four staff) gets a demand letter on Monday. Tuesday the app scans 25 pages and lists 61 failures. Wednesday the owner reviews 44 theme diffs in a preview and 17 alt-text and label fixes, then publishes. Thursday the lawyer receives a dated before/after log.

## 6. Why the LLM is load-bearing
- A scanner says "button has no accessible name on /products/x"; fixing it means finding which section, snippet or app block renders it and patching without breaking layout. That tracing and patching is what the model does.
- Alt text for hundreds of product images with product context is vision plus language work that merchants skip.
- Without the model the product is a scanner plus a checklist (the free tier of every rival).

## 7. The insight
Merchants cannot judge accessibility vendors (FORCE-23), and widgets are discredited (FORCE-24), so the product that wins is the one that shows its work as a diff and a log. Honest note: both direct rivals already sell "code fixes, not overlays", so this belief is not private.

## 8. Why now, and why this does not exist yet
- Why now: the EAA became enforceable on 2025-06-28 (FORCE-20); the FTC finalized a $1,000,000 order against accessiBe over compliance claims (proposed Jan 2025, finalized Apr 2025, per a competitor's article, secondary); coding models can now write theme patches.
- It exists. Patrol (launched Dec 2024) and TestParty both ship source-code fixes; see section 10.
- What may still be open: a lower price point ($79) than the $200 and $599 tiers, and agency-first white-label use. Both are pricing choices, not insights.

## 9. Inspiration and derivation
- Parents: TestParty (managed remediation as monthly GitHub pull requests), Patrol (AI theme fixes), Deque axe-core scanning, accessiBe/UserWay overlays (the thing to avoid).
- Changed: business model (self-serve $79 with a free audit instead of a $200 to $599 managed plan), distribution channel (agencies reselling per store). Core job and user are unchanged, which is why this is CROWDED.

## 10. Competition check
Queries run (2026-10-31):
1. Web: "Shopify accessibility app fixes theme code WCAG source code remediation not overlay TestParty"
2. Product Hunt: "site:producthunt.com Shopify accessibility WCAG app" (returned no Product Hunt pages)
3. YC: "site:ycombinator.com/companies accessibility WCAG AI remediation" (returned no YC pages)
4. Shopify App Store: "apps.shopify.com accessibility app European Accessibility Act EAA compliance Shopify store"
5. Funding: "TestParty accessibility startup raises funding seed AI accessibility remediation Shopify"
6. Platform: "Shopify Sidekick accessibility audit theme alt text fix merchants 2026" (nothing found on Sidekick accessibility features)
Reads: the [TestParty Shopify listing](https://apps.shopify.com/testparty) and a [2026 comparison of Shopify accessibility apps](https://www.fudge.ai/blog/best-shopify-accessibility-apps/) (written by a rival app vendor, so prices and ratings are second-hand; I read it twice).

Findings:
- [TestParty](https://apps.shopify.com/testparty): "AI-powered accessibility compliance platform" delivered by a team; fixes WCAG failures "directly in your theme's source code" via monthly GitHub PRs, monthly manual audits and compliance certificates. Free (home-page scan) or Pro $599/month ($6,469/year). 5.0 rating, 27 reviews. Funded: [$4M seed, TechCrunch 2024-06-25](https://techcrunch.com/2024/06/25/testparty-raises-4-million-to-help-create-inclusive-websites), plus a [$1,184,700 NSF SBIR Phase II award](https://testparty.ai/blog/testparty-awarded-dollar1184700-in-sbir-phase-ii-funding) (company blog, 2026-08-03).
- [Patrol](https://apps.shopify.com/patrol): "ADA Code Level Fixes"; per the rival's article, a free audit and monitoring plan, then Starter at $200/month ($2,000/year) with automated fixes written into theme source plus image alt text; 5.0 rating, 26 reviews; launched December 2024. Whether fixes land via GitHub PRs or inside Shopify is reported inconsistently. Maker not named on the listing.
- Smaller code-level or audit apps seen in search results (snippet level only): [Remedify](https://apps.shopify.com/remedify) (reviewable drafted alt text), [AccessFix](https://apps.shopify.com/accessfix) (WCAG 2.2 AA storefront check with severity and score), [Access Proof](https://apps.shopify.com/accessproof-3) (audit, free basic plan).
- Overlay and widget apps (the majority): accessiBe ($59/$179/$479 per month, 3.9 stars, 16 reviews), UserWay ($49/$149/$349, 2.6 stars, 10 reviews), Avada Accessibility ($9 to $19, 5.0 stars, 293 reviews), Accessibly (from $5), Accessibility Enabler AW ($12 to $72). AudioEye is not on the Shopify App Store. Prices and ratings from the rival's article, 2026.
- Shopify itself: a testing vendor's blog says the admin has alt text fields but no native scanning, monitoring or VPAT; I found no Shopify accessibility remediation feature (negative result from one search; not proof).

Classification: CROWDED. Two well-reviewed Shopify apps with the same insight, one with venture funding, sit above a long tail of cheap widgets. The open price tier ($29 to $99) is a pricing gap, not a product gap.

Platform risk: medium to high. Shopify controls theme file access and could add accessibility scanning or fixes to admin or Sidekick (not found today, [UNVERIFIED] either way). TestParty and Patrol can drop prices. OpenAI and Anthropic assistants can already patch a theme for a merchant who has a developer. Platform risk caps Whitespace at 3 and Scale at 2; the funded direct rival caps Whitespace at 2; I score 1 because both apply.

## 11. Business model
- Payer: the merchant (owner or ops lead), or the agency paying per store.
- Price hypothesis: $79/month per store with a free public audit; agency plan $29 per store per month for 10+ stores. Anchors: Patrol $200, TestParty $599, accessiBe $59 to $479 (rival article). $79 is a discount to the code-fix tier and a premium to widgets.
- Model cost per store per month [ESTIMATE] (Sonnet 5.5 $2.00 in / $10.00 out; Haiku 5.5 $0.10 / $0.50, from `research/LANDSCAPE.md` section 6):
  - Alt text, 20 new images, Haiku 5.5, 1,500 in + 100 out each: 20 x (1,500 x $0.10 + 100 x $0.50) / 1M = $0.004.
  - Fix drafting, 15 issues a month, Sonnet 5.5, 12,000 in + 1,500 out each: 15 x (12,000 x $2 + 1,500 x $10) / 1M = $0.585.
  - Diff review and re-render check, 15 x (6,000 in + 500 out): 15 x (6,000 x $2 + 500 x $10) / 1M = $0.255.
  - Model total $0.844, about $0.85. Headless-browser compute about $0.10 [ASSUMPTION]. Total $0.94.
  - One-time onboarding (150 issues x ($0.039 + $0.017)) = $8.40.
- Gross margin: ($79 - $0.94 - 15% Shopify revenue share $11.85) / $79 = 83.8%, about 84% [ASSUMPTION: 15% share applies; the share may be lower for early revenue, UNVERIFIED].

## 12. Market size
- [ASSUMPTION] about 4 million active Shopify stores (no verified current count); assume 6% have revenue above $250K or EU exposure above the microenterprise exemption = 240,000 stores.
- Assume 5% buy a recurring accessibility service within two years = 12,000 stores x $79 x 12 = $11.4M a year serviceable.
- Realistic solo-founder share: 10% of that = 1,200 stores x $948 = $1.14M ARR. Churn after cleanup could halve it.

## 13. Go-to-market
- First 100 customers: (1) 40 from a free "scan any Shopify store URL" page ranking for "Shopify ADA demand letter", "Shopify EAA checklist" and "Shopify accessibility audit", and from honest answers in r/shopify and the Shopify Community threads like FORCE-23 and FORCE-24; (2) 30 from the Shopify App Store listing after the first 15 reviews; (3) 30 from 8 to 10 Shopify agencies on the $29 per store plan.
- Timing: demand-letter waves and EU deadlines; agencies need a fix before a client renewal.
- Growth loop: the public scan report is shareable with a developer or lawyer; the generated accessibility statement links back to the evidence log.

## 14. Moat and scale path
- Weak. Candidates: a per-theme fix library (Dawn, Horizon, popular paid themes) that raises diff acceptance rates; the evidence log; agency lock-in.
- Scale path: other platforms (WooCommerce, BigCommerce), then PDFs and documents (see 023), where the same evidence log applies.

## 15. Solo feasibility
- MVP (8 weeks): embedded app and OAuth; storefront crawler with an axe-style rule engine; theme reading through the API or GitHub; diff generation with preview-theme testing; alt text queue; evidence log and statement generator; Shopify billing.
- Running cost before revenue: about $90/month (hosting $25, database $20, headless browser minutes $20, model tests $15, domain and email $10) [ESTIMATE].
- Hardest technical risk: patches that fix one rule and break layout or checkout flows, and Shopify's access rules for writing theme files (theme-write scopes may need Shopify approval, UNVERIFIED), which is why the MVP writes diffs to GitHub or a preview theme instead of live files. Automated tools catch only part of WCAG, so the product cannot promise compliance; the FTC order shows the cost of that claim.

## 16. Pre-mortem
1. Crowded: Patrol at $200 and TestParty at $599 with funding already hold the code-fix slot, and the widgets own the cheap end.
2. One-off demand: merchants fix once and cancel, so lifetime value is a few months.
3. Trust and liability: a customer sued after using the app blames it; accessibility experts say automation alone does not reach conformance (SVC-32), and no outcome guarantee can be offered.

## 17. Cheapest validation test
- Run the scan manually on 20 Shopify stores that posted accessibility or demand-letter questions in r/shopify or the Shopify Community in the last 90 days, send each a free fix list for their top 5 failures (public pages only), and ask whether they would pay $79 a month for the full set plus monitoring.
- Cost: about $20 of model spend and 12 hours; duration 2 weeks.
- Pass: at least 6 of 20 reply and at least 3 say they would pay $79 instead of Patrol's $200 or a freelancer; the proposed patches pass an axe re-scan on at least 80% of tested pages. Fail: fewer than 2 replies that mention price, or a majority already using TestParty or Patrol.

## 18. Open questions
- Recommendation: do not build as a standalone merchant app. Revisit only as an agency white-label product if the test shows agencies pay per store.
- Do Patrol's fixes ship as PRs or inside Shopify, and what is its real churn after the first month?
- Does Shopify require approval for theme-write access, and has it hinted at native accessibility scanning?
- How many EU merchants fall outside the microenterprise exemption (under 10 staff and under EUR 2 million turnover) and so must comply with the service requirements (FORCE-20)?
