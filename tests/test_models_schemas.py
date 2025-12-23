"""Tests for the models.schemas module."""

import pytest
from pydantic import ValidationError

from podcaster.models.schemas import StorySchema


class TestStorySchema:
    """Tests for StorySchema model."""

    def test_story_schema_valid_creation(self):
        """Test creating a valid StorySchema instance."""
        story = StorySchema(
            title="Test Story",
            description="A test story description",
            content="This is the content of the test story.",
            keywords=["test", "story"],
        )

        assert story.title == "Test Story"
        assert story.description == "A test story description"
        assert story.content == "This is the content of the test story."
        assert story.keywords == ["test", "story"]

    def test_story_schema_default_keywords(self):
        """Test that keywords defaults to empty list."""
        story = StorySchema(
            title="Test Story",
            description="A test story description",
            content="This is the content.",
        )

        assert story.keywords == []

    def test_story_schema_missing_required_fields(self):
        """Test that ValidationError is raised when required fields are missing."""
        with pytest.raises(ValidationError) as exc_info:
            StorySchema()

        errors = exc_info.value.errors()
        assert len(errors) == 3  # title, description, content are required
        error_fields = {error["loc"][0] for error in errors}
        assert error_fields == {"title", "description", "content"}

    def test_story_schema_missing_title(self):
        """Test that ValidationError is raised when title is missing."""
        with pytest.raises(ValidationError) as exc_info:
            StorySchema(
                description="A test story description",
                content="This is the content.",
            )

        errors = exc_info.value.errors()
        assert any(error["loc"][0] == "title" for error in errors)

    def test_story_schema_missing_description(self):
        """Test that ValidationError is raised when description is missing."""
        with pytest.raises(ValidationError) as exc_info:
            StorySchema(
                title="Test Story",
                content="This is the content.",
            )

        errors = exc_info.value.errors()
        assert any(error["loc"][0] == "description" for error in errors)

    def test_story_schema_missing_content(self):
        """Test that ValidationError is raised when content is missing."""
        with pytest.raises(ValidationError) as exc_info:
            StorySchema(
                title="Test Story",
                description="A test story description",
            )

        errors = exc_info.value.errors()
        assert any(error["loc"][0] == "content" for error in errors)

    def test_story_schema_invalid_keywords_type(self):
        """Test that ValidationError is raised when keywords is not a list."""
        with pytest.raises(ValidationError) as exc_info:
            StorySchema(
                title="Test Story",
                description="A test story description",
                content="This is the content.",
                keywords="not_a_list",
            )

        errors = exc_info.value.errors()
        assert any(error["loc"][0] == "keywords" for error in errors)

    def test_story_schema_serialization(self):
        """Test that StorySchema can be serialized to dict."""
        story = StorySchema(
            title="Test Story",
            description="A test story description",
            content="This is the content.",
            keywords=["test", "story"],
        )

        story_dict = story.model_dump()
        assert story_dict == {
            "title": "Test Story",
            "description": "A test story description",
            "content": "This is the content.",
            "keywords": ["test", "story"],
        }

    def test_story_schema_json_serialization(self):
        """Test that StorySchema can be serialized to JSON."""
        story = StorySchema(
            title="Test Story",
            description="A test story description",
            content="This is the content.",
            keywords=["test", "story"],
        )

        story_json = story.model_dump_json()
        assert '"title":"Test Story"' in story_json
        assert '"description":"A test story description"' in story_json
        assert '"content":"This is the content."' in story_json
        assert '"keywords":["test","story"]' in story_json

    def test_story_schema_empty_keywords_list(self):
        """Test that an empty keywords list is valid."""
        story = StorySchema(
            title="Test Story",
            description="A test story description",
            content="This is the content.",
            keywords=[],
        )

        assert story.keywords == []

    def test_story_schema_multiple_keywords(self):
        """Test that multiple keywords can be provided."""
        keywords = ["reddit", "funny", "work", "story", "viral"]
        story = StorySchema(
            title="Test Story",
            description="A test story description",
            content="This is the content.",
            keywords=keywords,
        )

        assert story.keywords == keywords
        assert len(story.keywords) == 5
