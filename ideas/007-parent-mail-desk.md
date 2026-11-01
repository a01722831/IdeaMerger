---
id: "007"
slug: parent-mail-desk
name: Parent Mail Desk
one_liner: "A parent texts a photo of any letter; AI explains it and gives the adult child a one-tap action."
target_user: "Adult children who handle an aging parent's mail, bills and phone calls, often sharing the load with siblings"
form_factor: "web app"
lens: "Pain-first"
frontier: false
competition: "WEAK DIRECT"
confidence: "MED"
status: "developed"
signals: [LIFE-14, LIFE-13, HN-22, HN-28, LIFE-25, LIFE-15, LIFE-16, LIFE-26]
scores:
  pain: 3
  evidence: 4
  ai_leverage: 3
  whitespace: 2
  novelty: 2
  why_now: 3
  solo_feasibility: 4
  distribution: 3
  wtp_economics: 2
  scale_defensibility: 2
total: 56.8
price_hypothesis: "$14.99/month per family (one parent, up to four relatives); first scam check free"
model_cost_per_user_month: "$0.22 model plus about $1.5 for text messages and a phone number"
gross_margin: "84%"
mvp_weeks: 6
deep_dive: true
red_team: true
---

# Parent Mail Desk

## 1. One-liner
A parent texts a photo of any letter; AI explains it and gives the adult child a one-tap action.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Weekly mail, hours of calls, emotionally heavy (LIFE-13 has 108 points); not a 5 because many children cope with a photo and a phone call. Red team: 4 to 3, red team: the product as scoped leaves out calling, proxy authority and paying |
| Evidence quality | 2 | 4 | Eight cited signals from 2026, two strong; no one states a willingness to pay (LIFE-16 only hears a suggestion to hire a care manager). |
| AI leverage | 2 | 3 | Explaining and classifying a letter is native to any assistant; the model does the triage and drafting, but the value is the workflow around it. |
| Whitespace | 2 | 2 | About ten small caregiver apps in one App Store search plus Adrina AI and TendTo; none funded as far as I saw, and the household-agent red zone sits on top. |
| Novelty of insight | 1 | 2 | Every care-coordination app pitches shared tasks; the parent-side photo-by-text channel is the only real twist. |
| Why now | 1 | 3 | Vision models read a letter for a fraction of a cent and caregivers grew 45% in a decade, but free assistants have the same capability. |
| Solo feasibility | 2 | 4 | Text and email intake, a web queue and classification are about 6 weeks; the risks are parent adoption and scam-check errors. |
| Distribution | 2 | 3 | Dense intent communities (r/AgingParents, AgingCare), a shareable letter checker and sibling invites; crowded by lookalikes. |
| Willingness to pay and unit economics | 2 | 2 | Caregivers pay for help and a related senior-AI plan lists $19/month, but free apps abound and caregiving episodes end, so churn is structural. Red team: 3 to 2, red team: no payment signal; Antigrift at $9 to $19 a month and free assistants set the ceiling |
| Scale and defensibility | 2 | 2 | Platform risk from household agents (Gemini, Siri, ChatGPT) caps this at 2; the family case log and vault are the only lock-in. |
| **Total** | | **56.8** | |

Confidence: MED. FRONTIER: no.

Red-team adjustment (main researcher, 2026-11-01): pain severity and frequency 4 to 3 (red team: the product as scoped leaves out calling, proxy authority and paying); willingness to pay and unit economics 3 to 2 (red team: no payment signal; Antigrift at $9 to $19 a month and free assistants set the ceiling).

## 3. The problem
- Who: the adult child (usually one "designated" child) of a parent aged 70 or more, plus siblings who help unevenly.
- What happens: parents photograph every letter and ask the child to summarize it or phone the company (LIFE-14). After a death, bills, pension and logins land on one child (LIFE-13). Siblings lack a shared record (LIFE-15). Nobody knows where documents are (HN-22). Health admin becomes a full-time job (HN-28).
- Cost: hours every week, missed deadlines, money lost to scams and forgotten subscriptions (LIFE-25), and a trust problem when a stranger is hired to help (LIFE-26).
- Workarounds: texted photos, mail forwarded to the child, binders, spreadsheets, a paid geriatric care manager (suggested in LIFE-16). Companies often talk only to the account holder [ASSUMPTION], and proxy 2FA is a snag (LIFE-25).
- Scale: AARP and the National Alliance for Caregiving count 63M US family caregivers, up 45% in a decade (2025 report).

## 4. Evidence
- **LIFE-14** (medium, 2026-10-27, r/AgingParents, 14 comments): "For example, they might send me a photo of a letter and want me to me to summarize it for them like I am ChatGPT. They want me to call customer service for them to resolve issues." https://www.reddit.com/r/AgingParents/comments/1xgsqtk/
- **LIFE-13** (strong, 2026-10-27, r/AgingParents, 108 pts / 31 comments): "I (33 F) sifted through all the utility bills, mortgage, and car loan documents. Set up the pension documents and the IRA rollover process which should be processed by January." https://www.reddit.com/r/AgingParents/comments/1xh4xpu/
- **HN-22** (medium, 2026-07-09; poster is the vendor of LastShelf, an emergency map of a family's documents): "In the middle of dealing with all the medical logistics, I realized none of our family could answer if he: [...] How to trigger his life insurance policy?" https://news.ycombinator.com/item?id=48847298
- **HN-28** (medium, 2026-08-10): "His full time job became managing his health: medicare, state benefits, doctors appointments, medications, talking with billing people. [...] I just imagine my father, or my 75yr old mother (whose health is beginning to decline) trying to navigate this new AI world." https://news.ycombinator.com/item?id=49248278
- **LIFE-25** (medium, 2026-01-03, HN): "Imagine finding 12 renewing subscriptions to malwarebytes and other security suites. Or having to burn credit cards every month because they can no longer tell the difference between ads/scams and actual needs." https://news.ycombinator.com/item?id=46472471
- **LIFE-15** (medium, 2026-10-29, r/AgingParents): "whoever takes her comes back with their version, and by the time it gets to everyone else half the details are gone. last time we went back and forth about one of her meds because two people remembered it differently" https://www.reddit.com/r/AgingParents/comments/1xiv9rr/
- **LIFE-16** (medium, 2026-10-06, AgingCare): "My father recently moved in with me, he is 75 years old and I am having a hard time managing the follow up appointments, coordinating referrals and just doing these admin things. I don't know how to address this with a full time job and other commitments." https://www.agingcare.com/questions/stressed-about-paperwork-about-my-father-in-need-need-tips-499738.htm
- **LIFE-26** (medium, 2026-09-26, AgingCare): wants recurring checking and renewal tracking but worries about trusting a hired bookkeeper. "I am trying to see, going forward, how to help him manage his finances which would include checking his credit card expenses to make sure they are valid, reconciling his checking account and keeping track of when he needs to renew his CDs, pay his home and car insurance etc." https://www.agingcare.com/questions/how-safe-is-it-to-hire-an-outside-bookkeeper-to-take-care-of-my-92-year-old-brothers-finances-499678.htm
- New evidence (not in SIGNALS.md): r/AgingParents, 2026-10-20, 1 pt / 5 comments: "My dad, who managed their finances for decade, is cognitively declining. Management of household finances cannot be his job anymore." The hand-off moment this product targets. https://www.reddit.com/r/AgingParents/comments/1xawl4i/

## 5. The product
- What it does: each parent gets a dedicated phone number and email address. The parent texts a photo of a letter (or the child forwards one). AI reads it, explains it in two plain sentences (English or Spanish), classifies it (bill, suspected scam, deadline, medical, informational, junk), extracts amount, due date and sender, checks for duplicates and already-paid bills, and puts a card in the family queue with a one-tap action for the child: open the payment page, call (with a script, the number printed on the letter and what to have ready), reply (draft letter), file to the vault, shred, or hand to a sibling. The parent gets a short text back.
- Core AI loop: photo or email in -> OCR, classification, extraction and scam check -> plain-language reply to the parent and an action card for the child -> the child acts or reassigns -> outcome logged (paid, called, resolved) -> sender memory improves the next classification.
- Interaction model: parent uses text messages only, no install. Children use a web app or PWA with push, email and text alerts, a sibling assignment board, a searchable vault, and a monthly digest.
- Form factor: web app plus an SMS and MMS channel.
- Day in the life: Rosa (78) texts a photo of a letter from her Medicare Advantage plan. In a minute she gets "This says your plan changes next year. Nothing is due today. Ana will look at it." Ana's queue shows a card: plan change, decision window closes Dec 7, "Call the plan" with a script, Luis assigned to compare options. Another photo, "final notice, pay by gift card", is flagged as a likely scam and Ana is alerted.
- Liability line: it explains, routes and drafts. It never pays, signs or gives medical, legal or financial advice, and scam flags are informational.

## 6. Why the LLM is load-bearing
- Letters come from every sender in every layout, photographed badly. Reading them, extracting due dates and amounts, judging scam versus legitimate, rewriting bureaucratic language as two sentences, and drafting a reply or call script are all language tasks.
- Without the model this is a shared inbox with manual tagging, which is what the care-coordination apps already are.

## 7. The insight
- The summary is a commodity: LIFE-14's parent already uses the child "like I am ChatGPT". The product is the family workflow: who handles what, by when, with which document, plus a zero-install channel for the parent.
- The unit is the case: letter, next action, owner and evidence, kept together for the sibling who takes over and for the day the estate needs a record.
- Honest limit: TendTo and Family Tend pitch the same coordination. The real differences would be the parent-side photo channel and action depth.

## 8. Why now, and why this does not exist yet
- Why now: a letter costs about $0.004 to read and classify (math in section 11), and caregiver numbers jumped 45% in a decade.
- Why not here: it partly is. Adrina AI scans and shares bills and notices, TendTo coordinates bills, medications and documents, Scam Scanner checks letters. In my searches none ties a parent's text-a-photo intake to child actions with assignments, and all are months old with almost no traction.

## 9. Inspiration and derivation
- Parents: care-coordination apps (ianacare, Caring Village), paperwork apps (Adrina AI, DueBox) and family document vaults (LastShelf in HN-22).
- Changed: interaction model (the parent texts a photo, no app), core job (an action queue, not storage), user (the adult child buys and operates, the parent is the sensor), channel (caregiver communities and a free letter checker).

## 10. Competition check
Queries run:
1. WebSearch: "app helps adult children manage aging parent's mail bills photo of letter AI explains what to do shared family"
2. WebSearch (Product Hunt): "site:producthunt.com aging parents paperwork mail bills family caregiver AI"
3. WebSearch (YC directory): "site:ycombinator.com/companies aging parents family caregivers paperwork elder care AI"
4. App Store, `scripts/app_reviews.py --find`: "caregiver family documents parent", "family caregiving coordination", "scam protection seniors" (three other queries failed with connection errors)
5. WebSearch: "Carefull senior financial monitoring service price banks trusted contact person feature older adults accounts family alerts"
6. WebSearch: "Caregiving in the US 2025 report AARP National Alliance for Caregiving million family caregivers adults caring for older adult"; WebFetch of the Adrina AI and TendTo pages; Reddit archive r/AgingParents, r/eldercare, r/over60.

| Product | What it does | Price | How it differs |
|---|---|---|---|
| [Adrina AI](https://www.producthunt.com/products/adrina-ai) (Product Hunt, 2026) | "Family paperwork, finally under control": scan or upload bills, notices, policies and receipts, reminders, share selected records with trusted people; English and Spanish | Free options | Closest on scanning; no parent channel or assignments; 2 followers |
| [TendTo.ai](https://betalist.com/startups/tendto-ai) (BetaList, 2026-04-03) | Bills, meds, appointments, documents, role-based family dashboard, AI companion; mail photos not mentioned | None listed | Coordination without mail intake |
| [Family Tend](https://hunted.space/product/family-tend), [Kinly](https://www.hunted.space/product/kinly-2) (Product Hunt mirrors, snippets) | Shared calendars, sibling tasks, medication schedule from a pill-bottle photo | n/a | Care coordination, not mail |
| [ianacare](https://apps.apple.com/us/app/ianacare-family-caregiving/id1441737626) (57 ratings, 4.4), [Caring Village](https://apps.apple.com/us/app/caring-village-caregiver-app/id1093814557) (36 ratings) | Care logs, family coordination; ianacare adds human navigators through employers | Free to consumers | Care-focused; no letter handling |
| [Scam Scanner](https://apps.apple.com/us/app/scam-scanner-ai-scam-detector/id6758177873) (Happy Grandma Senior Tech Support, 2026-02-05, 12 ratings) | Point the camera at a letter or message; AI says whether it looks safe | Free plus premium | Scam check only |
| Carefull, [EverSafe](https://eversafe.com/index7.html) (snippets) | Money monitoring with family alerts, sold through banks | Not found | Watches money movement, not mail |
| YC: [ReverCare](https://www.ycombinator.com/companies/revercare), [Oma Care](https://ycombinator.com/companies/oma-care); F26 RFS "AI for the Aging Population" ([mirror](https://modelence.com/yc-rfs-fall-2026/ai-for-the-aging-population)) | Elder-care concierge; pay for family caregiving; RFS asks for caregiver coordination | n/a | Different jobs; shows investor interest |
| ChatGPT, Gemini, Claude | Summarize a letter photo | Subscription | No family workflow |

Classification: **WEAK DIRECT**. About ten small caregiver apps (0 to 5 App Store ratings each, App Store ids suggest 2026 launches) and two close paperwork rivals, none with visible traction or funding. It slides toward CROWDED if any of them raises money.

Platform risk: high for the explain-a-letter feature. Apple's iOS 27 Siri (personal context, on-screen awareness; coverage of mixed reliability), Google's household agent (Labs) and ChatGPT Work already sit in the household-agent red zone in `research/LANDSCAPE.md`. A generic family inbox could absorb the workflow within 12 months. Per the rubric this caps Scale and defensibility at 2 and Whitespace at 3; I score Whitespace 2 because of the lookalikes.

## 11. Business model
- Payer: the adult child. Price: $14.99/month per family (one parent, up to four relatives), annual $129; first scam check free. Anchors: Memory Lane's senior-AI premium lists $19/month (aggregator listing), Adrina is free, TendTo lists no price.
- Model cost per family per month [ESTIMATE]: 12 letters. Haiku 5.5 vision pass 2,500 in x $0.10/1M + 600 out x $0.50/1M = $0.00055. A Sonnet 5.5 second pass on 30% of letters, (3,000 in x $2/1M + 600 out x $10/1M) x 0.3 = $0.0036. Per letter $0.0042 x 12 = $0.05. Child chat, call scripts and drafts, 15 Sonnet calls x $0.011 = $0.165. Total $0.22.
- Other variable [ASSUMPTION, not in the landscape table]: a phone number $1.15/month; 12 inbound photo texts at $0.01 and 32 outbound texts at $0.008 = $0.38; total about $1.5.
- Gross margin [ESTIMATE]: $14.99 - $0.22 - $1.5 - Stripe fee ($0.43 + $0.30 = $0.73) = $12.54, about 84%.

## 12. Market size
- Buyers [ESTIMATE]: 63M US family caregivers (AARP and NAC, 2025). Assume 20% manage a parent's mail and bills [ASSUMPTION] = 12.6M households.
- Revenue: 12.6M x $180 a year = $2.3B if all paid. Realistic penetration 0.25% = 31K families x $180 = $5.7M ARR. With a 24-month average life, about 13K new families a year are needed to hold that level.
- Reading: a real but modest business that depends on cheap acquisition and on beating free alternatives.

## 13. Go-to-market
- First 100 customers: (1) answer "my mom sends me photos of letters" and scam-letter threads in r/AgingParents, r/eldercare and AgingCare, about 40; (2) a free web "Is this letter a scam?" checker with a shareable result, capturing the adult child's email, about 40; (3) SEO on "how to manage an elderly parent's mail and bills", about 20.
- Growth loop: sibling invites (LIFE-15 shows siblings need a shared record) and the checker's share link; the parent's friends are a secondary loop.

## 14. Moat and scale path
- Moat: the family case log and vault (switching cost grows with history), sender intelligence (which senders are legitimate, which are scams) and authorization templates by company.
- Scale path: bills and portals, POA workflows, hand-off to estate settlement (see 015 Estate Clerk), and employer or bank resale, which would need partnerships and is not a launch dependency.

## 15. Solo feasibility
- MVP (6 weeks): text and email intake, OCR and classification, plain-language replies, scam check, the child's action queue, assignments, vault with search, call scripts and reply drafts, monthly digest.
- Running cost before revenue: about $60 to $100 a month (hosting, a few parent numbers, a few dollars of model calls).
- Hardest risk: getting the parent to send photos at all, followed by scam-check false negatives and the sensitivity of stored documents (Social Security numbers, medical letters).

## 16. Pre-mortem
1. Parents do not send photos, so the child uploads everything and the product is just a vault.
2. Free assistants and household agents make "explain this letter" free, and about ten lookalikes make acquisition expensive.
3. Churn and trust: the caregiving episode ends within one to three years, and one breach of sensitive documents ends the company.

## 17. Cheapest validation test
- What: concierge version. Recruit 10 adult children from r/AgingParents; give each parent a dedicated text number; answer each photo within 5 minutes using Claude plus manual review for 2 weeks; then ask for $15/month.
- Cost: about $50 and 20 hours. Duration: 2 weeks plus a week for the ask.
- Pass: at least 6 of 10 parents send 6 or more photos and at least 4 of 10 children pay. Fail: fewer than 3 parents active; then the channel idea is dead and only the child-side vault remains.

## 18. Open questions
- Will parents text photos reliably, and who sets it up?
- Which companies accept the child as authorized representative, and should the product generate authorization requests (not legal documents)?
- What false-negative rate on scam checks is acceptable, and who carries the liability?
- Are banks, insurers or employers a better payer than the child (partnerships, so later)?
- How much overlap with 009 Bill Detective (bills), 037 Retirement Desk (Medicare letters) and 036 Do It With Me (parent on the phone) argues for one family-admin product?

## Deep dive

### Competitor table
| Competitor | Link | What it does | Price (as published, with date read) | Funding or traction (sourced) | Gap this idea exploits |
|---|---|---|---|---|---|
| Antigrift | [antigrift.com](https://antigrift.com/), [Product Hunt](https://www.producthunt.com/products/antigrift) | Text a photo of any suspicious letter, flyer or postcard to 1 (833) 365-0211 (no app); daily email scanning; unlimited scam checks; weekly alerts; family dashboard; a free checker at antigrift.com/check (Product Hunt snippet) | Individual $9 a month; Family $19 a month for up to 4 protected members; 17% off annual (site, read 2026-10-31). A Product Hunt snippet showed $19 and $39, likely older | No user count, funding or founders stated; "CASA Tier 2 Security Assessed" and "Google Verified OAuth App" are its own claims; Trustpilot shows no reviews yet (search summary) | Scam verdicts only: no bill or deadline extraction, action queue, sibling assignment or vault |
| Adrina AI | [Product Hunt](https://www.producthunt.com/products/adrina-ai) | Scan or upload bills, notices and policies; reminders; share records with trusted people; English and Spanish | Free options (section 10) | 2 followers (section 10) | No parent text channel or assignments |
| TendTo.ai | [BetaList, 2026-04-03](https://betalist.com/startups/tendto-ai) | Bills, meds, appointments, documents and a role-based family dashboard | None listed | n/a | Coordination without mail intake |
| MailScan AI, Papierpilot, Mail Assistant, Billigent AI | [MailScan AI](https://apps.apple.com/mx/app/mailscan-ai/id6755808186), [Papierpilot](https://www.startuphub.ai/startups/papierpilot.md), [Mail Assistant](https://apps.apple.com/us/app/-/id6741898310), [Billigent AI](https://apps.apple.com/app/billigent-ai/id6745528779) | Single-user scan-and-explain apps for letters and bills; Papierpilot and Billigent work on-device (search summaries) | Not seen | Not seen | No family sharing, parent channel or assignments |
| Family Tend, Kinly, ianacare, Caring Village, ElderFi | [Family Tend](https://hunted.space/product/family-tend), [Kinly](https://www.hunted.space/product/kinly-2), [ianacare](https://apps.apple.com/us/app/ianacare-family-caregiving/id1441737626), [Caring Village](https://apps.apple.com/us/app/caring-village-caregiver-app/id1093814557), [ElderFi](https://appgoblin.info/apps/6780103761) | Care coordination, shared tasks, medication and care logs; ElderFi (iOS, June 2026) tracks recurring bills | ianacare and Caring Village free to consumers (section 10); others not seen | ianacare 57 ratings (4.4), Caring Village 36 (section 10) | Care-focused; no letter handling |
| Scam Scanner | [App Store](https://apps.apple.com/us/app/scam-scanner-ai-scam-detector/id6758177873) | Camera at a letter or message; AI says whether it looks safe | Free plus premium; premium price not seen | 12 ratings (section 10) | Scam check only |
| EverSafe | [pricing](https://www.eversafe.com/pricing/) | Money monitoring with family alerts | Essentials $7.49, Plus $16.99, Gold $26.99 a month; 15% off annual; 30-day trial; 10% senior discount (search summary of the pricing page, read 2026-10-31) | Page title says it acquired CATCH.ai | Watches money, not mail |
| Carefull | [AARP](https://www.aarp.org/personal-technology/tools-to-avoid-elder-financial-abuse/), [CityBiz](https://www.citybiz.co/article/16830/carefull-raises-3-2m/) | Monitors accounts for signs of elder financial abuse | $12.99 a month or $119.99 a year (AARP, search summary) | "Carefull raises $3.2M" (CityBiz title, date not seen); Nationwide partnership ([WealthManagement](https://www.wealthmanagement.com/financial-technology/preventing-elder-fraud-nationwide-partners-with-carefull), title) | Watches money, not mail |
| ReverCare, Oma Care; YC F26 "AI for the Aging Population" | [ReverCare](https://www.ycombinator.com/companies/revercare), [Oma Care](https://ycombinator.com/companies/oma-care), [RFS](https://modelence.com/yc-rfs-fall-2026/ai-for-the-aging-population) | Elder-care concierge; pay for family caregiving; the RFS asks for caregiver coordination | Not found | Investor interest | Different jobs |
| ChatGPT, Gemini, Claude | not applicable | Summarize a letter photo | Subscriptions; not re-checked | Not applicable | No family workflow or parent text channel with a queue |

Classification stays WEAK DIRECT, but Antigrift is a close new rival on the parent-side photo-by-text channel.

### Market sizing (bottom-up)
- Buyer: the adult child who handles a parent's mail and bills. Cited base: 63M US family caregivers, up 45% in a decade (AARP and NAC, 2025-07-24, [AARP release](https://www.aarp.org/press/releases/2025-07-24-new-report-reveals-crisis-point-for-americas-63-million-family-caregivers)). Share managing a parent's mail and bills: 20% [ASSUMPTION], so 63M x 0.20 = 12.6M households. Cross-check: a secondary source counts 51M adults caring for someone 50 or older ([Lifeline](https://www.lifeline.com/?p=44531), title only [UNVERIFIED]); 51M x 25% = 12.75M.
- Price $14.99 x 12 = $179.88 a year.

| Case | Penetration of 12.6M | Families | ARR | New families a year to hold it (24-month life) |
|---|---|---|---|---|
| Conservative | 0.1% | 12,600 | 12,600 x $179.88 = $2.27M | 6,300 |
| Optimistic | 0.5% | 63,000 | 63,000 x $179.88 = $11.33M | 31,500 |

- If all 12.6M paid: $2.27B. Revenue at 100, 1,000 and 10,000 families: $17,988, $179,880 and $1,798,800 ARR ($12,900, $129,000 and $1,290,000 on the $129 annual plan); 10,000 families is 0.08% of 12.6M. Anchors: Antigrift $9 and $19, EverSafe $7.49 to $26.99, Carefull $12.99, Adrina free, a senior-AI premium at $19 (section 11).

### Unit economics
Per family per month, 12 letters. Prices from `research/LANDSCAPE.md` section 6.

| Line | Volume | Tokens per call | Model and price per 1M | Arithmetic [ESTIMATE] | Cost |
|---|---|---|---|---|---|
| First pass (read, classify, extract, scam check) | 12 | 2,500 in, 600 out | Haiku 5.5, $0.10 / $0.50 | 12 x ($0.00025 + $0.0003) | $0.007 |
| Second pass on 30% of letters | 3.6 | 3,000 in, 600 out | Sonnet 5.5, $2 / $10 | 3.6 x ($0.006 + $0.006) | $0.043 |
| Child chat, call scripts, drafts | 15 | 3,000 in, 500 out | Sonnet 5.5 | 15 x ($0.006 + $0.005) | $0.165 |
| Monthly digest | 1 | 6,000 in, 1,000 out | Sonnet 5.5 | $0.012 + $0.010 | $0.022 |
| Total model | | | | | $0.24 |

- Messaging ([Twilio pricing](https://www.twilio.com/en-us/sms/pricing/us), read 2026-10-31; carrier fees assumed at $0.004 per SMS and $0.003 per MMS). Design A (the file: one number per parent, SMS alerts to the child): number $1.15 + 12 photo texts x ($0.0165 + $0.003) = $0.23 + 32 outbound SMS x ($0.0083 + $0.004) = $0.39 = $1.78. Design B (one pooled number routed by sender, child alerts by push and email): $1.15 / 50 families = $0.02 + $0.23 + 12 x $0.0123 = $0.15 = $0.40. Messaging, not AI, is the main variable cost.
- Payments 2.9% x $14.99 + $0.30 = $0.73. Infrastructure [ASSUMPTION] $80 a month / 100 families = $0.80 (/ 1,000 = $0.08). Support [ASSUMPTION] $1.00 (2 minutes at $30 an hour).
- Margin at 100 families: design A 0.24 + 1.78 + 0.73 + 0.80 + 1.00 = $4.55, so ($14.99 - $4.55) / $14.99 = 69.6%; design B 0.24 + 0.40 + 0.73 + 0.80 + 1.00 = $3.17, 78.9%; design B at 1,000 families $2.45, 83.7%; design B on the $129 annual plan ($10.75 a month, payments $0.34) $2.78, 74.1%. Section 11's 84% left out infrastructure and support.
- Heavy family (40 letters, 60 chat calls): model 40 x $0.00415 + 60 x $0.011 + $0.022 = $0.85; messaging (design B) $0.02 + 40 x $0.0195 + 40 x $0.0123 = $1.29; payments $0.73; infrastructure $0.80; support $3.00: $6.67, margin 55% (design A: 43%).
- Cap: the plan includes 30 letters and 30 chat calls a month. Beyond 30 letters the parent still gets an acknowledgement but the summary goes to the child by push and email, not SMS, and a pack of 30 more letters is $5 [ASSUMPTION]. Child alerts never use SMS.

### First 100 customers
Funnel [ESTIMATE]: a helpful reply brings 10 visits; visit to 7-day trial (a parent's number added) 8%; trial to paid 30%, so 2.4% of visits pay. Care managers: an individually written email gets a reply 10% of the time, 50% of repliers adopt, each recommends to 6 clients over 5 weeks, and 35% of those trials pay.

| Week | What you do | New paying families (math) | Cumulative |
|---|---|---|---|
| 1 | Convert the pilot families (3 of 8 pay at the day-7 ask); trial and pricing live; 10 helpful replies a week in r/AgingParents, r/eldercare and the AgingCare forum (disclose; link only where rules allow) | 3 + (10 x 10 x 2.4% = 2.4) = 5.4 | 5 |
| 2 | Free "Explain this letter" web tool (no signup; email capture for the shareable result); replies; 30 emails to Aging Life Care Association care managers | 2.4 | 8 |
| 3 | Show HN for the free tool; replies; 30 more care-manager emails | 2.4 + (1,500 visits x 15% use x 20% email x 10% trial x 30% paid = 1.4) = 3.8 | 12 |
| 4 | Replies; first two search pages ("how to manage an elderly parent's mail and bills", "Medicare annual notice of change letter explained") | 2.4 | 14 |
| 5 | Replies; care managers start recommending (3 adopters x 6 clients over 5 weeks x 35% = 1.3 a week) | 2.4 + 1.3 = 3.7 | 18 |
| 6 | Replies; $200 ad test at about $1.50 a click [ASSUMPTION]: 133 clicks x 4% trial x 30% paid | 2.4 + 1.3 + 1.6 = 5.3 | 23 |
| 7 | Replies; sibling-invite prompt (10% of paying families bring a second household, about 1 a week) | 2.4 + 1.3 + 1.0 = 4.7 | 28 |
| 8 | Review the funnel; cut the worst channel | 4.7 | 32 |

- Result: about 32 paying families by week 8, 4 to 5 a week. At 4.7 a week (ignoring churn) 100 families arrive near week 22 [ESTIMATE]; section 13's mix is faster than this.
- Channels: r/AgingParents, r/eldercare, the AgingCare forum; Aging Life Care Association care managers; Hacker News Show HN for the free tool; the search intents above; Medicare annual enrollment (October 15 to December 7) letters as a seasonal hook. Antigrift already offers a free checker, so the free tool must explain the letter and say what to do next, not only give a scam verdict.
- Message and offer: "Mom texts a photo; she gets two plain sentences back; you get a card saying what to do, with the number to call and a script. Siblings see who has it." 7-day free trial, $14.99 a month for one parent and up to four relatives, $129 a year, first scam check free, 14-day refund.
- Growth loop after 100: sibling invites (retention more than acquisition), the checker's share link, care-manager referrals; later the estate hand-off to 015 Estate Clerk and employer or bank resale, which are partnerships and not launch dependencies.

### One-week validation test (under $50)
- Build (day 1): a page saying "Pilot. A person reads each letter with AI help and replies within minutes (8am to 8pm). Free for 7 days, then $14.99 a month if you want to continue. Not an automated product yet. Do not send full account numbers; letters are deleted after 30 days." Form: child's name and email, parent's first name and mobile number, relationship, siblings' emails, and a checkbox "my parent has agreed to receive texts from this number". One number: your own line or a free Google Voice number [UNVERIFIED terms for business use]; a $15 prepaid line is the fallback.
- Recruit (days 1 to 3): post once in r/AgingParents (after checking the rules or asking the moderators) and the AgingCare forum, as yourself, with a disclosure line, for 8 adult children whose parent texts them photos of letters. No unsolicited messages, no second accounts.
- Run (days 3 to 7): the first text to each parent asks for a YES reply (consent) and STOP is honored. Reply to each photo within 5 minutes: two plain sentences to the parent and an emailed action card to the child (what it is, due date, who to call, a script). Log minutes per letter and whether the parent or the child sent it.
- Ask (day 7): a Stripe payment link for the first month, $14.99 (refundable), and one question: "if you had to forward the letters yourself, would you still pay $15? yes or no".
- Budget [ESTIMATE]: domain $12; page, form and email on free tiers $0; prepaid line $15 (or $0 on Google Voice); Claude 8 families x 6 letters x ($0.00415 + $0.011) = 48 x $0.0152 = $0.73; Stripe fees on 3 payments 3 x $0.73 = $2.20; contingency $10; total $39.93 ($24.93 with a free line).
- Pass (set in advance), with 8 families onboarded (fewer than 6 means recruiting failed, not the product): at least 5 of 8 parents personally text 4 or more photos in the first 4 days AND at least 3 of 8 children pay AND median human time per letter is 4 minutes or less AND 0 scam letters, by your own judgment, were missed. Fail: 2 or fewer of 8 parents active (the parent-text channel is dead; only a child-upload vault remains) or 0 payments. In between: improve setup help or the message and rerun.

### Build brief (paste into a coding session)
**Product summary.** Parent Mail Desk lets an aging parent text a photo of any letter to one number and get two plain sentences back, while the adult child gets an action card with the sender, amount, due date and a one-tap next step. Siblings share a queue, an assignment board and a searchable vault. $14.99 a month per family; the first scam check is free.

**Liability line (keep visible in the UI, copy and prompts).** It explains, routes and drafts. It never pays, signs, or gives medical, legal or financial advice; scam flags are informational; call scripts and reply drafts use only the letter's content and the family's notes and tell the user to use the number printed on the letter.

**MVP features (each testable)**
1. Inbound photo texts (MMS) to one pooled number, routed to the family by sender number; multi-page letters grouped when images arrive within 10 minutes. Test: 50 test photos reach the right family, none lost.
2. Acknowledgement within 10 seconds and a parent reply (at most 2 sentences, reading grade 6 or below, English or Spanish) within 60 seconds at p95. Test: 50 sample letters meet both limits.
3. Classification and extraction: type (bill, suspected scam, deadline, medical, informational, junk), sender, amount, due date, masked reference. Test: at least 90% type accuracy and 95% exact due dates on 100 letters.
4. Scam check with stated reasons (urgency, gift cards, mismatched phone or domain), informational only. Test: at least 90% recall on 40 known scam letters, at most 5% false positives on legitimate ones.
5. Child action card with one-tap actions: open the payment page printed on the letter, call with a script and the printed number, draft a reply, file to the vault, mark shredded, hand to a sibling. Test: each action logs an outcome.
6. Duplicate and already-paid detection. Test: at least 90% of seeded duplicates caught.
7. Sibling board: assignments, comments, due-date reminders by push and email. Test: a reassigned card reaches the new owner's queue within 10 seconds.
8. Vault with full-text search and zip export for estate use; SSN-like strings redacted in stored text. Test: 20 searches return the right letter; 0 SSN patterns stored.
9. Monthly digest email. Test: correct counts for a seeded month.
10. Consent and privacy: parent opt-in recorded, STOP handling, delete on request within 24 hours, 24-month default retention. Test: STOP halts texts within 1 minute; deletion removes images and text.

**Non-goals.** Paying bills; bank connections; calls made for the user; auto-submitting forms; inbox scanning in v1; medical, legal or financial advice; a native app (use a PWA); Medicare plan comparison (see 037); a voice assistant for the parent; physical mail scanning or forwarding; employer or bank dashboards.

**Core AI loop.** Inputs: MMS images or forwarded email, family notes. Haiku 5.5 vision ($0.10 / $0.50 per 1M) reads, classifies, extracts and runs the scam pattern check; Sonnet 5.5 ($2 / $10) takes a second pass on low-confidence, scam and medical letters and writes child chat, call scripts and drafts; a cached system prompt holds the sender knowledge base. Prompts extract fields with confidence, say what the letter is in two plain sentences, give reasons rather than verdicts for scam flags, and write scripts only from letter content. Outputs: parent SMS reply, child card, vault record. Human checkpoints: the child confirms every action; the parent is never asked to do more than read; the founder reviews 20 random cards a week; low-confidence letters go to the child as "please check".

**Data model.** Family, Parent, Member (child or sibling), PhoneRoute, Letter (image, text, type, sender, amount, due date, confidence), Card (action, status, assignee), ActionLog, Sender (knowledge), Reminder, VaultFolder, Consent, AuditEvent, Subscription.

**Integrations and stack.** Twilio Messaging with MMS webhooks ([docs](https://www.twilio.com/docs/messaging)) and A2P 10DLC registration, filed in week 1 because approval can take days or weeks [UNVERIFIED]; Anthropic API ([docs](https://platform.claude.com/docs)); Stripe Billing ([docs](https://docs.stripe.com/billing)); Resend email ([docs](https://resend.com/docs)); Web Push for the PWA. Next.js PWA on Vercel (about $20), Supabase Postgres, Auth and Storage with row-level security per family (about $25), a small worker on Fly.io or Vercel cron for the queue (about $10), Sentry and PostHog free tiers: about $60 to $80 a month before model and Twilio usage [ESTIMATE, list prices not re-checked].

**Evals.** (1) Classification: 100 letters (60 redacted real from volunteers, 40 synthetic): at least 90% type accuracy, 95% exact due dates. (2) Scam: 40 known scam letters or texts plus 40 legitimate ones: at least 90% recall, at most 5% false positives. (3) Reply constraints: 50 replies, at most 2 sentences, grade 6 or below, no "pay" or "ignore" instruction on scam or medical letters. (4) Duplicates: 20 seeded; at least 90% caught. (5) Latency: p95 parent reply within 60 seconds.

**Build plan (6 weeks).** Week 1: Twilio inbound, number routing, A2P registration, data model, auth. Week 2: extraction, classification, parent reply. Week 3: child queue, actions, assignments. Week 4: scam check, call scripts, drafts. Week 5: vault, search, digest, billing. Week 6: evals, pilot with 5 real families, launch the free checker.

**Key risks to test first.** (1) Whether parents send photos at all (the validation test). (2) Antigrift and others already covering the text-a-photo scam check, so differentiate on action depth. (3) Scam false negatives. (4) Security of SSNs and medical letters. (5) Churn when the caregiving episode ends. (6) Free assistants and household agents.

**Notes for the main researcher.** Antigrift ships the parent-side text-a-photo channel ($9 and $19 a month) and a free checker, so section 7's "only real twist" already exists for scams; what remains is the action queue, assignments, scripts and vault, and Novelty 2 and Whitespace 2 look right or generous. Margin is about 70% to 79%, not 84%, once infrastructure and support are counted; a dedicated number per parent costs more than the AI. About 32 paying families by week 8 and 100 near week 22 replace section 13's faster mix.

## Red team
Skeptical-investor review on 2026-11-01 (full text: `research/RED_TEAM_A.md`). Verdict: **pass**.

**Top attacks (summarized):**
1. **It solves the easy half.** LIFE-14 asks to summarize the letter and to call customer service; LIFE-25 adds proxy two-factor login and LIFE-26 reconciliation. The product stops before calling, proving authority and paying.
2. **No one is shown paying.** Paid neighbors sell through institutions, Antigrift ($9 to $19 a month) already runs the text-a-photo channel, and free assistants explain letters.
3. **Adoption is heavier than planned.** A parent who already sends photos to a child has little reason to adopt a new number, so the child may pay for a channel the parent does not use.
What would change the red team's mind: a concierge pilot where 6 of 10 parents text 6+ photos unprompted over two weeks and 4 children pay $15 knowing the product will not call, pay or file; or a bank, plan or employer paying per family.

**Response (main researcher):**
- Attacks 1 and 2 land. Pain drops from 4 to 3 (the product as scoped leaves out the most painful step) and willingness to pay from 3 to 2.
- Attack 3 is answered by the deep dive's concierge test, which already measures unprompted parent texting before any build.
- Re-scope worth testing: add the hard half (a three-way call where the agent dials and waits on hold with the parent on the line, plus the authorized-representative forms each company needs), which is where an adult child's time actually goes; or sell per family through employers' caregiver benefits.
