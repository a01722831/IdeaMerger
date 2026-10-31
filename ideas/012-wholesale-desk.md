---
id: "012"
slug: wholesale-desk
name: Wholesale Desk
one_liner: "Turns wholesale purchase orders arriving by email, PDF or chat into checked Shopify draft orders and net-terms invoices."
target_user: "Small Shopify brands with 5 to 50 wholesale accounts that order by email, PDF or chat on net terms"
form_factor: "plugin"
lens: "Pain-first"
frontier: false
competition: "CROWDED"
confidence: "LOW"
status: "developed"
signals: [RED-19, RED-20, RED-06, RED-18]
scores:
  pain: 2
  evidence: 2
  ai_leverage: 4
  whitespace: 1
  novelty: 1
  why_now: 3
  solo_feasibility: 4
  distribution: 3
  wtp_economics: 3
  scale_defensibility: 1
total: 48.4
price_hypothesis: "$49/month per store, free tier at 5 POs a month (market: free to $99)"
model_cost_per_user_month: "$0.40"
gross_margin: "83%"
mvp_weeks: 5
deep_dive: false
red_team: false
---

# Wholesale Desk

## 1. One-liner
Turns wholesale purchase orders arriving by email, PDF or chat into checked Shopify draft orders and net-terms invoices.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 2 | About 7 hours a month of re-keying for a brand with 40 wholesale orders [ESTIMATE]; real but small, and no one in the signals says they pay to fix it. |
| Evidence quality | 2 | 2 | Only RED-19 (medium, partly vendor voice) and RED-20 (weak) match the exact job; RED-18 and RED-06 are adjacent jobs. |
| AI leverage | 2 | 4 | Free-form orders and fuzzy SKU matching are model work; without it you need a template per buyer. |
| Whitespace | 2 | 1 | At least eight PO-to-draft-order apps on the Shopify App Store (NoRetype was listed 2026-10-06), plus funded order-entry agents one segment up. |
| Novelty of insight | 1 | 1 | "Buyers will not use a portal, translate their orders" is exactly what every competing app already does. |
| Why now | 1 | 3 | Cheap vision and long-context models make PDF-to-lines nearly free; the crowd of entrants proves timing but not a moat. |
| Solo feasibility | 2 | 4 | A five-week build on the Admin GraphQL API; the simplicity is why so many apps already do it. |
| Distribution | 2 | 3 | The Shopify App Store is a built-in channel, but it is saturated and reviews are the scarce asset. |
| Willingness to pay and unit economics | 2 | 3 | Margin is very high, but the market price floor is $0 to $39 and at least four rivals have free tiers. |
| Scale and defensibility | 2 | 1 | Feature-sized: Shopify (draft orders, B2B, Sidekick) can absorb it and many clones already exist. |
| **Total** | | **48.4** | |

Confidence: LOW. FRONTIER: no.

## 3. The problem
- Who: a small Shopify brand selling to boutiques, cafes or retailers on net terms. Buyers will not use a portal and send POs by email, PDF, spreadsheet or text.
- How often: every order from every wholesale account, plus reorders. A brand with 40 wholesale orders a month at about 10 minutes each (re-key, check stock, invoice with terms) loses about 7 hours a month [ESTIMATE: 40 x 10 min = 400 min].
- What goes wrong: SKU, price-tier or terms errors, late invoices, and tracking "who owes what and when" outside the store. It "works at five customers" and breaks at twenty (RED-19).
- Supplier side: POs and proforma invoices live in email and spreadsheets, and the time goes into receiving and price changes (RED-20, RED-18).
- Workarounds today: spreadsheets and email threads, draft orders typed by hand, wholesale portals, and a wave of PO-to-draft-order apps (section 10).

## 4. Evidence
Only two of the four seed signals match the exact job; the other two are adjacent (full rows in `research/SIGNALS.md`):
- RED-19 (medium, 2026-10-30): "A trade customer wants to pay by purchase order on net terms, and suddenly you're outside your store platform entirely, manually tracking who owes what and when." Shows: net-terms POs fall out of the store platform into email and a sheet. The poster consults for such stores, so this is partly vendor voice. https://www.reddit.com/r/smallbusiness/comments/1xj7o0i/
- RED-20 (weak, 2026-07-21): "Raising a PO isn't what takes time. Receiving is." Shows: supplier POs and replies live outside Shopify and receiving is the time sink; the thread is dominated by app builders. https://community.shopify.com/t/how-are-you-currently-managing-purchase-orders-and-supplier-inventory-in-shopify/636598
- RED-18 (strong, 2026-10-30): "We sell a lot of multiple SKUs in fitness categories and reorder every month. It’s a nightmare to manage all the documentation PI PR POs etc." Shows: monthly import reorders drown in proforma and PO paperwork. Supplier side, a different job from buyer POs. https://www.reddit.com/r/smallbusiness/comments/1xj87nb/
- RED-06 (medium, 2025-07-31): "We can't afford $100/mo for what we need and we don't need to track across multiple sales platforms, reorder inventory, etc. Just match up one item in and its COG with the eventual removal of that item from the inventory and the sale price." Shows: price sensitivity ("can't afford $100/mo") and hand-made invoices for a consignment seller; not a Shopify wholesale case. https://www.reddit.com/r/smallbusiness/comments/1mecoxb/
- New evidence (not in SIGNALS.md), r/shopify, 2026-10-22 (title only): "Alternatives or options for adding wholesale pricing to the store without an app or additional subscription?" Shows: resistance to paying for another app. https://www.reddit.com/r/shopify/comments/1xcmvwo/
- New evidence (not in SIGNALS.md), r/shopify, 2026-10-27 (title only): "Shopify B2B has no recurring orders. How are you handling wholesale accounts that order the same thing every month?" Shows: Shopify's B2B gaps remain at the reorder step. https://www.reddit.com/r/shopify/comments/1xgr0s9/

## 5. The product
- Outcome: forward or drop any wholesale order and get a checked Shopify draft order at the buyer's price tier with net terms, a confirmation to the buyer, and a stock warning before anything is promised.
- Core AI loop: input (email body, PDF, spreadsheet, photo or chat text, plus the catalog and each buyer's price list and terms) -> the model extracts lines, maps buyer wording and old SKUs to catalog variants with a confidence score, and spots missing facts (ship date, terms) -> output: draft order via the Admin GraphQL API, invoice with terms, buyer confirmation draft, exceptions list -> feedback: every fix is stored as a per-buyer alias ("Lav 8oz" = SKU LAV8OZ) and reused next time.
- Supplier side: upload a proforma or PO, then delivery notes; the model reconciles quantity, price changes and short ships and flags differences.
- Interaction model: a per-store inbox address and a review queue inside the Shopify admin; auto-create only above a confidence threshold.
- Form factor: embedded Shopify app (plugin).
- Day in the life: a candle brand gets a 3-page PDF from a boutique chain. The app drafts a 22-line order, flags two lines it could not match and one SKU short of stock. The owner fixes two lines, taps approve, and the buyer receives a confirmation with Net 30 terms.

## 6. Why the LLM is load-bearing
- Buyer POs arrive as free-form text, scans and photos with the buyer's own item names; template parsers need a setup per buyer.
- Fuzzy matching with clarifying questions ("the 8oz or the 16oz?") is model work.
- Without the model this is a template-based email parser, which still needs a template per buyer.

## 7. The insight
Wholesale buyers will not use a portal, so the product is the translation layer from messy orders to clean draft orders. Honest note: that belief is no longer unusual; at least eight apps now act on it.

## 8. Why now, and why this does not exist yet
- It does exist. NoRetype was listed on 2026-10-06; Orderseam, FolioPO, POinbox, POdraft, DraftFlow, AutoApprove, PasteOrder and LevelOps are also on the Shopify App Store. YC companies (Comena, Seals AI, Ventura, Stockline, Burnt) sell order-entry agents to larger distributors.
- Why now: cheap vision and long-context models make PDF-to-lines extraction nearly free, and many entrants are arriving at once.
- What may still be missing: the supplier-side half (proforma vs PO vs receipt) and recurring-order handling, where the evidence is thin (RED-18, RED-20, one r/shopify title).

## 9. Inspiration and derivation
- Parents: Comena and WizCommerce's Ella (AI order entry for distributors), Shopify PO-to-draft-order apps, Shopify B2B draft orders.
- Changed: target user (DTC brands with wholesale accounts, not distributors with ERPs), business model (flat low price, no implementation), channel (Shopify App Store). The core job and interaction model match the competitors', which is why the idea is not differentiated.

## 10. Competition check
Queries run (2026-10-31):
1. Web: "AI wholesale order entry email PDF purchase order to Shopify draft order"
2. Product Hunt: "site:producthunt.com wholesale orders email PDF purchase order automation Shopify B2B" (one PH page: a buyer-side portal; the rest were Shopify listings)
3. YC: "site:ycombinator.com/companies purchase orders email order entry AI distributors wholesalers"
4. Shopify App Store: "apps.shopify.com wholesale purchase order PDF import draft orders net terms app", plus a read of the NoRetype page
5. Platform: "Shopify Sidekick draft orders B2B wholesale purchase order AI Editions 2026"; also a Reddit archive scan of r/shopify, r/ecommerce and r/smallbusiness since 2026-07-01.

Findings (all vendor claims; NoRetype, Orderseam, FolioPO and AutoApprove showed 0 reviews on the page or in the search summary, review counts for the rest were not checked):
- [NoRetype](https://apps.shopify.com/noretype): listed 2026-10-06; Free (5 emailed POs a month), $39, $99, $199; PDF, Excel, CSV or photo POs; net terms; 0 reviews.
- [Orderseam](https://apps.shopify.com/orderseam): from $49/month; PDF, Excel, Word, CSV, email and phone-photo POs; flags unclear lines; Net-terms invoices with reminders.
- [FolioPO](https://apps.shopify.com/foliopo): from $39/month (30 drafts per 30 days on the lower tier), $129 for the higher tier.
- [AutoApprove](https://apps.shopify.com/autoapprove) (free plan, approval gate), [POdraft](https://apps.shopify.com/podraft) (forwarding address), [POinbox](https://apps.shopify.com/poinbox-pdf-to-order) (PDF, email, Excel, CSV, Word), [DraftFlow](https://apps.shopify.com/draftflow) (free plan), [PasteOrder](https://apps.shopify.com/pasteorder-1), LevelOps B2B PDF-to-Order (from $3 per order, per community posts), [The Usual](https://pickyourapp.com/products/the-usual) (free tier capped at 5 emailed POs a month).
- [ECOSIRE AI OCR Order and Invoice Capture](https://ecosire.com/apps/shopify/ai-ocr-order-invoice-capture): build-to-order from $249.
- Opposite bet: [B2B Quick Order](https://www.producthunt.com/products/b2b-quick-order) (Product Hunt) has buyers upload spreadsheets to a cart.
- Funded order-entry agents one segment up: [Comena](https://www.ycombinator.com/companies/comena) (YC S25), [Seals AI](https://www.ycombinator.com/launches/LqH-seals-ai-ai-employees-for-wholesalers-distributors), [Ventura](https://www.ycombinator.com/companies/ventura), [Stockline](https://www.ycombinator.com/launches/O2j-stockline-ai-native-erp-for-food-wholesalers) (orders from WhatsApp, SMS, email, calls), [Burnt](https://www.ycombinator.com/launches/OBd-burnt-agentic-os-for-food-supply-chain), and WizCommerce's [Ella](https://distributionstrategy.com/2026/06/wizcommerce-launches-ai-order-entry-tool-for-distributors/). They target distributors and ERPs and could move down-market.
- [Shopify Sidekick](https://sagnikbhattacharya.com/blog/shopify-sidekick-store-tasks): a third-party blog shows a prompt that creates a draft order at the wholesale price (not Shopify documentation).

Classification: CROWDED. Not by popularity (the four listings I could check have no reviews) but by count: at least eight direct apps priced $0 to $99, plus funded agents one segment up, and all share the key insight.

Platform risk: high. Shopify is the vertical incumbent and already has draft orders, B2B company pricing and Sidekick; reading an emailed PO is a small step. Any assistant with Gmail and Shopify access can do a one-off conversion. A native Shopify version within 12 months is likely, which caps Scale at 1 and Whitespace at 1.

## 11. Business model
- Payer: the Shopify merchant, billed monthly through Shopify.
- Price hypothesis: $49/month per store with a free tier of 5 POs a month to match the market. The market cluster is free to $99 (NoRetype, Orderseam, FolioPO, DraftFlow), so $49 is mid-market, not a discount.
- Model cost per store per month [ESTIMATE] (40 orders, 25 lines each, 10% messy; prices from `research/LANDSCAPE.md` section 6):
  - Extraction on Haiku 5.5: (3,500 fresh in x $0.10 + 2,000 cached x $0.01 + 1,000 out x $0.50) / 1M = $0.00087, x 1.3 tokenizer overhead = $0.0011, x 40 orders = $0.045.
  - Line disambiguation: 25% of 1,000 lines = 250 calls x (1,000 in x $0.10 + 100 out x $0.50) / 1M = $0.04.
  - 10% of orders (4) escalated to Sonnet 5.5: (6,000 x $2 + 800 x $10) / 1M = $0.02 x 4 = $0.08.
  - Buyer confirmations 40 x $0.0003 = $0.012; supplier reconciliation 8 documents x (5,000 x $2 + 700 x $10) / 1M = $0.017 x 8 = $0.136.
  - OCR for scanned PDFs: 20% of 40 orders x 2 pages x $4/1,000 pages = $0.064 (OCR price UNVERIFIED in LANDSCAPE.md).
  - Total about $0.38, called $0.40.
- Other variable cost: inbound email and hosting about $0.60 [ASSUMPTION].
- Gross margin: ($49 - 0.40 - 0.60) / $49 = 98% before store fees. With a 15% Shopify revenue share [UNVERIFIED rate]: ($41.65 - 1.00) / $49 = 83%, the figure in the front matter.

## 12. Market size
- [ESTIMATE] Shopify stores selling wholesale by email or PO: about 200,000 (assumption: around 4 million active stores x 5%; both inputs UNVERIFIED).
- 200,000 x $49 x 12 = $117.6M a year at full share. In a market with eight or more apps and a free tier, a realistic share is 0.5% = 1,000 stores = $0.59M ARR.

## 13. Go-to-market
- Channel: Shopify App Store search ("purchase order", "wholesale", "PDF to draft order"), r/shopify and Shopify Community threads where merchants ask for this, and Shopify partner agencies that set up B2B.
- First 100 customers: hard. The rivals split the same searches and the four I checked have no reviews yet, so early reviews are the scarce asset. Path: concierge conversions for 30 brands found in Shopify Community threads and r/shopify, ask each for a review, then price in the market middle.
- Growth loop: buyer confirmations and invoices carry a small "processed with" link. Weak.

## 14. Moat and scale path
- Thin. Per-buyer alias memory and supplier-side reconciliation are the only compounding assets; nothing stops a clone.
- Scale path if kept: supplier-side receiving (RED-20) and QuickBooks sync for importers, or fold this into 029 Forward-to-Post as a Shopify target.

## 15. Solo feasibility
- MVP (5 weeks): inbound email address, PDF, Excel and photo extraction, catalog sync and fuzzy matching, review queue, draft-order creation through the Admin GraphQL API, net-terms flag, confirmation email. Supplier-side reconciliation after launch.
- Running cost before revenue: about $60/month (hosting $25, database $15, model tests $10, email $10) [ESTIMATE].
- Hardest technical risk: SKU-matching accuracy on messy buyer wording, plus Shopify app review time. The code itself is simple, which is why so many apps already do it.

## 16. Pre-mortem
1. Crowded and cheap: at least eight apps, several with free tiers or $3 per order; there is no price to charge and no review lead.
2. Shopify ships it natively or Sidekick learns to handle PO attachments; the app becomes a feature.
3. Thin demand: brands with fewer than 10 wholesale orders a month will not pay, and brands with 50 or more move to an ERP or a B2B platform.

## 17. Cheapest validation test
- Free watch test (60 days, $0): record review counts, ratings and prices for the eight apps now and again on 2026-12-31. Kill if none has 10 or more reviews or if two more move to free plans, which would mean little willingness to pay.
- Concierge test (3 weeks, about $20): convert the last 10 wholesale orders for each of 10 brands with a script and Claude. Pass: median time saved at least 6 minutes per order and at least 5 of 10 brands with 20+ orders a month agree to $49/month. Fail: fewer than 3.

## 18. Open questions
- Recommendation: kill the buyer-PO half (CROWDED). Re-test the supplier-side half only if 10 importers confirm monthly proforma, PO and receiving pain (current evidence is RED-18 and RED-20 only), or fold it into 029.
- Do any of the new apps reach 10 or more reviews by year end?
- Is Shopify planning native PO attachment handling in Sidekick or Flow?
- Does the unserved slice (recurring orders for reorder accounts) justify its own app?
