from langchain_openai import ChatOpenAI
from models.configs import LLMConfig
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.utils.pydantic import TBaseModel
from pydantic import SkipValidation
from typing import Annotated, type


class StoryTeller:
    """StoryTeller uses OpenAI's language model to generate answers based on provided data."""

    def __init__(
        self,
        pydantic_object: Annotated[type[TBaseModel], SkipValidation()],
        system_prompt: str = "",
    ):
        llm_config = LLMConfig()
        self.model = ChatOpenAI(
            model=llm_config.MODEL, api_key=llm_config.API_KEY, use_responses_api=True
        )
        self.output_parser = PydanticOutputParser(pydantic_object=pydantic_object)
        self.prompt_template = PromptTemplate(
            template=system_prompt + "\n{user_prompt}\n{format_instructions}",
            input_variables=["user_prompt"],
            partial_variables={
                "format_instructions": self.output_parser.get_format_instructions()
            },
        )
        self.chain = self.prompt_template | self.model | self.output_parser

    def generate_answer(
        self, prompt: str
    ) -> Annotated[type[TBaseModel], SkipValidation()]:
        """Generate a answer based on the provided user prompt.
        Args:
            prompt (str): The user prompt to generate the answer for.
        Returns:
                Annotated[type[TBaseModel], SkipValidation()]: The generated answer as a Pydantic model instance."""
        result = self.chain.invoke({"user_prompt": prompt})
        return result
