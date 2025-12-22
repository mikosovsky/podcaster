"""Tests for the providers.openai module."""

from unittest.mock import Mock, patch

from podcaster.providers.openai import StoryTeller
from podcaster.models.schemas import StorySchema


class TestStoryTeller:
    """Tests for StoryTeller class."""

    @patch("podcaster.providers.openai.LLMConfig")
    @patch("podcaster.providers.openai.ChatOpenAI")
    @patch("podcaster.providers.openai.load_story_prompt")
    def test_storyteller_initialization(
        self, mock_load_prompt, mock_chat_openai, mock_llm_config
    ):
        """Test StoryTeller initialization."""
        # Setup mocks
        mock_config_instance = Mock()
        mock_config_instance.API_KEY = "test-api-key"
        mock_config_instance.MODEL = "gpt-4"
        mock_llm_config.return_value = mock_config_instance

        mock_load_prompt.return_value = "Test prompt template"

        # Initialize StoryTeller
        storyteller = StoryTeller()

        # Verify LLMConfig was called
        mock_llm_config.assert_called_once()

        # Verify ChatOpenAI was initialized with correct params
        mock_chat_openai.assert_called_once_with(
            model="gpt-4", api_key="test-api-key"
        )

        # Verify load_story_prompt was called
        mock_load_prompt.assert_called_once()

        # Verify that the prompt template was set up
        assert storyteller.prompt_template is not None
        assert storyteller.chain is not None

    @patch("podcaster.providers.openai.LLMConfig")
    @patch("podcaster.providers.openai.ChatOpenAI")
    @patch("podcaster.providers.openai.load_story_prompt")
    def test_storyteller_generate_story(
        self, mock_load_prompt, mock_chat_openai, mock_llm_config
    ):
        """Test StoryTeller generate_story method."""
        # Setup mocks
        mock_config_instance = Mock()
        mock_config_instance.API_KEY = "test-api-key"
        mock_config_instance.MODEL = "gpt-4"
        mock_llm_config.return_value = mock_config_instance

        mock_load_prompt.return_value = "Test prompt"

        # Mock the chain invoke method to return a StorySchema
        expected_story = StorySchema(
            title="Generated Story",
            description="A generated story description",
            content="This is the generated story content.",
            keywords=["generated", "test"],
        )

        # Initialize StoryTeller
        storyteller = StoryTeller()
        storyteller.chain = Mock()
        storyteller.chain.invoke = Mock(return_value=expected_story)

        # Call generate_story
        stories_list = "Story 1\nStory 2\nStory 3"
        result = storyteller.generate_story(stories_list)

        # Verify the chain was invoked with correct parameters
        storyteller.chain.invoke.assert_called_once_with(
            {"stories_list": stories_list}
        )

        # Verify the result
        assert isinstance(result, StorySchema)
        assert result.title == "Generated Story"
        assert result.description == "A generated story description"
        assert result.content == "This is the generated story content."
        assert result.keywords == ["generated", "test"]

    @patch("podcaster.providers.openai.LLMConfig")
    @patch("podcaster.providers.openai.ChatOpenAI")
    @patch("podcaster.providers.openai.load_story_prompt")
    def test_storyteller_generate_story_empty_keywords(
        self, mock_load_prompt, mock_chat_openai, mock_llm_config
    ):
        """Test generating a story with empty keywords."""
        # Setup mocks
        mock_config_instance = Mock()
        mock_config_instance.API_KEY = "test-api-key"
        mock_config_instance.MODEL = "gpt-4"
        mock_llm_config.return_value = mock_config_instance

        mock_load_prompt.return_value = "Test prompt"

        expected_story = StorySchema(
            title="Story Without Keywords",
            description="A story without keywords",
            content="Content without keywords.",
        )

        storyteller = StoryTeller()
        storyteller.chain = Mock()
        storyteller.chain.invoke = Mock(return_value=expected_story)

        result = storyteller.generate_story("Some stories")

        assert isinstance(result, StorySchema)
        assert result.keywords == []

    @patch("podcaster.providers.openai.LLMConfig")
    @patch("podcaster.providers.openai.ChatOpenAI")
    @patch("podcaster.providers.openai.load_story_prompt")
    def test_storyteller_prompt_template_includes_format_instructions(
        self, mock_load_prompt, mock_chat_openai, mock_llm_config
    ):
        """Test that the prompt template includes format instructions."""
        # Setup mocks
        mock_config_instance = Mock()
        mock_config_instance.API_KEY = "test-api-key"
        mock_config_instance.MODEL = "gpt-4"
        mock_llm_config.return_value = mock_config_instance

        system_prompt = "Generate a story"
        mock_load_prompt.return_value = system_prompt

        # Initialize StoryTeller
        storyteller = StoryTeller()

        # Verify the prompt template contains the system prompt
        assert storyteller.prompt_template is not None
        # The template should include the system prompt and placeholders
        template_str = storyteller.prompt_template.template
        assert system_prompt in template_str
        assert "{stories_list}" in template_str
        assert "{format_instructions}" in template_str

    @patch("podcaster.providers.openai.LLMConfig")
    @patch("podcaster.providers.openai.ChatOpenAI")
    @patch("podcaster.providers.openai.load_story_prompt")
    def test_storyteller_output_parser(
        self, mock_load_prompt, mock_chat_openai, mock_llm_config
    ):
        """Test that the output parser is configured correctly."""
        # Setup mocks
        mock_config_instance = Mock()
        mock_config_instance.API_KEY = "test-api-key"
        mock_config_instance.MODEL = "gpt-4"
        mock_llm_config.return_value = mock_config_instance

        mock_load_prompt.return_value = "Test prompt"

        # Initialize StoryTeller
        storyteller = StoryTeller()

        # Verify output_parser exists and has correct pydantic_object
        assert storyteller.output_parser is not None
        assert storyteller.output_parser.pydantic_object == StorySchema

    @patch("podcaster.providers.openai.LLMConfig")
    @patch("podcaster.providers.openai.ChatOpenAI")
    @patch("podcaster.providers.openai.load_story_prompt")
    def test_storyteller_with_multiline_stories_list(
        self, mock_load_prompt, mock_chat_openai, mock_llm_config
    ):
        """Test generating a story with a multiline stories list."""
        # Setup mocks
        mock_config_instance = Mock()
        mock_config_instance.API_KEY = "test-api-key"
        mock_config_instance.MODEL = "gpt-4"
        mock_llm_config.return_value = mock_config_instance

        mock_load_prompt.return_value = "Test prompt"

        expected_story = StorySchema(
            title="Multiline Story",
            description="Story from multiline input",
            content="Content based on multiple stories.",
            keywords=["multiline", "input"],
        )

        storyteller = StoryTeller()
        storyteller.chain = Mock()
        storyteller.chain.invoke = Mock(return_value=expected_story)

        # Test with multiline input
        stories_list = """Story 1: Title
Story 1: Description
Story 1: Content

Story 2: Title
Story 2: Description
Story 2: Content

Story 3: Title
Story 3: Description
Story 3: Content"""

        result = storyteller.generate_story(stories_list)

        storyteller.chain.invoke.assert_called_once_with(
            {"stories_list": stories_list}
        )
        assert isinstance(result, StorySchema)
