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
  intelligence: 75,         // Number (1-100) - capability/quality rating (relative scale)
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

The `intelligence` value is on a relative 1-100 scale. Use these reference points to calibrate new entries:

### Intelligence Scale (capability/quality)

| Range | Example Models | Description |
|-------|---------------|-------------|
| 5-15 | Transformer, ELMo, GPT-1, BERT | Early/foundational models |
| 15-30 | GPT-2, GPT-3, DALL-E 1, early diffusion | Pre-ChatGPT era |
| 30-45 | ChatGPT, GPT-4, Claude 1-2, Llama 1-2, SD XL, Midjourney v5 | 2023 generation |
| 45-60 | GPT-4o, Claude 3 Opus/Sonnet, Gemini 1.5, Llama 3, FLUX.1 | Early 2024 generation |
| 60-75 | Claude 3.5/3.7, DeepSeek-R1, Grok-3/4, GPT-5, Gemini 2.5 | Late 2024 - mid 2025 |
| 75-85 | GPT-5.1/5.2, Opus 4/4.5, Grok-4.1, Gemini 3, Qwen 3.5 | Late 2025 - early 2026 |
| 85-95 | Opus 4.6, Sonnet 4.6, GPT-5.4, Gemini 3.1, Qwen 3.5-Plus | Current frontier (early 2026) |

### Key Principles for Rating

1. **Intelligence** should reflect benchmark performance AND real-world capability relative to peers at release time
2. Reasoning models typically get higher intelligence than their non-reasoning counterparts
3. Open-weight models of similar architecture get the same ratings as closed equivalents
4. When uncertain, place the model between its known nearest neighbors in the timeline

---

## Quick Checklist Before Submitting

- [ ] No duplicate model names in the array
- [ ] All dates are ISO format (YYYY-MM-DD)
- [ ] All `type` values are one of: LLM, Diffusion, Reasoning, Multimodal, ASR, Text Diffusion
- [ ] All `cat` values are one of: text, image, video, audio, multi, code, reasoning
- [ ] `open` is correctly set (true = weights downloadable, false = API-only or proprietary)
- [ ] Intelligence values are calibrated against similar existing models
- [ ] No models that are only announced but not released
- [ ] Output is valid JS syntax ready to paste into the array
