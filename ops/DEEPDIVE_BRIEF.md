# DEEP-DIVE BRIEF (Phase 5)

You deepen existing idea files for the top-ranked ideas of a solo-founder startup-discovery project. Read first:
1. `ops/RESEARCH_BRIEF.md` (evidence rules and web access; sections 2 and 3).
2. `research/LANDSCAPE.md` section 6 (price table and cost rules of thumb). Use these prices for all model-cost math.
3. Each assigned idea file in full (it already has the 18 template sections and a competition check).

## What to add to each assigned file
Append one section at the end of the file, after section 18, titled exactly `## Deep dive`, with these subsections (in this order):

### Competitor table
| Competitor | Link | What it does | Price (as published, with date read) | Funding or traction (sourced) | Gap this idea exploits |
Include every direct and the most relevant adjacent competitor from section 10, plus any new ones you find (2 to 4 new searches allowed). Every price and funding fact needs a link; otherwise write "not published" or [UNVERIFIED].

### Market sizing (bottom-up)
Count target buyers from a cited source (government statistics, industry associations, platform counts) or an [ESTIMATE] with reasoning. Then: buyers x adoption rate x annual price = serviceable market. Give a conservative and an optimistic case, and the revenue at 100, 1,000 and 10,000 customers.

### Unit economics
Per active customer per month: model calls (input and output tokens per call x calls per month x price from the table), other variable costs (voice minutes, telephony, OCR, mail, payments at 2.9% + $0.30, human QA if any), infrastructure share, gross margin. Show every multiplication, tagged [ESTIMATE]. Add a heavy-user case and say how pricing caps it.

### First 100 customers
A week-by-week plan for the first 8 weeks after launch: named channels (specific subreddits, forums, associations, marketplaces, directories, newsletters, SEO queries with intent), the message, the offer, expected conversion at each step [ESTIMATE], and the growth loop after 100.

### One-week validation test (under $50)
Exactly what to build or post (e.g. a landing page with a priced pre-order, a concierge test done by hand, a forum post with a free audit offer), where, the budget line by line, the metric, and a numeric pass/fail threshold decided in advance. It must be doable by one person in 7 days, read-only with respect to other people's platforms (no spam, no fake accounts), and honest (no fake products presented as live; a waitlist or pre-order is fine if it says so).

### Build brief (paste into a coding session)
A self-contained block a founder can paste into an AI coding agent:
- Product summary (3 lines)
- MVP features (numbered, 6 to 10, each testable)
- Non-goals (what not to build in v1)
- Core AI loop (inputs, model calls with suggested model tier from the price table, prompts' job, outputs, human checkpoints)
- Data model (main entities)
- Integrations and APIs (with links to their docs where known)
- Suggested stack (frontend, backend, auth, payments, hosting, queues, observability), chosen for a solo founder at under $200 a month
- Evals: 3 to 5 test cases that prove the AI loop works
- Week-by-week build plan (4 to 8 weeks)
- Key risks to test first

## Rules
- Edit only the files assigned to you, and only by appending the `## Deep dive` section and setting `deep_dive: true` in the front matter. Do not change scores, signals or earlier sections; put disagreements in a short "Notes for the main researcher" line at the end of the deep dive.
- Evidence rules apply: no invented prices, funding, URLs or quotes.
- Validate with `python3 scripts/build_index.py --only <NNN-> --check` (writes nothing). No git.
- Budget: about 6 WebFetch and 15 WebSearch for the whole batch.
- Final reply: 10 lines or fewer; one line per idea with the validation test and its threshold, plus anything that changed your view of the idea.
