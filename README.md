```text
   ████████╗██████╗  █████╗ ███╗   ██╗███████╗██╗     ██╗
   ╚══██╔══╝██╔══██╗██╔══██╗████╗  ██║██╔════╝██║     ██║
      ██║   ██████╔╝███████║██╔██╗ ██║███████╗██║     ██║
      ██║   ██╔══██╗██╔══██║██║╚██╗██║╚════██║██║     ██║
      ██║   ██║  ██║██║  ██║██║ ╚████║███████║███████╗██║
      ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝
```

<div align="center">

**Real-time multi-modal speech translation with hybrid cloud and local AI.**

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green?logo=fastapi)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-19-61DAFB?logo=react)](https://react.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

*Speak in one language. Hear it back in another. Skip the copy-paste translation loop.*

</div>

---

## The Real Bottleneck in Cross-Language Communication

Every translation tool on the market gives you a text box and a swap button. Almost none of them solve the part that actually breaks the flow:

> You're in a meeting with someone who speaks Hindi. You pull out your phone, open a translator, type what you want to say, copy the result, read it out loud — badly — and wait while they do the same thing back. The conversation dies somewhere between the third tab switch and the autocorrect mishap.
>
> Or you have a PDF invoice in Spanish. You copy-paste paragraphs into Google Translate, lose the formatting, guess at the context, and end up with something that's technically translated but practically useless.

That's not translation. That's friction with a language dropdown.

The bottleneck in multilingual communication has never been about translation accuracy alone. It's about **getting speech in and translated speech out without breaking the conversational flow**. If your tool still expects a human to type, copy, paste, and read aloud, you haven't solved the problem — you've just moved the dictionary into a browser.

**Transli attacks that bottleneck directly.**

You speak into the mic. The AI hears it, transcribes it, translates it, and speaks it back in the target language. The whole loop — voice in, voice out — completes in 1.5 to 9.6 seconds depending on the provider combination.

---

## How It Works

```text
   ┌──────────────────────────┐
   │  Speak into Browser Mic   │
   └──────────┬───────────────┘
              │
              ▼
   ┌──────────────────────────────────┐
   │  Speech-to-Text (STT)            │
   │  → ElevenLabs Scribe (cloud)     │
   │  → OpenAI Whisper base (local)   │
   └──────────┬───────────────────────┘
              │
              ▼
   ┌──────────────────────────────────┐
   │  Translation                     │
   │  → Gemini 2.5 Flash (cloud)      │
   │  → Meta NLLB-200 600M (local)    │
   │  → glossary + context injection  │
   └──────────┬───────────────────────┘
              │
              ▼
   ┌──────────────────────────────────┐
   │  Text-to-Speech (TTS)            │
   │  → ElevenLabs (cloud)            │
   │  → Piper ONNX (local, CPU)       │
   │  → gTTS (free fallback)          │
   └──────────┬───────────────────────┘
              │
              ▼
   ┌──────────────────────────────────┐
   │  Play Translated Audio            │
   │  → display transcript            │
   │  → save to history               │
   └──────────────────────────────────┘
```

The entire user flow: **Speak → Translate → Listen → Done.**

---

## Features

**Quick Translate** — Speak into the mic or type text. Get back a transcript, translation, and synthesized audio. Supports one-to-many mode: translate into Hindi, French, and German simultaneously with independent audio per language.

**Live Conversation** — Two speakers, two languages, alternating turns. Context from recent turns is passed to the AI so pronouns and references stay consistent across the conversation.

**File & Document Translation** — Upload a PDF, Word doc, plain text file, or image. Transli extracts content (OCR for images) and translates it with side-by-side display and downloadable output.

**Custom Glossary** — Define term pairs like `NIT = NIT` or `neural network = न्यूरल नेटवर्क`. Terms are enforced in every translation — injected into Gemini's prompt or applied as post-processing for NLLB.

**Session Summaries** — After a live session, click Summarize. Gemini generates a plain-language summary of everything discussed.

**Provider Switching at Runtime** — Choose between cloud and local AI for each pipeline stage without restarting the server. Mix and match: ElevenLabs or Whisper for STT, Gemini or NLLB for translation, ElevenLabs/Piper/gTTS for TTS.

**Fully Offline Mode** — Whisper + NLLB + Piper. No API keys, no internet, benchmarked at **1.49s total**. Fastest configuration.

**Translation History** — Every session is saved to browser localStorage with full metadata. Export as `.txt` or `.json`.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React 19, Vite, Tailwind CSS 4 |
| Backend | Python 3.11, FastAPI, Uvicorn |
| STT | ElevenLabs Scribe v1, OpenAI Whisper |
| Translation | Google Gemini 2.5 Flash, Meta NLLB-200 |
| TTS | ElevenLabs, Piper ONNX, gTTS |
| OCR | Tesseract + Pillow |
| Documents | PyPDF2, python-docx |
| Audio | FFmpeg |
| GPU | CUDA (Whisper + NLLB), CPU (Piper) |

---

## Supported Languages

| Indian | International |
|---|---|
| English, Hindi, Bengali, Telugu | Chinese (Simplified & Traditional) |
| Marathi, Tamil, Urdu, Gujarati | French, German, Russian |
| Punjabi, Sanskrit | Japanese, Korean, Arabic |

---

## Provider Benchmark

All 12 provider combinations tested on the same audio clip.

| # | STT | Translation | TTS | Total |
|---|---|---|---|---|
| 1 | ElevenLabs | Gemini | ElevenLabs | 9.64s |
| 2 | ElevenLabs | Gemini | Piper | 20.31s |
| 3 | ElevenLabs | Gemini | gTTS | 15.27s |
| 4 | ElevenLabs | NLLB | ElevenLabs | 10.20s |
| 5 | ElevenLabs | NLLB | Piper | 8.61s |
| 6 | ElevenLabs | NLLB | gTTS | 17.83s |
| 7 | Whisper | Gemini | ElevenLabs | 8.56s |
| 8 | Whisper | Gemini | Piper | 7.06s |
| 9 | Whisper | Gemini | gTTS | 15.28s |
| 10 | Whisper | NLLB | ElevenLabs | 6.92s |
| **11** | **Whisper** | **NLLB** | **Piper** | **1.49s ⚡** |
| 12 | Whisper | NLLB | gTTS | 14.00s |

**Fastest overall** — #11 (Whisper + NLLB + Piper): 1.49s. Fully local, fully free, fully offline.  
**Best cloud hybrid** — #8 (Whisper + Gemini + Piper): 7.06s. Fast local STT, intelligent context-aware translation, free local TTS.

---

## Local Setup

### Prerequisites

- Python 3.11+
- Node.js 18+
- FFmpeg
- (Optional) NVIDIA GPU with CUDA for Whisper and NLLB local models

**Install FFmpeg:**

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install -y ffmpeg tesseract-ocr

# macOS
brew install ffmpeg tesseract

# Windows — download from https://ffmpeg.org/download.html and add to PATH
```

### 1. Clone the repo

```bash
git clone https://github.com/sombabaofficial/Transli.git
cd Transli
```

### 2. Backend setup

```bash
cd backend
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

Create your `.env` file:

```bash
# backend/.env
GEMINI_API_KEY="your-google-gemini-api-key"
ELEVENLABS_API_KEY="your-elevenlabs-api-key"
```

> API keys are optional if you use fully local providers (Whisper + NLLB + Piper). Get Gemini free at [aistudio.google.com](https://aistudio.google.com). Get ElevenLabs at [elevenlabs.io](https://elevenlabs.io).

Start the backend:

```bash
uvicorn main:app --reload --port 8000
```

### 3. Frontend setup

```bash
cd frontend
npm install
npm run dev
```

Open [http://localhost:5173](http://localhost:5173).

---

## Deployment

### Backend → Render.com

1. Connect your GitHub repo at [render.com](https://render.com)
2. **Root Directory:** `backend`
3. **Build Command:** `pip install -r requirements.txt`
4. **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables: `GEMINI_API_KEY`, `ELEVENLABS_API_KEY`, `FRONTEND_URL`

### Frontend → Vercel.com

1. Import your repo at [vercel.com](https://vercel.com)
2. **Root Directory:** `frontend`
3. Add environment variable: `VITE_API_URL` = your Render backend URL

> On free-tier hosting (no GPU), use Gemini + ElevenLabs providers. Local models (Whisper, NLLB, Piper) require CUDA GPU.

---

## Architecture Notes

The React frontend handles recording, playback, and UI state. The FastAPI backend is a provider abstraction layer — it keeps API keys server-side, dispatches to the correct model, and handles fallbacks automatically (NLLB → Gemini on unsupported input; ElevenLabs TTS → gTTS on failure). Whisper and NLLB run on CUDA when available, CPU otherwise. Piper runs on CPU intentionally to keep GPU memory free for inference models. Parallel translation across multiple target languages is handled with `asyncio.gather()` — wall-clock time equals the slowest single translation, not the sum.

---

## License

MIT License. See [`LICENSE`](LICENSE) for details.

---

<div align="center">

**Stop typing what you want to say.**

[Get Started with Transli →](https://github.com/sombabaofficial/Transli)

</div>
