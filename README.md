# Podcaster

An AI-powered storytelling application that generates realistic short-form stories and converts them into engaging video content with karaoke-style subtitles.

## 🎯 Overview

Podcaster is a Python-based tool that leverages AI to create compelling, realistic stories optimized for voice narration and automatically produces videos with synchronized karaoke-style subtitles. The project combines OpenAI's language models for story generation and ElevenLabs' text-to-speech technology for high-quality voice synthesis.

## ✨ Key Features

- **AI Story Generation**: Creates realistic, everyday life stories using OpenAI's GPT models
- **Text-to-Speech Synthesis**: Converts stories to natural-sounding audio using ElevenLabs TTS
- **Karaoke-Style Subtitles**: Burns word-by-word highlighted subtitles onto videos
- **Character-Based Narration**: Supports male and female voice selection based on story context
- **Video Processing**: Fits background videos to audio duration (trim or loop)
- **Configurable Story Parameters**: Customize story length, language, and narrative structure
- **Structured Storytelling**: Follows a proven narrative arc (Hook → Rising Action → Conflict → Comeback → Rising Action → Payoff)

## 🛠️ Technology Stack

- **Python 3.x** - Core programming language
- **OpenAI API** - Story generation with GPT models
- **ElevenLabs API** - Text-to-speech with character alignment
- **LangChain** - LLM orchestration and prompt management
- **Pydantic** - Data validation and settings management
- **MoviePy** - Video processing and subtitle rendering
- **Pillow (PIL)** - Image rendering for subtitles
- **NumPy** - Numerical operations for video frames

## 📋 Requirements

- Python 3.8+
- OpenAI API key
- ElevenLabs API key
- TrueType font file (for subtitle rendering)
- Background video file (MP4)

## 📦 Installation

1. **Clone the repository**:
```bash
git clone https://github.com/mikosovsky/podcaster.git
cd podcaster
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**:
```bash
cp example.env .env
```

4. **Configure your `.env` file** with your API keys and preferences:
```env
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-5.1-2025-11-13
ELEVENLABS_API_KEY=your_elevenlabs_api_key
ELEVENLABS_MODEL_ID=eleven_multilingual_v2
ELEVENLABS_MALE_VOICE_ID=cjVigY5qzO86Huf0OWal
ELEVENLABS_FEMALE_VOICE_ID=Xb7hH8MSUJpSbSDYk0k2
ELEVENLABS_SPEED=1.1
STORY_PROMPT_TEMPLATE_PATH=configs/story_prompt.md
STORY_LENGTH_MINUTES="1 minute and 30 seconds"
STORY_LANGUAGE="English"
```

5. **Add required assets**:
- Place your TrueType font file (`.ttf`) in the `configs/` directory
- Place your background video file (`.mp4`) in the `configs/` directory

## 🏗️ Architecture

### Project Structure

```
podcaster/
├── configs/                    # Configuration files
│   └── story_prompt.md        # Story generation prompt template
├── docs/                      # Documentation
│   └── img/
│       └── logic-diagram.svg  # Architecture diagram
├── src/podcaster/             # Source code
│   ├── core/                  # Core functionality
│   │   ├── audio.py          # Audio conversion utilities
│   │   ├── video.py          # Video fitting functions
│   │   └── karaoke.py        # Karaoke subtitle generation
│   ├── models/                # Data models
│   │   ├── schemas.py        # Pydantic schemas (StorySchema)
│   │   └── configs.py        # Configuration models
│   ├── providers/             # External service integrations
│   │   ├── openai.py         # OpenAI/LangChain integration
│   │   └── elevenlabs.py     # ElevenLabs TTS integration
│   ├── prompts/               # Prompt management
│   │   └── loader.py         # Prompt template loader
│   ├── graphs/                # Future: workflow graphs
│   ├── llm/                   # Future: LLM utilities
│   ├── tools/                 # Future: additional tools
│   └── main.py               # Main application entry point
├── tests/                     # Test suite
├── example.env               # Example environment variables
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

### Core Components

#### 1. Story Generation (`providers/openai.py`)
- **StoryTeller**: Uses LangChain and OpenAI to generate stories
- Implements structured output parsing with Pydantic
- Follows a specific narrative structure for engaging stories
- Generates metadata including title, description, keywords, and character sex

#### 2. Text-to-Speech (`providers/elevenlabs.py`)
- **SpeechSynthesizer**: Converts text to speech with character-level timestamps
- Supports voice selection based on character gender
- Provides character-level alignment data for precise subtitle timing
- Configurable speech speed

#### 3. Video Processing (`core/video.py`)
- **fit_video_to_audio()**: Matches video duration to audio length
- Automatically trims or loops video to fit audio
- Preserves video quality during processing

#### 4. Karaoke Subtitles (`core/karaoke.py`)
- **burn_karaoke_moviepy()**: Main function for subtitle rendering
- Character-to-word alignment conversion
- Intelligent text segmentation (max duration, max characters)
- Two-line layout with automatic line breaking
- Word-by-word highlighting with smooth transitions
- Image caching for performance optimization
- Auto-adjusting font size to fit video width

#### 5. Audio Utilities (`core/audio.py`)
- **base64_to_mp3()**: Converts base64-encoded audio to MP3 files

#### 6. Configuration Management (`models/configs.py`)
- **LLMConfig**: OpenAI API configuration
- **TTSConfig**: ElevenLabs TTS configuration
- **PromptConfig**: Story generation parameters

#### 7. Data Models (`models/schemas.py`)
- **StorySchema**: Story data structure with validation
- **Sex**: Enum for character gender (male/female)

## 🎬 Usage

### Basic Workflow

1. **Generate a Story**:
```python
from src.podcaster.providers.openai import StoryTeller

storyteller = StoryTeller()
story = storyteller.generate_story("List of trending stories...")
print(story.title)
print(story.content)
```

2. **Convert Story to Speech**:
```python
from src.podcaster.providers.elevenlabs import SpeechSynthesizer

synthesizer = SpeechSynthesizer()
audio = synthesizer.generate_speech(story_schema=story)
```

3. **Save Audio to File**:
```python
from src.podcaster.core.audio import base64_to_mp3

base64_to_mp3(audio.audio_base64, "output.mp3")
```

4. **Fit Video to Audio**:
```python
from src.podcaster.core.video import fit_video_to_audio

fit_video_to_audio(
    video_path="configs/background.mp4",
    audio_path="output.mp3",
    out_path="video_with_audio.mp4"
)
```

5. **Add Karaoke Subtitles**:
```python
from src.podcaster.core.karaoke import burn_karaoke_moviepy

burn_karaoke_moviepy(
    video_path="video_with_audio.mp4",
    alignment_obj=audio.alignment,
    output_path="final_video.mp4",
    font_path="configs/font.ttf",
    max_segment_chars=60,
    max_segment_duration=2.8,
    max_chars_per_line=20,
    y_pos_ratio=0.5,
    font_size_ratio=0.06
)
```

## ⚙️ Configuration

### Story Prompt Template

The `configs/story_prompt.md` file defines the storytelling guidelines:
- Language and story length (configurable via environment variables)
- Narrative structure (Hook → Rising Action → Conflict → Comeback → Rising Action → Payoff)
- Style requirements (confessional, intimate, first-person)
- Content rules (realistic, everyday life situations)

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API authentication | `sk-...` |
| `OPENAI_MODEL` | GPT model to use | `gpt-5.1-2025-11-13` |
| `ELEVENLABS_API_KEY` | ElevenLabs API authentication | `...` |
| `ELEVENLABS_MODEL_ID` | TTS model identifier | `eleven_multilingual_v2` |
| `ELEVENLABS_MALE_VOICE_ID` | Male narrator voice ID | `cjVigY5qzO86Huf0OWal` |
| `ELEVENLABS_FEMALE_VOICE_ID` | Female narrator voice ID | `Xb7hH8MSUJpSbSDYk0k2` |
| `ELEVENLABS_SPEED` | Speech speed multiplier | `1.1` |
| `STORY_PROMPT_TEMPLATE_PATH` | Path to prompt template | `configs/story_prompt.md` |
| `STORY_LENGTH_MINUTES` | Target story duration | `"1 minute and 30 seconds"` |
| `STORY_LANGUAGE` | Story output language | `"English"` |

## 📚 Dependencies

Key Python packages:
- `langchain` & `langchain-openai` - LLM orchestration
- `elevenlabs` - Text-to-speech API client
- `moviepy` - Video editing and processing
- `pydantic` & `pydantic-settings` - Configuration and validation
- `python-dotenv` - Environment variable management
- `pytest` - Testing framework
- `ruff` - Code linting and formatting
- `Pillow` - Image processing for subtitle rendering
- `numpy` - Numerical operations

See `requirements.txt` for complete list.

## 🧪 Testing

Run tests using pytest:
```bash
pytest tests/
```

## 🔍 Code Quality

The project uses Ruff for linting and code formatting:
```bash
ruff check .
ruff format .
```

## 🎨 Features in Detail

### Karaoke Subtitle System

The karaoke subtitle system is a sophisticated component that:
- Converts character-level timestamps to word-level alignment
- Intelligently segments text based on duration and character count
- Splits long segments into two balanced lines
- Highlights each word as it's spoken (yellow highlight)
- Renders text with black stroke outline for visibility
- Caches rendered images for performance
- Auto-adjusts font size to prevent overflow
- Centers text on screen with configurable positioning

### Story Generation

Stories are generated following a specific narrative structure:
1. **Hook**: Captures attention immediately
2. **Rising Action**: Builds tension and engagement
3. **Conflict**: Introduces the main challenge
4. **Comeback**: Shows the turning point
5. **Rising Action**: Escalates to resolution
6. **Payoff**: Provides satisfying conclusion that loops back to hook

Content is constrained to realistic, everyday scenarios (work, school, family, relationships) without fantasy, sci-fi, or technology themes.

## 🚀 Future Enhancements

Based on the project structure, planned features include:
- Workflow graphs for automated content generation pipelines
- Additional LLM utilities and integrations
- Extended tooling for content optimization
- Batch processing capabilities
- Template variations for different content types

## 📄 License

[Add license information]

## 🤝 Contributing

[Add contribution guidelines]

## 📧 Contact

[Add contact information]

---

**Note**: This project requires valid API keys for OpenAI and ElevenLabs services. Both services have usage costs associated with API calls.