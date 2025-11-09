# Text-to-Speech for Comedy Set

We've added the ability to convert the written comedy set into spoken audio!

## Quick Start

The easiest way:

```bash
# Install dependencies
pip install -r requirements.txt

# Generate audio (uses free Google TTS)
python generate_performance.py
```

This creates `comedy_set_performance.mp3` - an 8.5-minute spoken performance of the comedy set!

## Options

### 1. **Google TTS** (Free, default)
```bash
python generate_performance.py --provider gtts
```
- ✅ Free, no API key
- ⚠️ May hit rate limits in some environments
- 💡 Best for testing

### 2. **ElevenLabs** (Best quality)
```bash
export ELEVENLABS_API_KEY="your_key"
python generate_performance.py --provider elevenlabs --voice Charlie
```
- ✅ Most natural sounding
- ✅ Best for comedy delivery
- ⚠️ Requires paid API key
- 💡 Free tier: 10,000 chars/month

### 3. **OpenAI TTS** (Good quality)
```bash
export OPENAI_API_KEY="your_key"
python generate_performance.py --provider openai --voice onyx
```
- ✅ High quality
- ✅ Affordable ($0.08 for full set)
- ⚠️ Requires API key

### 4. **System TTS** (Offline)
```bash
python generate_performance.py --provider system
```
- ✅ Works offline
- ✅ Free
- ⚠️ Robotic quality

## Files

- `performance_script.txt` - Full 8.5-minute set optimized for TTS
- `generate_performance.py` - TTS generation script
- `TTS_GUIDE.md` - Comprehensive guide with all options and troubleshooting

## Script Format

The script uses timing markers:
- `<pause>` - Short pause (0.5s) for punchline timing
- `<break>` - Longer break (1.5s) between bits

## Examples

```bash
# Generate with custom voice
python generate_performance.py --provider elevenlabs --voice Josh

# Use custom script
python generate_performance.py --script my_jokes.txt --output my_set.mp3

# Keep individual segments (don't combine)
python generate_performance.py --no-combine
```

## For Best Results

1. **Test first** with free Google TTS
2. **Adjust timing** in `performance_script.txt` if needed
3. **Upgrade** to ElevenLabs or OpenAI for final quality

See **[TTS_GUIDE.md](TTS_GUIDE.md)** for complete documentation!

---

**Note:** If you encounter rate limits with Google TTS, try using `--provider system` for offline generation, or upgrade to a premium provider.
