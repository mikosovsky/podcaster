from pydantic import BaseModel, Field


class StorySchema(BaseModel):
    title: str = Field(..., description="The title of the story")
    description: str = Field(..., description="A brief description of the story")
    content: str = Field(..., description="The content of the story")
    keywords: list[str] = Field(
        default_factory=list,
        description="List of keywords associated with the story e.g., ['reddit', 'funny']",
    )
