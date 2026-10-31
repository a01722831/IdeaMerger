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
  pain: 3
  evidence: 3
  ai_leverage: 4
  whitespace: 3
  novelty: 2
  why_now: 4
  solo_feasibility: 3
  distribution: 2
  wtp_economics: 2
  scale_defensibility: 2
total: 55.8
price_hypothesis: "$1.50 per completed viva (5-8 minutes); semester pack of 100 for $129"
model_cost_per_user_month: "$15 to $40 per 100 vivas"
gross_margin: "66% to 86%"
mvp_weeks: 6
deep_dive: false
red_team: false
---

# Viva Voce

## 1. One-liner
After a student submits work, a short realtime voice conversation with an AI examiner checks they understand it.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Acute during grading periods (a third of one class, hundreds of hours of paperwork) but seasonal, and the instructor is not the budget holder. |
| Evidence quality | 2 | 3 | Six cited signals (two strong, all instructor-side, four from 2026-10) plus a published pilot; no statement of willingness to pay. |
| AI leverage | 2 | 4 | The voice examiner and rubric scoring are the product; a human reviews the flags, so not a 5. |
| Whitespace | 2 | 3 | Early direct entrants (OralExam.AI, verballi, better-ed) and a free published recipe, but no funded leader or LMS-native tool found. |
| Novelty of insight | 1 | 2 | Oral defense as an authorship test is well known and now studied in papers; the twist is its $0.15 to $0.42 cost. |
| Why now | 1 | 4 | Realtime voice at $0.05/min or less and the AI-authorship crisis arrived together; one NYU pilot ran 36 exams for $15. |
| Solo feasibility | 2 | 3 | A web voice agent is 6 weeks; LMS integration, student privacy and accommodations add risk. |
| Distribution | 2 | 2 | Instructors are reachable in communities and by SEO, but schools gate student-data tools and the culture is wary of AI. |
| Willingness to pay and unit economics | 2 | 2 | An instructor can copy the NYU setup for about $0.42 a student; institutions have budgets but buy slowly. |
| Scale and defensibility | 2 | 2 | DIY recipe, LMS vendors and AI labs can add a "defend your work" mode; the moat is thin. |
| **Total** | | **55.8** | |

Confidence: MED. FRONTIER: no.

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
