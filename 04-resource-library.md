# Full Resource Library (researched & verified July 2026)

Everything found in research, organized by topic with time estimates. The day plans pick the
essentials; come here to swap resources or go deeper if a block finishes early.

## Agentic frameworks

| Resource | Time | Why |
|---|---|---|
| [LangGraph Essentials — LangChain Academy](https://academy.langchain.com/courses/langgraph-essentials-python) | 2–3 h | Official fast on-ramp: State/Nodes/Edges/Memory, hands-on email agent |
| [Introduction to LangGraph — LangChain Academy](https://academy.langchain.com/courses/intro-to-langgraph) | 6–8 h (Modules 1–3 ≈ 3 h) | The canonical deep course; notebooks at [langchain-academy](https://github.com/langchain-ai/langchain-academy) |
| [LangGraph interrupts/HITL docs](https://docs.langchain.com/oss/python/langgraph/interrupts) | 1 h | `interrupt()`, `Command`, checkpointers, threads — the exact interview probes |
| [DeepLearning.AI: Long-Term Agentic Memory with LangGraph](https://www.deeplearning.ai/short-courses/long-term-agentic-memory-with-langgraph/) | 1.5 h | Semantic/episodic/procedural memory + LangMem (Harrison Chase) |
| [Anthropic: Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents) | 30 m | THE canonical essay — 5 workflow patterns, workflows vs agents |
| [Anthropic: How we built our multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system) | 25 m | Best real-world multi-agent + agent-evals war story |
| [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) + [Practical Guide to Building Agents (PDF)](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) | 1.5 h | Agents/handoffs/guardrails/sessions; orchestration + guardrail vocabulary |
| [Google ADK get-started](https://google.github.io/adk-docs/get-started/) + [agent-team tutorial](https://adk.dev/tutorials/agent-team/) | 1 h | ADK 2.0 GA Jun 2026; LlmAgent vs Sequential/Parallel/Loop workflow agents |
| [LlamaIndex agents](https://developers.llamaindex.ai/python/framework/use_cases/agents/) + [Agentic RAG post](https://www.llamaindex.ai/blog/agentic-rag-with-llamaindex-2721b8a49ff6) | 45 m | FunctionAgent, event-driven Workflows, query routing / sub-question decomposition |
| [12-Factor Agents](https://github.com/humanlayer/12-factor-agents) | 45 m | "Tool use is structured output + a switch statement"; own your control flow — very quotable |

## MCP

| Resource | Time | Why |
|---|---|---|
| [MCP intro](https://modelcontextprotocol.io/docs/getting-started/intro) → [Build a server](https://modelcontextprotocol.io/docs/develop/build-server) | 1–2 h | Official quickstart; FastMCP weather server |
| [Anthropic Academy: Intro to MCP](https://anthropic.skilljar.com/introduction-to-model-context-protocol) | 2–3 h | Free course w/ certificate; servers AND clients in Python |
| [Simplescraper: How to MCP](https://simplescraper.io/blog/how-to-mcp) | 45 m | Best community guide to remote servers (auth, deployment, gotchas) |
| [sarvam-mcp](https://github.com/sarvamai/sarvam-mcp) | 15 m | Sarvam's own MCP server — doubles as an API-surface map |

## Context engineering

| Resource | Time | Why |
|---|---|---|
| [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | 30 m | Canonical: compaction, note-taking, sub-agent isolation, JIT retrieval |
| [LangChain: Context Engineering for Agents](https://www.langchain.com/blog/context-engineering-for-agents) | 25 m | Write / Select / Compress / Isolate taxonomy |
| [Manus: Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) | 30 m | KV-cache hit rate as #1 metric; mask-don't-remove; filesystem-as-context |
| [Chroma: Context Rot](https://research.trychroma.com/context-rot) | 30 m | Empirical: performance degrades non-uniformly with length (supersedes lost-in-the-middle) |
| [Lance Martin's Manus deep-dive](https://rlancemartin.github.io/2025/10/15/manus/) | 20 m | Bonus synthesis |

## Tool use & structured outputs

| Resource | Time | Why |
|---|---|---|
| [Anthropic: Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | 25 m | Tool design: namespacing, meaningful returns, token efficiency |
| [OpenAI function calling](https://platform.openai.com/docs/guides/function-calling) + [structured outputs cookbook](https://cookbook.openai.com/examples/structured_outputs_intro) | 1 h | `strict: true`, schema limits, refusals, parallel calls |
| [TDS: JSON mode vs function calling vs structured outputs](https://towardsdatascience.com/structured-outputs-with-llms-json-mode-function-calling-and-when-to-use-each/) | 20 m | Cross-provider mental model + constrained decoding |
| Open-model ecosystem: Outlines, XGrammar, llguidance; [JSONSchemaBench](https://arxiv.org/pdf/2501.10868) | 15 m | Name-drops for "how is valid JSON guaranteed on open models?" |

## Evals

| Resource | Time | Why |
|---|---|---|
| [Hamel Husain: Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) | 40 m | The canonical post: 3 levels, look-at-your-data culture |
| [Hamel + Shreya: Evals FAQ](https://hamel.dev/blog/posts/evals-faq/) | 1.5–2 h | Highest-ROI: error analysis first, binary > Likert, judge alignment (TPR/TNR), RAG debugging |
| [Eugene Yan: LLM-Evaluators](https://eugeneyan.com/writing/llm-evaluators/) | 45 m | Judge biases; pairwise vs direct scoring |
| Tools: [promptfoo](https://www.promptfoo.dev/docs/intro/), [Ragas](https://docs.ragas.io/), LangSmith agentevals/openevals; Braintrust, DeepEval, Arize Phoenix | 1 h | Name accurately; trajectory vs final-answer evals |
| Sarvam's own: [llm_wer](https://github.com/sarvamai/llm_wer), [llm_intent_entity](https://github.com/sarvamai/llm_intent_entity) | 20 m | ASR eval pipelines — cite in interview |

## RAG (2026 refresh — your strength, light touch)

| Resource | Time | Why |
|---|---|---|
| [Anthropic: Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) | 25 m | Contextual embeddings + BM25 + reranking (−67% retrieval failures); "<200K → long context" rule |
| [Firecrawl: Chunking strategies for RAG in 2026](https://www.firecrawl.dev/blog/best-chunking-strategies-rag) | 25 m | Current defaults: recursive 400–512 tok / 10–20% overlap; semantic; page-level; agentic |
| [RAGFlow: From RAG to Context (2025 review)](https://ragflow.io/blog/rag-review-2025-from-rag-to-context) | 40 m | State of the field: hybrid search, rerankers, GraphRAG, agentic RAG |

## Voice agents

| Resource | Time | Why |
|---|---|---|
| [Voice AI & Voice Agents: An Illustrated Primer](https://voiceaiandvoiceagents.com/) | 2.5–3 h | THE canonical resource (Daily/Pipecat team): latency budgets, VAD, barge-in, telephony vs WebRTC |
| [Joey Wang's condensed notes](https://www.joeywang.blog/blog/voice-ai) | 30 m | The primer in a hurry |
| [LiveKit: Voice agent architecture](https://livekit.com/blog/voice-agent-architecture-stt-llm-tts-pipelines-explained) | 30 m | Streaming/overlapped pipelines + per-stage latency numbers |
| [Softcery: Real-time vs turn-based voice agents 2026](https://softcery.com/lab/ai-voice-agents-real-time-vs-turn-based-tts-stt-architecture) | 25 m | Cascaded vs speech-to-speech vs hybrid, with cost |
| [Pipecat](https://github.com/pipecat-ai/pipecat) / [framework comparison](https://webrtc.ventures/2026/03/choosing-a-voice-ai-agent-production-framework/) | 45 m | Pipecat (Python pipeline control) vs LiveKit Agents (WebRTC/SIP native) |
| [Sarvam skills repo — voice-agents skills](https://github.com/sarvamai/skills) | — | LiveKit + Pipecat pipelines on Sarvam's own STT/TTS |

## LLM production system design

| Resource | Time | Why |
|---|---|---|
| [Chip Huyen: Building A Generative AI Platform](https://huyenchip.com/2024/07/25/genai-platform.html) | 45 m | Best free architecture post; her *AI Engineering* (O'Reilly 2025) ch. 9–10 covers same |
| [Eugene Yan: Patterns for LLM Systems](https://eugeneyan.com/writing/llm-patterns/) + [applied-llms.org](https://applied-llms.org/) | 1.5 h | Seven patterns + a year of operational lessons |
| [System Design Handbook: LLM System Design Guide 2026](https://www.systemdesignhandbook.com/guides/llm-system-design/) | 40 m | Interview-formatted walkthrough |
| [7 patterns flashcard post](https://jamwithai.substack.com/p/system-design-for-ai-engineers-7) | 20 m | Night-before review |
| Dubbing: [NVIDIA Content Localization Blueprint (May 2026)](https://www.sportsvideo.org/2026/05/14/nvidia-releases-content-localization-blueprint-for-ai-assisted-dubbing-and-speech-translation/) + [Amazon dubbing paper](https://arxiv.org/pdf/2001.06785) | 1 h | Reference architecture + the four classic gotchas |

## Messaging & distributed systems

| Resource | Time | Why |
|---|---|---|
| [Confluent Kafka 101](https://developer.confluent.io/courses/apache-kafka/events/) | 2 h | Canonical free course (13 short videos) |
| [TechWorld with Nana: Kafka crash course](https://www.youtube.com/watch?v=B7CwU_tNYIE) | 1 h 08 m | One-sitting alternative, Python + Docker hands-on |
| ByteByteGo: [Ultimate Kafka 101](https://blog.bytebytego.com/p/ep126-the-ultimate-kafka-101-you) + [Why is Kafka fast?](https://blog.bytebytego.com/p/why-is-kafka-fast) | 25 m | Visual interview answers |
| [Svix: Kafka vs SQS](https://www.svix.com/resources/faq/kafka-vs-sqs/) + [TechUnfiltered comparison](https://techunfiltered.dev/sqs-vs-kafka-when-to-use-what-in-real-systems) | 20 m | The decision framework |
| [Idempotency/retries/DLQs](https://baxchain.com/blogs/resilient-event-driven-architecture-idempotency-retries-and-dead-letter-queues/) + [Background jobs 2026 reference](https://www.digitalapplied.com/blog/background-job-queue-patterns-2026-engineering-reference) | 40 m | Reliability patterns for AI pipelines |
| [Hookdeck: webhooks vs polling](https://hookdeck.com/webhooks/guides/when-to-use-webhooks) + [Svix FAQ](https://www.svix.com/resources/faq/webhooks-vs-api-polling/) | 15 m | Integration-pattern quick hit |

## FDE interview prep

| Resource | Time | Why |
|---|---|---|
| [Exponent: FDE Interview — Definitive 2026 Guide](https://www.tryexponent.com/blog/forward-deployed-engineer-interview-the-definitive-2026-guide-fde) | 30 m | Best cross-company overview of the FDE loop |
| [OpenAI FDE process writeup](https://gaijineer.co/openai-forward-deployed-engineer-interview-process) | 20 m | 7-stage loop incl. eval-design and customer-empathy rounds |
| [Anthropic Applied AI interview analysis](https://getperspective.ai/blog/anthropic-applied-ai-engineer-interview-process-frontier-lab-2026) | 15 m | The customer-conversation sim carries hidden weight |
| Palantir decomp: [Coditioning guide](https://www.coditioning.com/blog/703/palantir-swe-decomposition-interview) + [first-person mistakes post](https://medium.com/@anqi.silvia/my-palantir-decomposition-interview-mistakes-and-fixes-113e2a281bb6) + [Glassdoor](https://www.glassdoor.com/Interview/Palantir-Technologies-Forward-Deployed-Engineer-Interview-Questions-EI_IE236375.0,21_KO22,47.htm) | 1 h | The canonical FDE round + method |
| Sarvam intel: [Grapevine thread](https://www.grapevine.in/round1/job-interview/e87b2eb9-8bcf-4122-8122-2afaa2500801) + [2.5-h hackathon account (VAD from scratch)](https://getpersonalisedcv.in/blog/sarvam-ai-interview-experience-84-lpa-ml-engineer) | 20 m | Reported: timed practical task + solution-walkthrough deep-dives; no LeetCode. ⚠️ Glassdoor's "SarvM.ai" is a different company |
| [awesome-behavioral-interviews](https://github.com/ashishps1/awesome-behavioral-interviews) | 1.5 h | STAR question bank |
| [Exponent solutions-architect behavioral bank](https://www.tryexponent.com/questions?role=solutions-architect&type=behavioral) | 30 m | Closest role-match behavioral drills |
| [NeetCode practice](https://neetcode.io/practice) | ≤2 h | Insurance only: arrays/hashing, two pointers, strings |
