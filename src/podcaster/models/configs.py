from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class LLMConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    OPENAI_API_KEY: str = Field(..., alias="OPENAI_API_KEY")
    OPENAI_MODEL: str = Field(..., alias="OPENAI_MODEL")


class TTSConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    ELEVENLABS_API_KEY: str = Field(..., alias="ELEVENLABS_API_KEY")
    ELEVENLABS_MALE_VOICE_ID: str = Field(..., alias="ELEVENLABS_MALE_VOICE_ID")
    ELEVENLABS_FEMALE_VOICE_ID: str = Field(..., alias="ELEVENLABS_FEMALE_VOICE_ID")
    ELEVENLABS_SPEED: float = Field(..., alias="ELEVENLABS_SPEED")


class PromptConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    STORY_PROMPT_TEMPLATE_PATH: str = Field(..., alias="STORY_PROMPT_TEMPLATE_PATH")
    STORY_LENGTH_LETTERS_MIN: int = Field(..., alias="STORY_LENGTH_LETTERS_MIN")
    STORY_LENGTH_LETTERS_MAX: int = Field(..., alias="STORY_LENGTH_LETTERS_MAX")
    STORY_LENGTH_MINUTES: int = Field(..., alias="STORY_LENGTH_MINUTES")
    LANGUAGE: str = Field(..., alias="STORY_LANGUAGE")
