from models.configs import PromptConfig


def load_story_prompt() -> str:
    """Load the prompt template from a file and format it with length and language.
    Returns:
        str: The formatted prompt to generate a story as a string.
    """
    prompt_config = PromptConfig()
    template_path = prompt_config.PROMPT_TEMPLATE_PATH
    prompt_template = ""
    with open(template_path, "r", encoding="utf-8") as file:
        prompt_template = file.read()
    prompt = prompt_template.format(
        length=prompt_config.LENGTH_MINUTES, language=prompt_config.LANGUAGE
    )
    return prompt
