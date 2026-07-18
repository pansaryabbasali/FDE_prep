# 4-Day Plan (Thu–Sun) — Condensed

**The dashboard (index.html / the live site) is the canonical, fully detailed version** — each
block there has step-by-step instructions, links, and done-criteria. This file is the printable
outline. The plan maps to the confirmed interview loop: **R1** coding (read + write) + background/
intent/impact · **R2** business case study · **R3** live build using AI · **R4** hiring manager.

## Day 1 (Thu) — Agents, MCP, Context + first R1 drill (~9.5h)

| Time | Block | Round |
|---|---|---|
| 08:30–09:00 | Setup: Sarvam API key, Codespace, clone cookbook + langchain-academy, verify one call | — |
| 09:00–10:00 | Agent vocabulary: Anthropic "Building Effective Agents" + multi-agent research system | R2 |
| 10:00–13:00 | LangGraph sprint: Essentials course, typed by hand; interrupts/persistence docs; 20-min capstone drill | R1/R3 |
| 13:45–14:45 | Breadth: Google ADK + LlamaIndex; translation table vs watsonx Orchestrate | — |
| 14:45–15:45 | MCP: build weather server (FastMCP), test with Inspector, read sarvam-mcp | — |
| 16:15–17:45 | Context engineering: Anthropic + Lance Martin (Write/Select/Compress/Isolate) + Manus + Context Rot | R1/R4 |
| 17:45–18:30 | **Code-reading drill #1**: unfamiliar cookbook app, narrate aloud, 60-sec summary | **R1** |
| 18:30–19:00 | Flashcards | — |

## Day 2 (Fri) — Evals, Build #1, first R3 drill (~9.5h)

| Time | Block | Round |
|---|---|---|
| 08:30–09:00 | Warm-up: LangGraph capstone re-drill (timed) | R1 |
| 09:00–11:30 | Evals deep block: Hamel ×2, Eugene Yan, tooling skim, write YOUR evals playbook | R2/R4 |
| 11:30–12:30 | RAG-2026 refresh: contextual retrieval, chunking, the "is RAG dead" answer | R2 |
| 13:15–16:15 | **Build #1 (solo-typed)**: Sarvam call-analytics agent + JSON-schema outputs + eval harness → `build-1/` | R1 |
| 16:45–17:30 | **AI-assisted extension drill (45 min timed)**: extend Build #1 with an AI assistant; spec→prompt→verify loop; catch ≥1 AI mistake | **R3** |
| 17:30–18:15 | Tool use & structured outputs brush-up | — |
| 18:15–18:45 | Flashcards; push Build #1 | — |

## Day 3 (Sat) — Voice, Systems, Sarvam depth (~9.5h)

| Time | Block | Round |
|---|---|---|
| 08:30–11:00 | Voice architecture: the Primer + LiveKit + Softcery; memorize the ~800ms latency budget; whiteboard drill | R2 |
| 11:00–13:00 | **Build #2**: VAD from scratch in numpy + Saaras→30B→Bulbul streaming loop → `build-2/` | R1/R3 |
| 13:45–15:15 | Kafka/SQS/reliability: crash course + decision framework + DLQ/idempotency; WhatsApp-bot drill | R2 |
| 15:15–16:15 | System design sketches (timed): LIC-scale voice servicing; media dubbing pipeline — with cost/ROI framing | R2 |
| 16:45–17:45 | Sarvam memorization: cheat sheet cold + self-quiz | R1/R4 |
| 17:45–18:30 | **Code-reading drill #2**: sarvam-mcp or skills repo internals, narrated aloud | **R1** |
| 18:30–19:00 | Flashcards | — |

## Day 4 (Sun) — Full interview rehearsal R1→R2→R3→R4 (~8.5h)

| Time | Block | Round |
|---|---|---|
| 09:00–10:00 | R1(a) code: NeetCode arrays/hashing + timed code-read of an LLM-generated gnarly snippet + chunked-RMS from memory | **R1** |
| 10:00–11:00 | R1(b) background/intent/impact: 2-min career narrative with numbers + "why Sarvam/why FDE" — rehearsed aloud, recorded | **R1** |
| 11:00–12:30 | **R2 mock #1** (45 min timed + review): business case with LLM interviewer, ROI pushback | **R2** |
| 13:15–14:45 | **R3 mock**: 60-min live build with AI on an unseen problem + 15-min demo narration + retro → `build-3/` | **R3** |
| 15:15–16:15 | **R2 mock #2**: different domain (dubbing / build-vs-buy), CFO cost challenge | **R2** |
| 16:15–17:30 | R4 prep: 7 STAR stories, two deep-dive narratives, gap lines, 3 questions | **R4** |
| 17:30–18:15 | Final pass: six recitables, shaky flashcards, logistics; stop by 19:00 | — |

## The six recitables (final check)

① Voice latency budget · ② 5 workflow patterns · ③ Write/Select/Compress/Isolate ·
④ your evals playbook · ⑤ SQS-vs-Kafka framework · ⑥ Sarvam model lineup + timeline.
