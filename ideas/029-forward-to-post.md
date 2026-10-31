---
id: "029"
slug: forward-to-post
name: Forward-to-Post
one_liner: "Forward receipts, invoices and work orders; they post to the right record in your existing software and learn corrections."
target_user: "Owners of one-to-ten person businesses on QuickBooks, Xero, Jobber, Buildium or Vagaro who re-key receipts and work orders"
form_factor: "other"
lens: "Interaction shift"
frontier: false
competition: "CROWDED"
confidence: "MED"
status: "developed"
signals: [REV-17, REV-01, REV-18, REV-23, REV-30]
scores:
  pain: 3
  evidence: 3
  ai_leverage: 3
  whitespace: 1
  novelty: 2
  why_now: 3
  solo_feasibility: 3
  distribution: 3
  wtp_economics: 3
  scale_defensibility: 2
total: 52.6
price_hypothesis: "$29/month per business"
model_cost_per_user_month: "$0.25"
gross_margin: "90%"
mvp_weeks: 7
deep_dive: false
red_team: false
---

# Forward-to-Post

## 1. One-liner
Forward receipts, invoices and work orders; they post to the right record in your existing software and learn corrections.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Re-keying costs "hours extra per week" for one Vagaro user (REV-30) and led a landlord to build his own agent (REV-17); frequent but small per item, with cheap partial fixes. |
| Evidence quality | 2 | 3 | Five recent signals, three strong, from app reviews and one Reddit thread; none states willingness to pay. |
| AI leverage | 2 | 3 | Reading a receipt is a solved task; the value is routing to the right record and learning from corrections. |
| Whitespace | 2 | 1 | Dext, Hubdoc, Receiptor AI, Tailride, Receipt Bot, Inbox Ledger and Tofu already forward and post to QuickBooks and Xero, some claiming learning; the vertical-records slice has only Carly and DIY automations. |
| Novelty of insight | 1 | 2 | "Correction memory is the product" is claimed by rivals; the vertical-records angle is a twist. |
| Why now | 1 | 3 | Models make any-document-to-any-record mapping cheap; the forwarding pattern itself is not new (Dext and Hubdoc do it). |
| Solo feasibility | 2 | 3 | One or two targets fit in about 7 weeks; every added integration is a new API and review. |
| Distribution | 2 | 3 | App stores and communities exist but are saturated; search is dominated by Dext and Hubdoc. |
| Willingness to pay and unit economics | 2 | 3 | $29/month sits near Dext and above Hubdoc, at 90% margin; Xero bundles capture, which compresses price. |
| Scale and defensibility | 2 | 2 | Integration breadth and a corrections dataset give some lock-in, but Intuit, Xero and automation tools can match features. |
| **Total** | | **52.6** | |

Confidence: MED. FRONTIER: no.

## 3. The problem
- Who: owners and office managers of tiny service, property and retail businesses whose system of record is QuickBooks, Xero, Jobber, Buildium or Vagaro, and who handle receipts, vendor invoices, work orders and intake forms by hand.
- How often: daily to weekly. A rough load is 120 documents a month (80 receipts, 25 invoices, 10 work orders, 5 forms) [ASSUMPTION].
- What goes wrong: expenses are typed in again even after a Home Depot sync (REV-01), a receipt photo creates a duplicate instead of matching the bank line (REV-23), intake form answers do not reach the client profile (REV-30), and built-in AI overrides the user's categorization (REV-18).
- Workaround today: manual entry, a receipt-capture app that only feeds the ledger, Zapier-style flows, or a home-built agent (REV-17).

## 4. Evidence
Five signals, all 2026 (full rows in `research/SIGNALS.md`):
- REV-17 (strong, 2026-10-26): "I created one for my own Builidium setup. now I can Email the agent a HomeDepot receipt and say "put it in this work order" ." Shows: a landlord on Buildium built an email-driven agent to post receipts to work orders and leases to tenant records; the DIY signal is the strongest demand evidence. https://www.reddit.com/r/PropertyManagement/comments/1xdgsz7/
- REV-30 (strong, 2026-10-02): "there are so many things you have to do to work around their errors that I spend hours extra per week, either doing things manually or finding a workaround. Their forms don’t transfer into the client profile as they promised, so I have to go thru every client and determine what’s missing from their profile and add it, from their intake form." Shows: intake forms that fail to flow into profiles cost a salon user hours each week. https://apps.apple.com/us/app/id346778559
- REV-18 (strong, 2026-10-13): "The new AI integration makes doing expenses take almost twice as long, as it’s glitchy and tends to override when I correct the categorization." Shows: built-in AI categorization that overrides corrections, which is why correction memory matters. https://apps.apple.com/us/app/id584606479
- REV-01 (medium, 2026-09-25): "the Home Depot sync feature doesn’t matter when it comes to invoicing and still have to manually enter expenses." Shows: a Jobber user still keying job expenses by hand. https://apps.apple.com/us/app/id1014146758
- REV-23 (medium, 2026-07-15): "When you take a picture of a receipt it creates a new transaction. I was hoping it would ask me to match the receipt to an already existing transaction so that I don’t have doubles." Shows: receipt capture that duplicates instead of matching. https://apps.apple.com/us/app/id881629660
- New evidence (not in SIGNALS.md), Jobber Community, date n/a (title only): "Building custom AI agents to automate tasks in Jobber" Shows: Jobber users are building their own agents. https://community.getjobber.com/discussions/operations-forum/building-custom-ai-agents-to-automate-tasks-in-jobber/9461

## 5. The product
- Outcome: every business gets an email address and a WhatsApp number; whatever is forwarded or photographed lands in the right record of the software they already use, with the attachment, and the next similar item needs no touch.
- Core AI loop: input (forwarded email, PDF, photo, voice note; the target system's chart of accounts, jobs, work orders, vendors) -> the model classifies the document, extracts fields, picks the target record (which work order, job, vendor bill or client profile) and a confidence score -> output: a record created or updated through the official API, plus a reply ("posted to work order 1042, Plumbing, $86.40") -> feedback: every correction becomes a per-vendor, per-category or per-property rule that is applied first next time; low-confidence items wait in a review queue.
- Interaction model: email, WhatsApp and a web inbox for exceptions; no new app to open daily.
- Form factor: an email and WhatsApp address with a web dashboard (other).
- Day in the life: a self-managing landlord with 14 units forwards a Home Depot receipt from the truck and types "kitchen sink, unit 6". The system matches work order 1042, attaches the receipt, books the cost to the unit's owner ledger and replies. When he corrects the category once, the rule applies to the next Home Depot receipt.

## 6. Why the LLM is load-bearing
- Documents arrive in any layout and language, with handwritten notes and chat context; picking the right work order or job from a loose description is reasoning over records.
- Plain-language corrections ("always code Lowe's to Repairs") become rules without forms.
- Without the model it is OCR plus fixed templates and forwarding rules, which is what capture apps were in 2018.

## 7. The insight
Users want their existing system to be correct, not another app, and correction memory is the product. Honest note: that exact claim is on competitor pages (Receiptor AI lists a Memory feature; Tofu says it learns from past transactions); the open part is the vertical records beyond accounting.

## 8. Why now, and why this does not exist yet
- Why now: vision models read arbitrary documents for a fraction of a cent, official APIs exist for most small-business systems, and WhatsApp is how many owners already send things.
- It exists for accounting. Receiptor AI, Dext, Hubdoc, Tailride, Receipt Bot, Inbox Ledger, BillBjorn and Tofu all forward or watch inboxes and post to QuickBooks or Xero. Intuit's agent now verifies receipts, and Xero's JAX reconciles with a "memory" method.
- Less served: posting into vertical records (work orders, job costs, client profiles). I found Carly (an AI agent with its own email address for Jobber) and DIY automations, but no product that does it across Buildium, Jobber and Vagaro with correction memory.

## 9. Inspiration and derivation
- Parents: Dext and Hubdoc (forward to a ledger), expense-capture apps, and email-to-record agents such as Carly.
- Changed: target record (vertical software, not only the ledger), interaction model (a forwarding address plus WhatsApp reply instead of an app), and the learning loop (corrections as rules the user can read). The target user and channel are mostly the same as the capture apps'.

## 10. Competition check
Queries run (2026-10-31):
1. Web: "forward receipts and invoices by email or WhatsApp to bookkeeping software AI extracts and posts learns corrections"
2. Product Hunt: "site:producthunt.com forward receipts invoices email WhatsApp AI bookkeeping auto-post"
3. YC: "site:ycombinator.com/companies receipts invoices email inbox AI data entry accounting system of record small business" (no YC pages returned)
4. Xero and QuickBooks stores and pricing: "Dext Hubdoc Expensify receipt capture email forward QuickBooks Xero pricing 2026 per month"
5. Vertical angle: "AI agent email receipt attach to work order Buildium AppFolio Jobber Housecall Pro automatic data entry property management"; plus the shared platform searches (Claude for Small Business, Intuit Assist, Xero JAX) and an Apple App Store lookup ("receipt scanner bookkeeping QuickBooks") that errored and was not retried.

Findings:
- [Receiptor AI](https://www.producthunt.com/p/receiptor-ai/from-inbox-chaos-to-hands-free-bookkeeping-receiptor-ai-is-live) (also on the [Xero App Store](https://apps.xero.com/us/app/receiptor-ai)): finds receipts in the inbox (retroactive and real time) and in WhatsApp, extracts and categorizes, syncs to Xero and QuickBooks, rules engine; 14-day trial; 5.0 rating from a single review. Requires inbox access.
- [Dext](https://www.capterra.com/compare/160189-165724/Dext-vs-Hubdoc) and Hubdoc: the incumbents. Third-party figures: Dext about $25.21/month in the US billed annually for 5 users and 250 documents ([SparkReceipt](https://sparkreceipt.com/alternative-to/hubdoc/)); Hubdoc about $12 ([Capterra](https://www.capterra.com/p/165724/Hubdoc/pricing/)) to $20 per month; one source says Xero US plans include capture at no extra cost. Prices conflict across sites.
- [Tailride](https://tailride.so/blog/capture-invoices-whatsapp-telegram): WhatsApp or Telegram receipts pushed to QuickBooks, Xero and others, with plain-language rules. [Receipt Bot](https://www.everydev.ai/tools/receipt-bot): email forwarding, web, app or API intake, exports to QuickBooks, Xero, Sage, Excel. [Inbox Ledger](https://peerlist.io/inboxledger/project/inbox-ledger): read-only Gmail, Outlook or IMAP detection of invoices. [BillBjorn](https://www.g2.com/products/billbjorn/discuss): central inbox with OCR export. Tofu, per the Xero [AI apps for bills and expenses](https://apps.xero.com/ie/collection/ai-apps-for-bills-expenses) collection: posts invoices to Xero and says it learns from past transactions.
- Vertical records: [Carly](https://www.usecarly.com/blog/best-ai-automation-tools-jobber/), an AI agent with its own email address that reads client email and creates or looks up Jobber records (per a search summary; receipts and attachments not mentioned); [Pipedream's Gmail-to-Jobber automations](https://pipedream.com/apps/gmail/integrations/jobber) for custom flows.
- Platform: Intuit's [Accounting Agent](https://quickbooks.intuit.com/learn-support/en-global/help-article/bank-transactions/learn-accounting-agent-features/L6pl9rv94_ROW_en) says it "helps automatically verify the right receipts are uploaded" and offers ready-to-post groups; Xero's [JAX](https://www.xero.com/campaign/auto-bank-reconciliation/) uses a Memory method; Claude for Small Business connects to QuickBooks ([TechInformed](https://techinformed.com/anthropic-brings-claude-workflows-to-small-businesses/)).

Classification: CROWDED. At least seven products already forward or watch inboxes and post to QuickBooks or Xero, two incumbents bundle capture, and the accounting-agent vendors are adding it natively. A sharper wedge would be one vertical, such as landlords' receipts into Buildium work orders (REV-17), where competition is Carly-style agents and DIY flows.

Platform risk: high. Intuit and Xero are the vertical incumbents for the ledger and are adding receipt verification and memory; Anthropic's connectors, Zapier-style tools and general agents can do forward-to-post for any system with an API. I expect ledger-side forward-and-post to be a native feature within 12 months, which caps Whitespace at 1 and leaves Scale at 2 only because vertical systems (Buildium, Jobber, Vagaro) are not the labs' priority.

## 11. Business model
- Payer: the business owner, monthly; accountants and property managers as resellers.
- Price hypothesis: $29/month per business [ASSUMPTION]. Anchors: Dext about $25 and Hubdoc about $12 to $20 (third-party figures above); owners pay $300 to $800 a month for bookkeeping (PRO-105, weak), so a $29 tool that removes data entry is a small line item.
- Model cost per business per month [ESTIMATE] (120 documents; prices from `research/LANDSCAPE.md` section 6):
  - First pass on Haiku 5.5 (1,900 fresh in x $0.10 + 3,000 cached x $0.01 + 250 out x $0.50) / 1M = $0.000345, x 1.3 tokenizer overhead = $0.00045 per document, x 120 = $0.054.
  - 15% (18 documents) escalated to Sonnet 5.5: (3,000 cached x $0.10 + 3,000 fresh x $2 + 400 out x $10) / 1M = $0.0103 x 18 = $0.185.
  - Correction rules: 20 corrections x $0.0005 = $0.01.
  - Total model cost about $0.25.
- Other variable cost [ASSUMPTION]: inbound email 120 x $0.001 = $0.12; WhatsApp 60 messages x $0.005 = $0.30 (user-initiated replies may be free, UNVERIFIED); storage $0.02; hosting $1.00; card fees on $29 = 2.9% + $0.30 = $1.14.
- Gross margin: ($29 - 0.25 - 0.44 - 1.00 - 1.14) / $29 = 90.2%, about 90%.

## 12. Market size
- [ESTIMATE] Target buyers: about 1,000,000 micro businesses on QuickBooks, Xero, Jobber, Buildium or Vagaro that handle 50 or more documents a month (assumption, UNVERIFIED; validate with each vendor's public subscriber counts).
- 1,000,000 x $29 x 12 = $348M a year at full share. At 0.5% penetration = 5,000 businesses = $1.74M ARR. Price pressure from bundled capture argues against more.

## 13. Go-to-market
- Channel: the Xero and QuickBooks app stores (Receiptor AI shows an "AI apps for bills and expenses" shelf on Xero), Jobber and Buildium marketplaces, r/PropertyManagement (the REV-17 thread), r/QuickBooks and r/smallbusiness.
- Narrow first wedge: self-managing landlords on Buildium or DoorLoop, then trades on Jobber (REV-01). First 100: 40 landlords through concierge setup in r/PropertyManagement and BiggerPockets; 30 from app-store listings; 30 through accountants who give each client a forwarding address.
- SEO queries: "forward receipts to QuickBooks", "email receipts to Xero", "WhatsApp receipt to QuickBooks", "attach receipt to work order Buildium".
- Growth loop: accountants and property managers hand each client an address; owners tell peers. Modest.

## 14. Moat and scale path
- Moat candidates: a corrections dataset per vertical (vendor-to-category and vendor-to-property priors), integration depth in vertical systems, and workflow habit (the address stays the same while the target software changes).
- Scale path: landlords, then trades, then salons and clinics; then sell the routing layer to software vendors that lack their own AI front door. Ledger-only capture is a lost position.

## 15. Solo feasibility
- MVP (7 weeks): inbound email domain, WhatsApp Business Cloud API number, extraction pipeline, two targets (QuickBooks Online plus Buildium or Jobber), correction memory as a rules table, review queue, audit log, reply messages.
- Running cost before revenue: about $90/month (hosting $25, database $15, WhatsApp and email $20, model tests $20, domain and monitoring $10) [ESTIMATE].
- Hardest technical risk: write-back through official APIs (can Buildium attach a file to a work order; can Jobber create an expense?) [UNVERIFIED]. Second: WhatsApp Business onboarding and its policy on automated messaging [UNVERIFIED]. Third: wrong-record posting erodes trust faster than manual entry.

## 16. Pre-mortem
1. Crowded and bundled: Dext, Hubdoc and a dozen AI capture apps plus Intuit and Xero's own features leave no room in accounting.
2. Integration treadmill: every new target needs an API, review and upkeep; the vertical APIs may not allow what the use case needs.
3. Trust: a receipt posted to the wrong work order or owner ledger causes real accounting errors; users revert to manual entry.

## 17. Cheapest validation test
- Concierge test with 10 landlords or trade owners: for two weeks they forward real receipts to the founder's inbox; a Claude script posts them through the API (or a sandbox) and the founder sends the confirmation reply.
- Cost: about $20 and 15 hours; duration 3 weeks.
- Pass: at least 85% of week-two items post correctly after the stored corrections, and at least 5 of 10 say they would pay $29/month. Fail: under 70% correct, or fewer than 3 would pay.

## 18. Open questions
- Recommendation: narrow to one vertical (landlord receipts into Buildium or DoorLoop work orders) or kill; the accounting-capture version is CROWDED.
- Which vertical APIs allow attachments, expenses and work-order writes?
- Does correction memory beat Receiptor AI's Memory and Tofu's learning, or is it table stakes?
- Is WhatsApp worth the policy risk, or is email enough for the wedge?
