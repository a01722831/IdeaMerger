---
id: "018"
slug: viva-voce
name: Viva Voce
one_liner: "After a student submits work, a short realtime voice conversation with an AI examiner checks they understand it."
target_user: "College instructors and high-school teachers who assign written or project work and suspect AI authorship"
form_factor: "web app"
lens: "Newly possible"
frontier: false
competition: "WEAK DIRECT"
confidence: "MED"
status: "developed"
signals: [AI2-52, AI2-47, AI2-50, AI2-54, AI2-48, AI2-49]
scores:
  pain: 4
  evidence: 3
  ai_leverage: 5
  whitespace: 2
  novelty: 2
  why_now: 4
  solo_feasibility: 3
  distribution: 2
  wtp_economics: 2
  scale_defensibility: 2
total: 58.9
price_hypothesis: "$1.50 per completed viva (5-8 minutes); semester pack of 100 for $129"
model_cost_per_user_month: "$15 to $40 per 100 vivas"
gross_margin: "66% to 86%"
mvp_weeks: 6
deep_dive: true
red_team: false
---

# Viva Voce

## 1. One-liner
After a student submits work, a short realtime voice conversation with an AI examiner checks they understand it.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 4 | Acute during grading periods (a third of one class, hundreds of hours of paperwork) but seasonal, and the instructor is not the budget holder. Calibrated 3 to 4: integrity work hits every assignment (AI2-47, AI2-48 strong) |
| Evidence quality | 2 | 3 | Six cited signals (two strong, all instructor-side, four from 2026-10) plus a published pilot; no statement of willingness to pay. |
| AI leverage | 2 | 5 | The voice examiner and rubric scoring are the product; a human reviews the flags, so not a 5. Calibrated 4 to 5: the voice examiner is the product; without the model nothing is left |
| Whitespace | 2 | 2 | Early direct entrants (OralExam.AI, verballi, better-ed) and a free published recipe, but no funded leader or LMS-native tool found. Calibrated 3 to 2: early direct rivals (OralExam.AI, verballi, better-ed) and a free NYU recipe at $0.42 per student |
| Novelty of insight | 1 | 2 | Oral defense as an authorship test is well known and now studied in papers; the twist is its $0.15 to $0.42 cost. |
| Why now | 1 | 4 | Realtime voice at $0.05/min or less and the AI-authorship crisis arrived together; one NYU pilot ran 36 exams for $15. |
| Solo feasibility | 2 | 3 | A web voice agent is 6 weeks; LMS integration, student privacy and accommodations add risk. |
| Distribution | 2 | 2 | Instructors are reachable in communities and by SEO, but schools gate student-data tools and the culture is wary of AI. |
| Willingness to pay and unit economics | 2 | 2 | An instructor can copy the NYU setup for about $0.42 a student; institutions have budgets but buy slowly. |
| Scale and defensibility | 2 | 2 | DIY recipe, LMS vendors and AI labs can add a "defend your work" mode; the moat is thin. |
| **Total** | | **58.9** | |

Confidence: MED. FRONTIER: no.

Calibration (main researcher, 2026-10-31): pain severity and frequency 3 to 4 (integrity work hits every assignment (AI2-47, AI2-48 strong)); ai leverage 4 to 5 (the voice examiner is the product; without the model nothing is left); whitespace 3 to 2 (early direct rivals (OralExam.AI, verballi, better-ed) and a free NYU recipe at $0.42 per student).

## 3. The problem
- Who: instructors of large or online courses, and high-school teachers, who see work that looks AI-written but cannot prove it.
- Cost: integrity reports need an individual meeting and form per student, "hundreds of hours" in one case (AI2-47); detectors misfire and accusations on a hunch are costly (AI2-54); with 95 of 120 students citing the same three chatbot-recommended sources there is no objective evidence to act on (AI2-50).
- Workarounds: in-class blue-book exams, "pretend-proctored" lockdown browsers (AI2-48), AI detectors such as Pangram, which one instructor calls "game changing" (AI2-49), and human oral defenses, which do not scale (AI2-52).
- Gap: a fair, non-accusatory way to ask every student "explain your own work" without a human examiner for each.

## 4. Evidence
- **AI2-47** (strong, 2026-10-30, r/Professors, 53 pts / 31 comments): "Submitting academic dishonesty reports at my university requires first meeting with each student individually and then filling out each form individually. This would be hundreds of hours of work and isn’t feasible with all my other obligations." https://www.reddit.com/r/Professors/comments/1xjpk5x/
- **AI2-48** (strong, 2026-10-30, r/Professors, 66 pts / 65 comments): "I think my colleagues have stopped trying to maintain any level of integrity in their courses." https://www.reddit.com/r/Professors/comments/1xjkmy3/
- **AI2-50** (medium, 2026-10-30, r/Professors): "So far, about 95 of 120 have used one of the same three sources. Running my topic through Chat, these three sources are the three that it quotes if I ask it for sources." https://www.reddit.com/r/Professors/comments/1xjt42j/
- **AI2-54** (medium, 2026-03-07, HN): "I've seen a couple of examples now where students find sudden spurts of motivation and show unexpected talent on an assignment, to be accused of AI use after handing it in." https://news.ycombinator.com/item?id=47283293
- **AI2-52** (weak, 2026-08-08, HN, on Denmark's rule that students defend written work orally): "The oral system scales poorly. One examiner can only hear so many students in a day." https://news.ycombinator.com/item?id=49224973
- **AI2-49** (medium, 2026-10-29, r/Professors), a counter-signal: an instructor says of the Pangram detector, "Shout out to Pangram which has honestly been game changing." Detection has fans, so the pitch must be fairness and proof, not detection. https://www.reddit.com/r/Professors/comments/1xim2aj/
- New evidence (not in SIGNALS.md), a published pilot (headline only): "NYU professor fights AI cheating with AI-powered oral exams that cost 42 cents per student" (title). https://the-decoder.com/nyu-professor-fights-ai-cheating-with-ai-powered-oral-exams-that-cost-42-cents-per-student/ The paper is https://arxiv.org/abs/2603.18221. Per the search summary: $15 for 36 students, 70% of students agreed it tested genuine understanding, and 83% found it more stressful than written exams.
- New evidence (not in SIGNALS.md), a builder: OralExam.AI (Tulane professor, 2026-08-11) is "not built to grade papers or run detection scans". https://technical.ly/entrepreneurship/tulane-professor-builds-oralexam-ai-for-student-comprehension/

## 5. The product
- What it does: an instructor creates an assignment and connects it to the course (link or LTI later). The student submits work, then gets a link for a 5 to 8 minute voice conversation with an AI examiner that has read the submission and asks about their own choices ("why did you pick this source", "what would change if X"). The instructor gets a one-page report: transcript, rubric scores, inconsistencies between the written work and the answers, and the examiner's confidence. The instructor decides; nothing is automated into a grade or an accusation.
- Core AI loop: submission + rubric -> question plan (3 to 5 questions, one at a time) -> live voice conversation with follow-ups -> transcript -> rubric score and "what the student could not explain" -> instructor review -> optional human follow-up.
- Interaction model: student uses a browser and microphone; typed or extended-time alternatives for speech differences, anxiety and second-language speakers; instructor dashboard per assignment.
- Form factor: web app (LTI 1.3 listing after the MVP).
- Day in the life: a 120-student online course has a 2,000-word paper. 118 students hold the conversation over a weekend. The instructor reads 22 flagged reports, asks 9 students for a human follow-up, and spends two hours instead of fifty.
- Design lines: ask one question at a time (the NYU pilot's agent stacked questions and students felt shouted at), no voice biometrics in the MVP, a visible practice mode, and reports phrased as evidence for a conversation.

## 6. Why the LLM is load-bearing
- Questions must be generated from each student's own paper and adapt to the answers; that is reading plus live spoken dialogue, the thing human oral examiners do and models can now do at cents.
- Without the model the choices are a human examiner (the scaling failure in AI2-52) or a fixed quiz that students can answer with a chatbot.

## 7. The insight
- Explaining your own work is the oldest authorship test. Realtime voice at about $0.05 a minute or less makes it affordable at class scale, and framing it as a pedagogical conversation avoids the detector problem of accusing people on a hunch (AI2-54).
- Honest limit: the pedagogy is not new, and the NYU authors published how to build it.

## 8. Why now, and why this does not exist yet
- Why now: GPT Live bills $0.05 a minute, Gemini 3.8 Live about $0.005 in and $0.018 out (`research/LANDSCAPE.md` section 6); the reported cost of an AI oral exam fell to dollars per class; instructors in 2026-10 describe the problem as unmanageable.
- Why not yet: it is starting. OralExam.AI launched in August 2026 with free pilots, verballi presents at teaching conferences, and universities run prototypes. The product is early and unpriced, not absent.

## 9. Inspiration and derivation
- Parents: the Danish oral defense rule (AI2-52), the NYU Stern voice-agent exam, Coursera's AI Viva pilot, Integrevise, VivaBuddy.
- Changed: target user (the single overloaded instructor, not the institution), core job (authorship evidence and a fair conversation, not grading), interaction model (a short asynchronous voice session after submission, not a scheduled exam), business model (per completed viva), channel (instructor communities, not procurement).

## 10. Competition check
Queries run:
1. WebSearch: "AI voice oral exam students defend their own submitted work authenticity university instructor realtime voice agent cost per student"
2. WebSearch (Product Hunt): "site:producthunt.com AI oral exam viva voice assessment students explain their assignment" (one unrelated study tool)
3. WebSearch (YC directory): "site:ycombinator.com/companies AI oral exams education assessment voice students academic integrity" (no YC company found)
4. WebSearch (LMS marketplaces): "Canvas OR Moodle OR Blackboard LTI plugin AI oral assessment viva voice interview student authorship verification 2026"
5. WebFetch of the OralExam.AI profile; WebSearch on verballi pricing (not found).

| Product | What it does | Price | How it differs |
|---|---|---|---|
| [OralExam.AI](https://technical.ly/entrepreneurship/tulane-professor-builds-oralexam-ai-for-student-comprehension/) (New Orleans, three founders, self-financed, 2026-08-11) | Student uploads work, AI conducts a spoken interview and rates "thesis understanding", "evidence knowledge" and "authorship"; the professor decides | Not stated; free pilots this fall | Closest direct rival; same concept, pre-traction |
| [verballi](https://stars.library.ucf.edu/teaching-and-learning-with-ai/15) (UCF conference listing) | Voice-first short oral assessments outside class, voice authentication of authorship, AI grading against the instructor's rubric (vendor description) | not found | Direct; adds voice authentication |
| [better-ed](https://linkedin.com/showcase/better-ed) (LinkedIn showcase) | Students explain their thinking by voice or text; advertised free for teachers | Free | Free competitor [UNVERIFIED beyond a search summary] |
| NYU Stern voice-agent exam ([paper](https://arxiv.org/abs/2603.18221), [The Decoder](https://the-decoder.com/nyu-professor-fights-ai-cheating-with-ai-powered-oral-exams-that-cost-42-cents-per-student/)) | Course-level pilot: personalized oral exam on the student's project, graded by a panel of three LLMs; $15 for 36 students on a $99/month ElevenLabs plan (search summary) | DIY | Shows the DIY route and sets a price anchor of $0.42 per student |
| Academic prototypes: [viva voce simulator](https://arxiv.org/pdf/2511.05530), [Integrevise](https://digitalcommons.lindenwood.edu/faculty-research-papers/814) (Lindenwood, 52 vivas in spring 2026), VivaBuddy (UTS), Coursera AI Viva ([IATED](https://library.iated.org/view/WANG2024AIP)) | Pair a written submission with an adaptive oral viva | n/a | Not products yet; validate demand |
| [Eklavvya](https://www.eklavvya.com/blog/conduct-viva-online/) (online viva and voice-assessment pages); an LTI 1.3 exam platform with recorded spoken or video answers and AI-assisted rubric grading ([DEV post](https://dev.to/tahiralmas/universities-are-reviving-oral-exams-to-beat-ai-cheating-heres-how-to-scale-them-online-1blm)) | Online viva and recorded oral answers; AI-assisted grading in the second | n/a | Existing exam platforms that could add a live AI examiner |
| AI detectors (Pangram, per AI2-49) and process trackers | Flag AI text after the fact | n/a | Adjacent; accusation risk (AI2-54) |

Classification: **WEAK DIRECT**. Three early direct entrants and several research prototypes, none funded or with visible traction; but the product can be rebuilt by a motivated instructor from a published recipe. No Canvas, Moodle or Blackboard tool for this was found in a 2026 search.

Platform risk: medium to high. LMS vendors could add a "defend your work" assignment type, and OpenAI, Google and Anthropic ship education products with voice modes [ASSUMPTION, not verified]. The DIY route is the nearest threat: ChatGPT voice plus a prompt reproduces a rough version for one student at a time. Per the rubric, platform risk caps Scale and defensibility at 2 and Whitespace at 3.

## 11. Business model
- Payer: the instructor (card, expensed) first; department or institution licenses later. Price: $1.50 per completed viva, or a semester pack of 100 for $129; free practice mode. Anchors: NYU pilot $0.42 per student, ElevenLabs $99/month plan, free better-ed.
- Model cost per viva [ESTIMATE], 7 minutes: Gemini 3.8 Live, 7 min x $0.005 = $0.035 in plus 3.5 min x $0.018 = $0.063 out; question plan on Sonnet 5.5, 6,000 in x $2/1M + 800 out x $10/1M = $0.012 + $0.008 = $0.02; grading, 9,000 in x $2/1M + 1,000 out x $10/1M = $0.018 + $0.010 = $0.028. Total about $0.15 per viva, so $15 per 100. On GPT Live: 7 x $0.05 = $0.35 + $0.048 = $0.40, so $40 per 100.
- Gross margin [ESTIMATE]: pack of 100 at $129: ($129 - $14.6 - $4.04 Stripe) / $129 = 86% on Gemini; ($129 - $39.8 - $4.04) / $129 = 66% on GPT Live. Choose the cheaper voice stack.

## 12. Market size
- Buyers [ESTIMATE]: assume 1.0M US college instructors [ASSUMPTION; NCES faculty count not checked], of whom 10% teach writing-heavy or project courses with serious AI concerns = 100K. One instructor buys 2 semester packs a year at $129 = $258.
- Revenue: 100K x $258 = $25.8M a year. At 5% penetration (5,000 instructors) = $1.29M ARR.
- Reading: a small instructor-paid market; real scale needs department or institution licenses and high-school districts, which hit procurement and student-privacy review.

## 13. Go-to-market
- First 100: (1) a free "AI viva starter kit" (prompt, rubric, consent text, accommodation policy) posted where r/Professors-style instructors discuss integrity, with the hosted version as the upgrade, about 40; (2) teaching-and-learning-with-AI conferences and teaching-center newsletters (the verballi listing shows a UCF conference series), about 25; (3) SEO on "how to prove a student wrote their paper", "AI detector false positive alternative", "oral exam at scale", about 25; (4) high-school teachers in countries with oral-defense traditions (Denmark, per AI2-52), about 10.
- Growth loop: instructors share the starter kit and colleagues try the hosted version; students who liked the practice mode mention it to other instructors. Department-level adoption follows a pilot report.

## 14. Moat and scale path
- Moat: rubric and question libraries by discipline, accommodation workflows, and LMS integration. All copyable; the real edge is trust and privacy handling.
- Scale path: LTI 1.3 listing, department licenses, an authorship evidence packet usable in integrity hearings, then K-12 districts.

## 15. Solo feasibility
- MVP (6 weeks): assignment creation, submission upload (text and PDF), question planning, browser voice session, transcript and rubric report, typed fallback, consent and retention settings. No LMS integration or biometrics.
- Running cost before revenue: about $50 to $150 a month (hosting, 300 pilot vivas x $0.15 to $0.40 = $45 to $120).
- Hardest risks: student-data privacy (FERPA in the US and GDPR abroad [UNVERIFIED here]), fairness for students with speech differences or anxiety (83% found the NYU exam more stressful), and keeping the voice agent from piling on questions.

## 16. Pre-mortem
1. The buyer is the institution, not the instructor; instructors like it and cannot get it approved, so adoption stalls.
2. Students experience it as stressful or unfair, a complaint spreads, and instructors drop it.
3. A free DIY recipe, an LMS feature or a lab's education mode makes a paid product unnecessary.

## 17. Cheapest validation test
- What: run the starter kit with 6 volunteer instructors (recruited from instructor communities) over one assignment each, using a hosted prototype or a rented ElevenLabs agent; collect instructor and student ratings.
- Cost: about $50 to $100. Duration: 4 weeks including one assignment cycle.
- Pass: at least 4 of 6 instructors say the report saved them time or gave evidence they could act on, student completion above 85%, fewer than 25% of students rate it unfair, and at least 3 instructors prepay a $129 pack. Fail: fewer than 2 would pay or fairness complaints above 40%.

## 18. Open questions
- Will instructors pay when a recipe and a free competitor exist, and is the institution the real buyer?
- Does an oral conversation measure understanding or confidence? (A search summary of an Australian academic's warning says oral exams used as an "AI lie detector" test confidence.)
- Can the product be accommodation-first (typed answers, extended time) without losing the authorship signal?
- Which student-data rules apply to K-12, and can a teacher legally use a vendor without district approval?
- Is it better to sell the authorship evidence to integrity offices (a hearing packet) than to individual instructors?

## Deep dive

Method (reads dated 2026-10-31): WebFetch of oralexam.ai (an EDUCAUSE page on the HECVAT vendor-security questionnaire returned HTTP 403), 3 web searches (AI oral-exam platforms, NCES faculty and enrollment counts, student-paid ed-tech pricing), a scan of 800 r/Professors posts since 2026-09-15 through the Arctic Shift archive, and Hacker News search. Model prices: `research/LANDSCAPE.md` section 6. The question this deep dive centers on is who pays.

### Competitor table
| Competitor | Link | What it does | Price (as published, with date read) | Funding or traction (sourced) | Gap this idea exploits |
|---|---|---|---|---|---|
| OralExam.AI | [site](https://oralexam.ai), [Technical.ly](https://technical.ly/entrepreneurship/tulane-professor-builds-oralexam-ai-for-student-comprehension/) | Student uploads work, AI interviews them, rates understanding and authorship; sold to "educators and institutions, in higher education and in high schools"; "We are currently integrated with Canvas." | "Pricing is not set yet." (site, 2026-10-31) | "Multiple pilots are actively running, including one at Tulane University"; "the first university courses go live this fall"; self-financed (first pass). Privacy: "FERPA-aligned infrastructure"; "Webcam recordings carry a ninety day retention window" but "that purge is not yet on an automatic schedule"; "We are scoping SOC 2 Type I attestation." (via WebFetch summary, wording may be condensed) | Unpriced, Canvas only, webcam recordings, no SOC 2. It is ahead on pilots and LMS, so win on privacy-first design (no webcam, audio not stored) and clear pricing |
| verballi | [UCF listing](https://stars.library.ucf.edu/teaching-and-learning-with-ai/15) | Voice-first short oral assessments, voice authentication, AI grading against the instructor's rubric (vendor description) | not found | conference listing only | Voice biometrics add privacy and fairness risk; not in my MVP |
| better-ed | [LinkedIn](https://linkedin.com/showcase/better-ed) | Students explain their thinking by voice or text; advertised free for teachers | Free [UNVERIFIED beyond a search summary] | not found | Free anchors price expectations; sell reports and accommodations |
| NYU Stern recipe | [arXiv 2603.18221](https://arxiv.org/abs/2603.18221), [The Decoder](https://the-decoder.com/nyu-professor-fights-ai-cheating-with-ai-powered-oral-exams-that-cost-42-cents-per-student/) | Professor-built voice exam, three-LLM panel grading | DIY: $15 for 36 students, $0.42 each, on a $99/month ElevenLabs plan (search summary) | 83% found it more stressful (first pass). HN reader: "So what's next? Students using AIs with text-to-speech to orally respond to the "oral" exam questions from an AI?" ([2026-01-02](https://news.ycombinator.com/item?id=46468354)) | Sell the hosted version, rubric, consent, accommodations; build the AI-voice-answer check in |
| KouShi (NUS AICET) | [page](https://aicet.comp.nus.edu.sg/koushi-aicets-ai-chinese-oral-exam-platform-featured/) | AI Chinese oral exam, trialed by teachers from about 30 schools (primary level) | not found | university project | Adjacent language oral exam, not authorship |
| Research prototypes: viva simulator, Integrevise, VivaBuddy, Coursera AI Viva, ExamAI (TU/e) | [arXiv 2511.05530](https://arxiv.org/pdf/2511.05530), [Lindenwood](https://digitalcommons.lindenwood.edu/faculty-research-papers/814), [TU/e](https://drive.tue.nl/projects/ai-assisted-examination-examai/) | Adaptive oral vivas paired with written work | n/a | Integrevise: 52 vivas in spring 2026 (first pass) | Not products yet |
| Eklavvya and LTI exam platforms with recorded answers | [Eklavvya](https://www.eklavvya.com/blog/conduct-viva-online/), [DEV post](https://dev.to/tahiralmas/universities-are-reviving-oral-exams-to-beat-ai-cheating-heres-how-to-scale-them-online-1blm) | Online viva and recorded spoken answers with AI-assisted grading | n/a | n/a | Could add a live AI examiner |
| Manual oral exams and DIY voice assistants | [r/Professors 2026-10-10](https://www.reddit.com/r/Professors/comments/1x2bmvl/) | "I've been using online oral exams to replace a writing assignment in my online classes for 2 semesters now and they work pretty well." | free (instructor time; ChatGPT or Gemini voice plus a prompt) | 60 points, 14 comments | Does not scale; no record, rubric or accommodations |
| Payer analog: Packback | [pricing](https://packback.co/pricing), [help](https://help.packback.co/hc/en-us/articles/228015268-What-does-the-cost-cover) | Student-paid discussion platform the instructor selects | $39 per student per course (Questions), $49 with Deep Dives; "per community, per semester"; scholarship codes; institutional pricing (search summary) | not sourced | Proof that students will be billed per course |
| Payer analog: Top Hat | [Iowa](https://teach.its.uiowa.edu/top-hat), [NIU](https://www.niu.edu/blackboard/faq/clickers.shtml), [UMKC](https://tdx.umsystem.edu/TDClient/66/MOOnline/KB/PrintArticle?ID=139) | Student-paid response system | $10 a semester billed to the U-Bill at Iowa; $26 at NIU; $20 at UMKC (search summary) | n/a | Price range for a per-student course fee |

Read across: three early direct tools, none with a published price (better-ed is advertised as free) and none visibly funded, so there is no payer model to copy from them. Evidence that departments buy small integrity items: r/Professors, 2026-10-19, "I spoke to the department head today and he has agreed to purchase basic calculators for the students to use on exams." ([thread](https://www.reddit.com/r/Professors/comments/1xab0y9/)). Evidence against institutional urgency: 2026-10-15, "TL;DR School wants to lower assessment standards for online courses to grow enrollment and increase revenue." ([thread](https://www.reddit.com/r/Professors/comments/1x70iz9/)).

### Market sizing (bottom-up)
Source: NCES, about 1.5 million faculty at degree-granting institutions in fall 2022 (842,400 full time, 665,200 part time) and 19.0 million students ([Condition of Education](https://nces.ed.gov/programs/coe/indicator/csc/postsecondary-faculty), [Fast Facts](https://nces.ed.gov/fastfacts/); search summaries). I assume 10% of faculty teach writing- or project-heavy courses with serious AI concerns = 150,000 [ASSUMPTION], and an average department of 20 faculty = 75,000 departments [ASSUMPTION].
| Payer model | Buyer unit | Price a year | Conservative | Optimistic |
|---|---|---|---|---|
| A. Instructor pays by card | 150,000 instructors | 2 packs of 100 vivas x $129 = $258 | 2% = 3,000 x $258 = $0.77M | 5% = 7,500 = $1.94M |
| B. Department or course licence | 75,000 departments | $2,000 per department (about 3,000 vivas) or $499 per course section | 0.5% = 375 x $2,000 = $0.75M | 2% = 1,500 = $3.0M |
| C. Students pay through a course code | 150,000 instructors | 100 students x $6 x 2 terms = $1,200 per course | 0.5% = 750 x $1,200 = $0.90M | 2% = 3,000 = $3.6M |
Revenue at 100 / 1,000 / 10,000 customers: A $25.8K / $258K / $2.58M; B $200K / $2.0M / $20M; C $120K / $1.2M / $12M. 10,000 customers is 6.7% of instructors in A and C and 13.3% of departments in B. Reading: instructor-paid caps near $2M; B and C carry the upside. C brings about 4.7x the revenue per course ($600 a term against a $129 pack) but has a fairness problem: students paying to prove their own work. B hits security and privacy review at any price.

### Unit economics
Per active instructor-month = 100 vivas of 7 minutes (one assignment, one $129 pack). Every line [ESTIMATE].
| Line | Arithmetic | $ per viva |
|---|---|---|
| Live voice, Gemini 3.8 Live | 7 min in x $0.005 + 3.5 min out x $0.018 = $0.035 + $0.063 | 0.098 |
| Paper re-sent as context | 3,500 tokens x 8 turns = 28,000 x $1.50/1M (the post-2026-12-31 Flash rate) [ASSUMPTION: billed as text input] | 0.042 |
| Question plan, Sonnet 5.5 | 6,000 x $2/1M + 800 x $10/1M = $0.012 + $0.008 | 0.020 |
| Grading, Sonnet 5.5 | 9,000 x $2/1M + 1,000 x $10/1M = $0.018 + $0.010 | 0.028 |
| **Per viva, Gemini** | | **0.188** |
| Per viva, GPT Live | 7 min x $0.05 = $0.35 + $0.048 | 0.398 |
Per pack of 100: model $18.80 (Gemini) or $39.80 (GPT Live), Stripe on $129 = 2.9% x $129 + $0.30 = $4.04, infrastructure $80 / 100 customers = $0.80, support $3.00 [ASSUMPTION]. Cost $26.64 and margin 79% on Gemini; $47.64 and 63% on GPT Live. Student-paid at $6: $0.19 + Stripe $0.47 = $0.66, margin 89% if billed per student (cheaper in bulk). Department: 2,000 vivas cost 2,000 x $0.188 = $376, 81% margin before support; at 8,000 vivas cost is $1,504 against $2,000, margin 25%, so the licence includes 3,000 vivas and $0.50 beyond.
**Heavy user:** an instructor with 2,400 vivas in a semester (24 packs, $3,096) costs $451 on Gemini or $955 on GPT Live: fine. The real exposure is practice and retakes: 20 full-length practice sessions per student cost about 20 x $0.098 = $2.00 in voice alone, more than the $1.29 a student pays. Caps: practice is 2 sessions of 3 minutes or less; a real viva stops at 10 minutes (worst case $0.23 on Gemini, $0.55 on GPT Live); one free retry only for technical failure; pricing is per completed viva.

### First 100 customers
Channel volume (Arctic Shift, to 2026-10-30, broad regex): r/Professors about 40 posts a day, about 48 a week on AI, integrity or oral exams; r/Teachers about 100 a day, about 42 a week; r/highereducation under 1 a day. Funnel [ESTIMATE]: per 1,000 views of the kit post, 40 download (4%), 6 reserve a pilot (15%), 3 finish a pilot (50%), 1 buys a pack (30%). 100 paying instructors would need about 100,000 views, so reach must come from teaching-center newsletters (each reaching hundreds to thousands of faculty) and chairs. Message: "Ask every student to explain their own work in five minutes, without accusing anyone. Free starter kit, hosted version if you want it." Offer: free kit; one free pilot assignment up to 30 students; then $129 per 100 vivas.
| Week | Action (payer track) | New paying | Cum. |
|---|---|---|---|
| 1 | Publish the kit and the three offer cards (below). Post once in r/Professors if its rules allow resources; reply to oral-exam threads; "Show HN" to the audience of the NYU thread (A) | 0 | 0 |
| 2 | Email 10 teaching-center directors one personal note each, offering the kit for their faculty newsletter (B) | 2 | 2 |
| 3 | Run 5 free pilots with reserved instructors; collect instructor and student ratings (A) | 3 | 5 |
| 4 | Send each pilot instructor a one-page report to forward to their chair, with a security sheet (B) | 3 | 8 |
| 5 | SEO pages: "how to prove a student wrote their paper", "AI detector false positive alternative", "oral exam at scale" (A) | 3 | 11 |
| 6 | Propose a talk at a teaching-and-learning-with-AI event (the UCF series lists verballi) (A, B) | 3 | 14 |
| 7 | Student-paid trial with 2 instructors whose institutions allow course fees ($6, course code) (C) | 3 | 17 |
| 8 | Choose the primary payer from the numbers | 3 | 20 |
Base case about 20 paying instructors plus 2 to 3 department quotes by week 8; 100 customers around month 6. Loop after 100: instructors forward the kit; pilot reports help chairs justify a licence; students who liked practice mode mention it to other instructors.

### One-week validation test (under $50)
**What:** a free starter kit page with three honest purchase options, on a free host. The kit is real: examiner prompt, rubric template, consent text, accommodation policy, and steps to run an oral check with any voice assistant. Below it: "Want it hosted? The hosted version is not live. Reserve a pilot slot." Cards: **A** Instructor pack, 100 vivas for $129 (reserve with a $19 refundable deposit). **B** Course or department licence, $499 per section or $2,000 per department-year: request a one-page quote and security sheet; no payment; "who would sign (chair, teaching center, IT)?" **C** Students pay $6 each through a course code: join the interest list; "does your institution allow course fees for tools?" The form asks role and institution type. Traffic: one resource post in r/Professors only if its rules allow, replies in oral-exam threads, one "Show HN", your LinkedIn, 5 personal emails to teaching-center directors. No student data is collected, no LMS access, no ads.
**Budget:** domain $12 (optional); Stripe fees on 3 refunded $19 deposits 3 x ($0.55 + $0.30) = $2.55; model credit $10 to test the kit prompts in voice mode; host and forms $0. About $25.
**Decision rules, fixed now.** Downloads: 100 or more by instructors. Reservations: 15 or more. A passes with 3 or more deposits. B passes with 2 or more quote requests that name a budget holder who replies within 7 days. C passes only if 5 or more instructors say they would add a $6 course fee and at least 1 confirms the institution allows it, and fewer than 3 object that students should not pay to prove their work. Overall pass: 100 downloads and (A or B passes). If A fails but B passes, sell to departments. If only C is liked, do not build it. **Fail:** under 40 downloads, under 5 reservations, or no deposits and no budget-holder replies.

### Build brief (paste into a coding session)
```text
PRODUCT: Viva Voce lets an instructor attach a short AI-led voice conversation to any written or project assignment. The student submits, then explains their own work in 5 to 8 minutes.
The instructor gets a one-page report: rubric scores with quotes, what the student could not explain, inconsistencies, confidence. The instructor decides; nothing is graded or reported automatically.
MVP FEATURES (each testable)
1 Instructor creates an assignment: prompt, rubric, question budget, 10-minute cap, typed fallback, retention days. Test: settings persist and are enforced.
2 Student link with consent screen and a 3-minute practice mode (2 sessions max).
3 Submission upload (PDF, DOCX, text) with text extraction. Test: 20 sample files extract.
4 Question plan: 3 to 5 questions, each tied to a quoted passage, easiest to hardest, with follow-up bank.
5 Browser voice session: one question at a time, waits for silence, at most 2 follow-ups, hard stop at 10 minutes. Test: transcripts show one question per turn in 95% of turns.
6 Typed or extended-time alternative with the same questions.
7 Report with quote verification: every quote appears in the transcript or the submission, else regenerate.
8 Instructor dashboard: flagged reports first, request-human-follow-up button, student can ask for a human.
9 Retention and deletion: audio not stored, transcript deleted at the chosen day, export for the instructor.
10 Stripe: $129 pack of 100 completed vivas; licence by invoice later.
NON-GOALS: LMS/LTI integration, voice biometrics, webcam or proctoring, AI-detector scores, automatic grades or accusations, K-12 accounts, native apps.
CORE AI LOOP: (a) question plan, Sonnet 5.5 (about 6,000 in, 800 out); (b) live examiner on Gemini 3.8 Live (default, $0.005/min in, $0.018/min out) or GPT Live (fallback, $0.05/min) with a system prompt: neutral tone, one question, wait, no judging aloud, end at 8 minutes; (c) grading, Sonnet 5.5 (about 9,000 in, 1,000 out) to rubric scores and "could not explain" with quotes; (d) optional Haiku 5.5 pass to check that every report claim has a quote. Humans: instructor reviews every flag and decides; the student can request a human conversation.
DATA MODEL: Instructor, Course, Assignment(rubric, settings), Student(pseudonymous id), Submission(file, text, hash), Session(token, consent, accommodation, mode, started, ended, cost), Turn(speaker, text, t), QuestionPlan, Report(scores, flags, confidence, model_versions), Review(decision), Order(Stripe), RetentionPolicy, AuditLog.
INTEGRATIONS: Gemini Live API https://ai.google.dev/gemini-api/docs/live; OpenAI Realtime https://platform.openai.com/docs/guides/realtime; LiveKit Agents https://docs.livekit.io/agents/; Stripe https://docs.stripe.com/payments/payment-links; later LTI 1.3 https://www.imsglobal.org/spec/lti/v1p3/ and Canvas API https://canvas.instructure.com/doc/api/.
STACK (about $100 to $200 a month): Next.js on Vercel $20, Supabase $25, LiveKit Cloud or direct WebRTC $0 to $50 [ASSUMPTION], Stripe, Sentry and Langfuse free, pilot voice minutes $45 to $120.
EVALS: 1 Authentic persona (answers grounded in the paper), 10 runs: no authorship flag, most rubric items scored 3 of 4 or better. 2 Ghost-written persona (knows only the abstract), 10 runs: report lists 3 or more specific passages not explained in 8 of 10; no accusatory words. 3 Anxious persona with long pauses: examiner waits 8 seconds or more, offers typed fallback after 2 long pauses, delivery speed not scored, 10 of 10. 4 Question stacking: at most one question mark per examiner turn in 95% of turns over 30 sessions. 5 Quote integrity: 100% of quotes in reports found verbatim.
BUILD PLAN (6 weeks): W1 auth, assignments, upload and extraction, Stripe pack. W2 question planner and eval harness. W3 browser voice session, consent, practice mode, typed fallback. W4 transcript, grading, report with quote check. W5 dashboard, review actions, retention and deletion, accessibility. W6 pilot with 6 instructors, tune examiner behaviour, privacy page.
RISKS TO TEST FIRST: 1 payer (the validation test); 2 student fairness and stress (83% found the NYU exam more stressful); 3 AI-voice answers read by students (HN, 2026-01-02); 4 student-data rules and institutional security review (HECVAT page not read) [UNVERIFIED]; 5 accessibility for speech differences and second-language speakers; 6 OralExam.AI's head start with Canvas.
```

**Notes for the main researcher:** OralExam.AI states "Pricing is not set yet" and is already Canvas-integrated, so Whitespace 2 and WTP 2 look right. Payer is unresolved: instructor-paid caps near $2M ARR, department licences carry the upside but face security review, and student-paid earns about 4.7x per course with a fairness problem. The test splits all three; no score change proposed.
