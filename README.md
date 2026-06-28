<div align="center">

```
████████╗██████╗  █████╗ ███╗   ██╗███████╗██╗     ██╗
╚══██╔══╝██╔══██╗██╔══██╗████╗  ██║██╔════╝██║     ██║
   ██║   ██████╔╝███████║██╔██╗ ██║███████╗██║     ██║
   ██║   ██╔══██╗██╔══██║██║╚██╗██║╚════██║██║     ██║
   ██║   ██║  ██║██║  ██║██║ ╚████║███████║███████╗██║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝
```

### Real-time AI Voice Translation — speak once, hear it in any language.

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev)
[![Tailwind](https://img.shields.io/badge/Tailwind_CSS-4-38BDF8?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-F59E0B?style=for-the-badge)](LICENSE)

[Live Demo](#deployment) · [Quick Start](#quick-start) · [Features](#features) · [Benchmarks](#provider-benchmark)

</div>

---

## What is Transli?

Transli is a full-stack AI translation platform that goes beyond text boxes and swap buttons. It closes the **full speech loop** — you speak, it transcribes, translates, and speaks back in the target language.

Every piece of the pipeline is swappable at runtime between **cloud** and **local** providers. You can run it entirely offline with no API keys, or hook it up to ElevenLabs and Gemini for maximum quality. The fastest fully-local configuration completes the entire voice-in → voice-out loop in **1.49 seconds**.

> **Built for:** NIT Agartala Final Year Project — targeting impact for 2000+ students across language barriers in academia, research, and cross-regional communication.

---

## The Problem

Every translation tool gives you a text box. None of them solve the part that actually breaks conversations:

```
You want to say something in Hindi
→ Open phone
→ Type it out
→ Copy the translation
→ Read it aloud (badly)
→ Wait while the other person does the same
→ The conversation dies
```

That's friction, not translation. **Transli removes every manual step in that loop.**

---

## Features

| | Feature | Description |
|---|---|---|
| 🎙️ | **Quick Translate** | Speak or type — get transcript, translation, and synthesized audio instantly. One-to-many mode translates into up to 10 languages simultaneously. |
| 💬 | **Live Conversation** | Alternating bilingual conversation with context memory. AI maintains pronoun consistency and topic flow across turns. |
| 📄 | **File & Document Translation** | Upload PDF, DOCX, TXT, or images. OCR extracts text from images. Side-by-side output with download. |
| 🔁 | **Provider Switching** | Swap STT, translation, and TTS engines at runtime — no restart needed. 12 tested combinations. |
| 📖 | **Custom Glossary** | Define term mappings (e.g. `ISRO = ISRO`). Enforced in every translation via prompt injection or post-processing. |
| ⚡ | **Fully Offline Mode** | Whisper + NLLB + Piper — no API keys, no internet. Benchmarked at 1.49s end-to-end. |
| 🧠 | **AI Session Summaries** | One click generates a plain-language Gemini summary of the entire conversation. |
| 📜 | **Translation History** | Auto-saved to localStorage. Search, filter, export as `.txt` or `.json`. |

---

## How It Works

```
  🎤 Speak
      │
      ▼
  ┌─────────────────────────────────────┐
  │  Speech-to-Text (STT)               │
  │  ├─ ElevenLabs Scribe v1  (cloud)   │
  │  └─ OpenAI Whisper base   (local)   │
  └──────────────────┬──────────────────┘
                     │
                     ▼
  ┌─────────────────────────────────────┐
  │  Translation                        │
  │  ├─ Google Gemini 2.5 Flash (cloud) │
  │  └─ Meta NLLB-200 600M     (local)  │
  │       + glossary + context memory   │
  └──────────────────┬──────────────────┘
                     │
                     ▼
  ┌─────────────────────────────────────┐
  │  Text-to-Speech (TTS)               │
  │  ├─ ElevenLabs multilingual (cloud) │
  │  ├─ Piper ONNX              (local) │
  │  └─ gTTS                  (free)    │
  └──────────────────┬──────────────────┘
                     │
                     ▼
  🔊 Hear it in the target language
```

---

## Tech Stack

<div align="center">

| Layer | Technology |
|:---|:---|
| **Frontend** | React 19, Vite, Tailwind CSS 4, Lucide Icons |
| **Backend** | Python 3.11, FastAPI, Uvicorn, asyncio |
| **STT** | ElevenLabs Scribe v1, OpenAI Whisper (CUDA) |
| **Translation** | Google Gemini 2.5 Flash, Meta NLLB-200-distilled-600M |
| **TTS** | ElevenLabs multilingual v2, Piper ONNX, gTTS |
| **Documents** | PyPDF2, python-docx, Pillow + Tesseract OCR |
| **Audio** | FFmpeg (WAV → MP3 conversion) |
| **GPU** | CUDA for Whisper & NLLB · CPU for Piper |

</div>

---

## Supported Languages

<div align="center">

| Indian Languages | International Languages |
|:---|:---|
| English · Hindi · Bengali · Telugu | Chinese Simplified · Chinese Traditional |
| Marathi · Tamil · Urdu · Gujarati | French · German · Russian |
| Punjabi · Sanskrit | Japanese · Korean · Arabic |

**18 languages total · 12 provider combinations · All tested**

</div>

---

## Provider Benchmark

All 12 STT × Translation × TTS combinations tested on the same audio clip.

| # | STT | Translation | TTS | Total Time |
|:---:|:---|:---|:---|:---:|
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
| **11** ⚡ | **Whisper** | **NLLB** | **Piper** | **1.49s** |
| 12 | Whisper | NLLB | gTTS | 14.00s |

> **⚡ Fastest** — #11 (Whisper + NLLB + Piper): **1.49s** — fully local, fully free, fully offline.  
> **☁️ Best Cloud Hybrid** — #8 (Whisper + Gemini + Piper): **7.06s** — local STT, intelligent translation, free TTS.

---

## Quick Start

### Prerequisites

- Python 3.11+, Node.js 18+, Git
- FFmpeg installed and on PATH
- *(Optional)* NVIDIA GPU with CUDA drivers — for fast local Whisper + NLLB

```bash
# Install FFmpeg
# Ubuntu/Debian
sudo apt install -y ffmpeg tesseract-ocr

# macOS
brew install ffmpeg tesseract

# Windows — https://ffmpeg.org/download.html → add bin/ folder to PATH
```

### 1 — Clone

```bash
git clone https://github.com/sombabaofficial/Transli.git
cd Transli
```

### 2 — Backend

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set API keys (skip this if using fully local mode)
cp .env.example .env
# Edit .env and add your keys
```

```env
# backend/.env
GEMINI_API_KEY="your-gemini-api-key"        # free at aistudio.google.com
ELEVENLABS_API_KEY="your-elevenlabs-key"    # free tier at elevenlabs.io
```

```bash
# Start backend
uvicorn main:app --reload --port 8000
```

### 3 — Frontend

```bash
cd frontend
npm install
npm run dev
```

Open **http://localhost:5173** and speak your first translation.

---

## Deployment

### Backend → [Render.com](https://render.com) (free tier)

| Setting | Value |
|---|---|
| Root Directory | `backend` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn main:app --host 0.0.0.0 --port $PORT` |

**Environment Variables to set:**
- `GEMINI_API_KEY`
- `ELEVENLABS_API_KEY`
- `FRONTEND_URL` ← your Vercel URL (for CORS)

### Frontend → [Vercel.com](https://vercel.com) (free tier)

| Setting | Value |
|---|---|
| Root Directory | `frontend` |
| Build Command | `npm run build` |
| Output Directory | `dist` |

**Environment Variables to set:**
- `VITE_API_URL` ← your Render backend URL

> **Note:** Free cloud hosting has no GPU. Set providers to **Gemini** (translation) and **ElevenLabs** (STT/TTS) for cloud deployment. Local models require CUDA.

---

## Project Structure

```
Transli/
├── backend/
│   ├── main.py                  # FastAPI app, all endpoints
│   ├── config.py                # API key config
│   ├── language_catalog.py      # Supported language definitions
│   ├── requirements.txt
│   ├── piper_voices/            # Local ONNX voice models
│   └── services/
│       ├── stt.py               # STT dispatcher
│       ├── stt_whisper.py       # Local Whisper (CUDA)
│       ├── stt_elevenlabs.py    # Cloud STT
│       ├── translation.py       # Translation dispatcher
│       ├── translation_gemini.py# Cloud Gemini translation
│       ├── translation_nllb.py  # Local NLLB-200 (CUDA)
│       ├── tts.py               # TTS dispatcher
│       ├── tts_piper.py         # Local Piper ONNX
│       └── text_extract.py      # PDF/DOCX/image extraction
├── frontend/
│   └── src/
│       ├── pages/
│       │   ├── QuickTranslate.jsx
│       │   ├── LiveConversation.jsx
│       │   ├── FileTranslation.jsx
│       │   └── HistoryDownloads.jsx
│       └── config/
│           ├── api.js           # Central API base URL
│           └── languages.js     # Language list
├── render.yaml                  # Render deployment config
└── README.md
```

---

## Architecture Decisions

**Provider Abstraction** — Every pipeline stage (STT, translation, TTS) has a dispatcher that routes to the selected provider and handles fallbacks. Swapping providers requires no code changes — just a settings toggle in the UI.

**Parallel Multi-language** — `asyncio.gather()` runs all target language translations and TTS calls concurrently. Total wall-clock time = slowest single language, not the sum.

**NLLB Chunking** — NLLB-200 is a sentence-pair model best suited for ≤150 tokens. Long inputs are split at sentence boundaries before inference to prevent silent sentence drops.

**GPU Strategy** — Whisper and NLLB run on CUDA (GPU) for speed. Piper runs on CPU intentionally to keep VRAM free for the inference models. Falls back to CPU automatically if no GPU is detected.

**Smart Fallbacks** — NLLB falls back to Gemini if it detects Romanized Indian text (which it cannot handle). ElevenLabs TTS falls back to gTTS on any API failure.

---

## Contributing

Pull requests are welcome.

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

Please keep PRs focused — one feature or fix per PR.

---

## Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper) — open-source speech recognition
- [Meta NLLB-200](https://huggingface.co/facebook/nllb-200-distilled-600M) — multilingual neural machine translation
- [Piper TTS](https://github.com/rhasspy/piper) — fast local text-to-speech
- [ElevenLabs](https://elevenlabs.io) — high-quality cloud STT and TTS
- [Google Gemini](https://aistudio.google.com) — context-aware translation and summarization

---

## License

MIT License © 2025 [Somesh Raj](https://github.com/sombabaofficial)

See [`LICENSE`](LICENSE) for full terms.

---

<div align="center">

**Stop typing what you want to say.**

[⭐ Star this repo](https://github.com/sombabaofficial/Transli) · [Report a Bug](https://github.com/sombabaofficial/Transli/issues) · [Request a Feature](https://github.com/sombabaofficial/Transli/issues)

</div>
