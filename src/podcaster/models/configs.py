from pydantic_settings import BaseSettings, SettingsConfigDict


class LLMConfig(BaseSettings):
    """Configuration for the language model."""
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="OPENAI_", extra="ignore"
    )
    API_KEY: str
    MODEL: str


class TTSConfig(BaseSettings):
    """Configuration for the text-to-speech service."""
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="ELEVENLABS_",
        extra="ignore",
    )
    API_KEY: str
    MALE_VOICE_ID: str
    FEMALE_VOICE_ID: str
    SPEED: float


class PromptConfig(BaseSettings):
    """Configuration for story prompt generation."""
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="STORY_", extra="ignore"
    )
    PROMPT_TEMPLATE_PATH: str
    LENGTH_MINUTES: str
    LANGUAGE: str
