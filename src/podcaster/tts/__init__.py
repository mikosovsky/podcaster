"""Text-to-Speech integration for audio generation."""

from .synthesizer import TTSSynthesizer
from .providers import ElevenLabsProvider, GoogleTTSProvider, EdgeTTSProvider

__all__ = ["TTSSynthesizer", "ElevenLabsProvider", "GoogleTTSProvider", "EdgeTTSProvider"]

# TODO: Add voice cloning support for custom voices
# TODO: Add emotion/tone control for TTS
# TODO: Add multi-speaker support for dialogue
