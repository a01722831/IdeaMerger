---
id: "022"
slug: backlog-books
name: Backlog Books
one_liner: "Turns months of unreconciled statements into a categorized, evidence-linked ledger and accountant-ready export at a fixed price per month."
target_user: "Owners and bookkeepers facing 3 to 24 months of unreconciled books before a tax, loan, sale or divorce deadline"
form_factor: "web app"
lens: "Service-to-software"
frontier: false
competition: "CROWDED"
confidence: "MED"
status: "killed"
signals: [SVC-07, SVC-08, SVC-09, SVC-11, SVC-12, SVC-15, SVC-19, RED-37, PRO-104]
scores:
  pain: 4
  evidence: 4
  ai_leverage: 4
  whitespace: 1
  novelty: 1
  why_now: 3
  solo_feasibility: 3
  distribution: 3
  wtp_economics: 3
  scale_defensibility: 1
total: 56.8
price_hypothesis: "$79 per backlog month (up to 150 transactions), one-time; optional accountant review add-on"
model_cost_per_user_month: "$1.00 per backlog month"
gross_margin: "95%"
mvp_weeks: 7
deep_dive: false
red_team: false
---

# Backlog Books

> **Main-thread review, 2026-10-31: KILLED.** CROWDED. Accounting Ketchup sells exactly this shape (AI QuickBooks cleanup at a flat rate per backlog month), alongside Otto, Docyt, Botkeeper, Booke and Balance (YC). An unexplored re-scope: financial reconstruction for divorce or loan files (SVC-11), which would need its own evidence. The file is kept as a record of the competition check.

## 1. One-liner
Turns months of unreconciled statements into a categorized, evidence-linked ledger and accountant-ready export at a fixed price per month.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 4 | People already pay $150 to $1,200 per backlog month (SVC-15) or 40+ hours for 450 transactions (SVC-08), and deadlines force action; but each customer buys once. |
| Evidence quality | 2 | 4 | Six on-target signals with money attached (SVC-07, 08, 09, 11, 12, 15); SVC-19, RED-37 and PRO-104 are indirect, so not 5. |
| AI leverage | 2 | 4 | Statement reading, categorization, receipt matching and the owner question list are model work; batch tiers make a month cost about $1. |
| Whitespace | 2 | 1 | Accounting Ketchup already sells a flat rate per backlog month; Otto, Docyt, Botkeeper, Pilot and Balance sell AI-plus-CPA catch-up; Intuit, Xero and Claude do parts natively. |
| Novelty of insight | 1 | 1 | "Price per backlog month" is a competitor's pricing page today. |
| Why now | 1 | 3 | Batch pricing and cheap vision made it viable in the last 18 months, but the window is open to everyone. |
| Solo feasibility | 2 | 3 | Ledger engine, reconciliation to the penny and exports in about 7 weeks; accuracy is the hard risk (SVC-20 reports 71% raw). |
| Distribution | 2 | 3 | High-intent SEO, marketplace gigs and accountant referrals, in a crowded field with one-time customers. |
| Willingness to pay and unit economics | 2 | 3 | Clear payer with a deadline and 95% margin, but a $69 to $99 rival price band and no recurring revenue. |
| Scale and defensibility | 2 | 1 | Feature-sized and one-time; Intuit, Xero and assistants cover statement-based catch-up natively. |
| **Total** | | **56.8** | |

Confidence: MED. FRONTIER: no.

## 3. The problem
- Who: small-business owners and solo bookkeepers who are months or years behind, usually forced by a deadline (tax filing, loan, sale, divorce, a new bookkeeper asking for a look-back).
- How often: a one-time event per business, but a standing queue of such businesses exists (several r/Bookkeeping threads in the last week of October 2026 and live Freelancer.com projects with 39 to 93 proposals).
- What it costs: $150 to $1,200 per month of backlog at CPA firms (SVC-15), 40+ hours for about 450 transactions at a bookkeeping firm (SVC-08), $400 a month for fully manual work (SVC-07), and mistakes that force restatements (PRO-104).
- Workaround today: hire a bookkeeper or a Fiverr or Freelancer.com gig, grind through it in a spreadsheet, prompt a chat assistant one month at a time, or put it off (RED-37: a year unclosed).

## 4. Evidence
Nine cited signals; the six on target (full rows in `research/SIGNALS.md`):
- SVC-08 (strong, 2026-10-29): "Employee spent 40+ hours on a very simple catch-up totaling about 450 transactions. Please tell me I'm not crazy for thinking this is absolutely crazy." Shows: a time anchor, 40+ hours for a small catch-up. https://www.reddit.com/r/Bookkeeping/comments/1xi6k9w/
- SVC-11 (strong, 2026-10-31 (live page)): "I need help get my records back to date following a divorce. I can supply complete bank statements in FIVE different accounts, with money coming in and out as well as transfers FROM one of these FIVE accounts to the other 4 plus 4 other basic accounts, and I want every transaction entered, categorised, and above all I need to know how much money was transferred from one account to another as a total, how much money was supplied to certain suppliers, and how much money was spent." Shows: a live buyer with a GBP 250 to 750 budget wanting a finished file with transfer totals after a divorce. https://www.freelancer.com/projects/financial-analysis/backlog-bookkeeping-from-bank-statements
- SVC-15 (medium, 2026-09-24): "Many firms price catch-up work per month of history behind. Etisson’s 2026 pricing guide puts that rate at $150 to $300 per month for low-complexity books, $300 to $600 for medium, and $600 to $1,200 or more for high-complexity books with payroll problems, multiple entities, or heavy journal work." Shows: the price anchor, per month of backlog (vendor-authored guide). https://www.sdocpa.com/catch-up-bookkeeping-cost-guide/
- SVC-07 (strong, 2026-10-29): "She is charging $400 a month and does everything manually - never even heard of Quickbooks bank sync. Seems a bit high to me." Shows: a seasonal owner with no books since 2023, paying $400/month for manual work. https://www.reddit.com/r/Bookkeeping/comments/1xip24q/
- SVC-12 (medium, 2026-10-31 (live page)): live Freelancer.com project, 39 proposals, budget USD 30 to 250: raw bank statements into reconciled QuickBooks data. SVC-09 (medium, 2026-10-28): a Florida LLC wants a year of statements (about 1,100 transactions) categorized.
- Indirect: SVC-19 (paid migration of four years of Excel into QuickBooks Online), RED-37 (two founders had not closed their books for a year; builder pitch) and PRO-104 (human bookkeeper mistakes forced restated accounts).
- New evidence (not in SIGNALS.md): none usable. The competition searches returned vendor pages, not first-person quotes.

## 5. The product
- Outcome: upload statements and receipts, answer a short question list, and receive a ledger per backlog month that ties to each statement's ending balance, with an evidence link on every line and an export your accountant can import.
- Core AI loop: input (bank and card statements as PDF, CSV or OFX; receipts; prior returns; chart of accounts if any) -> extraction, categorization using the owner's own history, transfer matching between accounts, receipt-to-line matching, reconciliation to the penny -> output: ledger, P&L and balance sheet per month, question list of what the model could not decide, QuickBooks, Xero and CSV exports -> feedback: the owner answers in chat ("that $2,400 on March 3 was a loan payment"), each answer becomes a rule for the other months.
- Interaction model: web upload, then a chat-style question queue; a status page per backlog month; optional accountant review add-on.
- Form factor: web app.
- Day in the life: a salon owner with 14 unclosed months uploads three accounts of PDFs on Tuesday. Wednesday she answers 22 questions in 20 minutes. Thursday her accountant receives a QuickBooks import and a PDF pack where each line links to its statement row or receipt.

## 6. Why the LLM is load-bearing
- Statements and receipts are messy documents; matching "SQ *JOES SUPPLY 4412" to a vendor, a receipt and a category needs reading plus context.
- The question list is the product's interface: the model decides what it cannot know and asks, in plain language.
- Without the model it is a bank-feed rules engine plus manual coding, which is what the 40-hours workflow already is.

## 7. The insight
Catch-up is a one-time, deadline-driven purchase where the buyer wants a finished file, not software, and batch models make each extra month cost cents. Honest note: this belief is already priced into a competitor's page (Accounting Ketchup), so it is not private knowledge.

## 8. Why now, and why this does not exist yet
- Why now: batch tiers ($0.05 in / $0.25 out per 1M tokens on Haiku 5.5) and cheap OCR make a backlog month cost about $1 to process.
- It does exist. Accounting Ketchup (Product Hunt, 3 upvotes) sells AI catch-up per backlog month for QuickBooks; Otto sells fixed-price catch-up with CPA sign-off; Docyt and Botkeeper sell AI-plus-review catch-up; Intuit's agents and Claude for Small Business now do parts of it inside QuickBooks.
- What may still be open: non-QuickBooks, one-time "records reconstruction" jobs such as the divorce case in SVC-11, where the output is a multi-account ledger with transfer totals rather than a QuickBooks file.

## 9. Inspiration and derivation
- Parents: catch-up bookkeeping services (Otto, Docyt, Botkeeper), AI categorizers (Booke AI, Intuit Accounting Agent), statement converters (DocuClipper, Talio) and the Fiverr cleanup gig.
- Changed: core job (finished ledger per backlog month, not ongoing bookkeeping), business model (fixed price per month of backlog, no subscription), interaction model (question queue instead of a bookkeeper's emails). These are the same changes the closest competitors already made.

## 10. Competition check
Queries run (2026-10-31):
1. Web: "AI catch-up bookkeeping upload bank statements categorized reconciled books fixed price per month of backlog"
2. Product Hunt: "site:producthunt.com AI bookkeeping cleanup catch-up bank statements QuickBooks"
3. YC: "site:ycombinator.com/companies AI bookkeeping small business books categorization reconciliation"
4. Xero and QuickBooks apps: "apps.xero.com bank statement PDF import AI categorization backlog catch-up accountants" (no Xero App Store pages returned; statement converters instead)
5. Platform checks shared with 005, 024, 029: Claude for Small Business, Intuit Accounting Agent and Xero JAX searches; plus reads of the Accounting Ketchup listing and Otto's catch-up page.

Findings:
- [Accounting Ketchup](https://hunted.space/product/accounting-ketchup) (also [Product Hunt](https://www.producthunt.com/products/accounting-ketchup)): "AI-powered QuickBooks cleanup. Flat rate. Done in days." Pricing from $69/mo for deep cleans (13 to 24 months behind) to $99/mo for quick fixes (1 to 3 months), read here as a flat rate per backlog month (the page states no total). 3 upvotes, 3 comments; the user connects QuickBooks and says how far behind they are. The same product shape as this idea, but tiny.
- [Otto](https://joinotto.com/catch-up-bookkeeping): "fixed price" catch-up; AI reconciliation engine, with U.S. CPAs signing off every cleanup; "days not weeks" turnaround. No price or funding shown on the page.
- [Docyt](https://docyt.com/catch-up-bookkeeping-services/): AI catch-up bookkeeping service (claims 80%+ of transactions categorized instantly, a vendor claim). [Botkeeper](https://www.botkeeper.com/en/knowledge/automating-catch-up-clean-up-write-up-work): upload PDF statements, AI extracts and categorizes, low-confidence items go to a review queue.
- [Pelcro](https://www.get.pelcro.com/bookkeeping-services): $149/month starter for up to 100 transactions, catch-up quoted separately. [Booke AI](https://www.uplinq.com/uplinq-vs/booke-ai): AI inside QuickBooks and Xero; a comparison site lists $129 flat.
- YC and similar: [Balance](https://www.ycombinator.com/launches/PRK-balance-ai-accounting-firm-for-smbs) (AI-run bookkeeping with accountant sign-off), [Finlens](https://www.ycombinator.com/companies/finlens) (AI copilot for QuickBooks), [Mesh](https://www.ycombinator.com/companies/mesh-2); Pilot has an [AI accountant page](https://pilot.com/platform/ai-accountant) (title seen, not read).
- Statement converters: [DocuClipper](https://www.docuclipper.com/solutions/bank-statement-to-xero/) (PDF to Xero imports with AI categorization, 14-day trial); [Talio](https://workspace.google.com/marketplace/app/talio_expense_categorization_reports/717130884222) (Google Sheets add-on, PDF statements to QuickBooks and Xero, AI tagging; two listings give conflicting prices).
- Marketplace gigs: many Fiverr "clean up and catch up QuickBooks" gigs, for example [this one](https://fiverr.com/she14344/clean-up-and-catch-up-your-quickbooks) (price not seen).
- Platform: Intuit's [Accounting Agent](https://quickbooks.intuit.com/learn-support/en-global/help-article/bank-transactions/learn-accounting-agent-features/L6pl9rv94_ROW_en) suggests categories and matches bank transactions (available on all subscriptions per Intuit's global help page); a search summary of Intuit help also describes a Reconcile Companion that reads uploaded bank statements (page not opened). Xero's [JAX](https://www.xero.com/campaign/auto-bank-reconciliation/) reconciles automatically by rule, match, memory and prediction (in beta in some regions). Claude for Small Business runs a QuickBooks month-end close workflow ([TechInformed](https://techinformed.com/anthropic-brings-claude-workflows-to-small-businesses/)).

Classification: CROWDED. A direct clone at $69 to $99 per backlog month exists, human-reviewed fixed-price catch-up is sold by several venture-style firms (funding not verified here), and the incumbents' agents cover bank-statement matching natively.

Platform risk: high. Intuit and Xero already ship categorization and reconciliation agents inside the ledger, and Anthropic ships a QuickBooks close workflow; a catch-up wizard is a small step for any of them. OpenAI, Google and Microsoft assistants can already process a month of statements on request. A vendor-shipped version within 12 months is likely, which caps Whitespace at 1 and Scale at 1.

## 11. Business model
- Payer: the owner (sometimes the accountant or divorce lawyer), one-time per backlog file.
- Price hypothesis: $79 per backlog month (up to 150 transactions), so 12 months = $948. Anchors: $150 to $1,200+ per month at CPA firms (SVC-15); 40+ hours at $85 to $95/hour (SVC-10) is $3,400 to $3,800 for SVC-08's job; rival Accounting Ketchup $69 to $99; Freelancer.com budgets of USD 30 to 250 (SVC-12) and GBP 250 to 750 (SVC-11). $79 sits inside the incumbent's band, so there is no pricing edge.
- Model cost per backlog month [ESTIMATE] (100 transactions, 4 statement pages, 60 receipts; prices from `research/LANDSCAPE.md` section 6):
  - OCR: 64 pages x $4/1,000 pages = $0.256 (OCR price UNVERIFIED in LANDSCAPE.md).
  - Categorization on Haiku 5.5 batch: 100 x (800 in x $0.05 + 100 out x $0.25) / 1M = $0.0065.
  - 20% escalated to Sonnet 5.5 batch: 20 x (3,000 x $1 + 300 x $5) / 1M = $0.09.
  - Receipt-to-line matching on Sonnet 5.5 batch: 60 x (2,000 x $1 + 200 x $5) / 1M = $0.18.
  - Owner Q&A on Sonnet 5.5: 15 questions x 3 turns = 45 x (3,000 x $2 + 300 x $10) / 1M = $0.405.
  - Final anomaly pass: (20,000 x $2 + 2,000 x $10) / 1M = $0.06.
  - Total $0.9975, called $1.00.
- Other variable cost: storage and compute about $0.20 [ASSUMPTION]; card fees on $79 = 2.9% + $0.30 = $2.59.
- Gross margin: ($79 - 1.00 - 0.20 - 2.59) / $79 = 95.2%, about 95%. An optional accountant spot-check at $49 per backlog month with a $25 contract-bookkeeper cost gives 49% margin on the add-on [ASSUMPTION].

## 12. Market size
- [ESTIMATE] About 33 million US small businesses (commonly cited figure, UNVERIFIED here); assume 2% have three or more months of backlog at any time [ASSUMPTION] = 660,000; average backlog 8 months x $79 = $632.
- 660,000 x $632 = $417M one-time pool. At 0.5% penetration over two years = 3,300 buyers x $632 = $2.1M total, about $1.0M a year. One-time purchases mean revenue must be re-earned every year.

## 13. Go-to-market
- First 100 customers: (1) 40 from high-intent SEO ("catch up bookkeeping cost", "years behind on bookkeeping", "bookkeeping for divorce", "QuickBooks cleanup price"); CPA firms already rank with cost guides (SVC-15 is one); (2) 30 from marketplace gigs priced per month of backlog, where SVC-11 and SVC-12 show live buyers with 39 to 93 proposals; (3) 30 from 10 tax preparers and bookkeepers who refer delinquent clients for a revenue share.
- Timing: January to April tax season and the October extension deadline.
- Growth loop: the accountant who receives a clean file becomes the referrer; each export carries a "prepared with" footer.

## 14. Moat and scale path
- Weak. Candidates: a corrections memory by business type, an accountant referral network, and per-bank statement parsers.
- Scale path: convert finished files into a monthly close subscription, which lands in the crowded AI bookkeeping category (see 024 and 029), or serve legal-event reconstruction (divorce, loan underwriting, audits) where the output is a forensic multi-account ledger.

## 15. Solo feasibility
- MVP (7 weeks): ingestion of PDF, CSV and OFX statements with OCR; double-entry ledger with transfer detection; categorization with the owner's history; receipt matching; question queue; reconciliation checks against ending balances; exports to QuickBooks (API or import file), Xero CSV and PDF pack; evidence link per line.
- Running cost before revenue: about $80/month (hosting $25, database and storage $20, OCR and model tests $25, email and domain $10) [ESTIMATE].
- Hardest technical risk: reconciling to the penny with transfers, loans, payroll, sales tax and opening balances. Unassisted AI categorization topped out at 71% raw accuracy on month-end checks in one report (SVC-20), so deterministic checks and the question queue must carry the load. Liability for wrong filings is a business risk.

## 16. Pre-mortem
1. Crowded: a direct clone at $69 to $99 per month of backlog, human-reviewed rivals, and free native agents leave no room to win on price or novelty.
2. One-time revenue and acquisition cost: each customer buys once, SEO is contested by CPA firms, and the loop depends on accountants.
3. Accuracy and liability: a ledger that is wrong at tax time harms the buyer; owners need an accountant's sign-off, which a $79 price cannot include.

## 17. Cheapest validation test
- Concierge run with 10 owners with real backlogs (found in r/Bookkeeping style threads): process three backlog months each for free using Claude and a script, then ask them to pay.
- Cost: about $30 of model spend and 15 hours; duration 3 weeks.
- Pass: every month ties to its statement ending balance; at least 90% of lines are accepted without edit after the owner Q&A; at least 5 of 10 say they would pay $79 per month of backlog. Fail: below 75% accepted lines or fewer than 3 of 10 willing to pay.

## 18. Open questions
- Recommendation: kill as a standalone product, or narrow to non-QuickBooks "records reconstruction" for legal and financial events (SVC-11 type), or fold it into 024 and 029 as an onboarding feature.
- Who is the real buyer: the owner, or the accountant who receives the file?
- Where does it beat Otto's CPA sign-off and Accounting Ketchup's price?
- How many of Otto's, Docyt's and Pilot's customers come through catch-up, and what do they pay (not visible here)?
