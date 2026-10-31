# Landscape track B: Capability unlocks and API prices

Owner: subagent, 2026-10-31. Scope: what LLM-based products can do in Oct 2026 that was not practical 12 to 18 months ago, what the big assistants already ship natively, and a sourced price table for cost estimates.

**Top takeaways for ideation** (interpretation, each backed by the sections below)
1. The price floor for a usable small model is about $0.10 in / $0.50 out per 1M tokens (Claude Haiku 5.5, GPT-6 Luna). A 3k-in / 500-out call costs about $0.00055 there, so about 1,800 calls per dollar. At 10 calls per user per day that is about $0.17 per user per month on Haiku 5.5 versus $3.30 on Sonnet 5.5 [ESTIMATE, see Cost cheat sheet].
2. Voice is cheap enough for consumer and SMB products: $0.05/min flat (OpenAI `gpt-live-1`), about $0.01 to $0.02/min of audio on Gemini 3.8 Live (audio only, before text and tool tokens), $0.05 to $0.08/min for bundled agent platforms, or about $1.3 to $1.7 per hour for a DIY STT + LLM + TTS stack [ESTIMATE].
3. Looking at screens and video is cheap: about $0.0003 to $0.01 per screenshot, and about $0.1 to $0.3 per hour of video on Flash-Lite-class models [ESTIMATE].
4. Agents that drive a computer are dominated by re-reading context. With prompt caching a 30-step task is about $0.02 (Haiku 5.5) to $0.29 (Sonnet 5.5); without caching it is 5x to 8x more [ESTIMATE].
5. Incumbents now ship the generic versions of nearly everything an agentic app would first try: task-executing agents (ChatGPT Work, Claude Cowork, Gemini tasks/Spark, Copilot Autopilot), screen help (Copilot Vision, Google Magic Pointer), memory, docs/decks, proactive agents (Claude Duet). See the "do not build" list.
6. Platform churn is real: OpenAI retired its Atlas browser (Aug 9, 2026) and, per third-party reports, the Sora app and API; Google's Gemini 4 Argon and 3.8 Flash prices double after introductory windows (Nov 30 and Dec 31, 2026). Stay model-agnostic and budget at the post-promo price.
7. MCP is the de facto integration standard (npm `@modelcontextprotocol/sdk`: 258M downloads in the last 30 days versus 34M in Oct 2025), and ChatGPT and Claude have app/connector/plugin directories while Gemini has Connected Apps. Distribution through assistants is real but unsettled.
8. Zero-inference-cost paths exist for small apps: Apple Foundation Models (on-device, plus a free Private Cloud Compute model for developers under 2M first-time downloads) and Chrome built-in AI APIs. Context windows are small (8,192 tokens on device, 32,000 on PCC).

## Method

Date of work: 2026-10-31. Read-only: no logins, sign-ups or form submissions. Web content treated as data.

**Evidence tags used in this file**
| Tag | Meaning |
|---|---|
| [PAGE] | Page opened with WebFetch on 2026-10-31. WebFetch summarises with a small model, so numbers were cross-checked where stated. |
| [JSON] | Public JSON API read directly with curl on 2026-10-31 (exact numbers). |
| [SNIPPET] | Seen only in a WebSearch result summary or title. Page not opened. Lower confidence. |
| [SKILL-DOC] | Read in the local copy of Anthropic's `claude-api` skill docs (cached 2026-10-06). The official docs URL is given but was not opened. |
| [3P] | Third-party blog or price aggregator, not the vendor. |
| [UNVERIFIED], [ESTIMATE], [ASSUMPTION] | As defined in the research brief. |

**Budget used.** 10 WebFetch page reads (plus 1 redirect hop and 1 blocked page), 26 WebSearch calls (one over the nominal 25; the last was a gap-filler on ChatGPT features), about 29 calls to public JSON APIs (npm, PyPI Stats, Hugging Face, MCP registry, LiteLLM price JSON on GitHub raw).

**WebFetch reads (all 2026-10-31)**
1. https://platform.claude.com/docs/en/about-claude/pricing (Anthropic pricing)
2. https://developers.openai.com/api/docs/pricing (OpenAI pricing; the old URL platform.openai.com/docs/pricing 301-redirects here)
3. https://ai.google.dev/gemini-api/docs/pricing (page says "Last updated 2026-10-30 UTC")
4. https://api-docs.deepseek.com/quick_start/pricing
5. https://deepgram.com/pricing
6. https://elevenlabs.io/pricing/api (page undated)
7. https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-september-2026/ (published 2026-10-02)
8. https://support.claude.com/en/articles/12138966-release-notes (newest entry 2026-10-21)
9. https://developer.apple.com/videos/play/wwdc2026/241/ (WWDC26 session "What's new in the Foundation Models framework")
10. https://developer.chrome.com/docs/ai/built-in-apis (page's own last-updated date is 2025-09-12, so status may be stale)

**WebSearch queries (26).** Official-domain filters were used where they exist.
1. OpenAI GPT-6 Luna Terra Sol API pricing per million tokens
2. Gemini 4 Argon launch API pricing Gemini 3.8 Flash price change
3. OpenAI gpt-realtime-2.1 GPT Live gpt-live-1 voice agents API per minute SIP phone latency
4. gpt-realtime Realtime API voice agents SIP phone calls announcement (openai.com, developers.openai.com)
5. OpenAI computer use agent API ChatGPT agent Atlas browser agent mode 2026 (OpenAI domains)
6. OpenAI shutting down ChatGPT Atlas browser August 9 2026 ChatGPT desktop app browser agent
7. Gemini 4 Argon announcement agent mode computer use Chrome auto browse Gemini Live screen sharing (Google domains)
8. Claude Cowork Claude in Chrome memory Skills Claude apps connectors directory new features (Anthropic domains)
9. WWDC26 Foundation Models framework iOS 27 Siri Apple Intelligence on-device model developers (Apple domains)
10. Introducing ChatGPT Work GPT-5.6 ChatGPT agent apps memory Pulse features announcement (openai.com)
11. Model Context Protocol adoption 2026 Agentic AI Foundation Linux Foundation MCP servers count ChatGPT Apps SDK app directory
12. Chrome built-in AI APIs Prompt API Gemini Nano Summarizer Translator Writer Proofreader stable status (Chrome domains)
13. Groq pricing per million tokens gpt-oss-120b gpt-oss-20b Qwen Llama input output price (Groq, Together, Fireworks domains)
14. OpenAI shuts down Sora app 2026 video generation API price per second Veo Gemini Omni Kling Runway
15. Microsoft Copilot 2026 features Copilot Vision screen sharing Copilot Actions Windows 11 agent Edge Copilot Mode Journeys memory (Microsoft domains)
16. iOS 27 Siri new features released Apple Intelligence Gemini-powered Siri personal context on-screen awareness agentic
17. search API for AI agents pricing per 1000 requests Exa Tavily Brave Search API Parallel Perplexity Sonar 2026
18. Deep Research API pricing cost per task Gemini Deep Research agent Interactions API OpenAI deep research API o3-deep-research 2026
19. Browserbase pricing per browser hour 2026 hosted headless browsers for AI agents Steel Hyperbrowser Anchor Kernel cost
20. voice AI agent platform pricing per minute 2026 Vapi Retell Bland Twilio ConversationRelay Cartesia Sonic latency phone agent total cost
21. Mistral OCR pricing per 1000 pages 2026 document AI OCR API cost Gemini PDF Claude PDF support pages tokens
22. Gemini API video understanding tokens per second video frames per second media resolution long video hours context (Google domains)
23. Gemini Personal Intelligence memory past chats connected apps; ChatGPT memory; import memory from other AI assistants (Google and OpenAI domains)
24. best small open-weight models October 2026 Gemma 4 Qwen 3.8 gpt-oss Llama Phi on-device phone laptop local LLM release
25. ChatGPT apps directory Apps SDK developers submit apps MCP Instant Checkout agentic commerce ChatGPT memory (OpenAI domains)
26. ChatGPT 2026 new features Pulse memory voice mode video screen share shopping research health group chats

**JSON API calls (public, no auth).** npm downloads API for `@modelcontextprotocol/sdk`, `openai`, `@anthropic-ai/sdk` (last month, last week, Oct 2025); PyPI Stats for `mcp`, `openai`, `anthropic`, `openai-agents`, `claude-agent-sdk`, `browser-use`, `pipecat-ai`, `livekit-agents`, `google-adk`; MCP registry `registry.modelcontextprotocol.io/v0/servers` (3 calls); Hugging Face model API (google, Qwen, openai, microsoft, meta-llama; 11 calls); LiteLLM `model_prices_and_context_window.json` (1 download, parsed locally) used only as a cross-check.

**Local docs.** Anthropic `claude-api` skill docs (cached 2026-10-06) for model IDs, computer-use toolset availability and migration notes. Where they disagreed with the official pricing page I used the pricing page.

**Cross-checks and known conflicts**
- OpenAI rows come from WebFetch's small-model summary. A raw-HTML check was not done (see Blocked sources). I cross-checked 8 headline OpenAI rows (gpt-6-astra, gpt-6.1-sol, gpt-6.1-terra, gpt-6-luna, gpt-5.6-luna, gpt-5.4-mini, gpt-5.4-nano, gpt-5-nano), 6 Anthropic rows and 6 Google rows against the LiteLLM price JSON ([3P], https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json). All matched. ElevenLabs TTS ($0.08 and $0.04 per 1K characters), Scribe v2 ($0.22/hour) and Deepgram Aura-2 ($0.030 per 1K characters) also matched.
- Claude Sonnet 5.5 cache-read price: the official pricing page says $0.10/MTok (0.05x base); the bundled skill doc says $0.20. I used $0.10 (LiteLLM agrees).
- GPT-5.6 Sol: launch price $5/$30 on Jul 9, then cut to $4/$20 (page note: "promotional pricing runs at least through November 21, 2026"). Some third-party pages still show $5/$30. Sources: [OpenAI community: price drop](https://community.openai.com/t/20-price-reduction-for-gpt-5-6-sol-api-codex-credits-and-chatgpt-work/1391726/3) [SNIPPET].
- Google introductory prices: the pricing page lists "price now, then price later" with cutoffs Nov 30, 2026 (Gemini 4 Argon) and Dec 31, 2026 (other models). Third-party coverage agrees on Argon ($2/$10, then $4/$20 from Dec 1) and on 3.8 Flash ($0.75/$3.75, then $1.50/$7.50) [3P: https://www.eesel.ai/blog/gemini-4-argon-pricing, https://www.techplained.com/gemini-3-8-flash]. Plan on the second price.
- Apple on-device context window: 8,192 tokens per a code comment in WWDC26 session 241 [PAGE]; a search summary of another WWDC26 session said 4,096 [SNIPPET], which was the first-generation model's window. I used 8,192 with a caveat.
- Gemini video tokens per second: one Google docs page says 263, another about 300 [SNIPPET]. Both are shown.
- Gemini Deep Research launch date: April 21 versus July 7, 2026 in different third-party pages [3P]. Not resolved.

## Capability unlocks

Summary (maturity scale: experimental = works in demos, fails often or lacks a stable API; usable = ships in real products with human oversight or narrow scope; production = reliable enough to run unattended at volume).

| # | Unlock | When it became practical (approx.) | Maturity, Oct 2026 | Typical unit cost | Native-assistant overlap |
|---|---|---|---|---|---|
| 1 | Screen and video understanding | 2026 (hi-res screenshots, 1M-token video, live image/video input metered at $0.002/min) | usable (screenshots production, continuous live screen share usable) | ~$0.0003 to $0.01 per screenshot; ~$0.1 to $0.3 per video hour | High for generic help (Copilot Vision, Magic Pointer) |
| 2 | Computer use and browser agents | Toolsets GA in 2026; Gemini tool GA 2026-10-30; ChatGPT Work 2026-07-09 | usable (narrow, supervised) | ~$0.02 to $1.2 per 30-step task | Very high for generic web tasks |
| 3 | Realtime voice and phone agents | gpt-realtime GA Aug 2025; gpt-realtime-2.1 Jul 2026; Gemini 3.8 Live Sep 2026 | production for bounded call flows | $0.05 to $0.08/min platform layer; $1.3 to $4.8 per hour all-in voice stack | High for generic voice chat |
| 4 | 1M context and prompt caching | 2026 (flat 1M pricing on Claude 4.6+ except Haiku 5.5) | production | cached reads 10% (or 5%, 2.5%, 2%) of input price | Low (developer-side) |
| 5 | Cheap small models and on-device | Haiku 5.5 2026-10-07; Gemma 4 Mar 2026; Apple FM WWDC26; Chrome 138 APIs 2025 | production (server), usable (on-device) | $0.10/$0.50 per 1M; $0 on device | Medium (OS features) |
| 6 | Tool use, MCP, apps in assistants, agent SDKs | MCP to Linux Foundation Dec 2025; Apps SDK Oct 2025; plugin directory 2026-07-09 | production (tools), early (distribution) | Tool overhead ~286 tokens per request (more for toolsets) | Medium |
| 7 | Memory and personalization | Claude memory rewrite 2026-07-10; Gemini Personal Intelligence; Copilot long-term memory | production inside assistants | Negligible if structured | Very high for generic memory |
| 8 | Document understanding, structured outputs, media generation | OCR 4 2026-06-23; Nano Banana line; Omni video; Lyria 3.5 | production (docs, images), usable (video, music) | $4/1,000 pages OCR; ~$0.03 to $0.13 per image; ~$0.10/s video | Medium |
| 9 | Deep research and web-search APIs | Interactions API previews 2026; search at $5 to $14 per 1,000 | production (search), usable (deep research) | $5 to $14 per 1,000 searches; $1 to $30 per research task | High for consumer research |

### 1. Screen understanding and video understanding

- **What changed.**
  - Claude models since Opus 4.7 accept images up to 2576 px on the long edge (about 4,784 tokens per image at the limit, versus about 1,600 before); for computer use Anthropic recommends 1080p, with 720p or 1366x768 as cheaper options [SKILL-DOC: bundled `shared/model-migration.md`; docs: https://platform.claude.com/docs/en/build-with-claude/vision].
  - Gemini reads long video natively: default 1 frame per second, about 263 to 300 tokens per second of video at default resolution and about 100 at low resolution, so a 1M-token window holds about 1 hour (default) or 3 hours (low). An "agentic" long-video mode claims up to 88% fewer tokens (a 1-hour lecture: about 1.08M tokens static versus about 108K) [SNIPPET: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding, https://ai.google.dev/gemini-api/docs/media-resolution].
  - Live image/video input is metered cheaply: Gemini 3.8 Live charges $1.00 per 1M image/video tokens, about $0.002 per minute [PAGE: https://ai.google.dev/gemini-api/docs/pricing]. OpenAI's Realtime models take image input at $5.00 per 1M tokens ($0.80 for the mini) [PAGE: https://developers.openai.com/api/docs/pricing].
  - OS-level screen assistants exist: Google's Googlebook "Magic Pointer" ("point and ask Gemini about anything on your screen with a quick cursor wiggle", WebFetch extract) [PAGE: https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-september-2026/]; Microsoft Copilot Vision shares the screen from Windows, Edge and mobile, and needs a Microsoft 365 Personal, Family or Premium subscription [SNIPPET: https://support.microsoft.com/en-au/topic/using-copilot-vision-with-microsoft-copilot-3c67686f-fa97-40f6-8a3e-0e45265d425f]; Apple's rebuilt on-device model accepts images of any size and ships `OCRTool` and `BarcodeReaderTool` [PAGE: https://developer.apple.com/videos/play/wwdc2026/241/].
- **Date.** Mostly 2026. Gemini long-video support is older, but the combination of hi-res screenshots, cheap live image input and OS-level screen sharing is new this year. [Interpretation: I did not verify what screen-share features Gemini Live or ChatGPT voice had 12 to 18 months ago.]
- **Maturity.** Screenshot Q&A, chart and document reading: production. Continuous live screen share assistants: usable. Hour-long video analysis: usable, accuracy on fine detail not verified here.
- **Typical cost.** [ESTIMATE, see cheat sheet C and D] 100 screenshots at 1920x1080 about $0.04 (Haiku 5.5) to $0.81 (Sonnet 5.5); 1 hour of video about $0.09 (Gemini 2.5 Flash-Lite) to $0.24 (Gemini 3.1 Flash-Lite).
- **Key vendors / APIs.** Anthropic Messages API vision and `computer_toolset_20260801` zoom action; Gemini API video understanding and Live API; OpenAI Realtime image input; Apple Foundation Models image input.
- **Patterns for an app-layer startup** (interpretation).
  1. A voice-guided "sees your screen" coach for one complex professional application (tax, EHR, ERP, CAD, niche SaaS), sold to firms for onboarding and training, with app-specific playbooks, compliance checklists and team analytics. Generic versions are native (Magic Pointer, Copilot Vision), so the wedge is depth in one app and the audit trail.
  2. Long walkthrough video to structured, evidence-linked report (inspections, move surveys, site visits, claims adjusters): about $0.1 to $0.3 per video hour makes per-report pricing viable.
  3. Screen recording to SOP and automation-candidate list: record a task once, get step-by-step documentation with screenshots and a ranked list of automatable steps.
- **Watch-outs.** Google, Microsoft and Apple are all moving screen awareness into the OS. Sensitive on-screen data raises privacy and surveillance concerns (a MISSION kill criterion if misused).

### 2. Computer use and browser agents

- **What changed.**
  - Anthropic: computer use is a GA toolset (`computer_toolset_20260801`, no beta header, 17 member tools including `zoom`) on the Claude API and Google Cloud, and Claude Opus 5.5 and Sonnet 5.5 accept only the toolset there [SKILL-DOC: bundled `shared/platform-availability.md` and `shared/tool-use-concepts.md`; docs: https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool]. A separate browser use toolset (`browser_toolset_20260801`) works inside webpages; Haiku 5.5 supports it, Haiku 4.5 does not [SKILL-DOC]. Declaring the computer toolset adds about 4,500 input tokens per request, the browser toolset about 6,600 [PAGE: https://platform.claude.com/docs/en/about-claude/pricing].
  - Claude surfaces: Cowork sessions run remotely on web and mobile (2026-07-07); the Claude in Chrome side panel runs a full Cowork session [PAGE: https://support.claude.com/en/articles/12138966-release-notes; SNIPPET: https://claude.com/blog/cowork-chrome-side-panel].
  - OpenAI: a computer use tool in the Agents API runs the browser in an OpenAI-hosted environment [SNIPPET: https://developers.openai.com/api/docs/guides/agents-api/tools/computer-use]. ChatGPT Work (announced 2026-07-09) is "an agent that can take action across apps and files and keep working on a project for hours" (search summary wording) [SNIPPET: https://openai.com/index/chatgpt-for-your-most-ambitious-work/]. OpenAI announced on 2026-07-09 that its Atlas browser would stop working on 2026-08-09; agent features move into the ChatGPT desktop app, which gets a built-in browser and a cloud browser [SNIPPET: https://www.macrumors.com/2026/07/10/openais-chatgpt-atlas-browser-shutting-down/, https://thenextweb.com/news/openai-chatgpt-atlas-browser-shutdown-superapp].
  - Google: the Gemini API Computer Use tool reached GA across the Interactions and GenerateContent APIs in a release dated 2026-10-30, with a `safety_decision` field that can require user confirmation [SNIPPET: https://ai.google.dev/gemini-api/docs/computer-use, https://ai.google.dev/gemini-api/docs/changelog].
  - Microsoft: "Browse with Copilot" in Edge (U.S., Microsoft 365 Premium subscribers); Copilot Mode is being retired [SNIPPET: https://blogs.windows.com/msedgedev/2026/05/13/new-updates-to-edge-across-desktop-and-mobile/].
  - Hosted browsers: Browserbase Developer plan $20/month with 100 hours, overage $0.12/hour; Steel and Hyperbrowser about $0.10/hour; Kernel about $0.06/hour; Browser Use Cloud about $0.02/hour [3P, [UNVERIFIED]: https://ecorpit.com/cloud-browsers-ai-agents-browserbase-steel-kernel-2026/, https://scrapegraphai.com/blog/browserbase-pricing].
  - Open-source adoption signal: PyPI `browser-use` had 8.1M downloads in the last month [JSON: https://pypistats.org/api/packages/browser-use/recent].
- **Date.** Toolsets GA in 2026 (version string 2026-08-01); Gemini GA 2026-10-30; ChatGPT Work 2026-07-09; Atlas retired 2026-08-09.
- **Maturity.** Usable for narrow, supervised workflows. Not production for open-ended unattended use. Prompt injection is an acknowledged risk (OpenAI published "Continuously hardening ChatGPT Atlas against prompt injection") [SNIPPET: https://openai.com/index/hardening-atlas-against-prompt-injection/].
- **Typical cost.** [ESTIMATE, cheat sheet E] A 30-step task with caching: about $0.02 (Haiku 5.5), $0.29 (Sonnet 5.5), $0.57 (Opus 5.5), $1.21 (Fable 5.1); without caching 5x to 8x more. Hosted browser time is small by comparison ($0.02 to $0.12 per hour [3P]).
- **Key vendors / APIs.** Claude computer/browser toolsets and Managed Agents ($0.08 per session-hour plus tokens) [PAGE pricing]; OpenAI Agents API computer use; Gemini Computer Use; Browserbase, Steel, Kernel, Hyperbrowser, Browser Use.
- **Patterns for an app-layer startup** (interpretation).
  1. Supervised "portal worker" for one regulated back-office workflow where the customer owns the credentials and the portal permits automation (claim status checks, document submission, reconciliation), with human approval before every write and a full evidence log. Check MISSION kill criterion on automating platforms against their terms.
  2. Agentic QA: run natural-language test plans against a web app and report visual and functional regressions, priced per test run.
  3. [FRONTIER, speculative] "Agent-readiness" testing for businesses: check whether ChatGPT, Claude and Gemini agents can complete the site's key flows (book, buy, quote). No demand evidence collected in this track.
- **Watch-outs.** Four large vendors ship the generic version; OpenAI retiring Atlas less than a year after launch (eWeek headline: "OpenAI Is Shutting Down Atlas Less Than a Year After Launch") shows how hard the standalone agent-browser business is [SNIPPET: https://www.eweek.com/news/openai-atlas-browser-shutdown-chatgpt/].

### 3. Realtime voice and speech-to-speech

- **What changed.**
  - OpenAI's `gpt-realtime` reached GA with remote MCP servers, image input and SIP phone calling about 14 months ago (Aug 2025) [SNIPPET: https://openai.com/index/introducing-gpt-realtime/]. Current docs describe inbound SIP webhooks, call accept, transfer (refer) and hang-up endpoints, a "GPT Live" product (model `gpt-live-1`) and outbound SIP calling that must be enabled per organization [SNIPPET: https://developers.openai.com/api/docs/guides/voice-sip]. `gpt-realtime-2.1` and `gpt-realtime-2.1-mini` were released 2026-07-06 with configurable reasoning and tool use, and a claimed 25% p95 latency reduction [3P, vendor claim relayed: https://mer.vin/2026/07/gpt-realtime-2-1-api-reasoning-voice-agents-and-mini-pricing/].
  - Google: Gemini 3.8 Live and a "Live Extended Thinking" variant for multi-step reasoning (Google's wording: "the top-rated speech-to-speech model for multi-step reasoning without all the lag") now serve developers and everyone in Search Live, Gemini Live and Workspace; voice also works inside Gmail, Docs and Keep [PAGE: https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-september-2026/].
  - Platforms: ElevenLabs Agents ("Speech Engine") $0.08/min; Deepgram Voice Agent API $0.075/min standard; Vapi, Retell, Bland and Synthflow quote $0.05 to $0.31/min before or after providers [PAGE: https://elevenlabs.io/pricing/api, https://deepgram.com/pricing; 3P: https://www.morphllm.com/best-ai-voice-agent-platforms, https://speechify.ai/blog/best-voice-agent-platforms-2026].
  - Open-source voice stacks are widely used: PyPI `livekit-agents` 3.6M and `pipecat-ai` 1.0M downloads in the last month [JSON: https://pypistats.org/api/packages/livekit-agents/recent, https://pypistats.org/api/packages/pipecat-ai/recent].
- **Latency.** Vendor-stated only, not independently measured: Bland about 400 ms, Retell about 600 ms, Vapi 500 to 800 ms [3P, [UNVERIFIED]: https://www.morphllm.com/best-ai-voice-agent-platforms]; SIP bridging adds an estimated 50 to 100 ms each way [3P, [UNVERIFIED]: https://www.open.cx/blog/openai-realtime-api-voice-agent-guide-2026]. I did not find a primary-source latency benchmark.
- **Date.** Aug 2025 (GA), Jul 2026 (2.1), Sep 2026 (Gemini 3.8 Live).
- **Maturity.** Production for bounded phone call flows (intake, scheduling, status, routing); usable for tool-heavy or emotionally sensitive conversations.
- **Typical cost.** [ESTIMATE, cheat sheet B] One hour of conversation: $3.00 on `gpt-live-1` (flat $0.05/min [PAGE pricing note]); about $0.84 audio cost on Gemini 3.8 Live; $4.50 Deepgram Standard; $4.80 plus LLM on ElevenLabs; about $1.3 to $1.7 for a DIY stack. Telephony (Twilio or similar) is a separate per-minute line item [NOT PRICED in this file].
- **Key vendors / APIs.** OpenAI Realtime API (WebRTC, WebSocket, SIP), Gemini Live API, ElevenLabs, Deepgram, Vapi, Retell, Bland, LiveKit, Pipecat, Cartesia (not checked), Twilio (not checked).
- **Patterns for an app-layer startup** (interpretation).
  1. Vertical inbound phone agent with real write-back to the customer's system of record (appointments, intake, dispatch) for categories where a missed call is lost revenue. This touches the "support bots" red zone, so it needs a sharp niche and deep integration; competition was not checked in this track.
  2. Outbound "make the call for me" for consumers and small businesses (waiting on hold, insurance or vendor follow-ups, appointment moves). Reasoning-capable speech-to-speech plus outbound SIP and cheap minutes make this newly viable. Carrier, consent and call-recording rules need a legal check.
  3. Hands-busy voice plus camera copilots for physical work (field service, kitchens, labs, warehouses) on a phone, no new hardware.
- **Watch-outs.** Generic voice assistants are native (Gemini Live, ChatGPT voice). Reasoning-enabled speech models and long context re-reads raise per-minute cost beyond the headline audio price.

### 4. Long context (1M+) and prompt caching

- **What changed.**
  - Claude 4.6 and later models (except Haiku 5.5) include the full 1M-token window at standard pricing; Haiku 5.5 prices up above 100K prompt tokens ($0.50/$2.50 per 1M) [PAGE: https://platform.claude.com/docs/en/about-claude/pricing].
  - OpenAI charges roughly 2x input and 1.5x output above 272K tokens (for example `gpt-6.1-sol`: $2/$10 short, $4/$15 long) [PAGE: https://developers.openai.com/api/docs/pricing]. Gemini 3.1 Pro doubles input above 200K ($2 to $4) [PAGE: https://ai.google.dev/gemini-api/docs/pricing]. DeepSeek V4 models list a 1M context with up to 384K output [PAGE: https://api-docs.deepseek.com/quick_start/pricing].
  - Caching discounts: Anthropic cache reads cost 0.1x base input (0.05x on Opus 5.5 and Sonnet 5.5, 0.025x on Fable 5.1); writes 1.25x (5 min) or 2x (1 hour) [PAGE]. OpenAI cached input is 5% to 10% of input on the GPT-6 and 5.x lines (Luna: $0.01 versus $0.10; gpt-6.1-sol: $0.10 versus $2.00) [PAGE]. Google caching is about 10% of input on Flash and Pro (3.8 Flash: $0.075 versus $0.75) and 5% on Gemini 4 Argon ($0.10 versus $2.00, implicit only), with storage fees on explicit caches [PAGE]. DeepSeek cache hits are about 2% of the miss price (flash: $0.003 versus $0.15) [PAGE].
  - Anthropic also ships server-side compaction and context editing for very long sessions (beta) [SKILL-DOC: docs https://platform.claude.com/docs/en/build-with-claude/compaction].
- **Date.** 2026 (exact release dates of Claude 4.6 and later not verified here).
- **Maturity.** Production.
- **Typical cost.** [ESTIMATE] Re-reading a 500K-token dossier on Sonnet 5.5: $1.00 uncached versus $0.05 cached (500,000 x $2/M vs 500,000 x $0.10/M).
- **Key vendors / APIs.** Claude (1M, cache_control, batch), Gemini (1M, implicit caching), OpenAI (up to 922K per LiteLLM [3P]), DeepSeek (1M).
- **Patterns for an app-layer startup** (interpretation).
  1. "Whole client file" reasoning: load an entire matter, case, portfolio or patient history (under about 700K tokens) into a cached context and answer repeatedly at 5 to 10% of input price, instead of building RAG.
  2. Long-running agents with compaction and a cached tool and skill prefix, so each step re-reads context at the cache-read price.
  3. Bulk "read everything" jobs (archives, contract sets, call libraries) via Batch API (50% off, stacking with caching).
- **Watch-outs.** Quality on very long contexts is task-dependent and was not tested here. Cache writes cost 1.25x to 2x, and 5-minute TTLs punish bursty traffic.

### 5. Cheap small models and on-device models

- **What changed.**
  - Price floor: Claude Haiku 5.5 $0.10/$0.50 (released 2026-10-07 per release notes), GPT-6 Luna $0.10/$0.50, Gemini 2.5 Flash-Lite $0.10/$0.40, gpt-oss-20b on Groq $0.075/$0.30, DeepSeek flash $0.15/$0.60 off-peak [PAGE: pricing pages in the Price table; https://support.claude.com/en/articles/12138966-release-notes]. Haiku 4.5 was $1/$5, so Haiku-class is 10x cheaper per token (about 7x to 8x after the new tokenizer's ~30% extra tokens) [PAGE: Anthropic pricing].
  - Apple (WWDC26): a rebuilt on-device model (context 8,192 tokens per a code comment, image input, better tool calling); a Private Cloud Compute (PCC) server model with a 32,000-token window and reasoning, which is free of cloud API cost for developers with under 2M first-time downloads (WebFetch extract: "PCC is available with no cloud API costs to developers who have less than 2 million first time downloads"; an entitlement is required); Swift packages from Anthropic and Google for third-party models (billed per token); a model abstraction layer; an `fm` command-line tool and Python SDK; the framework is being open-sourced [PAGE: https://developer.apple.com/videos/play/wwdc2026/241/]. Apple says its foundation models were built with Google's Gemini technology [SNIPPET: https://developer.apple.com/videos/play/wwdc2026/102/?id=614].
  - Chrome built-in AI: Translator, Language Detector and Summarizer are stable from Chrome 138; the Prompt API is stable for extensions from Chrome 138 and listed for the web at Chrome 148 (page text still describes an origin trial); Writer, Rewriter and Proofreader are developer trials [PAGE: https://developer.chrome.com/docs/ai/built-in-apis]. The status page does not name the model or give hardware requirements or languages [UNVERIFIED]; a Chrome I/O 2025 post mentions Gemini Nano alongside these APIs (search summary only) [SNIPPET: https://developer.chrome.com/blog/web-at-io25].
  - Open weights (Hugging Face API, 2026-10-31) [JSON]: Gemma 4 E2B and E4B created 2026-03-02 (tags image-text-to-text and any-to-any, Apache-2.0; https://huggingface.co/api/models/google/gemma-4-E4B-it), 26B-A4B and 31B created 2026-03-11 and 12B created 2026-05-23 (licenses of these three not checked); Qwen3.8-27B created 2026-08-05, Apache-2.0 (https://huggingface.co/api/models/Qwen/Qwen3.8-27B); gpt-oss-20b and 120b created 2025-08-04, Apache-2.0 (https://huggingface.co/api/models/openai/gpt-oss-20b). The newest models in the `meta-llama` org are dated April 2025 (Llama 4 Scout/Maverick and Guard models) and no Phi-5 was found, so Gemma, Qwen and gpt-oss appear to lead small open weights (interpretation from one API listing: https://huggingface.co/api/models?author=meta-llama&sort=createdAt&direction=-1).
- **Date.** Gemma 4 Mar 2026; Qwen3.8 Aug 2026; Apple WWDC26 (2026; iOS 27 and macOS 27); Haiku 5.5 Oct 2026; Chrome APIs since 2025.
- **Maturity.** Server-side small models: production for classification, extraction, routing, tagging. On-device: usable (small windows, Apple-only or Chrome-only).
- **Typical cost.** [ESTIMATE] $0.00055 per 3k/500 call on Haiku 5.5; $0 marginal on device or on Apple PCC under the free allowance.
- **Key vendors / APIs.** Anthropic Haiku 5.5, OpenAI Luna/nano, Gemini Flash-Lite, DeepSeek, Groq, Together, DeepInfra, Apple Foundation Models, Chrome built-in AI, Gemma/Qwen/gpt-oss weights.
- **Patterns for an app-layer startup** (interpretation).
  1. iOS apps in privacy-sensitive categories (health logs, journaling, personal finance) with AI features that cost nothing to run per user (on-device and PCC), marketed on privacy. Limits: Apple-only, 8K on-device context, entitlement for PCC.
  2. Router architecture: Haiku-class for most calls, escalation to Sonnet/Opus for hard cases. At 300 calls per user per month the cost is about $0.17 on Haiku 5.5, which makes freemium viable.
  3. Browser extensions that use Chrome's Summarizer, Translator or Prompt API for zero server cost (Chrome only; hardware requirements unverified).
- **Watch-outs.** Haiku 5.5 runs adaptive thinking by default (effort `medium`), so output tokens can be several times the visible answer unless effort is lowered [SKILL-DOC: bundled `shared/models.md`]. Apple's and Google's OS-level features cover the generic cases (summaries, translation, rewrite).

### 6. Tool use, MCP, apps inside assistants, agent SDKs

- **What changed.**
  - MCP was donated to the Agentic AI Foundation, a directed fund under the Linux Foundation, in Dec 2025 [SNIPPET: https://campustechnology.com/Articles/2025/12/15/Newly-Launched-Agentic-AI-Foundation-Brings-Together-Tech-Giants-for-Open-Source-AI-Development.aspx, https://www.ciodive.com/news/big-tech-develop-open-standards-agentic-ai/807608/].
  - Adoption [JSON, 2026-10-31]: npm `@modelcontextprotocol/sdk` 258,265,500 downloads in the 30 days to 2026-10-29 versus 33,786,684 in Oct 2025, about 7.6x (https://api.npmjs.org/downloads/point/last-month/@modelcontextprotocol/sdk, https://api.npmjs.org/downloads/point/2025-10-01:2025-10-31/@modelcontextprotocol/sdk). PyPI `mcp` 235,193,557 in the last month (https://pypistats.org/api/packages/mcp/recent). For scale, npm `openai` 168M and `@anthropic-ai/sdk` 185M, PyPI `openai` 296M and `anthropic` 150M per month. Downloads include CI and mirrors, so read as direction, not users.
  - Agent SDKs [JSON, PyPI last month]: `claude-agent-sdk` 29.8M, `openai-agents` 12.4M, `google-adk` 10.1M (https://pypistats.org/api/packages/claude-agent-sdk/recent, https://pypistats.org/api/packages/openai-agents/recent, https://pypistats.org/api/packages/google-adk/recent).
  - ChatGPT apps: the Apps SDK is built on MCP and open source; developers can submit apps; as of 2026-07-09 the app directory migrated into a "Plugin directory" shared by ChatGPT and Codex; Instant Checkout is beta for select partners only, so external checkout is required otherwise [SNIPPET: https://openai.com/index/introducing-apps-in-chatgpt/, https://openai.com/index/developers-can-now-submit-apps-to-chatgpt/, https://developers.openai.com/apps-sdk/app-submission-guidelines, https://developers.openai.com/apps-sdk/build/monetization].
  - Claude: skills, connectors and plugins share one directory; a plugin developer portal opened 2026-09-25; Salesforce in Claude (beta, 2026-09-15) and Microsoft 365 write tools (2026-07-07) [PAGE: https://support.claude.com/en/articles/12138966-release-notes; SNIPPET: https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory].
  - Gemini: "Connected Apps" link Airtable, Linear and Adobe inside Gemini [PAGE: https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-september-2026/].
  - API side: strict tool schemas, tool search, programmatic tool calling, server-side web search/fetch and code execution; Managed Agents bill $0.08 per session-hour plus tokens (official worked example: a 1-hour Opus 5.5 session with 50K in / 15K out is $0.58) [PAGE: https://platform.claude.com/docs/en/about-claude/pricing; SKILL-DOC for feature list]. Tool use adds a fixed system prompt of 286 tokens on the 5.5 models [PAGE].
- **Date.** Apps SDK Oct 2025; MCP to Linux Foundation Dec 2025; directories and plugin portals Jul to Sep 2026.
- **Maturity.** Tool calling: production. MCP: production for developer and workplace tools. Assistant app stores as a distribution channel: early and shifting (directory renames, Instant Checkout limited, Atlas shutdown).
- **Typical cost.** Tokens only. Tool definitions and results are the main cost; use caching and tool search.
- **Key vendors / APIs.** MCP SDKs, OpenAI Apps SDK and Agents SDK, Claude Agent SDK and Managed Agents, Google ADK.
- **Patterns for an app-layer startup** (interpretation).
  1. Ship the product as an MCP server plus assistant app (ChatGPT, Claude, Gemini), letting the assistant be the UI; monetize outside the assistant because in-chat checkout is not generally available.
  2. Profession-specific bundles of skills, connectors and plugins (legal, accounting, clinical admin) distributed through the Claude directory and ChatGPT plugin directory.
  3. Approval and audit layer for agent actions (who approved what, replay, undo) for small businesses that let agents write to real systems. [Competition not checked.]
- **Watch-outs.** Distribution inside assistants can be re-platformed by the assistant owner (the ChatGPT app directory became a plugin directory within months).

### 7. Memory and personalization

- **What changed.**
  - Claude: memory rewritten as categorized, editable entries (2026-07-10); monthly recap under Settings > Reflect (2026-07-09); memory spans chat and cloud Cowork with editable topics and an opt-in for sensitive topics (2026-08-25) [PAGE: https://support.claude.com/en/articles/12138966-release-notes; SNIPPET: https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context].
  - Gemini: Personal Intelligence connects Gmail, Photos, YouTube and other Google apps (off by default; launched as a U.S. beta for AI Pro and Ultra); memory of past chats is a separate setting; tools import memories and full chat history from other AI apps [SNIPPET: https://blog.google/innovation-and-ai/products/gemini-app/personal-intelligence/, https://blog.google/innovation-and-ai/products/gemini-app/switch-to-gemini-app/].
  - Microsoft: long-term memory lets Copilot reference past chats on desktop and mobile (May 2026); an always-on cloud personal agent called Autopilot with persistent context and memory is described in the October 2026 Copilot update [SNIPPET: https://blogs.windows.com/msedgedev/2026/05/13/new-updates-to-edge-across-desktop-and-mobile/, https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/what%E2%80%99s-new-in-microsoft-copilot--october-2026/4568528].
  - ChatGPT memory: not verified in this track [UNVERIFIED].
  - For builders: Anthropic's memory tool (`memory_20250818`) and Managed Agents memory stores (beta `agent-memory-2026-07-22`) [SKILL-DOC: docs https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool].
- **Date.** Jul to Oct 2026 for the newest versions.
- **Maturity.** Production inside assistants. For app developers: usable (files or database plus a memory tool).
- **Typical cost.** Negligible if memory is structured notes of a few hundred tokens per turn, cached.
- **Patterns for an app-layer startup** (interpretation).
  1. Domain memory that assistants lack: per-client, per-patient or per-case memory with provenance, permissions and export, exposed over MCP so any assistant can use it.
  2. First-party preference learning inside a vertical app (coaching, shopping, scheduling) using data the assistants cannot see.
  3. Avoid: generic "memory layer for chat". It is native everywhere and Google even ships importers from rivals.

### 8. Document understanding, OCR, structured outputs, image/video/music generation

- **What changed.**
  - Documents: Claude accepts PDFs of up to 600 pages per request (100 for 200K-window models) and 32 MB, with citations and structured outputs via `output_config.format` and strict tools [SKILL-DOC: bundled SKILL.md; docs https://platform.claude.com/docs/en/build-with-claude/pdf-support, https://platform.claude.com/docs/en/build-with-claude/structured-outputs]. Mistral OCR 4 (announced 2026-06-23, 4.1 on 2026-08-13) is $4 per 1,000 pages, $2 batch, and Document AI with annotations $5 [3P, [UNVERIFIED]: https://tech-insider.org/mistral-ocr-4-launch-2026/, https://pasqualepillitteri.it/en/news/11041/mistral-ocr-4-1-bounding-boxes-marked-up-pages]. Apple's on-device model has OCR and barcode tools [PAGE].
  - Images: OpenAI `gpt-image-2` / `2.5` are token-priced ($8 in / $30 out per 1M image tokens; page gives no per-image price); Google's Nano Banana line is priced per image, about $0.034 (Nano Banana 2.1, 1K), $0.067 (Nano Banana 2, 1K), $0.134 (Nano Banana Pro, 1K/2K) [PAGE: pricing pages].
  - Video: Gemini Omni Flash outputs video at $17.50 per 1M tokens, about $0.10 per second of 720p video [PAGE: https://ai.google.dev/gemini-api/docs/pricing]. OpenAI's Sora consumer app closed 2026-04-26 and the Sora API was scheduled to end 2026-09-24 [3P: https://dev.to/mr_manushukla/sora-2-and-the-videos-api-shut-down-on-24-september-2026-the-migration-and-the-real-cost-per-second-bek, https://ecorpit.com/sora-2-videos-api-shutdown-migration-cost-2026/].
  - Music: Lyria 3.5 is available in Gemini, AI Studio, Flow Music and Vids [PAGE: https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-september-2026/]; ElevenLabs Music is $0.15 per minute [PAGE: https://elevenlabs.io/pricing/api].
- **Date.** 2026 for the current generation.
- **Maturity.** Extraction and OCR: production (with a verification UI). Image generation: production. Video: usable but pricey and platform-volatile. Music: usable.
- **Typical cost.** [ESTIMATE, cheat sheet G] 10,000 pages: $40 on Mistral OCR 4 ($20 batch) versus about $6.50 on Haiku 5.5 (1,500 image tokens + 1,000 output tokens per page, quality untested) versus $130 on Sonnet 5.5.
- **Patterns for an app-layer startup** (interpretation).
  1. Messy vertical paperwork to system-of-record pipelines (customs, permits, lab and inspection reports, rent rolls, bills of lading) with exceptions queue and human verification.
  2. Photo or video of a real-world object to structured data (inventory, damage, compliance evidence).
  3. Generated media inside a vertical workflow only with a sharp wedge. Generic image, video and music generators are a MISSION red zone and Sora's exit shows the economics.

### 9. Deep research and web-search APIs

- **What changed.**
  - First-party search tools: Anthropic web search $10 per 1,000 searches plus tokens, web fetch with no extra charge, and code execution free when used with web search/fetch [PAGE: https://platform.claude.com/docs/en/about-claude/pricing]; OpenAI web search $10 per 1,000 calls plus content tokens, `gpt-5-search-api` $1.25/$10 per 1M [PAGE: https://developers.openai.com/api/docs/pricing]; Google "Grounding with Google Search" free for the first 5,000 requests per month on Gemini 3 and newer, then $14 per 1,000 (Gemini 2.5: $35 per 1,000 grounded prompts) [PAGE: https://ai.google.dev/gemini-api/docs/pricing]; DeepSeek search and fetch $0.75 per 1,000 successful requests, billing from 2026-11-01 [PAGE: https://api-docs.deepseek.com/quick_start/pricing].
  - Independent search APIs (all [3P], [UNVERIFIED]): Brave $5 per 1,000, Perplexity Search API $5 per 1,000 with a "Fast Search" at $1 per 1,000 (Sep 2026), Exa about $7 per 1,000, Tavily $5 to $8 per 1,000, Parallel $5 per 1,000 [https://nesyona.com/articles/ai-web-search-tool-prices-per-1000-calls-2026, https://www.usagepricing.com/blueprint/activity/perplexity-ai-2026-09-28-search-api-fast-search, https://dev.to/team_metabees_4b5127db951/7-cheapest-web-search-apis-for-ai-agents-in-2026-ranked-76m].
  - Deep research as an API (all [3P], [UNVERIFIED]): Gemini Deep Research and Deep Research Max in the Interactions API (public preview; about $1 to $3 and $3 to $7 per task, billed at Gemini 3.1 Pro token rates plus $14 per 1,000 grounding queries); OpenAI `o3-deep-research` at $10/$40 per 1M tokens, with thorough tasks reported at $10 to $30; Perplexity Sonar Deep Research $2/$8 per 1M; Parallel Task API $100 per 1,000 queries [https://tokencost.app/blog/gemini-deep-research-agent-cost, https://www.linkup.so/blog/best-deep-research-api-in-2026-openai-gemini-and-linkup-compared, https://parallel.ai/articles/best-deep-research-apis].
- **Date.** Interactions-API deep research previews in 2026 (April 21 or July 7, sources conflict).
- **Maturity.** Search tools: production. Deep research APIs: usable, previews, prices unstable.
- **Typical cost.** [ESTIMATE, cheat sheet F] 1,000 searches: $10 (Anthropic/OpenAI tools) or $14 (Google after the free quota), plus result tokens that can match or exceed the search fee (5 results x 1K tokens each is $10 more per 1,000 searches on Sonnet 5.5).
- **Patterns for an app-layer startup** (interpretation).
  1. Recurring monitors on niche sources (regulatory notices, tenders, competitor pages) that deliver diffs and alerts instead of reports.
  2. Per-report research packs for a vertical decision (supplier due diligence, grant or permit lookup) priced at $5 to $50 per report against $1 to $7 of API cost.
  3. Citation and claim verification as a trust layer on top of whatever model drafted the research.

### 10. Combinations that are newly cheap (interpretation)

- Voice + screen + tools: a phone-based or desktop coach that sees the screen (about $0.002/min of image/video on Gemini Live), talks (about $0.02/min of audio) and writes to a system of record via MCP, for roughly $0.05 to $0.15/min before LLM tool calls. [ESTIMATE]
- Haiku-class + caching + batch: "process everything" jobs (every email, call, invoice) at fractions of a cent each, which turns back-office backlogs into subscription products.
- On-device first: free inference for the common path, with server escalation for hard cases.

## What the big assistants already do natively

Dated list of shipped features that define what an application-layer startup should NOT build as its core. Interpretation in the last column.

| Assistant | Feature (date) | Evidence | Overlaps with |
|---|---|---|---|
| ChatGPT | ChatGPT Work: agent that takes action across apps and files and works for hours, producing sheets, slides, docs and web apps (announced 2026-07-09; Pro/Enterprise/Edu first, Plus/Business after) | [SNIPPET: https://openai.com/index/chatgpt-for-your-most-ambitious-work/] | generic back-office agents, doc/deck generators |
| ChatGPT | Desktop app with built-in browser, cloud browser, Codex merged in; Atlas browser retired 2026-08-09 | [SNIPPET: https://www.macrumors.com/2026/07/10/openais-chatgpt-atlas-browser-shutting-down/] | agent browsers, coding+browse combos |
| ChatGPT | GPT-5.6 Sol/Terra/Luna selectable with effort levels; Luna for free users; GPT-6 family in the API | [SNIPPET: https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/; PAGE pricing] | model-choice wrappers |
| ChatGPT | Apps/plugins directory (apps built on MCP; submissions; directory migrated to Plugin directory 2026-07-09); Instant Checkout in beta for select partners | [SNIPPET: https://help.openai.com/en/articles/20001040-submitting-apps-to-the-chatgpt-app-directory, https://developers.openai.com/apps-sdk/app-submission-guidelines] | integrations, shopping |
| ChatGPT | Personal finance experience (rolling out 2026-05-15 per release notes), ads on Free and Go plans (Apr 2026), GPT-5.5 Instant default (May 2026) | [3P, [UNVERIFIED]: https://www.gend.co/blog/chatgpt-2026-latest-features, https://blog.memoryplugin.com/chatgpt-new-features-october-2026/] | personal finance chat |
| ChatGPT | Voice: "GPT Live" (`gpt-live-1`) billed at $0.05/min in the API | [PAGE pricing note; SNIPPET: https://developers.openai.com/api/docs/guides/voice-sip] | voice assistants |
| Claude | Cowork in every conversation: no mode selection, shared projects, connectors, skills (2026-09-16); Cowork on web and mobile with remote sessions (2026-07-07); Cowork in the Chrome side panel | [PAGE: https://support.claude.com/en/articles/12138966-release-notes; SNIPPET: https://claude.com/blog/cowork-chrome-side-panel] | generic task agents, browser agents |
| Claude | Designs, decks and docs in any chat (2026-09-16); edit drafts in place (2026-06-12) | [PAGE release notes] | doc, slide, report generators |
| Claude | Memory as categorized entries (2026-07-10), memory in Cowork (2026-08-25), monthly recap (2026-07-09) | [PAGE release notes] | memory layers |
| Claude | Microsoft 365 write tools (2026-07-07), Salesforce in Claude with 37 sales skills (2026-09-15), Claude Tag in Slack (2026-06-23) | [PAGE release notes] | thin connectors to big SaaS |
| Claude | Claude Duet, a proactive agent app (research preview, Pro and Max, 2026-10-21); WebFetch extract: "Claude Duet, a new app where Claude works as a proactive agent." | [PAGE release notes] | proactive/ambient assistants |
| Gemini | Gemini 4 Argon in the Gemini app with a toggle from chat to tasks; tasks can run when you are away; connects to 40+ apps (GA Oct 13, 2026) | [SNIPPET: https://blog.google/innovation-and-ai/products/gemini-app/gemini-4-argon-availability/] | task agents |
| Gemini | Gemini Spark on Windows (delegate multi-step tasks), Connected Apps (Airtable, Linear, Adobe), CC for groups (household agent with its own email, Labs) | [PAGE: https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-september-2026/] | household and work logistics agents |
| Gemini | Gemini 3.8 Live across Search Live, Gemini Live and Workspace; voice in Gmail, Docs, Keep; Rambler dictation to notes on Googlebook | [PAGE, same] | voice assistants, dictation/notes |
| Gemini | Magic Pointer: "point and ask Gemini about anything on your screen with a quick cursor wiggle" (Googlebook, pre-order) | [PAGE, same] | screen assistants |
| Gemini | Lyria 3.5 music, Nano Banana images, Gemini Omni video, Flash TTS, Gemini Notebook study tools (flashcards, quizzes, 60-second video overviews) | [PAGE, same] | media generators, study tools |
| Gemini | Personal Intelligence (connected Google apps) and memory/chat-history import from other assistants | [SNIPPET: https://blog.google/innovation-and-ai/products/gemini-app/personal-intelligence/, https://blog.google/innovation-and-ai/products/gemini-app/switch-to-gemini-app/] | personal context, memory portability |
| Microsoft Copilot | Copilot Vision (screen share) on Windows, Edge, mobile with Microsoft 365 Personal/Family/Premium; hands-free browsing with Voice and Vision; long-term memory (May 2026); Browse with Copilot (U.S., Premium); Autopilot always-on personal agent (Oct 2026); Microsoft 365 Copilot analyzing screen share and camera (Sep 2026) | [SNIPPET: https://blogs.windows.com/msedgedev/2026/05/13/new-updates-to-edge-across-desktop-and-mobile/, https://support.microsoft.com/en-au/topic/using-copilot-vision-with-microsoft-copilot-3c67686f-fa97-40f6-8a3e-0e45265d425f, https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/what%E2%80%99s-new-in-microsoft-copilot--october-2026/4568528] | screen help, browse agents, work agents |
| Apple Intelligence / Siri | Foundation Models framework for developers: on-device model, PCC model, third-party providers (WWDC26) | [PAGE: https://developer.apple.com/videos/play/wwdc2026/241/] | on-device AI wrappers |
| Apple Intelligence / Siri | Rebuilt Gemini-based Siri in iOS 27, reportedly released 2026-09-14, with personal context, on-screen awareness and a standalone Siri app; some features may be labeled beta | [3P, [UNVERIFIED]: https://www.freepressjournal.in/amp/tech/apple-event-2026-ios-27-announced-rollout-date-compatible-devices-whats-new, https://iphonelife.com/content/siri-ai-announced] | iPhone voice/agent assistants |

**Do NOT build as the core product** (interpretation from the table above)
1. A general browser or computer-use agent that "does tasks on the web for you". Four vendors ship it and OpenAI retired its own standalone browser.
2. A general personal agent for email, calendar, errands or household logistics, including proactive or always-on variants (Claude Duet, Gemini tasks and CC for groups, Copilot Autopilot, ChatGPT Work).
3. Document, slide, spreadsheet or report generation as the product (Claude designs/decks/docs, ChatGPT Work).
4. A generic "sees your screen and helps" overlay for mainstream apps (Copilot Vision, Magic Pointer, Gemini Live).
5. A generic memory or "second brain" layer for chat (native in all four, with importers).
6. A general voice assistant, translator or dictation tool (Gemini 3.8 Live, Live Translate, Rambler, ChatGPT voice).
7. Thin connectors to Microsoft 365, Salesforce, Slack or Google apps (vendors build them natively).
8. Plain transcription, OCR or summarization wrappers (transcription is $0.003 to $0.006/min, OCR is about $2 to $4 per 1,000 pages [3P], and OS and browser features are free).
9. Image, video or music generators (Nano Banana, Omni, Lyria in the Gemini app; Sora's exit shows the unit economics).

**What the assistants do not do (candidate gaps)** (interpretation, not verified as whitespace)
- Vertical depth with audit and liability: evidence-linked outputs, approval workflows, retention rules, domain-specific evals.
- Phone-based real-world actions under business-specific policies, with write-back to niche systems of record.
- Multi-party workflows (customer, vendor, regulator) and long-lived case state.
- Offline, on-device or data-residency-constrained use (Apple FM, local open weights).
- Hardware-free field work combining voice, camera and domain checklists.

## Price table

All prices are USD per 1M tokens unless noted, list prices, pay-as-you-go, **read on 2026-10-31**. Taxes, volume discounts and reseller markups excluded. Regional or data-residency uplifts: Anthropic US-only inference x1.1 on all token categories; OpenAI regional processing +10% for models released on or after 2026-03-05. Reasoning or thinking tokens are billed as output tokens (Google's page labels its output price "incl. thinking"). Claude 4.7 and later models count about 30% more tokens for the same text than earlier Claude models (Anthropic's pricing page), so compare vendors on cost per task, not per token.

### Anthropic (Claude)
Source: https://platform.claude.com/docs/en/about-claude/pricing [PAGE, read 2026-10-31]. Cross-checked against LiteLLM for 6 rows [3P].

| Model | Input | Output | Cache read | Cache write 5m / 1h | Batch in / out | Notes |
|---|---|---|---|---|---|---|
| Claude Fable 5.1 | $10 | $50 | $0.25 | $12.50 / $20 | $5 / $25 | Most capable widely released model; 1M context |
| Claude Mythos 5.1 | $10 | $50 | $0.25 | $12.50 / $20 | $5 / $25 | Limited availability (verified orgs only) |
| Claude Fable 5 | $10 | $50 | $1.00 | $12.50 / $20 | $5 / $25 | Still listed |
| Claude Opus 5.5 | $4 | $20 | $0.20 | $5 / $8 | $2 / $10 | Fast mode $8 / $40 |
| Claude Opus 5 | $5 | $25 | $0.50 | $6.25 / $10 | $2.50 / $12.50 | Fast mode $10 / $50 |
| Claude Opus 4.8, 4.7, 4.6, 4.5 | $5 | $25 | $0.50 | $6.25 / $10 | $2.50 / $12.50 | Opus 4.8 fast mode $10 / $50 |
| Claude Sonnet 5.5 | $2 | $10 | $0.10 | $2.50 / $4 | $1 / $5 | |
| Claude Sonnet 5 | $2 | $10 | $0.20 | $2.50 / $4 | $1 / $5 | Intro price made permanent; the planned rise to $3/$15 will not occur |
| Claude Sonnet 4.6, 4.5 | $3 | $15 | $0.30 | $3.75 / $6 | $1.50 / $7.50 | |
| Claude Haiku 5.5 (prompt up to 100K tokens) | $0.10 | $0.50 | $0.01 | $0.125 / $0.20 | $0.05 / $0.25 | 1M context; adaptive thinking on by default [SKILL-DOC] |
| Claude Haiku 5.5 (prompt over 100K tokens) | $0.50 | $2.50 | $0.05 | $0.625 / $1 | $0.25 / $1.25 | Whole request is repriced, cache reads count toward the threshold |
| Claude Haiku 4.5 | $1 | $5 | $0.10 | $1.25 / $2 | $0.50 / $2.50 | |
| Legacy | Opus 4.1 and Opus 4 $15 / $75; Sonnet 4 $3 / $15; Haiku 3.5 $0.80 / $4 | | | | | Retired on the first-party API except on Bedrock or Google Cloud, per the page |

Tools (same page): web search $10 per 1,000 searches; web fetch no extra charge; code execution free with web search/fetch, otherwise 1,550 free hours per month then $0.05 per hour per container; Managed Agents $0.08 per session-hour plus tokens; computer toolset about 4,500 input tokens per request, browser toolset about 6,600; tool-use system prompt 286 tokens on the 5.5 models.

### OpenAI text models
Source: https://developers.openai.com/api/docs/pricing [PAGE via WebFetch small-model summary, read 2026-10-31; 8 headline rows matched LiteLLM]. "Long" = prompts over 272K tokens. The page does not label tiers mini/nano for the GPT-6 family; the tier mapping in the first column is my reading [ASSUMPTION].

| Model (my tier reading) | Input | Cached input | Output | Long in / out | Batch in / out |
|---|---|---|---|---|---|
| gpt-6-astra (top tier) | $10.00 | $1.00 | $50.00 | $20 / $75 | $5 / $25 |
| gpt-6.1-sol (flagship workhorse) | $2.00 | $0.10 | $10.00 | $4 / $15 | $1 / $5 |
| gpt-6-sol | $2.00 | $0.20 | $10.00 | $4 / $15 | $1 / $5 |
| gpt-6.1-terra (mid, mini-class) | $1.00 | $0.05 | $5.00 | $2 / $7.50 | $0.50 / $2.50 |
| gpt-6-luna (small, nano-class) | $0.10 | $0.01 | $0.50 | $0.20 / $0.75 | $0.05 / $0.25 |
| gpt-5.6-sol (promo through at least 2026-11-21) | $4.00 | $0.40 | $20.00 | $8 / $30 | $2 / $10 |
| gpt-5.6-terra | $2.00 | $0.20 | $12.00 | $4 / $18 | $1 / $6 |
| gpt-5.6-luna | $0.20 | $0.02 | $1.20 | $0.40 / $1.80 | $0.10 / $0.60 |
| gpt-5.5 | $5.00 | $0.50 | $30.00 | $10 / $45 | $2.50 / $15 |
| gpt-5.4 | $2.50 | $0.25 | $15.00 | $5 / $22.50 | $1.25 / $7.50 |
| gpt-5.4-mini | $0.75 | $0.075 | $4.50 | | $0.375 / $2.25 |
| gpt-5.4-nano | $0.20 | $0.02 | $1.25 | | $0.10 / $0.625 |
| gpt-5-mini | $0.25 | $0.025 | $2.00 | | $0.125 / $1.00 |
| gpt-5-nano | $0.05 | $0.005 | $0.40 | | $0.025 / $0.20 |
| gpt-4.1-nano | $0.10 | $0.025 | $0.40 | | $0.05 / $0.20 |
| gpt-4o-mini | $0.15 | $0.075 | $0.60 | | $0.075 / $0.30 |

Other lines on the page: pro tiers (gpt-5.5-pro and gpt-5.4-pro $30 / $180; gpt-5.2-pro $21 / $168; gpt-5-pro $15 / $120); "Fast" (renamed from Priority on 2026-07-30) is roughly 2x standard (for example gpt-6.1-sol $4 / $20, gpt-6-luna $0.20 / $1.00); Flex matches Batch prices; fine-tuning is being wound down. Web search $10 per 1,000 calls plus content tokens (non-reasoning "preview" search $25 per 1,000 with free content tokens); file search $2.50 per 1,000 calls; containers from $0.03 per 1 GB per 20-minute session; `gpt-5-search-api` $1.25 / $10.

### OpenAI realtime, audio, image, speech
Same source and date.

| Model | Audio in / cached / out | Text in / cached / out | Image in / cached |
|---|---|---|---|
| gpt-realtime-2.1 (also 2) | $32.00 / $0.40 / $64.00 | $4.00 / $0.40 / $24.00 | $5.00 / $0.50 |
| gpt-realtime-2.1-mini | $10.00 / $0.30 / $20.00 | $0.60 / $0.06 / $2.40 | $0.80 / $0.08 |
| gpt-realtime-1.5 | $32.00 / $0.40 / $64.00 | $4.00 / $0.40 / $16.00 | $5.00 / $0.50 |
| gpt-audio, gpt-audio-1.5 | $32.00 / n.a. / $64.00 | $2.50 / n.a. / $10.00 | |
| gpt-audio-mini | $10.00 / n.a. / $20.00 | $0.60 / n.a. / $2.40 | |

- GPT Live: `gpt-live-1` sessions billed at $0.05 per minute (page note; also in a third-party comparison page seen in search results, [3P]).
- Transcription: `gpt-transcribe` $0.0045/min; `gpt-4o-mini-transcribe` $0.003/min; `gpt-4o-transcribe` $0.006/min; Whisper $0.006/min; live `gpt-live-transcribe` and `gpt-realtime-whisper` $0.017/min; `gpt-realtime-translate` $0.034/min.
- TTS: `gpt-4o-mini-tts` $0.60 per 1M text tokens in and $12.00 per 1M audio tokens out (about $0.015/min per OpenAI's 2025 launch post, [ASSUMPTION], not re-verified); `tts-1` $15 per 1M characters; `tts-1-hd` $30 per 1M characters.
- Images: `gpt-image-2` and `gpt-image-2.5-*` image tokens $8 in / $30 out (cached $2), text in $5; `gpt-image-1-mini` image $2.50 in / $8 out; no per-image prices on the page. Embeddings: `text-embedding-3-small` $0.02, `-large` $0.13. Sora is not listed.

### Google (Gemini API)
Source: https://ai.google.dev/gemini-api/docs/pricing [PAGE, "Last updated 2026-10-30 UTC", read 2026-10-31]. Cross-checked against LiteLLM for 6 rows [3P] and, for Argon and 3.8 Flash, against third-party coverage. Format "now, then later" shows the page's price change at the cutoff (Argon Nov 30, 2026; other models Dec 31, 2026). **Budget on the later price.**

| Model | Input | Output (incl. thinking) | Cache read | Batch in / out | Notes |
|---|---|---|---|---|---|
| Gemini 4 Argon | $2.00, then $4.00 | $10.00, then $20.00 | $0.10, then $0.20 (implicit only) | $1 / $5, then $2 / $10 | Frontier; no free tier |
| Gemini 3.1 Pro Preview | $2.00 (up to 200K), $4.00 (over) | $12.00 / $18.00 | $0.20 / $0.40 | $1.00 / $6.00 (up to 200K) | Preview |
| Gemini 2.5 Pro | $1.25 / $2.50 | $10.00 / $15.00 | $0.125 / $0.25 | $0.625 / $5.00 | |
| Gemini 3.8 Flash | $0.75, then $1.50 | $3.75, then $7.50 | $0.075, then $0.15 | $0.375 / $1.875, then double | Free tier available |
| Gemini 3.6 Flash (previous gen) | $0.75, then $1.50 | $3.75, then $7.50 | $0.075, then $0.15 | same as 3.8 Flash | |
| Gemini 3 Flash Preview (legacy) | $0.50 | $3.00 | $0.05 | $0.25 / $1.50 | |
| Gemini 2.5 Flash | $0.30 (audio $1.00) | $2.50 | $0.03 | $0.15 / $1.25 | |
| Gemini 3.5 Flash-Lite | $0.30 | $2.50 | $0.03 | $0.15 / $1.25 | |
| Gemini 3.1 Flash-Lite | $0.25 (audio $0.50) | $1.50 | $0.025 | $0.125 / $0.75 | |
| Gemini 2.5 Flash-Lite | $0.10 (audio $0.30) | $0.40 | $0.01 | $0.05 / $0.20 | Cheapest Gemini text tier listed |
| Gemma 4 | free tier only | free tier only | | | No paid tier on the page |

Other Google lines on the page:
- Grounding with Google Search: first 5,000 requests per month free on Gemini 3 and newer, then $14 per 1,000 (default cap 1,500 per day); Gemini 2.5: $35 per 1,000 grounded prompts.
- Live API: Gemini 3.8 Live audio in $3.00 (about $0.005/min), audio out $12.00 (about $0.018/min), text in $0.75 / out $4.50, image or video in $1.00 (about $0.002/min). Gemini 2.5 Flash Native Audio audio $3.00 in / $12.00 out. Gemini 3.5 Live Translate audio in $3.50 (about $0.0053/min), out $21.00 (about $0.0315/min).
- Transcription: Gemini 3.5 Transcribe audio in $2.00 (about $0.003/min) plus text out $12.00 (about $0.002/min), so about $0.005/min; Transcribe Live audio in about $0.005/min plus text out about $0.004/min.
- TTS (25 audio tokens per second): Gemini 3.8 Flash TTS audio out $9.00, then $18.00 ($0.00225 then $0.0045 per 10 s); Flash-Lite TTS $6.00, then $12.00 ($0.0015 then $0.003 per 10 s).
- Images per image: Nano Banana 2.1 about $0.0336 (1K), $0.0504 (2K), $0.113 (4K); Nano Banana 2 about $0.067 (1K), $0.101 (2K), $0.151 (4K); Nano Banana Pro about $0.134 (1K/2K), $0.24 (4K); Nano Banana (2.5 Flash Image) $0.039, deprecated, shutdown 2027-03-15.
- Video: Gemini Omni Flash video output $17.50 per 1M tokens, about $0.10 per second of 720p video. No Veo prices on the page.
- Embeddings: `gemini-embedding-2` text $0.20; `gemini-embedding-001` $0.15.
- Free-tier content may be used to improve Google's products; the page says paid tiers are not.

### Budget open-model hosts

| Host and model | Input | Output | Cached input | Source and tag |
|---|---|---|---|---|
| DeepSeek `deepseek-flash` (V4.1-Flash-1017), 1M context, vision | $0.15 off-peak / $0.30 peak | $0.60 / $1.20 | $0.003 / $0.006 | https://api-docs.deepseek.com/quick_start/pricing [PAGE] |
| DeepSeek `deepseek-v4-pro` (V4-Pro-0813), 1M context, no vision | $0.66 / $1.32 | $1.98 / $3.96 | $0.022 / $0.044 | same [PAGE] |
| Groq `openai/gpt-oss-120b` | $0.15 | $0.60 | $0.075 | https://console.groq.com/docs/model/openai/gpt-oss-120b [SNIPPET of GroqDocs; LiteLLM agrees] |
| Groq `openai/gpt-oss-20b` | $0.075 | $0.30 | $0.037 | https://console.groq.com/docs/model/openai/gpt-oss-20b [SNIPPET; LiteLLM agrees] |
| Together `gpt-oss-20b` / `gpt-oss-120b` | $0.05 / $0.15 | $0.20 / $0.60 | | LiteLLM JSON [3P, [UNVERIFIED]]; official page https://www.together.ai/pricing not opened |
| Together `DeepSeek-V4-Flash-0731` (1M ctx) | $0.14 | $0.28 | | LiteLLM [3P, [UNVERIFIED]] |
| DeepInfra `gemma-4-E4B-it` | $0.02 | $0.10 | | LiteLLM [3P, [UNVERIFIED]] |
| DeepInfra `gpt-oss-120b` | $0.037 | $0.17 | | LiteLLM [3P, [UNVERIFIED]] |

DeepSeek peak hours are 01:00 to 04:00 and 06:00 to 10:00 UTC, Monday to Friday, excluding Chinese public holidays; off-peak is half price [PAGE]. DeepSeek search and fetch are $0.75 per 1,000 successful requests each, billed from 2026-11-01.

### Speech: transcription (STT)

| Vendor and model | Price | Source and tag |
|---|---|---|
| Deepgram Nova-3 streaming (mono / multilingual) | $0.0077 / $0.0092 per min (Growth $0.0065 / $0.0078) | https://deepgram.com/pricing [PAGE] |
| Deepgram Nova-3 pre-recorded (mono / multilingual) | $0.0043 / $0.0052 per min | same [PAGE] |
| Deepgram Flux STT English streaming | $0.0077 per min | same [PAGE] |
| OpenAI `gpt-4o-mini-transcribe` | $0.003 per min | https://developers.openai.com/api/docs/pricing [PAGE] |
| OpenAI `gpt-transcribe` / `gpt-4o-transcribe` / Whisper | $0.0045 / $0.006 / $0.006 per min | same [PAGE] |
| OpenAI live transcription (`gpt-live-transcribe`, `gpt-realtime-whisper`) | $0.017 per min | same [PAGE] |
| ElevenLabs Scribe v2 / Scribe v2 Realtime | $0.22 / $0.39 per hour ($0.0037 / $0.0065 per min) | https://elevenlabs.io/pricing/api [PAGE] |
| Google Gemini 3.5 Transcribe | about $0.005 per min (audio in $0.003 + text out $0.002) | https://ai.google.dev/gemini-api/docs/pricing [PAGE] |
| AssemblyAI | not verified; aggregator values looked inconsistent | [UNVERIFIED] |

### Speech: synthesis (TTS) and voice-agent platforms

| Vendor and model | Price | Source and tag |
|---|---|---|
| Deepgram Aura-2 / Aura-1 / Flux TTS | $0.030 / $0.015 / $0.045 per 1,000 characters (Growth: $0.027 / $0.0135 / $0.045) | https://deepgram.com/pricing [PAGE] |
| ElevenLabs v4, v3, v2 Multilingual | $0.08 per 1,000 characters | https://elevenlabs.io/pricing/api [PAGE] |
| ElevenLabs v4 Turbo, v3 Conversational, Flash/Turbo | $0.04 per 1,000 characters | same [PAGE] |
| OpenAI `tts-1` / `tts-1-hd` | $15 / $30 per 1M characters ($0.015 / $0.030 per 1,000) | https://developers.openai.com/api/docs/pricing [PAGE] |
| OpenAI `gpt-4o-mini-tts` | about $0.015 per min | [ASSUMPTION], from OpenAI's 2025 launch, not re-verified |
| Google Gemini 3.8 Flash-Lite TTS / Flash TTS | $0.009 / $0.0135 per min now (double after Dec 31) | https://ai.google.dev/gemini-api/docs/pricing [PAGE], derived from per-10-second prices |
| Cartesia, others | not checked | [NOT CHECKED] |
| Deepgram Voice Agent API | $0.075/min Standard (STT + LLM + TTS); $0.065 BYO TTS; $0.065 BYO LLM; $0.050 BYO LLM and TTS; Advanced $0.163 | https://deepgram.com/pricing [PAGE] |
| ElevenLabs Agents ("Speech Engine") | $0.08/min (burst $0.16/min), LLM tokens extra; the page's "Realtime v1" rows are ambiguous, verify before use | https://elevenlabs.io/pricing/api [PAGE] |
| OpenAI GPT Live (`gpt-live-1`) | $0.05/min | https://developers.openai.com/api/docs/pricing [PAGE] |
| Vapi platform fee $0.05/min, Retell $0.07 to $0.31, Bland $0.11 to $0.14, all-in typically $0.07 to $0.30/min | | [3P, [UNVERIFIED]]: https://www.morphllm.com/best-ai-voice-agent-platforms, https://speechify.ai/blog/best-voice-agent-platforms-2026 |

### Search, browsers and other tools
First-party search prices are in the Anthropic, OpenAI, Google and DeepSeek sections above. Third-party search and research APIs and hosted browsers are summarised in Capability unlocks 9 and 2 (all [3P], [UNVERIFIED]). Mistral OCR 4: $4 per 1,000 pages ($2 batch) [3P, [UNVERIFIED]]. ElevenLabs Music $0.15/min, sound effects $0.12/min [PAGE].

### Batch and caching discounts

| Vendor | Batch | Cache read | Cache write | Source |
|---|---|---|---|---|
| Anthropic | 50% off input and output; stacks with caching and data residency; not available for fast mode | 0.1x input (0.05x Opus 5.5 and Sonnet 5.5; 0.025x Fable 5.1) | 1.25x (5 min), 2x (1 hour) | [PAGE] Anthropic |
| OpenAI | 50% off; Flex tier has Batch prices | 0.1x input on most GPT-6 and 5.x lines (0.05x on gpt-6.1-sol and gpt-6.1-terra; gpt-4.1: 0.25x) | none listed | [PAGE] OpenAI |
| Google | 50% off; Flex tier matches Batch | about 0.1x input (0.05x on Gemini 4 Argon, implicit only); explicit caches add storage fees ($0.50 to $4.50 per 1M tokens per hour on the page) | storage per hour | [PAGE] Google |
| DeepSeek | none listed | about 0.02x input (flash) | none | [PAGE] DeepSeek |
| Groq | not checked | 0.5x input on gpt-oss | | [SNIPPET] |

### Observations on prices (interpretation)
- The small-model floor has barely moved in absolute price since 2025 (gpt-5-nano is still $0.05/$0.40; Haiku 5.5 and Luna are $0.10/$0.50), but capability per dollar has risen. Frontier tiers got cheaper: Opus 4.1 $15/$75 to Opus 5.5 $4/$20 (-73%), Haiku 4.5 $1/$5 to Haiku 5.5 $0.10/$0.50 (-90%), before the ~30% token inflation of the new tokenizer [PAGE].
- Prices are not monotonic: Google's introductory windows end Nov 30 and Dec 31, 2026 (prices double); OpenAI's GPT-5.6 Sol price is promotional; DeepSeek has peak and off-peak rates and starts billing search on Nov 1; Mistral OCR rose from $2 to $4 per 1,000 pages [3P]. Re-check prices before committing to a margin.
- Cheap list prices can hide cost: default thinking (Haiku 5.5 adaptive thinking, medium effort), long-context re-reads, tool overhead (4,500 to 6,600 tokens per request for computer or browser toolsets), and search result tokens.

## Cost cheat sheet

All items [ESTIMATE]. Arithmetic is in a scratch script; prices are from the Price table above (read 2026-10-31). Output tokens are visible output only; reasoning tokens would add to the output line (set effort low for bulk work).

### A. 1,000 calls, each 3,000 input + 500 output tokens
Totals: 3.0M input tokens and 0.5M output tokens. Cost = 3.0 x input price + 0.5 x output price. "Cached prefix" assumes 2,500 of the 3,000 input tokens are a cache hit (cache write premium ignored; one write of 2,500 tokens costs $0.0003 on Haiku 5.5, $0.0063 on Sonnet 5.5).

| Tier | Model | Plain | With 2,500-token cached prefix | Batch (50%) | Math (plain) |
|---|---|---|---|---|---|
| Cheap | Gemini 2.5 Flash-Lite | $0.50 | $0.28 | $0.25 | 3.0 x 0.10 + 0.5 x 0.40 |
| Cheap | Claude Haiku 5.5 | $0.55 | $0.33 | $0.28 | 3.0 x 0.10 + 0.5 x 0.50 |
| Cheap | GPT-6 Luna | $0.55 | $0.33 | $0.28 | 3.0 x 0.10 + 0.5 x 0.50 |
| Cheap | gpt-oss-20b on Groq | $0.38 | $0.28 | n.a. | 3.0 x 0.075 + 0.5 x 0.30 |
| Cheap | DeepSeek flash (off-peak / peak) | $0.75 / $1.50 | $0.38 / $0.77 | n.a. | 3.0 x 0.15 + 0.5 x 0.60 |
| Cheap | Gemini 3.1 Flash-Lite | $1.50 | $0.94 | $0.75 | 3.0 x 0.25 + 0.5 x 1.50 |
| Mid | GPT-6.1 Terra | $5.50 | $3.13 | $2.75 | 3.0 x 1 + 0.5 x 5 |
| Mid | Gemini 3.8 Flash (now / after Dec 31) | $4.13 / $8.25 | $2.44 / $4.88 | $2.06 / $4.13 | 3.0 x 0.75 + 0.5 x 3.75 |
| Mid | Claude Sonnet 5.5 | $11.00 | $6.25 | $5.50 | 3.0 x 2 + 0.5 x 10 |
| Mid | GPT-6.1 Sol | $11.00 | $6.25 | $5.50 | 3.0 x 2 + 0.5 x 10 |
| Frontier | Gemini 4 Argon (now / after Nov 30) | $11.00 / $22.00 | $6.25 / $12.50 | $5.50 / $11.00 | 3.0 x 2 + 0.5 x 10 |
| Frontier | Claude Opus 5.5 | $22.00 | $12.50 | $11.00 | 3.0 x 4 + 0.5 x 20 |
| Frontier | Claude Fable 5.1 | $55.00 | $30.63 | $27.50 | 3.0 x 10 + 0.5 x 50 |
| Frontier | GPT-6 Astra | $55.00 | $32.50 | $27.50 | 3.0 x 10 + 0.5 x 50 |

Worked example of the cached column, Sonnet 5.5: 0.5M uncached x $2 = $1.00, plus 2.5M cached x $0.10 = $0.25, plus 0.5M output x $10 = $5.00, total $6.25 (43% below plain).

### B. One hour of realtime voice conversation
| Stack | Math | Cost per hour |
|---|---|---|
| OpenAI `gpt-live-1` flat | 60 min x $0.05 | $3.00 |
| Gemini 3.8 Live, audio only | [ASSUMPTION] user audio is metered for the whole hour: 60 x $0.005 = $0.30; AI speaks 30 of 60 min: 30 x $0.018 = $0.54 | $0.84 (about $1.06 if the AI speaks 70% of the time); excludes text/tool tokens and context re-reads |
| OpenAI `gpt-realtime-2.1` (audio tokens) | [ASSUMPTION] 600 input tokens/min for all 60 min x $32/M = $1.15; 1,200 output tokens/min for 30 min x $64/M = $2.30; plus 40 turns x 40K tokens re-read at $0.40/M cached = $0.64 | about $4.10 (token rates implied by OpenAI's 2024 per-minute figures, not re-verified) |
| Deepgram Voice Agent, Standard (STT + LLM + TTS) | 60 x $0.075 (Growth $0.068) | $4.50 ($4.08) |
| Deepgram Voice Agent, BYO LLM and TTS | 60 x $0.050 | $3.00 plus your LLM and TTS |
| ElevenLabs Speech Engine | 60 x $0.08 | $4.80 plus LLM tokens |
| DIY: Deepgram Nova-3 streaming STT + Haiku 5.5 or Sonnet 5.5 + Aura-2 TTS | STT 60 x $0.0077 = $0.46; TTS 30 min of speech at 150 words/min x 6 characters = 27,000 characters x $0.030/1K = $0.81; LLM 40 turns x 2,000 input + 80 output tokens = 80K in / 3.2K out = $0.01 (Haiku 5.5) or $0.19 (Sonnet 5.5) | $1.28 (Haiku) to $1.46 (Sonnet); Sonnet with ElevenLabs Flash TTS ($1.08 for the same 27,000 characters) about $1.73 |

Telephony (Twilio or other SIP carrier), number rental and call-recording storage are extra and not priced here.

### C. Analyzing 100 screenshots
[ASSUMPTION] Claude image tokens about width x height / 750 (Anthropic's vision docs formula, not re-read this session), capped near 4,784 tokens at maximum resolution [SKILL-DOC]. Each call also has 300 prompt tokens and 200 output tokens. Totals include 100 x 300 prompt tokens and 100 x 200 = 20,000 output tokens.

| Screenshot size | Tokens each | Input total | Haiku 5.5 | Sonnet 5.5 | Opus 5.5 | Fable 5.1 |
|---|---|---|---|---|---|---|
| 1366x768 | about 1,400 | 169,900 | $0.03 | $0.54 | $1.08 | $2.70 |
| 1920x1080 | about 2,765 | 306,500 | $0.04 | $0.81 | $1.63 | $4.07 |
| Maximum (about 4,784) | 4,784 | 508,400 | $0.06 | $1.22 | $2.43 | $6.08 |

Example, 1920x1080 on Sonnet 5.5: 0.3065M x $2 + 0.02M x $10 = $0.613 + $0.200 = $0.813. Per screenshot: $0.0004 (Haiku) to $0.04 (Fable).

### D. One hour of video analysis (Gemini)
Tokens = 3,600 s x tokens per second (263 default per one docs page, about 300 per another, about 100 low resolution) [SNIPPET]. Input price only.

| Tokens per second | Tokens | 2.5 Flash-Lite ($0.10) | 3.1 Flash-Lite ($0.25) | 3.8 Flash ($0.75, $1.50 after Dec 31) | 3.1 Pro ($2.00) |
|---|---|---|---|---|---|
| 263 (default) | 946,800 | $0.09 | $0.24 | $0.71 | $1.89 |
| 300 (default, alt. figure) | 1,080,000 | $0.11 | $0.27 | $0.81 | $2.16 |
| 100 (low resolution) | 360,000 | $0.04 | $0.09 | $0.27 | $0.72 |

Google's "agentic" long-video mode claims up to 88% fewer tokens (1.08M to about 130K at 88%), which would cut these figures by roughly 8x for long, mostly static video [SNIPPET].

### E. One 30-step computer-use task
Assumptions [ASSUMPTION]: 4,500-token toolset definition [PAGE] + 800-token system prompt, a 1,366x768 screenshot (about 1,400 tokens) and about 50 tokens of tool text per step, 250 output tokens per step, all prior content kept in a cached prefix. Step 1 is uncached; later steps read the prefix at cache-read price and write new content at the 5-minute cache-write price (1.25x input). Totals: 48,800 newly written tokens, 893,200 cache-read tokens, 7,500 output tokens.

| Model | With caching | Without caching | Math (with caching) |
|---|---|---|---|
| Haiku 5.5 | $0.02 | $0.10 | 48,800 x $0.125/M + 893,200 x $0.01/M + 7,500 x $0.50/M = $0.006 + $0.009 + $0.004 |
| Sonnet 5.5 | $0.29 | $1.96 | 48,800 x $2.50/M + 893,200 x $0.10/M + 7,500 x $10/M = $0.122 + $0.089 + $0.075 |
| Opus 5.5 | $0.57 | $3.92 | 48,800 x $5/M + 893,200 x $0.20/M + 7,500 x $20/M = $0.244 + $0.179 + $0.150 |
| Fable 5.1 | $1.21 | $9.80 | 48,800 x $12.50/M + 893,200 x $0.25/M + 7,500 x $50/M = $0.610 + $0.223 + $0.375 |

Reasoning tokens would add to output; the Anthropic browser toolset (about 6,600 tokens) is heavier than the computer toolset. Hosted browser time adds roughly $0.0003 to $0.004 per task at $0.02 to $0.12 per hour for a 1 to 2 minute task (Browserbase bills a one-minute minimum per session) [3P prices].

### F. Search and deep research
- 1,000 searches: Anthropic or OpenAI tool $10.00; Google $14.00 after 5,000 free per month; DeepSeek $0.75. Result tokens are billed on top: 5 results x 1,000 tokens x 1,000 searches = 5M input tokens, which is $10.00 on Sonnet 5.5 ($2/M) or $0.50 on Haiku 5.5. [ESTIMATE]
- 100 deep research reports a month: $100 to $700 if the Gemini figures ($1 to $7 per task) hold, $1,000 to $3,000 at OpenAI's reported $10 to $30 per task [3P, [UNVERIFIED]].

### G. OCR 10,000 pages
Mistral OCR 4: 10 x $4 = $40 ($20 batch) [3P]. LLM page reads at 1,500 image tokens in and 1,000 text tokens out per page: Haiku 5.5 15M x $0.10 + 10M x $0.50 = $1.50 + $5.00 = $6.50; Sonnet 5.5 15M x $2 + 10M x $10 = $30 + $100 = $130. Quality and layout fidelity untested.

### H. What $200 per month buys
Per user: 10 calls per day for 30 days = 300 calls of 3k in / 500 out.

| Model | Cost per call | Per user per month | Users covered by $200 |
|---|---|---|---|
| Claude Haiku 5.5 | $0.00055 | $0.17 | about 1,200 |
| Gemini 3.1 Flash-Lite | $0.0015 | $0.45 | about 440 |
| GPT-6.1 Terra | $0.0055 | $1.65 | about 120 |
| Claude Sonnet 5.5 | $0.011 | $3.30 | about 60 |
| Claude Opus 5.5 | $0.022 | $6.60 | about 30 |
| Claude Fable 5.1 | $0.055 | $16.50 | about 12 |

Caching and batching reduce these by roughly 40% to 50% where a stable prefix or asynchronous processing is possible (table A).

## Blocked sources

- `help.openai.com/en/articles/20001371` ("Evolving Atlas into ChatGPT for browser-based agentic work"): WebFetch returned HTTP 403 on the first try, not retried. The Atlas retirement claim relies on search summaries and press coverage (MacRumors 2026-07-10, The Next Web, eWeek).
- OpenAI pricing raw-HTML cross-check: the sandbox declined a curl request that used a browser-like User-Agent against `developers.openai.com` (classified as bot-check circumvention). I did not retry or work around it. OpenAI rows therefore rest on the WebFetch summary, LiteLLM and search results.
- `registry.modelcontextprotocol.io/v0/servers?limit=1000`: HTTP 422 (page size cap); the registry returns no total count, so I did not count MCP servers (full pagination would exceed the API-call budget).
- Pages not opened because of the page-read budget; their values come from search summaries or aggregators and are tagged: Together, Fireworks and DeepInfra pricing; AssemblyAI and Cartesia pricing; Twilio, Vapi, Retell and Bland pricing; Brave, Exa, Tavily, Perplexity and Parallel pricing; Browserbase, Steel, Kernel and Hyperbrowser pricing; Mistral OCR pricing; Gemini video and media-resolution docs; Claude vision, PDF and computer-use docs; Gemini Live screen-share and Android Gemini Nano docs; ChatGPT release notes and ChatGPT memory/voice documentation.
- Hugging Face API for `meta-llama` and `microsoft` returned model lists but no Phi-5 or post-April-2025 Llama weights; this is one listing, not proof that none exist elsewhere.
- Reddit, Product Hunt, G2, Trustpilot and similar blocked sources from the research brief were not needed and not attempted.
