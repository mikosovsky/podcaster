"""Tests for the models.configs module."""

import pytest
from pydantic import ValidationError

from podcaster.models.configs import LLMConfig, TTSConfig, PromptConfig


class TestLLMConfig:
    """Tests for LLMConfig model."""

    def test_llm_config_from_env(self, monkeypatch):
        """Test loading LLMConfig from environment variables."""
        monkeypatch.setenv("OPENAI_API_KEY", "test-api-key")
        monkeypatch.setenv("OPENAI_MODEL", "gpt-4")

        config = LLMConfig()
        assert config.API_KEY == "test-api-key"
        assert config.MODEL == "gpt-4"

    def test_llm_config_missing_api_key(self, monkeypatch):
        """Test that ValidationError is raised when API_KEY is missing."""
        monkeypatch.delenv("OPENAI_API_KEY", raising=False)
        monkeypatch.setenv("OPENAI_MODEL", "gpt-4")

        with pytest.raises(ValidationError) as exc_info:
            LLMConfig()

        errors = exc_info.value.errors()
        assert any(error["loc"][0] == "API_KEY" for error in errors)

    def test_llm_config_missing_model(self, monkeypatch):
        """Test that ValidationError is raised when MODEL is missing."""
        monkeypatch.setenv("OPENAI_API_KEY", "test-api-key")
        monkeypatch.delenv("OPENAI_MODEL", raising=False)

        with pytest.raises(ValidationError) as exc_info:
            LLMConfig()

        errors = exc_info.value.errors()
        assert any(error["loc"][0] == "MODEL" for error in errors)


class TestTTSConfig:
    """Tests for TTSConfig model."""

    def test_tts_config_from_env(self, monkeypatch):
        """Test loading TTSConfig from environment variables."""
        monkeypatch.setenv("ELEVENLABS_API_KEY", "test-elevenlabs-key")
        monkeypatch.setenv("ELEVENLABS_MALE_VOICE_ID", "male-voice-id")
        monkeypatch.setenv("ELEVENLABS_FEMALE_VOICE_ID", "female-voice-id")
        monkeypatch.setenv("ELEVENLABS_SPEED", "1.2")

        config = TTSConfig()
        assert config.API_KEY == "test-elevenlabs-key"
        assert config.MALE_VOICE_ID == "male-voice-id"
        assert config.FEMALE_VOICE_ID == "female-voice-id"
        assert config.SPEED == 1.2

    def test_tts_config_missing_required_fields(self, monkeypatch):
        """Test that ValidationError is raised when required fields are missing."""
        # Clear all ELEVENLABS env vars
        for key in ["API_KEY", "MALE_VOICE_ID", "FEMALE_VOICE_ID", "SPEED"]:
            monkeypatch.delenv(f"ELEVENLABS_{key}", raising=False)

        with pytest.raises(ValidationError) as exc_info:
            TTSConfig()

        errors = exc_info.value.errors()
        assert len(errors) >= 4
        error_fields = {error["loc"][0] for error in errors}
        assert "API_KEY" in error_fields
        assert "MALE_VOICE_ID" in error_fields
        assert "FEMALE_VOICE_ID" in error_fields
        assert "SPEED" in error_fields

    def test_tts_config_speed_as_float(self, monkeypatch):
        """Test that SPEED is correctly parsed as a float."""
        monkeypatch.setenv("ELEVENLABS_API_KEY", "test-key")
        monkeypatch.setenv("ELEVENLABS_MALE_VOICE_ID", "male-id")
        monkeypatch.setenv("ELEVENLABS_FEMALE_VOICE_ID", "female-id")
        monkeypatch.setenv("ELEVENLABS_SPEED", "1.5")

        config = TTSConfig()
        assert isinstance(config.SPEED, float)
        assert config.SPEED == 1.5


class TestPromptConfig:
    """Tests for PromptConfig model."""

    def test_prompt_config_from_env(self, monkeypatch):
        """Test loading PromptConfig from environment variables."""
        monkeypatch.setenv("STORY_PROMPT_TEMPLATE_PATH", "configs/story_prompt.md")
        monkeypatch.setenv("STORY_LENGTH_MINUTES", "2 minutes")
        monkeypatch.setenv("STORY_LANGUAGE", "English")

        config = PromptConfig()
        assert config.PROMPT_TEMPLATE_PATH == "configs/story_prompt.md"
        assert config.LENGTH_MINUTES == "2 minutes"
        assert config.LANGUAGE == "English"

    def test_prompt_config_missing_required_fields(self, monkeypatch):
        """Test that ValidationError is raised when required fields are missing."""
        # Clear all STORY env vars
        for key in ["PROMPT_TEMPLATE_PATH", "LENGTH_MINUTES", "LANGUAGE"]:
            monkeypatch.delenv(f"STORY_{key}", raising=False)

        with pytest.raises(ValidationError) as exc_info:
            PromptConfig()

        errors = exc_info.value.errors()
        assert len(errors) >= 3
        error_fields = {error["loc"][0] for error in errors}
        assert "PROMPT_TEMPLATE_PATH" in error_fields
        assert "LENGTH_MINUTES" in error_fields
        assert "LANGUAGE" in error_fields

    def test_prompt_config_different_language(self, monkeypatch):
        """Test that different languages can be configured."""
        monkeypatch.setenv("STORY_PROMPT_TEMPLATE_PATH", "configs/story_prompt.md")
        monkeypatch.setenv("STORY_LENGTH_MINUTES", "3 minutes")
        monkeypatch.setenv("STORY_LANGUAGE", "Spanish")

        config = PromptConfig()
        assert config.LANGUAGE == "Spanish"
