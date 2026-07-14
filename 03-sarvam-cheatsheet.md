# Sarvam AI Cheat Sheet (researched July 2026 — verify anything load-bearing before the interview)

## Company in five bullets

- Founded Aug 2023, Bengaluru, by **Dr. Vivek Raghavan** (12 yrs Aadhaar/UIDAI) and
  **Dr. Pratyush Kumar** (IBM/Microsoft Research, IIT-M, co-founder of AI4Bharat). Both from
  the AI4Bharat lineage — open Indic-language AI research.
- **Series A** Dec 2023: $41M (Lightspeed, Peak XV, Khosla). **Series B June 2026: $234M at
  $1.5B valuation led by HCLTech (~$150M)** — India's newest AI unicorn.
- **Apr 2025: first company selected under the IndiaAI Mission** to build India's sovereign
  foundation model — ~4,096 H100s of subsidized compute (Yotta "Shakti" cluster); the
  government takes a small equity stake in exchange.
- Revenue ~**$12M ARR**, with the conversational-agents business (**Samvaad**) at ~80% of it.
  BFSI is the beachhead: **Tata Capital, SBI Life, LIC, IDFC First Bank, CRED**.
- Positioning: "India's full-stack sovereign AI" — research + models + infra + applications;
  trained/hosted in India; air-gapped deployment as a first-class option.

## Model lineup (know what each is for)

| Model | What it is | Notes to drop in conversation |
|---|---|---|
| **Sarvam-105B** (Feb 2026, Apache-2.0) | Flagship MoE LLM: ~106B total / ~9–10B active, 128 experts top-8, Multi-head Latent Attention, 128K ctx, ~12T tokens, trained **from scratch on Indian compute** | Strong on agentic benchmarks (Tau-2 Bench); competitive with gpt-oss-120B class |
| **Sarvam-30B** (Feb 2026, Apache-2.0) | MoE: ~32B total / **~2.4B active**, GQA, 32–65K ctx, ~16T tokens | Purpose-built for **low-cost real-time conversation** — the voice-agent workhorse |
| **Sarvam-M** (May 2025, open) | 24B hybrid-reasoning model built on Mistral Small | Think/non-think modes; **reasons in English inside `<think>`, answers in the Indic language**; SFT → RLVR → FP8 + lookahead decoding |
| **Sarvam-Translate** (Jun 2025, open) | Translation FT of Gemma3-4B-IT | **All 22 scheduled languages**; document-level, preserves HTML/LaTeX structure |
| **Sarvam-1** (Oct 2024, open) | 2B Indic LLM from scratch | The **tokenizer story** (below) |
| **Saaras v3** | STT, 23 languages (22 Indic + En) | **Five modes: transcribe / translate / verbatim / transliterate / code-mixed**; noisy + code-mixed speech; batch API w/ diarization; WebSocket streaming. (Saarika = older transcribe-only line, being folded in) |
| **Bulbul v3** | TTS, 30+ Indic-accent voices, 11 languages | Sync + HTTP-stream + WebSocket; pronunciation dictionaries; gotcha: v3 rejects `pitch`/`loudness` params |
| **Mayura v1** | Text translation, ~12 languages | Formal/colloquial/code-mixed output styles; auto language detection |
| **Sarvam Vision / Document Intelligence** | OCR/doc parsing, 23 languages, script-preserving | Async job API (init → signed-URL upload → poll → download); HTML/MD/JSON out. **You used this at IBM.** |
| Shuka 1.0 (Aug 2024) | India's first open AudioLM (voice-in/text-out) | Historical credibility point |

## The signature technical story: tokenizer fertility

Generic multilingual tokenizers spend **4–8 tokens per word** on Indic scripts; Sarvam's
custom tokenizers hit **~1.4–2.1** — i.e., 2–4x cheaper and faster Indic inference. It's why
Sarvam-1 got a from-scratch tokenizer and why Sarvam-Translate was built on Gemma-3 (efficient
Indic tokenizer). Combine with Sarvam-30B's ~2.4B active params and you get the thesis:
**economical, low-latency Indic voice agents at population scale.**

## Platform & products

- **Samvaad** — enterprise conversational-agent platform (voice, WhatsApp, web, in-app). The
  revenue engine. Opened to public self-serve ~June 2026; voice heritage pricing ~₹1/min.
- **Arya** (Feb 2026) — multi-agent **orchestration** platform. Core philosophy to quote:
  *separate the deterministic control plane (code/graph handles iteration, branching, retries,
  scheduling) from LLM judgment*; append-only immutable **state ledger** for recovery/replay;
  8 primitives (LLM, Agent, MCP, Node, Ledger, Task Graph, Code Interpreter, Artefact);
  deploys cloud / on-prem / **air-gapped**. This is watsonx-Orchestrate-shaped — say so.
- **Indus** (Feb 2026) — consumer voice-first multilingual chat app (web/iOS/Android).
- **A1** (Aug 2024) — legal GenAI workbench (earlier product).
- **Official MCP server**: `uvx sarvam-mcp` — every public API as MCP tools —
  https://github.com/sarvamai/sarvam-mcp
- **APIs** at `https://api.sarvam.ai` (docs.sarvam.ai, keys at dashboard.sarvam.ai): STT
  (+batch, +WS streaming), TTS (+streaming), Translate, Transliterate, Language ID, Text
  Analytics, **OpenAI-compatible Chat Completions** (30B/105B, streaming + reasoning mode),
  Vision doc-intelligence jobs, pronunciation dictionaries. Python SDK: `pip install sarvamai`.
- **Pricing ballpark** (mid-2026): Chat 105B ₹4/₹16 per 1M in/out tokens (30B: ₹2.5/₹10);
  STT ₹30/hr; TTS v3 ₹30/10K chars; Translate ₹20/10K chars; doc parsing ₹0.5/page.
  Free credits on signup; startup program exists.

## 2025–2026 timeline (recitable)

Apr 2025 IndiaAI Mission selection → May 2025 Sarvam-M → Jun 2025 Sarvam-Translate →
Feb 10, 2026 **Arya** → Feb 18, 2026 **Sarvam-30B/105B** (India AI Impact Summit; Apache-2.0
in March) → Feb 20, 2026 **Indus** app → Feb 26, 2026 **SBI Life** partnership (80M customers,
350K distributors, 11 languages, rollout target Aug 2026) → Jun 2026 **$234M / unicorn /
HCLTech** + Samvaad public self-serve.

## Hands-on resources (used in the plan)

- Cookbook (notebooks: STT/TTS/translate/chat/doc-intelligence/**call-analytics** + example
  apps): https://github.com/sarvamai/sarvam-ai-cookbook
- Skills repo (condensed SDK reference + **LiveKit/Pipecat voice-agent skills** + documented
  SDK gotchas): https://github.com/sarvamai/skills
- ASR eval repos (they publicly care about eval pipelines — cite these):
  https://github.com/sarvamai/llm_wer, https://github.com/sarvamai/llm_intent_entity
- Docs: https://docs.sarvam.ai (+ /llms.txt), HF: https://huggingface.co/sarvamai
- SDK gotchas worth knowing (shows real usage): `client.text.translate()` (not
  `.translate.translate()`); chat `content` can be `None` when reasoning eats the token
  budget; Bulbul v3 400s on `pitch`/`loudness`; `output_script` ignored on sarvam-translate.

## Narrative answers to have ready

- **"Why Sarvam?"** — Population-scale Indic AI is the through-line of my IBM work (two state
  governments, farmers, citizens); I've already shipped Sarvam Document Intelligence inside a
  government engagement; I want to be at the company building the models, not just consuming
  them; and the FDE role is exactly the client-engineering arc I already own at IBM — but
  full-stack and higher-agency.
- **"Voice at a bank — what's hard?"** — code-mixed speech recognition, sub-second latency on
  telephony audio, barge-in, tool calls into decades-old core-banking systems, compliance/
  on-prem, and evals (WER per language, intent accuracy, task completion, escalation rate).
- **Sovereignty pitch in one line** — data residency + air-gapped deploys + models trained on
  Indian compute under IndiaAI = the only stack a regulated Indian FI can adopt without
  cross-border data questions.
