# 🧪 Setup Checklist for Manim with Voice

Use this checklist to ensure everything is properly configured.

## ✅ Installation Checklist

### 1. Check Python Version
```bash
python3 --version
# Should be Python 3.8 or higher
```
- [ ] Python 3.8+ installed

### 2. Check ffmpeg
```bash
ffmpeg -version
```
- [ ] ffmpeg installed and working
- [ ] Audio codecs available (aac, mp3)

**If ffmpeg is missing:**
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html and add to PATH
```

### 3. Install Python Dependencies
```bash
cd /Users/apple/manim_with_voice
pip3 install -r requirements.txt
```
- [ ] manim installed
- [ ] manim-voiceover installed
- [ ] edge-tts installed
- [ ] gTTS installed
- [ ] pydub installed

**Verify installation:**
```bash
python3 -c "import manim; print(manim.__version__)"
python3 -c "import manim_voiceover; print('Voiceover OK')"
python3 -c "import edge_tts; print('Edge TTS OK')"
python3 -c "from gtts import gTTS; print('GTTS OK')"
```

- [ ] All packages import successfully

### 4. Test Render (No Voice)
```bash
cd /Users/apple/manim_with_voice
python3 -m manim --version
```
- [ ] Manim runs without errors

### 5. Test Voice Render
```bash
# Test with Google TTS (requires internet)
python3 -m manim -pql 01_hello_manim_voice.py HelloManimVoice
```
- [ ] Scene renders successfully
- [ ] Audio is present in output video
- [ ] Audio syncs with animation
- [ ] Video saved in `media/videos/`

### 6. Make Scripts Executable
```bash
chmod +x render_all.sh
```
- [ ] render_all.sh is executable

### 7. Test Batch Rendering
```bash
./render_all.sh
```
- [ ] All 4 scenes from lesson 01 render
- [ ] All videos have audio
- [ ] No errors in terminal

## 🔧 Troubleshooting Tests

### Test 1: Basic TTS (Google)
```python
# test_gtts.py
from gtts import gTTS
import os

tts = gTTS("Hello world", lang="en")
tts.save("test_gtts.mp3")
print("✅ GTTS works! Check test_gtts.mp3")
os.system("ffmpeg -i test_gtts.mp3 2>&1 | grep Duration")
```
- [ ] MP3 file created
- [ ] ffmpeg can read the file

### Test 2: Edge TTS
```python
# test_edge.py
import asyncio
import edge_tts

async def test():
    tts = edge_tts.Communicate("Hello from Edge TTS", "en-US-AriaNeural")
    await tts.save("test_edge.mp3")
    print("✅ Edge TTS works! Check test_edge.mp3")

asyncio.run(test())
```
- [ ] MP3 file created with better quality

### Test 3: List Available Edge Voices
```python
# list_voices.py
import asyncio
import edge_tts

async def main():
    voices = await edge_tts.list_voices()
    en_voices = [v for v in voices if v['Locale'].startswith('en')]
    print(f"Found {len(en_voices)} English voices:\n")
    for v in en_voices[:10]:
        print(f"  {v['ShortName']}: {v['Gender']}")

asyncio.run(main())
```
- [ ] List of voices displays

### Test 4: Voiceover Cache
```bash
# Check if cache is created
ls -la media/voiceover_cache/ 2>/dev/null || echo "Cache will be created on first render"
```
- [ ] Cache directory exists after first render
- [ ] Audio files are cached (.mp3 files)

### Test 5: Audio in Video
```bash
# Check if rendered video has audio
ffmpeg -i media/videos/01_hello_manim_voice/480p15/HelloManimVoice.mp4 2>&1 | grep Audio
```
Expected output: `Stream #0:1: Audio: aac ...`
- [ ] Audio stream present in video

## 🎯 Quick Diagnostics

Run all checks at once:
```bash
#!/bin/bash
echo "🔍 Running diagnostics..."
echo ""

echo "1. Python version:"
python3 --version
echo ""

echo "2. ffmpeg version:"
ffmpeg -version | head -1
echo ""

echo "3. Manim version:"
python3 -c "import manim; print(f'Manim {manim.__version__}')" 2>&1
echo ""

echo "4. Manim-voiceover:"
python3 -c "import manim_voiceover; print('✅ Installed')" 2>&1
echo ""

echo "5. Edge TTS:"
python3 -c "import edge_tts; print('✅ Installed')" 2>&1
echo ""

echo "6. GTTS:"
python3 -c "from gtts import gTTS; print('✅ Installed')" 2>&1
echo ""

echo "7. pydub:"
python3 -c "import pydub; print('✅ Installed')" 2>&1
echo ""

echo "✅ Diagnostics complete!"
```

Save as `check_setup.sh`, make executable, and run:
```bash
chmod +x check_setup.sh
./check_setup.sh
```

## 📋 Expected Output Structure

After rendering, you should have:
```
manim_with_voice/
├── media/
│   ├── videos/
│   │   └── 01_hello_manim_voice/
│   │       └── 480p15/
│   │           ├── HelloManimVoice.mp4           ✅ With audio
│   │           ├── ColorfulCircleVoice.mp4       ✅ With audio
│   │           ├── MultipleAnimationsVoice.mp4   ✅ With audio
│   │           └── ShapesWithVoice.mp4           ✅ With audio
│   └── voiceover_cache/
│       └── (cached audio files)
```

## 🐛 Common Issues & Solutions

### Issue: "ModuleNotFoundError: No module named 'manim_voiceover'"
**Solution:**
```bash
pip3 install manim-voiceover
```

### Issue: "No audio in rendered video"
**Solution:**
1. Check ffmpeg: `ffmpeg -version`
2. Check if audio file was generated in cache
3. Try re-rendering with `-v DEBUG` flag:
   ```bash
   python3 -m manim -v DEBUG -pql 01_hello_manim_voice.py HelloManimVoice
   ```

### Issue: "Edge TTS voice not working"
**Solution:**
1. Check internet connection
2. Try a different voice
3. Fall back to GTTS:
   ```python
   configure_voiceover(self, backend="gtts", lang="en")
   ```

### Issue: "Audio too fast/slow"
**Solution for Edge TTS:**
```python
configure_voiceover(self, backend="edge", 
                   voice="en-US-AriaNeural",
                   rate="-10%")  # Slower
```

### Issue: "Permission denied: ./render_all.sh"
**Solution:**
```bash
chmod +x render_all.sh
```

### Issue: "Cache taking too much space"
**Solution:**
```bash
# Clear cache (will regenerate on next render)
rm -rf media/voiceover_cache/
```

## ✅ Final Checklist

Before starting your voiced lessons, ensure:

- [ ] Python 3.8+ installed
- [ ] ffmpeg installed and in PATH
- [ ] All Python packages installed
- [ ] Test render completes successfully
- [ ] Output video has audio
- [ ] Audio syncs with animation
- [ ] Scripts are executable
- [ ] You can choose between GTTS and Edge TTS

## 🚀 You're Ready!

If all checks pass, you're ready to create amazing narrated animations!

**Next steps:**
1. Explore different voices (see README.md)
2. Create your own voiced lessons
3. Experiment with timing and narration
4. Render in high quality for production

---

**Need help?** Check README.md for detailed documentation.


