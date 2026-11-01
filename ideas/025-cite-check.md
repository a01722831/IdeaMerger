---
id: "025"
slug: cite-check
name: Cite Check
one_liner: "Upload a manuscript or brief and get a reviewer report on which citations are fake or fail to support claims."
target_user: "Peer reviewers, journal and conference editors, grant reviewers, and litigators or clerks reading AI-assisted submissions"
form_factor: "web app"
lens: "Second-order AI"
frontier: false
competition: "CROWDED"
confidence: "MED"
status: "killed"
signals: [PRO-238, AI2-07, AI2-12, AI2-13, AI2-17]
scores:
  pain: 3
  evidence: 3
  ai_leverage: 4
  whitespace: 1
  novelty: 3
  why_now: 4
  solo_feasibility: 3
  distribution: 2
  wtp_economics: 1
  scale_defensibility: 2
total: 50.5
price_hypothesis: "$12 per document report, $39/month for 5; journal or conference plan about $499/year"
model_cost_per_user_month: "$2 (5 documents)"
gross_margin: "91%"
mvp_weeks: 7
deep_dive: true
red_team: true
---

# Cite Check

> **Main-thread review, 2026-11-01: KILLED after red team.** CROWDED: free citation lookups (CourtListener, CaseRead, CiteAudit), Westlaw Quick Check Judicial, Clearbrief, LawDroid CiteCheck, scite and Grounded AI cover existence and claim checks, and the people in pain (reviewers, clerks) do not pay. The file, deep dive and red team are kept as a record.

## 1. One-liner
Upload a manuscript or brief and get a reviewer report on which citations are fake or fail to support claims.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Real and rising (28% of one conference track flagged as AI-written; 2,246 court matters), but a reviewer meets it a few times a year. |
| Evidence quality | 2 | 3 | Five signals, three strong, all about the verification burden; none states willingness to pay, and the reviewer is unpaid. |
| AI leverage | 2 | 4 | Judging whether a cited passage supports a specific claim is reading work a model now does; retrieval and human review remain. |
| Whitespace | 2 | 1 | Grounded AI (publisher channel, Nature analysis), scite Reference Check, Manusights, CiteAudit and legal cite-checkers (Clearbrief, CiteSentinel) all do parts of it. Red team: 2 to 1, red team: ten or more named tools including Westlaw Quick Check, Clearbrief and free CourtListener lookups |
| Novelty of insight | 1 | 3 | A reader-side framing (the person who bears the cost of verifying) is a useful twist on author-side checkers. |
| Why now | 1 | 4 | AI-fabricated references went from curiosity to a flood in 2025 to 2026, and long context makes claim-by-claim reading cheap. |
| Solo feasibility | 2 | 3 | Reference resolution is easy; getting full text of cited sources (paywalls) is the hard part, so coverage is partial. |
| Distribution | 2 | 2 | Free author-side check can bring traffic, but reviewers and clerks have no budget and journals, courts and firms buy slowly. |
| Willingness to pay and unit economics | 2 | 1 | Cost per report is about $0.40 and margin is high, but the people in pain are unpaid; paying buyers are publishers and law firms who have incumbents. Red team: 2 to 1, red team: readers are unpaid, lawyers have bundled tools, publishers build in-house |
| Scale and defensibility | 2 | 2 | Labs' research agents and publisher integrity suites can add a "check the references" step; no data moat. |
| **Total** | | **50.5** | |

Confidence: MED. FRONTIER: no.

Red-team adjustment (main researcher, 2026-11-01): whitespace 2 to 1 (red team: ten or more named tools including Westlaw Quick Check, Clearbrief and free CourtListener lookups); willingness to pay and unit economics 2 to 1 (red team: readers are unpaid, lawyers have bundled tools, publishers build in-house).

## 3. The problem
- Who: volunteer peer reviewers, conference area chairs, grant panel members, journal editors, opposing counsel, judges and their clerks.
- Cost: a reviewer who finds one false claim stops trusting the paper but "I don't want to waste my time verifying every single paper they cite" (PRO-238). NeurIPS organizers say AI-written submissions externalise the cost of verification onto reviewers (AI2-07). Courts logged 2,246 matters with hallucinated content (AI2-12), and each needs someone to check the citations (AI2-13).
- Workarounds: check a handful of references by hand, run an AI-text detector, reject on suspicion, or fine the filer.
- Gap: author-side checkers exist, but the person who must read the document wants a ranked list of the references that matter and why each fails.

## 4. Evidence
- **PRO-238** (strong, 2026-09-14, r/AskAcademia, 226 pts / 109 comments): "Now I don't trust any other claim the paper makes, but I don't want to waste my time verifying every single paper they cite. Is it legitimate then to reject the paper based on that one false citation saying it raises questions about the credibility of everything else?" https://www.reddit.com/r/AskAcademia/comments/1wfvkdi/
- **AI2-07** (strong, 2026-06-02, NeurIPS 2026 blog): Pangram flagged 28.2% (273 of 969) position-track submissions; "submitting AI-generated text for peer review externalises the cost of verifying that work, imposing it on reviewers." https://blog.neurips.cc/2026/06/02/ai-generated-papers-in-the-neurips-2026-position-paper-track/
- **AI2-12** (strong, 2026-10-31, Damien Charlotin's database): "While seeking to be exhaustive (2246 cases identified so far)." Party filter: 887 lawyers, 1,296 pro se litigants, 33 judges. https://www.damiencharlotin.com/hallucinations/
- **AI2-17** (medium, 2025-08-24, Academia StackExchange, 57 votes): a PI on a trainee's AI-written grant draft: "I am also not happy about putting in time and effort to edit work that was generated from a prompt." https://academia.stackexchange.com/questions/221011/how-do-we-deal-with-trainees-students-using-llm-for-higher-academic-work
- **AI2-13** (weak, 2026-02-23, HN): on a $2,500 sanction, "the immense potential for damage and the wasted time, resources and costs of several attorneys, clerks, witnesses, the judge/panel". https://news.ycombinator.com/item?id=47117824
- New evidence (not in SIGNALS.md), snippet only: coverage on The Decoder says GPTZero found 100 fabricated citations in NeurIPS 2025 papers and over 50 hallucinated references in ICLR 2026 submissions. https://the-decoder.com/hallucinated-references-are-passing-peer-review-at-top-ai-conferences-and-a-new-open-tool-wants-to-fix-that/ [UNVERIFIED primary; seen through a search summary]
- New evidence (not in SIGNALS.md), snippet only: a Nature analysis with Grounded AI of 4,000+ publications reported "Around 5% [of manuscripts] show potential reference-related issues" (search summary of Nature coverage; the article itself was not read) [UNVERIFIED primary].
- New evidence (not in SIGNALS.md), context: a July 2026 arXiv position paper tested five public hallucinated-citation checkers and argues that none is sufficient alone as a gate (summary only). https://arxiv.org/pdf/2607.22693

## 5. The product
- What it does: the reader uploads a PDF or Word file (manuscript, grant, brief). Cite Check extracts every reference and every claim attached to it, resolves each reference to a real record, fetches the cited passage where full text is open, and labels each citation: verified, partly supported, not supported, source not found, or could not check (paywalled, with a reason). It outputs a one-page reviewer memo with the highest-risk references first and a quote from the source next to the claim, ready to paste into a review or a motion.
- Core AI loop: document -> parse claims and references -> resolve against Crossref, OpenAlex, Semantic Scholar, CourtListener -> retrieve passage(s) -> cheap model screens, stronger model judges uncertain cases -> memo with evidence quotes -> user marks agree or disagree -> thresholds improve.
- Interaction model: upload page and shareable report link; no automatic accusations; "could not check" is a first-class result.
- Form factor: web app (a browser extension for OpenReview-style review pages is a later option).
- Day in the life: a reviewer receives a 28-page paper with 61 references. The report shows 4 not found, 7 where the source says something different, 9 paywalled and unchecked. She spends 20 minutes on the 11 items, writes the review, and attaches the report.
- Scope guard: it checks existence and support, not scientific merit, and does not give legal advice.

## 6. Why the LLM is load-bearing
- "Does this paragraph support this claim, or only mention the topic?" needs reading comprehension over the source, which pattern matching cannot do. Existence checks need no LLM; claim-support checks are the value.
- Remove the model and you have DOI lookup, which free tools already do.

## 7. The insight
- Existence checks are easy and common; claim-support checks need reading the source, which long context made cheap. And the person who pays the cost of a bad citation is the reader, not the author, so the product should be built for the reader (ranked, evidence-quoted, shareable) rather than as an author pre-flight.
- Honest limit: paywalled sources cap coverage, and several teams are building the author side.

## 8. Why now, and why this does not exist yet
- Why now: AI-fabricated references reached top conferences and courts in 2025 to 2026 (AI2-07, AI2-12), and a claim-by-claim check costs about $0.40 per document (section 11).
- Why it partly exists: see section 10. Existence checking is common; verified claim-support at reader scale, with honest "could not check" states, is early and unproven (the position paper in section 4 says existing tools fall short).

## 9. Inspiration and derivation
- Parents: scite Reference Check, Grounded AI Veracity, Clearbrief's Cite Check Report, the CiteAudit and RefVerifier research pipelines.
- Changed: target user (the reader: reviewer, clerk, opposing counsel), interaction model (upload a document you did not write, get a ranked evidence memo), business model (per report, not per seat), channel (reviewer and clerk communities, shareable report). Four of five changed, but the core job overlaps with the incumbents' job.

## 10. Competition check
Queries run:
1. WebSearch: "AI tool checks whether cited sources actually support the claim, hallucinated references fabricated citations manuscript peer review reference verification"
2. WebSearch (Product Hunt): "site:producthunt.com citation checker verify references hallucinated citations papers" (no Product Hunt page returned)
3. WebSearch (YC directory): "site:ycombinator.com/companies citation verification hallucinated citations legal briefs research papers fact check references" (no YC company found)
4. WebSearch (named competitors): "scite OR "Clear Skies" OR "Grounded AI" OR Clearbrief reference check hallucinated citations journals publishers brief cite-checking 2026 pricing"
5. WebSearch: "scite smart citations supporting contrasting reference check tool; Clear Skies research integrity publishers manuscript screening" (nothing found on Clear Skies)

| Product | What it does | Price | How it differs |
|---|---|---|---|
| scite Reference Check ([CaSRAI profile](https://casrai.org/research-tools/ai-research-assistants/scite), [Manusights comparison](https://manusights.com/blog/is-scite-worth-it)) | Upload a manuscript PDF to examine cited sources; flags retractions, editorial notices and contrasting citation statements; Smart Citations classify supporting, contrasting, mentioning | paid, plans not verified | Strong on retractions and the citation graph; classification accuracy for "supporting" vs "mentioning" can be low per one source; not a passage-level check of the cited claim |
| Grounded AI "Veracity" (a Nature analysis of 4,000+ publications from five big publishers; seen only in a search summary, no vendor or Nature page read) | Checks citations against scholarly databases and the web; flags invalid, irrelevant or retracted references at submission | not found | Publisher-side; sold to publishers, the buyer with budget [UNVERIFIED primary] |
| [Manusights AI citation checker](https://manusights.com/blog/ai-citation-checker) | Fetches the cited paper's abstract and labels each claim supported, partly supported, not supported or unable to verify | not found | Closest consumer-style rival; abstract-level only per the summary; the vendor also sells manuscript review |
| [CiteAudit](https://arxiv.org/abs/2602.23452) (web app checkcitation.com), [RefVerifier](https://arxiv.org/pdf/2609.07652), [sciwrite-lint](https://arxiv.org/pdf/2604.08501), SemanticCite, CiteCheck, HalluCiteChecker | Open research pipelines for existence and claim support; sciwrite-lint runs locally | free | Prototypes; show the DIY floor and the accuracy gap |
| Legal: [Clearbrief Cite Check Report](https://www.lawnext.com/2025/12/clearbrief-launches-cite-check-report-to-give-law-firm-partners-an-audit-trail-against-ai-hallucinations.html) (Dec 2025), [CiteSentinel](https://www.cuinsight.com/press-release/tech-startup-launches-tool-built-to-catch-ai-hallucinations-in-legal-citations/) (BrentWorks, May 2026), CiteCheck AI ([Daily Record](https://thedailyrecord.com/2026/08/28/ai-hallucination-tech-tools/)) | Flag nonexistent or mismatched case and statute citations in briefs; Clearbrief says it uses classic ML and NLP rather than generative AI | not found | Funded or launched tools for the filer; the reader-side (opposing counsel, clerk) is less visibly served |
| Product Hunt, YC | No relevant listing or company found in two searches | n/a | Either absent or not indexed |

Classification: **WEAK DIRECT**. Academic and legal sub-markets each have small direct tools and a publisher-side vendor, but no clear leader for the reader-side, claim-support job; the rival count and a Nature-linked publisher tool push Whitespace to 2.

Platform risk: medium to high. Claude, ChatGPT and Gemini with search and file upload can already do a rough reference check on request; Google Scholar, Semantic Scholar, Overleaf or a publisher system could add a reference-support step; legal research incumbents (Thomson Reuters, LexisNexis) already sell brief analysis [ASSUMPTION, not verified in this research]. Per the rubric this caps Scale and defensibility at 2 and Whitespace at 3.

## 11. Business model
- Payer: individuals first (litigators, researchers, editors), then journals, conferences and small firms. Price: $12 per document report, $39/month for 5 reports, journal or conference plan about $499/year for up to 150 submissions [ASSUMPTION]. Anchors: a $2,500 sanction (AI2-13), scite and Manusights (prices not verified), Clearbrief (not found).
- Model cost per document [ESTIMATE], 30 pages, 60 references: parsing and OCR 30 pages x $4/1,000 = $0.12 (OCR price [UNVERIFIED]); reference extraction on Haiku 5.5, 8,000 in x $0.10/1M + 3,000 out x $0.50/1M = $0.0023; first-pass support check on Haiku, 3,500 in + 300 out = $0.0005 x 60 = $0.03; second pass on Sonnet 5.5 for the 30% uncertain (18): 3,500 in x $2/1M + 400 out x $10/1M = $0.011 x 18 = $0.20; memo on Sonnet, 6,000 in x $2/1M + 2,000 out x $10/1M = $0.032. Total about $0.38. Open scholarly APIs assumed free [ASSUMPTION].
- Per active user, 5 documents a month = $1.9, about $2.
- Gross margin [ESTIMATE]: ($39 - $1.9 - $1.43 Stripe) / $39 = 91%. At $12 per single report: ($12 - $0.38 - $0.65) / $12 = 91%.

## 12. Market size
- Buyers [ESTIMATE]: (a) small journals, societies and conferences: assume 1,500 buy at $499 [ASSUMPTION: about 5% of a roughly 30,000-journal universe, count not verified] = $0.75M; (b) solo and small-firm litigators: assume 150K US litigators in small practices [ASSUMPTION] x 3% x $39 x 12 = $2.1M; (c) individual reviewers: assume 20K paying $12 x 4 reports = $0.96M.
- Total at modest penetration: about $3.8M ARR. Reading: a small, fragmented market, better as a feature of a legal-tech or research-integrity business than a standalone company.

## 13. Go-to-market
- First 100: (1) a free author-side "are my references real" checker (existence only) for SEO and email capture on queries like "check if citations are real" and "ChatGPT fake references", about 40 free users who convert at 5%; (2) answer reviewer threads in r/AskAcademia and academic Mastodon or Bluesky with a worked example report on a public flagged paper, about 20; (3) litigators and law-librarian communities discussing sanctions cases from the Charlotin database, about 25 [ASSUMPTION: communities exist and accept vendor posts]; (4) outreach to small society journals and workshop organizers (a cold email with a sample report), about 15.
- Growth loop: reviewers paste the report into reviews and motions; the report carries a "checked with Cite Check" footer and a verify link.

## 14. Moat and scale path
- Moat: a labeled dataset of citation-support judgments with human feedback, a resolver that handles messy references, and trust (low false positives). Replicable by publishers over time.
- Scale path: publisher and conference API, then legal, then grant agencies, with an integrity audit trail.

## 15. Solo feasibility
- MVP (7 weeks): PDF and DOCX parsing, reference and claim extraction, resolvers (Crossref, OpenAlex, Semantic Scholar, CourtListener, Unpaywall for open full text), two-stage support check, memo generator, shareable report, feedback buttons. Open-access full text only; paywalled sources reported as "could not check".
- Running cost before revenue: about $40 to $100 a month (100 test documents x $0.38 = $38, hosting).
- Hardest risk: full-text coverage and false positives. If under about 50% of citations are checkable, the report is too sparse to trust [ASSUMPTION].

## 16. Pre-mortem
1. Coverage: most cited sources are paywalled, the report says "could not check" too often, and users go back to checking by hand.
2. A false accusation of fabrication harms an author, or a "verified" label misses a bad citation; trust and liability end the product.
3. The paying buyers (publishers, firms) go with incumbents, and the unpaid reviewers never convert.

## 17. Cheapest validation test
- What: assemble 20 documents with known problems (10 court filings from the Charlotin database and 10 papers flagged in public reports) and 10 clean papers; run the pipeline; then show the memos to 10 reviewers, editors or lawyers and ask what they would pay.
- Cost: about $15 in model calls plus a weekend. Duration: 2 weeks.
- Pass: at least 85% of fabricated references found, at least 60% of unsupported-claim cases flagged, under 5% false flags on clean papers, and at least 5 of 10 say they would pay $12 per report. Fail: false flags above 10% or fewer than 2 would pay.

## 18. Open questions
- Is the real buyer the publisher or conference (Grounded AI's route), and can a solo founder reach them?
- Can claim-support be judged reliably from open-access full text alone?
- Does the reader-side framing beat Clearbrief and scite for litigators and reviewers, or is it one feature of theirs?
- Should the first market be legal (more budget, more incumbents) or academic (less budget, more pain)?
- How should the report word a "not supported" finding so an editor can act on it without accusing an author?

## Deep dive

Added 2026-11-01. New facts were read 2026-11-01; "idea file" means sections 10 to 12 above (read 2026-10-31). Search-summary means I saw the fact only in a search result summary, not on the page. The payer is the crux: the people in pain (reviewers, clerks) rarely pay, so each part below tests who does.

### Competitor table
| Competitor | Link | What it does | Price (as published, with date read) | Funding or traction (sourced) | Gap this idea exploits |
|---|---|---|---|---|---|
| Westlaw Quick Check and Quick Check Judicial (Thomson Reuters) NEW | [TR page](https://legal.thomsonreuters.com/en/c/quick-check-judicial-on-westlaw-edge), [LawNext 2020-08](https://lawnext.com/2020/08/if-your-judge-is-using-this-new-ai-tool-should-you-be-using-it-too.html) | Upload up to six briefs from one matter, three per party; "analyze multiple documents from a single matter - your own and your opponent's"; flags inaccurate quotes and cases the parties missed; used by judges, and opposing counsel can use it too (search-summary) | At the 2020 launch, "no additional charge to all Westlaw Edge subscribers"; 2026 Westlaw Advantage $256.75 to $399.75 a month for firms up to 10 attorneys per a third-party blog ([Vaquill](https://www.vaquill.ai/blog/westlaw-precision-ai-review-honest-assessment), citing Thomson Reuters, June 2026); Quick Check pricing itself unconfirmed [UNVERIFIED] | Platform scale | The legal reader side is not empty. Open: lawyers without Westlaw, pro se opponents, non-US, academic |
| Clearbrief Cite Check Report | [LawNext Dec 2025](https://www.lawnext.com/2025/12/clearbrief-launches-cite-check-report-to-give-law-firm-partners-an-audit-trail-against-ai-hallucinations.html), [LawNext directory](https://directory.lawnext.com/products/clearbrief/pricing/) | Audit trail of a filer's citations; says it uses classic ML and NLP, not generative AI (idea file) | "$150 Per User/Month" unlimited or "$300 Per Brief" (directory listing, search-summary 2026-11-01); [G2](https://www.g2.com/products/clearbrief-clearbrief/pricing) lists no price | Not found | Filer-side. Its $300 a brief is the legal price anchor, 25 times a $12 report |
| CiteSentinel, CiteCheck AI | [CiteSentinel](https://www.cuinsight.com/press-release/tech-startup-launches-tool-built-to-catch-ai-hallucinations-in-legal-citations/), [Daily Record](https://thedailyrecord.com/2026/08/28/ai-hallucination-tech-tools/) | Flag nonexistent or mismatched case and statute citations in briefs | Not found | Launched May 2026 and by Aug 2026 (idea file) | Filer-side; claim support unproven |
| CiteAudit (checkcitation.com) | [paper](https://arxiv.org/abs/2602.23452), [The Decoder, 2026-03-08](https://the-decoder.com/hallucinated-references-are-passing-peer-review-at-top-ai-conferences-and-a-new-open-tool-wants-to-fix-that/) | Open benchmark and web app that detects hallucinated citations | Free: the team is "making CiteAudit freely available as a web application"; up to 500 citations a day after an email sign-up (The Decoder, as summarized by my fetch) | Academic team (Yuan et al.), no company named | Existence checking is free, so individual academics are unlikely to pay for it |
| GPTZero | [The Decoder](https://the-decoder.com/hallucinated-references-are-passing-peer-review-at-top-ai-conferences-and-a-new-open-tool-wants-to-fix-that/) | Found "more than 50 hallucinated references in ICLR 2026 submissions" (The Decoder) | Not found for citation checking | Funding not verified [UNVERIFIED] | Conference-side detection; support checks not shown |
| scite Reference Check | [CaSRAI](https://casrai.org/research-tools/ai-research-assistants/scite), [Manusights](https://manusights.com/blog/is-scite-worth-it) | Flags retractions, editorial notices, contrasting citations | Not verified: scite.ai/plans returned a 404 on 2026-11-01 | Not found | Citation graph, not passage-level support |
| Grounded AI "Veracity", Manusights citation checker | [Manusights](https://manusights.com/blog/ai-citation-checker) | Publisher-side checks (Nature analysis of 4,000+ publications, search-summary); abstract-level claim labels | Not found | Not verified | Sold to publishers; abstract-level only |
| RefVerifier, sciwrite-lint, SemanticCite, HalluCiteChecker | [RefVerifier](https://arxiv.org/pdf/2609.07652), [sciwrite-lint](https://arxiv.org/pdf/2604.08501) | Open pipelines | Free (idea file) | None | The DIY floor |
| ChatGPT, Claude, Gemini with upload and search | none | Rough reference checks on request | Subscription or free (idea file) | Platform scale | No resolver stack, "could not check" states or shareable memo |
| Free data rails: Crossref, OpenAlex, Semantic Scholar, Unpaywall, CourtListener, [Charlotin database](https://www.damiencharlotin.com/hallucinations/) | see build brief | Records, open full text, case law; 2,246 cases logged (idea file) | Free APIs (limits unverified) | n/a | Inputs, and the top of the funnel |

### Market sizing (bottom-up)
- Legal: 1.37M US lawyers in 2025 ([ABA Profile via TaxProf Blog](https://taxprofblog.aals.org/2025/12/10/aba-profile-of-the-legal-profession-number-of-lawyers-increase/), search-summary). 30% litigate [ASSUMPTION] = 411,000; 40% lack a Westlaw-class checker [ASSUMPTION] = 164,400. At $39 a month ($468 a year): conservative 1% = 1,644 x $468 = $0.77M; optimistic 4% = 6,576 x $468 = $3.08M.
- Academic individuals ($12 a report, 4 a year = $48): conservative 2,000 payers = $0.10M (free CiteAudit caps willingness to pay); optimistic 20,000 (idea file) = $0.96M.
- Journals, societies, conferences at $499 a year: conservative 300 = $0.15M; optimistic 1,500 (about 5% of a roughly 30,000-journal universe, count not verified) = $0.75M.
- Serviceable market: conservative $1.02M, optimistic $4.79M a year. Legal is 75% of the conservative and 64% of the optimistic total, so the first market is legal.
- Revenue at 100 / 1,000 / 10,000 customers: subscribers at $39 a month $46,800 / $468,000 / $4.68M (10,000 is above the optimistic legal pool of 6,576); journal plans $49,900 / $499,000 / not reachable.

### Unit economics
Per document, then per month. Prices from `research/LANDSCAPE.md` section 6. All [ESTIMATE].
- One 30-page, 60-reference document: OCR 30 x $4/1,000 = $0.12 (price [UNVERIFIED]); reference extraction on Haiku 5.5, 8,000 x $0.10/1M + 3,000 x $0.50/1M = $0.0023; first-pass support check, 60 x (3,500 x $0.10/1M + 300 x $0.50/1M = $0.0005) = $0.03; second pass on Sonnet 5.5 for 30% (18) x (3,500 x $2/1M + 400 x $10/1M = $0.011) = $0.198; memo 6,000 x $2/1M + 2,000 x $10/1M = $0.032. File total $0.382. Added here: embeddings, 60 papers x 8,000 tokens x $0.02/1M = $0.0096; web-search fallback for unresolved references, 10 x $10/1,000 = $0.10 [ASSUMPTION]. Total $0.49.
- Subscriber, 5 documents a month: model 5 x $0.49 = $2.46; payment fee $39 x 2.9% + $0.30 = $1.43; human QA, 1 report in 20 read for 10 minutes at $30 an hour = $0.25 each, so $1.25 [ASSUMPTION]; infrastructure $80 a month / 100 customers = $0.80 (or $0.08 at 1,000). Cost $5.94 at 100 customers, margin (39 - 5.94) / 39 = 85%; $5.22 and 87% at 1,000.
- Single $12 report: $0.49 + fee $0.65 + QA $0.25 + infrastructure $0.16 = $1.55, margin 87%. If lawyers pay $29 a report: cost $2.04, margin 93%.
- Journal plan, $499 a year for 150 submissions: 150 x $0.49 = $73.78 + fee $14.77, margin 82%.
- Heavy user, 40 long briefs a month (80 pages, 150 citations): per brief OCR $0.32 + extraction $0.006 + first pass 150 x $0.0005 = $0.075 + second pass 45 x $0.011 = $0.495 + memo $0.05 + embeddings $0.024 + search 20 x $0.01 = $0.20 = $1.17, so $46.80 a month, more than the $39 price. Pricing cap: 5 reports included, then $6 each (cost $1.17 + fee $0.47, margin 73%).

### First 100 customers
Three payer tracks with a stop rule. Funnel [ESTIMATE]: legal visitor to a free partial run (first 10 citations) 20%, run to paid report 5%, so 1.0% visitor to paid; academic 15% x 2% = 0.3%; journals: 10 individual emails a week, 20% reply, 25% of replies take a free pilot, 25% of pilots pay $499. Worked examples use court sanction orders (public record) and a synthetic manuscript with seeded errors; no author or lawyer is named beyond the court's own order.
| Week | Channel and action | Message and offer | Legal visitors | Legal paid (cumulative) |
|---|---|---|---|---|
| 1 | Five worked examples from the Charlotin database plus a synthetic manuscript; one post in r/LawyerTalk if the moderators agree; legal posts on Bluesky and Mastodon | "Check an opposing brief's citations in minutes. First 10 free, full report $12 (lawyers $29)" | 200 | 2 |
| 2 | Email the editors of two legal-tech outlets (LawNext among them) with a worked example; ask for a directory listing | Same | 250 | 5 |
| 3 | Individual emails to 10 law librarians at firms and courts offering a free trial | Same | 300 | 8 |
| 4 | r/AskAcademia and Academia StackExchange threads like PRO-238 ("reject on one false citation?") | Free reviewer report; decision gate at the end of the week | 400 | 12 |
| 5 | 10 emails to small society journals and workshop organizers with the synthetic sample | Free pilot for 30 submissions, then $499 a year | 500 | 17 |
| 6 | Pitch a solo and small-firm section of a state bar for a short session | Same | 600 | 23 |
| 7 | Convert $12 buyers: 5 reports, then $6 each, for $39 a month | Subscription offer | 700 | 30 |
| 8 | Show HN with the sanction-database example; review the funnel | Same | 800 | 38 |
Base case: 3,750 legal visitors and 38 paid, plus about 3 academic buyers and 1 journal = 41 paying by week 8; 100 around week 15. Stop rule at the end of week 4: fewer than 10 paying litigators and no journal agreeing to a paid pilot means the product is a free tool; fold it into a legal-tech product or stop. Growth loop after 100: each report carries a "checked with Cite Check" footer and a verify link, lawyers attach it to motions, and clerks and opposing counsel who see it become users.

### One-week validation test (under $50)
Accuracy gate first (days 1 to 3), then the payer test (days 4 to 7).
- Gate: script a rough pipeline (reference extraction, Crossref, OpenAlex and CourtListener lookups, a two-step support judge). Run it on 8 public filings from the Charlotin database and 4 clean public filings; check by hand. Pass the gate if it finds at least 85% of the known fabricated citations, wrongly flags no more than 5% of citations in the clean filings, and never labels a paywalled source "verified". If it fails, skip the rest and fix it.
- Page (day 4): one static page, "Cite Check, pre-launch", saying reports this week are produced by a script I run by hand, with one worked example. Legal section: reserve a $29 report on any public filing, refundable, delivered within 48 hours. Reviewer section: reserve a $12 report. Journal section: request a free 30-submission pilot. All via Stripe Payment Links and a form.
- Reach (days 4 to 7): one disclosed post in r/LawyerTalk and one in r/AskAcademia, only if rules allow; 12 individually written emails to public addresses (6 solo or small-firm litigators who write publicly about AI-citation sanctions, 6 editors or organizers of small society journals and workshops). No unsolicited messages beyond those, no accounts but my own.
- Budget: model calls $10 (12 documents x $0.49 = $5.90 plus retries and up to 5 delivered reports); domain $12 [ASSUMPTION]; Stripe fees on 3 refunded $29 reservations 3 x $1.14 = $3.42 and 2 refunded $12 reservations 2 x $0.65 = $1.30 [ASSUMPTION: fees not returned]; APIs, hosting and forms free. Total about $27, cap $50.
- Valid if at least 150 unique legal-section visitors.
- Legal arm: pass = at least 3 paid $29 reservations; 1 to 2 = weak, retest at $12 and $49; 0 = fail. Reviewer arm: record only; 2 or more paid reservations would be a surprise worth noting. Journal arm: pass = at least 1 reply asking for a pilot that names who holds the budget (editors are slow; if none by day 7, extend to day 14).
- Overall pass = gate passed and (legal arm passes or journal arm passes). Fail = gate failed, or 0 paid reservations at 150+ visitors and 0 pilot requests by day 14.

### Build brief (paste into a coding session)
- Product summary: A reader-side citation check. Upload a manuscript, grant or brief you did not write; get a ranked evidence memo of citations that have no matching record or do not support the claim, with the source passage quoted. "Could not check" (paywall, missing text) is a first-class result with a reason. It states findings of fact about records, never accusations.
- MVP features (each testable):
  1. PDF and DOCX parsing that extracts the reference list and each in-text claim tied to a reference (at least 95% of references extracted on 30 documents).
  2. Resolution of each reference against Crossref, OpenAlex, Semantic Scholar and, for case law, CourtListener, with a match confidence.
  3. A second-source search before any "no matching record found" label (test: 20 real but obscure references are not mislabeled).
  4. Open full-text retrieval through Unpaywall and passage retrieval; otherwise "could not check" with the reason (paywalled sources are never "verified").
  5. Two-stage support judgment: Haiku 5.5 screens every pair, Sonnet 5.5 judges the uncertain 30%; labels are verified, partly supported, not supported, no matching record found, could not check.
  6. A one-page memo, highest risk first, with the source quote beside the claim.
  7. Shareable report link that can be revoked, with a "checked with Cite Check" footer and a verify link.
  8. Agree or disagree buttons per finding, saved as labeled data.
  9. Stripe: first 10 citations free; per-report prices set by the test ($12 reviewers, $29 lawyers); $39 a month for 5 reports; $6 per extra; journal plan $499 a year.
  10. A wording filter so memos contain no accusatory terms ("fabricated", "fraud").
- Non-goals (v1): AI-text detection; judgments of scientific merit or legal advice; plagiarism checks; paywall circumvention; a browser extension; a publisher API; Westlaw or Lexis integration.
- Core AI loop: document -> text extraction in code (OCR only for scans, $4 per 1,000 pages) -> Haiku 5.5 ($0.10/$0.50) extracts references and claims into JSON -> resolvers in code -> passage retrieval by embeddings ($0.02/1M tokens) -> Haiku screens each claim-source pair -> Sonnet 5.5 ($2/$10) judges uncertain pairs and writes the memo -> checkpoints: the founder reads the first 100 reports and 1 in 20 after that; the reader agrees or disagrees; the wording filter runs last.
- Data model: Account, Document, Reference, Citation (claim sentence, reference id), Resolution (source, record id, confidence), SourceText (URL, license, passages), Judgment (label, quote, rationale, model, confidence), Report (share token, revoked), Feedback, Plan.
- Integrations (docs): [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/), [OpenAlex](https://docs.openalex.org/), [Semantic Scholar](https://www.semanticscholar.org/product/api), [Unpaywall](https://unpaywall.org/products/api), [CourtListener](https://www.courtlistener.com/help/api/) (rate limits and commercial terms [UNVERIFIED]), [Stripe](https://docs.stripe.com/), [Anthropic API](https://docs.anthropic.com/).
- Stack (about $100 to $150 a month): Next.js on Vercel for the app; a Python worker (PyMuPDF for parsing) on Fly.io or Render; Supabase Postgres with pgvector, auth and storage; Stripe; Sentry; Langfuse free tier for traces and evals; model spend about $40 for 100 test documents.
- Evals: (1) 10 court filings and 10 flagged papers: at least 85% of fabricated references found. (2) The same set: at least 60% of unsupported-claim cases flagged. (3) 10 clean papers: under 5% of citations wrongly flagged. (4) 20 paywalled-only sources: none labeled verified. (5) 50 memos: no accusatory words.
- Build plan (7 weeks): W1 parsing, reference and claim extraction, eval harness; W2 resolvers with second-source search; W3 Unpaywall retrieval and passage matching; W4 two-stage judge and memo; W5 share links, feedback, wording filter; W6 Stripe, free tier, case-law module; W7 pilot with 10 users, QA sampling, launch.
- Key risks to test first: (1) the payer (the test above); (2) the legal reader side being served by Westlaw Quick Check Judicial and Clearbrief; (3) coverage: if under about 50% of citations are checkable the memo is too sparse; (4) a false "no matching record" label harming an author; (5) CourtListener and API limits for commercial use.

Notes for the main researcher: Section 10 only assumed that legal incumbents sell brief analysis; Westlaw Quick Check Judicial is now confirmed as a reader-side product that compares briefs from both sides and is open to opposing counsel and judges, so the legal gap is narrower than "less visibly served"; Whitespace 2 is fair and I would not raise it. CiteAudit is free for 500 citations a day, so individual academics will not pay for existence checks; the only paying wedge I can see is claim support for litigators without Westlaw, plus journals. Clearbrief lists $300 a brief, so $12 may read as a toy to lawyers; the test prices lawyers at $29. WTP 2 holds.

## Red team
Skeptical-investor review on 2026-11-01 (full text: `research/RED_TEAM_B.md`). Verdict: **pass**.

**Top attacks (summarized):**
1. **The easy half is free and the hard half is crowded or unproven.** Existence checks are free (CourtListener's Citation Lookup API, CaseRead, CiteAudit at 500 citations a day); legal readers have Westlaw Quick Check Judicial and Clearbrief ($150 a user a month or $300 a brief); LawDroid CiteCheck, QiXCite and CiteProof add more; scite and Grounded AI cover research.
2. **The precision bar is loose for the harm a false flag does.** Under 5% false flags means about 3 false accusations per clean 60-reference paper.
3. **The people in pain do not pay, and the people who pay buy elsewhere.** Reviewers are unpaid, lawyers have bundled tools, publishers build in-house; the journal funnel yields about 0.1 journals a week [ESTIMATE in the red-team file].
What would change the red team's mind: the accuracy gate passing with false flags under 2%, plus 3 paid reservations from non-Westlaw litigators or a journal naming a budget for a paid pilot.

**Response (main researcher):**
- All three attacks land, and attack 1 changes the classification: with ten or more named tools including the dominant legal-research incumbent, this is CROWDED by the methodology's definition. Whitespace drops from 2 to 1 and willingness to pay from 2 to 1.
- **Decision: killed after red team.** Consistent with how other crowded drafts were treated. The deep dive stays in the file as a record; the claim-support check for academic peer review is the only unproven sliver.
