---
id: "040"
slug: payee-shield
name: Payee Shield
one_liner: "Inbox add-on and payment checkpoint that catches vendor bank-detail changes and runs an independent callback before money moves."
target_user: "Bookkeepers and MSPs protecting small companies (5 to 50 seats) that pay vendors by ACH or wire"
form_factor: "plugin"
lens: "Second-order AI"
frontier: false
competition: "CROWDED"
confidence: "LOW"
status: "killed"
signals: [GAP-43, GAP-44, GAP-45, GAP-46, AI2-46, AI2-45]
scores:
  pain: 3
  evidence: 3
  ai_leverage: 3
  whitespace: 2
  novelty: 2
  why_now: 4
  solo_feasibility: 2
  distribution: 3
  wtp_economics: 3
  scale_defensibility: 2
total: 53.7
price_hypothesis: "$39/month per protected company; bookkeeper and MSP plan $19 per client per month for 10+ clients"
model_cost_per_user_month: "$1.17 (300 emails scanned, 4 voice callbacks)"
gross_margin: "93%"
mvp_weeks: 8
deep_dive: false
red_team: false
---

# Payee Shield

> **Main-thread review, 2026-10-31: KILLED.** CROWDED. Eftsure, Trustpair and Trustmi verify payees, Bill.com confirms bank-detail changes, and the Federal Reserve plans payee-name verification; a solo startup also faces a trust wall for mailbox access. Nacha's 2026 fraud-monitoring rule is the one tailwind. The file is kept as a record of the competition check.

## 1. One-liner
Inbox add-on and payment checkpoint that catches vendor bank-detail changes and runs an independent callback before money moves.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | One hit costs $15K to about $180K (GAP-43, GAP-45), but any single small company is hit rarely; the cost is a tail risk, not a weekly chore. |
| Evidence quality | 2 | 3 | Three strong signals (a $15K consumer wire, an MSP with two missed incidents, FBI AI-related loss figures) but no small-business owner saying they would pay; GAP-46 and AI2-46 are weak. |
| AI leverage | 2 | 3 | Reading threads and running the callback are model work; lookalike-domain checks and vendor-master comparison are deterministic and already sold. |
| Whitespace | 2 | 2 | Eftsure, Trustpair and Trustmi are funded direct rivals, Bill.com has a built-in confirmation step; the bookkeeper and MSP lane at small-company prices looks unserved but is unproven. |
| Novelty of insight | 1 | 2 | "The callback is the defense" is bank boilerplate; an agent that always performs it from independent contact data is a modest twist. |
| Why now | 1 | 4 | Nacha's fraud-monitoring rule reached all non-consumer originators on 2026-06-22, AI-assisted fraud is rising, and voice agents cost about $0.05 a minute. |
| Solo feasibility | 2 | 2 | Reading finance email needs heavy trust and security work; payments cannot be frozen in every AP system; voice calling adds compliance questions. |
| Distribution | 2 | 3 | MSP and bookkeeper communities and add-in stores are reachable, but both groups are skeptical of unknown vendors with inbox access. |
| Willingness to pay and unit economics | 2 | 3 | Clear payer and 93% margin with a loss-avoidance story, but no verified small-company price anchor. |
| Scale and defensibility | 2 | 2 | A shared registry of verified payee details would be a real network moat, but banks, Fed tools and AP platforms can absorb the control. |
| **Total** | | **53.7** | |

Confidence: LOW (the bookkeeper and MSP buying behavior is untested). FRONTIER: no.

## 3. The problem
- Who: owners and bookkeepers at small companies, and the MSPs that secure their Microsoft 365 tenants, where an impersonator slips into a real invoice thread and swaps bank details.
- How often: rare per company, frequent across the base. Three-quarters of organizations reported attempted or actual payments fraud in 2025 in a survey figure quoted by Corpay (secondary, UNVERIFIED).
- What it costs: a $15K wire (GAP-43), $38K through a lookalike accountant domain (same thread), about $180,000 for a California business that changed a vendor's bank details on request (GAP-45).
- Workaround today: manual callbacks, which are inconsistently applied and skipped under pressure (Kognitos, search summary) or fail when the number comes from the email itself (Stampli, search summary), plus email filters and identity-threat tools that missed two incidents at one MSP's clients (GAP-44).

## 4. Evidence
Six cited signals (full rows in `research/SIGNALS.md`):
- GAP-44 (strong, 2026-09-29): "Today we had another BEC at a different client, again with ITDR in place, and again no detection." Shows: an MSP serving 5 to 50 seat Microsoft 365 clients, two incidents two years apart despite a managed identity-threat product; the thread has 183 comments. https://www.reddit.com/r/msp/comments/1wtlxo1/
- GAP-43 (strong, 2026-10-27): "I paid my catering / rentals invoice over a week ago. And today I discovered I was the victim of a BEC - business email compromise." Shows: a months-long invoice thread hijacked, about $15K wired; a commenter lost $38K the same way (629 points, 247 comments; the poster is a consumer, not a company). https://www.reddit.com/r/Scams/comments/1xgduji/
- GAP-45 (medium, 2025-06-06, news report): "Police said the business took a loss of approximately $180,000." Shows: a vendor impersonator asked a Fremont business to change the vendor's bank details. https://www.yahoo.com/news/vendor-fraudsters-scammed-fremont-business-193628376.html
- AI2-45 (strong, 2026-04-07): "These AI-related complaints reported losses of $893 million, the agency said." Shows: FBI logged 22,364 AI-related complaints in 2025, including business email compromise. https://www.pymnts.com/cybersecurity/2026/fbi-flags-893-million-in-ai-driven-scams/
- GAP-46 (weak, 2026-10-26): "Anyone here been hit with a vendor bank-change scam? What tipped you off?" Shows: a bookkeeper lists callback and second-approval controls; only one reply, so it reads like engagement, not a victim report. https://www.reddit.com/r/bookkeeping/comments/1xfwvhz/
- AI2-46 (weak, 2026-07-15): "The finance employee saw and heard his superiors in what appeared to be a normal conference situation." Shows: deepfake executive calls target finance staff (second-hand, widely reported case). https://news.ycombinator.com/item?id=48923956
- New evidence (not in SIGNALS.md), a rule fact read on Nacha's page: the Phase 2 fraud-monitoring rule requires "risk-based processes and procedures" aimed at entries "suspected of being unauthorized or authorized under False Pretenses", reviewed "at least annually", effective 2026-06-19 (practically 2026-06-22) for all non-consumer originators regardless of volume. https://www.nacha.org/rules/risk-management-topics-fraud-monitoring-phase-2
- Caution: the sample found no small-business owner or bookkeeper reporting a loss in about 3,000 posts of the gap-fill track; the loudest victim was a consumer.

## 5. The product
- Outcome: no payment goes out to changed bank details without an independent confirmation, and every confirmation leaves an evidence record.
- Core AI loop: input (read-only access to the mailbox or a forwarded-mail address, the vendor list from QuickBooks Online, Xero or Bill.com, the original W-9 or contract phone number) -> the model reads invoice threads, flags payment-detail changes, urgency language, tone shifts, reply-chain hijacks and lookalike or new domains, and compares the new details with the vendor record -> output: a hold request on the bill (task to the approver; an actual payment hold only where the AP system's API allows), an independent verification (voice callback to the number on file, or a confirmation link sent to a contact from the vendor record), and a one-page evidence log -> feedback: the approver marks the case real or false, and the vendor's verified details are stored for next time.
- Interaction model: Outlook and Gmail add-on plus a small web console for the bookkeeper or MSP, with a client list and monthly report.
- Form factor: plugin (mail add-on) with a web app.
- Day in the life: a 12-person remodeler's bookkeeper gets a note, in a real thread, that "ABC Lumber has changed banks". The add-on flags a sender domain two letters off, registered nine days ago, with details that differ from QuickBooks. It starts a callback to the number on the vendor's W-9; the vendor says nothing changed. The bill is marked held, and the log goes to the owner and to the bank if needed.

## 6. Why the LLM is load-bearing
- Reading a 40-message thread for a quiet change of payment instructions, a shifted tone or a hijacked reply chain is a language task; keyword rules miss it.
- The callback conversation (gatekeepers, voicemail, refusal, a read-back of account digits) needs a voice agent and judgment.
- Without the model it is a lookalike-domain checker and a task list, which email security tools already ship.

## 7. The insight
BEC beats filters because the email is real or nearly real; the defense is a process at the moment of payment (GAP-44: detection failed twice with a security product in place). The process fails in practice because it is skipped under pressure or run against numbers taken from the suspicious email. An agent that always runs it, from independent contact data, and logs it, fixes the human failure. Honest note: this is a process-compliance product, and banks and AP platforms are moving into the same step.

## 8. Why now, and why this does not exist yet
- Why now: Nacha's Phase 2 rule applies from 2026-06-22 to all non-consumer originators and demands documented, risk-based fraud monitoring that covers False Pretenses (it adds no duty to monitor before processing and does not change liability); AI-assisted fraud complaints are growing (AI2-45); realtime voice costs about $0.05 a minute.
- It partly exists: see section 10. Enterprise tools verify payees; the gap is the small company reached through a bookkeeper or MSP.
- Why it may stay open: security vendors prefer enterprise deals, and small-company buyers rarely pay for tail-risk tools until they are hit.

## 9. Inspiration and derivation
- Parents: Eftsure and Trustpair (payee verification networks), Trustmi (payment security), Bill.com's vendor bank-change confirmation, email security tools such as Abnormal, bank callback guidance.
- Changed: target user (bookkeepers and MSPs for small clients, not enterprise AP), core job (enforce the callback and keep evidence, not only detect), interaction model (an agent that makes the call), business model (per-client pricing through partners).

## 10. Competition check
Queries run (2026-10-31):
1. Web: "Eftsure Trustmi Trustpair vendor bank account verification pricing small business bookkeepers MSP vendor bank detail change fraud"
2. Regulation: "Nacha 2026 rules fraud monitoring false pretenses ACH originators June 2026 phase vendor impersonation business email compromise requirement" and a read of [Nacha's Phase 2 page](https://www.nacha.org/rules/risk-management-topics-fraud-monitoring-phase-2)
3. Product Hunt: "site:producthunt.com business email compromise vendor bank change invoice fraud verification callback" (no Product Hunt pages)
4. YC: "site:ycombinator.com/companies vendor payment fraud bank account change verification accounts payable BEC" (no YC pages)
5. AP store and platforms: "Bill.com QuickBooks Bill Pay vendor bank account change verification fraud protection small business Outlook add-in invoice fraud detection 2026"
6. Banks: "verification of payee United States banks 2026 confirmation of payee UK EU Instant Payments Regulation October 2025 US businesses ACH wire no payee name check"
7. Funding: "Trustmi raises Series funding B2B payment fraud prevention Eftsure raises funding vendor verification"

Findings:
- [Eftsure](https://www.eftsure.com/vendor-email-compromise/): verification network where an analyst calls the vendor and a bank-link option exists; says it serves all sizes; pricing is quote-based and, per a review site, scales with annual spend and new-vendor onboarding; 39 countries; backed by Level Equity ([Eftsure announcement](https://www.eftsure.com/blog/industry-news/eftsure-partners-with-level-equity/), amount not found); publishes a [Nacha 2026 explainer](https://www.eftsure.com/blog/industry-news/nachas-2026-fraud-monitoring-rules-what-every-finance-team-needs-to-know/).
- [Trustpair](https://trustpair.com/eftsure-alternative/): enterprise procure-to-pay with ERP connectors (SAP listing), "price available upon request", and a third-party review calls it less accessible to small businesses.
- Trustmi: [$17M Series A, TechCrunch 2023-07-26](https://techcrunch.com/2023/07/26/trustmi-lands-17m-to-scale-its-payments-fraud-prevention-tech); described as a Nacha Preferred Partner for fraud prevention and account validation (search summary); no small-business pricing found.
- PaymentWorks (supplier onboarding and payee verification, skews enterprise; see its [Nacha guide](https://www.paymentworks.com/?p=9099)); Corpay and Kognitos publish AP-control guides and sell AP automation.
- Bill.com: when a user changes a vendor's bank details, Bill emails the vendor to confirm; payments can still be scheduled before the vendor responds ([help page](https://support.wf.bill.com/hc/en-us/articles/360056648691)). I could not confirm what QuickBooks Bill Pay does.
- Detection stack: [Abnormal AI](https://abnormal.ai/ja/threat-intelligence/digest/vendor-impersonation-used-to-siphon-invoice-payments) tracks vendor impersonation in email; Huntress ITDR is the tool in GAP-44's thread; Microsoft and Google protections not checked.
- Bank guidance: JPMorgan treats the callback as the key control and publishes [why callbacks go wrong](https://www.jpmorgan.com/insights/cybersecurity/business-email-compromise/when-callbacks-go-wrong) (snippet only).
- Payee verification by banks: euro-area providers have had to offer verification of payee since October 2025 under the Instant Payments Regulation and the UK has Confirmation of Payee (a regulator fined Bank of Ireland UK over GBP 3.7M in February 2026 for not implementing it); in the US, the Federal Reserve announced a Payee Name Verification tool for 2026 ([PYMNTS](https://www.pymnts.com/?p=4265632), title and summary only). All from search summaries.

Classification: CROWDED at the category level. Three funded verification vendors and a mainstream AP platform cover payee verification. The small-company lane via bookkeepers and MSPs is not visibly served, but no one in the evidence has asked to pay for it.

Platform risk: high. Banks and the Federal Reserve (payee name checks), Bill.com or Intuit (making bank-change confirmation mandatory), Microsoft and Google (payment-change warnings in mail), and MSP stacks (Huntress, Abnormal) can each absorb part of the control; Eftsure or Trustpair can add a small-business tier. Caps Whitespace at 3 and Scale at 2.

## 11. Business model
- Payer: the bookkeeper or MSP (per client company); small companies directly through the add-in store.
- Price hypothesis: $39/month per protected company (3 users, 150 vendor payments), $19 per client per month for partners with 10+ clients. No verified price anchor: Eftsure and Trustpair are quote-only [UNVERIFIED]. The anchor is loss avoidance: $468 a year is about 3% of a $15K loss (GAP-43) [ESTIMATE: 468 / 15,000 = 3.1%].
- Model cost per protected company per month [ESTIMATE] (Haiku 5.5 $0.10 in / $0.50 out; Sonnet 5.5 $2.00 / $10.00; GPT Live $0.05/min; from `research/LANDSCAPE.md` section 6):
  - Email triage, 300 emails on Haiku 5.5, 2,000 in + 150 out: 300 x (2,000 x $0.10 + 150 x $0.50) / 1M = $0.0825.
  - Thread analysis, 10 flagged threads on Sonnet 5.5, 8,000 in + 800 out: 10 x (8,000 x $2 + 800 x $10) / 1M = $0.24.
  - Voice callbacks, 4 x 3 minutes x $0.05 = $0.60; telephony 12 minutes x $0.014 = $0.17 [ASSUMPTION: telephony is not in the price table].
  - Confirmation links by SMS or email, 10 x $0.008 = $0.08 [ASSUMPTION]; evidence summaries, 4 x $0.0005 = $0.002.
  - Total $1.17.
- Gross margin: ($39 - $1.17 - card fee $1.43) / $39 = 93.3%.

## 12. Market size
- [ASSUMPTION, no verified counts] 40,000 US MSPs plus 100,000 bookkeeping and accounting practices that handle payables for small clients = 140,000 partner firms; 1% sign up within two years = 1,400 firms x 15 protected companies x $19 x 12 = $4.8M ARR.
- Realistic solo share: 0.3% of firms = 420 firms x 15 x $19 x 12 = $1.44M ARR. A direct-to-company channel would add little because owners buy protection only after a loss.

## 13. Go-to-market
- First 100 customers: (1) 40 bookkeepers from r/bookkeeping, r/QuickBooks and ProAdvisor communities through a free "paste a bank-change email, get a verdict and callback script" web tool (no inbox access); (2) 30 MSPs from r/msp threads such as GAP-44, peer groups and a Microsoft AppSource add-in listing; (3) 30 through two or three MSP peer groups or cyber-insurance brokers who want evidence of callbacks.
- Growth loop: the vendors who confirm their bank details once become a shared verified-payee registry, and each confirmation request tells another small company about the service; this loop needs scale and consent from vendors.
- Timing: year-end and tax-season payment peaks; Nacha's annual review requirement gives a reason to buy each year.

## 14. Moat and scale path
- Candidates: a registry of vendor bank details verified across customers (Eftsure's moat); evidence logs that cyber insurers accept; MSP console lock-in.
- Scale path: add ACH and wire holds through bank and AP integrations, then payroll-redirect and executive-impersonation checks. Needs scale before the registry matters.

## 15. Solo feasibility
- MVP (8 weeks): Microsoft 365 add-in and mail read via Graph (admin consent), thread analysis, vendor record import from QuickBooks Online and Xero (read-only), alert and hold task, SMS or email confirmation link, a voice callback agent with call consent and AI disclosure, evidence log PDF, bookkeeper console.
- Running cost before revenue: about $110/month (hosting $30, database $20, model tests $20, telephony and voice tests $30, domain and email $10) [ESTIMATE].
- Hardest technical risk: trust and permissions. Finance buyers expect a security review (SOC 2 or similar) before granting mailbox access, Gmail restricted scopes may need an external security assessment [UNVERIFIED], and QuickBooks Bill Pay may not allow payment holds through any API [UNVERIFIED]. AI-voice outbound calls raise consent and disclosure questions (TCPA) that need a lawyer. A missed fraud creates liability, so the pitch must be "evidence and process", not a guarantee.

## 16. Pre-mortem
1. Trust wall: bookkeepers and MSPs will not give a solo founder's startup mailbox access to payables mail, and larger names (Eftsure, Abnormal, Microsoft) win the same buyers.
2. Absorption: payee name verification at banks, mandatory confirmation in AP platforms and mail warnings remove most of the gap within 12 to 24 months.
3. Low willingness to pay: small companies treat this as a tail risk and buy after a loss; the evidence has no one saying they would pay, and a false negative ends the business.

## 17. Cheapest validation test
- Two-part test. (a) Build a labeled set of 30 public BEC and vendor-impersonation threads plus 30 genuine bank-change threads (public examples or realistic synthetic ones) and measure detection with Claude. (b) Offer the no-integration "paste a thread, get a verdict, callback script and evidence record" web page to 10 bookkeepers and MSPs.
- Cost: about $25 of model spend and 25 hours; duration 3 weeks.
- Pass: recall at least 90% with false positives at most 10% on the labeled set; at least 6 of 10 testers use it on 3 or more real threads and at least 4 say they would pay $19 per client. Fail: recall below 80%, or fewer than 2 testers willing to pay.

## 18. Open questions
- Recommendation: do not build the inbox product first. Build only the no-integration verdict and callback-script tool as a lead magnet, and fold the checkpoint into a bookkeeping product (see 024 Books Second Opinion) if bookkeepers pay.
- Does a documented callback satisfy the Nacha Phase 2 requirement for small originators, and would cyber insurers value the evidence log?
- What do Eftsure and Trustmi charge a 20-person company, and do they sell through MSPs?
- Do AI voice callbacks to vendors need prior consent under the TCPA, and how do vendors react to an AI caller?
