"""Shared pytest fixtures and configuration."""

import os
import pytest


@pytest.fixture(autouse=True)
def clean_env(monkeypatch):
    """Automatically clean environment variables for each test.
    
    This fixture runs before each test and ensures a clean environment
    by removing any environment variables that might affect the tests.
    Individual tests can then set their own environment variables as needed.
    """
    # List of environment variable prefixes used by the application
    env_prefixes = ["OPENAI_", "ELEVENLABS_", "STORY_"]
    
    # Get all environment variables that match our prefixes
    vars_to_remove = [
        key for key in os.environ.keys()
        if any(key.startswith(prefix) for prefix in env_prefixes)
    ]
    
    # Remove them for the test
    for var in vars_to_remove:
        monkeypatch.delenv(var, raising=False)


@pytest.fixture
def sample_story_data():
    """Provide sample story data for testing."""
    return {
        "title": "The Unexpected Meeting",
        "description": "A story about a chance encounter that changes everything",
        "content": "It was a typical Tuesday morning when I walked into the coffee shop...",
        "keywords": ["coffee", "meeting", "life-changing"],
    }


@pytest.fixture
def sample_stories_list():
    """Provide a sample list of stories as a string for testing."""
    return """Story 1: The Office Prank
A hilarious prank that went too far at work.
Keywords: office, funny, prank

Story 2: Family Reunion
An emotional reunion after years apart.
Keywords: family, emotional, reunion

Story 3: The Lost Wallet
Finding a wallet and the journey to return it.
Keywords: honesty, journey, wallet"""
