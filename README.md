# Podcaster

## Project Overview

[DESCRIPTION] This project aims to generate complete, ready-to-publish podcasts for YouTube and Spotify using AI-powered tools.

## Key Technologies

- **LLM**: OpenAI (for script generation, titles, descriptions, chapters, tags, and image prompts)
- **Text-to-Speech**: ElevenLabs (for audio synthesis)

## High-Level Pipeline

1. **Topic Selection** → User provides a topic or theme
2. **Research & Outline** → AI researches and creates an outline
3. **Script Generation** → AI generates the full podcast script
4. **Text-to-Speech** → ElevenLabs synthesizes the audio
5. **Audio Editing** (optional) → Post-processing and enhancement
6. **Metadata Generation** → Titles, descriptions, chapters, tags, thumbnails
7. **Export** → Package for YouTube and Spotify platforms

## Repository Structure

```
/docs/               - Product documentation, architecture, workflows
/podcaster/          - Main application package with logical modules
/prompts/            - AI prompt templates for various generation tasks
/configs/            - Example configuration files and schemas
/data/               - Data directories (raw, processed, cache)
/outputs/            - Generated podcast packages ready for export
/scripts/            - Utility scripts for automation tasks
/logs/               - Application logs
```

## Configuration

Configuration is managed through environment variables defined in `.env` file. See `.env.example` for required variables.

## Getting Started

[TODO] Add instructions for:
- Setting up the environment
- Installing dependencies
- Configuring API keys
- Running the pipeline

## Module Descriptions

### Research Module
[TODO] Describe research capabilities and data gathering

### Script Generation Module
[TODO] Describe script generation workflow

### TTS Module
[TODO] Describe audio synthesis integration

### Editing Module
[TODO] Describe audio post-processing features

### Metadata Module
[TODO] Describe metadata generation (titles, descriptions, etc.)

### Export Module
[TODO] Describe platform-specific export packaging

## License

[TODO] Specify license type