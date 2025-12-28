import base64


def base64_to_mp3(base64_string: str, output_file: str) -> None:
    """Convert a base64 string to an MP3 file.

    Args:
        base64_string (str): The base64 encoded string.
        output_file (str): The path to the output MP3 file.
    """
    audio_data = base64.b64decode(base64_string)
    with open(output_file, "wb") as file:
        file.write(audio_data)