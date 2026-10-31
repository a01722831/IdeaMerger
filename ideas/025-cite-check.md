---
id: "025"
slug: cite-check
name: Cite Check
one_liner: "Upload a manuscript or brief and get a reviewer report on which citations are fake or fail to support claims."
target_user: "Peer reviewers, journal and conference editors, grant reviewers, and litigators or clerks reading AI-assisted submissions"
form_factor: "web app"
lens: "Second-order AI"
frontier: false
competition: "WEAK DIRECT"
confidence: "MED"
status: "developed"
signals: [PRO-238, AI2-07, AI2-12, AI2-13, AI2-17]
scores:
  pain: 3
  evidence: 3
  ai_leverage: 4
  whitespace: 2
  novelty: 3
  why_now: 4
  solo_feasibility: 3
  distribution: 2
  wtp_economics: 2
  scale_defensibility: 2
total: 54.7
price_hypothesis: "$12 per document report, $39/month for 5; journal or conference plan about $499/year"
model_cost_per_user_month: "$2 (5 documents)"
gross_margin: "91%"
mvp_weeks: 7
deep_dive: false
red_team: false
---

# Cite Check

## 1. One-liner
Upload a manuscript or brief and get a reviewer report on which citations are fake or fail to support claims.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | Real and rising (28% of one conference track flagged as AI-written; 2,246 court matters), but a reviewer meets it a few times a year. |
| Evidence quality | 2 | 3 | Five signals, three strong, all about the verification burden; none states willingness to pay, and the reviewer is unpaid. |
| AI leverage | 2 | 4 | Judging whether a cited passage supports a specific claim is reading work a model now does; retrieval and human review remain. |
| Whitespace | 2 | 2 | Grounded AI (publisher channel, Nature analysis), scite Reference Check, Manusights, CiteAudit and legal cite-checkers (Clearbrief, CiteSentinel) all do parts of it. |
| Novelty of insight | 1 | 3 | A reader-side framing (the person who bears the cost of verifying) is a useful twist on author-side checkers. |
| Why now | 1 | 4 | AI-fabricated references went from curiosity to a flood in 2025 to 2026, and long context makes claim-by-claim reading cheap. |
| Solo feasibility | 2 | 3 | Reference resolution is easy; getting full text of cited sources (paywalls) is the hard part, so coverage is partial. |
| Distribution | 2 | 2 | Free author-side check can bring traffic, but reviewers and clerks have no budget and journals, courts and firms buy slowly. |
| Willingness to pay and unit economics | 2 | 2 | Cost per report is about $0.40 and margin is high, but the people in pain are unpaid; paying buyers are publishers and law firms who have incumbents. |
| Scale and defensibility | 2 | 2 | Labs' research agents and publisher integrity suites can add a "check the references" step; no data moat. |
| **Total** | | **54.7** | |

Confidence: MED. FRONTIER: no.

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
