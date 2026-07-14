# Gap Analysis — Resume vs. Sarvam FDE JD

## Strengths (prep a talk track, don't study)

| JD requirement | Your evidence | How to frame it |
|---|---|---|
| "Own the technical arc of customer engagements" | IBM Client Engineering: discovery → architecture → build → demo → deployment across BFSI, state gov, defense, manufacturing | This *is* the FDE job. Lead every behavioral answer with it. |
| RAG at production depth | Two-model RAG for AIOps RCA (Granite + Llama 3.3, 128K ctx), tuned chunking/retrieval/prompt ordering against lost-in-the-middle, on-prem UAT install | You already fought context rot before it had a name — connect it to the 2026 "context engineering" vocabulary on Day 1 evening. |
| Regulated / on-prem deployments ("even better if") | Defense entity, PSU bank, state governments, on-premises UAT install, watsonx.governance GRC | Sarvam's whole sales narrative is sovereignty + BFSI + air-gapped (their Arya platform deploys air-gapped). Direct hit. |
| **Used Sarvam's products** ("even better if") | OCR via **Sarvam Document Intelligence** in the state-government chatbots | Gold. You've already shipped their API inside a government engagement at IBM. Say this in the first five minutes. |
| Multi-agent systems | watsonx Orchestrate ADK document-intelligence pipeline (ingestion → entity extraction → routing to inventory/ELM) | You know *an* ADK deeply; Day 1 maps its concepts onto LangGraph / Google ADK so you speak the JD's language. |
| Multilingual AI for India | Farmer-advisory + citizen Q&A assistants for two state governments; Llama 4 Maverick; 1000+-doc multilingual corpora | Population-scale Indic AI is literally their mission. |
| Client-facing communication | Trusted technical point of contact; mentoring; EY consulting | Covers "customer instinct." |

## Gaps (this is where the 48 hours go)

Priority-ordered by (JD emphasis × resume weakness × interview likelihood):

1. **Named agentic frameworks — LangGraph, LlamaIndex, Google ADK.** The JD names them; your
   resume only shows watsonx Orchestrate ADK. You need to *build* in LangGraph (not just read)
   and speak Google ADK / LlamaIndex concepts. → Day 1 morning (~4 hrs).
2. **Evals mindset.** The JD dedicates a full paragraph to it ("clear opinions on what good
   evaluation looks like versus what's just noise"); your resume says "familiar." This is the
   single biggest differentiator between candidates at this level. → Day 1 afternoon (~2.5 hrs)
   + eval harness inside both hands-on builds.
3. **Voice/conversational systems.** Sarvam's revenue engine is Samvaad (voice agents, ~80% of
   ARR); engagements are "voice and conversational systems at enterprise customers." You have
   zero voice on the resume, and their reported hackathon task was **building a VAD from
   scratch**. → Day 2 morning (~4.5 hrs incl. build).
4. **Messaging/queues — Kafka, SQS.** JD names them under "systems thinker"; resume has none.
   You need working vocabulary (partitions, consumer groups, DLQs, idempotency, backpressure),
   not operational depth. → Day 2 early afternoon (~1.5 hrs).
5. **MCP servers.** Named in the JD ("agentic workflows and the MCP servers... that underpin
   them"). One quickstart + build a toy server + read Sarvam's own `sarvam-mcp`. → Day 1 (~1 hr).
6. **Sarvam's stack itself.** Model lineup, API surface, pricing, Arya, Samvaad, the tokenizer
   story, partnerships. Interviewers expect you to design with their models. → Day 1 setup +
   Day 2 memorization block + cheat sheet.
7. **Structured outputs / tool calling across providers.** You've done agentic tool use on
   watsonx; brush up on `strict` schemas, constrained decoding, open-model tooling
   (Outlines/XGrammar). → Day 1 (~1 hr, folded into evals/agents blocks).
8. **AWS/GCP.** You're Azure-first. Don't study consoles in 2 days — prepare the honest line:
   "cloud-portable via K8s/OpenShift; services map 1:1 (S3↔Blob/GCS, SQS↔Service Bus/PubSub);
   I pick up stacks in hours" — and know SQS/SNS/Lambda/S3 at diagram level from the Kafka block.
9. **Coding under time pressure.** Their format rewards practical Python + audio/streaming/numpy
   fluency over LeetCode. → Both builds + Day 2 evening insurance hour.

## What deliberately gets almost no time

- Fine-tuning/training internals (FDE role is integration-side; know the decision framework only).
- Classic DSA grinding (1 insurance hour max — evidence says practical hackathon, not LeetCode).
- AWS/GCP console specifics (talk track only, see above).
- Frontend/UI work (not in the JD).
