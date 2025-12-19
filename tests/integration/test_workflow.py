"""Integration tests for podcast workflow."""

import unittest
from pathlib import Path
from src.podcaster.core import Podcast, PodcastOrchestrator
from src.podcaster.llm import LLMGenerator
from src.podcaster.tts import TTSSynthesizer


class TestPodcastWorkflow(unittest.TestCase):
    """Test complete podcast creation workflow."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.podcast = Podcast(
            title="Test Podcast",
            description="Integration test podcast",
            author="Test Author"
        )
        self.orchestrator = PodcastOrchestrator(
            llm_generator=LLMGenerator(),
            synthesizer=TTSSynthesizer()
        )
    
    def test_create_episode_workflow(self):
        """Test creating a complete episode."""
        episode = self.orchestrator.create_episode(
            podcast=self.podcast,
            topic="Testing AI Podcasts",
            title="Test Episode",
            description="A test episode"
        )
        
        self.assertIsNotNone(episode)
        self.assertEqual(episode.title, "Test Episode")
        self.assertIsNotNone(episode.script)


if __name__ == "__main__":
    unittest.main()
