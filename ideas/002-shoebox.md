---
id: "002"
slug: shoebox
name: Shoebox
one_liner: "Turns a decade of medical bills and EOBs into matched, audit-ready proof for tax-free HSA reimbursement."
target_user: "HSA holders who pay medical costs out of pocket now and plan to reimburse themselves years later"
form_factor: "web app"
lens: "Pain-first"
frontier: false
competition: "WEAK DIRECT"
confidence: "MED"
status: "developed"
signals: [LIFE-09, LIFE-10, LIFE-11]
scores:
  pain: 3
  evidence: 3
  ai_leverage: 3
  whitespace: 2
  novelty: 2
  why_now: 3
  solo_feasibility: 4
  distribution: 3
  wtp_economics: 2
  scale_defensibility: 2
total: 54.7
price_hypothesis: "$19/year after 25 free documents; $49 one-time backlog import and audit binder"
model_cost_per_user_month: "$0.07 steady state; $5.2 one-time for a 250-document backlog"
gross_margin: "90%"
mvp_weeks: 4
deep_dive: false
red_team: false
---

# Shoebox

## 1. One-liner
Turns a decade of medical bills and EOBs into matched, audit-ready proof for tax-free HSA reimbursement.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Large dollars at stake (about $50K to substantiate in LIFE-10) but it bites once a year to once a decade, and Drive folders and spreadsheets mostly cope. |
| Evidence quality | 2 | 3 | Three cited signals plus six more 2026 r/HSA threads; nobody states a willingness to pay and a dozen apps are free or under $7 a year. |
| AI leverage | 2 | 3 | Extraction is a commodity; the model earns its keep pairing a messy itemized bill with the right EOB, but a manual tracker works without it. |
| Whitespace | 2 | 2 | About ten small HSA receipt apps, most launched in 2026, and custodians store receipts for free; only automatic bill-to-EOB pairing is unclaimed. |
| Novelty of insight | 1 | 2 | The matched pair is a useful framing, but HSA guides already say to keep the EOB with the itemized bill. |
| Why now | 1 | 3 | Record 41.7M accounts and cheap extraction, but the same cheap build is what produced the indie flood. |
| Solo feasibility | 2 | 4 | Four weeks with off-the-shelf OCR and LLM calls; the risks are match accuracy and a 20-year storage promise. |
| Distribution | 2 | 3 | Search plus r/HSA, Bogleheads and FIRE forums, but every competitor targets the same places and there is no built-in loop. |
| Willingness to pay and unit economics | 2 | 2 | Price anchors are $0 to $7 a year and $4.99 once; margin is excellent but the price will not hold above about $20. |
| Scale and defensibility | 2 | 2 | Feature-sized; custodians could add pairing; the only lock-in is a decade of archived documents. |
| **Total** | | **54.7** | |

Confidence: MED. FRONTIER: no.

## 3. The problem
- Who: HSA holders running the "20-year shoebox" strategy (pay medical costs from cash now, let the HSA compound, reimburse tax-free years later), including couples near retirement with 10+ years of paper.
- How often: every medical expense for decades; the crunch comes at withdrawal or audit. A 112-comment r/HSA thread (LIFE-09) shows it is a live, recurring question.
- Cost: one retired couple scanned 200 to 300 bills and hand-built a spreadsheet to substantiate about $50K (LIFE-10); thermal receipts fade within two years (LIFE-09). HSA guides say a card statement or total-only receipt does not show what was bought.
- Workarounds: Google Drive folders, spreadsheets, a NAS plus a one-button "medical scan" printer (LIFE-11), and a growing set of free indie apps.
- Gap: nobody hands the holder a de-duplicated set where each expense has its itemized bill, its EOB and a "not reimbursed elsewhere" record.

## 4. Evidence
- **LIFE-09** (strong, 2026-10-11, r/HSA, 63 pts / 112 comments): "As the years go on and receipts pile up, keeping track of everything for a future IRS audit has been a bit of a headache. I noticed a couple of my physical thermal paper receipts from 2 years ago are already starting to fade, and my Google Drive folder is getting messy." https://www.reddit.com/r/HSA/comments/1x30ge3/
- **LIFE-10** (medium, 2026-07-16, r/HSA): retired couple scanning 200 to 300 bills for about $50K. "Next part is creating a spreadsheet with a row for each scanned bill. I'm about halfway through this process now." https://www.reddit.com/r/HSA/comments/1uy3pkc/
- **LIFE-11** (weak, 2025-08-05, HN): home-built NAS pipeline, a workaround rather than a complaint. "For keeping receipts, we have a process where we dump our eligible receipts into a folder on the NAS and have the scanner/printer setup with a one-button "medical scan" that also dumps paper bills into that folder." https://news.ycombinator.com/item?id=44796783
- New evidence (not in SIGNALS.md): r/HSA, 2026-05-13, 9 pts / 14 comments (title): "What is the best HSA software/app to maintain EOBs, invoices, etc for the IRS?" https://www.reddit.com/r/HSA/comments/1tbnlr5/
- New evidence (not in SIGNALS.md): r/HSA, 2026-09-12, 7 pts / 7 comments: "Can I use the past insurance EoB’s where I have paid out of pocket as receipts, to get my HSA reimbursed." Shows the EOB-versus-bill confusion directly. https://www.reddit.com/r/HSA/comments/1we8vnm/
- New evidence (not in SIGNALS.md): r/HSA, 2026-05-19, 25 pts / 30 comments: "What are people doing to record or keep those expenses?" https://www.reddit.com/r/HSA/comments/1th6kwf/
- Counter-signal (same thread as LIFE-10): "Even though the odds of an IRS audit are low, I became paranoid about losing all this to a fire." Fear of loss, not a present audit, drives the effort. https://www.reddit.com/r/HSA/comments/1uy3pkc/
- Documentation guide (WebFetch extract of a third-party HSA site, page dated 2026-02-10, updated 2026-04-03; not IRS text): "Credit card statements are rarely enough on their own." It adds that an EOB "is especially useful when you reimburse yourself later and need to prove you did not double-dip." https://www.hsalist.org/resources/hsa-audit-risk-and-documentation-guide

## 5. The product
- What it does: a private inbox for a household's medical paperwork. AI reads every receipt, itemized bill, EOB and pharmacy statement, pairs each provider bill with its EOB (billed, plan paid, patient owes), checks the item against published IRS Pub 502 categories, flags duplicates and anything already reimbursed, keeps the unreimbursed balance, and exports an audit binder (indexed PDF plus originals) at withdrawal time.
- Core AI loop: photo, PDF or forwarded email in -> OCR and extraction (provider, date of service, line items, amounts) -> candidate matching by provider, date window and amount, with LLM adjudication when ambiguous -> ledger row with a confidence score and the attached pair -> user confirms or corrects; corrections become matching rules.
- Interaction model: a personal email address, a share-sheet upload and bulk import; a monthly digest ("3 bills are still waiting for their EOB"). No bank connection.
- Form factor: web app (PWA) with a one-click full export; optional sync to the user's own cloud drive so the proof outlives the company.
- Day in the life: Dana forwards a $240 lab bill. Two weeks later the EOB arrives by mail and she snaps it. Shoebox pairs them, marks the item as matching a Pub 502 category, and adds $240 to her unreimbursed balance. In year 14 she taps "Build audit binder for a $30,000 withdrawal" and gets an index with each pair attached and a duplicates check.
- Liability line: organization and arithmetic only. The eligibility check reports a match against a published list; the holder decides what to withdraw; no tax advice.

## 6. Why the LLM is load-bearing
- Without the model, OCR still reads totals, but it cannot reliably pair a provider's multi-line itemized bill (service dates, CPT lines) with an EOB whose descriptions are worded differently, or tell that a total-only receipt lacks the detail a reviewer would want.
- The long tail of formats (dental ledgers, pharmacy printouts, EOBs from dozens of insurers) is what breaks template-based parsers.
- Without the model the product collapses into a $5 manual tracker, which is exactly what the competitors are.

## 7. The insight
- The unit of proof is a matched pair (itemized bill = what was bought, EOB = what insurance paid and what remained) plus a record that it was not reimbursed elsewhere. Apps store receipts; the job at withdrawal time is a defensible, de-duplicated set.
- Honest limit: this is a modest insight. The documentation guide above already says the EOB helps prove no double-dipping, so the idea is more packaging than discovery.

## 8. Why now, and why this does not exist yet
- Why now: Devenir counts 41.7M HSA accounts and $174B at year-end 2025, with about 4.2M accounts holding invested dollars (roughly 10%) and invested assets up 33% in a year (https://www.devenir.com/hsa-assets-reach-nearly-174-billion-at-year-end-2025-as-investment-assets-rise-to-85-billion/). The shoebox strategy is spreading, and extraction costs about a cent a document.
- Why it partly exists already: HSA Tracker Pro lets users "attach receipts and EOB documents" and detects duplicates. What I could not find is any app that automatically pairs a bill with its EOB.
- The 2026 launch wave (most of about ten apps appeared this year) shows how cheap the build is, which is also the main threat.

## 9. Inspiration and derivation
- Parents: receipt-capture apps for expenses (Dext, Smart Receipts, Receipt Lens in the App Store) and HSA trackers (HSA Tracker, HSA Monster).
- Changed: target user (HSA holders, not bookkeepers); core job (decades-long substantiation with bill-EOB pairs, not monthly expense reporting); business model (annual or one-time consumer fee, not a per-seat subscription); channel (HSA and FIRE communities, not accountants).

## 10. Competition check
Queries run:
1. WebSearch: "HSA receipt storage app match EOB itemized bill reimburse yourself later shoebox method audit"
2. WebSearch (Product Hunt): "site:producthunt.com HSA receipts tracker"
3. WebSearch (YC directory): "site:ycombinator.com/companies HSA FSA receipts health savings account"
4. App Store, `scripts/app_reviews.py --find`: "HSA receipts", "HSA receipt tracker", "medical receipts vault"
5. WebSearch: "HSA custodian receipt vault upload store receipts HealthEquity Lively Fidelity Optum Bank reimburse yourself later documents stored indefinitely"
6. HN comment search "HSA receipts"; Reddit archive r/HSA (364 posts since 2026-05-01, regex receipts/EOB/app).

| Product | What it does | Price | How it differs |
|---|---|---|---|
| [HSA Tracker](https://hsatracker.org/) (Eric Rosenberg; page read 2026-10-31) | Photo, PDF or email-forward capture, reimbursable total, ZIP export, household splits; web, iOS, Android | "Free to start, $7 a year after that" | No EOB matching mentioned; sets the price floor |
| [HSA Tracker Pro](https://apps.apple.com/us/app/hsa-tracker-pro/id6759116912) (Good Steward Labs, 2026-03-27, 6 ratings) | "attach receipts and EOB documents", itemization, duplicate detection, eligibility checker, AI scan | Free app, Pro tier (price not seen) | Closest direct rival; attaches EOBs, automatic pairing not stated |
| [HSA Monster](https://apps.apple.com/us/app/hsa-monster-expense-tracker/id6757624949) (2026-02-23, 3 ratings) | On-device AI receipt scan, iCloud sync, family share | Free | Receipts only |
| [HSA Vault](https://apps.apple.com/us/app/hsa-vault-receipt-tracker/id6759198475) (Pensive Products, 2026-05-26, 4 ratings) | On-device AI scan, Pub 502 eligibility check | Free | No EOB handling stated |
| HSA Vault+ ([Reddit post](https://www.reddit.com/r/HSA/comments/1tvrj5m/), 2026-06-03) | Logs expenses, data kept in the user's Google Drive | "$4.99, one-time, no subscription" | Price anchor |
| Stowe ([Reddit post](https://www.reddit.com/r/HSA/comments/1t2nrbs/), 2026-05-03) and Avows ([HN](https://news.ycombinator.com/item?id=48113083), 2026-05-12) | Free local desktop app; browser app that classifies with Gemini against Pub 502 | Free | Privacy-first hobby projects |
| [ExpenseTracker by HSA Store](https://apps.apple.com/us/app/expensetracker-by-hsa-store/id6528121942) (2024-10-29, 12 ratings, 3.3) | Scans connected store purchase history for eligible items | Free | Retail-purchase angle |
| [Burst](https://pulse2.com/burst-3-million-raised-for-hsa-fsa-reimbursement-platform-and-rebrand/amp/), [Silver](https://chromewebstore.google.com/detail/geopmmjhgiigoelgcgnpcfmblameojce), [Flex](https://www.ycombinator.com/companies/flex) (YC S23), [Veryfi](https://www.veryfi.com/document/hsa-hcsa-fsa-receipt/) | Claims filing, merchant payments, OCR API | n/a | Adjacent jobs, not an archive |
| Custodians: [Fidelity Health](https://apps.apple.com/us/app/fidelity-health/id1508025073), [HealthEquity EZ Receipts](https://apps.apple.com/us/app/ez-receipts/id412650768) (FSA/HRA/commuter), [Further](https://learn.hellofurther.com/Individuals/Spending_Your_Account/Maintaining_Documentation_for_Eligible_Expenses) | Receipt upload and storage inside the account (an [r/HSA user uploads receipts in the Fidelity app](https://www.reddit.com/r/HSA/comments/1t4pxi4/), 2026-05-05) | Free | No bill-EOB pairing seen; HealthEquity and Lively HSA vault limits not verified |
| ChatGPT, Claude, Gemini | Read receipt photos and build a spreadsheet on request | In subscription | No durable multi-year vault |

Classification: **WEAK DIRECT**. Roughly ten direct trackers, all tiny (0 to 12 App Store ratings), free or under $7 a year, none funded; the pairing wedge is partly covered. Kill criterion 1 is close: free alternatives with no clear defensible wedge.

Platform risk: custodians (Fidelity, HealthEquity, Lively, Optum) are the vertical incumbents and could add EOB attachment or AI pairing within 12 months, though a vault is a retention feature for them, not a revenue line. Frontier labs do one-off extraction but have no durable vault; low risk. Per the rubric, Scale and defensibility stays at 2 and Whitespace at 2.

## 11. Business model
- Payer: the HSA holder. Price: free up to 25 documents, then $19/year; $49 one-time backlog import plus audit binder for people about to withdraw. Anchors: $7/year (HSA Tracker), $4.99 once (HSA Vault+), free (most others, custodians).
- Model cost per active user per month [ESTIMATE], steady state: 40 new documents a year, about 3.3 a month. Per document: OCR 2 pages x $0.004 = $0.008; Haiku 5.5 extraction 3,000 in x $0.10/1M + 500 out x $0.50/1M = $0.00055; a Sonnet 5.5 pairing call on half of documents, 8,000 in x $2/1M + 800 out x $10/1M = $0.024, so $0.012 averaged. Total $0.0206 per document x 3.3 = $0.068, plus 5 chat calls on Haiku ($0.003) = about $0.07 a month, or $0.8 a year.
- One-time backlog [ESTIMATE]: 250 documents x $0.0206 = $5.2. Storage of 250 MB is negligible [ASSUMPTION: about $0.02/GB-month].
- Gross margin [ESTIMATE]: $19/year less Stripe fee ($0.55 + $0.30 = $0.85) less $0.8 model less $0.1 storage = $17.25, about 90%. Backlog pack: $49 - $1.72 fee - $5.2 model = $42.1, about 86%.

## 12. Market size
- Target buyers [ESTIMATE]: 41.7M HSA accounts (Devenir, year-end 2025); about 4.2M hold invested balances, a proxy for long-horizon holders. Assume 30% of those run deferred reimbursement and keep receipts [ASSUMPTION; no census exists] = 1.26M.
- Revenue: 1.26M x $19 = $24M a year if everyone paid. Realistic penetration of 5% = 63K users x $19 = $1.2M ARR, plus backlog packs: assume 3% of the 1.26M reach retirement each year (38K) and 10% of them buy at $49 = $0.19M.
- Reading: a $1M to $1.5M a year niche business unless a broader audience pays. It is a lifestyle product, not a venture-scale one.

## 13. Go-to-market
- First 100 customers: (1) answer deferred-reimbursement threads in r/HSA, Bogleheads and FIRE forums with a free checklist and a free backlog scan, about 40 users; (2) SEO on queries that appear in the threads ("can I use an EOB as an HSA receipt", "how to organize HSA receipts for 20 years", "HSA audit documentation"), about 40; (3) personal-finance newsletters and the White Coat Investor audience, about 20.
- Caution: r/HSA already has several builders posting their apps, so promotion must lead with the free backlog scan and the pairing demo.
- Growth loop: weak. A spouse invite and a yearly "reimbursable balance" email are the only loops; content and SEO carry the load.

## 14. Moat and scale path
- Moat: switching cost of a decade of paired documents, plus a corrections dataset for EOB and bill formats. Both are modest and the user can export everything.
- Scale path: add FSA, HRA and dependent-care receipts, medical-expense itemizing, long-term-care insurance claim files; white-label to custodians (a partnership, so not a launch dependency).

## 15. Solo feasibility
- MVP (4 weeks): inbound email and upload, OCR and extraction, rules plus LLM pairing, ledger, Pub 502 eligibility check, duplicate detection, ZIP and PDF binder export. No bank links.
- Weeks: 4. Running cost before revenue: about $40 to $60 a month (hosting, storage, a few dollars of model calls, inbound email, domain).
- Hardest risk: pairing accuracy across messy bills and EOBs, followed by the trust problem of holding sensitive health documents and promising decades of access. Mitigation: user-owned export and optional sync to the user's own drive. State consumer-health-data privacy rules need checking [UNVERIFIED].

## 16. Pre-mortem
1. Nobody pays: custodians and $0 to $7 apps are good enough, and the price floor kills revenue.
2. Pairing is not what holders want: audits are rare (the LIFE-10 poster says so), a folder and a spreadsheet feel sufficient, and the pain peaks only at withdrawal.
3. Trust and longevity: a one-person company asking to hold 20 years of medical records; one breach or shutdown ends it.

## 17. Cheapest validation test
- What: a one-page site and a concierge backlog import. Recruit 15 people with 100+ bills from r/HSA and Bogleheads; process each pile with scripts plus manual review for a $29 pre-payment; measure first-pass auto-pairing.
- Cost: about $60 and 15 hours. Duration: 2 weeks.
- Pass: at least 5 of 15 pre-pay and first-pass pairing is at least 70% correct. Fail: fewer than 2 pay or pairing is below 50%; then kill or fold the pairing engine into a broader life-admin vault.

## 18. Open questions
- Will anyone pay more than about $7 a year for pairing, or only once at withdrawal time?
- Do HealthEquity, Lively or Optum already accept EOBs and show pairs? [UNVERIFIED]
- What do tax professionals say counts as adequate substantiation? The product must stay on the organization side of the line and say it is not tax advice.
- Is the right buyer the person about to withdraw, making this a service-like one-time pack?
- Do the same pairing and EOB-reading components serve 007 Parent Mail Desk and 009 Bill Detective, so that this should be a module rather than a product?
