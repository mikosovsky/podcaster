"""
Podcaster - AI-powered podcast creation tool.

This package provides functionality for creating podcasts using:
- LLMs (Large Language Models) for content generation and scripting
- Text2Speech (TTS) models for audio generation from text

The main workflow:
1. Generate podcast scripts using LLMs
2. Convert scripts to audio using TTS models
3. Process and manage podcast episodes
"""

__version__ = "0.1.0"
__author__ = "Podcaster Team"

from .core.podcast import Podcast
from .core.episode import Episode

__all__ = ["Podcast", "Episode", "__version__"]

# TODO: Add version checking and compatibility warnings
# TODO: Add plugin system for custom LLM/TTS providers
# TODO: Add telemetry and analytics (optional, privacy-focused)
