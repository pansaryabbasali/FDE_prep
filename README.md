# Sarvam AI — FDE Interview Prep (2-Day Sprint)

A full-commitment, 2-day study plan for the **Forward Deployed Engineer** role at Sarvam AI,
built from a gap analysis of my resume against the JD, and researched online (July 2026).

## How to use this repo

1. Read **[00-gap-analysis.md](00-gap-analysis.md)** first (15 min) — it explains *why* the plan
   is weighted the way it is. Your strengths get talk-track prep only; your gaps get hours.
2. Execute **[01-day-1.md](01-day-1.md)** and **[02-day-2.md](02-day-2.md)** hour by hour.
   Each block says what to do, with which resource, and what "done" looks like.
3. Keep **[03-sarvam-cheatsheet.md](03-sarvam-cheatsheet.md)** open all weekend — memorize it.
   Interviewers expect you to design with *their* stack.
4. **[04-resource-library.md](04-resource-library.md)** is the full researched resource list by
   topic (with time estimates) — use it if you finish a block early or want to swap a resource.
5. **[05-interview-playbook.md](05-interview-playbook.md)** is for Day 2 evening: interview
   format intel, STAR stories mapped from your resume, the decomp method, and questions to ask.

## The one-paragraph strategy

The JD wants an engineer who can own a client engagement end-to-end and has **agents + evals +
voice/systems** depth. Your IBM Client Engineering experience already *is* the FDE job — the
gaps are vocabulary and tooling, not capability. So the sprint converts what you've done on
watsonx into the 2026 open-ecosystem stack: **LangGraph/MCP** (Day 1 morning), **evals as a
discipline** (Day 1 afternoon — the JD's biggest differentiator), **Sarvam's own APIs
hands-on** (Day 1 evening), **voice-agent architecture + Kafka + AI system design** (Day 2),
and interview execution (Day 2 evening). Two hands-on builds anchor it, because Sarvam's
reported interview format is a practical hackathon (one reported task: build a Voice Activity
Detector from scratch), not LeetCode.

## Doing the hands-on work with no local machine

You don't need a laptop setup — run everything in the browser:

1. **GitHub Codespaces** (main environment): on this repo's page click **Code → Codespaces →
   Create codespace**. You get VS Code + a Linux terminal in the browser, running on GitHub's
   servers. The `.devcontainer/` in this repo auto-installs everything in `requirements.txt`
   (sarvamai, langgraph, mcp, jupyter, numpy, audio libs) on first boot. Free personal quota
   is 120 core-hours/month — ~60 hours on the default 2-core machine, more than the whole
   sprint needs. Codespaces auto-stop when idle, so the quota stretches.
   - Put your Sarvam API key in the terminal each session: `export SARVAM_API_KEY=sk_...`
     (or add it once as a Codespaces secret: repo → Settings → Secrets → Codespaces).
   - Commit your build work from the Codespace terminal with plain `git add/commit/push` —
     it's already authenticated to this repo.
2. **Google Colab** (for notebooks): the sarvam-ai-cookbook and langchain-academy notebooks
   run fine on the free tier — open https://colab.research.google.com, File → Open notebook →
   GitHub tab, paste the repo URL. Zero setup, good for quick API experiments.
3. **Audio caveat**: cloud environments have no microphone. For the Day 2 voice build, work
   file-to-file (WAV in → WAV out) exactly as the plan's fallback describes — the learning is
   in the streaming APIs and buffers, not the mic.

## Timeboxes at a glance

| | Morning | Afternoon | Evening |
|---|---|---|---|
| **Day 1** | Agent patterns + LangGraph sprint | Framework breadth + MCP + **Evals deep block** | Build #1 on Sarvam APIs + context engineering |
| **Day 2** | Voice-agent architecture + **Build #2 (voice + VAD)** | Kafka/queues + AI system design drills + Sarvam memorization | Mock decomp + STAR stories + coding insurance |
