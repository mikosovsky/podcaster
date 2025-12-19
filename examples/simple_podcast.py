"""Example: Create a simple podcast episode.

This example demonstrates the basic workflow:
1. Create a podcast series
2. Initialize LLM and TTS components
3. Generate an episode from a topic
4. View the results
"""

from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from podcaster.core import Podcast, Episode, PodcastOrchestrator
from podcaster.llm import LLMGenerator
from podcaster.tts import TTSSynthesizer

# TODO: Add error handling and validation
# TODO: Add configuration loading from file
# TODO: Add logging for debugging


def main():
    """Create a simple podcast episode."""
    print("Creating a podcast episode example...")
    
    # Create a podcast
    podcast = Podcast(
        title="Tech Talk Podcast",
        description="Discussions about technology and innovation",
        author="Tech Team",
        language="en",
        category="Technology"
    )
    
    # Initialize the orchestrator
    orchestrator = PodcastOrchestrator(
        llm_generator=LLMGenerator(model="gpt-4", temperature=0.7),
        synthesizer=TTSSynthesizer(voice="default")
    )
    
    # Create an episode
    episode = orchestrator.create_episode(
        podcast=podcast,
        topic="The Future of Artificial Intelligence",
        title="AI: What's Next?",
        description="Exploring the latest developments in AI and their impact on society"
    )
    
    print(f"\nPodcast: {podcast.title}")
    print(f"Episode: {episode.title}")
    print(f"Episode ID: {episode.id}")
    print(f"Script preview: {episode.script[:200] if episode.script else 'N/A'}...")
    print(f"Total episodes: {len(podcast.episodes)}")
    
    # TODO: Add audio playback functionality
    # TODO: Add episode export to various formats
    # TODO: Add episode statistics (duration, word count, etc.)


if __name__ == "__main__":
    main()
