# Landscape (October 2026)

Synthesis of three research files in `research/landscape/`:
- `launches.md`: what is launching (Product Hunt, YC batches, launch sites, directories), crowded vs emerging, 95 products worth remixing, HeyClicky calibration.
- `capabilities.md`: what models can newly do, what the big assistants now ship natively, full price tables, cost cheat sheet.
- `theses-graveyard.md`: YC Requests for Startups, 20 VC theses, 26 dead or absorbed AI products and why.

All facts below are sourced in those files (links, read dates, evidence codes). Interpretation is marked as such.

## 1. The one-paragraph read
By late 2026 the four big assistants (ChatGPT, Claude, Gemini, Copilot) have absorbed most horizontal AI use cases: general agents that browse and act, proactive "always-on" personal agents (Claude Duet 2026-10-21, Copilot Autopilot Oct 2026, Gemini tasks GA 2026-10-13, ChatGPT Work 2026-07-09), screen-aware help (Copilot Vision, Gemini Magic Pointer), memory, docs and decks, voice. Even OpenAI killed its own standalone surfaces (Atlas browser retired 2026-08-09, Sora shut down, Operator folded in). Meanwhile model prices fell hard at the small tier (Claude Haiku 5.5 and GPT-6 Luna at $0.10 in / $0.50 out per 1M tokens) and realtime voice is now a commodity ($0.05/min flat on OpenAI GPT Live). The investor consensus is "sell outcomes, not tools" in big regulated verticals (insurance, accounting, healthcare revenue cycle, legal), which is crowded and enterprise-sold. **Interpretation:** the solo-founder opening is narrow, deep, self-serve products for unglamorous buyers where the assistant cannot follow: domain-specific outputs with audit trails, multi-party workflows with long-lived case state, phone or voice actions under a business's own rules, write-back into niche systems of record, and verification layers for AI-produced work.

## 2. Red zones
### From the brief
Generic chat assistants and chat-with-your-docs; meeting notetakers, note-taking apps, inbox assistants; AI writing/copywriting and social post generators; resume and cover letter tools, interview copilots; AI headshots/avatars, image/video generators; website and landing page builders; support bots, AI SDR/cold email; tutoring chat, AI companions, therapy chatbots; travel and meal planners; coding assistants.

### Added from this research (evidence in `capabilities.md` and `theses-graveyard.md`)
| Added red zone | Why (short) |
|---|---|
| General browser or computer-use agents ("does web tasks for you") | Shipped by Anthropic, OpenAI, Google, Microsoft; OpenAI retired its own Atlas browser |
| General personal or household agents (email, calendar, errands, family logistics), incl. proactive or ambient variants | Claude Duet, Gemini tasks and "CC for groups" household agent, Copilot Autopilot, ChatGPT Work |
| Generic "sees your screen and helps" overlays for mainstream apps | Copilot Vision, Gemini Magic Pointer, Gemini Live; also HeyClicky itself (YC S26) for Mac |
| Document, slide, spreadsheet or report generators as the product | Claude designs/decks/docs in any chat; ChatGPT Work |
| Generic memory or "second brain" for chat | Native in all four assistants, with importers |
| General voice assistants, live translators, dictation | Gemini 3.8 Live, Live Translate, Rambler; ChatGPT voice; Siri rebuilt on Gemini (iOS 27, [UNVERIFIED]) |
| Thin connectors to Microsoft 365, Salesforce, Slack, Google | Vendors ship them natively (Claude M365 write tools, Salesforce skills, Claude in Slack) |
| Plain transcription, OCR or summarization wrappers | Transcription $0.003 to $0.006/min; OCR about $4 per 1,000 pages; OS features free |
| Personal finance chat | ChatGPT personal finance experience (rolling out May 2026, [UNVERIFIED]) |
| Study tools (flashcards, quizzes, video overviews) | Gemini Notebook study tools; Chegg's collapse shows answers-as-a-product is dead |
| "AI-native services" in insurance brokerage, accounting/audit, healthcare revenue cycle, legal transactions | Most crowded VC thesis (Sequoia, Bessemer, General Catalyst $1.5B, Mayfield $100M fund); licenses and enterprise procurement also hit kill criteria |
| Standalone consumer novelty apps (AI video feeds, AI social) | Sora: ~1M users to under 500k, ~$1M/day burn; Huxe, Yupp, Figgs, Dot died |
| Hardware companions and pendants | Humane, Rabbit, Limitless (also violates the no-hardware rule) |
| AI visibility / GEO trackers ("get recommended by ChatGPT") | Many PH launches in 2025 to 2026 (ReSO, Promptmonitor, Anvil), 2 YC S26 companies (Scope, Armature), several on BetaList |
| Dictation and push-to-talk typing | Wispr Flow (reported $280M raise), MacWhisper, superwhisper, Aqua Voice, many PH launches; OpenAI desktop voice 2026-07-23 |
| Generic Mac/PC voice assistants and overlays (indie Clicky clones) | Six Show HN clones in 10 months (Lenma, VibeWhisper, Hitoku Draft, Wisp, Atticus, Ida), plus VoiceOS, Goldfish, Clico, Sider Omni; labs entering |
| Invisible live-coaching overlays (sales calls, interviews) | Cluely (~$7M ARR claimed 2025) and copycats (Glass, TalkPilot, PitchMonster); also a cheating risk |
| Developer agent infrastructure (MCP servers, sandboxes, gateways, evals, agent memory) | 22 of 40 Launch HN posts since April 2026; "agent" or "MCP" in 42 to 48% of top-50 PH names mid-2026 |

## 3. Capability unlocks and what they enable
Maturity: production = runs unattended at volume; usable = real products with human oversight or narrow scope; experimental = demos.

| Unlock (approx. date) | Maturity Oct 2026 | Unit cost | What it enables for an app-layer startup (interpretation) |
|---|---|---|---|
| Screen and video understanding (2026) | usable to production | ~$0.0003 to $0.01 per screenshot; ~$0.1 to $0.3 per video hour (Flash-Lite tiers) | Watch a worker's screen inside a niche app (an EHR, a TMS, a government portal) and guide, check or document; turn video walkthroughs into SOPs, inspections, claims evidence |
| Computer use and browser agents (toolsets GA 2026; Gemini GA 2026-10-30) | usable, narrow and supervised | ~$0.02 (Haiku 5.5) to $0.29 (Sonnet 5.5) per 30-step task with caching, 5 to 8x more without | Fill a specific portal or legacy desktop app that has no API, under human approval; risky where platform terms forbid automation |
| Realtime voice and phone agents (gpt-realtime GA Aug 2025; Gemini 3.8 Live Sep 2026) | production for bounded call flows | $0.05/min (GPT Live) to ~$0.08/min platform; DIY STT+LLM+TTS ~$1.3 to $1.7 per hour | Phone agents that make or take calls under a business's rules (vendors, insurers, schedulers), voice-first tools for field workers and older adults |
| 1M context and prompt caching (2026) | production | cached reads at 2% to 10% of input price | Reason over a whole case file, contract set, building's history or codebase for cents; cheap repeated queries over the same corpus |
| Cheap small and on-device models (Haiku 5.5 2026-10-07; Apple Foundation Models WWDC26; Chrome built-in AI) | production (server), usable (device) | $0.10/$0.50 per 1M; $0 on device | "Process everything" products (every email, call, invoice, review) at fractions of a cent; privacy-first local apps; free tiers that do not burn cash |
| Tool use, MCP, apps inside assistants (MCP to Linux Foundation Dec 2025; ChatGPT Apps SDK Oct 2025; plugin directory 2026-07-09) | production (tools), early (distribution) | ~286 tokens overhead per request | Ship as an MCP server or ChatGPT/Claude app to reach users inside the assistant; agent-facing data products |
| Memory and personalization (2026) | production inside assistants | negligible | Mostly closed to startups as a standalone layer; open inside vertical workflows (case memory, client memory) |
| Document understanding and structured outputs (OCR 4 2026-06) | production | ~$4 per 1,000 pages OCR | Reliable extraction from messy paperwork (bills of lading, EOBs, permits, invoices) into systems of record |
| Deep research and web search APIs (2026) | production (search), usable (deep research) | $5 to $14 per 1,000 searches; $1 to $30 per research task | Monitoring and research products sold per report (compliance changes, competitor moves, grant opportunities) |

**Newly cheap combinations (interpretation):** voice + screen + tools at ~$0.05 to $0.15/min; Haiku-class + caching + batch for back-office backlogs; on-device first with server escalation for hard cases.

## 4. What the big assistants do natively (do not build as the core)
Summarized from `capabilities.md` (dated table with sources):
- ChatGPT: ChatGPT Work agent (2026-07-09), built-in browser in desktop app, apps/plugin directory on MCP, personal finance experience, GPT Live voice.
- Claude: Cowork in every conversation (2026-09-16), Cowork in Chrome side panel, designs/decks/docs, categorized memory, M365 write tools, Salesforce skills, Claude in Slack, Claude Duet proactive agent (2026-10-21).
- Gemini: Gemini 4 Argon tasks that run while you are away (2026-10-13), Gemini Spark on Windows, CC for groups household agent (Labs), Gemini 3.8 Live everywhere, Magic Pointer screen help, Notebook study tools, Personal Intelligence.
- Copilot: Copilot Vision screen share, hands-free browsing, long-term memory, Autopilot always-on agent (Oct 2026).
- Apple: Foundation Models framework for developers; Gemini-based Siri with on-screen awareness in iOS 27 ([UNVERIFIED]).

**Gaps the assistants leave (interpretation, to be tested in Phase 4):** vertical depth with audit and liability (evidence-linked outputs, approvals, retention); phone-based real-world actions under business-specific policies with write-back to niche systems; multi-party workflows (customer, vendor, regulator) with long-lived case state; offline or data-residency-constrained use; field work combining voice, camera and domain checklists.

## 5. Timing shifts
1. **Frontier labs moved into vertical workflows** (Claude Cowork plugins Jan 2026 triggered a reported $285 to 300B software selloff on Feb 2 to 3, 2026). Closes generic copilots; opens AI-native challengers to seat-based incumbents in niches the labs will not go deep on.
2. **Pricing is moving from seats to outcomes and hybrids**, with reversals (Ada and Legora retreated to predictable pricing). Per-job pricing works for narrow agents if cost per job is capped.
3. **AI assistants became distribution surfaces** (ChatGPT app directory on MCP, Instant Checkout beta). A new channel with gatekeeper risk.
4. **Labs collapse standalone products into one assistant** (Sora, Atlas, Operator, DALL-E). Standalone horizontal surfaces are a losing game.
5. **Acqui-hire is the default exit for feature-scoped capability** (Vercept to Anthropic, Hiro to OpenAI, Relay team to Google Chrome).
6. **Agents are becoming software users** (YC S26 "Software for Agents", F26 "Self-Maintaining APIs"). Opens agent-facing tooling.
7. **YC's asks moved from apps to bottlenecks** (W27: "AI's biggest bottlenecks are moving beyond the models"): credentials ("The $15-an-Hour Expert"), government paperwork rails ("Plaid for Government Benefits", "AI for City Hall"), air-gapped AI, owned models. F26 also asked for "AI for the Aging Population", "Proving You're Human", "AI-Native Compliance Infrastructure", "Multiplayer AI".
8. **Regulation:** EU AI Act high-risk obligations pushed to 2027 to 2028 by the Digital Omnibus; Article 50 transparency duties reportedly still from Aug 2026. Companion and minor-facing products closing (Character.AI under-18 ban, then bankruptcy Oct 2026).
9. **Enterprise AI budgets are real but concentrating** (Menlo: ~$37B gen-AI spend in 2025, 3.2x y/y) on vendors that prove hard ROI.
10. **Record funding and record shutdowns at once** (headlines, 2026). Obvious ideas face well-funded competitors.

## 6. Model price table (for cost estimates)
USD per 1M tokens, list price, read 2026-10-31. Full tables, sources and caveats in `capabilities.md`. **Use these numbers in every idea file.**

| Tier | Model | Input | Output | Cached input | Batch in / out |
|---|---|---|---|---|---|
| Cheap | Claude Haiku 5.5 (prompt up to 100K) | $0.10 | $0.50 | $0.01 | $0.05 / $0.25 |
| Cheap | GPT-6 Luna | $0.10 | $0.50 | $0.01 | $0.05 / $0.25 |
| Cheap | Gemini 2.5 Flash-Lite | $0.10 | $0.40 | $0.01 | $0.05 / $0.20 |
| Cheap | gpt-oss-20b on Groq | $0.075 | $0.30 | $0.037 | n/a |
| Cheap | DeepSeek flash (off-peak / peak) | $0.15 / $0.30 | $0.60 / $1.20 | $0.003 | n/a |
| Mid | Claude Sonnet 5.5 | $2.00 | $10.00 | $0.10 | $1 / $5 |
| Mid | GPT-6.1 Terra | $1.00 | $5.00 | $0.05 | $0.50 / $2.50 |
| Mid | Gemini 3.8 Flash (doubles after 2026-12-31) | $0.75 then $1.50 | $3.75 then $7.50 | $0.075 then $0.15 | half |
| Frontier | Claude Opus 5.5 | $4.00 | $20.00 | $0.20 | $2 / $10 |
| Frontier | GPT-6.1 Sol | $2.00 | $10.00 | $0.10 | $1 / $5 |
| Frontier | Gemini 4 Argon (doubles after 2026-11-30) | $2.00 then $4.00 | $10.00 then $20.00 | $0.10 then $0.20 | half |
| Top | Claude Fable 5.1 / GPT-6 Astra | $10.00 | $50.00 | $0.25 / $1.00 | $5 / $25 |

Caveats: Haiku 5.5 reprices the whole request to $0.50/$2.50 above 100K prompt tokens; Claude 4.7+ tokenizer counts ~30% more tokens for the same text; thinking tokens bill as output; Google intro prices double on Nov 30 / Dec 31, 2026 (budget on the later price).

| Speech and voice | Price |
|---|---|
| STT: OpenAI gpt-4o-mini-transcribe | $0.003/min |
| STT: Deepgram Nova-3 streaming / pre-recorded | $0.0077 / $0.0043 per min |
| STT: ElevenLabs Scribe v2 | $0.0037/min |
| TTS: Deepgram Aura-2 | $0.030 per 1,000 characters |
| TTS: ElevenLabs Flash/Turbo | $0.04 per 1,000 characters |
| TTS: Gemini 3.8 Flash-Lite TTS | ~$0.009/min (doubles after 2026-12-31) |
| Realtime voice: OpenAI GPT Live (gpt-live-1) | $0.05/min flat |
| Realtime voice: Gemini 3.8 Live | ~$0.005/min audio in, ~$0.018/min audio out |
| Voice agent platform: Deepgram Voice Agent API | $0.075/min standard |
| Voice agent platforms: Vapi, Retell, Bland all-in | ~$0.07 to $0.30/min ([UNVERIFIED]) |

| Other tools | Price |
|---|---|
| Web search (Anthropic, OpenAI) | $10 per 1,000 |
| Google Search grounding (Gemini 3+) | 5,000/month free, then $14 per 1,000 |
| OCR (Mistral OCR 4) | ~$4 per 1,000 pages ([UNVERIFIED]) |
| Embeddings (OpenAI text-embedding-3-small) | $0.02 per 1M tokens |

### Cost rules of thumb [ESTIMATE]
- One "typical" call of 3,000 input + 500 output tokens: Haiku 5.5 = 3,000 x $0.10/1M + 500 x $0.50/1M = $0.0003 + $0.00025 = **$0.00055**; Sonnet 5.5 = $0.006 + $0.005 = **$0.011**; Opus 5.5 = $0.012 + $0.010 = **$0.022**.
- A user making 10 such calls a day (300/month): Haiku **$0.17**, Sonnet **$3.30**, Opus **$6.60** per month.
- One hour of phone-agent talk time: GPT Live $0.05 x 60 = **$3.00**; Deepgram Voice Agent $0.075 x 60 = **$4.50**; plus telephony (not priced here).
- 100 screenshots analyzed on a cheap vision tier: about **$0.03 to $1.00** depending on resolution and model (see `capabilities.md` cheat sheet C).
- A 30-step computer-use task: **$0.02** (Haiku 5.5) to **$0.29** (Sonnet 5.5) with caching.
- $200/month of runway buys roughly 360,000 Haiku-class typical calls, or ~18,000 Sonnet-class calls, or ~66 hours of GPT Live voice.

## 7. Traps to avoid (from 26 graveyard cases)
1. **Thin wrapper, no workflow lock-in** (Jasper, Tome's original product, Relay, Huxe). The general model makes the plain version free.
2. **Could be a button in the assistant, browser or OS within 12 months** (Relay, Notion Mail, Vercept, Hiro; OpenAI's own Atlas, Operator, DALL-E). Ask "what if ChatGPT, Claude, Gemini or Chrome adds this?"
3. **Hardware and devices** (Humane, Rabbit, Limitless).
4. **Consumer novelty without retention** (Sora, Huxe, Yupp, Figgs, Dot).
5. **Model cost per user above price** (Sora ~$1M/day, Figgs free tier, Character.AI "wildly unsustainable"). Cap free tiers; set a cost ceiling per task.
6. **Single supplier or platform dependency** (Windsurf lost Claude access on under 5 days' notice; Scale AI). Build model-agnostic; own the customer.
7. **Training your own frontier model** (Inflection, Adept, Covariant, Character.AI).
8. **Over-claiming capability or revenue** (Builder.ai insolvency; Apple's $250M Siri settlement).
9. **Minors, companionship and emotional support** (Character.AI lawsuits, under-18 ban, bankruptcy).
10. **Selling information or answers** (Chegg: two big layoffs in 2025). Sell action, workflow, verification or trusted outcomes.
11. **Pivots that worked moved to a workflow where AI is the interaction and data accrues** (Tome to Lightfield).
12. **"Services as software" is not a free pass**: most crowded thesis; implementation-heavy delivery does not fit a solo founder unless the product is self-serve.

## 8. AI launches: crowded vs emerging
Source: `launches.md` (95 products with links, YC batch counts from a mirror of YC's directory, Product Hunt via mirrors, BetaList, Uneed, Microlaunch, Futurepedia).

**Baseline.** AI words appear in 73 to 85% of every YC batch since Winter 2025, so AI is no longer a differentiator. "Agent" language rose to 29 to 30% of one-liners (Spring and Fall 2026); robotics rose from 1 to 5% (2025) to 8 to 11% (2026). YC has nearly stopped funding AI SDRs, support bots and notetakers (0 to 2% of one-liners in 2026) while launch sites stay full of them (BetaList ~32% AI; ~35 to 42% of Microlaunch AI listings are media-generation wrappers). Extruct's analysis of W26 puts "AI-native service" companies at 28% of the batch, the largest cluster.

**Crowded on launch sites:** media generators and model wrappers; coding agents and their tooling; developer agent infrastructure; GEO/AI-visibility trackers; chat widgets, AI receptionists, support bots and SDRs; dictation; indie Mac voice overlays; notetakers and inbox assistants; invisible live-coaching overlays; "Cursor for X / Lovable for X" positioning.

**Emerging (each with products in `launches.md`):**
1. Hold-a-key desktop voice agents (HeyClicky cluster). New but already contested by labs.
2. Ambient work memory that agents can query (Screenpipe YC S26, Littlebird, Sentient OS). Privacy objections are the sharpest in the sample (LAND-01).
3. Proactive agents behind approval gates (jo, Moonshot, Memoir; labs arrived in Oct 2026 with Claude Duet and OpenAI Dots).
4. Supervising fleets of agents (Rindler, Paradev, Muster, Nowdex): "past two or three sessions, you become the bottleneck" (LAND-08).
5. Agents as customers: payments, identity, discovery (Orthogonal, Bluerails, Armature).
6. No-API automation sold as an API or finished service (Minicor, Kampala, Lance, Zomma).
7. Shipping inside the LLM client as MCP apps (Kipper, Floot, Skybridge).
8. AI-native services with outcome or milestone pricing (Panacea, Altair Health with a theorem-prover gate, Arden audit workpapers).
9. Bring-your-own-subscription agents where the user's model plan carries cost of goods (Atticus, Turnstone, Agibot, OpenWork).
10. The post-build stack for vibe coders: distribution, payments, security (CREEM, Pancake, Harden).
11. Physical AI (context only; outside this project's constraints).

### HeyClicky calibration (the interaction bar)
HeyClicky (YC Spring 2026, from Farza's open-source Clicky) sits by the cursor, sees the screen only when you press a hotkey, answers by voice, points at UI elements, and can spawn background agents. Pricing: Free, $20 Pro, $100 Max, metering "agent messages" while talk stays unlimited. It reached Product Hunt #6 of the day (2026-04-11) and claims 25,000+ users [UNVERIFIED]; no revenue figure was found. Within months it was cloned (six Mac voice or overlay Show HNs) and absorbed (ChatGPT desktop voice plus computer control 2026-07-23; Claude Duet 2026-10-21; OpenAI Dots on PH Oct 2026). **Lesson for this project (interpretation):** the HeyClicky interaction pattern is the right bar for "AI is the interaction", but the generic version is now a lab feature. A defensible version attaches the pattern to a narrow job with domain data, a specific system of record, or a workflow the labs will not go deep on (for example a niche professional app, a government portal, a regulated checklist).

### Interaction patterns worth stealing
1. Consent by gesture: capture only while a key is held (HeyClicky, Goldfish, Atticus). Always-on capture draws privacy objections.
2. The cursor as context and pointer (VoiceOS, Clicky pointing, "spatial feedback loops").
3. Meter the expensive thing, not the conversation (HeyClicky caps agent messages, talk is unlimited).
4. Ride the user's existing model access (Atticus via `claude -p`, Agibot "free forever with your key"). Moves cost of goods to the user; vendor-terms risk.
5. Cheap path first: local routing, replay saved steps without AI, "show it once, let it run" (Atticus, IrisGo, Minicor).
6. Autonomy with explicit approval gates (Dardaris, Claude Duet, Altair Health's theorem-prover gate with human fallback).
7. The agent lives in a channel people already use (iMessage, Slack, Teams, Telegram, email).
8. Background and overnight work, ready by morning (Sentient OS, HeyClicky Agent).
9. One orchestrator to talk to, plus a phone remote (Rindler, Paradev, Muster).
10. Outcome, milestone or per-call pricing (Panacea, Orthogonal, Altair Health, pay-per-minute transcription).
11. Deliver the finished artifact, not a chat answer (Open Portal, Arden workpapers, Memoir).
12. Open-source seed, paid product on top (Clicky to HeyClicky, Agent Relay, OpenWork).
