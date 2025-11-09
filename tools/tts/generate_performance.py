#!/usr/bin/env python3
"""
Comedy Set TTS Generator

Converts the written comedy set into spoken audio using various TTS providers.
Supports: ElevenLabs, OpenAI TTS, Google TTS (gTTS), and system TTS as fallback.

Usage:
    python generate_performance.py --provider elevenlabs --api-key YOUR_KEY
    python generate_performance.py --provider openai --api-key YOUR_KEY
    python generate_performance.py --provider gtts  # No API key needed
    python generate_performance.py --provider system  # No API key needed

Environment Variables:
    ELEVENLABS_API_KEY - Your ElevenLabs API key
    OPENAI_API_KEY - Your OpenAI API key
"""

import argparse
import os
import sys
import re
from pathlib import Path
from typing import List, Tuple
import time

try:
    import requests
except ImportError:
    print("Installing required package: requests")
    os.system(f"{sys.executable} -m pip install requests -q")
    import requests


class TTSGenerator:
    """Base class for TTS generation"""

    def __init__(self, api_key: str = None):
        self.api_key = api_key

    def generate(self, text: str, output_file: str):
        """Generate audio from text"""
        raise NotImplementedError

    def add_silence(self, duration: float, output_file: str):
        """Add silence/pause"""
        raise NotImplementedError


class ElevenLabsTTS(TTSGenerator):
    """ElevenLabs TTS implementation"""

    VOICE_IDS = {
        "adam": "pNInz6obpgDQGcFmaJgB",  # Deep, narrative
        "Antoni": "ErXwobaYiN019PkySvjV",  # Well-rounded
        "Arnold": "VR6AewLTigWG4xSOukaG",  # Crisp, strong
        "Callum": "N2lVS1w4EtoT3dr4eOWO",  # Middleaged American male
        "Charlie": "IKne3meq5aSn9XLyUdCD",  # Casual, conversational
        "Clyde": "2EiwWnXFnvU5JabPnv8n",  # Mid-range American
        "Dave": "CYw3kZ02Hs0563khs1Fj",  # Young British male
        "Fin": "D38z5RcWu1voky8WS1ja",  # Old Irish male
        "George": "JBFqnCBsd6RMkjVDRZzb",  # Warm British male
        "Josh": "TxGEqnHWrfWFTfGW9XjX",  # Deep, young American
    }

    def __init__(self, api_key: str, voice: str = "Charlie"):
        super().__init__(api_key)
        self.voice_id = self.VOICE_IDS.get(voice, voice)
        self.base_url = "https://api.elevenlabs.io/v1"

    def generate(self, text: str, output_file: str):
        """Generate audio using ElevenLabs API"""
        url = f"{self.base_url}/text-to-speech/{self.voice_id}"

        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.api_key
        }

        data = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.5,  # Lower for more expressive
                "similarity_boost": 0.75,
                "style": 0.5,  # Style exaggeration for comedy
                "use_speaker_boost": True
            }
        }

        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            with open(output_file, 'wb') as f:
                f.write(response.content)
            return True
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return False


class OpenAITTS(TTSGenerator):
    """OpenAI TTS implementation"""

    VOICES = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]

    def __init__(self, api_key: str, voice: str = "onyx"):
        super().__init__(api_key)
        self.voice = voice if voice in self.VOICES else "onyx"

    def generate(self, text: str, output_file: str):
        """Generate audio using OpenAI TTS"""
        try:
            from openai import OpenAI
        except ImportError:
            print("Installing OpenAI package...")
            os.system(f"{sys.executable} -m pip install openai -q")
            from openai import OpenAI

        client = OpenAI(api_key=self.api_key)

        response = client.audio.speech.create(
            model="tts-1-hd",  # Higher quality
            voice=self.voice,
            input=text,
            speed=1.0  # Normal speed for comedy timing
        )

        response.stream_to_file(output_file)
        return True


class GoogleTTS(TTSGenerator):
    """Google TTS (gTTS) implementation - Free, no API key needed"""

    def __init__(self, api_key: str = None):
        super().__init__(api_key)
        try:
            from gtts import gTTS
            self.gtts = gTTS
        except ImportError:
            print("Installing gTTS package...")
            os.system(f"{sys.executable} -m pip install gtts -q")
            from gtts import gTTS
            self.gtts = gTTS

    def generate(self, text: str, output_file: str):
        """Generate audio using Google TTS"""
        max_retries = 3
        for attempt in range(max_retries):
            try:
                tts = self.gtts(text=text, lang='en', slow=False)
                tts.save(output_file)
                return True
            except Exception as e:
                if attempt < max_retries - 1:
                    wait_time = (attempt + 1) * 2
                    print(f"      ⚠️  Error: {str(e)[:80]}...")
                    print(f"      Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    print(f"      ❌ Failed after {max_retries} attempts")
                    print(f"      Consider using --provider system for offline TTS")
                    return False
        return False


class SystemTTS(TTSGenerator):
    """System TTS using pyttsx3 - Works offline, no API key needed"""

    def __init__(self, api_key: str = None):
        super().__init__(api_key)
        try:
            import pyttsx3
            self.engine = pyttsx3.init()
            # Adjust rate for comedy (slightly faster than normal)
            self.engine.setProperty('rate', 175)
        except ImportError:
            print("Installing pyttsx3 package...")
            os.system(f"{sys.executable} -m pip install pyttsx3 -q")
            import pyttsx3
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 175)

    def generate(self, text: str, output_file: str):
        """Generate audio using system TTS"""
        self.engine.save_to_file(text, output_file)
        self.engine.runAndWait()
        return True


def parse_script(script_file: str) -> List[Tuple[str, str]]:
    """
    Parse the performance script and identify segments with timing markers.

    Returns list of (type, content) tuples where type is 'text', 'pause', or 'break'
    """
    with open(script_file, 'r') as f:
        content = f.read()

    segments = []

    # Split by markers while preserving them
    parts = re.split(r'(<pause>|<break>)', content)

    for part in parts:
        part = part.strip()
        if not part:
            continue
        elif part == '<pause>':
            segments.append(('pause', '0.5'))  # 0.5 second pause
        elif part == '<break>':
            segments.append(('break', '1.5'))  # 1.5 second break between bits
        else:
            # Clean up the text
            text = part.replace('\n\n', ' ').replace('\n', ' ')
            text = re.sub(r'\s+', ' ', text)
            if text:
                segments.append(('text', text))

    return segments


def generate_silence(duration: float, output_file: str):
    """Generate a silent audio file of specified duration"""
    try:
        from pydub import AudioSegment
        from pydub.generators import Sine
    except ImportError:
        print("Installing pydub package for silence generation...")
        os.system(f"{sys.executable} -m pip install pydub -q")
        from pydub import AudioSegment
        from pydub.generators import Sine

    # Create silence
    silence = AudioSegment.silent(duration=int(duration * 1000))  # duration in ms
    silence.export(output_file, format="mp3")


def combine_audio_files(file_list: List[str], output_file: str):
    """Combine multiple audio files into one"""
    try:
        from pydub import AudioSegment
    except ImportError:
        print("Installing pydub package for audio combination...")
        os.system(f"{sys.executable} -m pip install pydub -q")
        from pydub import AudioSegment

    combined = AudioSegment.empty()

    for audio_file in file_list:
        if os.path.exists(audio_file):
            segment = AudioSegment.from_mp3(audio_file)
            combined += segment

    combined.export(output_file, format="mp3")
    print(f"\n✅ Final performance saved to: {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Generate spoken performance of comedy set")
    parser.add_argument(
        "--provider",
        choices=["elevenlabs", "openai", "gtts", "system"],
        default="gtts",
        help="TTS provider to use (default: gtts - free, no API key needed)"
    )
    parser.add_argument(
        "--api-key",
        help="API key for the provider (can also use environment variables)"
    )
    parser.add_argument(
        "--voice",
        help="Voice to use (provider-specific)"
    )
    parser.add_argument(
        "--script",
        default="performance_script.txt",
        help="Path to script file (default: performance_script.txt)"
    )
    parser.add_argument(
        "--output",
        default="comedy_set_performance.mp3",
        help="Output file path (default: comedy_set_performance.mp3)"
    )
    parser.add_argument(
        "--no-combine",
        action="store_true",
        help="Don't combine segments, keep individual files"
    )

    args = parser.parse_args()

    # Get API key from args or environment
    api_key = args.api_key
    if not api_key:
        if args.provider == "elevenlabs":
            api_key = os.getenv("ELEVENLABS_API_KEY")
        elif args.provider == "openai":
            api_key = os.getenv("OPENAI_API_KEY")

    # Initialize TTS provider
    if args.provider == "elevenlabs":
        if not api_key:
            print("❌ ElevenLabs API key required. Set ELEVENLABS_API_KEY env var or use --api-key")
            return
        tts = ElevenLabsTTS(api_key, voice=args.voice or "Charlie")
        print(f"🎙️  Using ElevenLabs TTS with voice: {args.voice or 'Charlie'}")
    elif args.provider == "openai":
        if not api_key:
            print("❌ OpenAI API key required. Set OPENAI_API_KEY env var or use --api-key")
            return
        tts = OpenAITTS(api_key, voice=args.voice or "onyx")
        print(f"🎙️  Using OpenAI TTS with voice: {args.voice or 'onyx'}")
    elif args.provider == "gtts":
        tts = GoogleTTS()
        print("🎙️  Using Google TTS (free, no API key needed)")
    else:  # system
        tts = SystemTTS()
        print("🎙️  Using System TTS (offline)")

    # Parse script
    print(f"📝 Parsing script: {args.script}")
    segments = parse_script(args.script)
    print(f"   Found {len(segments)} segments")

    # Create temp directory for segments
    temp_dir = Path("temp_audio_segments")
    temp_dir.mkdir(exist_ok=True)

    # Generate audio for each segment
    audio_files = []

    print("\n🎬 Generating audio segments...")
    for i, (seg_type, content) in enumerate(segments):
        output_file = temp_dir / f"segment_{i:03d}.mp3"

        if seg_type == 'text':
            print(f"   [{i+1}/{len(segments)}] Generating speech: {content[:50]}...")
            success = tts.generate(content, str(output_file))
            if success:
                audio_files.append(str(output_file))
            else:
                print(f"   ⚠️  Failed to generate segment {i}")
        elif seg_type in ['pause', 'break']:
            duration = float(content)
            print(f"   [{i+1}/{len(segments)}] Adding {seg_type} ({duration}s)")
            generate_silence(duration, str(output_file))
            audio_files.append(str(output_file))

    # Combine all segments
    if not args.no_combine and audio_files:
        print("\n🎵 Combining audio segments...")
        combine_audio_files(audio_files, args.output)

        # Clean up temp files
        print("🧹 Cleaning up temporary files...")
        for f in audio_files:
            os.remove(f)
        temp_dir.rmdir()
    else:
        print(f"\n✅ Individual segments saved in: {temp_dir}")

    print("\n🎉 Done!")


if __name__ == "__main__":
    main()
