---
id: "000"
slug: example-slug
name: Example Name
one_liner: "Twenty words max describing who it is for and the finished outcome it delivers."
target_user: "Specific persona, e.g. independent property managers with 20-200 units"
form_factor: "web app"            # web app | browser extension | desktop app | mobile app | plugin | API | voice agent | other
lens: "Pain-first"                # Pain-first | Newly possible | Remix | Transplant | Service-to-software | Second-order AI | Interaction shift | Forcing function | Underserved users | Wild
frontier: false                   # true only with leading indicators (see METHODOLOGY.md)
competition: "ADJACENT ONLY"      # WHITESPACE | ADJACENT ONLY | WEAK DIRECT | CROWDED
confidence: "MED"                 # HIGH | MED | LOW
status: "developed"               # developed | deep-dive | killed
signals: [HN-01, PRO-012, REV-03]
scores:
  pain: 3                 # weight 3
  evidence: 3             # weight 2
  ai_leverage: 3          # weight 2
  whitespace: 3           # weight 2
  novelty: 3              # weight 1
  why_now: 3              # weight 1
  solo_feasibility: 3     # weight 2
  distribution: 3         # weight 2
  wtp_economics: 3        # weight 2
  scale_defensibility: 3  # weight 2
total: 60.0               # computed by scripts/build_index.py: sum(weight x score) / 95 x 100
price_hypothesis: "$29/month per seat"
model_cost_per_user_month: "$1.50"
gross_margin: "85%"
mvp_weeks: 6
deep_dive: false
red_team: false
---

# Example Name

## 1. One-liner
Twenty words max.

## 2. Scores
| Criterion | Weight | Score | Why |
|---|---|---|---|
| Pain severity and frequency | 3 | 3 | ... |
| Evidence quality | 2 | 3 | ... |
| AI leverage | 2 | 3 | ... |
| Whitespace | 2 | 3 | ... |
| Novelty of insight | 1 | 3 | ... |
| Why now | 1 | 3 | ... |
| Solo feasibility | 2 | 3 | ... |
| Distribution | 2 | 3 | ... |
| Willingness to pay and unit economics | 2 | 3 | ... |
| Scale and defensibility | 2 | 3 | ... |
| **Total** | | **60.0** | |

Confidence: MED. FRONTIER: no.

## 3. The problem
Who has it, how often, what it costs them, what they do today (the workaround).

## 4. Evidence
At least 3 independent signals by ID from `research/SIGNALS.md`, each with a one-line note on what it shows. Quote the most telling one.

## 5. The product
- What it does (the finished outcome).
- Core AI loop (input -> model work -> output -> feedback).
- Interaction model (where it lives, how the user triggers it).
- Form factor.
- Day in the life (a short scenario).

## 6. Why the LLM is load-bearing
What breaks if you remove the model.

## 7. The insight
What we believe that others do not.

## 8. Why now, and why this does not exist yet
Be honest.

## 9. Inspiration and derivation
Parent products or patterns, and which of these changed: target user, core job, interaction model, business model, distribution channel (at least two).

## 10. Competition check
- Queries run (4+, differently worded, across web, Product Hunt, YC directory, relevant store).
- Findings with links.
- Classification: WHITESPACE / ADJACENT ONLY / WEAK DIRECT / CROWDED.
- Platform risk: could OpenAI, Anthropic, Google, Microsoft, Apple or the vertical incumbent ship this within 12 months?

## 11. Business model
Who pays, price hypothesis, model cost per active user per month from the price table in `research/LANDSCAPE.md` (show math, [ESTIMATE]), gross margin.

## 12. Market size
Bottom-up: number of target buyers x price x realistic penetration. Tagged [ESTIMATE] with the math.

## 13. Go-to-market
Channel to the first 100 customers, and the growth loop. Favor built-in channels.

## 14. Moat and scale path

## 15. Solo feasibility
MVP scope, weeks to build, monthly running cost, hardest technical risk.

## 16. Pre-mortem
Top 3 ways it fails.

## 17. Cheapest validation test
What to do, cost, duration, pass/fail threshold.

## 18. Open questions
