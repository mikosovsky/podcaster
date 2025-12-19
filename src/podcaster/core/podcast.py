"""Podcast data model and management."""

from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

# TODO: Add RSS feed generation support
# TODO: Add podcast artwork/cover image handling
# TODO: Add podcast statistics and analytics


@dataclass
class Podcast:
    """Represents a podcast series with metadata and episodes."""
    
    title: str
    description: str
    author: str
    language: str = "en"
    category: str = "Technology"
    created_at: datetime = field(default_factory=datetime.now)
    episodes: List["Episode"] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)
    
    def add_episode(self, episode: "Episode") -> None:
        """Add an episode to the podcast."""
        self.episodes.append(episode)
    
    def get_episode(self, episode_id: str) -> Optional["Episode"]:
        """Get an episode by ID."""
        for episode in self.episodes:
            if episode.id == episode_id:
                return episode
        return None
    
    def __str__(self) -> str:
        return f"Podcast(title='{self.title}', episodes={len(self.episodes)})"
    
    # TODO: Add method to export podcast metadata to JSON/XML
    # TODO: Add method to generate RSS feed
    # TODO: Add method to validate podcast metadata
    # TODO: Add method to sort/filter episodes by date, title, etc.
