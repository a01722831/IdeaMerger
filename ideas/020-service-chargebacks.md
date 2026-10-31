---
id: "020"
slug: service-chargebacks
name: Service Chargebacks
one_liner: "Builds reason-code-specific chargeback evidence packets from job records for salons, trades and studios paid by card."
target_user: "Service businesses (salons, trades, studios) taking card payments on Stripe or Square with job records in Jobber, Vagaro or similar"
form_factor: "web app"
lens: "Transplant"
frontier: false
competition: "CROWDED"
confidence: "MED"
status: "developed"
signals: [REV-03, REV-31, REV-24, PRO-218, PRO-219, SVC-45]
scores:
  pain: 3
  evidence: 3
  ai_leverage: 3
  whitespace: 2
  novelty: 2
  why_now: 2
  solo_feasibility: 3
  distribution: 3
  wtp_economics: 2
  scale_defensibility: 1
total: 49.5
price_hypothesis: "$19/month plus 10% of recovered disputes (market success fees run 10% to 25%)"
model_cost_per_user_month: "$0.05"
gross_margin: "93%"
mvp_weeks: 6
deep_dive: false
red_team: false
---

# Service Chargebacks

## 1. One-liner
Builds reason-code-specific chargeback evidence packets from job records for salons, trades and studios paid by card.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | An $8,000 loss and blocked accounts are severe (REV-03), but disputes are rare per merchant, so frequency is low. |
| Evidence quality | 2 | 3 | Six signals, three strong, but only REV-03 and REV-31 are service-business chargebacks and none states willingness to pay for help. |
| AI leverage | 2 | 3 | The model maps messy job records to a reason-code argument; the rest is integrations and templates. |
| Whitespace | 2 | 2 | Funded generic leaders (Chargeflow, Justt) and Stripe Smart Disputes; no service-specific product found, so 2 and not 1. |
| Novelty of insight | 1 | 2 | Moving an e-commerce pattern to services is an obvious extension for the incumbents. |
| Why now | 1 | 2 | Template packets predate LLMs; the model only adds handling of unstructured evidence. |
| Solo feasibility | 2 | 3 | Stripe and Square dispute APIs are public; access to job records and platform-held accounts is the unknown. |
| Distribution | 2 | 3 | High-intent SEO at the moment of a dispute and Stripe and Square app marketplaces; crowded, with no growth loop. |
| Willingness to pay and unit economics | 2 | 2 | Success fees on about 6 disputes a year yield roughly $7 a month per merchant, so a flat fee is needed and is unproven. |
| Scale and defensibility | 2 | 1 | Feature-sized: Stripe, Chargeflow or a field-service platform can add a services path. |
| **Total** | | **49.5** | |

Confidence: MED. FRONTIER: no.

## 3. The problem
- Who: owners of salons, studios, mobile trades and similar service businesses that take cards through Stripe, Square or a booking or field-service platform.
- How often: rare per merchant (assume about 6 disputes a year [ASSUMPTION]) but severe: a lost $8,000 chargeback, a blocked account, withheld payouts (REV-03, REV-31, REV-24).
- What goes wrong: merchants submit receipts and see the dispute decided against them, are not clearly notified, cannot appeal, and the platform then withholds new payments to recover the amount (REV-31). Processors hold payouts and demand invoices and incorporation papers (REV-24).
- Why evidence fails: e-commerce tools prove delivery with tracking numbers; service businesses prove it with signed approvals, job photos, GPS check-ins and texts, which nobody turns into a reason-code argument.
- Workaround today: attach whatever is handy in the processor dashboard, call support, or accept the loss.

## 4. Evidence
Six signals (full rows in `research/SIGNALS.md`): two service-business disputes, one payout hold, two e-commerce disputes and one competitor pricing page:
- REV-03 (strong, 2026-03-14): "I had a customer recently charge back $8000. I filed the dispute gave receipts, etc., and the company still sided with the customer and did not refund the money to me." Shows: an $8,000 loss despite filed receipts; the platform gave no help and blocked the account until the balance was paid. https://apps.apple.com/us/app/id1014146758
- REV-31 (strong, 2026-09-30): "I provided the service and submitted documentation showing that the service was completed, but the dispute was still decided against me." Shows: a second platform (Vagaro) with the same outcome; Booksy shows four more chargeback cases with no final answers (noted in the signal). https://apps.apple.com/us/app/id346778559
- REV-24 (strong, 2026-09-09): "They put me through a rigorous process where I had to send them everything from invoices to article articles of incorporation, internal emails, etc. they’ve held my money for more than three weeks." Shows: processors that hold money and ask for documents; this is a payout hold, adjacent to a dispute. https://apps.apple.com/us/app/id881629660
- SVC-45 (medium, 2026-07-20): "Published rates cluster around 20 to 25 percent of recovered revenue. Chargeflow publishes 25%; Disputifier publishes 20% capped at $250 per won case (both checked July 20, 2026)." Shows: the evidence-packet category is already sold as software at 20% to 25% success fees (the signal itself tags it CROWDED). https://redo.com/resources/articles/comparisons/chargeback-representment-pricing
- PRO-218 (medium, 2026-09-15): an e-commerce store at a 1.2% chargeback rate loses most "item not received" disputes despite delivery tracking. PRO-219 (medium, 2026-10-25): an eBay seller faces a $338 bank dispute after declining a return.
- New evidence (not in SIGNALS.md), r/Entrepreneur, 2026-10-25 (title only): "What I learned about fighting chargebacks as a small seller (the reason code matters more than you think)" Shows: sellers are discovering the reason-code insight on their own. https://www.reddit.com/r/Entrepreneur/comments/1xf55ql/

## 5. The product
- Outcome: when a dispute lands, the owner reviews a one-page argument with the right exhibits and taps submit; before disputes, completed jobs automatically collect proof.
- Core AI loop: input (Stripe or Square dispute webhook; job records: estimate, signed approval, completion photos, GPS check-in, texts, prior visits, refund policy acceptance) -> the model classifies the reason code, picks the exhibits that answer that claim and drafts the argument -> output: evidence packet PDF and fields submitted through the Stripe or Square dispute API -> feedback: the outcome (won, lost, reason given) is logged per reason code and vertical and tunes exhibit selection.
- Prevention: at job completion a text asks the customer to confirm the work (photo of the result, one tap), creating dated evidence and cutting "service not provided" claims.
- Interaction model: web app plus email and SMS alerts; owners upload or forward missing evidence; read-only job-record connectors where an API exists (Jobber first).
- Form factor: web app.
- Day in the life: a mobile detailer gets a "services not rendered, $480" dispute. The app pulls the booking, the signed work order, before and after photos with timestamps, the GPS check-in and a thank-you text. The owner reviews the argument in two minutes and submits. The outcome is tracked.

## 6. Why the LLM is load-bearing
- Service evidence is unstructured (texts, photos, estimates, notes); mapping it to the claim made under a given reason code is judgment, not field filling.
- The written argument must cite exhibits in the issuer's terms and vary by reason code.
- Without the model it is a template packet with attachments, which is roughly what Stripe's rules engine already does with transaction data.

## 7. The insight
E-commerce dispute tools prove delivery with tracking numbers; service businesses prove it with photos, signatures and messages, which only a language model can turn into a reason-code argument. Honest note: the idea is a vertical adapter of a crowded category, not a new category.

## 8. Why now, and why this does not exist yet
- Why now: models read photos and message threads cheaply, and Stripe (Smart Disputes) and Square (Disputes API) expose programmatic dispute evidence.
- Why a service-specific product may not exist: disputes are rare per merchant, so revenue per customer is small; job records sit inside field-service platforms that do not expose them; payments may be run by the platform.
- It is not unserved in principle: Chargeflow integrates with Square and many systems, and a "services" template is a short step for any of them.

## 9. Inspiration and derivation
- Parents: Chargeflow, Justt, Chargehound, DisputeNinja, ChargePilot and Stripe Smart Disputes (all e-commerce or SaaS evidence packets).
- Changed: target user (salons, trades and studios), core job (assemble evidence from job records and capture proof at job completion), distribution (field-service and booking platform communities rather than Shopify), and business model (flat fee plus success fee).

## 10. Competition check
Queries run (2026-10-31):
1. Web: "chargeback evidence AI service business Stripe dispute automatic evidence packet reason code"
2. Product Hunt: "site:producthunt.com chargeback dispute evidence automation AI win disputes" (surfaced a hunted.space mirror of one PH launch)
3. YC: "site:ycombinator.com/companies chargebacks disputes payments merchants AI"
4. Stripe App Marketplace: "marketplace.stripe.com dispute management app evidence submit chargeback Stripe App Marketplace" (marketplace pages not returned; vendor blogs and Stripe docs instead)
5. Platform: "Square disputes chargebacks respond with evidence automatically AI dispute assistant sellers 2026"; also read Stripe's Smart Disputes docs and the ChargePilot listing, and an Apple App Store lookup ("chargeback dispute evidence", only noise).

Findings:
- [Stripe Smart Disputes](https://docs.stripe.com/disputes/get-started/smart-disputes): "automatically compiles and submits high-quality evidence packets on your behalf before the dispute deadline" using an AI rules engine over transaction, Stripe and cardholder data; merchants can add evidence and Stripe merges it. Its documented recommended-evidence examples are shipping carrier, tracking and email, so the examples are goods-oriented; eligibility for service disputes is not stated. No fee stated on that page.
- [Chargeflow](https://fintech.global/2025/11/19/chargeflow-launches-ai-suite-after-35m-series-a/): $35M Series A (Nov 2025), AI suite, integrates with 100+ systems including [Square](https://www.chargeflow.io/integration/square); published 25% success fee (SVC-45).
- [Justt](https://techcrunch.com/2021/11/16/justt-comes-out-of-stealth-with-70m-in-funding-to-help-online-merchants-fight-false-chargebacks-with-ai): raised $70M in 2021 (headline); AI against false chargebacks for online merchants.
- YC: [Chargehound](https://www.ycombinator.com/companies/chargehound) (one integration to automate disputes), [DisputeNinja](https://www.ycombinator.com/launches/NDa-disputeninja-ai-powered-chargeback-responses) (YC S23; AI chargeback responses, aimed at software and AI startups on Stripe).
- [Disputed.ai](https://www.crowdfundinsider.com/2025/03/237415-ai-powered-chargeback-platform-disputed-ai-raises-1-12-million-in-seed-funding/): $1.12M seed (Mar 2025); targets merchants with 1,000 to 100,000 chargebacks a month.
- [ChargePilot](https://hunted.space/product/chargepilot): live on the Stripe App Marketplace since March 2026; 15% success fee, no subscription; pulls evidence from Stripe, Shopify, WooCommerce, BigCommerce, Recharge, Skio, Gorgias, Help Scout, ShipStation and Gmail; 3 upvotes. E-commerce focus; no service-business mention.
- Shopify apps with success fees: [Chargeback Dispute Specialist](https://apps.shopify.com/chargeback-specialist) (15% on wins), [Chargeback Dispute: Recovery](https://apps.shopify.com/chargeback-dispute) (10% on wins); Disputifier 20% capped at $250 (SVC-45).
- [Square Disputes API](https://developer.squareup.com/docs/disputes-api/overview): developers can build tools that submit evidence automatically. I found no native Square AI responder.
- [Signifyd's Stripe app](https://martechvibe.com/article/signifyd-launches-an-app-for-stripe) shows dispute cases inside the Stripe dashboard (visibility, not evidence building).

Classification: CROWDED. Several funded or YC-backed direct competitors serve the evidence-packet job for any Stripe or Square merchant, and Stripe's own engine does it natively. No service-business-specific, job-record-backed product turned up, which is the only reason Whitespace is 2.

Platform risk: high. Stripe is both processor and vertical incumbent and already auto-builds and submits packets; extending recommended-evidence fields to service documentation is an obvious step (Stripe's API has service evidence fields [UNVERIFIED, from memory]). Chargeflow already connects to Square. Field-service platforms (Jobber, Vagaro, Booksy) could build it where they run payments. Anthropic, OpenAI and Google are unlikely to ship dispute-specific tooling. I expect Stripe or a funded vendor to cover services within 12 months, which caps Scale at 1 and Whitespace at 2.

## 11. Business model
- Payer: the service business, billed monthly plus a success fee.
- Price hypothesis: $19/month plus 10% of recovered disputes. Market success fees: Chargeflow 25%, Disputifier 20% capped at $250, ChargePilot 15%, Shopify apps 10% to 15%. A pure success fee does not work here: 6 disputes a year x $400 average x 35% win rate [ASSUMPTION] = $840 recovered, and 10% of that is $84 a year, or $7 a month.
- Revenue per merchant: $19 + $7 = $26/month.
- Model cost [ESTIMATE] (prices from `research/LANDSCAPE.md` section 6): per dispute on Sonnet 5.5, 14,000 input tokens (8,000 text + 6 images x 1,000) x $2/1M = $0.028 plus 1,500 output x $10/1M = $0.015 = $0.043, x 1.3 tokenizer overhead = $0.056, plus Haiku 5.5 reason-code classification $0.001, so about $0.06 per dispute. At 0.5 disputes a month = $0.03, plus a monthly proof-gap check over 40 jobs on Haiku 5.5 (40 x $0.00015 = $0.006). Total about $0.04, called $0.05.
- Other variable cost: SMS confirmations 40 jobs x $0.008 = $0.32 [ASSUMPTION, not in LANDSCAPE.md]; hosting $0.50 [ASSUMPTION]; card fees on $26 = 2.9% + $0.30 = $1.05.
- Gross margin: ($26 - 0.05 - 0.32 - 0.50 - 1.05) / $26 = 92.6%, about 93%. The margin is fine; the revenue per customer is the problem.

## 12. Market size
- [ESTIMATE] Reachable service businesses on Stripe or Square based tools with exportable job records: about 500,000 in the US (assumption, UNVERIFIED; validate with Jobber, Housecall Pro, Vagaro and Square seller counts).
- 500,000 x $312 (= $26 x 12) = $156M a year at full share. At 1% penetration = 5,000 merchants = $1.56M ARR. Low frequency and cheap rivals make 1% optimistic.

## 13. Go-to-market
- First 100 customers (concierge style, slow because a dispute must occur): (1) high-intent SEO for the moment of need: "chargeback services not rendered evidence template", "how to win a chargeback for a service business", "Jobber chargeback", "Vagaro chargeback", "Booksy chargeback"; (2) helpful answers in r/sweatystartup and r/smallbusiness and replies to App Store reviews complaining about lost chargebacks (REV-03 and REV-31 types); (3) Stripe and Square app marketplaces ("free until you win").
- Bigger lever with a dependency: pitch field-service and booking platforms to embed it. That needs a partnership, so it cannot be the launch plan.
- Growth loop: weak. Won disputes produce testimonials and shareable templates; nothing compounds by itself.

## 14. Moat and scale path
- Moat candidates: win-rate data per reason code and vertical, job-record connectors, an exhibit library, and "proof at completion" habits that make the packet exist before any dispute.
- Scale path: embed in field-service, booking and ISO or payfac platforms that serve small service merchants, then expand to clinics, tutors and rentals. Standalone, it stays small.

## 15. Solo feasibility
- MVP (6 weeks): Stripe and Square OAuth with dispute webhooks; manual upload and forwarding of evidence; a Jobber read connector; reason-code classifier; argument and exhibit builder; PDF packet; submission through the dispute APIs; outcome tracking; completion-confirmation texts.
- Running cost before revenue: about $70/month (hosting $25, database $15, SMS $15, model tests $10, misc $5) [ESTIMATE].
- Hardest risk: access. If Jobber, Vagaro or Booksy run payments as the platform, merchants may be unable to authorize a third party to submit evidence [UNVERIFIED], and job-record APIs vary. Second: accuracy of reason-code arguments and issuer outcomes outside the founder's control.

## 16. Pre-mortem
1. Economics: about $26 a month per merchant means the business only works with embedded distribution or a flat fee merchants will not pay for insurance-like protection.
2. Platform and competition: Stripe Smart Disputes adds service fields, Chargeflow adds a services template, or field-service platforms build it where they hold the payment.
3. Outcomes: many service disputes are fraud or "unrecognized" claims that issuers favor cardholders on, so win rates may be low and the value unproven.

## 17. Cheapest validation test
- Step 1 (1 week, $0): ask 15 service owners in r/sweatystartup, Jobber, Vagaro and Booksy communities how many disputes they had last year, the amounts, and whether they can export the job records. Pass: at least 8 of 15 had two or more disputes or one over $1,000 and can export evidence.
- Step 2 (60 to 90 days, about $50 and 20 hours): build packets by hand with Claude for 10 live disputes on a success-fee basis. Pass: at least 4 of 10 won and at least 5 of 10 owners say they would pay $19/month plus 10%. Fail: fewer than 2 wins or fewer than 3 would pay.

## 18. Open questions
- Recommendation: do not build this standalone. Test the partner route (embedded in a field-service platform) or kill it.
- Can a merchant on a platform-run payments account authorize a third party to submit evidence, and does Stripe Connect allow it?
- What share of service disputes are "service not provided" claims (winnable with job proof) versus fraud claims?
- Does Stripe's Smart Disputes already cover service disputes? Test with a sandbox dispute.
- Would Jobber, Housecall Pro, Vagaro or Booksy pay for an embedded version, and at what price?
