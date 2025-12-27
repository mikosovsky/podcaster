from elevenlabs import ElevenLabs, AudioWithTimestampsResponse
from models.configs import TTSConfig
from models.schemas import StorySchema, Sex


class SpeechSynthesizer:
    def __init__(self):
        tts_config = TTSConfig()
        self.client = ElevenLabs(api_key=tts_config.API_KEY)
        self.model_id = tts_config.MODEL_ID
        self.female_voice_id = tts_config.FEMALE_VOICE_ID
        self.male_voice_id = tts_config.MALE_VOICE_ID
        self.speed = tts_config.SPEED

    def generate_speech(
        self, story_schema: StorySchema | None = None, text: str = ""
    ) -> AudioWithTimestampsResponse:
        """Generate speech audio from the story content using ElevenLabs Text to Speech.
        Args:
            story_schema (StorySchema): The story data containing content and main character sex.
        Returns:
            AudioWithTimestampsResponse: The generated speech audio with timestamps."""
        if story_schema is None:
            voice_id = self.female_voice_id
            text_to_speak = text
        else:
            voice_id = (
                self.male_voice_id
                if story_schema.sex == Sex.MALE
                else self.female_voice_id
            )
            text_to_speak = story_schema.content

        audio = self.client.text_to_speech.convert_with_timestamps(
            text=text_to_speak,
            voice_id=voice_id,
            model_id=self.model_id,
            voice_settings={"speed": self.speed},
        )
        return audio
