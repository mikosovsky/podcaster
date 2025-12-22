from models.configs import PromptConfig

def load_story_prompt() -> str:
    """Load the story prompt template from a file."""
    prompt_config = PromptConfig()
    template_path = prompt_config.PROMPT_TEMPLATE_PATH
    prompt_template = ""
    with open(template_path, "r", encoding="utf-8") as file:
        prompt_template = file.read()
    prompt = prompt_template.format(length=prompt_config.LENGTH_MINUTES, language=prompt_config.LANGUAGE)
    return prompt