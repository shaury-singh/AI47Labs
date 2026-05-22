# AI Advertisement Generator

An AI-powered multi-agent workflow that automatically generates ecommerce marketing creatives from a product webpage URL.

The system performs:

- Product research and information extraction
- Market research generation
- AI creative strategy generation
- Advertisement prompt refinement
- AI image generation
- Promotional video generation
- Batch processing using CSV uploads

---

# Features

## AI Multi-Agent Workflow

The project uses multiple specialized AI agents:

| Agent | Responsibility |
|---|---|
| Scraping Agent | Extract webpage content |
| Product Research Agent | Filter useful ecommerce information |
| Market Research Agent | Generate marketing hooks and audience insights |
| Creative Strategy Agent | Create cinematic advertisement prompts |
| Critic Agent | Evaluate advertisement quality |
| Image Generation Agent | Generate AI product advertisements |
| Video Generator Agent | Create promotional videos |

---

# Architecture

```text
                    ┌─────────────────────┐
                    │ Product URL Input   │
                    └──────────┬──────────┘
                               │
                               ▼
                 ┌──────────────────────────┐
                 │ Scraping Agent           │
                 │ (BeautifulSoup + Requests)
                 └──────────┬───────────────┘
                            │
                            ▼
                 ┌──────────────────────────┐
                 │ Product Research Agent   │
                 │ (Qwen2.5 via Ollama)     │
                 └──────────┬───────────────┘
                            │
                            ▼
                 ┌──────────────────────────┐
                 │ Market Research Agent    │
                 │ Hooks + Audience +       │
                 │ Emotional Triggers       │
                 └──────────┬───────────────┘
                            │
                            ▼
                 ┌──────────────────────────┐
                 │ Creative Strategy Agent  │
                 │ Ad Creative Prompts      │
                 └──────────┬───────────────┘
                            │
                            ▼
                 ┌──────────────────────────┐
                 │ Critic Agent             │
                 │ Prompt Evaluation        │
                 └──────────┬───────────────┘
                            │
                            ▼
                 ┌──────────────────────────┐
                 │ Image Generation Agent   │
                 │ FLUX.1-schnell Model     │
                 └──────────┬───────────────┘
                            │
                            ▼
                 ┌──────────────────────────┐
                 │ Video Generator Agent    │
                 │ MoviePy                  │
                 └──────────┬───────────────┘
                            │
                            ▼
                 ┌──────────────────────────┐
                 │ Final Ads + Videos       │
                 └──────────────────────────┘
```

---

# Tech Stack

## Frontend
- Streamlit

## Backend
- Python

## AI Models
- Qwen2.5:1.5b (Ollama)
- FLUX.1-schnell (HuggingFace)

## Libraries
- BeautifulSoup4
- Requests
- MoviePy
- Pandas
- Concurrent Futures

---

# Project Structure

```bash
AI47Labs/
│
├── Backend/
│   ├── config.py
│   ├── scrappingAgent.py
│   ├── marketReserachAgent.py
│   ├── creativeStrategyAgent.py
│   ├── criticAgent.py
│   ├── imageGenerationAgent.py
│   ├── movieGeneratorAgent.py
│   └── wrapper.py
│
├── Frontend/
│   └── ui.py
│
├── Generated_Images/
├── Generated_Videos/
├── requirements.txt
├── .env
└── README.md
```

---

# Setup Guide

# 1. Clone Repository

```bash
git clone https://github.com/shaury-singh/AI47Labs.git
cd AI47Labs
```

---


# 2. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

---

# 3. Install Ollama

Download Ollama:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```

---

# 4. Pull Required Model

Download Qwen model:

```bash
ollama pull qwen2.5:1.5b
```

---

# 5. Start Ollama Server

```bash
ollama serve
```

The server will run at:

```bash
http://localhost:11434
```

---

# 6. Setup HuggingFace API Key

Create a `.env` file in the root directory.

```env
HF_API_KEY=your_huggingface_api_key
```

Get your HuggingFace token from:

https://huggingface.co/settings/tokens

---

# 7. Run Streamlit Application

```bash
cd Frontend
streamlit run Frontend/ui.py
```

---

# Application Workflow

## Single URL Mode

The user enters:
- Brand name
- Product webpage URL

The system:
1. Scrapes webpage data
2. Extracts relevant product information
3. Generates marketing hooks
4. Creates advertisement strategies
5. Reviews prompt quality
6. Generates AI images
7. Creates promotional video

---

## Batch CSV Processing

Upload CSV file format:

```csv
name,url
Nike,https://example.com
Apple,https://example.com
```

The application:
- Processes multiple brands
- Shows progress tracking
- Displays generated advertisements

---

# Generated Output

## Images

Saved in:

```bash
Generated_Images/
```

---

## Videos

Saved in:

```bash
Generated_Videos/
```

---

# AI Workflow Explanation

# Scraping Agent

Extracts webpage text using:
- Requests
- BeautifulSoup

Filters duplicate and irrelevant data.

---

# Product Research Agent

Uses Qwen2.5 model to:
- Remove noisy webpage content
- Keep marketing-relevant information

Examples:
- Product features
- Customer pain points
- Benefits
- Pricing information

---

# Market Research Agent

Generates:
- Marketing hooks
- Emotional triggers
- Target audience

---

# Creative Strategy Agent

Creates cinematic AI advertisement prompts optimized for:
- FLUX
- Stable Diffusion
- Midjourney

Includes:
- Lighting
- Emotional tone
- Camera composition
- Branding aesthetics

---

# Critic Agent

Evaluates prompts based on:
- Commercial appeal
- Product visibility
- Branding quality
- Emotional impact

If score is low:
- Prompt regeneration is triggered

---

# Image Generation Agent

Uses HuggingFace Inference API:

```python
black-forest-labs/FLUX.1-schnell
```

Generates:
- Social media advertisements
- Cinematic product visuals
- Commercial marketing creatives

---

# Video Generator Agent

Uses MoviePy to:
- Combine generated images
- Create promotional advertisement videos

---

# Concurrency Support

The system supports parallel batch execution using:

```python
ThreadPoolExecutor
```

Allows multiple advertisement jobs to run simultaneously.

---

# Troubleshooting

# Ollama Connection Error

Ensure Ollama server is running:

```bash
ollama serve
```

---

# HuggingFace Authentication Error

Verify `.env` file:

```env
HF_API_KEY=your_api_key
```

---

# Streamlit Command Not Found

Install Streamlit:

```bash
pip install streamlit
```

---

# MoviePy Errors

Install FFmpeg.

## Windows

Download:
https://ffmpeg.org/download.html

Add FFmpeg to system PATH.

---