---
id: "008"
slug: paper-trail
name: Paper Trail
one_liner: "Photograph an IRS or SSA notice; get the plain-English meaning, a drafted reply, tracked certified mail and escalation."
target_user: "Individuals and adult children handling IRS, SSA and state agency notices"
form_factor: "web app"
lens: "Pain-first"
frontier: false
competition: "WEAK DIRECT"
confidence: "MED"
status: "developed"
signals: [LIFE-27, LIFE-28, LIFE-29, LIFE-30, LIFE-31, LIFE-22, REV-45, REV-47, UND-30, LIFE-43]
scores:
  pain: 3
  evidence: 3
  ai_leverage: 3
  whitespace: 2
  novelty: 3
  why_now: 3
  solo_feasibility: 3
  distribution: 3
  wtp_economics: 2
  scale_defensibility: 2
total: 53.7
price_hypothesis: "$59 per notice case (one tracked certified letter included), $12 per extra letter"
model_cost_per_user_month: "$0.12 per case (about $12.50 of mail and print on top)"
gross_margin: "72%"
mvp_weeks: 6
deep_dive: true
red_team: true
---

# Paper Trail

## 1. One-liner
Photograph an IRS or SSA notice; get the plain-English meaning, a drafted reply, tracked certified mail and escalation.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Deadlines, unreachable phones and fear; people pay relief firms $2,000+; but any one person gets a notice rarely Calibrated 4 to 3: notices are infrequent per household and usually lower-stakes than a Medicaid or disaster case |
| Evidence quality | 2 | 3 | 10 recent signals across Reddit, App Store and HN, 4 strong; demand for the mailing and escalation layer is inferred Red team: 4 to 3, red team: signals show phone failure and fear; demand for mailing and escalation is inferred |
| AI leverage | 2 | 3 | Model reads notices and drafts replies; rules, mailing and escalation are not AI, and OweRight shows reading is a commodity |
| Whitespace | 2 | 2 | WEAK DIRECT: OweRight (8 days old) reads and drafts; I found nobody who mails, tracks and escalates for individuals Calibrated 3 to 2: OweRight (live 2026-10-23) reads about 150 notice types and drafts replies, and general assistants read notices well |
| Novelty of insight | 1 | 3 | Owning case state, proof of mailing and the escalation playbook is a useful twist, not a new category |
| Why now | 1 | 3 | Cheap vision reading and mail APIs, IRS phones unreachable in 2026; a version was buildable in 2024 |
| Solo feasibility | 2 | 3 | About 6 weeks with off-the-shelf APIs; the curated rules library is the real labour Red team: 4 to 3, red team: reviewed rules library, proof-of-mailing and Circular 230 questions |
| Distribution | 2 | 3 | Notice-code SEO and r/IRS style communities, but IRS, TurboTax and TaxAct pages hold the top results |
| Willingness to pay and unit economics | 2 | 2 | $59 against $2,000+ relief fees; postage caps margin near 72%; owners of small bills will not pay Red team: 3 to 2, red team: OweRight at $29.99 and the free IRS upload tool cap the price |
| Scale and defensibility | 2 | 2 | Episodic use; Intuit, H&R Block or the assistants can copy the explain-and-draft slice |
| **Total** | | **53.7** | |

Confidence: MED. FRONTIER: no.

Red-team adjustment (main researcher, 2026-11-01): evidence quality 4 to 3 (red team: signals show phone failure and fear; demand for mailing and escalation is inferred); willingness to pay and unit economics 3 to 2 (red team: OweRight at $29.99 and the free IRS upload tool cap the price); solo feasibility 4 to 3 (red team: reviewed rules library, proof-of-mailing and Circular 230 questions).

Calibration (main researcher, 2026-10-31): pain severity and frequency 4 to 3 (notices are infrequent per household and usually lower-stakes than a Medicaid or disaster case); whitespace 3 to 2 (OweRight (live 2026-10-23) reads about 150 notice types and drafts replies, and general assistants read notices well).

## 3. The problem
- Who: people who get an IRS, SSA or state notice and cannot reach a human, often an adult child handling a parent's mail (LIFE-27, LIFE-29).
- How often: one r/IRS thread drew 115 comments (LIFE-27) and one r/SocialSecurity thread 347 (LIFE-29). In my sample of 117 low-star reviews of the IRS app dated since 2025-05-01, 40 mention refunds, "under review", letters, notices or delays (REV-47, regex count).
- Cost: response windows are short (a blog summary puts a CP2000 reply at 30 days, [UNVERIFIED]) and silence becomes collections (LIFE-22). Tax-relief firms quote roughly $2,000 to $5,000 for resolution and some take only debts of $10,000+ (search summaries of comparison sites, [UNVERIFIED], https://www.bench.co/blog/tax-tips/tax-relief-companies).
- Workaround: hours on hold, asking a child, pasting the letter into ChatGPT or Claude (LIFE-43), paying a relief firm, or doing nothing out of fear (LIFE-31).

## 4. Evidence
Ten independent signals, all dated 2026-09 or 2026-10 (the oldest is 2026-09-09).
- **LIFE-27** (strong, 2026-10-22, r/IRS, 115 comments): "Due to the High Volume of Callers...we are never answering again! My Dad got a notice saying they have not processed his refund because his account # was not provided." Shows the phone route is closed and a child is doing the work.
- **LIFE-29** (strong, 2026-10-20, r/SocialSecurity, 347 comments): "I just got a notice on my online account that my payments are suspended because either my mailing address is wrong or my payment information is wrong." Shows SSA notices carry the same panic.
- **REV-47** (strong, 2026-10-01, App Store): "App just tells me my refund is delayed and hasn’t changed since April 1st." Shows the official app gives status but no next step.
- **LIFE-43** (strong, 2026-09-09, HN): "Ten unrelated fights (IRS penalties, a car warranty, two insurance denials, a robot mop, grocery stuff), yielded just over $12k back! The biggest single one was an IRS first-time penalty abatement I'd never heard of, $6.8k, eight years into an installment plan." Shows recoverable money, and that people already use a Claude agent for it (platform risk).
- **LIFE-31** (medium, 2026-10-21): "I want to pay it back but I am unsure how to get in touch with the IRS (I know that many are having this struggle). The bill is for roughly 17k." Weighing a relief firm.
- **LIFE-30** (medium, 2026-10-27): "For approximately SIX MONTHS, I’ve been stuck in an endless identity verification loop between ID.me and the IRS." Shows the need to escalate, not just reply.
- **LIFE-22** (medium, 2026-10-21): "In July, I sent a 1310 form to release his tax returns. Three months later, they sent me a letter denying my claim, stating I submitted it three years after the tax year which is false." Shows why proof of mailing matters.
- **LIFE-28** (medium, 2026-10-27) and **REV-45** (medium, 2026-10-28): hours on hold with an app that says nothing; a TurboTax customer who cannot get anyone to explain an IRS bill ("no phone or message area I can find to get help").
- **UND-30** (medium, 2026-10-29): a Korean pension-service notice due the next day: "Could someone help me?" Shows the second-language variant.

## 5. The product
- Finished outcome: the notice is understood, the right reply is sent with proof, and the case is followed until it closes or is escalated.
- Core AI loop: photo or PDF of the notice -> vision model extracts notice code, amount, tax year, deadline and quotes each fact from the page -> a human-curated rules library (notice code -> options the agency itself lists, forms, mailing address, escalation triggers) -> model drafts the reply from the user's facts and uploaded documents -> user approves and signs -> certified mail with return receipt through a print-and-mail API (or upload/fax where the notice allows) -> user photographs any agency reply -> model updates the case and the next action.
- Escalation packets when stuck: Taxpayer Advocate Service Form 911 and a congressional casework release, prepared for the user to sign and submit.
- Interaction: mobile-first web app, email and SMS reminders, family mode where an adult child manages a parent's case with the parent's consent.
- Day in the life: Dana photographs three pages of her father's CP2000. In a minute she sees the proposed adjustment, the tax year and a 30-day date, each quoted from the pages. She uploads his 1099 and return, approves a draft that disputes one line, pays $59, and gets the green-card scan when it arrives. At day 75 with no answer it offers the Form 911 packet.
- Liability line: it prepares, organizes, mails and tracks the user's own correspondence. It does not advise whether to agree or disagree, does not represent anyone before the IRS (no Form 2848 power of attorney), and does not prepare returns. It lists options the notice and agency publications state, the user chooses and signs. Levies, liens, audits, identity-theft flags and large balances show a referral to a CPA, enrolled agent, attorney or low-income taxpayer clinic.

## 6. Why the LLM is load-bearing
Notices come in about 150 types and many layouts, photographed at angles; the user's supporting documents are unstructured; the reply must cite their facts. A decision tree covers the top 20 codes only. The model does the reading, matching and drafting; the rules, mailing and escalation sit beside it as plain code and curated data, so remove the model and you get a form library, not a service.

## 7. The insight
The reply rarely needs a professional; it needs the right form, proof of mailing and persistence. The newest rival, OweRight, is stateless by design ("does not send or file anything for you", reminders stay on the phone), which leaves case state, mailing proof and escalation open. People fail at silence after sending (LIFE-27, LIFE-28, LIFE-30), not at understanding.

## 8. Why now, and why this does not exist yet
Vision models read photographed letters for a fraction of a cent, print-and-mail APIs start near $0.63 to $0.83 a letter (https://www.lob.com/pricing), and IRS phones are unreachable (LIFE-27). It does not exist for individuals because relief firms chase $10,000+ debts and professional tools (Canopy, NoticeNinja, CCH) sell to preparers. Honest caveat: consumer entrants are appearing now, so "does not exist" is weeks old.

## 9. Inspiration and derivation
Parents: tax-relief firms and audit-defense add-ons (human service), Canopy Notices and NoticeNinja (preparer tools), Lob-style mail APIs, DoNotPay-style letter generators. Changed: target user (individual or adult child, not preparer), business model (flat $59 instead of $2,000+), interaction (photo plus persistent case), channel (notice-code search pages and community answers).

## 10. Competition check
Queries run (2026-10-31): (1) web "AI app explains IRS notice and drafts response letter CP2000 CP504 taxpayer"; (2) Product Hunt via search, "site:producthunt.com IRS notice letter response" (no PH pages returned) and "IRS notice letter help AI" restricted to producthunt.com (TaxGPT, Jupid, Mezzi; no notice tool); (3) YC, "site:ycombinator.com/companies IRS tax notices resolution" and "tax notices IRS taxpayers" restricted to ycombinator.com (only HN threads), then the YC directory mirror https://yc-oss.github.io/api/companies/all.json (6,358 companies) with regexes `IRS|tax notice|tax resolution|tax debt|tax relief` and a broad `tax|CPA|accountant` from 2021 (TaxGPT Summer 2024, Rally Tax Winter 2023 acquired, Gravy Spring 2026, pro tools such as Magnetic and Soraban; no consumer notice product); (4) App Store `--find "tax notice"` and `--find "IRS letter"` plus an iTunes lookup; (5) web "tax relief company fees cost IRS tax resolution typical fee"; (6) web "USPS Certified Mail fee 2026 return receipt price" (cost input).

| Product | What it does | Price | Difference |
|---|---|---|---|
| [OweRight: IRS Letter Help](https://apps.apple.com/us/app/oweright-irs-letter-help/id6822549187) (iOS, released 2026-10-23, 3 ratings) | Reads about 150 IRS notice types in English and Spanish, quotes facts, drafts a reply | Reply letter $29.99 once, "Resolution Options" $79.99 | Closest rival. Says it "does not send or file anything for you"; no case state or escalation |
| [TaxGPT](https://www.taxgpt.com/taxgpt-insights/respond-to-irs-notice) (YC Summer 2024, [YC page](https://www.ycombinator.com/companies/taxgpt)) | AI tax assistant; publishes a "draft the response in 10 mins" notice workflow | [PH](https://www.producthunt.com/products/taxgpt) lists "File your taxes for only $50" | Built for accountants and tax professionals; funded, could add a consumer notice flow |
| [CCH AnswerConnect Document Analysis](https://www.wolterskluwer.com/en/expert-insights/how-to-respond-to-irs-notices-with-a-clear-structured-workflow) | Reads an uploaded IRS or state notice, drafts a response for a reviewer | Not found | Professional seat product |
| [Canopy Notices](https://www.accountingtoday.com/news/canopy-releases-tool-to-manage-irs-notices), [NoticeNinja](https://blog.noticeninja.com/blog/how-to-resolve-tax-notices-tips-and-tools-for-success), [IRS Solutions Software](https://directory.lawnext.com/products/irs-solutions-software/) | Notice triage and resolution workflow for tax pros | Not found | Sold to firms, not to the person holding the letter |
| Tax-relief firms ([fee guide](https://www.bench.co/blog/tax-tips/tax-relief-companies), [reviews](https://lendedu.com/blog/precision-tax-relief-review/)) | Human negotiation of larger debts | About $2,000 to $5,000 typical resolution fee (comparison sites, [UNVERIFIED]) | High price, minimum debt, aggressive marketing |
| [IRS app](https://apps.apple.com/us/app/irs/id414113282) (4.6 stars, 11k ratings) and IRS.gov | Status, accounts, notice lookup | Free | No next step or reply help (REV-47) |
| ChatGPT, Claude, Gemini | Explain a pasted letter, draft a reply | Free tiers exist | The free baseline (LIFE-43); no mailing, memory of the case or escalation |

Classification: WEAK DIRECT. Platform risk: the explain-and-draft slice is already free in assistants, and Intuit or H&R Block could add notice help (REV-45 shows TurboTax users asking). Odds a lab ships certified mail plus escalation tracking within 12 months are low, but the labs, Intuit or the IRS could erode the rest, so scale is capped at 2.

## 11. Business model
- Payer: the individual, one-time. Anchors: OweRight $29.99 for a reply and $79.99 for options; relief firms $2,000+. Hypothesis: free notice decoder, $59 "send and track" case (one certified letter, 90 days of follow-ups), $12 per extra letter.
- Model cost per case [ESTIMATE], prices from `research/LANDSCAPE.md`: read notice on Haiku 5.5, 4,000 in + 500 out = 4,000 x $0.10/1M + 500 x $0.50/1M = $0.00065; explain on Sonnet 5.5, 6,000 in + 1,500 out = $0.012 + $0.015 = $0.027; extract documents on Haiku, 15,000 in + 1,500 out = $0.00225; draft reply on Sonnet, 10,000 in + 1,500 out = $0.035; check pass on Sonnet, 6,000 in + 800 out = $0.020; five chat turns on Sonnet with 8,000 cached tokens at $0.10/1M, 1,000 new in, 500 out = 5 x ($0.0008 + $0.002 + $0.005) = $0.039. Total about $0.12.
- Other variable cost: USPS Certified Mail $5.30 (as of 2026-01-18; vendor pages report $5.55 from July 2026, [UNVERIFIED]) + electronic return receipt $2.82 + postage about $0.78 + print $0.66 to $0.83 (Lob) = about $9.65 a letter, x 1.3 letters per case = $12.50. Payment fee 2.9% + $0.30 = $2.01. Support allowance $1.67 [ASSUMPTION]. Sources: https://www.postgrid.com/usps-certified-mail-costs-rates/, https://www.lob.com/pricing.
- Gross margin = ($59 - $0.12 - $12.50 - $2.01 - $1.67) / $59 = about 72%.

## 12. Market size
[ESTIMATE] Buyers: assume 150M individual returns a year [ASSUMPTION, not verified here] x 4% needing a reply = 6.0M; add 30% for SSA and state notices = 7.8M cases; 15% would pay for help over doing it alone [ASSUMPTION] = 1.17M x $59 = $69M a year. Realistic penetration of 2% by year 3 = 23k cases x $59 = about $1.4M a year. Small unless it expands to other agencies.

## 13. Go-to-market
- First 100 customers in about 12 weeks: 40 from hand-answered posts in r/IRS, r/SocialSecurity and r/tax using the free decoder (follow each sub's rules); 30 from search pages per notice code and situation (long tail such as "deceased parent refund Form 1310", since big brands own head terms); 20 from free-clinic and library volunteer referrals [UNVERIFIED which programs]; 10 from CPAs and enrolled agents who decline small notice work.
- Growth loop: shareable proof-of-mailing certificate, consented "what happened with notice X" outcome pages, family invites (siblings share one case).

## 14. Moat and scale path
Curated, versioned rules library per notice code (deadlines, forms, addresses, triggers), case outcome data, an archive of mailing receipts, family accounts. Scale path: SSA, state tax agencies, unemployment, DMV and immigration notices, and second-language notices (UND-30). Moat is moderate; Intuit could replicate it with distribution.

## 15. Solo feasibility
- MVP in 6 weeks: weeks 1-2 intake, extraction and 25 notice types in a rules file; week 3 drafting, checklists and an evaluation set of about 200 notices; week 4 Lob mail, Stripe and receipts; week 5 reminders and case timeline; week 6 Form 911 packet, disclaimers, legal review.
- Running cost before revenue about $80 a month (hosting $25, database $15, SMS and email $15, model testing $20, domain and misc $5), plus a one-time CPA or attorney review of $500 to $1,500 [ASSUMPTION].
- Hardest risk: rule correctness and notice classification, plus minimizing SSN-bearing data (encrypt, auto-delete, refuse on low confidence).

## 16. Pre-mortem
1. Free substitutes: people paste the photo into an assistant and mail it themselves; OweRight already sells the draft at $29.99, so WTP for anything but mailing and escalation collapses.
2. Liability: a wrong deadline or option, or a regulator treating paid letter drafting as unauthorized practice, hurts a user who then misses a window.
3. Episodic demand: most users need it once, SEO takes 6+ months and tax season skews traffic.

## 17. Cheapest validation test
Cost under $200 and about 20 hours over 3 weeks. Landing page plus free decoder for 10 notice codes; Stripe pre-orders for a $29 reply kit and a $59 send-and-track tier; answer 40 real posts by hand. Pass: at least 25 paid pre-orders from 1,000 or fewer visitors (2.5% conversion) and at least 40% of buyers choosing the $59 tier. If under 25% pick it, the mailing and escalation wedge fails: kill or fold into a broader life-admin product.

## 18. Open questions
- Do buyers value certified mail and tracking over mailing it themselves? Some notices accept online replies [UNVERIFIED, seen only as a search-result title], which would shrink the mailing value.
- Which states treat paid letter drafting as unauthorized practice, and is E&O insurance needed? Get one hour each with a CPA or enrolled agent and an attorney.
- SSA fixes are often a call or office visit (LIFE-29): is it a fit, or only a call script and document pack?
- Start with notice types where proof of mailing matters (CP2000 disputes, penalty abatement, Form 1310 refunds for deceased taxpayers) rather than all 150? Watch whether OweRight adds sending.

## Deep dive

Method (reads dated 2026-10-31): iTunes lookup of the OweRight listing, 4 web searches (IRS online reply options, IRS notice volumes, proof-of-mailing rules, consumer notice apps), an iTunes app search, and the Arctic Shift Reddit archive for channel volume and live threads. Model prices: `research/LANDSCAPE.md` section 6. Not tax or legal advice.

### Competitor table
| Competitor | Link | What it does | Price (as published, with date read) | Funding or traction (sourced) | Gap this idea exploits |
|---|---|---|---|---|---|
| OweRight: IRS Letter Help | [App Store](https://apps.apple.com/us/app/oweright-irs-letter-help/id6822549187) | Reads about 150 IRS notice types (English, Spanish), quotes facts, drafts a reply, says how to send it "upload, fax or mail, the way your notice allows"; "Reminders stay on your phone" | App free; reply letter $29.99 once; Resolution Options $79.99; "No account needed. No subscription." (listing, 2026-10-31) | Seller OweRight LLC, released 2026-10-23, v1.0.1 on 2026-10-27, 2 to 3 ratings; no funding found | "OweRight does not send or file anything for you" and "does not keep your pages": no mailing, no proof, no case memory, no escalation |
| TaxGPT (YC Summer 2024) | [notice workflow](https://www.taxgpt.com/taxgpt-insights/respond-to-irs-notice), [YC](https://www.ycombinator.com/companies/taxgpt) | AI tax assistant with a "respond to IRS notice" workflow, built for tax pros | [Product Hunt](https://www.producthunt.com/products/taxgpt) lists "File your taxes for only $50" (first pass) | YC S24 | Pro tool; no mailing or consumer case |
| CCH AnswerConnect Document Analysis (Wolters Kluwer) | [article, 2026-07-06](https://www.wolterskluwer.com/en/expert-insights/how-to-respond-to-irs-notices-with-a-clear-structured-workflow) | Reads an uploaded notice and drafts a response for a reviewer | not found | not found | Professional seat product |
| Canopy Notices, NoticeNinja, IRS Solutions Software | [Canopy](https://www.accountingtoday.com/news/canopy-releases-tool-to-manage-irs-notices), [NoticeNinja](https://blog.noticeninja.com/blog/how-to-resolve-tax-notices-tips-and-tools-for-success), [IRS Solutions](https://directory.lawnext.com/products/irs-solutions-software/) | Notice triage and resolution workflow for tax firms | not found | not found | Sold to firms, not to the person holding the letter |
| Acculink IRS Notice Decoder | [tool](https://acculinkcpa.com/tools/irs-notice-decoder) | Explains a pasted notice and drafts a starting response; warns it is a template (search summary) | free | not found | Does not mail or track anything |
| Tax-relief firms | [Bench guide](https://www.bench.co/blog/tax-tips/tax-relief-companies) | Human negotiation of larger debts | about $2,000 to $5,000 (comparison-site summaries, [UNVERIFIED]) | n/a | Minimum debts; ignore small notices |
| IRS Document Upload Tool, IRS app | [Topic 652 (CP2000)](https://www.irs.gov/node/68416), [IRS app](https://apps.apple.com/us/app/irs/id414113282) | CP2000 reply "through the Document Upload Tool, by fax, or by mail"; window 30 days (60 outside the US) (search summary of IRS pages) | free | IRS app 4.6 stars, 11,228 ratings (2026-10-31) | Free official channel for eligible notices, so mailing matters only where upload is not offered. No drafting, no case memory |
| Taxpayer Advocate Service (Form 911) and congressional casework | [r/IRS 2026-10-24](https://www.reddit.com/r/IRS/comments/1xdzj86/) | Free escalation; the poster: "Took TAS and local gov 28 days to finally tell me that u have an agent assigned to my case and look into my refund." | free | n/a | Free but unguided and slow; people assemble the packet themselves |
| Claimyr | [IRS page](https://claimyr.com/government-services/irs/IRS-sent-me-this-letter-in-the-mail-Should-I-be-worried/2025-04-11) | Appears to sell help reaching the IRS by phone (page not opened) | not read [UNVERIFIED] | not found | Phone access, not a reply or a record |
| ChatGPT, Claude, Gemini; TurboTax and H&R Block | (LIFE-43, REV-45) | Explain a pasted letter and draft a reply; tax suites could add notice help | free tiers | very large | The free baseline for reading and drafting |

**The wedge, stated plainly.** Reading and drafting are now free or $29.99. What is left to charge for:
| Job | OweRight | Free assistants | IRS free channels | Paper Trail |
|---|---|---|---|---|
| Read and explain, draft a reply | Yes ($29.99) | Yes (free) | No | Free decoder, so no moat here |
| Send with proof (certified mail, return receipt, tracked) | No, "you sign and send" | No | Upload or fax for some notices; no mail proof service | Yes: a USPS certified letter with tracking events and receipt kept in the case |
| Deadlines | Reminder on the phone | Forgets next session | Date printed on the notice | Server-side countdown, SMS and email, shared with a family member |
| Follow-up after sending | No | No | None | Day 30, 60, 75 prompts; photo of the agency reply updates the next step |
| Escalation | Resolution Options $79.99 (payment options) | Can explain Form 911 if asked | TAS, congressional offices: free, slow | Form 911 and congressional release prepared for signature when the case stalls |
Why proof matters: under IRC 7502 a USPS postmark on or before the deadline counts as timely; registered or certified mail with the sender's receipt is the strongest proof, while certificates of mailing, Priority Mail receipts and delivery confirmations are not accepted, and courts have refused the common-law mailbox rule ([Texas CPA Society, 2025-10-17](https://www.tx.cpa/news-publications/news-announcements/article/2025/10/17/establishing-proof-of-timely-mailing-under-the-irs-mailbox-rule); [Current Federal Tax Developments, 2023-09-23](https://www.currentfederaltaxdevelopments.com/blog/2023/9/23/taxpayer-cannot-use-common-law-mailbox-rule-to-prove-timely-filing-of-a-refund-claim); search summaries). Warning sign: a r/IRS poster (2026-10-14) who used a third-party USPS mail unit wrote "however, when they stamped the certified mail receipt, they did so with a generic date stamp for today and not the usual circle stamp that traditional post offices use." ([thread](https://www.reddit.com/r/IRS/comments/1x63q0b/)). A mail API may not return a postmarked sender's receipt; this is risk 1 below.

### Market sizing (bottom-up)
Cited anchor: the IRS Automated Underreporter program closed 987,460 cases in fiscal 2025 and assessed $5.9 billion ([NYSSCPA, 2026-06-09](https://nysscpa.org/news/1047348-new-irs-data-shows-strong-filing-season-despite-workforce-decline-2026-06-09), search summary). That is one notice family; no official count of all notices was found. Buyers are cases a year that need a reply: conservative 987,460 x 3 = 2.96M (AUR plus balance-due, penalty, identity and SSA/state notices, the x3 is an [ASSUMPTION]); optimistic 7.8M (150M returns x 4% x 1.3 for SSA and state, section 12 [ASSUMPTION]). Price per case: $59 + 0.3 extra letters x $12 = $62.60.
| Case | Buyers | Adoption | Price | Serviceable cases / revenue |
|---|---|---|---|---|
| Conservative | 2,962,380 | 0.5% = 14,812 | $62.60 | $0.93M a year |
| Optimistic | 7,800,000 | 2% = 156,000 | $62.60 | $9.77M a year |
Revenue at 100 / 1,000 / 10,000 cases: $6.3K / $62.6K / $626K. Customers are episodic (one case, then gone), so these are cases sold per year, not recurring revenue; 10,000 cases a year is 0.34% of the conservative pool. A $9 a month "notice watch" for adult children is an untested recurring layer [ASSUMPTION].

### Unit economics
Per case, 90 days, one Haiku 5.5 / Sonnet 5.5 pipeline (LANDSCAPE prices, [ESTIMATE]): read notice, Haiku, 4,000 in + 500 out = $0.0004 + $0.00025 = $0.00065; explain, Sonnet, 6,000 + 1,500 = $0.012 + $0.015 = $0.027; extract documents, Haiku, 15,000 + 1,500 = $0.0015 + $0.00075 = $0.00225; draft reply, Sonnet, 10,000 + 1,500 = $0.020 + $0.015 = $0.035; check pass, Sonnet, 6,000 + 800 = $0.012 + $0.008 = $0.020; 5 chat turns, 8,000 cached x $0.10/1M + 1,000 x $2/1M + 500 x $10/1M = $0.0078 x 5 = $0.039; 2 agency replies read and next step, 2 x ($0.00065 + $0.020) = $0.041. Model total $0.17.
| Other variable cost | Arithmetic | $ |
|---|---|---|
| Certified mail | ($5.30 + $2.82 return receipt + $0.78 postage + about $0.75 print) = $9.65 x 1.3 letters ([PostGrid](https://www.postgrid.com/usps-certified-mail-costs-rates/), [Lob](https://www.lob.com/pricing), first pass) | 12.55 |
| Stripe on $59 | 2.9% x $59 + $0.30 | 2.01 |
| Support, SMS, email | $1.67 [ASSUMPTION] + 6 x $0.008 + $0.01 | 1.73 |
| Infrastructure share | $80 / 100 cases a month | 0.80 |
| **Total with model** | 0.17 + 12.55 + 2.01 + 1.73 + 0.80 | **17.26** |
Gross margin: (59 - 17.26) / 59 = 71%. Postage, not models, is the cost. **Heavy user:** a family manager with a 6-letter case and 40 chat turns: model $0.93, mail 6 x $9.65 = $57.90, Stripe $2.01, support $5.00, other $0.86 = $66.70 against $59, a 13% loss. Cap: the $59 case includes 30 chat turns and one certified letter, each extra letter is $12 (cost $9.65 + about $0.35 fees). Then revenue 59 + 5 x 12 = $119 against $68.44, margin 42%. Form 911 packets are a $19 add-on (one certified letter plus support).

### First 100 customers
Channel volume (Arctic Shift, 2026-10-24 to 10-30; broad regex, upper bounds): r/IRS about 21 posts a day, about 49 a week on notices, letters, CP codes or penalties; r/tax about 25 a day, about 52 a week; r/SocialSecurity about 17 a day, about 26 a week. I cannot read the sub rules (Reddit is blocked here), so assume no links until the sidebar says otherwise: help in the thread, link only in the profile or when allowed. The long tail is by notice code; recent r/IRS titles include "CP504, tax debt" (2026-10-20), "Received notice CP15 and owe $10'000" (2026-10-18), "CP05A notice: question about paystubs" (2026-10-19), "Letter 6255C" (2026-10-12). Message: "Understand your notice for free. If you need to reply, we send it certified, keep the proof, and tell you what to do on day 30, 60 and 75." Offer: free decoder; $29 reply kit; $59 send-and-track. Funnel [ESTIMATE]: per 100 visits, 40 use the decoder, 10 leave an email, 3 buy.
| Week | Action | New paid | Cum. |
|---|---|---|---|
| 1 | Ship the decoder for 10 codes (CP2000, CP14, CP501, CP503, CP504, CP05A, CP15, 5071C, 6255C, LT11) with a reply-channel map (upload/fax/mail) for each; 10 helpful replies; founding price for the first 20 cases | 4 | 4 |
| 2 | One SEO page per code ("CP2000 response letter", "CP504 what to do"); 15 replies; email 20 enrolled agents and CPAs who turn away small notice work, $10 referral per case | 5 | 9 |
| 3 | One-page handout and email to 10 low-income taxpayer clinics, 10 libraries or senior centers | 6 | 15 |
| 4 | "Handling a parent's IRS letter" page for adult children; caregiver communities (r/AgingParents, check rules) | 7 | 22 |
| 5 | Add 3 SSA notice types and the Form 1310 refund-for-deceased flow | 8 | 30 |
| 6 | "TAS and Form 911: what to send" explainer plus 3 consented outcome stories | 9 | 39 |
| 7 | Referral credit: send a letter, get a letter | 8 | 47 |
| 8 | Review reply-channel map vs mailing demand; price test $59 vs $49 | 8 | 55 |
Base case 55 cases by week 8; 100 around week 12, matching section 13. Loop after 100: consented "what happened with notice X" pages, family invites, EA/CPA and clinic referrals, shareable proof-of-mailing receipt with personal data redacted.

### One-week validation test (under $50)
**What:** an honest pre-order page, not a live product. One page (Carrd free or GitHub Pages) with a free guide "10 common IRS notices, what each says, the deadline printed on it" (static text from IRS pages, labeled not advice), 3 sample explainers (CP2000, CP504, CP05A), and the line: "Paper Trail is not launched. Reserve a founding case with a $9 refundable deposit, credited to the price. Choose: $29 reply kit, or $59 send-and-track (certified mail, proof, deadlines, follow-ups). Refundable any time before launch." One question: "What would you do if this did not exist?" (call the IRS / ChatGPT / pay a CPA / OweRight / nothing). Traffic: answer 10 notice threads by hand (no link), post the guide once in r/tax or r/IRS only if self-posts with links are allowed, share with your own network, email 3 libraries or clinics. No ads, no fake accounts, one account per place.
**Budget:** domain $12 (optional); Stripe fees on 5 refunded deposits 5 x (2.9% x $9 + $0.30 = $0.56) = $2.81; model credit $5 for the samples; everything else free. About $20.
**Pass:** 150 or more unique visitors, 10 or more emails, 5 or more deposits (3.3%), and 50% or more of depositors pick $59. **Fail:** 2 or fewer deposits, or 25% or fewer pick $59 (then mailing and escalation are not valued: fold into a draft-only product or kill). Under 100 visitors is inconclusive: extend to 14 days.

### Build brief (paste into a coding session)
```text
PRODUCT: Paper Trail turns a photographed IRS, SSA or state notice into a quoted explanation, a user-approved reply, a tracked certified mailing with proof, and a deadline-and-escalation timeline.
It prepares, organizes, mails and tracks the user's own correspondence. It does not give tax advice, represent anyone (no Form 2848), or prepare returns.
Levies, liens, audits, identity theft and large balances show a referral card (CPA, enrolled agent, attorney, low-income taxpayer clinic) and no draft.
MVP FEATURES (each testable)
1 Upload photos/PDF (up to 8 pages); mask SSNs in the browser; encrypt at rest; auto-delete at 90 days. Test: no SSN pattern in DB or logs.
2 Notice reader: code, tax year, amount, response date, return address; each fact with quote and page region and confidence; ask the user when a date is unreadable. Test: 50-notice set.
3 Versioned rules library (YAML) per code: options the notice lists, forms, reply channels (upload/fax/mail), address, escalation and referral triggers.
4 Reply drafter from user facts and documents; check pass flags unsupported claims; user approves and signs.
5 Certified mail with return receipt through a mail API; store tracking events and receipt scans.
6 Timeline with reminders (SMS/email) at T-10 and T-3 days and after mailing at day 30, 60, 75.
7 Agency-reply intake: photo updates the case and next action.
8 Escalation packets: Form 911 and a congressional casework release, prepared for signature.
9 Family mode with a recorded consent from the parent.
10 Stripe: $29 reply kit, $59 send-and-track, $12 per extra letter, $19 escalation packet.
NON-GOALS: representation, return preparation, advice on agree/disagree, phone automation, native apps, more than 25 notice types and 3 states in v1, a separate OCR vendor.
CORE AI LOOP: read notice (Haiku 5.5 vision) -> explain (Sonnet 5.5) -> extract user documents (Haiku 5.5) -> draft (Sonnet 5.5) -> check pass (Sonnet 5.5) -> read agency reply (Haiku 5.5) -> next action (Sonnet 5.5). Prompts quote the source, cite the rules entry, refuse to invent dates or amounts. Humans: the user approves every letter; a CPA or enrolled agent reviews the rules library; low confidence means ask or refuse.
DATA MODEL: User, Case(agency, notice_code, tax_year, deadline, status), Document, Fact(key, value, quote, page), Draft(version, text, approved_at), Mailing(tracking, events, receipt_file, mailed_on), Reminder, AgencyReply, EscalationPacket, FamilyLink(consent), AuditLog.
INTEGRATIONS: Lob https://docs.lob.com/ (certified mail); USPS tracking https://developers.usps.com/; Stripe https://docs.stripe.com/payments/payment-links; Twilio https://www.twilio.com/docs/messaging; Resend https://resend.com/docs. The IRS Document Upload Tool has no API: the app links the user to it when a notice allows it.
STACK (about $100 a month): Next.js on Vercel, Supabase (Postgres, auth, storage) with libsodium envelope encryption for files, Inngest for reminders and delete jobs, Stripe, Sentry, Langfuse free tiers.
EVALS: 1 Reader, 50 notices incl. angled photos and Spanish: code, year, amount, date exact in 95%, zero invented dates. 2 Referral triggers, 10 notices (levy warning, lien, audit, identity theft, balance over $10,000): referral card shown 10/10, no draft. 3 Rules fidelity: for 10 codes the listed options match the notice text, signed off by a CPA or EA. 4 Mail proof: send 5 test letters to a friendly address; confirm what proof comes back and ask a CPA whether it meets IRC 7502. 5 Privacy: SSN search in DB and logs returns zero; the delete job removes files at day 90.
BUILD PLAN (6 weeks): W1 intake, reader, rules for 10 codes, eval set. W2 explain, draft, check. W3 mail API, Stripe, receipts. W4 timeline, reminders, agency-reply intake. W5 Form 911 packet, family mode, privacy hardening. W6 CPA and attorney review, disclaimers, beta with 10 cases.
RISKS TO TEST FIRST: 1 proof of mailing under IRC 7502 when a vendor mails; 2 unauthorized-practice line; 3 upload and fax channels shrinking mailing demand (map the top 25 notices); 4 SSN data handling; 5 OweRight adding send; 6 episodic demand and slow SEO.
```

**Notes for the main researcher:** The IRS Document Upload Tool lets CP2000 replies be filed free online, so the mailing wedge is narrower than section 7 implies; it holds where a notice offers no upload and where a statutory deadline makes a postmarked certified receipt matter, but only if the mail vendor returns an acceptable receipt (untested). WTP 3 stands only if the $59 tier beats a $29 draft-only tier in the test.

## Red team
Skeptical-investor review on 2026-11-01 (full text: `research/RED_TEAM_A.md`). Verdict: **pass**.

**Top attacks (summarized):**
1. **The wedge is a receipt that may not exist, next to a free one that does.** The IRS Document Upload Tool gives free electronic confirmation; elsewhere, IRC 7502 proof needs a USPS-postmarked receipt, and r/IRS evidence shows a third-party mail unit stamping a generic date.
2. **The liability line carves out the people who would pay.** The $2,000+ relief-firm anchor is for large debts (levies, liens, audits, identity theft), which the product refers out.
3. **Licensing is also federal.** Composing and mailing a taxpayer's reply for a fee raises a Circular 230 practice-before-the-IRS question the file does not ask.
What would change the red team's mind: five test letters through the mail API returning a postmarked receipt a CPA accepts under IRC 7502, 25+ paid pre-orders with 40%+ choosing $59 over $29, and a written practitioner view on Circular 230.

**Response (main researcher):**
- All three attacks land. Evidence drops from 4 to 3 (the signals show phone failure and fear; demand for mailing and escalation is inferred), willingness to pay from 3 to 2 (OweRight at $29.99 and the free upload tool set the ceiling), solo feasibility from 4 to 3 (a reviewed rules library plus the proof-of-mailing and Circular 230 questions).
- Possible re-scope: Social Security and state-agency notices (payment suspensions, overpayment demands), where no IRS-style upload confirmation exists and the strongest signal in this file came from (LIFE-29, 347 comments).
