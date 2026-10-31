---
id: "026"
slug: ai-governance-kit
name: AI Governance Kit
one_liner: "A safe-yes AI gateway that MSPs resell per seat: redaction, logging, policy prompts and AI-literacy records for small companies."
target_user: "MSPs serving 10-200 person companies whose staff already paste company data into personal AI accounts"
form_factor: "browser extension"
lens: "Second-order AI"
frontier: false
competition: "CROWDED"
confidence: "MED"
status: "killed"
signals: [AI2-27, AI2-55, AI2-56, AI2-57, AI2-58, AI2-59, RED-36]
scores:
  pain: 3
  evidence: 3
  ai_leverage: 2
  whitespace: 1
  novelty: 1
  why_now: 4
  solo_feasibility: 2
  distribution: 2
  wtp_economics: 3
  scale_defensibility: 2
total: 46.3
price_hypothesis: "$3 per seat per month wholesale to MSPs (MSP resells at about $8)"
model_cost_per_user_month: "$0.10 per seat"
gross_margin: "97% on model cost, about 80% with assumed support"
mvp_weeks: 8
deep_dive: false
red_team: false
---

# AI Governance Kit

> **Main-thread review, 2026-10-31: KILLED.** CROWDED. DefensX, Portal26 and Pax8's own AI gateway already sell AI governance to MSPs; only an AI-literacy records add-on is left, which is a feature. The file is kept as a record of the competition check.

## 1. One-liner
A safe-yes AI gateway that MSPs resell per seat: redaction, logging, policy prompts and AI-literacy records for small companies.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Daily exposure for every small firm and a career risk for IT admins, but the loss is potential rather than felt, and owners accept the risk. |
| Evidence quality | 2 | 3 | Seven signals; one strong (506 pts / 448 comments), four weak or vendor-disclosed; no one states a price they would pay. |
| AI leverage | 2 | 2 | Redaction, logging and policy enforcement are mostly rules; the model helps classify prompts and write training. AI is a feature here. |
| Whitespace | 2 | 1 | DefensX, Portal26, Pax8's own gateway, Microsoft Purview, Strac, LayerX and a long tail of Product Hunt launches already sell this to MSPs. |
| Novelty of insight | 1 | 1 | "Safe yes through the MSP channel" is exactly what the incumbents say in 2026. |
| Why now | 1 | 4 | Shadow AI, executive agent demands and the EU AI-literacy duty (reworded by the Digital Omnibus that entered into force 2026-07-27) all landed in the last 12 months. |
| Solo feasibility | 2 | 2 | An extension, proxy, multi-tenant console and PSA links is 8+ weeks, and a security product needs trust and assurance a solo founder lacks. |
| Distribution | 2 | 2 | The MSP channel is real but crowded with vendors; Pax8 and similar marketplaces gate listing. |
| Willingness to pay and unit economics | 2 | 3 | MSPs buy per-seat security and mark it up; model cost is tiny; the price anchor is unverified. |
| Scale and defensibility | 2 | 2 | Microsoft, Pax8 and funded MSP-specific vendors cap it at 2; MSP switching costs are the only lock-in. |
| **Total** | | **46.3** | |

Confidence: MED. FRONTIER: no. Honest read: CROWDED; section 18 recommends against the full kit.

## 3. The problem
- Who: IT admins and MSPs for 10 to 200 person companies; executives and staff who want AI with full data access.
- Cost: the admin may be blamed for a leak they warned about (AI2-27); policy cannot be enforced when owners accept the risk (AI2-55); auditors are said to ask for logs of what data went to which model (AI2-57); the EU AI Act asks for staff AI-literacy measures (AI2-59).
- Workarounds: a written AI policy, blocking sites, buying an enterprise chatbot plan for a few, Microsoft Purview where licensed, or nothing.
- Gap claimed: a cheap, MSP-deployable layer that says yes safely. The research below shows that several vendors already claim exactly this gap.

## 4. Evidence
- **AI2-27** (strong, 2026-10-30, r/sysadmin, 506 pts / 448 comments): "My C-Suite staff have finally discovered AI agents, and no matter how much I advise risks, they just continue to push it further. There is a clear disregard for any information/data security, and who am I to tell the CEO not to upload our entire HR database to Grok so he can have a fancy dashboard?" https://www.reddit.com/r/sysadmin/comments/1xjcst2/
- **AI2-55** (medium, 2026-09-28, r/msp): when IT blocks a use, "the user went back to claude with the mandate that it has to make it work without IT input or control." https://www.reddit.com/r/msp/comments/1wspbxd/_/pco583q/
- **AI2-58** (medium, 2025-10-02, HN, quoting the MIT "GenAI Divide" study): "While only 40% of companies say they purchased an official LLM subscription, workers from over 90% of the companies we surveyed reported regular use of personal AI tools for work tasks." https://news.ycombinator.com/item?id=45449942
- **AI2-56** (weak, 2026-10-19, r/msp, commenter discloses building an AI-literacy training tool): "Lots of SMB teams on personal ChatGPT accounts and nobody actually decided anything." https://www.reddit.com/r/msp/comments/1x4v66h/_/php3hjs/
- **AI2-57** (weak, 2026-03-16, HN, likely vendor): "SOC 2 and ISO 27001 auditors are now explicitly asking for evidence of data flow controls around AI integrations." https://news.ycombinator.com/item?id=47394564
- **AI2-59** (weak, 2026-07-27, Lewis Silkin): the Digital Omnibus entered into force; Article 4 "now requires providers and deployers to take measures supporting AI literacy among staff". https://www.lewissilkin.com/insights/2026/07/27/the-digital-omnibus-on-ai-enters-into-force-today-102nedo
- **RED-36** (weak, 2026-05-14, HN): "There is a lot of friction taking AI into use right now for people who aren't developers." https://news.ycombinator.com/item?id=48132789
- New evidence (not in SIGNALS.md), supply-side demand: in a trade article on Portal26's MSP launch, its CEO says inbound demand from smaller businesses "had overwhelmed the direct-sales model" (page shows "Oct 21" without a year; context suggests 2026). https://www.remio.ai/post/portal26-msp-ai-governance-platform-turns-shadow-ai-into-a-revenue-test This confirms the MSP channel but also that a funded rival is in it.

## 5. The product
- What it does: a Chrome and Edge extension pushed by the MSP's RMM or MDM, plus a cloud proxy. Staff use approved chatbots. The extension scans prompts and uploads, redacts personal data and secrets, shows a one-line policy reminder when a rule is hit, and writes an audit log. A monthly per-client report shows who used which tools, what was redacted and what was blocked. Short role-based AI-literacy modules are generated and tracked, with a certificate record per person.
- Core AI loop: prompt or upload -> fast rules plus a small model classify sensitivity -> redact, warn or block -> log -> weekly report -> policy suggestions -> staff training assigned from the hits.
- Interaction model: invisible to staff until a rule triggers; an MSP console across tenants.
- Form factor: browser extension plus multi-tenant web console.
- Day in the life: the owner's assistant pastes a customer list into a free chatbot; the extension redacts emails and phone numbers, shows "customer data is replaced; use the approved account for full data", logs it, and the MSP's monthly review shows the pattern.

## 6. Why the LLM is load-bearing
- Weakly. Pattern rules catch card numbers and keys; a small model helps with names, health facts, contract text and unstructured secrets, and generates role-specific training. Remove the model and the product still works as ordinary DLP, which is what most competitors sell.

## 7. The insight
- Small companies buy security through MSPs, so a safe-yes product that MSPs resell per seat beats selling to each company. Honest limit: every vendor in section 10 reached the same conclusion; there is no non-obvious belief here.

## 8. Why now, and why this does not exist yet
- Why now: agent demands from executives (AI2-27), 90% personal-account use (AI2-58) and the AI-literacy duty (AI2-59) all peaked in 2025 to 2026.
- It already exists: see section 10. DefensX has sold this to MSPs since at least November 2025, Portal26 launched an MSP edition, and Pax8 previewed its own gateway.

## 9. Inspiration and derivation
- Parents: browser DLP (Strac, LayerX, Microsoft Purview browser extension), DefensX and Portal26 for MSPs, security-awareness training platforms.
- Changed: target user (MSP resale to 10 to 200 person firms), core job (safe yes with proof), business model (wholesale per seat). Little is new relative to DefensX.

## 10. Competition check
Queries run:
1. WebSearch: "shadow AI governance small business MSP browser extension PII redaction logging approved ChatGPT usage policy per seat resell"
2. WebSearch (Product Hunt): "site:producthunt.com AI usage control employees ChatGPT data leak prevention browser extension redact sensitive data company"
3. WebSearch (YC directory): "site:ycombinator.com/companies shadow AI security employees ChatGPT data leakage governance AI usage policy enforcement"
4. WebSearch (MSP marketplace): "Pax8 marketplace AI governance shadow AI DLP MSP vendors 2026 Microsoft Purview Copilot readiness small business MSP offering"
5. WebFetch of the Portal26 MSP launch article and of the DefensX Shadow AI page.

| Product | What it does | Price | How it differs |
|---|---|---|---|
| [DefensX Shadow AI Protection for MSPs](https://www.defensx.com/blog/the-ai-revolutions-achilles-heel-browser/) (page dated 2025-11-17) | Browser-native control: monitors AI tools, redacts PII and source code before transmission, monitor/redact/block modes, SSO enforcement, logs mapped to SOC 2, GDPR and NIS 2, just-in-time micro-training | per-user price not stated | This idea, already shipped, aimed at MSPs |
| [Portal26 Managed Intelligence Platform](https://www.remio.ai/post/portal26-msp-ai-governance-platform-turns-shadow-ai-into-a-revenue-test) | Multi-tenant AI governance for MSPs: usage discovery, policy, audit, ROI, with a partner academy | not stated | Enterprise vendor adapting to the MSP channel |
| Pax8 ([AI governance as a managed service](https://www.pax8.com/blog/your-next-offering-ai-governance-as-a-managed-service/), [8os launch, Oct 2026](https://www.channelinsider.com/ai/pax8-8os-8bot-ai-msp-managed-intelligence/)) | The marketplace itself pitches AI governance as recurring revenue, points to Microsoft 365 Copilot with Purview, previewed an Agent Gateway for multi-tenant AI governance and launched 8os | n/a | The channel owner is building the layer |
| [Microsoft Purview browser extension](https://nikkichapple.com/microsoft-purview-browser-extension-protect-ai/), [Strac Browser DLP](https://addons.mozilla.org/addon/strac-browser-dlp/), [LayerX](https://solutionsreview.com/backup-disaster-recovery/layerx-secure-data-usage-of-generative-ai/) | Browser-level AI data controls | n/a | Established DLP vendors |
| Product Hunt: [AI Prompt Guard](https://www.producthunt.com/products/ai-prompt-guard), [Honest AI Shield](https://www.producthunt.com/products/honest-ai-shield), [AI Safeguard](https://www.producthunt.com/posts/ai-safeguard), [Privent](https://www.producthunt.com/p/privent/privent), [NMB Shadow](https://www.producthunt.com/products/nmb-shadow) | Prompt scanning and masking extensions with admin dashboards; few reviews | n/a | A crowded long tail, mostly early |
| YC: Compliant LLM (W23), [PromptArmor](https://ycombinator.com/companies/promptarmor) (W24) | LLM security and compliance (YC pages thin) | n/a | Adjacent, not SMB-MSP focused [UNVERIFIED] |
| [VerifyWise](https://verifywise.ai/shadow-ai-monitor) and AI-literacy training tools (see AI2-56) | Shadow AI monitor; literacy training with records | n/a | Smaller entrants in the training niche |

Classification: **CROWDED**. Several funded or established vendors sell this to MSPs now, and the marketplace operator is building it.

Platform risk: very high. Microsoft bundles Purview controls into its stack, Pax8 builds a gateway for its own partners, and ChatGPT, Claude and Gemini business plans add admin controls and logs. Per the rubric this caps Scale and defensibility at 2 and Whitespace at 3; the number of direct vendors puts Whitespace at 1.

## 11. Business model
- Payer: the MSP, billed per protected seat (the client pays the MSP). Price: $3 per seat wholesale (minimum 25 seats), MSP resells at about $8 [ASSUMPTION; no vendor price was visible]. AI-literacy records as a $1 add-on.
- Model cost per seat per month [ESTIMATE]: 440 prompts (20 a day x 22 days); classification on Haiku 5.5 of the 30% of prompts that rules cannot decide: 132 x (800 in x $0.10/1M + 100 out x $0.50/1M = $0.00013) = $0.017; monthly report and policy suggestions per seat share about $0.01; training generation amortized about $0.01; log storage under $0.01 [ASSUMPTION]. Total about $0.05 to $0.10 per seat.
- Gross margin [ESTIMATE]: ($3 - $0.10) / $3 = 97% on model and storage alone; with support, security tooling and invoicing at an assumed $0.50 per seat, about 80%. The real costs are support and assurance, not tokens.

## 12. Market size
- Buyers [ESTIMATE]: assume 20,000 US MSPs actively reselling security [ASSUMPTION; count not verified]. At 3% adoption of a newcomer (600 MSPs) with 300 protected seats each, at $3 x 12 = $36 a seat per year: 600 x 300 x $36 = $6.5M ARR. Everyone buying: 20,000 x 300 x $36 = $216M.
- Reading: a real market, and exactly why funded vendors are in it; a 3% share is optimistic for a solo entrant.

## 13. Go-to-market
- First 100 customers (MSPs): (1) r/msp threads like AI2-55 and AI2-56, where MSPs ask how to enforce AI policy, offering a free "AI exposure scan" of a client's browsers and a policy template, about 30 MSPs; (2) MSP-focused channels such as Pax8's marketplace (listing requires onboarding [ASSUMPTION]); (3) SEO on "AI acceptable use policy template" and "EU AI Act Article 4 AI literacy training record", about 40 leads; (4) guest posts for MSP newsletters.
- Growth loop: the monthly client report is branded for the MSP's quarterly business review, which sells more seats and referrals; no consumer loop.

## 14. Moat and scale path
- Moat: per-industry redaction rules, PSA and RMM integrations, audit evidence history per tenant. All replicable by DefensX or Portal26.
- Scale path: compliance packs (HIPAA, SOC 2 evidence), agent permissions review, then a direct-to-SMB channel.

## 15. Solo feasibility
- MVP (8 weeks): Chrome and Edge extension with local redaction for a few categories, a thin proxy, audit log, multi-tenant console, monthly PDF report, AI-literacy module generator. No PSA integrations.
- Running cost before revenue: about $60 to $150 a month (hosting, storage, a few pilot seats).
- Hardest risks: browser extension permissions and store review, false positives breaking staff workflows, being trusted with prompts that hold client data, and security questionnaires from MSPs.

## 16. Pre-mortem
1. MSPs already have DefensX, Purview or a Pax8 bundle, and a new vendor has no reason to be added to their stack.
2. A redaction miss or an outage causes a leak or breaks workflows, and a solo vendor cannot carry the liability.
3. Chatbot vendors add admin controls and logs, making the extension unnecessary for most small firms.

## 17. Cheapest validation test
- What: before building anything, offer a free "AI exposure review" (a spreadsheet and a 30-minute call) to 15 MSPs found in MSP communities, and ask them to name their current tool and what they pay per seat; then show a mock monthly report and ask for a $3 per seat letter of intent.
- Cost: $0 apart from time. Duration: 3 weeks.
- Pass: at least 8 of 15 MSPs have no per-seat AI control today, and at least 3 sign a non-binding intent for 100 or more seats at $3. Fail: most already use an incumbent, or fewer than 2 will commit.

## 18. Open questions
- Recommendation: do not build the full kit; it is CROWDED and the channel owner is building it. The only evidence-linked niche is AI-literacy training plus a per-person record for EU AI Act Article 4 (AI2-56, AI2-59): no extension, no proxy, solo-feasible in 4 weeks, but it is a low-price compliance checkbox. Test it with MSPs in the section 17 call, otherwise kill.
- What do MSPs pay per seat for DefensX or similar tools today? No price was visible.
- Do MSP buyers want a separate vendor, or will they take whatever Pax8 bundles?
- Does the EU duty (Article 4) create purchases from US MSP clients, or only EU ones?
