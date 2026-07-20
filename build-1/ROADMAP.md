# Build #1 Roadmap — Sarvam Call-Analytics Agent + Eval Harness (Claude Code edition)

Concrete, phase-by-phase execution plan for today's two activities:
**Build #1 (~2.5–3h)** and the **AI-assisted extension drill (45 min timed)**.
You are driving Claude Code for both — which turns the whole session into R3 practice.

> **Tell Claude Code at the start:** "Read build-1/ROADMAP.md and follow it phase by phase.
> Stop after each phase so I can review and run it."

## Ground rules (this is what R3 graders watch for)

1. **One phase at a time.** Never let Claude produce the whole app in one shot.
2. **Read every diff before running it.** Find at least one thing to question or improve per
   phase — a hardcoded value, a missed error path, an unclear name. Say it, fix it.
3. **You author the eval test cases and rubric yourself** (Phase 4, step 2). That's the
   thinking the interview probes; Claude only wires the harness around your cases.
4. **After each phase, explain the file aloud in 60 seconds.** The solution-walkthrough
   rounds test whether you understand what you shipped. If you can't explain it, have
   Claude walk you through it line by line before moving on.
5. Commit at the end of each phase: `git add build-1/ && git commit -m "phase N" && git push`

## Phase 0 — Preflight (10 min)

- [ ] `cd /workspaces/FDE_prep && git pull`
- [ ] `echo $SARVAM_API_KEY` prints your key (else `export SARVAM_API_KEY=sk_...`)
- [ ] Sample call audio exists: look in `sarvam-ai-cookbook/` for the call-analytics example's
      `sample_data/` (or any `.wav`/`.mp3` sample in the notebooks folders). Copy 1–2 files to
      `build-1/audio/`.
- [ ] Claude Code running in the Codespace terminal (`npm install -g @anthropic-ai/claude-code && claude` if not installed).
- [ ] Give Claude context once: *"For exact Sarvam SDK signatures, consult the notebooks in
      ../sarvam-ai-cookbook and https://docs.sarvam.ai/llms.txt — do not guess method names."*

**Authoritative references (point Claude here instead of letting it guess):**
- Cookbook notebooks: `sarvam-ai-cookbook/notebooks/` (stt, chat completion, call-analytics)
- Exact SDK signatures + gotchas: https://github.com/sarvamai/skills
- Model docs: https://docs.sarvam.ai/api-reference-docs/models/saaras · machine-readable index: https://docs.sarvam.ai/llms.txt

## Phase 1 — Transcription (30 min) → `build-1/transcribe.py`

**Prompt to Claude Code:**
> Create build-1/transcribe.py: a function `transcribe(path, mode)` that calls Sarvam's
> speech-to-text (Saaras) on an audio file using the `sarvamai` SDK — check
> ../sarvam-ai-cookbook/notebooks/stt for the exact API usage. Support at least the
> `transcribe` and `code-mixed` output modes. CLI: `python transcribe.py audio/call1.wav`
> prints both modes' outputs. Handle missing API key and API errors with clear messages.

**Your review checklist:** Is the API key read from env (never hardcoded)? What happens on a
network error? Then run it on your sample and **diff the two modes' outputs** — note one
concrete difference in `notes.md` (interview gold: "code-mixed mode kept the English loan
terms in Latin script instead of transliterating").

## Phase 2 — Structured analysis (40 min) → `build-1/analyze.py`

**Prompt to Claude Code:**
> Create build-1/analyze.py: send a call transcript to Sarvam's OpenAI-compatible chat
> completion endpoint (check ../sarvam-ai-cookbook/notebooks for usage) and extract a JSON
> object matching this schema: {intent: one of [complaint, query, request, escalation],
> entities: {names, amounts, dates, products as lists}, sentiment: positive|neutral|negative,
> summary: string <= 50 words, callback_needed: boolean}. Validate the response against the
> schema; on invalid JSON or schema mismatch, retry once with the validation error included
> in the prompt. IMPORTANT known gotcha: the response `content` can be None when reasoning
> consumes the token budget — detect and handle that case explicitly.

**Your review checklist:** Where's the retry? What happens after the second failure (should
surface a clear error, not crash)? Is the schema enforced or just hoped for? Ask Claude:
*"Show me exactly what happens if the model returns markdown-fenced JSON"* — a classic
real-world failure.

## Phase 3 — Pipeline + report (20 min) → `build-1/main.py`

**Prompt to Claude Code:**
> Create build-1/main.py: for each audio file in build-1/audio/, run transcribe (code-mixed
> mode) then analyze, and print a clean per-call report (file, intent, sentiment, entities,
> summary, callback_needed) plus a totals line. Write results to build-1/results.json.

Run the full pipeline end-to-end on your sample audio. This is your demo artifact — make
sure `python main.py` works from a fresh terminal.

## Phase 4 — Eval harness (50 min) → `build-1/evals/`

**Step 1 — Prompt to Claude Code (scaffold only):**
> Create build-1/evals/run_evals.py: loads test cases from build-1/evals/cases.json
> (format: [{transcript, expected: {intent, sentiment, callback_needed}, judge_criteria}]),
> runs analyze.py's extraction on each transcript, checks the deterministic fields
> (intent/sentiment/callback_needed) by exact match, and evaluates the summary with an
> LLM-as-judge call that answers a STRICTLY binary pass/fail against the case's
> judge_criteria string. Print a table: case id, field checks, judge verdict, and a final
> pass rate. No Likert scales — binary only.

**Step 2 — YOU write `cases.json` by hand (this is the actual skill):** 10–15 short
transcripts you compose (mix Hindi-English code-mixed, a clear complaint, an ambiguous one,
an angry customer with no actionable request, one with amounts/dates to extract, one empty/
garbage input). For each, set expected fields + a one-line binary judge criterion
("summary mentions the failed EMI payment: yes/no"). Edge cases matter more than volume.

**Step 3 — Run, read every failure, fix or annotate.** A failing case you can explain
("the judge is right — my prompt drops amounts on long transcripts; here's the fix") is
worth more in an interview than 15/15 green.

**Why this design (say this in the walkthrough):** error analysis first · binary > Likert ·
deterministic checks where possible, LLM-judge only where needed · the judge itself would
need human alignment (TPR/TNR) before you'd trust it at scale — cite Hamel's Evals FAQ:
https://hamel.dev/blog/posts/evals-faq/

## Phase 5 — Wrap (10 min)

- [ ] Update `build-1/README.md`: 3 lines — what it does, how to run, eval pass rate.
- [ ] `git add build-1/ notes.md && git commit -m "Build #1: call analytics + eval harness" && git push`
- [ ] Say the 60-second walkthrough of the whole build, out loud, once.

---

# AI-Assisted Extension Drill (45 min, HARD timer) — the R3 rehearsal

Same session, new discipline: this one is **timed and observed** (by you). Set a 45-min timer.

**Pick ONE extension** (in order of interview value):
1. **Language-ID routing**: detect the transcript's language mix (Sarvam Language ID API —
   in the cookbook) and route to a Hindi-first vs English-first analysis prompt.
2. **HTML report**: generate `build-1/report.html` from results.json — a clean table with
   per-intent counts (no frameworks, inline CSS).
3. **Second judge + agreement**: add a second LLM-judge with differently-worded criteria;
   report agreement rate between judges (and what disagreement tells you).

**The loop, explicitly (narrate it aloud as you go):**
1. Write a 3-line spec in `notes.md` BEFORE prompting.
2. Prompt Claude for increment 1 only. Read the diff. Run it.
3. Iterate in small steps. **Catch ≥1 AI mistake out loud** — there is always one.
4. At 40 min: stop adding, make it run clean, whatever state it's in.
5. (5 min) Retro in `notes.md`: which prompt phrasing worked, where the AI wasted time,
   what you'll do differently in the real R3.

**Commit:** `git add -A && git commit -m "extension drill: <what>" && git push`

---

## Known Sarvam gotchas (keep visible while building)

- Chat `content` can be **None** when reasoning eats the token budget — handle it.
- It's `client.text.translate()`, **not** `client.translate.translate()` — signatures live in https://github.com/sarvamai/skills
- Bulbul v3 400-errors on `pitch`/`loudness` params (not needed today, but know it).
- Rate limits exist on the free tier — if you hit 429s, add a small sleep/backoff between calls: https://docs.sarvam.ai/api-reference-docs/ratelimits

## If you're running out of time (priority order)

Phases 1–3 + five hand-written eval cases beats all phases half-done. The drill is
non-negotiable — cut Build #1 scope before you cut the timed drill; the drill is the
confirmed R3 format. Skip Phase 2's retry polish before you skip eval cases.
