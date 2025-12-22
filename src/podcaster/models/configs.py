from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class LLMConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    OPENAI_API_KEY: str = Field(..., alias="OPENAI_API_KEY")
    OPENAI_MODEL: str = Field(..., alias="OPENAI_MODEL")
    LANGUAGE: str = Field(..., alias="SCRIPT_LANGUAGE")
    SCRIPT_LENGTH_LETTERS_MIN: int = Field(..., alias="SCRIPT_LENGTH_LETTERS_MIN")
    SCRIPT_LENGTH_LETTERS_MAX: int = Field(..., alias="SCRIPT_LENGTH_LETTERS_MAX")
    SCRIPT_LENGTH_MINUTES: int = Field(..., alias="SCRIPT_LENGTH_MINUTES")


class TTSConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    ELEVENLABS_API_KEY: str = Field(..., alias="ELEVENLABS_API_KEY")
    ELEVENLABS_MALE_VOICE_ID: str = Field(..., alias="ELEVENLABS_MALE_VOICE_ID")
    ELEVENLABS_FEMALE_VOICE_ID: str = Field(..., alias="ELEVENLABS_FEMALE_VOICE_ID")
    ELEVENLABS_SPEED: float = Field(..., alias="ELEVENLABS_SPEED")
