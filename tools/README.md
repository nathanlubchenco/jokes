# Tools & Utilities

Scripts and utilities for working with the comedy material.

## 📁 tts/ - Text-to-Speech Generation

Convert written comedy sets into spoken audio performances.

### Quick Start:

```bash
cd tts/
pip install -r requirements.txt
python generate_performance.py
```

### Files:

- **generate_performance.py** - Main TTS generation script
  - Supports multiple providers: ElevenLabs, OpenAI, Google TTS, System TTS
  - Handles timing markers (`<pause>`, `<break>`)
  - Combines audio segments automatically

- **performance_script.txt** - TTS-optimized script of the comedy set
  - Includes timing markers for natural delivery
  - Formatted for text-to-speech engines

- **requirements.txt** - Python dependencies

### Documentation:

See `../docs/guides/tts/` for full TTS documentation:
- `README.md` - Quick start guide
- `guide.md` - Comprehensive guide with all providers, voices, troubleshooting

### Usage Examples:

```bash
# Free option (Google TTS)
python generate_performance.py --provider gtts

# Premium quality (ElevenLabs)
export ELEVENLABS_API_KEY="your_key"
python generate_performance.py --provider elevenlabs --voice Charlie

# OpenAI TTS
export OPENAI_API_KEY="your_key"
python generate_performance.py --provider openai --voice onyx

# Offline (System TTS)
python generate_performance.py --provider system
```

## Future Tools

Potential additions:
- Joke analyzer (test premises against quality criteria)
- Callback finder (identify callback opportunities in sets)
- Timing calculator (estimate runtime from script)
- Laugh density analyzer (estimate laughs per minute)
