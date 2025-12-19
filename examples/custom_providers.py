"""Example: Using different LLM and TTS providers.

This example shows how to:
1. Configure specific LLM providers (OpenAI, Anthropic, local models)
2. Configure specific TTS providers (ElevenLabs, Google, Edge TTS)
3. Create episodes with custom provider settings
"""

from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from podcaster.core import Podcast, PodcastOrchestrator
from podcaster.llm import LLMGenerator, OpenAIProvider
from podcaster.tts import TTSSynthesizer, ElevenLabsProvider

# TODO: Add provider comparison functionality
# TODO: Add cost estimation for different providers
# TODO: Add quality metrics comparison


def main():
    """Demonstrate using different providers."""
    print("Example: Using custom providers...")
    
    # Create podcast
    podcast = Podcast(
        title="Advanced Tech Podcast",
        description="Deep dives into technology",
        author="Tech Expert"
    )
    
    # Initialize with specific providers
    llm_provider = OpenAIProvider(api_key="your-api-key")
    tts_provider = ElevenLabsProvider(api_key="your-api-key")
    
    orchestrator = PodcastOrchestrator(
        llm_generator=LLMGenerator(provider=llm_provider, model="gpt-4"),
        synthesizer=TTSSynthesizer(provider=tts_provider, voice="Adam")
    )
    
    # Create episode
    episode = orchestrator.create_episode(
        podcast=podcast,
        topic="Quantum Computing Breakthroughs",
        title="Quantum Computing in 2024",
        description="Latest advances in quantum computing technology"
    )
    
    print(f"Episode created: {episode.title}")
    print(f"Using LLM Provider: OpenAI")
    print(f"Using TTS Provider: ElevenLabs")
    
    # TODO: Add fallback provider demonstration
    # TODO: Add provider switching based on availability
    # TODO: Add provider performance benchmarking


if __name__ == "__main__":
    main()
