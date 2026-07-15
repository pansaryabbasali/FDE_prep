# Build #2 — VAD from scratch + Sarvam voice loop (Day 2, 10:30–12:30)

## Part 1 (~45 min): `vad/` — Voice Activity Detector in numpy, no frameworks

The reported Sarvam hackathon task. Read a WAV → frame it (20–30 ms windows, 10 ms hop) →
short-time energy + zero-crossing rate → adaptive noise-floor threshold + hangover smoothing
→ output speech segments with timestamps. Then compare your segments against `webrtcvad`
(installed via requirements.txt) on the same file.

Vocabulary to be fluent in: sample rate, frame size, hop length, SNR, hangover.

## Part 2 (~75 min): `agent/` — minimal Sarvam voice loop

Audio in → Saaras v3 **WebSocket streaming STT** → Sarvam-30B chat completion →
**Bulbul v3 streaming TTS** → audio out. Half-duplex/turn-based is fine.
Reference: the voice-agents skill in [sarvamai/skills](https://github.com/sarvamai/skills).

Cloud environments have no mic — work file-to-file (WAV in → WAV out). The learning is in
the streaming APIs and buffers, not the microphone.

## Done when

Your VAD's segments roughly match webrtcvad's on a sample file, and a WAV question goes in
one end of your pipeline and a spoken answer comes out the other.
