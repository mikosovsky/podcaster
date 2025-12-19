# Configuration Guide

## Overview

[DESCRIPTION] This guide explains how to configure the podcaster application.

## Environment Variables

All environment variables should be defined in a `.env` file at the project root. See `.env.example` for a complete list.

### Required Variables

#### OpenAI Configuration
- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `OPENAI_MODEL`: Model to use (default: gpt-4)
- `OPENAI_MAX_TOKENS`: Maximum tokens per request (default: 4000)

#### ElevenLabs Configuration
- `ELEVENLABS_API_KEY`: Your ElevenLabs API key (required)
- `ELEVENLABS_VOICE_ID`: Default voice ID to use
- `ELEVENLABS_MODEL_ID`: TTS model identifier (default: eleven_monolingual_v1)

#### Application Settings
- `APP_ENV`: Environment (development, production)
- `LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR)
- `LOG_DIR`: Directory for log files

### Optional Variables

#### Path Configuration
- `DATA_DIR`: Base directory for data files
- `OUTPUT_DIR`: Base directory for output files
- `PROMPTS_DIR`: Directory containing prompt templates
- `CONFIGS_DIR`: Directory containing configuration files

#### Processing Options
- `MAX_RETRIES`: Maximum retry attempts for API calls
- `TIMEOUT_SECONDS`: Timeout for API requests
- `ENABLE_CACHING`: Enable/disable result caching

---

## Configuration Files

### Podcast Configuration (`configs/podcast_config.yaml`)

[DESCRIPTION] Main configuration file for podcast generation

**Expected sections:**

#### General Settings
- project_name: Name for the podcast project
- output_format: audio, video, or both
- language: Target language code

#### Content Settings
- default_duration_minutes: Target podcast length
- tone: casual, formal, educational, storytelling
- pacing: slow, medium, fast
- complexity_level: beginner, intermediate, advanced

#### OpenAI Settings
- model: Model identifier
- temperature: Creativity level (0.0-1.0)
- max_tokens: Token limit per request
- retry_config: Retry settings

#### ElevenLabs Settings
- voice_settings:
  - stability: Voice stability (0.0-1.0)
  - similarity_boost: Similarity boost (0.0-1.0)
- audio_format: mp3, wav, etc.
- sample_rate: Audio sample rate

#### Audio Processing
- normalize_volume: Enable volume normalization
- remove_silence: Remove long silences
- fade_in_duration: Fade in duration in seconds
- fade_out_duration: Fade out duration in seconds
- intro_audio: Path to intro audio file (optional)
- outro_audio: Path to outro audio file (optional)

---

### TTS Voices Configuration (`configs/tts_voices.yaml`)

[DESCRIPTION] Configuration for available TTS voices

**Expected structure:**

```
voices:
  - id: voice_id_1
    name: Professional Male
    language: en-US
    style: authoritative, clear
    use_cases:
      - news
      - educational
      - corporate
    
  - id: voice_id_2
    name: Friendly Female
    language: en-US
    style: warm, conversational
    use_cases:
      - storytelling
      - lifestyle
      - interviews
```

---

### Export Settings Configuration (`configs/export_settings.yaml`)

[DESCRIPTION] Platform-specific export configuration

**Expected sections:**

#### YouTube Settings
- video_format: mp4, mkv
- video_codec: h264, h265
- audio_codec: aac, mp3
- resolution: 1920x1080, 1280x720
- frame_rate: 30, 60
- thumbnail:
  - generate: true/false
  - dimensions: WIDTHxHEIGHT
  - format: jpg, png

#### Spotify Settings
- audio_format: mp3
- bitrate: 192, 256, 320 kbps
- sample_rate: 44100 Hz
- channels: stereo, mono

#### Common Settings
- include_chapters: true/false
- generate_transcript: true/false
- metadata_format: json, yaml

---

## Prompt Templates Configuration

[DESCRIPTION] Prompt templates are text files with placeholders

**Location:** `prompts/` directory

**Available Templates:**
- research_prompt.txt: For research and outline generation
- script_generation_prompt.txt: For script creation
- title_generation_prompt.txt: For title generation
- description_generation_prompt.txt: For description creation
- chapters_generation_prompt.txt: For chapter markers
- tags_generation_prompt.txt: For tag generation
- image_prompt_generation.txt: For thumbnail prompts

**Placeholder Syntax:**
- `{{topic}}`: Topic/theme
- `{{duration}}`: Target duration
- `{{style}}`: Content style
- `{{outline}}`: Generated outline
- `{{script}}`: Generated script
- `[[INSTRUCTION]]`: Special instructions section

---

## Best Practices

### API Keys Security
[TODO] Document security practices:
- Never commit `.env` file
- Use environment-specific keys
- Rotate keys regularly
- Use read-only keys when possible

### Performance Optimization
[TODO] Document optimization tips:
- Enable caching for repeated requests
- Adjust timeouts based on content length
- Use appropriate model sizes
- Monitor API usage and costs

### Quality Settings
[TODO] Document quality recommendations:
- Balance quality vs. speed
- Test different voice settings
- Adjust temperature for creativity
- Review generated content before finalizing

### Error Handling
[TODO] Document error handling configuration:
- Set appropriate retry limits
- Configure timeout values
- Enable detailed logging for debugging
- Set up monitoring alerts

---

## Troubleshooting

### Common Issues

**API Key Errors**
[TODO] Steps to verify and fix API key issues

**Audio Quality Issues**
[TODO] Settings to adjust for better audio quality

**Generation Timeouts**
[TODO] How to handle long-running operations

**Cache Issues**
[TODO] When and how to clear cache
