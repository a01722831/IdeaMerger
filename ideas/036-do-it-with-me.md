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
  wtp_economics: 2
  scale_defensibility: 1
total: 52.6
price_hypothesis: "$14.99/month per parent device with 60 guided minutes included; first two routines free"
model_cost_per_user_month: "$1.4 on Gemini Live voice, up to $3.4 on GPT Live"
gross_margin: "72% to 86%"
mvp_weeks: 8
deep_dive: true
red_team: true
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
| Willingness to pay and unit economics | 2 | 2 | Adult children pay for family help (a rival lists $19/month), but Gemini Live and FaceTime are free; margin 72% to 86%. Red team: 3 to 2, red team: price signals are a $19 rival with a free tier and $20 to $40 scam plans; the guided half competes with free Gemini Live |
| Scale and defensibility | 2 | 1 | OS assistants own the primitives, which caps this at 2; the routine library and family trust are the moat. Red team: 2 to 1, red team: the routine library is upkeep, not a moat; OS makers ship the primitives |
| **Total** | | **52.6** | |

Confidence: LOW (the platform feasibility and the willingness to pay are untested). FRONTIER: no.

Red-team adjustment (main researcher, 2026-11-01): willingness to pay and unit economics 3 to 2 (red team: price signals are a $19 rival with a free tier and $20 to $40 scam plans; the guided half competes with free Gemini Live); scale and defensibility 2 to 1 (red team: the routine library is upkeep, not a moat; OS makers ship the primitives).

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

## Deep dive

Added 2026-11-01. New facts were read 2026-11-01; "idea file" means sections 10 to 12 above (read 2026-10-31). Search-summary means I saw the fact only in a search result summary, not on the page. Platform risk comes first, because it decides whether the rest matters.

### Competitor table
Platform test (what the free assistants already do for an older adult):
- Gemini Live on Android: screen and camera sharing, free to Android users since April 2025 ([9to5Google, 2025-04-01](https://9to5google.com/2025/04/01/gemini-live-camera-any-android/), [Tom's Guide](https://tomsguide.com/ai/gemini-live-video-and-screen-sharing-is-now-free-for-android-heres-how-to-use-it), [Android Central](https://androidcentral.com/apps-software/android-os/gemini-live-real-time-screen-sharing-now-available-to-all-android-users)). Coverage describes step-by-step guidance, including "highlighting what to tap in settings" (search-summary of a 2025 article; not checked against current builds). Not seniors-specific.
- Copilot Vision with Highlights on Windows 10 and 11 in the US since 2025-06-12: "show me how" points out where to click in the shared window and never clicks for you ([Microsoft](https://blogs.windows.com/windowsexperience/2025/06/12/copilot-vision-on-windows-with-highlights-now-available-in-us/), [PCWorld](https://www.pcworld.com/article/2657888/copilot-vision-for-windows-can-walk-you-through-tech-issues-step-by-step.html), search-summary). Pointing on desktop is therefore not a differentiator.
- iOS 27 Siri (September 2026): a WSJ review is headlined "Siri finally grows up: Apple's new assistant can see your screen, search your photos, and get real work done" ([MacDailyNews, 2026-09-16](https://macdailynews.com/2026/09/16/wsj-siri-finally-grows-up-apples-new-assistant-can-see-your-screen-search-your-photos-and-get-real-work-done/), title). MacStories says Siri reads metadata from compatible apps rather than screenshots, so results depend on developer adoption ([review](https://www.macstories.net/stories/ios-and-ipados-27-review/6/), search-summary). Websites and non-adopting bank apps may be weak [UNVERIFIED].
- Android 16 in-call protections ([Google, 2025-05-13](https://blog.google/security/whats-new-in-android-security-privacy-2025/)): first-time sideloading and granting accessibility permissions are blocked during a call (Android 16); opening a participating banking app while screen sharing with an unknown contact triggers a warning (pilot UK banks Monzo, NatWest, Revolut; later US banks including Chase and Cash App per a [BleepingComputer](https://www.bleepingcomputer.com/news/security/google-expands-android-scam-protection-feature-to-chase-cash-app-in-us/) headline). Two consequences: the child cannot walk a parent through enabling an accessibility service by phone, and escalation must reach a saved contact, not an unknown one.
- Verdict: generic screen help and pointing are free on desktop and Android. I found no source showing family-set approved payees and limits, a refusal that stops a scam step, or automatic escalation to a named family member with the screen shared. That is an absence in what I read, not a tested fact; the validation test below tests it.

| Competitor | Link | What it does | Price (as published, with date read) | Funding or traction (sourced) | Gap this idea exploits |
|---|---|---|---|---|---|
| Gemini Live and Magic Pointer (Google) | links above; [Google Sept 2026 updates](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-september-2026/) (per `capabilities.md`) | Live screen and camera help; Magic Pointer "point and ask Gemini about anything on your screen" on Googlebook | Free on Android; Googlebook pre-order [UNVERIFIED] | Platform scale | User-started and generic; no family rules, no stop, no named escalation |
| Copilot Vision with Highlights (Microsoft) | links above | Shows where to click in a shared Windows window | Not verified for 2026 | Platform scale | Windows only; generic |
| iOS 27 Siri (Apple) | links above | On-screen awareness, personal context | Bundled with iOS 27 [UNVERIFIED] | Platform scale | Depends on app metadata; no family layer |
| Android 16 in-call scam protections (Google) | [Google post](https://blog.google/security/whats-new-in-android-security-privacy-2025/) | Blocks risky actions during a call; bank warnings | Free | Bank coverage partial (UK pilot, then some US banks) | Covers calls from unknown contacts only; not in-task guidance |
| Memory Lane "Geni" | [listing](https://aigregator.com/tools/memory-lane/llms.txt) | On-screen AI tech support, reminders, scam detection, WhatsApp updates to family (vendor claims) | Free 15 daily messages; $19/month premium (idea file) | Not published | Family rules and escalation not described |
| CareLink | [App Store](https://apps.apple.com/us/app/id6801002430) | Parent taps "Ask for help"; child sees the screen and can draw | Free listing (idea file) | US release 2026-09-20, 0 ratings | Human only, no AI guide; the escalation half |
| Siggi, AI Elder Assist | [Siggi](https://apps.apple.com/us/app/id6747631567), [AI Elder Assist](https://apps.apple.com/us/app/ai-elder-assist/id6753666581) | Voice guides for phone settings; reminders | $8.49; free (idea file) | 0 ratings each | Generic, no bank tasks |
| helpmee.ai, Nini, Kolvia, ElderMate, Elsy, EDNA | [helpmee mirror](https://hunted.space/product/helpmee-ai), [Nini mirror](https://hunted.space/product/nini) | Senior computer help, check-in calls, companions (snippets) | Not published | None found | Not task guidance |
| EverSafe NEW | [pricing](https://www.eversafe.com/pricing/) | Elder financial monitoring with caregiver read-only access | Core $7.49, Plus $16.99, Gold $26.99 a month; 15% off annual (search-summary, 2026-11-01) | Pricing page says it acquired CATCH.ai (search-summary) | After-the-fact alerts; no guided task. Shows what families pay for protection |
| Aura Family NEW | [Cybernews](https://cybernews.com/identity-theft-protection/aura-review/aura-pricing/) | Identity and fraud protection for up to 5 adults | $29 a month billed annually, $39 monthly (search-summary) | Not verified | General identity theft, not parent task help |
| Scam Scanner, Phonely CallGuard, Carefull, bank trusted-contact tools | [Scam Scanner](https://apps.apple.com/us/app/scam-scanner-ai-scam-detector/id6758177873) | Message checks, phrase alerts, money monitoring | Carefull price not found | Not verified | Detection after the fact |
| FaceTime screen sharing with drawing | none read | Child draws on the parent's screen on a call | Free [UNVERIFIED] | Platform | Human only |

### Market sizing (bottom-up)
- Count: 63M US family caregivers (AARP and NAC 2025, figure from section 12; I did not re-open the report). 20% help a parent with phone or computer tasks and have a parent who would use a guide [ASSUMPTION] = 12.6M.
- Adoption: conservative 0.5% (assumes the free assistants satisfy half of would-be buyers) = 63,000; optimistic 5% (section 12) = 630,000. Price $14.99 x 12 = $179.88 a year.
- Serviceable market: conservative 63,000 x $179.88 = $11.3M; optimistic 630,000 x $179.88 = $113.3M. Obtainable at 3% of that: 1,890 subscribers = $0.34M, to 18,900 = $3.40M ARR.
- Revenue at 100 / 1,000 / 10,000 subscribers: $17,988 / $179,880 / $1.80M (annual plan $129: $12,900 / $129,000 / $1.29M). 10,000 is 1.6% of the optimistic pool.
- Reading: the market is real but the adoption rate is the weakest number; the validation test measures it.

### Unit economics
Per active parent device per month (60 guided minutes). Prices from `research/LANDSCAPE.md` section 6. All [ESTIMATE].
- Gemini 3.8 Live: 60 min parent audio x $0.005 = $0.300; 30 min AI speech x $0.018 = $0.540; screen input 60 x $0.002 = $0.120; 48 step checks on Sonnet 5.5, each 1,500 x $2/1M + 300 x $10/1M = $0.006, so $0.288; 6 live-session text loads on Gemini 3.8 Flash, each 20,000 x $0.75/1M + 3,000 x $3.75/1M = $0.026, so $0.158. Model total $1.41 (the file used $4.50 for output, a $0.014 difference).
- Other variable: escalation video, 1 call x 5 min x 2 people x $0.004 a person-minute = $0.04 [ASSUMPTION]; weekly summary emails 4 x $0.001 = $0.004; payment fee $14.99 x 2.9% + $0.30 = $0.735; infrastructure $150 a month / 100 customers = $1.50, or $0.15 at 1,000.
- Gross margin: at 100 customers cost $3.68, margin 75%; at 1,000 cost $2.33, margin 84%. If Google prices double after 2026-12-31: $3.74 and 75% at 1,000. On GPT Live (60 x $0.05 = $3.00 + $0.12 + $0.288 = $3.41 model): $4.34 and 71% at 1,000. Budget on the doubled and GPT cases.
- Heavy user, 300 minutes (5x): voice $1.50 + speech $2.70 + screen $0.60 + 240 step checks $1.44 + 30 text loads $0.79 = $7.03; with other costs $7.96, margin 47%. Pricing cap: 60 minutes included, hard cap 150 minutes (model $3.51, margin 70%), top-up of 60 minutes at $4.99 [ASSUMPTION] (cost $1.41 plus fee $0.45, margin 63%).
- No human QA per customer; the routine library is founder time.

### First 100 customers
Funnel [ESTIMATE]: visit to child signup 6%; signup to parent device set up 45% (80% with a free 30-minute setup call, offered to the first 40 families, because setup is the real funnel); set up to first guided task within 7 days 70%; first task to paid after the two free routines 35%. Visit to paid = 0.06 x 0.45 x 0.7 x 0.35 = 0.66%.
| Week | Channel and action | Message and offer | Visitors | Paid (cumulative) |
|---|---|---|---|---|
| 1 | Show HN (the HN-21 audience) and one post in r/AgingParents | "Mom presses one button; you set the rules; it stops scams and calls you." Two routines free, setup call for 40 families | 300 | 2 |
| 2 | Answer open parent-tech threads in r/AgingParents and r/eldercare (e.g. "Technology illiterate parent") | Free "set up Mom's phone safely" checklist, then the trial | 400 | 5 |
| 3 | Search pages: "help my mom with online banking", "senior safe bank transfer", "stop my parent falling for gift card scams" | Scam-rules checklist for email capture | 500 | 8 |
| 4 | AgingCare.com forums and AARP Online Community answers; labeled prototype demo video | Same | 600 | 12 |
| 5 | Individual emails to geriatric care managers and senior move managers | Three free families each, referral link | 800 | 17 |
| 6 | In-product sibling invite on the family dashboard | "Add your sister; she sees the weekly summary" | 1,000 | 24 |
| 7 | Second Show HN or blog post on the first real "scam stopped" cases, with consent | Same | 1,200 | 32 |
| 8 | Review funnel; fix setup friction first | Same | 1,500 | 42 |
Base case: 6,300 visitors, 42 paying by week 8, 100 around week 13 if weekly visitors keep rising 10% to 15%. Growth loop after 100: siblings (the dashboard invite), gifting ("give Mom a Guide"), and routines recorded for one bank that serve every family at that bank after review.

### One-week validation test (under $50)
Platform baseline first (days 1 to 2, about 6 hours):
- Build a three-page fake bank site (login, pay bills, add payee) marked "FAKE BANK, test only". Write 10 scripted scenarios: 6 routine tasks and 4 scams (caller demands gift cards; caller asks to install a remote-access app; urgent "government" new payee; "grandchild in jail" wire).
- Run each scenario twice (20 runs per assistant) on Gemini Live (Android, screen share), Copilot Vision with Highlights (Windows) and iOS 27 Siri (only if I own a compatible iPhone; otherwise mark "not tested"). Log three yes/no items per run: correct next step; flagged or stopped the scam; offered a call to a named family member with the screen shared. A scam scenario counts as stopped only if both of its runs stop.
- Platform pass (wedge open): the best assistant stops at most 1 of the 4 scam scenarios and offers a family handoff in 0 of its 20 runs. Platform fail: any assistant stops 3 or more of 4 and offers a handoff in at least 5 of 20 runs; stop, and fold into 007 or drop. In between: go on, and narrow the pitch to what is missing.
Demand (days 3 to 7):
- One static page, "Guardrails for Mom's AI helper, pre-launch, not live", with a 60-second mock-up video labeled as a prototype, a free waitlist, and a refundable $15 reservation (Stripe Payment Link, refund promised on the page).
- One question-led post (not a pitch) in r/AgingParents and r/eldercare if their rules allow: how do you handle a scam call mid-task? Offer 20-minute calls; book 8.
- Budget: domain $12 [ASSUMPTION]; assistants on free tiers $0; Stripe fees on 3 refunded reservations 3 x $0.735 = $2.21 [ASSUMPTION: fees not returned]; page, form and analytics on free tiers $0. Total about $14, cap $50.
- Valid if at least 150 unique visitors. Pass = platform not failed, and at least 15 waitlist entries (10%) and at least 2 paid reservations and at least 4 of 8 interviewed adult children say they would pay $15 a month and name a scam or help-call incident in the last 90 days. Fail = platform fail, or fewer than 8 waitlist entries, or 0 reservations at 150+ visitors.

### Build brief (paste into a coding session)
- Product summary: A family-configured voice guide for a parent aged 70 or more. The child records routines and sets rules (approved payees, limits). The parent presses "Help me"; the guide gives one short step at a time with an on-page highlight, stops and explains when a step looks like a scam, and phones the child with the screen shared. It never clicks, types or moves money.
- MVP features (each testable):
  1. Chrome and Edge extension with a large "Help me" button, push-to-talk, a visible sharing indicator and per-session consent (no audio or frames leave the browser before the press; check the network log).
  2. Screen classification into a routine step or "unknown" (at least 90% of steps over 5 sites x 3 routines).
  3. One spoken instruction of at most 15 words plus a DOM highlight of the target (correct on at least 90% of steps).
  4. Child web app: record a routine as ordered labeled steps; set payees, per-payment limit and blocked actions (a rule edit applies to the next session).
  5. Money-step confirmation: read payee and amount from the page, require a spoken "yes", and stop and escalate on any mismatch with the rules (20 of 20 mismatches stop; done in code, not by the model).
  6. Scam stop on speech and page text (gift cards, crypto ATM, remote-access app, new payee under urgency): stop, explain in plain words, call the child.
  7. Live escalation by WebRTC to the child's saved contact; the child can draw but not control.
  8. Weekly summary email: sessions, tasks, stops, minutes.
  9. Metering and Stripe billing: 60 minutes included, hard cap 150, $14.99 a month, $129 a year, $4.99 top-up.
  10. Privacy: no screenshots stored; mask long digit strings before frames reach the model; 24-hour debug capture only with the child's opt-in.
- Non-goals (v1): automatic clicking, typing or payment; iPhone or iPad overlays; Android build before the platform test and a bank-terms check; call screening; general chat or companion; financial or medical advice; storing bank credentials; bank or senior-living deals.
- Core AI loop: parent speech (streamed) + screen frame on change (at most 1 per second) + routine step + child rules -> Gemini 3.8 Live (mid tier, $0.005/$0.018 a minute) hears the parent and sees the screen -> Sonnet 5.5 ($2/$10) verifies the step and the money fields at decision points (about 48 a month) while plain code compares payee and amount to the rules; Haiku 5.5 ($0.10/$0.50) may filter frame changes -> one short instruction and highlight, or stop and escalate -> checkpoints: the child sets the rules and receives escalations; the founder reviews every routine before it is shared across families.
- Data model: Family, Child, ParentDevice, Routine, RoutineStep, Rule (payee, limit, blocked action), Session, Event (step, stop, escalation), Summary, Subscription, UsageMeter.
- Integrations (docs): [Chrome extensions](https://developer.chrome.com/docs/extensions), [Gemini Live API](https://ai.google.dev/gemini-api/docs/live), [OpenAI Realtime](https://platform.openai.com/docs/guides/realtime) as the alternate voice, [LiveKit](https://docs.livekit.io/) for WebRTC, [Stripe Billing](https://docs.stripe.com/billing), [Supabase](https://supabase.com/docs); later Android [AccessibilityService](https://developer.android.com/guide/topics/ui/accessibility/service) with Google Play's accessibility policy (page not verified).
- Stack (about $100 to $150 a month): TypeScript Manifest V3 extension, Next.js child dashboard on Vercel, Supabase auth and Postgres, LiveKit Cloud, Stripe, Resend, Sentry; 20 pilot users x $1.41 = $28 of model spend.
- Evals: (1) 5 sites x 3 routines with a scripted confused-parent persona: at least 85% finished without escalation. (2) 20 scripted scam utterances: at least 18 stopped, each with a plain-words reason. (3) 20 benign sessions containing urgency words ("the bill is due today"): at most 1 stopped. (4) Payee or amount outside the rules: 20 of 20 stop. (5) First spoken step within 2.5 s of a screen change (median) and escalation connected within 10 s.
- Build plan (8 weeks): W1 extension, consent, voice session; W2 screen classification and highlight on 2 sites; W3 child app and rules; W4 money confirmation, scam stop, eval harness; W5 WebRTC escalation; W6 billing, metering, summaries; W7 pilot with 10 families (hand-operated fallback for failures) and 3 more sites; W8 privacy hardening, bank-terms review, waitlist launch.
- Key risks to test first: (1) the platform baseline; (2) bank terms and screen privacy; (3) whether parents press the button; (4) setup friction (Android 16 blocks accessibility grants mid-call, so setup is in person or by a QR link, not by phone); (5) a scam getting through.

Notes for the main researcher: Whitespace 2 holds. Pointing is free on Windows and Android, so the wedge is the trio of family rules, a stop, and a named escalation, which I could not find anywhere (not tested yet). Section 12's 5% adoption looks high given free alternatives; my conservative case uses 0.5%. The Android 16 in-call protections cut both ways: they cover part of the scam problem for participating banks and block mid-call setup. Whether to fold this into 007 Parent Mail Desk stays open; the family-configuration layer is what both would share.

## Red team
Skeptical-investor review on 2026-11-01 (full text: `research/RED_TEAM_B.md`). Verdict: **pass**.

**Top attacks (summarized):**
1. **The demand is on mobile and the MVP is not.** The only willingness-to-pay signal (HN-21) asks for an iPad button and MyChart reviews come from phones, yet the MVP is a desktop extension; Google Play restricts accessibility-service use by non-accessibility apps, and banking apps blank screen capture (FLAG_SECURE).
2. **The scam-refusal wedge is thin.** Family scam alerts already sell for $20 to $40 a month, and Android 16 adds call-time protections.
3. **Free generic help covers the rest.** Gemini Live screen sharing, Copilot Vision highlights and iOS 27 Siri read the screen for free; only family rules plus a scam stop plus named escalation is unique, and untested.
What would change the red team's mind: the file's platform baseline test passing (the best free assistant stops at most 1 of 4 scams and never hands off to family), a Play reviewer accepting the accessibility declaration, and 4 of 8 adult children paying a refundable $15.

**Response (main researcher):**
- All three attacks land. Willingness to pay drops from 3 to 2 and scale from 2 to 1 (a routine library breaks with every app change, and the OS makers own the primitives).
- The platform-baseline test in the deep dive is the right first step: if the free assistants already stop scams and offer handoffs, drop the idea.
- Kept live because the HeyClicky-style interaction for older adults with family escalation is the clearest interaction-shift idea in the set, but it is a platform-risk bet.
