# File Formats

## Overview

[DESCRIPTION] This document describes all file formats used in the podcaster system.

## Input Files

### Topic Configuration File
**Format:** YAML or JSON  
**Location:** User-provided or `configs/`

**Expected Fields:**
- topic: Main topic/theme
- duration_minutes: Target duration
- platform: youtube, spotify, or both
- voice_id: ElevenLabs voice identifier
- style: casual, formal, educational, etc.
- additional_instructions: Free-form text for special requirements

---

## Intermediate Files

### Research Outline
**Format:** JSON  
**Location:** `data/cache/research/`

**Expected Structure:**
- outline_id: Unique identifier
- topic: Original topic
- sections: Array of section objects
  - title: Section title
  - key_points: Array of key points
  - estimated_duration: Duration in seconds
- research_notes: Supporting information
- generated_at: Timestamp

### Podcast Script
**Format:** Markdown or structured text  
**Location:** `data/processed/scripts/`

**Expected Structure:**
- Front matter: YAML metadata (title, duration, sections)
- Body: Script text with section markers
- Sections marked with headers (## Section Name)
- Timestamps or duration estimates
- Speaker notes (if multi-voice)

### Raw Audio
**Format:** MP3, WAV, or FLAC  
**Location:** `data/processed/audio/raw/`

**Metadata:**
- Sample rate: 44.1kHz or 48kHz recommended
- Bit depth: 16-bit or 24-bit
- Channels: Mono or stereo
- Duration: Actual audio length

### Enhanced Audio
**Format:** MP3, WAV  
**Location:** `data/processed/audio/enhanced/`

**Metadata:** Same as raw audio plus processing log

---

## Metadata Files

### Podcast Metadata
**Format:** JSON  
**Location:** `data/processed/metadata/`

**Expected Structure:**
```
{
  "title": "Podcast title",
  "description": "Full description text",
  "chapters": [
    {
      "title": "Chapter title",
      "start_time": "00:00:00",
      "end_time": "00:05:30"
    }
  ],
  "tags": ["tag1", "tag2", "tag3"],
  "thumbnail_prompt": "Description for image generation",
  "duration_seconds": 1234,
  "generated_at": "ISO8601 timestamp"
}
```

---

## Output Files

### YouTube Package
**Location:** `outputs/youtube/<project_id>/`

**Contains:**
- video_file.mp4: Audio with static or generated thumbnail
- description.txt: Formatted description with chapters
- tags.txt: Line-separated tags
- thumbnail_prompt.txt: Prompt for thumbnail generation
- upload_instructions.md: Checklist for manual upload

### Spotify Package
**Location:** `outputs/spotify/<project_id>/`

**Contains:**
- audio_file.mp3: Final audio in Spotify-compatible format
- episode_metadata.json: Title, description, etc.
- upload_instructions.md: Checklist for manual upload

---

## Configuration Files

### Podcast Configuration
**Format:** YAML  
**Location:** `configs/podcast_config.yaml.example`

**Expected Sections:**
- general: Global settings
- openai: OpenAI API configuration
- elevenlabs: TTS configuration
- audio_processing: Audio editing settings
- export: Platform-specific export settings

### TTS Voices Configuration
**Format:** YAML  
**Location:** `configs/tts_voices.yaml.example`

**Expected Structure:**
- voices: Array of voice objects
  - id: Voice identifier
  - name: Human-readable name
  - language: Language code
  - style: Description of voice style
  - use_cases: Recommended use cases

### Export Settings
**Format:** YAML  
**Location:** `configs/export_settings.yaml.example`

**Expected Sections:**
- youtube: YouTube-specific settings
- spotify: Spotify-specific settings
- common: Shared settings

---

## Prompt Template Files

**Format:** Plain text with placeholders  
**Location:** `prompts/`

**Placeholder Format:**
- Use `{{variable_name}}` for variables
- Use `[[INSTRUCTION]]` for special instructions
- Include examples and guidelines as comments

---

## Log Files

**Format:** Plain text or JSON  
**Location:** `logs/`

**Naming Convention:**
- `podcaster_YYYY-MM-DD.log`: Daily application logs
- `api_calls_YYYY-MM-DD.log`: API interaction logs
- `errors_YYYY-MM-DD.log`: Error-specific logs

---

## Cache Files

**Location:** `data/cache/`

**Purpose:** Store intermediate results to avoid re-processing

**Naming Convention:**
- Use content-based hashing for filenames when possible
- Include timestamps for time-sensitive data
- Maintain cache index file for cleanup
