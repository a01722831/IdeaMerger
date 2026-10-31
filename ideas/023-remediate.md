---
id: "023"
slug: remediate
name: Remediate
one_liner: "Self-serve PDF accessibility remediation: upload documents, get tagged PDF/UA files with a validation report, priced per page."
target_user: "Webmasters and compliance leads at small local governments, colleges, nonprofits and publishers with 500+ legacy PDFs and no remediation budget line"
form_factor: "web app"
lens: "Service-to-software"
frontier: false
competition: "CROWDED"
confidence: "MED"
status: "developed"
signals: [SVC-29, SVC-30, SVC-31, SVC-32, SVC-33, UND-04, UND-05, FORCE-21]
scores:
  pain: 4
  evidence: 3
  ai_leverage: 4
  whitespace: 1
  novelty: 1
  why_now: 3
  solo_feasibility: 3
  distribution: 2
  wtp_economics: 3
  scale_defensibility: 1
total: 52.6
price_hypothesis: "$149/month for 300 pages ($0.50/page), $0.60/page overage; optional human QA at $3/page"
model_cost_per_user_month: "$1.80 (300 pages), about $2.80 with OCR and compute"
gross_margin: "95%"
mvp_weeks: 8
deep_dive: false
red_team: false
---

# Remediate

## 1. One-liner
Self-serve PDF accessibility remediation: upload documents, get tagged PDF/UA files with a validation report, priced per page.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 4 | Buyers already pay $4 or more per page (SVC-29), one state legislature budgeted $931K for it (SVC-30), and public-sector deadlines are fixed (FORCE-21). |
| Evidence quality | 2 | 3 | Prices and a budget line exist, but SVC-30 and SVC-31 are old and the demand signals are few: one buyer evaluating AI add-ons (SVC-33), two blind users (UND-04, UND-05). |
| AI leverage | 2 | 4 | Reading order, table structure, form labels and alt text need layout vision plus language; validators stay deterministic. |
| Whitespace | 2 | 1 | Allyant/CommonLook, Equidox, Adobe, Grackle, YuJa and an MIT-licensed AWS pipeline already sell or give away AI tagging, some at $0.50/page or $29/month. |
| Novelty of insight | 1 | 1 | "AI makes remediation cents per page" is AWS's own headline (SVC-31). |
| Why now | 1 | 3 | ADA Title II dates (2027-04-26 and 2028-04-26) and the EAA push demand, but rivals shipped AI tagging in 2025. |
| Solo feasibility | 2 | 3 | Parsing, structure-tree writing and veraPDF validation are buildable in about 8 weeks; screen-reader-grade output on complex pages is the risk. |
| Distribution | 2 | 2 | No built-in channel; buyers are institutions, and SEO is held by vendors with analyst-style comparison pages. |
| Willingness to pay and unit economics | 2 | 3 | Clear payer and 95% margin, but the price band is collapsing toward cents and conformance needs paid human QA. |
| Scale and defensibility | 2 | 1 | Adobe's auto-tag API and AWS's open-source pipeline commoditize the core; there is no data or network moat. |
| **Total** | | **52.6** | |

Confidence: MED. FRONTIER: no.

## 3. The problem
- Who: people who publish PDFs they are now legally required to make accessible: small cities, counties and special districts (DOJ ADA Title II dates moved to 2027-04-26 for 50,000+ population and 2028-04-26 for smaller entities, FORCE-21), colleges, nonprofits, and employers whose onboarding packets reach blind hires (UND-04).
- How often: a backlog (hundreds to tens of thousands of pages) plus a trickle of new documents each week.
- What it costs: $4.00 per page and up at a specialist (SVC-29); about $11 per page implied by one legislature's 2023 spend of $931,028 on 84.8K pages (SVC-30, [ESTIMATE], the chart notes its dollars are about 85% of cost); managed vendors quote $7.50 to $11.50 per page (search summary, vendor quote).
- Workaround today: Adobe Acrobat Pro auto-tag then hand fixes, an agency or offshore team, an accessibility platform add-on (SVC-33 shows a buyer weighing an AI "PDF remediation agent" at renewal), or asking each sender to reissue the file (UND-04).

## 4. Evidence
Eight cited signals (full rows in `research/SIGNALS.md`):
- SVC-29 (medium, 2026-10-31 live page): "Document accessibility remediation costs start at $4.00 per page. The price of remediating PDFs, Word documents, PowerPoint presentations, and Excel spreadsheets for WCAG 2.1 AA conformance depends on the document status and project scope." Shows: a live price anchor. https://accessible.org/pricing/
- SVC-30 (medium, 2024-02, old): "Vendor Document Remediation, $931,000, 56%" of a Colorado Legislative Council Staff FY2025 request. Shows: a real government budget line. https://leg.colorado.gov/sites/default/files/images/castle_slide_deck_on_lcs_fy25_budget_request.pdf
- SVC-31 (medium, 2025-04-28, old): AWS says its solution "reduces cost and time from $1-$4 per page and hours per document, to cents per page and seconds to minutes per document". Shows: the incumbent-platform claim that sets the price floor. https://aws.amazon.com/blogs/publicsector/from-inaccessible-to-inclusive-how-the-new-pdf-accessibility-remediation-solution-helps-institutions-compliantly-address-accessibility-requirements
- SVC-32 (medium, 2026-04-23): law-firm alert on the DOJ rule: "Automated remediation tools aren't reliable enough yet" (sentence continues about complex educational and STEM content). Shows: automation alone is not trusted by public entities. https://www.duanemorris.com/alerts/doj_extends_ada_title_ii_digital_accessibility_deadlines_one_year_0426.html
- SVC-33 (medium, 2026-10-18): "Any prospect, cons or neutral observations would be great to hear. Org is considering it for an upcoming renewal." Shows: buyers are evaluating AI remediation agents now, so the category is being sold to them. https://www.reddit.com/r/accessibility/comments/1x93vvw/
- UND-04 (medium, 2026-10-24): "I've been starting several jobs and all (even those at blindness organizations lol) have given me inaccessible onboarding paperwork. they're PDFs without edit boxes." Shows: the recipient-side pain, felt by a user who is not the buyer. https://www.reddit.com/r/Blind/comments/1xdubf3/
- UND-05 (medium, 2026-10-15): "Can we enter signatures on pdf forms either in adobe acrobat reader or using markup in ios? Or do we still need sighted help." Shows: the same problem for signing. https://www.reddit.com/r/Blind/comments/1x6t21a/
- FORCE-21 (weak, 2026-04-20): the Federal Register rule moving the deadlines by one year; the forcing function is delayed, not removed. https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web
- New evidence (not in SIGNALS.md), vendor-authored and not first-person, from a competitor's roundup as returned by a page fetch: Adobe Acrobat Pro "Requires significant manual intervention and accessibility expertise for comprehensive remediation", and axes4 notes "human review still required for reading-order accuracy and alternative-text correctness." https://www.continualengine.com/blog/best-pdf-remediation-tools/ (undated). Shows: even tool vendors say human review stays.

## 5. The product
- Outcome: drop in a PDF, a ZIP, or a link to a document library and get back tagged PDF/UA files plus a per-file report (what changed, what a human should check, validator results) and a dated log for compliance records.
- Core AI loop: input (PDFs, scans, Word and PowerPoint files) -> layout vision and text extraction produce a structure map (headings, lists, tables with header cells, figures, form fields, reading order, artifacts), the model writes alt text and field labels, a PDF library writes the tag tree, veraPDF-style validators check it -> output (remediated PDF, report, list of low-confidence items) -> feedback (reviewer corrections on flagged items feed per-customer templates for recurring documents).
- Interaction model: web upload with a review queue; optional human QA lane; API and a folder or SharePoint connector in phase two.
- Form factor: web app.
- Day in the life: a county webmaster uploads 340 meeting packets on Monday. By Tuesday 290 pass validation, 50 are flagged (complex tables, scanned maps). She approves alt text in a queue for 40 minutes, sends the 50 to the paid QA lane, and downloads the log her attorney asked for.

## 6. Why the LLM is load-bearing
- Tagging is a judgment task: what is a heading, which cells are table headers, what is decoration, in what order should a screen reader read a two-column page with a sidebar. Vision-language models now do this at page level.
- Alt text and form-field labels need meaning, which rules cannot supply.
- Without the model it is a rules-based tagger plus manual editing, which is Acrobat Pro, PDFix or axesPDF today.

## 7. The insight
Remediation is a labor market priced per page, and the model turns the labor into cents. Honest note: AWS published this exact belief in 2025 (SVC-31) and gave away the code, so it is shared knowledge. The only candidate for a private belief is the recipient side: a blind user cannot wait for each sender to reissue a form (UND-04, UND-05), but those users are not buyers.

## 8. Why now, and why this does not exist yet
- Why now: DOJ's WCAG 2.1 AA dates for public entities (2027-04-26 and 2028-04-26), the EAA, and layout-aware models that cost cents per page.
- It exists. See section 10: Adobe, Allyant, Equidox, Grackle, YuJa, AWS and several self-serve tools.
- What may still be open: a recipient-side "make this form fillable now" tool for screen-reader users that employers or state blindness agencies fund, and per-customer template learning for recurring documents. Both are unproven.

## 9. Inspiration and derivation
- Parents: CommonLook/Allyant, Equidox, GrackleDocs, Adobe Auto-Tag API, the AWS open-source pipeline, accessible.org's per-page service.
- Changed: business model (self-serve per-page pricing instead of quotes), distribution (credit-card purchases below procurement thresholds). Both are already used by cheaper rivals (Fruition, PDFAccessibility.ai).

## 10. Competition check
Queries run (2026-10-31):
1. Web: "AI PDF accessibility remediation tool PDF/UA auto-tag Equidox CommonLook Grackle price per page 2026"
2. Product Hunt: "site:producthunt.com PDF accessibility remediation tagging screen reader" (returned no Product Hunt pages)
3. YC: "site:ycombinator.com/companies PDF accessibility document remediation" (returned no YC pages)
4. Platforms: "AWS PDF Accessibility Remediation solution open source Adobe Acrobat auto-tag AI cost per page"
5. Pricing: "Allyant AI-powered PDF remediation software launch pricing Equidox pricing per page self-serve PDFAccessibility.ai Pro $29" and "pdfaccessibility.ai pricing free plan Pro monthly pages PDF/UA remediation AI"
6. Adobe: "Adobe Acrobat accessibility auto-tag AI alt text PDF Accessibility Auto-Tag API Acrobat Studio 2026" (an Adobe blog fetch returned HTTP 503 once; not retried)
Read: a [vendor roundup of 10 PDF remediation tools](https://www.continualengine.com/blog/best-pdf-remediation-tools/) (written by Continual Engine, which sells PREP, so rankings are not independent).

Findings:
- [Adobe Acrobat Pro and the Auto-Tag API](https://developer.adobe.com/document-services/apis/pdf-accessibility-auto-tag/): cloud-based AI auto-tagging built on Adobe Sensei, an accessibility checker aligned to WCAG and PDF/UA, and an API for backlogs. An [AbilityNet evaluation](https://abilitynet.org.uk/news-blogs/evaluating-adobes-new-cloud-based-auto-tagging-feature-pdf-accessibility) (search summary, undated) found alt text is not added automatically.
- [AWS open-source solution](https://aws.amazon.com/blogs/publicsector/from-inaccessible-to-inclusive-how-the-new-pdf-accessibility-remediation-solution-helps-institutions-compliantly-address-accessibility-requirements) (also [Content Accessibility Utility on AWS](https://awslabs.github.io/content-accessibility-utility-on-aws/)): built by the ASU AI Cloud Innovation Center under the MIT License; uses Adobe's Auto-Tag API for tags and Amazon Bedrock for alt text; makers claim "cents per page"; a managed install is sold on AWS Marketplace. Free code removes any pricing power for a thin wrapper.
- [Allyant CommonLook PDF](https://www.businesswire.com/news/home/20250708014451/en/Allyant-Announces-the-Launch-of-its-AI-Powered-PDF-Remediation-Software): AI-powered web version launched 2025-07-08; no published price (contact sales).
- [Equidox](https://equidox.co/blog/smarter-automation-higher-roi-the-future-of-pdf-remediation/): AI-assisted element detection, cloud or on-premises; claims it "Automates up to 90% of manual tagging" (vendor claim as quoted by the roundup); no price found.
- GrackleDocs (Google Workspace add-ons), PDFix, axes4, EqualWeb, ADAPT AI and Continual Engine's PREP (all named in the roundup, claims unverified); [YuJa PDF Remediation Max](https://www.silicon.co.uk/press-release/coastal-carolina-southwestern-law-school-and-other-institutions-streamline-accessibility-workflows-with-yujas-pdf-remediation-max-add-on-to-panorama-accessibility-platform) inside its accessibility platform; [Crawford AccessibilityNow Remediate](https://documentmedia.com/article-3145-Crawford-Technologies-Releases-AccessibilityNowreg-Remediate.html); [Nutrient accessibility API](https://www.nutrient.io/api/accessibility-api/) (quota-billed, says auto-tagging does not guarantee PDF/UA).
- Cheap self-serve: [Fruition](https://www.fruition.net/ai-platforms/pdf-accessibility) lists a $0.50/page basic AI tier with 10 free pages a month (and $2 per page elsewhere on the page; search summary); [PDFAccessibility.ai](https://www.itechguides.com/products/pdfaccessibility-ai/pricing/) is freemium, from $29/month per a review site (price checked there 2026-09-20; not confirmed on the vendor's page).
- Service anchors: [accessible.org](https://accessible.org/pricing/) from $4.00 per page (SVC-29).

Classification: CROWDED. Several funded or platform-backed direct competitors, an MIT-licensed reference pipeline, and self-serve rivals at $0.50 per page or $29 a month.

Platform risk: high. Adobe already ships auto-tagging in Acrobat and as an API, and AWS gives away a Bedrock pipeline. Microsoft and Google can improve accessible export from Word and Docs, and a general assistant that writes a PDF script can close easy cases [UNVERIFIED]. This caps Whitespace at 1 and Scale at 1.

## 11. Business model
- Payer: the organization's webmaster or compliance lead, on a card.
- Price hypothesis: $149/month for 300 pages ($0.50/page), overage $0.60/page; human QA add-on $3/page. Anchors: $4.00+ per page specialist (SVC-29), $7.50 to $11.50 managed, Fruition $0.50, PDFAccessibility.ai from $29/month. The price matches the cheapest rivals; there is no price edge.
- Model cost per page [ESTIMATE] (Haiku 5.5 $0.10 in / $0.50 out; Sonnet 5.5 $2.00 / $10.00; Haiku batch $0.05 / $0.25; from `research/LANDSCAPE.md` section 6):
  - Standard page on Haiku 5.5 (85% of pages): 3,000 in + 1,500 out = 3,000 x $0.10/1M + 1,500 x $0.50/1M = $0.0003 + $0.00075 = $0.00105.
  - Complex page on Sonnet 5.5 (15%): 4,000 in + 2,500 out = $0.008 + $0.025 = $0.033.
  - Blend: 0.85 x $0.00105 + 0.15 x $0.033 = $0.00089 + $0.00495 = $0.00584.
  - Verification on Haiku batch, 2,000 in + 300 out = $0.0001 + $0.000075 = $0.000175. Model total about $0.006 per page.
- Per active customer at 300 pages a month: model 300 x $0.006 = $1.80; OCR for 30% scanned pages, 90 x $4/1,000 = $0.36 (OCR price UNVERIFIED in LANDSCAPE.md); compute and storage about $0.60 [ASSUMPTION]. Variable total $2.76, before card fees of 2.9% + $0.30 = $4.62.
- Gross margin: ($149 - $2.76 - $4.62) / $149 = 95.0%. Human QA at $3/page with a $1.00 reviewer cost (3 minutes at $20/hour, [ASSUMPTION]) gives 67% on that add-on.

## 12. Market size
- Bottom-up [ESTIMATE]: assume 20,000 US small local governments, special districts and similar entities with a web PDF library of 500+ files [ASSUMPTION, no verified count]; 20% buy a tool or service before the 2028-04-26 deadline = 4,000 organizations x $149 x 12 = $7.2M a year.
- Add colleges, nonprofits and publishers: assume the same again = $14M a year serviceable.
- Realistic solo share: 3% of 4,000 = 120 organizations x $1,788 = $0.21M ARR from this segment; reaching $1M ARR needs about 560 customers at this price.

## 13. Go-to-market
- First 100 customers: (1) 40 from a free PDF/UA checker and cost-per-page comparison pages ranking for "PDF remediation cost per page", "make PDF accessible", "ADA Title II PDF deadline"; (2) 30 from helpful answers (no cold outreach) in r/accessibility, r/sysadmin and municipal clerk and webmaster groups where SVC-33 style threads appear; (3) 30 from university and K-12 accessibility coordinators and employer HR teams (the UND-04 angle).
- Timing: fiscal-year budget cycles and the 2027-04-26 deadline.
- Growth loop: each remediated file carries a "remediated with" metadata line and a public verification link; weak.

## 14. Moat and scale path
- Weak. Candidates: per-customer templates for recurring document types (agendas, forms, reports) that cut review time; a labeled corpus of reviewer corrections; a trusted human QA lane.
- Scale path: documents beyond PDFs (Word, PowerPoint, email templates), then ongoing monitoring of a site's document library.

## 15. Solo feasibility
- MVP (8 weeks): upload and queue; text and layout extraction; VLM structure map; tag-tree writer; alt text and form-label review queue; veraPDF validation and a plain-language report; Stripe; a manual QA lane with 2 contract reviewers.
- Running cost before revenue: about $110/month (hosting and workers $40, storage $15, model and OCR tests $35, domain and email $10, reviewer test hours $10) [ESTIMATE].
- Hardest technical risk: output that passes validators but fails a real screen-reader test (reading order, nested tables, forms). Machine-checkable rules cover only part of the standard, so human review stays in the loop, and any "compliant" promise creates liability.

## 16. Pre-mortem
1. Commoditized: Adobe's API and AWS's free pipeline set the price near zero, and cheaper rivals already sit at $0.50 per page or $29 a month.
2. Quality gap: complex PDFs need human QA that costs about as much as the old workflow, which kills the margin story and the speed promise.
3. Slow, procurement-shaped buyers: public entities buy from known vendors and delay; the small ones that can use a card are few and hard to reach.

## 17. Cheapest validation test
- Take 30 real inaccessible PDFs from public council or college sites (public pages only), run the pipeline, validate with veraPDF, and have a screen-reader user or a contract tester review 10 of them.
- Cost: about $60 of model spend and OCR plus $100 for tester time; duration 3 weeks.
- Pass: at least 80% of pages pass PDF/UA validation unaided, at least 7 of 10 reviewed files are usable in a screen reader without manual repair, and at least 3 of 10 small organizations that see the results say they would pay $149 a month. Fail: below 60% machine-valid pages or no one willing to pay above $29.

## 18. Open questions
- Recommendation: kill the general product. If anything is pursued, test only the recipient-side or employer-onboarding wedge (UND-04) as a feature of a larger accessibility offering.
- Who funds the recipient-side tool: employers, state blindness agencies, or no one?
- What is the real cost per page for Adobe's Auto-Tag API at volume, and what does the AWS pipeline cost in practice (not visible here)?
- Does a PDF that passes veraPDF and axesPDF checks satisfy what auditors actually test?
