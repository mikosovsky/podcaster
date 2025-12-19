"""Tests for podcast core functionality."""

import unittest
from src.podcaster.core import Podcast, Episode


class TestPodcast(unittest.TestCase):
    """Test Podcast class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.podcast = Podcast(
            title="Test Podcast",
            description="A test podcast",
            author="Test Author"
        )
    
    def test_podcast_creation(self):
        """Test podcast creation."""
        self.assertEqual(self.podcast.title, "Test Podcast")
        self.assertEqual(self.podcast.author, "Test Author")
        self.assertEqual(len(self.podcast.episodes), 0)
    
    def test_add_episode(self):
        """Test adding episode to podcast."""
        episode = Episode(
            title="Test Episode",
            description="A test episode"
        )
        self.podcast.add_episode(episode)
        self.assertEqual(len(self.podcast.episodes), 1)
    
    def test_get_episode(self):
        """Test retrieving episode by ID."""
        episode = Episode(
            title="Test Episode",
            description="A test episode"
        )
        self.podcast.add_episode(episode)
        retrieved = self.podcast.get_episode(episode.id)
        self.assertEqual(retrieved, episode)


class TestEpisode(unittest.TestCase):
    """Test Episode class."""
    
    def test_episode_creation(self):
        """Test episode creation."""
        episode = Episode(
            title="Test Episode",
            description="A test episode"
        )
        self.assertEqual(episode.title, "Test Episode")
        self.assertIsNotNone(episode.id)
        self.assertIsNone(episode.script)
    
    def test_episode_with_script(self):
        """Test episode with script."""
        episode = Episode(
            title="Test Episode",
            description="A test episode",
            script="This is a test script."
        )
        self.assertEqual(episode.script, "This is a test script.")


if __name__ == "__main__":
    unittest.main()
