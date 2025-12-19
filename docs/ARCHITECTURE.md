# Project Architecture

## Overview

Podcaster is designed with a modular architecture that separates concerns and allows for easy extension and customization.

## Core Components

### 1. Core Module (`src/podcaster/core/`)

The foundation of the application, handling data models and workflow orchestration.

**Files:**
- `podcast.py` - Podcast series data model
- `episode.py` - Individual episode data model
- `orchestrator.py` - Coordinates the workflow between LLM and TTS components

**Key Responsibilities:**
- Maintain podcast and episode metadata
- Orchestrate the content generation -> audio synthesis pipeline
- Manage episode lifecycle (creation, storage, retrieval)

### 2. LLM Module (`src/podcaster/llm/`)

Handles all Large Language Model integrations for content generation.

**Files:**
- `generator.py` - Main LLM generator with script generation logic
- `providers.py` - Provider-specific implementations (OpenAI, Anthropic, Local)

**Key Responsibilities:**
- Generate podcast scripts from topics
- Support multiple LLM providers with a unified interface
- Handle prompt engineering and response processing

**Extension Points:**
- Add new LLM providers by implementing `BaseLLMProvider`
- Customize prompt templates in `generator.py`
- Add streaming generation support
- Implement caching for frequently generated content

### 3. TTS Module (`src/podcaster/tts/`)

Manages Text-to-Speech synthesis for converting scripts to audio.

**Files:**
- `synthesizer.py` - Main TTS synthesizer with audio generation logic
- `providers.py` - Provider-specific implementations (ElevenLabs, Google, Edge, Coqui)

**Key Responsibilities:**
- Convert text scripts to audio files
- Support multiple TTS providers with a unified interface
- Handle voice selection and audio parameters

**Extension Points:**
- Add new TTS providers by implementing `BaseTTSProvider`
- Add voice cloning support
- Implement multi-speaker synthesis for dialogue
- Add SSML support for advanced speech control

### 4. Utils Module (`src/podcaster/utils/`)

Provides utility functions for common tasks.

**Files:**
- `audio.py` - Audio processing utilities (format conversion, normalization, merging)
- `file_manager.py` - File and directory management
- `config.py` - Configuration loading and management

**Key Responsibilities:**
- Audio post-processing and enhancement
- Organize file structure and manage storage
- Load and validate configuration

**Extension Points:**
- Add advanced audio effects
- Implement cloud storage support
- Add configuration encryption

## Data Flow

```
User Input (Topic)
       ↓
[LLM Generator]
   → Generate Script
       ↓
[TTS Synthesizer]
   → Convert to Audio
       ↓
[Audio Processor]
   → Post-processing
       ↓
[File Manager]
   → Save to Disk
       ↓
Episode Complete
```

## Extension Patterns

### Adding a New LLM Provider

1. Create a class inheriting from `BaseLLMProvider` in `llm/providers.py`
2. Implement the `generate()` method
3. Add provider initialization logic
4. Update documentation and examples

### Adding a New TTS Provider

1. Create a class inheriting from `BaseTTSProvider` in `tts/providers.py`
2. Implement the `synthesize()` method
3. Add voice listing and management
4. Update documentation and examples

### Adding New Features

Key areas marked with `TODO` comments indicate where implementations should be added:
- API integrations
- Audio processing algorithms
- Configuration validation
- Error handling and retry logic
- Caching mechanisms
- Testing coverage

## Design Principles

1. **Modularity**: Each component is self-contained and can be tested/used independently
2. **Extensibility**: Easy to add new providers without modifying existing code
3. **Flexibility**: Support for multiple providers with runtime selection
4. **Clarity**: Clear separation between data models, business logic, and utilities
5. **Documentation**: Comprehensive TODO comments guide future development

## Testing Strategy

- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test complete workflows end-to-end
- **Provider Mocks**: Use mock providers for testing without API costs

## Configuration Management

The application supports multiple configuration formats:
- YAML files (`config/default.yaml`)
- JSON files (`config/default.json`)
- Environment variables (`.env`)

Configuration precedence: Environment Variables > Config File > Defaults
