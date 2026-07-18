# Sarvam AI — FDE Interview Prep (4-Day Sprint)

A 4-day (Thu–Sun, ~9h/day) study plan for the **Forward Deployed Engineer** role at Sarvam AI,
built from a gap analysis of my resume against the JD, researched online (July 2026), and
structured around the **confirmed interview loop**:

- **R1 — Coding Assessment**: code read AND write + background, intent, impact discussion
- **R2 — Business Case Study**: business + technical scenarios, thinking evaluated
- **R3 — Live Build**: on-the-spot problem, build a small application **using the help of AI**
- **R4 — Hiring Manager** round

## The main interface

**The live dashboard: https://pansaryabbasali.github.io/FDE_prep/** — tabbed UI with all four
day plans (step-by-step instructions, links, done-criteria, progress checkboxes), the gap
analysis, Sarvam cheat sheet, interview playbook, and full resource library.

## Repo contents

| File | What |
|---|---|
| `index.html` | The dashboard (auto-deployed to GitHub Pages on every push) |
| [00-gap-analysis.md](00-gap-analysis.md) | Resume vs JD: strengths to frame, gaps that get the hours |
| [01-day-plans.md](01-day-plans.md) | Condensed printable outline of all 4 days |
| [03-sarvam-cheatsheet.md](03-sarvam-cheatsheet.md) | Sarvam models, APIs, products, timeline — memorize |
| [04-resource-library.md](04-resource-library.md) | Full researched resource list by topic |
| [05-interview-playbook.md](05-interview-playbook.md) | Round-by-round prep, STAR stories, questions to ask |
| `notes.md` | Flashcards + drill outputs (filled during the sprint) |
| `build-1/ build-2/ build-3/` | Sprint build work (committed as interview evidence) |

## Doing the hands-on work with no local machine

1. **GitHub Codespaces** (main environment): repo → **Code → Codespaces → Create codespace**.
   The `.devcontainer/` auto-installs `requirements.txt` (sarvamai, langgraph, mcp, jupyter,
   numpy, audio libs). Free quota: 120 core-hours/month ≈ 60 hours on the 2-core machine.
   - API key: `export SARVAM_API_KEY=sk_...` per session, or add it once as a Codespaces
     secret (repo → Settings → Secrets → Codespaces).
   - Commit build work from the Codespace terminal with plain `git add/commit/push`.
   - Reference projects go in sibling folders: `cd /workspaces && git clone ...`
     (they're also gitignored if cloned inside the repo).
2. **Google Colab** for notebooks: cookbook and langchain-academy notebooks run on the free tier.
3. **AI assistant for R3 practice**: Copilot Chat inside the Codespace, or a claude.ai/code
   session on this repo — practice the spec → prompt → verify → iterate loop before the real round.
4. **Audio caveat**: no mic in cloud environments — voice builds work file-to-file (WAV in →
   WAV out), which is where the learning is anyway.

## Days at a glance

| Day | Focus | Round emphasis |
|---|---|---|
| **Day 1 (Thu)** | Agents (LangGraph/ADK/LlamaIndex), MCP, context engineering + code-reading drill #1 | R1 |
| **Day 2 (Fri)** | Evals deep block, Build #1 on Sarvam APIs (solo), first AI-assisted drill | R1 · R3 |
| **Day 3 (Sat)** | Voice architecture + Build #2 (VAD + streaming loop), Kafka/SQS, system design, Sarvam memorization | R2 · R1 |
| **Day 4 (Sun)** | Full rehearsal: R1 code+narrative → R2 mock ×2 → R3 timed AI build → R4 stories | All |
