# Road to AGI - Every AI Model Since Transformers

Interactive timeline tracking **270+ AI models** from the original Transformer (2017) to the current frontier (March 2026).

**Live:** [countdowntoai.com](https://countdowntoai.com/)

## Features

- **Interactive scatter chart** — models plotted by date vs intelligence rating, with weighted trend line
- **Drag-to-zoom** — select any region of the chart to zoom in, double-click to reset
- **Filters** — by type (LLM, Diffusion, Reasoning, Multimodal, ASR, Text Diffusion), category (text, code, image, video, audio, multi), open/closed source, and year range
- **Sort** — by date (newest first) or intelligence ranking
- **Search** — filter by model name, company, or type
- **i18n** — English, Spanish, and Portuguese with auto-detection via timezone and browser language
- **Dark/Light theme** — toggle with persistence via localStorage
- **Timeline playback** — animated reveal of models chronologically
- **Card tooltips** — comparative stats (this model vs type average vs type max)

## Intelligence Scale

Relative 0-100 scale calibrated against public benchmarks (AIME, SWE-bench, MMLU, HLE, ARC-AGI, GPQA), expert opinions, and market positioning. Not absolute metrics.

| Range | Era | Examples |
|-------|-----|----------|
| 5-15 | 2017-2018 | Transformer, ELMo, GPT-1, BERT |
| 15-30 | 2019-2021 | GPT-2, GPT-3, DALL-E 1 |
| 30-45 | 2022-2023 | ChatGPT, GPT-4, Claude 1-2, Llama 1-2 |
| 45-60 | Early 2024 | GPT-4o, Claude 3, Gemini 1.5, FLUX.1 |
| 60-75 | Late 2024-Mid 2025 | Claude 3.5/3.7, DeepSeek-R1, Grok-3/4 |
| 75-85 | Late 2025 | GPT-5.1/5.2, Opus 4/4.5, Gemini 3 |
| 85-95 | Early 2026 | Opus 4.6, Sonnet 4.6, GPT-5.4, Gemini 3.1 |

## Tech Stack

Single HTML file — zero dependencies, zero build step. Just HTML + CSS + vanilla JS.

## Updating

See [UPDATE_GUIDE.md](UPDATE_GUIDE.md) for a reusable prompt to audit and add new models.

## License

MIT
