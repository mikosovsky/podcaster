"""Tests for the prompts.loader module."""

import pytest

from podcaster.prompts.loader import load_story_prompt


class TestLoadStoryPrompt:
    """Tests for load_story_prompt function."""

    def test_load_story_prompt_success(self, monkeypatch, tmp_path):
        """Test successfully loading and formatting a story prompt."""
        # Create a temporary template file
        template_content = "Generate a story that is {length} long in {language}."
        template_file = tmp_path / "test_prompt.md"
        template_file.write_text(template_content)

        # Set environment variables
        monkeypatch.setenv("STORY_PROMPT_TEMPLATE_PATH", str(template_file))
        monkeypatch.setenv("STORY_LENGTH_MINUTES", "2 minutes")
        monkeypatch.setenv("STORY_LANGUAGE", "English")

        result = load_story_prompt()
        assert result == "Generate a story that is 2 minutes long in English."

    def test_load_story_prompt_with_different_values(self, monkeypatch, tmp_path):
        """Test loading prompt with different length and language values."""
        template_content = "Create a {length} story in {language}."
        template_file = tmp_path / "test_prompt.md"
        template_file.write_text(template_content)

        monkeypatch.setenv("STORY_PROMPT_TEMPLATE_PATH", str(template_file))
        monkeypatch.setenv("STORY_LENGTH_MINUTES", "5 minutes")
        monkeypatch.setenv("STORY_LANGUAGE", "Spanish")

        result = load_story_prompt()
        assert result == "Create a 5 minutes story in Spanish."

    def test_load_story_prompt_file_not_found(self, monkeypatch):
        """Test that FileNotFoundError is raised when template file doesn't exist."""
        monkeypatch.setenv("STORY_PROMPT_TEMPLATE_PATH", "/nonexistent/path.md")
        monkeypatch.setenv("STORY_LENGTH_MINUTES", "2 minutes")
        monkeypatch.setenv("STORY_LANGUAGE", "English")

        with pytest.raises(FileNotFoundError):
            load_story_prompt()

    def test_load_story_prompt_with_complex_template(self, monkeypatch, tmp_path):
        """Test loading a more complex template with multiple placeholders."""
        template_content = """You are a storyteller.
Generate a story that is {length} long.
The story must be in {language}.
Length: {length}
Language: {language}
"""
        template_file = tmp_path / "complex_prompt.md"
        template_file.write_text(template_content)

        monkeypatch.setenv("STORY_PROMPT_TEMPLATE_PATH", str(template_file))
        monkeypatch.setenv("STORY_LENGTH_MINUTES", "3 minutes")
        monkeypatch.setenv("STORY_LANGUAGE", "French")

        result = load_story_prompt()
        assert "3 minutes" in result
        assert "French" in result
        assert result.count("3 minutes") == 2
        assert result.count("French") == 2

    def test_load_story_prompt_preserves_newlines(self, monkeypatch, tmp_path):
        """Test that newlines in the template are preserved."""
        template_content = "Line 1\nLine 2 {length}\nLine 3 {language}\nLine 4"
        template_file = tmp_path / "newline_prompt.md"
        template_file.write_text(template_content)

        monkeypatch.setenv("STORY_PROMPT_TEMPLATE_PATH", str(template_file))
        monkeypatch.setenv("STORY_LENGTH_MINUTES", "1 minute")
        monkeypatch.setenv("STORY_LANGUAGE", "English")

        result = load_story_prompt()
        lines = result.split("\n")
        assert len(lines) == 4
        assert lines[0] == "Line 1"
        assert lines[1] == "Line 2 1 minute"
        assert lines[2] == "Line 3 English"
        assert lines[3] == "Line 4"

    def test_load_story_prompt_empty_template(self, monkeypatch, tmp_path):
        """Test loading an empty template file."""
        template_file = tmp_path / "empty_prompt.md"
        template_file.write_text("")

        monkeypatch.setenv("STORY_PROMPT_TEMPLATE_PATH", str(template_file))
        monkeypatch.setenv("STORY_LENGTH_MINUTES", "2 minutes")
        monkeypatch.setenv("STORY_LANGUAGE", "English")

        result = load_story_prompt()
        assert result == ""

    def test_load_story_prompt_no_placeholders(self, monkeypatch, tmp_path):
        """Test loading a template without placeholders."""
        template_content = "This is a static prompt without any placeholders."
        template_file = tmp_path / "static_prompt.md"
        template_file.write_text(template_content)

        monkeypatch.setenv("STORY_PROMPT_TEMPLATE_PATH", str(template_file))
        monkeypatch.setenv("STORY_LENGTH_MINUTES", "2 minutes")
        monkeypatch.setenv("STORY_LANGUAGE", "English")

        result = load_story_prompt()
        assert result == template_content

    def test_load_story_prompt_utf8_encoding(self, monkeypatch, tmp_path):
        """Test that UTF-8 encoded characters are handled correctly."""
        template_content = "Generate a {length} story in {language}. Special chars: é, ñ, ü, 中文"
        template_file = tmp_path / "utf8_prompt.md"
        template_file.write_text(template_content, encoding="utf-8")

        monkeypatch.setenv("STORY_PROMPT_TEMPLATE_PATH", str(template_file))
        monkeypatch.setenv("STORY_LENGTH_MINUTES", "2 minutes")
        monkeypatch.setenv("STORY_LANGUAGE", "English")

        result = load_story_prompt()
        assert "é" in result
        assert "ñ" in result
        assert "ü" in result
        assert "中文" in result
