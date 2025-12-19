"""Setup script for Podcaster package."""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="podcaster",
    version="0.1.0",
    author="Podcaster Team",
    author_email="contact@podcaster.example",
    description="AI-powered podcast creation tool using LLMs and Text2Speech",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mikosovsky/podcaster",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
    install_requires=[
        # Core dependencies
        "pyyaml>=6.0",
        "python-dotenv>=1.0.0",
        
        # Optional: LLM providers (install based on your needs)
        # "openai>=1.0.0",
        # "anthropic>=0.7.0",
        
        # Optional: Text-to-Speech
        # "elevenlabs>=0.2.0",
        # "edge-tts>=6.1.0",
        # "TTS>=0.22.0",  # Coqui TTS
        
        # Optional: Audio processing
        # "pydub>=0.25.0",
        # "soundfile>=0.12.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
            "isort>=5.12.0",
        ],
        "llm": [
            "openai>=1.0.0",
            "anthropic>=0.7.0",
        ],
        "tts": [
            "elevenlabs>=0.2.0",
            "edge-tts>=6.1.0",
            "TTS>=0.22.0",
        ],
        "audio": [
            "pydub>=0.25.0",
            "soundfile>=0.12.0",
            "ffmpeg-python>=0.2.0",
        ],
        "all": [
            "openai>=1.0.0",
            "anthropic>=0.7.0",
            "elevenlabs>=0.2.0",
            "edge-tts>=6.1.0",
            "TTS>=0.22.0",
            "pydub>=0.25.0",
            "soundfile>=0.12.0",
            "ffmpeg-python>=0.2.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "podcaster=scripts.cli:main",
        ],
    },
)
