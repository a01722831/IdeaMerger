---
id: "017"
slug: real-applicant
name: Real Applicant
one_liner: "Small employers drown in AI-written applications; applicants take a short role-specific voice screen and the owner reviews a ranked shortlist."
target_user: "Small employers (5-100 staff) and small staffing agencies that post jobs on open boards and have no enterprise ATS"
form_factor: "web app"
lens: "Pain-first"
frontier: false
competition: "CROWDED"
confidence: "MED"
status: "killed"
signals: [PRO-127, PRO-128, PRO-129, PRO-130, PRO-131, AI2-23, AI2-24, AI2-25]
scores:
  pain: 3
  evidence: 4
  ai_leverage: 4
  whitespace: 1
  novelty: 2
  why_now: 4
  solo_feasibility: 3
  distribution: 2
  wtp_economics: 2
  scale_defensibility: 2
total: 53.7
price_hypothesis: "$79/month for 30 completed screens, or $3 per extra completed screen"
model_cost_per_user_month: "$3 to $9 (30 screens)"
gross_margin: "85% to 93%"
mvp_weeks: 6
deep_dive: false
red_team: false
---

# Real Applicant

> **Main-thread review, 2026-10-31: KILLED.** CROWDED. Greenhouse Voice AI (September 2026) sells the same role-specific voice screen to any ATS, and rivals charge $1 to $6 per screen. The file is kept as a record of the competition check.

## 1. One-liner
Small employers drown in AI-written applications; applicants take a short role-specific voice screen and the owner reviews a ranked shortlist.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Every open role gets hundreds or thousands of look-alike applications, but small employers hire a few times a year, so the pain comes in bursts. |
| Evidence quality | 2 | 4 | Eight recent signals (2025-06 to 2026-08, one strong) plus new competition-side evidence; no first-person statement of willingness to pay for screening. |
| AI leverage | 2 | 4 | The voice conversation, question generation and consistency scoring are the product; a human reviewer is the fallback, so not a 5. |
| Whitespace | 2 | 1 | Greenhouse Voice AI is sold standalone for other ATSs, and Ribbon, Alex, Classet, Hyring and others sell the same screen at $1 to $6 each. |
| Novelty of insight | 1 | 2 | "Add a little synchronous effort to restore signal" is now the common vendor pitch. |
| Why now | 1 | 4 | Realtime voice at about $0.05/min and AI-written resumes arrived together; this was not possible in 2022. |
| Solo feasibility | 2 | 3 | A link-based voice screen is 6 weeks; applicant drop-off, bias exposure and deepfake detection are the hard parts. |
| Distribution | 2 | 2 | Small employers are reachable through communities and SEO, but the category is noisy and ATS vendors bundle. |
| Willingness to pay and unit economics | 2 | 2 | Good margin, but the market price is $1 to $6 a screen, employers hire rarely, and churn between hiring bursts is high. |
| Scale and defensibility | 2 | 2 | Platform risk from ATS vendors (capped at 2); the question bank and outcome data are thin moats. |
| **Total** | | **53.7** | |

Confidence: MED. FRONTIER: no. Honest read: CROWDED; section 18 recommends against building it as a standalone.

## 3. The problem
- Who: owners and hiring managers at small employers, and recruiters at small staffing and HR agencies, who post to open job boards.
- Cost: hours of screening per role, interviews wasted on fakes, and bad hires. One hiring manager says the cost of a fake hire is "time wasted, needing to open the role once more" (AI2-24); another company now requires an on-site interview (AI2-23). The alternative spend is a recruiter fee of GBP 12 to 25K per senior hire (PRO-134).
- Workarounds: knockout questions, paid job-board filters, an on-site interview as a first step, ignoring most applications, Google Forms pipelines (PRO-131).
- Gap: a cheap, applicant-side step that costs a fraud farm more than a copy-paste does, and gives the owner a short, evidence-linked shortlist.

## 4. Evidence
- **AI2-23** (strong, 2026-03-26, HN): a company with a contracted recruiter reports scam and fake candidates and AI-run interviews on video. "We've mandated at least one on-site interview just so we can be sure we're getting actual people." https://news.ycombinator.com/item?id=47534241
- **PRO-127** (medium, 2025-09-17, Ask HN, 28 comments): "My company recently posted an open role and we've been inundated with AI-generated applicants. 404 LinkedIn profiles, near-copies of known real applicants, no-show interviews, artificial voices, the whole gamut." https://news.ycombinator.com/item?id=45270331
- **PRO-128** (medium, 2025-06-24, Semafor): "Applications submitted via LinkedIn jumped 45% this year, with the site now clocking 11,000 applications per minute". https://www.semafor.com/article/06/24/2025/recruiters-swamped-with-ai-generated-job-applications
- **PRO-129** (medium, 2026-02-17, News 12, Robert Half): resumes "looking very similar, that it's taking companies longer to go through and longer to vet things to make sure people really have the skills that are on their resume". https://westchester.news12.com/hiring-experts-warn-aicreated-resumes-are-creating-bottlenecks
- **AI2-25** (medium, 2026-08-11, HN): "whenever we put up a job ad it's filled with thousands of LLM generated fake candidates in a few days." https://news.ycombinator.com/item?id=49265580
- **AI2-24** (medium, 2026-03-18, HN): fake hires fail in weeks; the cost is "time wasted, needing to open the role once more to find a real candidate". https://news.ycombinator.com/item?id=47428980
- **PRO-130** (weak, 2025-09-17) recruiter with 5,000+ applications per role; **PRO-131** (weak, 2026-04-18) about 1,000 applicants per post and a pipeline that breaks at later stages. https://news.ycombinator.com/item?id=45271736 and https://news.ycombinator.com/item?id=47814216
- New evidence (not in SIGNALS.md), vendor-side and unverified: search summaries repeat a Gartner projection that one in four candidate profiles will be fake by 2028, and a Greenhouse report that 31% of US hiring managers interviewed someone using a fake identity [UNVERIFIED primary, seen only through vendor blogs]. Treat as context, not proof.

## 5. The product
- What it does: the employer pastes a job post and gets an apply link. Each applicant does a 5-8 minute voice (or typed, on request) screen with questions generated from the job (a scenario, a "walk me through your last X", a check of one resume claim). The model scores substance and resume consistency, flags repeated or scripted answers across applicants, and shows the owner the top 10 with transcript quotes as evidence.
- Core AI loop: job text -> role-specific question set and rubric (the owner edits it) -> live voice conversation with follow-ups -> transcript -> rubric score plus consistency findings -> ranked list -> owner marks hire or reject -> rubric adjusts to the owner's choices.
- Interaction model: apply link in the job ad; applicants need only a browser. Owner sees a ranked inbox and an email digest. Everything the AI says is logged; no automatic rejections.
- Form factor: web app (browser WebRTC for the applicant, no phone costs).
- Day in the life: an 8-person HVAC contractor posts a dispatcher role, gets 600 applications in three days, and adds the link. 140 applicants finish the screen. The owner opens 12 ranked transcripts, calls 5, and hires one.
- Safety lines: an accessible typed alternative, no scoring on accent or voice quality, no biometric identity claims in the MVP, and disclosure that an AI conducts the screen.

## 6. Why the LLM is load-bearing
- Question generation from a job and an adaptive follow-up conversation are language and speech work; a fixed quiz would be copied and answered by an LLM within hours.
- Consistency checking (does the story match the resume, do many applicants give the same scripted answer) needs reading across transcripts.
- Without the model, what remains is a knockout form that AI already defeats, which is the problem.

## 7. The insight
- Cheap applications broke the filter, so a small amount of synchronous, role-specific effort restores signal for the employer's time. Honest limit: this is the common vendor thesis now; the open angle is price and simplicity for owners with no ATS, which is a modest business.

## 8. Why now, and why this does not exist yet
- Why now: GPT Live bills $0.05 a minute and Gemini 3.8 Live about $0.005 in and $0.018 out (`research/LANDSCAPE.md` section 6); application volume is up (PRO-128).
- Why it already exists: it was built by many teams in 2025 to 2026, including Greenhouse, a well-known ATS vendor (section 10). The honest answer to "why not yet" is that it is already here.

## 9. Inspiration and derivation
- Parents: Greenhouse Voice AI, Ribbon and Alex (AI phone and video screens), Proof and Sardine (identity fraud checks), oral exams.
- Changed: target user (owners with no ATS and no HR staff), channel (apply link in the job ad and community-led), business model (flat bundle for bursts rather than per-seat enterprise). The core job is unchanged, so only two of the five parts changed.

## 10. Competition check
Queries run:
1. WebSearch: "AI voice interview candidate screening fake candidates deepfake identity verification hiring small business applicant fraud tool 2026"
2. WebSearch (Product Hunt): "site:producthunt.com AI interviewer screen applicants fake candidates AI-generated applications"
3. WebSearch (YC directory): "site:ycombinator.com/companies AI voice interviewer recruiter screening candidates fraud detection"
4. WebSearch (ATS marketplaces): "Greenhouse OR Workable OR Ashby OR Lever marketplace candidate fraud detection identity verification AI interview integration 2026"
5. WebSearch: "AI phone screening interviews hourly hiring small business pricing per interview Ribbon OR Tenzo OR Humanly OR Alex OR Paradox"
6. WebFetch of the Greenhouse Voice AI page (September 2026) and of Alex Verify.

| Product | What it does | Price | How it differs |
|---|---|---|---|
| [Greenhouse Voice AI](https://www.greenhouse.com/product-features/voice-ai-now-works-with-60-ats-platforms) (Sept 2026) | Applicants complete a conversational application instead of a resume; includes a resume authenticity layer and voice signals that flag responses that may not be the candidate's own (page summary) | not stated; "Available as an add-on to Greenhouse, or as a standalone product for teams on a different ATS."; works with 60+ ATSs | The incumbent shipping this exact idea, sold to non-customers too |
| [Alex](https://www.alex.com/verify) (YC, formerly Apriora, [YC page](https://ycombinator.com/companies/apriora)) | AI recruiter with live video interviews; Verify scores each application for fraud risk (email age, VOIP phone, VPN, footprint); customers named include EY, Upwork, Randstad | demo only | Funded, enterprise and staffing focus |
| [Lightscreen AI](https://ycombinator.com/companies/lightscreen-ai) (YC), [Symphony](https://ycombinator.com/companies/symphony) (YC) | Voice interviewer with multimodal cheating detection for technical roles; voice screens for customer-facing roles | n/a | Direct, narrower verticals |
| [Phenom Fraud Detection Agent](https://www.mychesco.com/a/news/regional/phenom-targets-hiring-fraud-with-ai-screening-agent/), [Proof](https://proof.com/blog/how-to-catch-candidate-fraud-without-changing-your-lever-workflow) (Lever integration), [Sardine](https://sardine.ai/candidate-fraud) | Identity, liveness and behavioral checks across hiring stages | not visible | Identity-fraud layer; the hard part this idea would not build |
| [Ribbon](https://ribbon.ai/blog/cost-analysis-conversational-ai-screening), PhoneScreen AI, [Hyring](https://hyring.com/ai-phone-screener), Classet, InterviewFlowAI | AI phone and web screens | Ribbon $3 per successful screen; PhoneScreen AI $3; Hyring from about $1 to $5; Classet from $599/month for 200 interviews, $3 overage; InterviewFlowAI $0.99 (vendor pages, via search summary) | Priced at exactly the small-employer level this idea targets |
| Product Hunt: [AI Interviews](https://www.producthunt.com/p/ai-interviews) (proctoring flags; from $3 per interview per its listing, another listing says $6 for 1 to 49 interviews), [Screenz](https://www.producthunt.com/p/screenz-live-ai-recruiter-interviews/screenz-2), [Truely by Validia](https://www.producthunt.com/p/truthful-by-validia/truely-by-validia) (AI-assistant detection in interviews) | Screens and anti-cheating | $3 to $6 | Crowded launch-site category |
| [Metaview](https://www.metaview.ai/resources/blog/deepfake-interviews), Gem, [Sapia.ai](https://sapia.ai/?p=10750), InCruiter | Recruiter tooling with deepfake or AI-answer detection (vendor claims, e.g. Sapia's 98% accuracy claim [UNVERIFIED]) | n/a | More entrants |

Classification: **CROWDED**. The ATS leader sells the product standalone, YC companies are in it, and price per screen is $1 to $6.

Platform risk: very high. Greenhouse already ships it, and Workday, iCIMS, LinkedIn and Indeed hold the application flow and can add a "verified applicant" step [ASSUMPTION]. Frontier labs are unlikely to build it directly, but ChatGPT and Claude voice can power DIY versions. Per the rubric this caps Scale and defensibility at 2 and Whitespace at 3; the number of cheap rivals puts Whitespace at 1.

## 11. Business model
- Payer: the employer (or agency). Price: $79/month for 30 completed screens, $3 for each extra, agency plan $249/month for 150. Anchors: Ribbon and PhoneScreen AI $3, Classet $599/month, AI Interviews from $3, recruiter fees of GBP 12 to 25K per senior hire (PRO-134).
- Model cost per screen [ESTIMATE]: 6-minute call. Gemini 3.8 Live: 6 min x $0.005 = $0.03 in plus 3 min speech x $0.018 = $0.054 out; scoring on Sonnet 5.5, 3,500 in x $2/1M + 600 out x $10/1M = $0.007 + $0.006 = $0.013. About $0.10 per screen. On GPT Live: 6 x $0.05 = $0.30 + $0.013 = $0.31.
- Per employer per month (30 screens): $3 on Gemini, $9 on GPT Live. Question generation per job adds under $0.05. No telephony in the MVP.
- Gross margin [ESTIMATE]: ($79 - $3 - $2.59 Stripe) / $79 = 93%; with GPT Live ($79 - $9.3 - $2.59) / $79 = 85%. Extra screens at $3 against $0.10 to $0.31 of model cost keep margin near 90% to 97% before card fees (billed monthly in aggregate).

## 12. Market size
- Buyers [ESTIMATE]: assume 1.0M US employers with 5 to 100 staff post at least one open-board job a year [ASSUMPTION, no source checked]. Assume 10% suffer enough applicant volume to pay = 100K. At $79 x 12 months only during hiring bursts, say 4 months a year = $316 a year per customer.
- Revenue: 100K x $316 = $31.6M. At 3% penetration (3,000 customers) = $0.95M ARR.
- Reading: a thin market for a solo business unless agencies (more screens per month) are the focus.

## 13. Go-to-market
- First 100: (1) r/smallbusiness, r/recruiting and r/humanresources threads where owners ask how to screen hundreds of applicants, using a free "paste a job post, get 5 role-specific screening questions" tool, about 40; (2) Show HN and Ask HN threads like PRO-127 where employers share workarounds, about 20; (3) SEO on "how to screen 500 applicants", "fake job applicants", "AI generated resumes how to detect", about 25; (4) staffing and HR-agency communities, about 15.
- Growth loop: job posts carry the apply link; applicants who finish see a "powered by" line and a free practice mode, which spreads among job seekers, but a negative applicant reaction is the main risk.

## 14. Moat and scale path
- Moat: per-role question banks, hire/no-hire outcome data (which answers predicted a good hire), and employer-specific rubrics. Weak next to an ATS with outcome data.
- Scale path: agency edition with client portals, then identity verification partners. Both put the product against funded rivals.

## 15. Solo feasibility
- MVP (6 weeks): job-to-questions generator, WebRTC voice agent on a realtime model API, transcript store, rubric scoring, cross-applicant duplicate and scripted-answer detection, ranked inbox, typed fallback, consent and disclosure screens.
- Running cost before revenue: about $60 to $150 a month (hosting, 300 pilot screens x $0.10 to $0.31 = $30 to $93).
- Hardest risks: applicant drop-off, fairness and legal exposure for automated screening (the EU AI Act treats recruitment AI as high risk and some US cities require bias audits [UNVERIFIED here]), and being fooled by voice cloning.

## 16. Pre-mortem
1. Applicants refuse a voice screen; completion under 30% and good people drop out.
2. Greenhouse, Ashby and others bundle the same thing; small employers use a free ATS feature or ChatGPT.
3. A discrimination complaint (accent, disability) or a deepfake that passes ends trust.

## 17. Cheapest validation test
- What: recruit 5 small employers with an open role from the communities above; add a typed-or-voice screen link to their ad; compare the ranking with their own shortlist and measure completion.
- Cost: about $30 in model calls. Duration: 3 weeks.
- Pass: at least 40% of applicants who open the link finish, at least 70% of the interviewees the owner picks are in the AI's top 10, and at least 3 of 5 employers pay $79 for the next role. Fail: completion under 25% or fewer than 2 employers would pay.

## 18. Open questions
- Recommendation: do not build this as a standalone company. It is CROWDED, the incumbent ATS sells it separately, and the price per screen has fallen to $1 to $3. A narrower wedge could be an owner-friendly typed-or-voice screen for employers with no ATS at a flat $29 to $49 a month, but the market and moat are thin. Kill unless the section 17 test shows completion above 40% and payment above $49.
- Do small employers perceive fraud as their problem, or only tech companies hiring remote engineers?
- What do applicants think of an AI screen, and does a disclosed AI hurt the employer brand?
- Which laws apply to a US small employer using an AI screen in each state?
