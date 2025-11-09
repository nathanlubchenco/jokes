# Text-to-Speech Performance Guide

This guide explains how to convert the written comedy set into a spoken audio performance using various TTS providers.

## Quick Start (Free Option)

The easiest way to get started uses **Google TTS** - no API key required:

```bash
# Install dependencies
pip install -r requirements.txt

# Generate performance (uses Google TTS by default)
python generate_performance.py

# Output: comedy_set_performance.mp3
```

## TTS Provider Options

### 1. Google TTS (gTTS) - **FREE** ✅
**Best for:** Testing, demos, no-cost option

```bash
python generate_performance.py --provider gtts
```

**Pros:**
- ✅ Completely free
- ✅ No API key required
- ✅ Decent quality
- ✅ Easy to use

**Cons:**
- ❌ Less natural than premium options
- ❌ Limited control over voice characteristics
- ❌ Robotic timing

---

### 2. ElevenLabs - **PREMIUM** 💎
**Best for:** Professional quality, natural delivery, comedy timing

```bash
# Set API key
export ELEVENLABS_API_KEY="your_api_key_here"

# Generate with default voice (Charlie - conversational)
python generate_performance.py --provider elevenlabs

# Or specify a voice
python generate_performance.py --provider elevenlabs --voice Adam
```

**Available Voices:**
- `Charlie` (Casual, conversational) - **Recommended for comedy**
- `Adam` (Deep, narrative)
- `Josh` (Deep, young American)
- `Antoni` (Well-rounded)
- `Arnold` (Crisp, strong)
- `Callum` (Middle-aged American)
- `Clyde` (Mid-range American)
- `George` (Warm British)

**Pros:**
- ✅ Most natural sounding
- ✅ Best for comedy timing
- ✅ Expressive delivery
- ✅ Multiple voice options
- ✅ Good with emphasis and pauses

**Cons:**
- ❌ Requires paid API key
- ❌ Costs per character generated

**Pricing:**
- Free tier: 10,000 characters/month
- Starter: $5/month for 30,000 characters
- Creator: $22/month for 100,000 characters

**Get API Key:** https://elevenlabs.io/

---

### 3. OpenAI TTS - **PREMIUM** 🤖
**Best for:** Good quality, if you already have OpenAI API access

```bash
# Set API key
export OPENAI_API_KEY="your_api_key_here"

# Generate with default voice (onyx)
python generate_performance.py --provider openai

# Or specify a voice
python generate_performance.py --provider openai --voice echo
```

**Available Voices:**
- `onyx` (Deep, authoritative) - **Recommended for comedy**
- `echo` (Clear, engaging)
- `alloy` (Neutral)
- `fable` (British accent)
- `nova` (Energetic)
- `shimmer` (Soft)

**Pros:**
- ✅ Very good quality
- ✅ Reliable API
- ✅ Good value for existing OpenAI users

**Cons:**
- ❌ Requires paid API key
- ❌ Less expressive than ElevenLabs
- ❌ Timing can be flat

**Pricing:**
- $15 per 1 million characters (~$0.015 per 1,000 characters)
- Our 8-minute set ≈ 5,000 characters ≈ $0.08

**Get API Key:** https://platform.openai.com/api-keys

---

### 4. System TTS (pyttsx3) - **FREE** 🖥️
**Best for:** Offline usage, testing

```bash
python generate_performance.py --provider system
```

**Pros:**
- ✅ Completely free
- ✅ Works offline
- ✅ No API key needed

**Cons:**
- ❌ Very robotic
- ❌ Poor timing
- ❌ Not recommended for final performance

---

## Advanced Usage

### Custom Script File
```bash
python generate_performance.py --script my_custom_script.txt --output my_performance.mp3
```

### Keep Individual Segments
```bash
# Generates individual files without combining
python generate_performance.py --no-combine
```

### Using API Key Directly
```bash
# Instead of environment variable
python generate_performance.py --provider elevenlabs --api-key sk_xxxxx
```

---

## Script Format

The performance script uses special markers for timing:

### Markers:
- `<pause>` - Short pause (0.5 seconds) for comedic timing
- `<break>` - Longer break (1.5 seconds) between bits

### Example:
```
I got a smart home system because I wanted to feel like I was living in the future.

<pause>

Turns out the future is just getting judged by your furniture.

<break>

Every website wants a unique password now...
```

### Tips for Script Editing:
1. Use `<pause>` before/after punchlines
2. Use `<break>` between different bits/topics
3. Remove stage directions like *(beat)* or *[gesture]*
4. Keep emphasis markers: CAPS for loud words
5. Keep natural punctuation for rhythm

---

## Quality Comparison

Based on testing with our comedy set:

| Provider | Quality | Timing | Naturalness | Cost | Best For |
|----------|---------|--------|-------------|------|----------|
| **ElevenLabs** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | $$$ | Final performance |
| **OpenAI** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | $$ | Good alternative |
| **Google TTS** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | FREE | Testing/demos |
| **System TTS** | ⭐⭐ | ⭐ | ⭐ | FREE | Offline only |

---

## Recommended Workflow

### For Testing/Development:
```bash
# Quick test with free option
python generate_performance.py --provider gtts

# Listen and adjust script timing
# Edit performance_script.txt to add pauses

# Test again
python generate_performance.py --provider gtts
```

### For Final Performance:
```bash
# Use ElevenLabs for best quality
export ELEVENLABS_API_KEY="your_key"

python generate_performance.py \
  --provider elevenlabs \
  --voice Charlie \
  --output final_comedy_set.mp3
```

---

## Troubleshooting

### "Module not found" errors
```bash
pip install -r requirements.txt
```

### ElevenLabs API errors
- Check your API key is valid
- Verify you have credits remaining
- Check character limit for your tier

### Audio combination fails
```bash
# Install ffmpeg (required by pydub)
# macOS:
brew install ffmpeg

# Ubuntu/Debian:
sudo apt-get install ffmpeg

# Windows:
# Download from https://ffmpeg.org/download.html
```

### Output sounds robotic
- Try different voices
- Adjust pause durations in script
- Use premium provider (ElevenLabs or OpenAI)

---

## Tips for Best Results

### 1. Voice Selection
- **Comedy works best with:** Conversational, casual voices
- **ElevenLabs:** Charlie, Josh, or Callum
- **OpenAI:** onyx or echo
- **Avoid:** Overly formal or theatrical voices

### 2. Script Timing
- Add `<pause>` before punchlines (builds anticipation)
- Add `<pause>` after big laughs (let it land)
- Use `<break>` between topic changes
- Don't overuse pauses (kills momentum)

### 3. Emphasis
- Use CAPS for emphasized words
- Use punctuation for rhythm (commas, periods, ellipses...)
- Break long sentences into shorter ones
- Read aloud to test flow

### 4. Cost Optimization
- **Test with gTTS first** (free) to get timing right
- **Only use premium TTS for final version**
- Our 8-minute set ≈ 5,000 characters
  - ElevenLabs: ~$0.17 on starter plan
  - OpenAI: ~$0.08
- Edit script to remove unnecessary words

---

## Example: Full Workflow

```bash
# 1. Install dependencies
pip install requests gtts pydub

# 2. Test with free option
python generate_performance.py --provider gtts

# 3. Listen to comedy_set_performance.mp3
# (Adjust timing in performance_script.txt as needed)

# 4. Get ElevenLabs API key from elevenlabs.io
# (Free tier gives you 10,000 characters/month)

# 5. Generate final version
export ELEVENLABS_API_KEY="sk_xxxxx"
python generate_performance.py \
  --provider elevenlabs \
  --voice Charlie \
  --output final_performance.mp3

# 6. Listen to final_performance.mp3
# 7. Share your AI-generated comedy!
```

---

## API Key Setup

### ElevenLabs

1. Go to https://elevenlabs.io/
2. Sign up for free account (10,000 chars/month free)
3. Go to Profile → API Keys
4. Generate new key
5. Set environment variable:
   ```bash
   export ELEVENLABS_API_KEY="sk_xxxxx"
   ```

### OpenAI

1. Go to https://platform.openai.com/
2. Sign up and add payment method
3. Go to API Keys section
4. Create new secret key
5. Set environment variable:
   ```bash
   export OPENAI_API_KEY="sk-xxxxx"
   ```

---

## Performance Metrics

Our 8.5-minute comedy set:
- **Total characters:** ~5,000
- **ElevenLabs cost:** ~$0.17 (starter plan)
- **OpenAI cost:** ~$0.08
- **Google TTS cost:** FREE
- **Generation time:**
  - ElevenLabs: ~30-60 seconds
  - OpenAI: ~15-30 seconds
  - Google TTS: ~10-20 seconds

---

## Next Steps

1. **Generate your first version** with free gTTS
2. **Adjust timing** in the script
3. **Upgrade to premium TTS** for final quality
4. **Share the results!** We'd love to hear how it sounds

Remember: The script timing matters more than the TTS provider. Spend time perfecting the pauses and emphasis markers first, then upgrade to premium TTS for the final version.

Happy comedy generation! 🎤
