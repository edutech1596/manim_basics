# 🎙️ Manim with Voice Narration

Professional voice narration for Manim animations using **manim-voiceover**.

## 🎯 What's Different from `manim_basics`?

This project adds **synchronized voice narration** to animations:
- ✅ Automatic timing - animations sync perfectly with speech
- ✅ Multiple TTS backends (Google TTS, Edge TTS, Azure)
- ✅ Programmatic and scalable for many lessons
- ✅ High-quality, natural-sounding voices

## 📦 Installation

```bash
cd /Users/apple/manim_with_voice

# Install dependencies
pip install -r requirements.txt

# Verify ffmpeg is installed (required for audio)
ffmpeg -version
```

### Install ffmpeg (if needed):
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

## 🎬 Quick Start

### Render a single scene with voice:
```bash
python3 -m manim -pql 01_hello_manim_voice.py HelloManimVoice
```

### Render all voiced scenes:
```bash
chmod +x render_all.sh
./render_all.sh        # Low quality (fast)
./render_all.sh pqh    # High quality (slow)
```

## 🗣️ Available TTS Backends

### 1. **Google TTS (GTTS)** - Default, Simple
```python
configure_voiceover(self, backend="gtts", lang="en")
```
- ✅ Free, no API keys needed
- ✅ Works offline after first download
- ⚠️ Requires internet for first generation
- 🎭 Good quality, robotic tone

### 2. **Edge TTS** - Best Quality
```python
configure_voiceover(self, backend="edge", voice="en-US-AriaNeural")
```
- ✅ Excellent quality, natural voices
- ✅ Many voice options
- ✅ Free
- 🎭 Most realistic option

Popular voices:
- `en-US-AriaNeural` (female, friendly)
- `en-US-GuyNeural` (male, professional)
- `en-GB-SoniaNeural` (British female)
- `en-IN-NeerjaNeural` (Indian female)

### 3. **Azure TTS** - Premium
```python
configure_voiceover(self, backend="azure", voice="en-US-JennyNeural")
```
- Requires Azure account
- Set environment variables:
  ```bash
  export AZURE_SPEECH_KEY="your-key"
  export AZURE_SPEECH_REGION="eastus"
  ```

### 4. **Recorder** - Your Own Voice
```python
configure_voiceover(self, backend="record")
```
- Records your voice line-by-line
- Interactive prompts for each narration block

## 📝 How It Works

### Traditional Manim (without voice):
```python
class HelloManim(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        self.wait(1)
        self.play(FadeOut(circle))
```

### With Voice Narration:
```python
class HelloManimVoice(VoiceoverScene):
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle = Circle()
        
        # Narration block 1
        with self.voiceover(text="We will draw a circle") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
        
        # Narration block 2
        with self.voiceover(text="Now it fades away") as tracker:
            self.play(FadeOut(circle), run_time=tracker.duration)
```

**Key Points:**
- `VoiceoverScene` instead of `Scene`
- `with self.voiceover(text=...)` wraps each narrated action
- `tracker.duration` auto-syncs animation to speech length
- One narration block = one visual beat

## 📂 Project Structure

```
manim_with_voice/
├── requirements.txt              # Dependencies
├── voiceover_config.py          # TTS backend configuration
├── 01_hello_manim_voice.py      # First voiced lesson
├── render_all.sh                # Batch render script
├── README.md                    # This file
└── media/                       # Output (created on first render)
    └── videos/
        └── 01_hello_manim_voice/
            └── 480p15/
                ├── HelloManimVoice.mp4
                └── ...
```

## 🎯 Available Scenes

### Lesson 01 - Hello Manim with Voice
1. **HelloManimVoice** - Simple circle with narration
2. **ColorfulCircleVoice** - Colorful circle with detailed narration
3. **MultipleAnimationsVoice** - Three circles with synchronized voice
4. **ShapesWithVoice** - Educational narration for geometric shapes

## 🎨 Quality Options

| Flag | Resolution | Speed | Use Case |
|------|-----------|-------|----------|
| `-pql` | 480p | Fast | Preview/testing |
| `-pqm` | 720p | Medium | Review |
| `-pqh` | 1080p | Slow | Production |
| `-pqk` | 4K | Very Slow | Premium |

## 🔧 Troubleshooting

### No audio in output?
```bash
# Check ffmpeg
ffmpeg -version

# If missing, install it
brew install ffmpeg  # macOS
```

### Voice sounds robotic?
```python
# Switch from gtts to edge for better quality
configure_voiceover(self, backend="edge", voice="en-US-AriaNeural")
```

### Edge TTS not working?
```bash
# Reinstall edge-tts
pip install --upgrade edge-tts
```

### Audio too fast/slow?
```python
# Adjust rate (Edge TTS only)
configure_voiceover(self, backend="edge", 
                   voice="en-US-AriaNeural",
                   rate="-10%")  # slower
```

### List all Edge TTS voices:
```python
import asyncio, edge_tts

async def main():
    voices = await edge_tts.list_voices()
    for v in voices:
        print(f"{v['ShortName']}: {v['Gender']}, {v['Locale']}")

asyncio.run(main())
```

### Clear audio cache:
```bash
rm -rf media/voiceover_cache/
```

## 📖 Writing Good Narration

### ✅ Do:
- Keep sentences short and clear
- One sentence per visual action
- Match narration to what's happening on screen
- Use natural, conversational language

### ❌ Don't:
- Make sentences too long (>15 words)
- Describe things not visible yet
- Use technical jargon without explanation
- Rush multiple actions in one narration

### Example - Good:
```python
with self.voiceover(text="A red circle appears.") as tracker:
    self.play(Create(red_circle), run_time=tracker.duration)
```

### Example - Bad:
```python
with self.voiceover(text="Now we're going to create a red circle and then move it to the right side while simultaneously rotating it and changing its color to blue.") as tracker:
    # Too much happening in one narration!
```

## 🚀 Next Steps

1. **Try different voices** - Experiment with Edge TTS voices
2. **Add more lessons** - Create voiced versions of other lessons
3. **Customize timing** - Fine-tune narration for perfect sync
4. **Create playlists** - Organize videos by topic
5. **Export for YouTube** - Render in high quality with voice

## 🔗 Resources

- [manim-voiceover docs](https://voiceover.manim.community/)
- [Edge TTS voices](https://speech.microsoft.com/portal/voicegallery)
- [Manim documentation](https://docs.manim.community/)
- [GTTS documentation](https://gtts.readthedocs.io/)

## 📊 Comparison with `manim_basics`

| Feature | manim_basics | manim_with_voice |
|---------|-------------|------------------|
| Animations | ✅ | ✅ |
| Comments | ✅ Detailed | ✅ Detailed |
| Voice Narration | ❌ | ✅ Professional |
| Auto-timing | ❌ | ✅ Perfect sync |
| Multiple languages | ❌ | ✅ 50+ languages |
| Accessibility | ❌ | ✅ Audio descriptions |

---

**Happy animating with voice! 🎬🎙️**


