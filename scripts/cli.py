#!/usr/bin/env python3
"""
Podcaster CLI - Command-line interface for podcast creation.

This CLI provides easy access to podcast creation features:
- Create episodes from topics using LLMs
- Synthesize audio from scripts using TTS
- Manage podcast metadata and files

Usage:
    python cli.py create --topic "AI in Healthcare" --title "Episode 1"
    python cli.py synthesize --script-path path/to/script.txt
"""

import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from podcaster.core import Podcast, PodcastOrchestrator
from podcaster.llm import LLMGenerator
from podcaster.tts import TTSSynthesizer
from podcaster.utils import ConfigManager, FileManager

# TODO: Add interactive mode for guided podcast creation
# TODO: Add progress bars for long-running operations
# TODO: Add verbose/quiet modes for output control
# TODO: Add configuration file support via --config flag


def create_podcast_command(args):
    """Create a new podcast episode."""
    print(f"Creating podcast episode on topic: {args.topic}")
    
    # Initialize components
    podcast = Podcast(
        title=args.podcast_title or "My Podcast",
        description=args.podcast_description or "Generated podcast",
        author=args.author or "Podcaster"
    )
    
    orchestrator = PodcastOrchestrator(
        llm_generator=LLMGenerator(),
        synthesizer=TTSSynthesizer()
    )
    
    # Create episode
    episode = orchestrator.create_episode(
        podcast=podcast,
        topic=args.topic,
        title=args.title,
        description=args.description
    )
    
    print(f"Episode created: {episode.title}")
    print(f"Episode ID: {episode.id}")
    if episode.script:
        print(f"Script length: {len(episode.script)} characters")
    if episode.audio_path:
        print(f"Audio saved to: {episode.audio_path}")
    
    # TODO: Save episode metadata to file
    # TODO: Add option to preview script before synthesis
    # TODO: Add option to edit script interactively


def synthesize_command(args):
    """Synthesize speech from text."""
    print(f"Synthesizing speech from: {args.script_path or 'stdin'}")
    
    if args.script_path:
        text = Path(args.script_path).read_text()
    else:
        text = args.text
    
    synthesizer = TTSSynthesizer(voice=args.voice)
    output_path = synthesizer.synthesize(
        text,
        output_path=Path(args.output) if args.output else None
    )
    
    print(f"Audio generated: {output_path}")
    
    # TODO: Add audio post-processing options
    # TODO: Add preview playback before saving
    # TODO: Add batch synthesis from multiple scripts


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Podcaster - AI-powered podcast creation tool using LLMs and Text2Speech"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Create command
    create_parser = subparsers.add_parser("create", help="Create a new podcast episode")
    create_parser.add_argument("--topic", required=True, help="Episode topic")
    create_parser.add_argument("--title", required=True, help="Episode title")
    create_parser.add_argument("--description", help="Episode description")
    create_parser.add_argument("--podcast-title", help="Podcast series title")
    create_parser.add_argument("--podcast-description", help="Podcast series description")
    create_parser.add_argument("--author", help="Podcast author")
    create_parser.add_argument("--output-dir", help="Output directory", default="./data/output")
    
    # Synthesize command
    synthesize_parser = subparsers.add_parser("synthesize", help="Synthesize speech from text")
    synthesize_parser.add_argument("--script-path", help="Path to script file")
    synthesize_parser.add_argument("--text", help="Text to synthesize")
    synthesize_parser.add_argument("--output", help="Output audio file", default="output.mp3")
    synthesize_parser.add_argument("--voice", help="Voice to use", default="default")
    
    args = parser.parse_args()
    
    if args.command == "create":
        create_podcast_command(args)
    elif args.command == "synthesize":
        synthesize_command(args)
    else:
        parser.print_help()
        sys.exit(1)
    
    # TODO: Add 'list' command to show all episodes
    # TODO: Add 'delete' command to remove episodes
    # TODO: Add 'export' command to package podcast for distribution


if __name__ == "__main__":
    main()
