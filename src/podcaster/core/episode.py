"""Episode data model and management."""

from dataclasses import dataclass, field
from typing import Optional, Dict
from datetime import datetime
import uuid

# TODO: Add episode status tracking (draft, in-progress, completed, published)
# TODO: Add episode tags/categories
# TODO: Add chapter markers support


@dataclass
class Episode:
    """Represents a single podcast episode."""
    
    title: str
    description: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    script: Optional[str] = None
    audio_path: Optional[str] = None
    transcript: Optional[str] = None
    duration_seconds: Optional[float] = None
    created_at: datetime = field(default_factory=datetime.now)
    published_at: Optional[datetime] = None
    metadata: Dict = field(default_factory=dict)
    
    def __str__(self) -> str:
        return f"Episode(id='{self.id[:8]}...', title='{self.title}')"
    
    # TODO: Add method to export episode to JSON
    # TODO: Add method to calculate estimated reading time from script
    # TODO: Add method to validate episode data completeness
    # TODO: Add method to generate episode show notes from script
