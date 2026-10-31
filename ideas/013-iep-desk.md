---
id: "013"
slug: iep-desk
name: IEP Desk
one_liner: "Keeps special-education caseloads compliant: IEP timelines, accommodation sheets for every teacher and substitute, progress data by voice."
target_user: "Special-education case managers, and the principals or SPED directors who answer for IEP compliance"
form_factor: "web app"
lens: "Pain-first"
frontier: false
competition: "CROWDED"
confidence: "LOW"
status: "killed"
signals: [PRO-201, PRO-202, PRO-203, PRO-204]
scores:
  pain: 4
  evidence: 3
  ai_leverage: 4
  whitespace: 2
  novelty: 2
  why_now: 3
  solo_feasibility: 3
  distribution: 2
  wtp_economics: 2
  scale_defensibility: 2
total: 55.8
price_hypothesis: "$12/month per case manager, or $99/year per case manager on a school plan"
model_cost_per_user_month: "$1.02"
gross_margin: "82%"
mvp_weeks: 8
deep_dive: false
red_team: false
---

# IEP Desk

> **Main-thread review, 2026-10-31: KILLED.** CROWDED. MagicSchool, Frontline and PowerSchool special-education modules and funded AI entrants serve IEP paperwork, and student-data privacy rules block the bottom-up teacher sale this idea relied on; there is no clear payer below the district. The file is kept as a record of the competition check.

## 1. One-liner
Keeps special-education caseloads compliant: IEP timelines, accommodation sheets for every teacher and substitute, progress data by voice.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 4 | Weekly, about 60 unpaid hours (PRO-202), legal deadlines; but the sufferer is not the buyer |
| Evidence quality | 2 | 3 | 4 recent signals, 3 strong, all from r/Teachers; none shows willingness to pay |
| AI leverage | 2 | 4 | Long free-form IEPs become structured accommodations, notes and drafts; without the model it is manual entry |
| Whitespace | 2 | 2 | CROWDED: systems of record (Frontline, PowerSchool), MagicSchool, funded AI-native entrants |
| Novelty of insight | 1 | 2 | "Admin, not lesson plans" is now the common pitch; the sub-sheet and voice-data angle is a small twist |
| Why now | 1 | 3 | Cheap long-context extraction and voice at $0.003/min; teachers openly ask; others are also building |
| Solo feasibility | 2 | 3 | Product is 8 weeks; student-data privacy approvals are the hard, slow part |
| Distribution | 2 | 2 | Teachers cannot legally upload IEPs on their own; districts need data agreements; r/Teachers helps awareness only |
| Willingness to pay and unit economics | 2 | 2 | Margin is high but the payer is unclear (teacher vs district) and MagicSchool is free for teachers |
| Scale and defensibility | 2 | 2 | Incumbents can add AI inside the system of record schools already buy |
| **Total** | | **55.8** | |

Confidence: LOW (the key unknown is who is allowed and willing to pay). FRONTIER: no.

## 3. The problem
- Who: special-education case managers (caseloads near 30, PRO-202), the gen-ed teachers who must follow each accommodation, and principals who must prove compliance.
- Frequency and cost: IEP and ARD meetings eat conference periods, so paperwork moves to personal time, "often pushing 60 hours a week" (PRO-202). One principal wants all 300 IEPs in emergency sub plans (PRO-203).
- Workaround: Word and Excel trackers, binders, copy-paste from the district system, accommodation lists retyped for each sub.

## 4. Evidence
Four independent signals, all from r/Teachers, 2025-08 to 2026-03; three are strong.
- **PRO-202** (strong, 2025-08-23, 14 pts / 35 comments): "The result of this, as anyone who is a SPED teacher understands, is that I am forced to take excessive paperwork come with me and work for free on my own time, often pushing 60 hours a week." Shows the pain is unpaid time.
- **PRO-203** (strong, 2025-10-11, 49 pts / 150 comments): "Now the principal is expecting that we get IEPs from our co-teachers for all students in the school and put them in our emergency plans “just in case”, since once per month we could in theory have any of our 700+ students for a 45 min class. Should a sub really have access to 300 student IEPs “just in case”?" Shows the accommodations-at-a-glance gap, and the privacy question.
- **PRO-201** (strong, 2026-03-11, 345 pts): "Planning the lesson is the fun part. The part that causes burnout is the admin bloat: tracking attendance, writing behavioral reports, mapping standards, and updating parents." Teachers want admin help, not lesson help.
- **PRO-204** (medium, 2026-03-16): "I became a teacher to actually teach, but some weeks it genuinely feels like I'm a data entry clerk who occasionally gets to stand in front of kids." Weekly list: progress reports, IEP documentation, parent logs.
- Gap: no signal says a teacher or school would pay, or that a district would allow an outside tool to hold IEP data.

## 5. The product
- Finished outcome: a case manager opens one screen that shows what is due, who needs what accommodation today, and which progress reports are ready to review.
- Core AI loop: IEP PDF (names and IDs redacted in the browser before upload) -> model extracts accommodations, services, goals, key dates and team, each quoted with page reference -> accommodation matrix per teacher, class period and substitute -> deadline tracker from dates plus a state rule table -> case manager dictates session data after groups ("goal 2, 4 of 5 trials, needed two prompts") -> structured rows -> model drafts progress-report narratives and meeting notices from the data and district templates -> teacher reviews, edits, approves.
- Interaction: mobile web for voice capture, desktop for review; one-page "sub packet" printouts and shareable teacher links.
- Day in the life: at 7:10 Mr. Alvarez sees three annual reviews due within 21 days and one reevaluation 4 days overdue, with the rule and date source shown. He prints Tuesday's sub packet: per period, four students, one quoted line each. After lunch groups he dictates 90 seconds of data; Friday ten progress drafts wait, he edits two.
- Liability line: the tool organizes, extracts, calculates dates and drafts from teacher-entered data. It never writes goals, decides eligibility, services or placement (IEP team decisions), never interprets clinical data, and gives no legal or medical advice. Deadlines show their rule source and need teacher confirmation; extracted accommodations link back to the IEP text.

## 6. Why the LLM is load-bearing
IEPs are long, free-form and vary by state and district template; accommodations hide in prose. The model normalizes them into a matrix, turns dictated notes into goal-linked data and drafts narratives. Remove it and the product is a manual-entry tracker, which is what incumbents already sell.

## 7. The insight
The unsolved gap is the last mile of the IEP system of record: the gen-ed teacher and substitute who need accommodations at a glance (PRO-203, 150 comments) and the case manager's data capture. Honest correction to the concept note: the main obstacle is not the AI, it is the data-privacy gate and the lack of an individual payer.

## 8. Why now, and why this does not exist yet
Long-context extraction and cheap transcription ($0.003/min) make per-student documents affordable, and teachers openly ask for admin help (PRO-201). It "does not exist" only in a narrow sense: AI-native entrants are appearing in 2026 (see section 10) and systems of record are the natural place for it. Most of this was buildable in 2023; the change is cost and teacher appetite.

## 9. Inspiration and derivation
Parents: Frontline and PowerSchool special-education systems (compliance records), AbleSpace (goal tracking), MagicSchool and Brisk (teacher AI). Changed: user (the case manager and sub, not the district office), interaction (voice capture, printable sub packets), business model (seat or school plan instead of district license), channel (teacher-led, with a no-names lead magnet).

## 10. Competition check
Queries run (2026-10-31): (1) web "AI IEP software special education case manager compliance deadlines progress monitoring MagicSchool Brisk SchoolAI"; (2) Product Hunt via search, "IEP special education teachers AI paperwork" restricted to producthunt.com (no IEP product); (3) YC directory mirror https://yc-oss.github.io/api/companies/all.json with `IEP|special education|SPED|special needs|disabilit` (no IEP company) and `K-12|teachers|school district|classroom` from 2022 (Scout, Winter 2025, a K-12 student information system; Edexia and Frizzle, AI grading); (4) web "special education case management software IEP compliance Frontline PowerSchool Special Programs Embrace SpedTrack pricing per student"; (5) web "AI special education startup raises seed IEP writing compliance teachers paperwork funding 2026"; (6) App Store `--find "IEP special education"`; (7) homepages of MagicSchool, SchoolAI and Brisk.

| Product | What it does | Price | Difference |
|---|---|---|---|
| [MagicSchool](https://www.magicschool.ai/) | District AI platform, 80+ teacher tools; third parties describe IEP goal and accommodation drafting and warn output may need manual editing for compliance ([Progress Learning](https://progresslearning.com/news-blog/ai-iep-goal-generator/), [UNVERIFIED]) | "Free for teachers"; districts get quotes | Sells to districts with privacy terms; drafts content, no caseload compliance tracker |
| [Brisk](https://www.briskteaching.com/) | Free AI tools for teachers, "Trusted in 10,000+ Districts" | Free tier | A comparison blog says no IEP tools ([source](https://aitoolsbakery.com/blog/magicschool-vs-brisk/), [UNVERIFIED]) |
| [SchoolAI](https://www.schoolai.com/) | Teacher and student AI spaces; [raised $25M](https://www.homebrew.co/blog-posts/schoolai-secures-usd25-million-to-help-teachers-and-schools-reach-every-student) | Not found | No IEP features found |
| Frontline Special Education ([G2](https://www.g2.com/products/frontline-special-education-management-software/pricing)), PowerSchool Special Programs ([TrustRadius](https://www.trustradius.com/compare-products/powerschool-unified-classroom-special-programs-vs-recordables)), [SEAS](https://www.capterra.com/p/37129/SEAS/), [EasyIEP](https://www.softwareadvice.com/k-12/easyiep-profile/) | Systems of record: IEP forms, compliance dates, reports | Quote only; one Ohio consortium lists [$1.25 to $1.40 per student](https://www.swoca.net/fee-schedule/) with $1,750 to $2,000 minimums; reviewer estimates [$2,000 to $50,000+ a year](https://www.itqlick.com/Products/22453) | Own the district contract and data; weak on teacher-level convenience |
| [AbleSpace](https://apps.apple.com/us/app/ablespace-iep-goal-tracking/id1662372988) (iOS, since 2023, 5 ratings) | Goal data collection, graphs, caseload tools | Free listing | Closest direct tool for case managers; tiny on the store |
| [Journify Learning](https://www.vcbacked.co/company/journify-learning), [Scholar Education](https://www.trysignalbase.com/news/funding/scholar-education-raises-2m-seed-round) | AI assistants for special education; $3.8M seed (May 2026) and $2M seed (2026-09-24) per aggregators | Not found | Funded, AI-native, same buyer; amounts unverified |

Classification: CROWDED. Platform risk: Frontline or PowerSchool adding AI inside the system schools already hold, and MagicSchool adding IEP workflows, are both plausible within 12 months; either caps scale at 2 and whitespace at 3 (scored 2 here).

## 11. Business model
- Payer: starts with the case manager at $12 a month [ASSUMPTION, no evidence teachers pay]; real money is a school or district plan at $99 per case manager per year. Anchor: full systems of record cost about $1.25 to $1.40 per student (30 students = $38 to $42 a year), so $99 is a premium add-on.
- Model cost per case manager per month [ESTIMATE], prices from `research/LANDSCAPE.md`: 3 IEP extractions on Sonnet 5.5 at 12,000 in + 2,000 out = $0.024 + $0.020 = $0.044 each, $0.132; 258 voice notes (30 students x 2 a week) at $0.0015 transcription = $0.387 and Haiku structuring at $0.00015 = $0.039; 10 progress drafts on Sonnet at 8,000 in + 1,200 out = $0.028 each, $0.28; 5 sub packets at 6,000 in + 2,000 out = $0.032 each, $0.16; 100 Q&A on Haiku with cached context $0.018; notices $0.005. Total about $1.02.
- Margin at $12: payment fee 2.9% + $0.30 = $0.65, support allowance $0.50 [ASSUMPTION]; ($12 - 1.02 - 0.65 - 0.50) / $12 = 82%.

## 12. Market size
[ESTIMATE] About 7.5M US students receive IDEA services [UNVERIFIED, from memory] / 30 per case manager (PRO-202) = 250k case managers x $99 = $24.8M a year. Realistic 2% in three years = 5,000 seats = about $0.5M ARR. A small niche unless it widens to gen-ed teachers and districts.

## 13. Go-to-market
- First 100 customers: posts and answers in r/Teachers and r/specialed (PRO-202 was cross-posted there, 31 comments), state special-education association conferences and newsletters, principal groups; a free "accommodations at a glance" sheet maker that takes pasted, name-free lines as the lead magnet; pilots paid from a principal's school budget.
- Growth loop: every sub packet and gen-ed sheet carries the product name and a link; gen-ed teachers who like it ask their case manager to sign up.

## 14. Moat and scale path
State rule tables, district templates, signed data agreements (trust and switching cost) and longitudinal progress data. Scale: gen-ed teacher seats, 504 plans, district dashboards. Moat is thin against incumbents; compliance posture is the real asset.

## 15. Solo feasibility
- MVP, 8 weeks: browser redaction and IEP extraction on 20 sample IEPs (weeks 1-2), accommodation sheets (3), timelines for 3 states starting with Texas ARD (4), voice capture (5), progress drafts (6), privacy pack with data map, no-training clause and agreement template (7), pilot (8).
- Running cost before revenue about $60 a month (hosting, database, transcription and model testing).
- Hardest risk: school approval of any outside tool, then extraction recall: a missed accommodation is worse than no tool, so target 98%+ recall on a test set and always link to the source text.

## 16. Pre-mortem
1. Data gate: districts bar uploading IEPs to new vendors and individual teachers cannot consent, so bottom-up growth stalls and the sale becomes long procurement.
2. Incumbent bundle: the system of record or MagicSchool ships accommodation sheets and AI notes inside contracts already signed.
3. Error liability: a wrong deadline or missed accommodation creates compliance exposure and risk managers say no.

## 17. Cheapest validation test
3 weeks, under $100 plus about 30 hours. Make accommodation sheets and timeline views by hand with an LLM from 10 synthetic or public sample IEPs; show them to 15 case managers, principals or SPED directors found through teacher communities. Pass: at least 3 of 15 principals or directors agree to a pilot or prepay $99, and at least 8 of 15 teachers say they would use it weekly. Kill if none of the 15 can legally use an outside tool.

## 18. Open questions
- Who is the first payer, and what do district data agreements require before an outside tool sees an IEP?
- Is the sub-packet sheet a sharp enough wedge against the reports the system of record already prints?
- Can redaction in the browser (or on-device models) keep student data off the server entirely?
- Recommendation: CROWDED, so narrow to the sub-packet and accommodation sheet sold to principals, or drop it for the parent-side or non-school ideas.
