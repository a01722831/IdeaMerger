---
id: "003"
slug: fix-desk
name: Fix Desk
one_liner: "Text-and-voice maintenance line that triages tenant requests and books a landlord's own vendors, with one-tap owner approval."
target_user: "Self-managing landlords with 2-50 doors and their own vendors"
form_factor: "other"
lens: "Pain-first"
frontier: false
competition: "CROWDED"
confidence: "MED"
status: "developed"
signals: [PRO-011, PRO-012, PRO-013, REV-13, REV-14, REV-15, REV-17]
scores:
  pain: 3
  evidence: 3
  ai_leverage: 3
  whitespace: 1
  novelty: 2
  why_now: 2
  solo_feasibility: 4
  distribution: 3
  wtp_economics: 3
  scale_defensibility: 2
total: 53.7
price_hypothesis: "$15/month flat for up to 10 doors"
model_cost_per_user_month: "$2.10"
gross_margin: "86%"
mvp_weeks: 5
deep_dive: false
red_team: false
---

# Fix Desk

## 1. One-liner
Text-and-voice maintenance line that triages tenant requests and books a landlord's own vendors, with one-tap owner approval.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Weekly phone tag for a self-manager, but a nuisance that costs time, not a loss event; the alternative is a 10% manager fee (PRO-011). |
| Evidence quality | 2 | 3 | Seven recent signals, one strong on the pain; the REV signals show an AI backlash, not demand for this product. |
| AI leverage | 2 | 3 | Model triages photos and free text and negotiates windows, but a form plus vendor list covers half of it. |
| Whitespace | 2 | 1 | Vendoroo, Latchel, AppFolio Realm-X, three YC companies and several WhatsApp-first tools already do this; see section 10. |
| Novelty of insight | 1 | 2 | Own vendors plus owner approval is sensible but others already offer it. |
| Why now | 1 | 2 | Photo triage got cheap, but everyone noticed in 2025-26; the only edge is the backlash against AI front doors. |
| Solo feasibility | 2 | 4 | SMS, photos, scheduling and approvals on off-the-shelf APIs in about 5 weeks; US SMS registration is the lead-time risk. |
| Distribution | 2 | 3 | BiggerPockets, r/Landlord and SEO are real channels, but every competitor targets the same queries. |
| Willingness to pay and unit economics | 2 | 3 | Margin is high at $15/month; self-managers are frugal and compare against free spreadsheets. |
| Scale and defensibility | 2 | 2 | PM suites and funded coordinators can copy it; vendor-bench data is thin lock-in. |
| **Total** | | **53.7** | |

Confidence: MED. FRONTIER: no. **Recommendation: this is CROWDED; kill it unless the section 17 test passes.**

## 3. The problem
- Who: landlords with 2-50 doors, often with a day job, who manage themselves to avoid a manager's fee of about 10% of rent.
- What hurts: scheduling a repair is tenant-plumber-landlord phone tag (PRO-011); tenants text or WhatsApp whoever's number they have and requests sit when someone is off (PRO-012); a manager silently handled compliance notices that self-managers must rebuild in spreadsheets (PRO-013).
- Cost [ESTIMATE]: a 10-unit landlord at $1,500 rent pays about 10 x $1,500 x 10% = $1,500 a month to a manager; one BiggerPockets commenter reports saving about $7,200 a year by self-managing (PRO-013 note). The time cost is a few hours a week.
- Workaround: texts, a vendor list in a phone, spreadsheets; or a manager; or a vendor-coordination service. Tenants and owners have also learned to distrust AI front doors (REV-13, REV-14, REV-15).

## 4. Evidence
- PRO-011 (strong, BiggerPockets, 2026-09-22): "I text the tenant for their availability, call a plumber, get a completely different time slot, and then mediate back and forth while sitting at my day job. I really don't want to hand over 10% of my gross rent to a full-service property manager just to handle scheduling calls, but doing it manually is driving me crazy."
- PRO-012 (medium, r/PropertyManagement, 2026-10-16): "They text or WhatsApp a photo of a leak, a question about rent, a noise complaint, all to whoever’s number they have. When someone on the team is off, the request just sits there and we find out when the tenant calls angry."
- PRO-013 (medium, BiggerPockets, 2026-06-10): "Your PM was (hopefully) handling AB 1482 annual rent cap notices, just-cause requirements, and related compliance tasks."
- REV-15 (strong, App Store DoorLoop, 2026-03-24): "Submitting a maintenance request forces me to speak with an AI agent that doesn’t understand what im asking it to do, instead of just letting me fill out a form." At least six more reviews repeat it.
- REV-14 (medium, r/PropertyManagement, 2026-10-30): "It mis-sorts urgent communications as non-urgent, Whereas before a person would triage, or it would trust the form input for severity. Now there is property damage."
- REV-13 (medium, App Store AppFolio, 2026-04-07): a user says the AI additions made the product worse: "You are making your product inferior."
- REV-17 (strong, r/PropertyManagement, 2026-10-26): a landlord built his own email agent for Buildium ("I created one for my own Builidium setup."), a sign owners hack their own automation.
- New evidence (not in SIGNALS.md): r/PropertyManagement, 2026-10-26, https://www.reddit.com/r/PropertyManagement/comments/1xft6qs/ (25 comments, reads like market research): "Every after-hours setup I've seen eventually hits the same problem: tenants call everything urgent."

## 5. The product
- Outcome: one phone number per portfolio that tenants text, WhatsApp or call; the request is triaged, the owner's own vendor is booked, access is confirmed, and the owner taps once to approve any quote over their limit.
- Core AI loop: input (tenant text, photo, voicemail) -> model work (classify trade and urgency under the owner's written rules, run a cheap troubleshooting step such as breaker or filter, propose windows to the owner's vendors by text, parse vendor replies and quotes, chase silence) -> output (booked visit, confirmations, cost log per unit, monthly summary) -> feedback (owner overrides become rules).
- Guardrails taken from the backlash: the line says it is an automated assistant for the owner; it sends only owner-approved templates to tenants; safety words (gas, smoke, flooding, sparks, carbon monoxide) trigger an immediate phone call to the owner; any doubt escalates instead of guessing urgency.
- Interaction: SMS and WhatsApp for tenants and vendors, a plain web dashboard for the owner. Optional compliance-notice calendar (PRO-013).
- Form factor: SMS/WhatsApp line plus web app.
- Day in the life: at 9:40 pm a tenant texts a photo of a dripping trap. Fix Desk matches it to "non-urgent, plumbing", asks two questions, and offers the owner's plumber Thursday 9-11 or 2-4. The plumber picks 2-4, the tenant confirms, and the owner sees a $180 quote and taps approve.

## 6. Why the LLM is load-bearing
Tenants describe problems in free text and photos in any language, vendors answer with "can do Thursday after 2" or a photo of a handwritten quote, and three parties must be reconciled. A form and a vendor list handle intake but not the negotiation of windows, the parsing of replies or the chasing. Without the model it is a ticket system, which is what the incumbents' portals already are.

## 7. The insight
Owners want their own vendors and control of spend, and they distrust a bot that speaks for them. So the AI should be a dispatcher on the owner's team: coordinate three parties, apply the owner's rules, escalate on doubt. Honest note: Guardian Landlord already drafts messages for owner approval, and Latchel lets owners add their own technicians, so this insight is shared, not unique.

## 8. Why now, and why this does not exist yet
It does exist. Photo and text triage became cheap in 2024-26 and AppFolio, Vendoroo, three YC companies and small WhatsApp tools shipped it. The open slice I could find is a self-manager with 2-50 doors who has no property-management software, wants SMS only, and wants a flat fee. That slice is small and its serving tools are early (Guardian Landlord has 11 followers on Product Hunt), but it is cheap to serve for anyone.

## 9. Inspiration and derivation
- Parents: Vendoroo and Latchel (coordination for managers), AppFolio Realm-X Maintenance Performer, Guardian Landlord (owner-in-the-loop action plans).
- Changed: target user (self-manager, not a manager with 50+ doors), interaction model (SMS/voice, no portal), business model (flat fee for up to 10 doors, not per-unit with minimums), vendor model (the landlord's own bench).

## 10. Competition check
- Queries run: (1) "AI maintenance coordinator for small landlords tenant texts triage vendor scheduling own vendors Vendoroo Latchel pricing per unit"; (2) "site:producthunt.com landlord maintenance requests AI tenants text WhatsApp vendors self-managing"; (3) "site:ycombinator.com/companies property management maintenance requests AI tenants vendors dispatch"; (4) "AppFolio Realm-X maintenance AI work orders Buildium DoorLoop Nora AI maintenance triage 2026 features". Also: Product Hunt page read for Guardian Landlord, Vendoroo SMB page read, Reddit archive pull of r/Landlord and r/PropertyManagement (Aug-Oct 2026), HN search (0 hits), news search for Latchel funding. The App Store lookup script returned HTTP 403.
- [Vendoroo](https://vendoroo.ai): AI maintenance coordinator that triages tenant requests, troubleshoots, assigns vendors and follows up. [SMB page](https://www.vendoroo.ai/smb) lists "Vendor selection & dispatch" and "Owner approvals, warranties & complex coordination"; own-vendor use not stated; the page says to book a demo. Published prices conflict across pages: a $5 per unit per month base module, a $400 monthly minimum on another tier, and a company blog range of $3 to $8.50 per door (search summary). Integrations include [Rent Manager](https://www.rentmanager.com/integrations/vendoroo/). Funding not verified.
- [Latchel](https://rentredi.com/?p=5279) (listed on RentRedi): $15 per unit per month for 24/7 emergency service, $25 for full coordination, month to month; owners can add their own technicians to the network. Raised $16.7M (HousingWire headline, 2022-07-27).
- [AppFolio Realm-X Maintenance Performer](https://www.appfolio.com/property-manager/maintenance): answers residents in about six seconds (vendor claim), triages, reads photos, opens work orders; vendor outreach added in [Q1 2026](https://www.appfolio.com/blog/product-update-2026-q1); dispatches to in-house techs or the Lula network. Only for AppFolio customers, and users complain (REV-13). DoorLoop's AI intake draws the same complaints (REV-15). No 2026 AI-maintenance details surfaced for Buildium.
- [Guardian Landlord](https://www.producthunt.com/products/guardian-landlord) (Product Hunt, launched 2026): "Self-manage your rentals. Still live your life."; AI turns each request into urgency, who to call and a drafted tenant message; "Away Mode" where real people handle issues; free options and 3 months free; 2 upvotes, 11 followers. Closest to this user; own-vendor use and auto-sending not confirmed.
- WhatsApp-first tools: [TenantFix](https://www.saashub.com/tenantfix-app), [AskLettie](https://peerpush.com/p/asklettie), [TenantDesk](https://www.capterra.in/software/1101520/TenantDesk), and [Rentway](https://hunted.space/product/rentway) (all-in-one, flat rate). Vendor claims only.
- YC: [CentralComs (P26)](https://www.ycombinator.com/companies/centralcoms), [Haven](https://www.ycombinator.com/companies/haven-2) (a job post claims 10,000+ properties, unverified) and [Brickwise](https://ycombinator.com/companies/brickwise), all selling to property managers. Also [Magic Door](https://magicdoor.com/features/maintenance/maintenance-requests). Reddit shows more builders arriving (r/PropertyManagement, 2026-10-24).
- Classification: CROWDED. Funded or popular direct competitors exist for managers and for self-managers.
- Platform risk: high for managers (AppFolio ships it inside the suite; DoorLoop and Buildium can follow); lower for self-managers who run no suite, where the threat is cheap copycats. A general assistant can draft messages but cannot hold a vendor bench, text vendors on a schedule or keep case state.

## 11. Business model
- Payer: the landlord. Price hypothesis: $15 a month flat for up to 10 doors ($1.50 a door), $1 per extra door. Anchors: Vendoroo $3-$8.50 per door, Latchel $15-$25 per unit, a manager's 10% of rent (PRO-011).
- Cost per active user per month [ESTIMATE], 8 units, 4 requests a month [ASSUMPTION: 0.5 per unit]: photo triage on Sonnet 5.5 at 3,000 in + 600 out = $0.006 + $0.006 = $0.012; 11 Haiku 5.5 calls at $0.00055 = $0.006; total $0.018 per request x 4 = $0.07. Voice: 2 calls x 2 minutes x $0.05 (GPT Live) = $0.20. SMS and MMS: 14 messages per request x 1.2 segments x $0.01 [ASSUMPTION] x 4 = $0.67. Phone number $1.15 [ASSUMPTION]. Total about $2.10.
- Gross margin (15 - 2.10) / 15 = 86%.

## 12. Market size
Bottom-up [ESTIMATE]: a search summary of Census and IRS data says individuals own about 70% of rental properties and that 6.7% of individual filers, about 10.3 million, reported rental income in 2018 (sources named in the results: [CRS R47332](https://sgp.fas.org/crs/misc/R47332.pdf), [NBER](https://www.nber.org/papers/w35258); not opened). Assume 10% self-manage 2-50 doors, text-first and would pay: about 1.0 million. At 1% penetration, 10,000 x $15 x 12 = $1.8M ARR. A real but modest niche business.

## 13. Go-to-market
- First 100: answer maintenance-coordination threads on BiggerPockets (the PRO-011 thread is the model) and r/Landlord; local real-estate-investor club meetings; free tools (emergency versus routine policy generator, vendor-bench template). SEO: "how to handle maintenance requests as a landlord", "after hours maintenance policy for landlords".
- Loop: vendors who work for several landlords see the line and ask to be on it; tenants carry the number to the next unit. Weak, and I would not count on it.

## 14. Moat and scale path
Little. The vendor bench, per-unit repair history and owner rules create mild switching cost. Scale path: more doors per owner, small managers (competes with Vendoroo SMB), compliance calendar. Capped at 2 by platform risk.

## 15. Solo feasibility
- MVP in 5 weeks: SMS number with US registration started on day 1, photo triage, vendor bench and scheduling, owner approval link, cost log, web dashboard. WhatsApp and voice later.
- Running cost before revenue: about $50-80 a month (numbers $5, hosting $20, models $10, SMS $15).
- Hardest risk: mis-triage of a real emergency (REV-14) and carrier registration lead time for business SMS.

## 16. Pre-mortem
1. Nobody switches: Vendoroo, Latchel and AppFolio own the manager segment and cheap WhatsApp tools undercut self-managers.
2. One missed emergency causes damage and the owner blames the tool; liability and trust end the product.
3. Low willingness to pay and churn when landlords sell or hire a manager make $15 accounts uneconomic after acquisition cost.

## 17. Cheapest validation test
Recruit 20 self-managing landlords (BiggerPockets, r/Landlord). Give each a shared number for 30 days and run it by hand with model drafts. Cost about $150 plus time. Pass: 12 of 20 route 3 or more real requests, 5 or more prepay $15 for three months, and they prefer it to Guardian Landlord or Latchel. Fail: fewer than 3 pay, or "I would just text my plumber" wins.

## 18. Open questions
- Recommendation: kill the general maintenance front door. The only wedge worth testing is own-vendor bench plus owner approval rules, SMS-only, flat fee, for 2-50 door self-managers who run no suite, paired with a compliance-notice calendar (PRO-013).
- Does Vendoroo or Latchel serve a self-manager with 8 doors, and at what real price?
- Do tenants accept an automated line when the owner signs the messages?
- How long does US business SMS registration take in 2026 [UNVERIFIED]?
