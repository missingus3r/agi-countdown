# AI Timeline Update Guide

This is a reusable prompt/guide for any LLM to audit and update the AI models list in `ai-timeline-combined.html`. The data lives in a single JavaScript array `const models = [...]` (starting around line 241).

---

## Data Schema

Each model is a JS object with exactly 7 fields:

```js
{
  name: "Model Name",       // String - official model name
  date: "YYYY-MM-DD",       // String - release/announcement date (ISO format)
  company: "Company Name",  // String - developer/organization
  open: true,               // Boolean - true if open-weight/open-source, false if proprietary
  intelligence: 45,         // Number (1-100) - capability rating on the leveled scale (frontier ≈ 66, see Scale Reference)
  type: "LLM",              // String - model category (see valid values below)
  cat: "text"               // String - primary output modality (see valid values below)
}
```

### Valid `type` values

| Type | Description |
|------|-------------|
| `LLM` | Standard language model (text in, text out) |
| `Diffusion` | Diffusion-based generative model (images, video, audio) |
| `Reasoning` | Extended-thinking / chain-of-thought model |
| `Multimodal` | Model with native multi-modal capabilities |
| `ASR` | Automatic speech recognition |
| `Text Diffusion` | Diffusion-based text generation (e.g., Mercury/dLLM) |

### Valid `cat` values

| Cat | Description |
|-----|-------------|
| `text` | Text generation |
| `image` | Image generation |
| `video` | Video generation |
| `audio` | Audio/music generation |
| `multi` | Multi-modal (text + vision + more) |
| `code` | Code generation (specialized) |
| `reasoning` | Reasoning-focused |

---

## The Update Prompt

Copy everything below and give it to any LLM with internet access:

---

### PROMPT START

You are updating an AI models timeline. Follow these steps exactly:

**Step 1: Read the current data**

Read the file `ai-timeline-combined.html` and locate the `const models = [...]` array. Note every existing model name to avoid duplicates.

**Step 2: Find the cutoff date**

Identify the most recent model by `date` field. All models on or before this date are already covered. You are looking for models released AFTER this date.

**Step 3: Review existing providers**

Compile the full list of companies already in the dataset (see Provider Checklist below). You will check each one for new releases.

**Step 4: Research new models**

Search the internet systematically for new AI models released after the cutoff date. Cover ALL of the following categories:

- **LLMs (text):** New foundation models, chat models, instruction-tuned variants
- **Reasoning models:** New chain-of-thought / extended-thinking models
- **Code models:** New code-specialized LLMs
- **Image generation:** New diffusion models, image generators
- **Video generation:** New video AI models
- **Audio/Music:** New music generation, TTS, audio AI models
- **ASR:** New speech recognition models
- **Multimodal:** New models with native multi-modal input/output
- **Text Diffusion:** New speculative/diffusion-based text generation

For each existing provider, search for: `"[Company] new AI model [current year]"` or check their official blog/announcements.

**Step 5: Check for NEW companies/providers**

Search for new AI companies or labs that have released notable models but are NOT yet in the provider list. Look for:
- New startups with breakout models
- University/research lab releases
- New entrants from major tech companies
- Chinese AI labs with new internationally notable models

**Step 6: Assign ratings**

For each new model, assign an `intelligence` value using the Scale Reference section below. Compare against similar existing models to maintain consistency.

**Step 7: Output the entries**

Output ONLY the new entries as JS objects, ready to paste into the array. Use this exact format:

```js
  {name:"Model Name",date:"YYYY-MM-DD",company:"Company",open:false,intelligence:70,type:"LLM",cat:"text"},
```

Rules:
- Use double quotes for string values
- No trailing comma on the last entry
- Date must be ISO format (YYYY-MM-DD)
- If exact release date is unknown, use the 1st or 15th of the month
- `open` is `true` only if model weights are publicly downloadable
- Do NOT add models that are merely announced but not yet released/available
- Do NOT duplicate any model already in the list (check by name AND company)

### PROMPT END

---

## Complete Provider Checklist

Systematically check each of these providers for new releases:

### Major LLM Labs
- **OpenAI** - GPT series, o-series reasoning, DALL-E, Sora, Codex, GPT Image
- **Google / DeepMind** - Gemini, Gemma, Imagen, Veo, Lyria, Nano Banana, Gemini Diffusion
- **Anthropic** - Claude Opus, Sonnet, Haiku series
- **Meta** - Llama series, Movie Gen, MusicGen/AudioCraft
- **xAI** - Grok series, Aurora, Grok Imagine Video
- **DeepSeek** - DeepSeek-V series, DeepSeek-R reasoning series
- **Mistral AI** - Mistral, Mixtral, Mistral Large, Codestral, Devstral, Magistral, Ministral, Voxtral

### Chinese AI Labs
- **Alibaba** - Qwen series, Qwen-Image, Wan (video), Qwen-Coder
- **Baidu** - Ernie series
- **Zhipu AI** - GLM series (also Tsinghua/Zhipu for CogVideo)
- **Moonshot AI** - Kimi K series
- **ByteDance** - Seed series, Seedance (video), Seedream (image)
- **Tencent** - Hunyuan series
- **Kuaishou** - Kling series (video)
- **Xiaomi** - MiMo series
- **MiniMax** - MiniMax-M series, Hailuo AI (video)
- **01.AI** - Yi series

### Enterprise & Infrastructure
- **Microsoft** - Phi series
- **Amazon** - Nova series
- **NVIDIA** - Nemotron series, Megatron
- **IBM** - Granite series
- **Cohere** - Command R series
- **AI21 Labs** - Jurassic, Jamba series
- **LG AI** - EXAONE series

### Open-Source & Research
- **AI2 (Allen Institute)** - OLMo series
- **HuggingFace** - DistilBERT, SmolLM, etc.
- **BigScience** - BLOOM
- **TII** - Falcon series
- **Essential AI** - Rnj series
- **Liquid AI** - LFM series
- **AllenNLP** - ELMo (historical)
- **fast.ai** - ULMFiT (historical)

### Image Generation
- **Midjourney** - Midjourney v-series
- **Stability AI** - Stable Diffusion series, Stable Video Diffusion
- **Black Forest Labs** - FLUX series
- **Recraft** - Recraft V series
- **Ideogram** - Ideogram series
- **Inception** - Mercury (Text Diffusion / dLLM)

### Video Generation
- **Runway** - Gen series
- **Pika** - Pika series
- **Luma AI** - Dream Machine, Ray series
- **Genmo** - Mochi series
- **Lightricks** - LTX Video series

### Audio & Music
- **Suno** - Suno v-series, Bark TTS
- **Udio** - Udio v-series
- **ElevenLabs** - ElevenLabs Music, voice models
- **Riffusion** - Riffusion
- **AIVA** - AIVA
- **Mureka** - Mureka
- **Boomy** - Boomy
- **Sesame AI** - Sesame CSM

### Other
- **Yandex** - YaLM (historical)

---

## Scale Reference

The `intelligence` value is a 1-100 rating where 100 is the AGI ceiling. On 2026-09-03 the whole array was leveled **once** against the [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index) v4.1.1 (a composite of nine benchmarks: GDPval-AA, τ³-Banking, Terminal-Bench, SciCode, HLE, GPQA Diamond, CritPt, AA-Omniscience, AA-LCR). Models present in the index took its value (best configuration); the rest were extrapolated from a monotone calibration curve fitted on the ~200 overlapping models, anchored to indexed siblings where available. The current frontier is therefore ≈ 66, not 99.

### Intelligence Scale (leveled 2026-09-03)

| Range | Era | Example Models |
|-------|-----|----------------|
| 60-66 | Sep 2026 frontier | Claude Fable 5.1 (66), Claude Opus 5 (63), GPT-6 Astra (61), Kimi K3 (60) |
| 50-59 | Mid 2026 | Gemini 3.8 Flash (59), GPT-5.5 (56), GPT-5.4 Thinking (53) |
| 40-49 | Early 2026 | Claude Sonnet 4.6 (48), Gemini 3.1 Pro (48), Opus 4.6 (45), GPT-5.2 (43), Opus 4.5 (42) |
| 25-39 | 2025 | GPT-5 (35), Gemini 2.5 Pro (26) |
| 10-24 | Late 2024 - early 2025 | DeepSeek-R1 (19), GPT-4o (12), Claude 3.5 Sonnet (10) |
| 3-9 | 2023 - mid 2024 | GPT-4 (7), Llama 3 (3), GPT-3.5 (3) |
| 1-2 | 2017-2022 | Transformer, BERT, GPT-2, GPT-3 |

Non-LLM modalities (image, video, audio, world models) were leveled with the same calibration curve, so they sit on one scale with the LLMs: Sora 2 (20), Veo 3 (15), Nano Banana (10), FLUX.1 (6).

### Key Principles for Rating

1. **Do not copy Artificial Analysis values for new models.** The leveling was a one-time calibration. New entries are inferred from the benchmarks published on the model's official blog/model card (GPQA, HLE, SWE-bench, Terminal-Bench, GDPval, AIME, etc.) and from reputable coverage, then placed against the reference points above.
2. Compare reported benchmarks with peers already on the scale: a model that beats GPT-5.5 on most benchmarks but trails Claude Opus 5 lands around 57-62.
3. Rate the best configuration of the model (reasoning / max effort), not the cheapest one.
4. Non-LLM models are placed relative to their predecessors on the same scale (Veo 3 = 15, so a clearly better Veo 4 ≈ 20-25).
5. Nothing goes above the current frontier by more than a few points without extraordinary evidence; the headroom up to 100 is deliberate.

---

## Quick Checklist Before Submitting

- [ ] No duplicate model names in the array
- [ ] All dates are ISO format (YYYY-MM-DD)
- [ ] All `type` values are one of: LLM, Diffusion, Reasoning, Multimodal, ASR, Text Diffusion
- [ ] All `cat` values are one of: text, image, video, audio, multi, code, reasoning
- [ ] `open` is correctly set (true = weights downloadable, false = API-only or proprietary)
- [ ] Intelligence values are inferred from official benchmarks/news and placed against the Scale Reference (never copied from Artificial Analysis)
- [ ] No models that are only announced but not released
- [ ] Output is valid JS syntax ready to paste into the array
