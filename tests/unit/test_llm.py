"""Tests for LLM generator functionality."""

import unittest
from src.podcaster.llm import LLMGenerator


class TestLLMGenerator(unittest.TestCase):
    """Test LLMGenerator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.generator = LLMGenerator()
    
    def test_generator_creation(self):
        """Test generator creation."""
        self.assertIsNotNone(self.generator)
        self.assertEqual(self.generator.model, "gpt-4")
    
    def test_generate_script(self):
        """Test script generation."""
        script = self.generator.generate_script(
            topic="AI in Healthcare",
            duration_minutes=5
        )
        self.assertIsInstance(script, str)
        self.assertGreater(len(script), 0)


if __name__ == "__main__":
    unittest.main()
