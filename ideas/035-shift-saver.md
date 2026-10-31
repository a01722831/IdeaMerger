---
id: "035"
slug: shift-saver
name: Shift Saver
one_liner: "A daily exception queue for home care agencies that fixes EVV visit problems before billing and fills call-outs by text."
target_user: "Home care agencies with 10-200 caregivers on a payer-mandated EVV system they cannot change"
form_factor: "web app"
lens: "Underserved users"
frontier: false
competition: "CROWDED"
confidence: "MED"
status: "killed"
signals: [UND-43, UND-44, UND-45, UND-46, UND-33, UND-34, UND-35, UND-36, UND-17]
scores:
  pain: 4
  evidence: 4
  ai_leverage: 3
  whitespace: 1
  novelty: 2
  why_now: 3
  solo_feasibility: 2
  distribution: 3
  wtp_economics: 4
  scale_defensibility: 2
total: 57.9
price_hypothesis: "$299/month flat for up to 50 active caregivers, $6 per extra caregiver"
model_cost_per_user_month: "$17 per agency (30 caregivers)"
gross_margin: "about 91%"
mvp_weeks: 8
deep_dive: false
red_team: false
---

# Shift Saver

> **Main-thread review, 2026-10-31: KILLED.** CROWDED. Zingage (raised a $12.5M seed, HHAeXchange partner) already fills caregiver call-outs and flags missed clock-ins, and EVV data access is partner-gated; agencies on other EVV vendors are a thin, temporary gap. The file is kept as a record of the competition check.

## 1. One-liner
A daily exception queue for home care agencies that fixes EVV visit problems before billing and fills call-outs by text.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 4 | Daily: lost visits mean unpaid aides and unbilled revenue, and each call-out is a scramble; one owner lost real money and wrote legislation. |
| Evidence quality | 2 | 4 | Nine recent signals (two strong, owner and aide voices, app reviews with dates); none states a price for this product. |
| AI leverage | 2 | 3 | Voice and text call-out coordination and fix-note drafting use the model; exception detection is mostly rules over exports. |
| Whitespace | 2 | 1 | Zingage ($12.5M seed, 400+ agencies, HHAeXchange partner) already answers calls, fills shifts and flags missed clock-ins; four YC companies and the EVV and care-software vendors overlap. |
| Novelty of insight | 1 | 2 | "Value sits in the layer around the EVV vendor" is sound but now the stated path of several funded teams. |
| Why now | 1 | 3 | Realtime voice at $0.05/min is new, but EVV mandates and agency pain are years old. |
| Solo feasibility | 2 | 2 | Needs EVV data (exports or partner access one company can revoke), SMS and voice compliance and PHI handling; the MVP is possible but the risks are structural. |
| Distribution | 2 | 3 | Agency owners are findable in associations, owner communities and "EVV denied visit" searches; Zingage competes in the same places. |
| Willingness to pay and unit economics | 2 | 4 | A 30-caregiver agency has roughly $1M+ of revenue exposed to EVV problems [ESTIMATE]; a $299 price sits far below that and margin is about 91%. |
| Scale and defensibility | 2 | 2 | EVV vendors and funded rivals cap it at 2; payer-rule libraries are the only moat. |
| **Total** | | **57.9** | |

Confidence: MED. FRONTIER: no. Honest read: CROWDED; the best use of this file is as a pointer to what Zingage and its peers leave open.

## 3. The problem
- Who: owners, schedulers and billing staff at home care agencies; aides who are paid by the visit or hour.
- Cost: EVV apps erase completed tasks, so the agency says visits were not done (UND-33); glitches lower pay (UND-34); supervisors chase correction sheets (UND-35); paper timesheet signatures lost real money (UND-43); every call-out on a 24-hour client turns into a fire drill (UND-44).
- Workarounds: daily manual review of exception lists inside the EVV portal, paper correction sheets, Google Voice and group texts for call-outs (UND-45), standby pools and overtime.
- Constraint: managed care organizations force the EVV vendor, so the agency has no alternative (UND-46).
- Gap: a layer that sits outside the forced EVV app, reconciles it against schedules and caregiver confirmations, and writes the fix documentation each payer wants before the claim goes out.

## 4. Evidence
- **UND-43** (strong, 2026-06-21, HN, owner of home care agencies in 13 states): "We lost real money when signatures weren’t collected or were lost because there were times we couldn’t collect a replacement for various reasons." The commenter built a digital signature system and had to get legislation passed to make it valid. https://news.ycombinator.com/item?id=48622007
- **UND-33** (strong, 2026-02-16, Sandata EVV app 1-star): "Quit messing with people’s money and fix this app. I’m sick and tired of being told that I ‘didn’t complete my tasks’ as if I didnt do my job." https://apps.apple.com/us/app/id6451209985
- **UND-46** (medium, 2026-04-05, HHAeXchange app 1-star, agency owner in Pennsylvania): "This app is required by my Agency located in Pennsylvania (PA) and is forced upon Agency’s by Managed Care Organizations (MCOs) therefore there is no alternative choice for Agency’s like mine to choose from to meet Electronic Visit Verification (EVV) requirements." https://apps.apple.com/us/app/id883673336
- **UND-44** (medium, 2026-08-24, r/Entrepreneur, 18 pts / 20 comments, owner): "Just trying to figure out what systems other people have put in place so every call-out or no-show doesn’t turn into a complete fire drill." https://www.reddit.com/r/Entrepreneur/comments/1vx6lpd/
- **UND-45** (medium, 2026-08-22, r/Entrepreneur, owner): "We're still growing, but between caregivers, families, new client calls, scheduling, recruiting, etc. I'm realizing Google Voice probably isn't going to cut it much longer." https://www.reddit.com/r/Entrepreneur/comments/1vvpt1u/
- **UND-35** (medium, 2026-05-08, Sandata app, aide): "The amount of calls I receive from my supervisor to submit correction sheets because SanData doesn’t show them is insane." https://apps.apple.com/us/app/id6451209985
- **UND-34** (medium, 2025-08-18, HHAeXchange app, aide): "This app reflects on your pay. One mistake and you will have a lower pay because this dumb app is glitchy." https://apps.apple.com/us/app/id883673336
- **UND-36** (medium, 2026-06-02, HHAeXchange app, aide): availability entered in the app is ignored by the agency. https://apps.apple.com/us/app/id883673336
- **UND-17** (medium, 2026-08-21, Sandata app, 79-year-old paid neighbor-carer): the agency forced a switch from a web timekeeping tool that "works perfectly" to a phone app she struggles to use. https://apps.apple.com/us/app/id6451209985
- Note: UND-33 to UND-36 and UND-17 are aide-side app reviews, so the agency-side willingness to pay rests on UND-43, UND-44 and UND-45 plus the competitor traction in section 10.

## 5. The product
- What it does: each morning the agency gets one exception queue. Visits are loaded from the EVV portal export (CSV, or a vendor connection where one exists) and compared with the schedule and caregiver texts. For each problem (missed clock-in, early clock-out, GPS mismatch, missing signature, task not recorded) the queue shows the likely cause, the payer's required fix wording and reason code, and a one-tap action: text the aide to confirm, draft the correction note, or mark for manual review. A second lane handles call-outs: when an aide texts or calls out, the system texts qualified available caregivers in ranked order (continuity, hours, overtime risk, distance), then calls if nobody answers, and hands the scheduler a confirmed replacement.
- Core AI loop: EVV export + schedule + messages -> rules flag candidates -> model reads notes and messages, explains the cause and drafts the fix per payer -> scheduler approves -> corrections or messages sent -> outcome tracked (billed, denied) -> rules improve.
- Interaction model: web queue for the scheduler and billing lead, SMS with caregivers (voice as fallback), weekly revenue-saved report. Nothing is written into the EVV system by the MVP; the user applies the fix there.
- Form factor: web app.
- Day in the life: at 7:05 the scheduler sees 14 exceptions from yesterday, 9 with a drafted fix and 3 waiting on aide replies. A 24-hour client's overnight aide calls out at 10 pm; the system texts four aides and the second confirms in 12 minutes.
- Safety lines: PHI minimized (visit IDs and first names only where possible), no clinical content, no changes to times without the aide's confirmation and a manager's approval, because falsifying visit data is fraud.

## 6. Why the LLM is load-bearing
- Payer-specific fix notes, reason codes and the free-text justification they require are language work, and replies from aides arrive as messy texts and voice messages.
- Ranking and persuading replacement caregivers across many small constraints is coordination the model does well.
- Without the model the product is an exception report plus a mass-text tool, which care-management suites already include.

## 7. The insight
- Agencies cannot change the EVV vendor, so value sits in a reconciliation layer around it, and denied visits are direct revenue loss. Honest limit: Zingage and the EVV vendors reached the same conclusion first.

## 8. Why now, and why this does not exist yet
- Why now: voice and text agents at $0.05/min or less make call-out coordination cheap (`research/LANDSCAPE.md` section 6). Frontier-model reading of messy notes is reliable enough for drafts.
- Why it already exists: see section 10. Zingage, funded in November 2025, does call-outs and flags exceptions with HHAeXchange. The open gap is the agency on a different EVV aggregator and the payer-specific fix documentation, not the idea.

## 9. Inspiration and derivation
- Parents: Zingage (AI operator for home care), HHAeXchange EVV Compliance Management, ShiftCare's pre-submission denial dashboard, Claim Health (denials for at-home care).
- Changed: target user (small agencies on forced Sandata or other aggregators, not only HHAeXchange), core job (exception clearance with per-payer documentation), business model (flat price against revenue at risk). Two or three of five changed.

## 10. Competition check
Queries run:
1. WebSearch: "home care agency AI fills caregiver call-outs open shifts texts calls caregivers automatically scheduling Zingage"
2. WebSearch (Product Hunt): "site:producthunt.com home care agency software caregiver scheduling EVV AI" (no Product Hunt page returned)
3. WebSearch (YC directory): "site:ycombinator.com/companies home care agencies AI caregivers scheduling voice agent EVV billing"
4. WebSearch (EVV vendors and payers): "EVV visit exceptions missed clock-in reconciliation before billing home care agency AxisCare OR WellSky OR HHAeXchange OR Sandata aggregator denied claims software"
5. WebFetch of the Zingage funding article and the HHAeXchange Partner Connect listing for Zingage.

| Product | What it does | Price | How it differs |
|---|---|---|---|
| [Zingage](https://www.zingage.com) ([$12.5M seed, Bessemer-led, 2025-11-18](https://www.healthcareittoday.com/2025/11/18/zingage-raises-12-5m-to-build-the-ai-care-delivery-platform-for-home-care/); [HHAeXchange partner listing](https://www.hhaexchange.com/partner-connect/zingage)) | AI operator: answers inbound calls, fills open shifts on call-outs, "documents every resolution in HHAeXchange without staff involvement" and "flags exceptions such as missed clock-ins and early clock-outs"; 400+ agencies; runs on Claude and ElevenLabs per its [Claude case study](https://claude.com/customers/zingage) (vendor-reported results, such as under 40 minutes from call-out to confirmed replacement) | not stated | The funded direct rival on both halves, integrated with HHAeXchange (a headline cites its network as 32,000+ providers) |
| [MochaCare](https://www.ycombinator.com/companies/mochacare), [TakeCareOS](https://www.ycombinator.com/companies/takecareos), [Sage Care](https://www.ycombinator.com/companies/sagecare), [Claim Health](https://www.ycombinator.com/launches/NPm-claim-health-ai-revenue-platform-for-at-home-care-providers) (all YC) | AI scheduling and hiring for home care; AI-native home care operations; client intake and caregiver matching; AI revenue platform (billing, denial appeals, voice agents to insurers) | n/a | Overlapping halves; Claim Health is closest to the denial side |
| [HHAeXchange EVV Compliance Management](https://knowledge.hhaexchange.com/enterprise/Content/Documentation/Visit/Visit-N-EVV-Management-P.htm) | Visit maintenance and compliance review in the EVV system itself; a visit missing a clock-in or clock-out is non-compliant | bundled | The vendor owns the data and the exception workflow |
| [ShiftCare](https://shiftcare.com/), [CareSmartz360](https://www.capterra.com/p/147660/CareSmartz360/) (voice bot in its AI layer, per one profile), AxisCare (AI matching), AlayaCare Visit Optimizer, WellSky Personal Care ([IntuitionLabs roundup](https://intuitionlabs.ai/software/home-health-home-care)) | Scheduling, EVV and billing suites with growing AI features; ShiftCare says most EVV denials arise at reconciliation and sells a pre-submission dashboard ([blog](https://shiftcare.com/us/blog/top-medicaid-evv-features-fewer-claim-denials)) | not found | Suites that agencies on a free choice of vendor already use; irrelevant when the payer forces the EVV vendor |
| Product Hunt | No relevant listing found | n/a | Not a launch-site category |

Classification: **CROWDED**. A funded AI-native competitor with an HHAeXchange partnership, four YC companies nearby, and suites adding AI.

Platform risk: very high. HHAeXchange, Sandata and the care-software vendors own the visit data and can add AI exception handling and call-out filling to their own apps; Partner Connect already has an "AI Workforce Optimization" category. Frontier labs will not build this directly (Claude powers Zingage). Per the rubric this caps Scale and defensibility at 2 and Whitespace at 3; the funded direct rival puts Whitespace at 1.

## 11. Business model
- Payer: the agency owner. Price: $299/month flat for up to 50 active caregivers, $6 per extra caregiver, first month's exception audit free. Anchors: no competitor price was visible; the sizing anchor is revenue at risk. A 30-caregiver agency at 25 billed hours a week and $30 an hour [ASSUMPTION] bills 30 x 25 x 52 x $30 = $1.17M a year; if 2% is lost to EVV problems [ASSUMPTION], that is $23K a year, about $1,950 a month. $299 is 15% of that.
- Model and messaging cost per agency per month [ESTIMATE], 30 caregivers, 4,500 visits, 40 call-outs: triage of all visits on Haiku 5.5, 500 in x $0.10/1M + 100 out x $0.50/1M = $0.0001 x 4,500 = $0.45; 8% exceptions (360) read and explained on Sonnet 5.5, 3,000 in x $2/1M + 500 out x $10/1M = $0.011 x 360 = $3.96; fix and message drafts 360 x $0.005 = $1.80. Call-outs: 6 SMS x $0.01 = $0.06 plus 3 minutes of voice at $0.05 + $0.02 telephony = $0.21 [telephony and SMS prices ASSUMED, not in the landscape table], so $0.27 x 40 = $10.8. Total about $17.
- Gross margin [ESTIMATE]: ($299 - $17 - $8.97 Stripe) / $299 = 91%. Compliance, security and support costs (HIPAA program, BAAs) are extra and not priced here.

## 12. Market size
- Buyers [ESTIMATE]: a headline reports HHAeXchange alone has a network of 32,000+ home care providers (Zingage press coverage, title). Assume half are agencies with 10 to 200 caregivers = 16,000 [ASSUMPTION].
- Revenue: 16,000 x $299 x 12 = $57M a year if all bought. At 1% (160 agencies) = $0.57M ARR; at 3% (480) = $1.7M ARR. For scale, Zingage reports 400+ agencies a year after raising $12.5M, so even 1% is a stretch for a solo entrant.
- Reading: a real market with a funded leader; a solo product needs a niche the leader skips.

## 13. Go-to-market
- First 100: (1) owner communities where UND-44 and UND-45 were posted (r/Entrepreneur home care threads), with a free "EVV exception audit" offer, about 30; (2) Home Care Association of America and state home care association members and webinars [ASSUMPTION: open to vendor content; Zingage already has an HCAOA listing], about 30; (3) SEO on "EVV visit denied how to fix", "Sandata EVV missed clock in", "home care call-out coverage template", about 30; (4) HN threads where owners describe their own builds (UND-43), about 10.
- Growth loop: the weekly "revenue saved" report is forwarded to the owner's accountant and peers; owners of several agencies (like the 13-state owner) roll it out to each.

## 14. Moat and scale path
- Moat: a library of payer and state rules for EVV exception fixes (reason codes, free-text requirements) built from agencies' outcomes; caregiver response data for ranking replacements. Moderate.
- Scale path: more states and payers, billing integration, then recruiting and retention modules. This moves toward Zingage's scope.

## 15. Solo feasibility
- MVP (8 weeks): CSV import of EVV and schedule exports, exception rules for two states and two payers, queue UI, fix-note drafts, SMS call-out lane with ranking, outcome tracking. No EVV write-back, no voice in v1.
- Running cost before revenue: about $60 to $150 a month (hosting, SMS numbers and registration, 3 pilot agencies at about $17).
- Hardest risks: data access (an export may carry PHI and the EVV vendors can change formats or terms), HIPAA obligations, SMS consent rules, and wrongly nudging staff to edit visit times.

## 16. Pre-mortem
1. Zingage or an EVV vendor ships the same exception queue for free inside its product.
2. No EVV export without PHI, or vendors restrict export use, killing the data supply (kill criterion 4).
3. A recommended fix is wrong or reads as falsification; an audit finding ends trust.

## 17. Cheapest validation test
- What: offer a free "EVV exception audit" to 10 agencies in the communities above; they send 30 to 60 days of de-identified EVV exports and payer denial lists [ASSUMPTION: de-identified exports are available]; run the pipeline by hand; deliver a report of exceptions caught, fixes drafted and dollars at risk; ask for $299/month.
- Cost: about $30 in model calls plus time. Duration: 4 weeks.
- Pass: at least 6 of 10 agencies send data, the audit finds at least $1,500 a month of recoverable revenue on average, and at least 3 agree to pay. Fail: fewer than 3 send data, or most already use Zingage or their vendor's compliance tool.

## 18. Open questions
- Recommendation: do not build the call-out filler; it is Zingage's core and funded. The only gap in the evidence is agencies on EVV aggregators other than HHAeXchange (Sandata appears in UND-33, UND-35 and UND-17) and payer-specific fix documentation. Test the audit offer in section 17 first; if most agencies already have a tool, kill.
- Can an agency export EVV data without a partner agreement, and is it allowed to hand it to a third party?
- Which states and payers have the highest EVV denial rates and the strictest fix wording?
- What does an agency pay today for scheduling and EVV software? No price was found.
- Is a BAA and HIPAA program feasible for a solo founder before the first customer?
