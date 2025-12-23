from langchain_openai import ChatOpenAI
from podcaster.models.configs import LLMConfig
from podcaster.models.schemas import StorySchema
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from podcaster.prompts.loader import load_story_prompt


class StoryTeller:
    """StoryTeller uses OpenAI's language model to generate stories based on provided data."""

    def __init__(self):
        llm_config = LLMConfig()
        self.model = ChatOpenAI(model=llm_config.MODEL, api_key=llm_config.API_KEY)
        self.output_parser = PydanticOutputParser(pydantic_object=StorySchema)
        system_prompt = load_story_prompt()
        self.prompt_template = PromptTemplate(
            template=system_prompt
            + "\nLast best stories data:\n{stories_list}\n{format_instructions}",
            input_variables=["stories_list"],
            partial_variables={
                "format_instructions": self.output_parser.get_format_instructions()
            },
        )
        self.chain = self.prompt_template | self.model | self.output_parser

    def generate_story(self, stories_list: str) -> StorySchema:
        """Generate a story based on the provided stories list.
        Args:
            stories_list (str): A string containing the list of 3 most viewed stories.
        Returns:
                StorySchema: The generated story in the form of a StorySchema object."""
        result = self.chain.invoke({"stories_list": stories_list})
        return result
