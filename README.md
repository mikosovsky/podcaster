# podcaster

A Python application for generating podcast stories using AI language models and text-to-speech services.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mikosovsky/podcaster.git
cd podcaster
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables by copying the example file:
```bash
cp example.env .env
```

Then edit `.env` with your actual API keys and configuration values.

## Running Tests

The project uses pytest for testing. All tests are located in the `tests/` directory.

### Run all tests
```bash
pytest tests/
```

### Run tests with verbose output
```bash
pytest tests/ -v
```

### Run tests for a specific module
```bash
pytest tests/test_models_schemas.py
pytest tests/test_models_configs.py
pytest tests/test_prompts_loader.py
pytest tests/test_providers_openai.py
```

### Run tests with coverage (if pytest-cov is installed)
```bash
pytest tests/ --cov=src --cov-report=html
```

### Test Structure

- `tests/test_models_schemas.py` - Tests for Pydantic data models
- `tests/test_models_configs.py` - Tests for configuration classes
- `tests/test_prompts_loader.py` - Tests for prompt template loading
- `tests/test_providers_openai.py` - Tests for OpenAI story generation
- `tests/conftest.py` - Shared pytest fixtures and configuration
- `pytest.ini` - Pytest configuration

## Project Structure

```
podcaster/
├── src/podcaster/
│   ├── models/          # Pydantic models and configurations
│   ├── prompts/         # Prompt template loading
│   ├── providers/       # External service providers (OpenAI)
│   ├── core/            # Core functionality
│   ├── graphs/          # Graph-based logic
│   ├── llm/             # Language model integrations
│   └── tools/           # Utility tools
├── tests/               # Test suite
├── configs/             # Configuration files
└── requirements.txt     # Python dependencies
```

## Configuration

The application requires the following environment variables:

- `OPENAI_API_KEY` - Your OpenAI API key
- `OPENAI_MODEL` - The OpenAI model to use (e.g., gpt-4)
- `ELEVENLABS_API_KEY` - Your ElevenLabs API key
- `ELEVENLABS_MALE_VOICE_ID` - Voice ID for male voices
- `ELEVENLABS_FEMALE_VOICE_ID` - Voice ID for female voices
- `ELEVENLABS_SPEED` - Speech speed multiplier
- `STORY_PROMPT_TEMPLATE_PATH` - Path to the story prompt template
- `STORY_LENGTH_MINUTES` - Target story length
- `STORY_LANGUAGE` - Language for story generation

## Development

### Linting

The project uses `ruff` for linting:
```bash
ruff check src/
```

### Code Style

Follow PEP 8 guidelines and use the existing code style in the project.