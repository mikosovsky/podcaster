# Pipeline Workflow

## Complete Workflow

[DESCRIPTION] This document describes the end-to-end workflow for generating a podcast.

## Workflow Stages

### Stage 1: Topic Input & Configuration

**Input:**
- Topic or theme for the podcast
- Target duration
- Platform preferences (YouTube, Spotify, or both)
- Voice preferences
- Style/tone preferences

**Output:**
- Validated configuration object
- Initial project structure

**Error Handling:**
- Validate all required inputs
- Check API key availability
- Verify output directory permissions

---

### Stage 2: Research & Outline Generation

**Purpose:** Generate a structured outline based on the topic

**Process:**
1. Send topic to OpenAI with research prompt
2. Parse research results
3. Generate structured outline
4. Cache results for potential regeneration

**Input:**
- Topic/theme
- Research prompt template
- Target length/depth

**Output:**
- Structured outline (JSON/YAML format)
- Research notes
- Source references (if applicable)

**Cache Location:** `data/cache/research/`

---

### Stage 3: Script Generation

**Purpose:** Convert outline into a full podcast script

**Process:**
1. Load outline from previous stage
2. Apply script generation prompt template
3. Generate full script via OpenAI
4. Validate script format
5. Save script with timestamps/sections

**Input:**
- Structured outline
- Script generation prompt template
- Style guidelines

**Output:**
- Complete podcast script (markdown/text format)
- Section markers
- Estimated duration

**Cache Location:** `data/processed/scripts/`

---

### Stage 4: Text-to-Speech Synthesis

**Purpose:** Convert script to audio

**Process:**
1. Load script from previous stage
2. Split script into manageable chunks (if needed)
3. Send each chunk to ElevenLabs API
4. Receive audio segments
5. Combine segments into complete audio file
6. Save raw audio output

**Input:**
- Podcast script
- Voice ID and TTS settings
- Audio format preferences

**Output:**
- Raw audio file (MP3/WAV)
- Audio metadata (duration, format, etc.)

**Cache Location:** `data/processed/audio/raw/`

---

### Stage 5: Audio Editing (Optional)

**Purpose:** Enhance and polish the audio

**Process:**
1. Load raw audio file
2. Apply audio processing:
   - Silence removal/trimming
   - Volume normalization
   - Fade in/out effects
   - Add intro/outro music (if configured)
3. Export enhanced audio

**Input:**
- Raw audio file
- Editing configuration

**Output:**
- Enhanced audio file
- Processing log

**Cache Location:** `data/processed/audio/enhanced/`

---

### Stage 6: Metadata Generation

**Purpose:** Generate all required metadata for publishing

**Process:**
1. Generate title (using OpenAI)
2. Generate description (using OpenAI)
3. Generate chapter markers (using OpenAI)
4. Generate tags/keywords (using OpenAI)
5. Generate thumbnail image prompt (using OpenAI)
6. Compile all metadata into platform-specific formats

**Input:**
- Script content
- Audio duration
- Platform requirements

**Output:**
- Title
- Description
- Chapter markers (with timestamps)
- Tags/keywords list
- Thumbnail prompt
- Metadata JSON file

**Cache Location:** `data/processed/metadata/`

---

### Stage 7: Platform Export

**Purpose:** Package everything for target platforms

**Process:**
1. Load all assets (audio, metadata)
2. Create platform-specific packages:
   - **YouTube:** Video file (audio + static/generated image), description, chapters
   - **Spotify:** Audio file, episode metadata
3. Validate package completeness
4. Generate upload instructions/checklist

**Input:**
- Enhanced audio file
- All metadata
- Platform selection

**Output:**
- Platform-specific packages in `outputs/youtube/` or `outputs/spotify/`
- Upload instruction files
- Quality check reports

---

## Workflow Variations

### Quick Mode
[DESCRIPTION] Skip audio editing stage for faster turnaround

### Batch Mode
[DESCRIPTION] Process multiple topics in sequence

### Incremental Mode
[DESCRIPTION] Resume from any stage using cached data

## State Management

[TODO] Describe how pipeline state is tracked:
- Progress markers
- Checkpoint files
- Recovery from failures

## Logging

[TODO] Define logging strategy for each stage:
- Input/output logging
- API call logging
- Error logging
- Performance metrics
