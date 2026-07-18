# Interview Playbook

## The CONFIRMED process (insider info via a friend, July 2026)

| Round | What it is | How to prep |
|---|---|---|
| **R1 — Coding Assessment** | Code **read AND write** + candidate background, **intent**, impact in previous role + general discussion | Code-reading drills (Days 1/3/4), light DSA, career narrative with impact numbers, crisp "why Sarvam / why FDE" (= the "intent") |
| **R2 — Business Case Study** | Business and technical scenarios; they evaluate your thinking | Decomp method + system-design sketches + two timed mocks (Day 4). Business framing: v1 scope, cost, ROI, success metrics |
| **R3 — Live Build** | Problem given on the spot; build a small application **using the help of AI** | The AI-assisted loop: spec → prompt → **verify** → iterate → demo. Drilled Day 2, full rehearsal Day 4. Narrate while driving the AI; catch its mistakes out loud |
| **R4 — Hiring Manager** | Fit, ownership, expectations | STAR stories + deep-dive narratives + 3 questions |

R3 note: never accept AI output unread — catching its mistakes IS the test. A running ugly
app beats a beautiful fragment; save 5 minutes to demo.

(Earlier secondary reports — proctored hackathon, VAD-from-scratch — may apply to other
tracks; the audio/streaming fluency still pays off in R1/R3.)

## The decomp method (memorize the sequence)

1. **Ask before solving** (5+ min of questions is a *positive* signal): Who are the users?
   What actions? Data volumes and formats? Latency/accuracy/cost constraints? What does
   failure cost? What exists today?
2. Name entities, data flows, and integration points; draw the boxes.
3. **Scope an explicit v1** and justify what's out ("v1 does X for the top intent only,
   because that's 60% of call volume; here's the metric that tells us to expand").
4. State failure modes and mitigations unprompted (the FDE tell).
5. Think out loud continuously — silence reads as stuck.

## STAR stories to write out (bullets, ~5 lines each) — Day 2, 18:00 block

| # | JD trait | Your story |
|---|---|---|
| 1 | Own the technical arc / trusted point of contact | An IBM engagement end-to-end: discovery → architecture → build → demo → production (pick the strongest account: defense doc-intelligence or a state gov) |
| 2 | Evals & iterating from data | AIOps RCA system: how you *measured* retrieval quality, fought lost-in-the-middle, tuned chunking/prompt ordering, and what "good" meant (RCA time 1–3 h → ~30 min) |
| 3 | High agency / unblocking yourself | On-prem UAT install in the client's environment — the constraint you hit and worked around without waiting for direction |
| 4 | Difficult client / pushback | From IBM or EY: a client who disagreed with your approach; how you used data/demos to converge (or conceded intelligently) |
| 5 | Ambiguity with no spec | The state-gov chatbots: turning "help farmers" into a scoped system grounded in location/weather data from public portals |
| 6 | Deadline pressure / shipping | The 1000+-doc multilingual pilot: retrieval 30–40 min → under 1 min; what you cut to ship |
| 7 | Failure/learning | Pick one honestly — a demo that broke, a model that underperformed, what changed in your process after |

Rehearse out loud once. Bullets, not scripts — scripted answers sound scripted.

## Two deep-dive narratives (they will pick one and drill)

1. **AIOps RCA RAG system** — be ready for 20 minutes of "why": why two models (Granite
   preprocessing + Llama 3.3)? why that chunking? how did you *know* lost-in-the-middle was
   the problem? what would you do differently in 2026 (contextual retrieval, reranker,
   trajectory evals, KV-cache-aware prompt layout)?
2. **State-gov multilingual chatbots** — the Sarvam connection: why Sarvam Document
   Intelligence for OCR, what its output looked like, how you grounded answers in circulars,
   how you handled Indic-language quality. Practice saying the model/mode names correctly
   (Sarvam Vision / doc-intelligence async jobs).

## Your gap-handling lines (prepared honesty beats bluffing)

- **"Have you used LangGraph?"** → "My production multi-agent work was on watsonx Orchestrate
  ADK; this week I built [Build #1/#2] with LangGraph — the concepts map directly: state
  graph + checkpointing + interrupts vs Orchestrate's skills/agents orchestration. Happy to
  walk through the code."
- **"Voice experience?"** → "Not in production yet — so I built a streaming Saaras→30B→Bulbul
  pipeline and a VAD from scratch this week to understand the latency budget concretely.
  Here's what surprised me: [real detail from your build]."
- **"AWS/GCP?"** → "Azure and on-prem OpenShift in production; the services map 1:1 and I
  ship on new stacks in days — did exactly that with [example]."

## Questions to ask them (pick 3)

1. "When Samvaad deployments hit quality issues at a client — say, code-mixed speech in a
   noisy branch — what does the eval-and-iteration loop actually look like between the FDE
   and the research team?" (shows evals mindset + field-to-research loop from the JD)
2. "For the SBI Life-scale rollouts: what does the FDE own vs. the client's engineering team
   — telephony integration, core-system tool calls, on-prem infra?"
3. "How much do FDEs shape Arya's roadmap — does field feedback drive which primitives get
   built next?"
4. "What separates the FDEs who thrive here from the ones who don't, in the first 90 days?"
5. "What's the ratio of greenfield builds vs. rescuing/hardening existing deployments?"

## Red flags to avoid

- Don't say "I'd just use long context" or "RAG is dead" — the 2026 answer is hybrid.
- Don't present metrics dashboards as evals — error analysis on real traces comes first.
- Don't bluff on Kafka internals; the vocabulary + decision framework is enough at this level.
- Don't let any answer end without a measurement ("...and we'd know it works because X").
- Never confuse "SarvM.ai" reviews with Sarvam AI — different company.

## Day-before checklist

- [ ] Recite: 5 workflow patterns; Write/Select/Compress/Isolate; voice latency budget;
      SQS-vs-Kafka; evals playbook; Sarvam model lineup + timeline.
- [ ] Both builds run clean from a fresh terminal; you can screen-share them.
- [ ] STAR bullets printed/open; 3 questions chosen.
- [ ] Sarvam dashboard account + API key working (in case of a live task on their APIs).
- [ ] Confirm interview format with recruiter if not already known.
- [ ] Sleep. A rested brain beats one more blog post.
