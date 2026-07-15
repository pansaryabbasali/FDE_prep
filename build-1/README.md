# Build #1 — Sarvam-stack agent with an eval harness (Day 1, 18:00–20:30)

**Option A (recommended): BFSI call analytics.** Sample call audio is in the
[sarvam-ai-cookbook](https://github.com/sarvamai/sarvam-ai-cookbook) call-analytics example.
Pipeline: Saaras v3 STT → Sarvam chat completion → intent/entities/summary as structured JSON
→ printed report.

**Option B: multilingual doc Q&A.** Sarvam Vision async job → chunk → retrieve → cited answers.

## Non-negotiables (whichever option)

1. Structured output against a JSON schema, with a retry-on-invalid path
   (chat `content` can be `None` when reasoning eats the token budget).
2. Eval harness: 10–15 hand-written test cases + one binary-rubric LLM-judge +
   a pass-rate table printed at the end.
3. Type the code yourself. Commit here when it runs.

## Done when

You can run one command, watch the pipeline process real audio/docs, and see an eval
pass-rate table — and you can explain every design choice out loud.
