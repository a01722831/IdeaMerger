---
id: "005"
slug: grant-ledger
name: Grant Ledger
one_liner: "Allocates every nonprofit expense to the right grant from the award agreement and drafts funder and board reports."
target_user: "Small nonprofits ($250K to $5M budgets) with 2 to 10 restricted grants, a part-time bookkeeper or finance lead, and QuickBooks Online"
form_factor: "web app"
lens: "Pain-first"
frontier: false
competition: "WEAK DIRECT"
confidence: "MED"
status: "developed"
signals: [PRO-208, PRO-209, PRO-211, PRO-212]
scores:
  pain: 3
  evidence: 3
  ai_leverage: 4
  whitespace: 3
  novelty: 3
  why_now: 3
  solo_feasibility: 3
  distribution: 3
  wtp_economics: 3
  scale_defensibility: 2
total: 60.0
price_hypothesis: "$149/month per organization (up to 5 grants), +$29 per extra grant"
model_cost_per_user_month: "$2.50"
gross_margin: "94%"
mvp_weeks: 7
deep_dive: true
red_team: true
---

# Grant Ledger

## 1. One-liner
Allocates every nonprofit expense to the right grant from the award agreement and drafts funder and board reports.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Monthly coding and quarterly reports eat hours (PRO-211) and one lookup took two days (PRO-208); no evidence of acute loss, so not higher. |
| Evidence quality | 2 | 3 | Four independent r/nonprofit signals from 2026, two strong; none states willingness to pay for this exact job. |
| AI leverage | 2 | 4 | Reading agreements into rules, coding lines with clause citations and drafting narratives is model work; setup cost drops to near zero. |
| Whitespace | 2 | 3 | One tiny direct entrant (4granted) plus adjacent fund-accounting and grant suites; Intuit and Sage are visibly moving, so capped at 3. |
| Novelty of insight | 1 | 3 | "The agreement is the rules engine" is a useful twist on class tracking, not a new category. |
| Why now | 1 | 3 | Long context and Haiku-tier prices make per-line judgment cheap; the need itself is old. |
| Solo feasibility | 2 | 3 | QuickBooks read, agreement extraction and reports fit in about 7 weeks; accuracy and trust are the one hard risk. |
| Distribution | 2 | 3 | State nonprofit associations, bookkeepers with many nonprofit clients, r/nonprofit and the QuickBooks app store; no built-in loop. |
| Willingness to pay and unit economics | 2 | 3 | Clear payer and 94% gross margin, but nonprofit budgets are tight and willingness to pay is unmeasured. |
| Scale and defensibility | 2 | 2 | Niche of perhaps $5M ARR; Intuit (hiring for AI-native nonprofit) and Sage (AI fund accounting) could ship a version; moat is the funder-rule library. |
| **Total** | | **60.0** | |

Confidence: MED. FRONTIER: no.

## 3. The problem
- Who: the finance lead or part-time bookkeeper at a nonprofit with a $250K to $5M budget and several restricted grants, each with its own allowable costs, budget lines, dates and report format.
- How often: coding and variance checks monthly, funder reports quarterly or yearly, board packs every cycle, audits yearly.
- What it costs: one "which grant paid for this flight" lookup took two days (PRO-208); a report pack takes hours of Excel mapping (PRO-211); data clean-up goes to a $10-15K consultant (PRO-209, donor CRM, adjacent). Disallowed or unspent grant money is the downside risk [ASSUMPTION: not quantified in the signals].
- Workaround today: QuickBooks classes or sub-customers per grant, spreadsheets, and coding weeks later from receipts with no context.

## 4. Evidence
Four independent r/nonprofit signals, all 2026 (full rows in `research/SIGNALS.md`):
- PRO-208 (strong, 2026-09-18): "Got asked the other day which grant covered a specific flight and I genuinely couldn't tell them, it took me like two days and even then I was reconstructing it rather than looking it up." Shows: the core pain, an expense-to-grant lookup that takes days because coding happens late. https://www.reddit.com/r/nonprofit/comments/1wju6lb/
- PRO-211 (medium, 2026-02-11): "Right now my process is pretty manual. I export the general ledger file, spend a few hours in Excel mapping accounts to the right line items, build the SOA with restriction columns, then try to make sure the SFP ties out." Shows: the report pack is rebuilt by hand each cycle, with restriction columns and tie-outs. https://www.reddit.com/r/nonprofit/comments/1r1zt5h/
- PRO-212 (medium, 2026-08-06): "I recently read instructions to not spend more than an hour on a report. I appreciate that guidance but the reality is we are a large nonprofit with multiple staff working on multiple aspects of a project that requires gathering data and review in order to ensure accuracy." Shows: funder reports take several staff hours even at a large nonprofit; the writer also doubts funders read them, a caution on report value. https://www.reddit.com/r/nonprofit/comments/1vhidxk/
- PRO-209 (strong, 2026-09-03): "When I ask them to run a query, realign our codes (they were not tracking DAFs or family foundations as foundations) they have to use a consultant. We end up paying 10-15k for the consultant for CRM management." Shows: nonprofits pay five figures for outside data help; this is donor-CRM work, so it is adjacent proof of spend, not proof for this job. https://www.reddit.com/r/nonprofit/comments/1w6dimt/
- Price anchor from `research/SIGNALS.md`: SVC-52 (weak, builder-authored) says a grant writer costs $50 to $150/hour, out of reach for small nonprofits.
- New evidence (not in SIGNALS.md): none usable. The competition searches returned vendor pages, not first-person quotes, so none are counted.

## 5. The product
- Outcome: a live ledger per grant where every charge shows its receipt and the agreement clause that allows it, plus funder-ready budget-vs-actuals, board packs, and warnings before money goes unspent or a cost looks disallowed.
- Core AI loop: input (QuickBooks transactions, bank feed, receipts, award agreements as PDF) -> the model reads each agreement into a rules record (allowable and unallowable categories, budget lines, period, caps, indirect rate, prior-approval items, report dates) -> codes each line as allowed, needs approval, disallowed or split, with a clause citation and confidence -> output: proposed allocation, exception inbox, draft reports -> feedback: the finance lead approves or corrects, and corrections become per-vendor and per-account rules and improve the funder-rule library.
- Interaction model: web app with an exception inbox and a weekly email digest; one-click approve; optional write-back of class or customer tags to QuickBooks after approval.
- Form factor: web app with QuickBooks Online OAuth (Xero second).
- Day in the life: Maria runs finance at a $1.8M youth nonprofit. On Monday the inbox flags 14 of 212 new lines: a flight with no travel line in the federal budget and a software bill to split across two grants. She approves nine in one tap and corrects three. A program officer asks which grant paid for the flight; she answers in 30 seconds from the ledger. At month end she exports budget-vs-actuals for the state grant with a draft narrative.

## 6. Why the LLM is load-bearing
- Award agreements state allowable costs in prose; turning 30 pages of clauses into per-line decisions is reading comprehension, not template matching.
- Ambiguous lines (a flight, a team meal, a subscription) need context from memos, receipts and the budget narrative.
- Funder reports need narrative sections and per-funder formats.
- Without the model the product collapses into fund-accounting setup, where a person hand-builds the rules for every grant.

## 7. The insight
The grant agreement is the rules engine. Fund-accounting tools model grants as buckets and leave the real constraint, written in prose, to a human; once a model reads the agreement, applying it to every transaction costs cents and leaves an audit trail. Finance leads do not want another grant portal; they want to answer "which grant paid for this, and was it allowed?" in seconds.

## 8. Why now, and why this does not exist yet
- Long-context reading and Haiku-tier prices ($0.10 in / $0.50 out per 1M tokens) make per-line judgment cheap. The QuickBooks API has existed for years, so the blocker was reading agreements, not data access.
- Honest status: it partly exists. 4granted (a tiny Product Hunt launch) pitches grant tracking with QuickBooks receipts and reporting, and Sage markets AI for fund, grant and project accounting. I found no product that reads the agreement and enforces it line by line for small QuickBooks-based nonprofits.
- Small nonprofits are a low-ARPU segment that enterprise fund-accounting vendors have little reason to chase.

## 9. Inspiration and derivation
- Parents: fund accounting (Aplos, Sage Intacct, Blackbaud), QuickBooks class tracking, grant-management suites (Instrumentl, Foundant), and evidence-trail products such as chargeback tools.
- Changed: core job (enforce the agreement per transaction, not track fund balances), interaction model (exception inbox instead of chart-of-accounts setup), target user (QuickBooks-based small orgs, not Sage-sized ones), business model (flat SaaS priced under a bookkeeper's hourly cost).

## 10. Competition check
Queries run (2026-10-31):
1. Web: "nonprofit grant expense allocation software QuickBooks restricted funds AI funder reports"
2. Product Hunt: "site:producthunt.com nonprofit grant tracking expenses funder reports AI" (no PH pages returned; surfaced a hunted.space mirror of one PH launch)
3. YC: "site:ycombinator.com/companies nonprofit grant accounting compliance AI" (no grant-accounting company; only YC's nonprofit industry list)
4. QuickBooks marketplace: "QuickBooks app marketplace grant tracking nonprofit apps.intuit.com" (no grant app listing confirmed)
5. Platform checks shared with 022, 024, 029: "Claude for Small Business QuickBooks month-end close Anthropic launch" and "Intuit Assist accounting agent QuickBooks categorize reconcile bank transactions AI agents 2026"; plus a read of the 4granted listing.

Findings:
- [4granted](https://hunted.space/product/4granted): tagline "AI Powered Grant management portal"; "designed to track grants, manage budgets, file receipts, and stay compliant", with QBO integration for expenditures, receipts and reporting. 0 upvotes, 1 comment, no pricing shown. Closest direct competitor; no traction visible; nothing on the page about reading agreements.
- [Instrumentl](https://marketplace.virtuous.org/solutions/instrumentl?taxon_id=7): AI funder matching; post-award tools include spend-down tracking and custom funder reports (marketplace listing). Grant-management first; does not allocate ledger lines.
- [Foundant GrantHub Pro](https://opengrants.io/best-grant-management-software-for-nonprofits/): a roundup says it adds post-award financial tracking and reporting. Same gap.
- [Sage Intacct for nonprofits](https://www.sage.com/en-us/industry/nonprofit-1/), [Aplos](https://www.aplos.com/academy/quickbooks-for-nonprofits-guide-comparison), [Blackbaud](https://www.blackbaud.com/competitors/quickbooks-comparison): fund accounting that handles restricted funds natively; Sage's page pitches AI for fund, grant and project accounting. Prices not verified; aimed above the small end.
- QuickBooks itself: [one grant = one sub-customer or class](https://blueandco.com/tracking-grants-programs-quickbooks) (Blue & Co guide). No agreement reading.
- [Microsoft Copilot nonprofit scenario](https://adoption.microsoft.com/en-gb/scenario-library/nonprofit/grant-tracking-and-reporting): a macro that fills Excel with grant data from CSVs. A workaround, not a product.
- Intuit job listing titled ["Principal Product Manager, AI-Native Nonprofit"](https://jobs.anitab.org/companies/intuit/jobs/82521384-principal-product-manager-ai-native-nonprofit) (title seen in search results, posting not opened): Intuit is staffing for this segment.

Classification: WEAK DIRECT. One direct entrant, tiny and unreviewed; the funded suites are adjacent (different org size or a different job).

Platform risk: moderate. Intuit's [Accounting Agent](https://quickbooks.intuit.com/learn-support/en-global/help-article/bank-transactions/learn-accounting-agent-features/L6pl9rv94_ROW_en) already suggests categories for bank transactions, Intuit is hiring for AI-native nonprofit, and Sage sells AI in fund accounting. Anthropic's Claude for Small Business connects to QuickBooks ([TechInformed](https://techinformed.com/anthropic-brings-claude-workflows-to-small-businesses/)), so a motivated user can prompt an assistant with an agreement PDF and a QBO export, though without approvals or an audit trail. A vendor-shipped version within 12 months is possible but not likely, since per-funder rule logic is niche. This caps Scale at 2 and Whitespace at 3.

## 11. Business model
- Payer: the nonprofit (admin or indirect budget), sometimes through its bookkeeper or CPA firm.
- Price hypothesis: $149/month per organization up to 5 grants, +$29 per extra grant [ASSUMPTION]. Anchors: a freelance bookkeeper quotes $85 to $95/hour (SVC-10), a grant writer $50 to $150/hour (SVC-52); saving 8 hours a month at $35 to $50/hour is $280 to $400 of labor [ASSUMPTION].
- Model cost per active org per month [ESTIMATE] (5 grants, 600 expense lines, 150 receipts a month; prices from `research/LANDSCAPE.md` section 6):
  - Reading agreements, once per grant: 30 pages x 500 tokens x 1.3 tokenizer overhead = 19,500 in on Sonnet 5.5 = $0.039, plus 3,000 out x $10/1M = $0.030, so $0.07 per grant; 5 grants over 12 months = $0.03/month.
  - First-pass coding on Haiku 5.5: (6,000 cached x $0.01 + 500 fresh x $0.10 + 150 out x $0.50) / 1M = $0.000185 per line x 600 = $0.11.
  - 20% escalated to Sonnet 5.5: (6,000 cached x $0.10 + 2,000 x $2 + 400 out x $10) / 1M = $0.0086 x 120 lines = $1.03.
  - OCR for 150 receipts x 1.5 pages x $4/1,000 pages = $0.90 (OCR price UNVERIFIED in LANDSCAPE.md); extraction on Haiku 5.5 150 x $0.00025 = $0.04.
  - Reports and checks on Sonnet 5.5: 5 narratives x $0.035 + board pack $0.06 + funder draft $0.08 + 5 disallowed-cost scans x $0.022 = $0.43.
  - Total about $2.54, called $2.50.
- Other variable cost: hosting, storage and email about $1.00 [ASSUMPTION]; card fees on $149 = 2.9% + $0.30 = $4.62.
- Gross margin: ($149 - 2.54 - 1.00 - 4.62) / $149 = 94.5%, about 94%. Support time is not included.

## 12. Market size
- [ESTIMATE] Target organizations: about 100,000 US nonprofits with $250K to $5M in expenses and two or more restricted grants. Basis: roughly 7% of about 1.5 million registered 501(c)(3) organizations [both figures UNVERIFIED, order of magnitude from memory]; validate with IRS Form 990 extracts (Candid or ProPublica Nonprofit Explorer).
- 100,000 x $149 x 12 = $178.8M a year at full share. At 1% penetration (1,000 orgs) = $1.79M ARR; at 3% (3,000 orgs) = $5.4M ARR. UK, Canadian and Australian charities are upside, not counted.

## 13. Go-to-market
- First 100 customers: (1) a free "grant allocation audit": the founder runs one agreement plus three months of a QuickBooks export and returns a risk report, offered through useful r/nonprofit answers (where PRO-208, PRO-209, PRO-211 and PRO-212 were found), LinkedIn nonprofit-finance groups and state nonprofit association newsletters; target 30 audits and 20 customers. (2) Nonprofit-focused bookkeeping and CPA firms: 10 firms x 6 clients = 60 orgs through a multi-client dashboard and a revenue share. (3) A QuickBooks app store listing (needs Intuit review) for 20 more.
- SEO queries: "which grant paid for this expense", "grant expense tracking QuickBooks", "restricted grant budget vs actual template", "allowable costs checklist 2 CFR 200".
- Growth loop: every funder report and board pack carries an evidence link (each line cites its receipt and clause); program officers and auditors who like it ask other grantees to use it; bookkeepers add clients.

## 14. Moat and scale path
- Moat candidates: a library of funder rule templates (federal Uniform Guidance, state agencies, large foundations) refined by every correction; per-organization precedent memory; an audit-ready evidence ledger that auditors reuse; QuickBooks write-back lock-in.
- Scale path: small nonprofits, then multi-entity and mid-size orgs (single-audit prep), then other grant-funded users (university labs, research groups, public agencies). It stays a niche business unless it moves upmarket.

## 15. Solo feasibility
- MVP (7 weeks): QuickBooks Online read connection; agreement upload and rules extraction with human edit; line coding with citations and a confidence threshold; exception inbox; budget-vs-actuals and one funder report template exported to Excel and PDF; deadline and underspend alerts. Xero, bank feeds, write-back and more templates come after launch.
- Running cost before revenue: about $90/month (hosting and database $45, model tests $25, email and domain $10, monitoring $10) [ESTIMATE].
- Hardest technical risk: line-level accuracy on ambiguous costs and split allocations, with a trust bar set by fiduciary duty. Second: Intuit app review and API terms [UNVERIFIED].

## 16. Pre-mortem
1. Trust: one wrong "allowed" call on a federal grant and the finance lead abandons the tool; auditors may not accept AI coding. Mitigation: suggest-only mode, clause citations, confidence thresholds.
2. Platform: Intuit or Sage ships agreement-aware allocation inside the suite at no extra cost.
3. Sales: small nonprofits buy slowly and churn when a grant ends; the signals show pain but no stated willingness to pay, and an ACV near $1.8K caps the business.

## 17. Cheapest validation test
- Concierge test with 10 small nonprofits: take one agreement and three months of QuickBooks export, run the pipeline plus 30 minutes of manual cleanup, and return the allocation sheet and a draft funder report within 48 hours.
- Cost: about $20 of model spend and 15 hours of work; duration 3 weeks.
- Pass: at least 90% of lines match the finance lead's own coding after one correction round, at least 6 of 10 say they would pay $149/month, and at least 3 pay a $99 deposit or sign an intent letter. Fail: accuracy under 80%, or fewer than 3 of 10 would pay.

## 18. Open questions
- Is the real buyer the nonprofit or its bookkeeper (reseller)? Do multi-client firms pay more per organization?
- Which funder types first (federal pass-through, state agency, foundation), and how many templates before it feels complete?
- Do Intuit's API terms and any usage fees allow write-back at this price [UNVERIFIED]?
- Would auditors accept model-assisted allocation with a clause citation and an approval log?
- How does 4granted work in practice, and is it still maintained?

## Deep dive

Method (reads dated 2026-10-31): IRS Exempt Organizations Business Master File extracts (eo1 to eo4 CSVs, downloaded and counted), WebFetch of an Intuit App Partner Program explainer, 4 web searches (Intuit program, Xero developer pricing, Aplos and Instrumentl pricing, nonprofit counts), and the Arctic Shift Reddit archive for channel volume and platform mentions. Model prices: `research/LANDSCAPE.md` section 6.

### Competitor table
| Competitor | Link | What it does | Price (as published, with date read) | Funding or traction (sourced) | Gap this idea exploits |
|---|---|---|---|---|---|
| 4granted | [listing](https://hunted.space/product/4granted) | "AI Powered Grant management portal"; tracks grants, budgets, receipts; QuickBooks Online integration | not published | 0 upvotes, 1 comment (first pass) | Nothing on reading the agreement or line-level enforcement |
| Instrumentl | [Virtuous listing](https://marketplace.virtuous.org/solutions/instrumentl?taxon_id=7), [Capterra](https://www.capterra.com/p/233384/Instrumentl/) | AI funder matching; post-award spend-down tracking and funder reports | Capterra: Basic $179/month (5 projects), Standard $299 (10), Pro $499 (20), Advanced $899 (40). A competitor, GrantWatch, reports $349 monthly or $299 billed annually, and $999 for Full Lifecycle. Conflicting, [UNVERIFIED] (search summary, 2026-10-31) | not found | Discovery first; does not allocate ledger lines |
| Foundant GrantHub Pro | [roundup](https://opengrants.io/best-grant-management-software-for-nonprofits/) | Adds post-award financial tracking (roundup) | not read | not found | Same gap |
| Aplos | [pricing](https://www.aplos.com/pricing) | Fund accounting for small nonprofits | Lite $79/month, Core $129/month, 50% off for 3 months, 15-day trial (official page per search summary, 2026-10-31); third-party listings show Core $99, Advanced $189 to $229 | not found | A replacement ledger with funds as buckets, so orgs already on QuickBooks must migrate; does not read agreements |
| Sage Intacct for nonprofits, Blackbaud | [Sage](https://www.sage.com/en-us/industry/nonprofit-1/), [Blackbaud](https://www.blackbaud.com/competitors/quickbooks-comparison) | Fund accounting; Sage pitches AI for fund, grant and project accounting | not published in sources read | not sourced | Aimed above the small end |
| QuickBooks classes, Intuit Accounting Agent | [Blue & Co guide](https://blueandco.com/tracking-grants-programs-quickbooks), [Accounting Agent](https://quickbooks.intuit.com/learn-support/en-global/help-article/bank-transactions/learn-accounting-agent-features/L6pl9rv94_ROW_en) | One grant = one class or sub-customer; the agent suggests categories. Intuit lists a "Principal Product Manager, AI-Native Nonprofit" role (title only, first pass) | not read | Intuit is the platform | No agreement reading; the largest platform risk |
| Claude for Small Business with QuickBooks; Microsoft Copilot nonprofit scenario | [TechInformed](https://techinformed.com/anthropic-brings-claude-workflows-to-small-businesses/), [Microsoft](https://adoption.microsoft.com/en-gb/scenario-library/nonprofit/grant-tracking-and-reporting) | Assistant and macro routes: prompt with an agreement and an export | n/a | n/a | No approvals, no audit trail, no memory of corrections |
| Bookkeepers and Excel | SVC-10 ($85 to $95 an hour); Arctic Shift sample | In 1,000 r/nonprofit posts (2026-08-17 to 2026-10-30) Excel or spreadsheets appear in 18, QuickBooks in 10, Sage in 1, Blackbaud in 1, Xero 0, Aplos 0 | n/a | n/a | The real baseline is a spreadsheet; QuickBooks is the named platform |

**Marketplace channel check (QuickBooks and Xero).**
- Intuit ([explainer](https://www.apideck.com/blog/quickbooks-api-pricing-and-the-intuit-app-partner-program), published 2025-09-20, updated 2026-10-06): Builder $0 a month, Silver $300, Gold $1,700, Platinum $4,500. Core calls (create, update) are free and uncapped; CorePlus calls (reads, queries, reports) are metered: Builder gets 500,000 credits a month and is blocked beyond that, Silver 1M with overage at $3.50 per 1,000 calls, Platinum up to 75M at $0.25 per 1,000. Full variable fees began 2025-11-01. My app is read-heavy, so it uses CorePlus: about 90 calls per org-month (30 nightly syncs x 3 queries) [ESTIMATE], so the free tier covers about 5,500 orgs, and Silver overage would cost 90 x $3.50 / 1,000 = $0.32 per org-month. Fees are not the barrier. Not covered by the page: production-key review, store listing rules, review time, AI-data terms [UNVERIFIED].
- Xero ([developer FAQ](https://developer.xero.com/faq/pricing-and-policy-updates), [pricing](https://developer.xero.com/pricing), search summaries): since 2026-03-02 tiers are by connections (Starter 5, Core 50, Plus 1,000, Advanced 10,000, Enterprise unlimited); secondary sources give about AUD 0 / 35 / 245 / 1,445 a month; the app-store revenue share was dropped; public listing is reportedly required only at Enterprise; updated developer terms reportedly bar using API data for AI or ML training and certain automated tools. Read those terms before building. Demand evidence is thin: Xero appears in 0 of 1,000 r/nonprofit posts.
- Verdict: cheap to connect, unproven as a channel. Connect by invitation (OAuth) for the first 100 customers, apply for the Intuit listing around customer 20 as a trust badge, treat Xero as optional.

### Market sizing (bottom-up)
Source: IRS Exempt Organizations Business Master File, [eo1.csv](https://www.irs.gov/pub/irs-soi/eo1.csv) to eo4.csv (eo1 last modified 2026-10-13), counted 2026-10-31: 1,650,468 records with SUBSECTION 03 (501(c)(3)); 1,519,714 after removing private foundations (FOUNDATION codes 02, 03, 04). Latest-return income (INCOME_AMT, income not expenses) of $250K to $5M: 169,515; $500K to $5M: 111,655; $1M to $5M: 65,951. Some may be inactive.
| Case | Buyers | Adoption | Annual price | Serviceable ARR |
|---|---|---|---|---|
| Conservative | 111,655 x 40% with 2+ restricted grants x 50% on QuickBooks Online [both ASSUMPTION; QuickBooks leads platform mentions] = 22,331 | 2% = 447 orgs | $149 x 12 = $1,788 | $0.80M |
| Optimistic | 169,515 x 60% x 65% = 66,111 | 5% = 3,306 orgs | $1,788 + 1 extra grant x $29 x 12 = $2,136 | $7.06M |
Revenue at 100 / 1,000 / 10,000 orgs: $179K / $1.79M / $17.9M at $149 (or $214K / $2.14M / $21.4M at $2,136). 10,000 orgs would be 45% of the conservative pool and 15% of the optimistic one, so that row needs the bookkeeper channel plus UK, Canada and Australia. The first-pass 100,000 is plausible but is an upper bound after the grant and QuickBooks filters.

### Unit economics
Per org-month: 5 grants, 600 lines, 150 receipts. Every line [ESTIMATE].
| Line | Arithmetic | $ |
|---|---|---|
| Read agreements, Sonnet 5.5 | 30 pages x 500 x 1.3 = 19,500 in x $2/1M = $0.039 + 3,000 out x $10/1M = $0.030 = $0.069 per grant x 5 / 12 months | 0.03 |
| First-pass coding, Haiku 5.5 | (6,000 cached x $0.01 + 500 x $0.10 + 150 x $0.50) / 1M = $0.000185 per line x 600 | 0.11 |
| 20% escalated to Sonnet 5.5 | (6,000 cached x $0.10 + 2,000 x $2 + 400 x $10) / 1M = $0.0086 x 120 lines | 1.03 |
| OCR and receipt extraction | 150 x 1.5 pages x $4/1,000 = $0.90 (price UNVERIFIED) + 150 x $0.00025 Haiku = $0.04 | 0.94 |
| Reports and checks | 5 narratives x $0.035 + $0.06 board pack + $0.08 funder draft + 5 scans x $0.022 | 0.43 |
| Hosting, storage, email | [ASSUMPTION] | 1.00 |
| Stripe on $149 | 2.9% x $149 + $0.30 | 4.62 |
| Infrastructure share | $90 / 100 orgs | 0.90 |
| Support | 12 min at $25/hour [ASSUMPTION] | 5.00 |
| **Total** | model and OCR $2.53 + the rest | **14.05** |
Gross margin (149 - 14.05) / 149 = 91%. In the first two months add an hour of founder review at $25: margin 74%. **Heavy user:** 15 grants, 3,000 lines, 600 receipts (900 pages): agreements $0.09, Haiku 3,000 x $0.000185 = $0.56, Sonnet 600 x $0.0086 = $5.16, OCR 900 x $0.004 = $3.60, extraction $0.15, reports $1.32, QuickBooks reads $0.35 = $11.22. Priced at $149 + 10 extra grants x $29 = $439, cost with Stripe $13.03, hosting $3, infrastructure $0.90 and support $10 is $38.15: margin 91%. Left on the $149 plan it would cost $29.74: margin 80%. Caps: the base plan includes 1,000 lines and 300 receipts; each extra grant adds 200 lines; extra lines $0.02; Sonnet escalations above 25% of lines prompt the user to create a vendor rule.

### First 100 customers
Channel volume (Arctic Shift to 2026-10-30, broad regex): r/nonprofit about 12.6 posts a day, about 15 a week on grants, restricted funds, QuickBooks or audits; r/Accounting about 94 a day, about 40 a week on nonprofit, grant or fund accounting; r/QuickBooks about 8 a day, about 4 a week. Reddit is thin; associations and bookkeepers carry volume. Message: "Which grant paid for this flight? Answer in 30 seconds, with the clause and the receipt." Offer: free allocation audit (one agreement plus 3 months of export), then $149 a month, first month free. Funnel [ESTIMATE]: audit request to completed submission 50%, audit to paid 25%, webinar attendee to audit request 15%, bookkeeper call to pilot 40%.
| Week | Action | New paid | Cum. |
|---|---|---|---|
| 1 | Convert audits from the validation test; post an "expense-to-grant lookup checklist" in r/nonprofit and r/Accounting after reading their rules | 2 | 2 |
| 2 | Pitch 2 state nonprofit associations for a member webinar or newsletter slot (30 attendees x 15% = about 4 audits each) | 2 | 4 |
| 3 | 40 individual notes to bookkeepers and CPA firms that list nonprofit clients; aim for 10 calls | 2 | 6 |
| 4 | Run 12 audits; publish an allowable-cost checklist keyed to 2 CFR 200 (SEO: "allowable costs checklist 2 CFR 200", "which grant paid for this expense") | 3 | 9 |
| 5 | 4 bookkeeper firms pilot with 1 to 3 clients each; 20% revenue share | 4 | 13 |
| 6 | LinkedIn nonprofit-finance groups; second webinar | 4 | 17 |
| 7 | Apply for the Intuit App Store listing (lead time unknown) | 4 | 21 |
| 8 | Review corrections and accuracy; price test $149 vs $99 | 4 | 25 |
Base case about 25 paying orgs by week 8; 100 around month 6 if 10 firms bring 6 clients each. Loop: each funder report and board pack carries a link from every line to its receipt and clause, so program officers and auditors meet the product; bookkeepers add clients through a multi-client dashboard.

### One-week validation test (under $50)
**What:** a free manual sample allocation, labeled as such. Day 1: one-page site and form: "Send one grant agreement (PDF) and a 3-month QuickBooks transaction export (CSV or Excel, personal and donor names removed). In 48 hours I return every line coded to a grant with the clause that allows it, plus an exception list. Manual test, no software live, files deleted after 14 days, no QuickBooks login needed." Days 1 to 2: post once in r/nonprofit and once in r/Accounting after reading rules; a LinkedIn post; 5 individual emails to bookkeepers who list nonprofit clients; 1 email to a state nonprofit association. Days 2 to 6: run the pipeline by hand (Sonnet 5.5 to read the agreement, Haiku 5.5 first pass, Sonnet on about 10% of lines), return the sheet; the finance lead marks each exception "useful" or "wrong" and 10 random auto-allowed lines "agree" or "disagree". Day 7: ask for a $99 refundable founding deposit (or a signed intent) and a 3-question survey.
**Budget:** domain $12 (optional); model credit $20 (8 audits x about $1.95: agreement $0.07 + 1,800 Haiku lines x $0.000185 = $0.33 + about 180 Sonnet lines x $0.0086 = $1.55); Stripe fees on 3 refunded $99 deposits 3 x ($2.87 + $0.30) = $9.51. About $42.
**Pass:** 5 or more orgs submit both files; 75% or more of flagged exceptions marked useful; 38 or more of 40 random auto-allowed lines agreed (4 orgs); 2 or more deposits or signed intents; 3 of 5 say they would pay $99 a month or more. **Fail:** under 3 submissions, exception precision under 65%, an obviously unallowable line (alcohol, entertainment) auto-allowed twice, or zero deposits.

### Build brief (paste into a coding session)
```text
PRODUCT: Grant Ledger reads each grant agreement into a rules record, codes every nonprofit expense to the right grant with a clause citation, and drafts funder and board reports.
The finance lead works an exception inbox; nothing is written back to QuickBooks. Target: nonprofits with $250K to $5M in income, 2 to 10 restricted grants, QuickBooks Online.
MVP FEATURES (each testable)
1 QuickBooks Online OAuth, read-only, nightly sync of Purchase, Bill, Deposit, JournalEntry, Account, Class, Customer, Vendor and attachments. Test: 600 lines sync in under 2 minutes and totals match the QBO report.
2 Agreement upload (PDF) to a rules record: period, budget lines, allowed and unallowed categories, caps, indirect rate, prior-approval items, report dates; each rule with clause quote and page; edit screen. Test: every quote found in the PDF text.
3 Line coder: allowed / needs approval / disallowed / split, with clause, confidence, reason.
4 Exception inbox with approve or correct; corrections become vendor and account rules.
5 Per-grant ledger: search any expense, see receipt and clause (the "which grant paid for this flight" answer).
6 Budget-vs-actuals, underspend and deadline alerts, Excel and PDF export.
7 Draft funder narrative and board pack from approved lines only; numbers copied from the ledger.
8 Weekly email digest. 9 Stripe: $149/month up to 5 grants, +$29 per grant, 1,000 lines included. 10 Audit log of every decision (model version, prompt hash, user action), exportable.
NON-GOALS: write-back to QuickBooks, Xero, bank feeds, grant discovery, donor CRM, payroll or time tracking, multi-entity, single-audit prep, native apps.
CORE AI LOOP: (a) agreement to rules JSON, Sonnet 5.5, once per grant, human edits; (b) first-pass coding, Haiku 5.5 with the rules record cached and per-vendor memory; (c) low-confidence or high-dollar lines to Sonnet 5.5 with memo and receipt; (d) receipt OCR plus Haiku 5.5 extraction; (e) reports, Sonnet 5.5, from ledger JSON; (f) disallowed-cost scan before every export. Prompts: cite a clause id or say "no clause found"; never mark "allowed" without a citation; suggest-only mode. Humans: finance lead approves exceptions; auto-approve only lines matching a previously approved rule.
DATA MODEL: Org, User, QboConnection, Grant(period, budget), Agreement, RuleRecord, Rule(category, status, cap, quote, page), Transaction, Receipt, Allocation(txn, grant, status, confidence, clause_id, model_version), Exception, Correction, VendorRule, Report, AuditLog.
INTEGRATIONS: QuickBooks Online API https://developer.intuit.com/app/developer/qbo/docs/get-started (path not opened; tiers and fees: https://www.apideck.com/blog/quickbooks-api-pricing-and-the-intuit-app-partner-program); Xero https://developer.xero.com/pricing (optional, read the AI terms first); Stripe https://docs.stripe.com/billing; Resend https://resend.com/docs; ExcelJS https://github.com/exceljs/exceljs; Mistral OCR https://docs.mistral.ai/ (price UNVERIFIED).
STACK (about $90 to $120 a month): Next.js on Vercel $20, Supabase $25, Inngest free tier, Resend, Stripe, Sentry and Langfuse free, OCR pay per use.
EVALS: 1 Synthetic agreement with 12 clauses (prior approval for travel above $1,000, alcohol unallowed, indirect cap 10% of direct costs, period 2026-01-01 to 2026-12-31) and 60 labeled lines: 90% match, zero false "allowed" on the 10 unallowable lines. 2 Split: a $1,200 software invoice with memo "60/40 Grant A/B": two allocations summing to exactly $1,200. 3 Out of period: an expense dated 2025-12-30 flagged against a grant starting 2026-01-01, 10 of 10. 4 Citation integrity: 100% of cited quotes appear verbatim in the agreement. 5 Learning: after one vendor correction the next 10 lines from that vendor follow it; report totals equal ledger sums to the cent.
BUILD PLAN (7 weeks): W1 auth, Stripe, QBO OAuth and sync, schema. W2 agreement upload, rules extraction, edit screen, quote check. W3 line coder with cached prompts; evals 1 to 3. W4 exception inbox, vendor rules, per-grant ledger. W5 budget-vs-actuals, alerts, exports. W6 receipt OCR, narratives, digest. W7 audit log, privacy settings, onboarding, pilot with 5 orgs.
RISKS TO TEST FIRST: 1 one wrong "allowed" call destroys trust (suggest-only mode, citations); 2 Intuit production-key and listing review (unknown); 3 many orgs misuse or skip classes, so lines lack a grant hint; 4 will auditors accept model-assisted coding with an approval log; 5 Xero AI-data terms; 6 buyer is the nonprofit or its bookkeeper.
```

**Notes for the main researcher:** The IRS file gives 169,515 public charities with $250K to $5M of latest-return income, so section 12's 100,000 is a plausible upper bound after the grant and QuickBooks filters, not a count. Marketplace fees are low (Intuit Builder tier $0), but listing review and reach are unverified, so Distribution 3 rests on bookkeepers and associations. No score change proposed.

## Red team
Skeptical-investor review on 2026-11-01 (full text: `research/RED_TEAM_B.md`). Verdict: **maybe**.

**Top attacks (summarized):**
1. **The hardest allocation is out of scope and the accuracy bar is loose for a fiduciary.** Payroll and time-and-effort are non-goals, yet salaries charged to several grants are usually the biggest grant line; a 90% to 95% accuracy bar means 30 to 60 wrong lines a month on a nonprofit's books [ESTIMATE in the red-team file].
2. **The channel sells against its partners.** 60 of the first 100 organizations come through bookkeepers whose billable hours the tool removes, and the Intuit listing path is unreviewed.
3. **The platform is both data source and competitor.** Intuit staffs an AI-native nonprofit product and ships an Accounting Agent; Anthropic ships a QuickBooks connector; Intuit's and Xero's terms on AI use of data are unresolved.
What would change the red team's mind: five concierge nonprofits where the finance lead leaves 95%+ of auto-allowed lines unchanged (including a salary test), 3 paying the $99 deposit, and one CPA who audits federal awards accepting clause-cited, approver-logged allocations as support.

**Response (main researcher):**
- Attack 1 lands as a product gap, not a score change. v1 adds salary allocation from simple time-and-effort percentages (the biggest grant line), and every allocation is a proposal the finance lead approves, so the miss rate becomes review time, not wrong books. The CPA acceptance letter is added to the validation plan.
- Attack 2 lands partly. Bookkeepers on fixed monthly fees gain from removing allocation grunt work; hourly bookkeepers do not. Direct channels (nonprofit finance communities, state nonprofit associations, TechSoup) carry the rest. Distribution stays at 3.
- Attack 3 is already priced in: whitespace 3 and scale 2 reflect the platform cap.
- Evidence stays at 3: four on-job signals, two strong, one with real spend (a $10K to $15K consultant, PRO-209). No score changes; this is the only idea in the second batch the red team did not pass on.
