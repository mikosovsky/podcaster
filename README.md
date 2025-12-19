# Podcaster

An AI-powered podcast creation tool using Large Language Models (LLMs) and Text-to-Speech (TTS) technology.

## Overview

Podcaster automates podcast creation by combining:
- **LLMs** (GPT-4, Claude, local models) for generating engaging scripts and content
- **Text2Speech** models (ElevenLabs, Google TTS, Edge TTS) for converting scripts to high-quality audio

## Features

- 🤖 **AI Script Generation**: Create podcast scripts from topics using state-of-the-art LLMs
- 🎙️ **High-Quality TTS**: Convert scripts to natural-sounding speech with multiple voice options
- 🔌 **Multiple Providers**: Support for OpenAI, Anthropic, ElevenLabs, Google Cloud, and more
- 🎨 **Customizable**: Configure voices, tones, formats, and generation parameters
- 📦 **Complete Workflow**: End-to-end podcast creation from idea to audio file
- 🛠️ **Audio Processing**: Built-in audio normalization, format conversion, and post-processing

## Project Structure

```
podcaster/
├── src/podcaster/           # Main package source code
│   ├── __init__.py         # Package initialization
│   ├── core/               # Core podcast functionality
│   │   ├── podcast.py      # Podcast data model
│   │   ├── episode.py      # Episode data model
│   │   └── orchestrator.py # Workflow orchestration
│   ├── llm/                # LLM integration
│   │   ├── generator.py    # Content generation logic
│   │   └── providers.py    # LLM provider implementations (OpenAI, Anthropic, Local)
│   ├── tts/                # Text-to-Speech integration
│   │   ├── synthesizer.py  # TTS synthesis logic
│   │   └── providers.py    # TTS provider implementations (ElevenLabs, Google, Edge, Coqui)
│   └── utils/              # Utility modules
│       ├── audio.py        # Audio processing utilities
│       ├── file_manager.py # File management
│       └── config.py       # Configuration management
├── tests/                  # Test suite
│   ├── unit/              # Unit tests
│   └── integration/       # Integration tests
├── scripts/               # CLI and utility scripts
│   └── cli.py            # Command-line interface
├── examples/             # Example usage scripts
│   ├── simple_podcast.py
│   └── custom_providers.py
├── config/               # Configuration files
│   ├── default.yaml      # Default configuration
│   ├── default.json      # JSON format config
│   └── .env.example      # Environment variables template
├── data/                 # Data directories
│   ├── input/           # Input files
│   ├── output/          # Generated podcasts
│   └── temp/            # Temporary files
├── docs/                # Documentation
├── setup.py             # Package setup file
├── pyproject.toml       # Modern Python project config
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## Installation

### Basic Installation

```bash
# Clone the repository
git clone https://github.com/mikosovsky/podcaster.git
cd podcaster

# Install core dependencies
pip install -e .
```

### With Optional Dependencies

```bash
# Install with LLM providers
pip install -e ".[llm]"

# Install with TTS providers
pip install -e ".[tts]"

# Install with audio processing
pip install -e ".[audio]"

# Install everything
pip install -e ".[all]"

# Install development tools
pip install -e ".[dev]"
```

## Quick Start

### 1. Set Up Environment Variables

```bash
cp config/.env.example .env
# Edit .env with your API keys
```

### 2. Create Your First Podcast

```python
from podcaster.core import Podcast, PodcastOrchestrator
from podcaster.llm import LLMGenerator
from podcaster.tts import TTSSynthesizer

# Create a podcast
podcast = Podcast(
    title="My Podcast",
    description="An AI-generated podcast",
    author="Your Name"
)

# Initialize orchestrator
orchestrator = PodcastOrchestrator(
    llm_generator=LLMGenerator(),
    synthesizer=TTSSynthesizer()
)

# Create an episode
episode = orchestrator.create_episode(
    podcast=podcast,
    topic="The Future of AI",
    title="Episode 1: AI Revolution",
    description="Exploring the latest in AI technology"
)

print(f"Created: {episode.title}")
print(f"Script: {episode.script[:200]}...")
print(f"Audio: {episode.audio_path}")
```

### 3. Using the CLI

```bash
# Create a podcast episode
python scripts/cli.py create \
  --topic "AI in Healthcare" \
  --title "AI Revolution in Medicine" \
  --podcast-title "Tech Talk" \
  --author "John Doe"

# Synthesize audio from a script
python scripts/cli.py synthesize \
  --script-path my_script.txt \
  --output episode.mp3 \
  --voice "default"
```

## Configuration

Configure the application using YAML or JSON files in the `config/` directory:

```yaml
# config/default.yaml
llm:
  provider: "openai"
  model: "gpt-4"
  temperature: 0.7

tts:
  provider: "elevenlabs"
  voice: "default"
  language: "en"

podcast:
  default_format: "interview"
  default_duration: 10
  default_tone: "conversational"
```

## Supported Providers

### LLM Providers
- **OpenAI** (GPT-3.5, GPT-4)
- **Anthropic** (Claude)
- **Local Models** (via llama.cpp, Ollama)

### TTS Providers
- **ElevenLabs** - High-quality, natural voices
- **Google Cloud TTS** - WaveNet and Neural2 voices
- **Edge TTS** - Free, Microsoft voices
- **Coqui TTS** - Open-source, local TTS

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/podcaster --cov-report=html

# Run specific test file
pytest tests/unit/test_core.py
```

### Code Quality

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Type checking
mypy src/

# Linting
flake8 src/ tests/
```

## TODO and Extension Points

Throughout the codebase, you'll find `TODO` comments indicating areas for implementation or enhancement:

- LLM integration with actual API clients
- TTS provider implementations
- Audio processing with pydub/ffmpeg
- Configuration validation and management
- Error handling and retry logic
- Caching and optimization
- Cloud storage integration
- RSS feed generation
- And many more...

## Contributing

Contributions are welcome! Areas needing implementation:
1. Complete LLM provider integrations
2. Complete TTS provider integrations
3. Audio processing implementations
4. Additional examples and documentation
5. Tests for all modules
6. Performance optimizations

## License

MIT License - See LICENSE file for details

## Support

For issues, questions, or contributions, please visit:
https://github.com/mikosovsky/podcaster/issues

---

**Note**: This is a framework/skeleton project with comprehensive structure and placeholders. The TODO comments throughout the codebase indicate where actual implementations should be added.