from pydantic import BaseModel, Field
from enum import Enum


class Sex(str, Enum):
    MALE = "male"
    FEMALE = "female"


class StorySchema(BaseModel):
    title: str = Field(..., description="The title of the story")
    description: str = Field(..., description="A brief description of the story")
    content: str = Field(..., description="The content of the story")
    sex: Sex = Field(..., description="The sex of the main character.")
    keywords: list[str] = Field(
        default_factory=list,
        description="List of keywords associated with the story e.g., ['reddit', 'funny']",
    )
