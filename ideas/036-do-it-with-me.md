---
id: "036"
slug: do-it-with-me
name: Do It With Me
one_liner: "A voice guide walks an older parent through bank and portal tasks, refuses scam-like steps, and calls the child."
target_user: "Adult children who set up and support a parent aged 70 or more who struggles with phone, bank and health-portal tasks"
form_factor: "voice agent"
lens: "Underserved users"
frontier: false
competition: "WEAK DIRECT"
confidence: "LOW"
status: "developed"
signals: [HN-21, UND-15, UND-16, UND-12, UND-19, HN-20]
scores:
  pain: 3
  evidence: 3
  ai_leverage: 5
  whitespace: 2
  novelty: 3
  why_now: 4
  solo_feasibility: 2
  distribution: 2
  wtp_economics: 3
  scale_defensibility: 2
total: 56.8
price_hypothesis: "$14.99/month per parent device with 60 guided minutes included; first two routines free"
model_cost_per_user_month: "$1.4 on Gemini Live voice, up to $3.4 on GPT Live"
gross_margin: "72% to 86%"
mvp_weeks: 8
deep_dive: false
red_team: false
---

# Do It With Me

## 1. One-liner
A voice guide walks an older parent through bank and portal tasks, refuses scam-like steps, and calls the child.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Heavy emotionally, but help is needed monthly rather than daily, parents often resist, and a phone call or FaceTime works for many. |
| Evidence quality | 2 | 3 | Six cited signals (two strong, one possibly staged) plus three new posts; only HN-21 states willingness to pay, and it reacts to a generic arrow tool. |
| AI leverage | 2 | 5 | Voice plus screen understanding is the interaction; remove the model and a screen-share call (CareLink) is left. Not a 5 because a human is the fallback. Calibrated 4 to 5: the guide is the interaction (the HeyClicky test) |
| Whitespace | 2 | 2 | About five small direct entrants, free Gemini Live screen sharing, iOS 27 Siri on-screen awareness; only the family-configured, scam-refusing, child-escalating version is open. |
| Novelty of insight | 1 | 3 | A useful twist on the HeyClicky pattern: the child configures routines and the guide's main job is declining unsafe steps. |
| Why now | 1 | 4 | Realtime voice at $0.05/min or less and cheap screen understanding make a guided month cost about $1.4; impossible at this price in 2022. |
| Solo feasibility | 2 | 2 | Mobile OS limits on overlays, accessibility-permission policies, bank-flow safety and device testing push the MVP to 8 weeks with one hard platform risk. |
| Distribution | 2 | 2 | Seniors will not find or install it; the child must set up the parent's device; communities exist but there is no store channel or built-in loop. |
| Willingness to pay and unit economics | 2 | 3 | Adult children pay for family help (a rival lists $19/month), but Gemini Live and FaceTime are free; margin 72% to 86%. |
| Scale and defensibility | 2 | 2 | OS assistants own the primitives, which caps this at 2; the routine library and family trust are the moat. |
| **Total** | | **56.8** | |

Confidence: LOW (the platform feasibility and the willingness to pay are untested). FRONTIER: no.

Calibration (main researcher, 2026-10-31): ai leverage 4 to 5 (the guide is the interaction (the HeyClicky test)).

## 3. The problem
- Who: adult children whose parent (70+) is online but fragile: bank transfers, MyChart bill pay and booking, Medicare and Social Security sites, saving a contact in WhatsApp.
- Cost: repeated calls and visits, anxiety about scams, and money at risk. Elder-fraud stories are common in the evidence (HN-20, AI2-41).
- Workarounds: phone instructions, a hand-made key of app icons, FaceTime or a remote tool, or visiting. Banks offer little: one family was told the only guardrail was a limited ATM card.
- Gap: nobody provides a guide that knows the parent's own routines, follows rules the child set, and stops and phones the child when something looks wrong.

## 4. Evidence
- **HN-21** (medium, 2026-10-09, HN): would pay for a "make a bank transfer" button for aging parents. "I would pay good money for something like this on iPad. [...] That would be a godsent for those of us with aging parents." https://news.ycombinator.com/item?id=50019407
- **UND-16** (medium, 2026-10-23, MyChart 3-star review): "Booking a medical appointment or paying a bill requires the help of a son or a grandchild, assuming there is one, then the system has failed." https://apps.apple.com/us/app/id382952264
- **UND-15** (medium, 2026-10-29, MyChart 2-star review): "I think this tool is not the best for seniors, in fact it hinders those who don’t use computers from being able to access care." https://apps.apple.com/us/app/id382952264
- **UND-12** (strong, 2026-10-17, r/retirement, 190 pts / 178 comments): "I had researched everything, knew what I would take from my funds, knew I’d take COBRA, applied for SS, we got husband’s (66m) Medicare and Medigap set up and ready to go, but nothing happened quickly and without multiple phone calls." https://www.reddit.com/r/retirement/comments/1x8kblo/
- **UND-19** (medium, 2026-10-16; the signal file notes the body looks edited and the post may be staged, so I give it little weight): "The insurance money is just sitting in savings right now and the bank keeps pushing the annuity. I mostly want to know if I should be in a hurry or not." https://www.reddit.com/r/retirement/comments/1x7ht5c/
- **HN-20** (strong, 2025-12-22, HN, 137 pts / 67 comments): "I went down this road with my godmother, $300k still unrecovered, despite lots of information documented. [...] There needs to be an alert and approval mechanism for outbound wires that older people can be strongly encouraged to set up." https://news.ycombinator.com/item?id=46355145
- New evidence (not in SIGNALS.md): r/AgingParents, 2026-10-28, 14 pts / 24 comments: "I asked his bank if they have anything that can help put guardrails up, short of not giving him any cards, and all they have is an ATM card that he can use to get cash and MAYBE at limited stores." https://www.reddit.com/r/AgingParents/comments/1xhdz76/
- New evidence (not in SIGNALS.md): r/eldercare, 2026-10-09, 6 pts / 9 comments: "He can’t even understand the difference between the gmail app vs the chrome browser, I had to make a key with the app icons and descriptions on a PDF." https://www.reddit.com/r/eldercare/comments/1x1pcd4/
- New evidence (not in SIGNALS.md), a builder validating the same idea: r/AgingParents, 2026-10-24: "I’m building a free practice app where parents try a task on a safe fake screen, with a voice guiding them, before doing it for real." https://www.reddit.com/r/AgingParents/comments/1xe7ejx/

## 5. The product
- What it does: the child picks or records routines for the parent (pay the water bill, move money to cover it, book a MyChart visit, find a Medicare Summary Notice, save a WhatsApp contact). The parent taps a big "Help me" button or says "Guide". With consent for that session, the guide sees the screen, says the next step in one short sentence, highlights the right button where the device allows, and confirms before any money step against the child's rules (approved payees, limits). It never taps, types or moves money for the parent.
- Scam refusal: gift cards, crypto machines, installing a remote-access app, a new payee tied to a "government" or "tech support" request, or a caller urging speed makes the guide stop, say why in plain words, and ring the child with the screen shared.
- Core AI loop: routine goal plus live voice and screen -> the model identifies the screen and the next step -> speech and highlight -> the parent acts -> check -> next step; on a rule hit -> live escalation to the child; the child's fix can be saved as a new routine step.
- Interaction model: voice first on the parent's device; a child app for routines, rules and live calls; a weekly summary.
- Form factor: voice agent. Desktop browser extension and Android first; iPhone and iPad voice-only (see platform constraints below).
- Day in the life: Mom (76) says "pay the water bill". The guide recognizes the bank login, says "Tap the blue Pay Bills button", highlights it, and at the payee screen says "This is the water company Ana set up. The amount is $62. Say yes to continue." Another day a caller tells her to buy gift cards; she opens the guide, hears herself say "gift cards", and the guide says "This looks like a scam. I am calling Ana now."
- Platform constraints [ASSUMPTION, not verified in this research]: iOS does not let a third-party app draw over other apps, and Google Play restricts accessibility-service permissions, so pointing may be possible only in a desktop browser and on Android with approval.
- Liability line: it guides steps the family approved, gives no financial advice and never initiates payments; the child is the escalation.

## 6. Why the LLM is load-bearing
- Bank and portal screens change every few months and differ by institution; a model can read an unfamiliar screen, find the right button and phrase one short instruction, where scripted macros break.
- Spotting a scam needs language understanding of the parent's speech and the screen together.
- Without the model the product is a recorded macro or a human video call, which is what CareLink already is.

## 7. The insight
- Generic screen assistants help anyone with anything. Older adults need a trusted, family-configured, scam-aware guide that can say no and call a person. The child is the configurator and the safety rule-setter; the parent only has to press one button.
- Honest limit: this is a thesis. Parents may refuse the button, and many children will keep using FaceTime.

## 8. Why now, and why this does not exist yet
- Why now: GPT Live bills $0.05/min and Gemini 3.8 Live about $0.005 in and $0.018 out per audio minute, with screen input around $0.002/min (`research/LANDSCAPE.md` section 6). Gemini Live screen and camera sharing is free to Android users.
- Why not yet: parts exist. Memory Lane's Geni claims on-screen AI tech support for any app, and CareLink gives families a live screen-share call. In my searches none combined family-set rules, scam refusal and live escalation. The generic overlay is a red zone and the labs are moving in.

## 9. Inspiration and derivation
- Parents: HeyClicky (YC S26: hotkey, screen-aware voice, pointing; Free, $20 Pro in `research/LANDSCAPE.md`), CareLink (parent taps "Ask for help", the child sees the screen).
- Changed: target user (older adult plus adult child as configurator), core job (finish an approved task safely, not general help), business model (family subscription, not prosumer), channel (adult-child communities, not user-led app discovery). Per the landscape, the defensible version attaches the pattern to a narrow job; here that is approved banking and portal routines.

## 10. Competition check
Queries run:
1. WebSearch: "AI voice guide walks older adults through phone apps step by step bank transfer scam warning family configure screen sharing"
2. WebSearch (Product Hunt): "site:producthunt.com seniors AI assistant phone help tech support elderly parents"
3. WebSearch (YC directory): "site:ycombinator.com/companies seniors elderly AI voice assistant technology help older adults" (no company pages returned; only the F26 request for startups)
4. App Store, `scripts/app_reviews.py --find`: "scam protection seniors" ("tech help for seniors" and "senior help phone scam guide" failed); listings read through the iTunes lookup API
5. WebSearch: "Genie app seniors press side button sees what they see guides step-by-step phone helpmee.ai senior computer help voice screen sharing"
6. WebSearch: "Gemini Live share screen camera help navigate apps step by step Android; iOS 27 Siri on-screen awareness; FaceTime screen sharing remote control family tech support"
7. WebSearch: "iOS 27 Siri release on-screen awareness personal context Gemini-powered Siri app features September 2026"; WebFetch of the Memory Lane listing; Reddit archive r/AgingParents, r/eldercare.

| Product | What it does | Price | How it differs |
|---|---|---|---|
| Memory Lane "Geni" ([aggregator listing](https://aigregator.com/tools/memory-lane/llms.txt)) | "Instant on-screen AI tech support for any smartphone app", reminders, scam detection, WhatsApp updates to family (vendor claims) | Free 15 daily messages; $19/month premium | Closest direct rival; family rules and escalation not described |
| [CareLink](https://apps.apple.com/us/app/id6801002430) (ITERAON, US release 2026-09-20, 0 ratings) | Parent taps "Ask for help", the child's phone rings, sees the screen live and can draw; the child cannot tap or type; consent each time | Free listing | Human-in-the-loop, no AI; the escalation half of this idea |
| [Siggi - Smartphone Guide](https://apps.apple.com/us/app/id6747631567) (2025-06-24, 0 ratings), [AI Elder Assist](https://apps.apple.com/us/app/ai-elder-assist/id6753666581) (0 ratings) | Voice commands and guides for phone settings; voice companion with reminders | $8.49; free | Generic and unproven |
| helpmee.ai ([mirror](https://hunted.space/product/helpmee-ai), snippet) | "guides seniors step-by-step through any computer problem" with voice and screen sharing | n/a | Page had no data [UNVERIFIED] |
| Nini, Kolvia, ElderMate, Elsy, EDNA ([Product Hunt mirrors](https://hunted.space/product/nini), snippets) | Phone-number assistants, check-in calls, companions | n/a | Not task guidance |
| Scam side: Phonely CallGuard (snippet), [Scam Scanner](https://apps.apple.com/us/app/scam-scanner-ai-scam-detector/id6758177873), EverSafe and Carefull, bank "trusted contact" designations | Phrase alerts to a trusted person, message and letter checks, money monitoring | n/a | Detection after the fact, none inside a guided task |
| Gemini Live ([Tom's Guide](https://tomsguide.com/ai/gemini-live-video-and-screen-sharing-is-now-free-for-android-heres-how-to-use-it), [9to5Google 2025-04-01](https://9to5google.com/2025/04/01/gemini-live-camera-any-android/)) | Free screen and camera sharing on Android; per the search summary of its coverage you can show Gemini a webpage or a tangled mess of app settings and ask for help; stops when the screen locks | Free | Generic, user-started, no pointing or rules |
| iOS 27 Siri ([Digital Trends](https://www.digitaltrends.com/phones/siri-ai-ios-27-launch/), [iPhone Life](https://iphonelife.com/content/siri-ai-announced)) | Gemini-based Siri with personal context and on-screen awareness; coverage of mixed reliability [UNVERIFIED primary] | Bundled | Generic |
| FaceTime screen sharing with drawing and remote control (iOS 18) | Child draws or controls the parent's screen on a call | Free | [UNVERIFIED]: an Apple page I fetched did not confirm it |

Classification: **WEAK DIRECT**. About five small direct entrants with no visible traction, and the generic version is free from the OS makers. Kill criterion 2 (the OS handles it) and criterion 4 (access one platform can revoke) are live risks. A YC request for startups for F26 ("AI for the Aging Population") asks for voice interfaces and caregiver coordination, but no funded task-guidance company turned up.

Platform risk: high. Google, Apple and Microsoft each ship screen-aware voice help and own family-account primitives (Family Link, Family Sharing, Assistive Access). A "helper mode" for a family member is plausible within 12 months. Per the rubric this caps Scale and defensibility at 2 and Whitespace at 3 (scored 2). The pool already killed S150 Scam Call Screen for platform features, so scam handling here stays inside guided tasks.

## 11. Business model
- Payer: the adult child. Price: $14.99/month per parent device, 60 guided minutes included, first two routines free; annual $129. Anchors: Memory Lane $19/month, Siggi $8.49 once, CareLink free, HeyClicky $20 Pro.
- Model cost per active parent per month [ESTIMATE]: 6 sessions x 10 minutes = 60 minutes. Voice on Gemini 3.8 Live: 60 min user audio x $0.005 = $0.30 plus 30 min AI speech x $0.018 = $0.54, so $0.84. Screen input 60 x $0.002 = $0.12. Step checks on Sonnet 5.5: 48 steps x (1,500 in x $2/1M + 300 out x $10/1M = $0.006) = $0.29. Live-session text tokens 6 x (20,000 in x $0.75/1M + 3,000 out x $4.50/1M) = $0.17. Total $1.42.
- Sensitivities: if Google's intro prices double, $2.84; on GPT Live, 60 x $0.05 = $3.00 plus $0.12 plus $0.29 = $3.41.
- Gross margin [ESTIMATE]: ($14.99 - $1.42 - $0.73 Stripe fee) / $14.99 = 86%; 76% at doubled prices; 72% on GPT Live. Meter guided minutes, not conversations, as HeyClicky does.

## 12. Market size
- Buyers [ESTIMATE]: 63M US family caregivers (AARP and NAC 2025). Assume 20% help a parent with phone or computer tasks and have a parent who would use a guide [ASSUMPTION] = 12.6M. Assume 5% pay when Gemini Live and FaceTime are free [ASSUMPTION; the weakest number] = 630K.
- Revenue: 630K x $180 = $113M a year. Realistic penetration of 3% of that = 19K subscribers = $3.4M ARR.
- Reading: a modest niche with a fragile willingness-to-pay assumption.

## 13. Go-to-market
- First 100 customers: (1) answer parent-tech threads in r/AgingParents and r/eldercare ("Technology illiterate parent", "Need a security setup for my parent who clicks on everything") with a free "set up Mom's phone" checklist and a routine trial, about 50; (2) Show HN, where the HN-21 audience of adult children of aging parents lives, about 20; (3) SEO on "help my mom with online banking" and "senior safe bank transfer", about 30.
- Growth loop: siblings and holiday gifting ("give Mom a Guide"); the parent's peers are a weak secondary loop. The child is buyer and installer, so setup friction is the real funnel.

## 14. Moat and scale path
- Moat: a library of verified routines per bank and portal (a routine tested for one bank's web flow serves every customer of that bank), a scam-pattern rulebook, and the family's approved-payee history.
- Scale path: senior-living and bank channel partnerships (later, not a launch need), caregiver agencies, and routines for Medicare and Social Security tasks that connect to 037 Retirement Desk.

## 15. Solo feasibility
- MVP (8 weeks): a Chrome and Edge extension with voice, highlight, rules and live escalation over WebRTC, covering five sites (two large banks, MyChart, Medicare.gov, Social Security); an Android voice-and-screen-share alpha; child-side routine recording and rules; no automatic clicks.
- Running cost before revenue: about $100 to $150 a month (20 pilot users x $1.42 = $28, hosting, developer-account fees [UNVERIFIED]).
- Hardest risks: mobile OS permission limits, safe handling of bank screens (consent, screen privacy, bank terms), and screen-grounding reliability.

## 16. Pre-mortem
1. Platform: Gemini Live, Siri or FaceTime is good enough and free, and mobile OS rules block overlays and accessibility use.
2. A safety incident: the guide misleads a payment or misses a scam; loss, liability and press follow.
3. Adoption: parents do not press the button, so the child's setup effort goes unused and churn is high.

## 17. Cheapest validation test
- What: a Wizard-of-Oz test with 10 adult children and their parents on Android phones or Chromebooks. The child lists 3 tasks; parents attempt them with Gemini Live screen sharing alone for a week; then offer the real version (approved-payee checks plus a call to the child) at $15/month.
- Cost: about $0 to $100. Duration: 2 weeks.
- Pass: at least 60% of attempted tasks finished without calling the child, at least 5 of 10 children say they would pay $15/month, and at least 3 parents use "ask for help" unprompted twice. Fail: under 30% completion or under 2 would pay.

## 18. Open questions
- Can pointing be done legitimately on Android under store policy, and what is possible on iOS? [UNVERIFIED]
- Who is liable when a scam gets through, and does the guide's disclaimer hold when the screen is a bank's?
- Is desktop-first (web banking, portals) acceptable when most parents use phones?
- Do bank terms of service forbid reading a customer's screen in this way?
- Should this fold into 007 Parent Mail Desk as the parent-side "Help me" button, instead of standing alone?
