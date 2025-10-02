# 🚀 Quick Start Guide - Manim with Voice

Get started with voiced Manim animations in 5 minutes!

---

## 📋 Prerequisites Check

```bash
# 1. Check Python (need 3.8+)
python3 --version

# 2. Check ffmpeg (required for audio)
ffmpeg -version

# 3. Navigate to project
cd /Users/apple/manim_with_voice
```

✅ All installed? Great! Let's render!

---

## 🎬 Render Your First Voiced Animation

### Method 1: Single Scene (Recommended for first try)
```bash
cd /Users/apple/manim_with_voice

# Render with voice narration
python3 -m manim -pql 01_hello_manim_voice.py HelloManimVoice
```

**What happens:**
1. ⏳ Generates voice audio using Google TTS
2. 📦 Caches audio for reuse
3. 🎬 Creates animation
4. 🎙️ Combines video + audio
5. ✅ Opens video automatically!

**Output:** `/Users/apple/manim_with_voice/media/videos/01_hello_manim_voice/480p15/HelloManimVoice.mp4`

---

## 🎭 Try Different Scenes

```bash
# Scene 1: Simple circle (3 voice lines)
python3 -m manim -pql 01_hello_manim_voice.py HelloManimVoice

# Scene 2: Colorful circle (better narration)
python3 -m manim -pql 01_hello_manim_voice.py ColorfulCircleVoice

# Scene 3: Multiple circles (synchronized)
python3 -m manim -pql 01_hello_manim_voice.py MultipleAnimationsVoice

# Scene 4: Educational shapes
python3 -m manim -pql 01_hello_manim_voice.py ShapesWithVoice
```

---

## 🎨 Render All Scenes at Once

```bash
# Make script executable (first time only)
chmod +x render_all.sh

# Render all scenes
./render_all.sh

# Or for high quality (slower)
./render_all.sh pqh
```

**This renders 10 scenes:**
- 4 from lesson 01 (basics)
- 3 from lesson 02 (equations)
- 3 from lesson 03 (transformations)

---

## 🎙️ Change Voice Quality

### Option 1: Edit the Python file

Open `01_hello_manim_voice.py` and change line in `construct()`:

```python
# Simple voice (default)
configure_voiceover(self, backend="gtts", lang="en")

# Better quality voice ⭐ RECOMMENDED
configure_voiceover(self, backend="edge", voice="en-US-AriaNeural")

# Male voice
configure_voiceover(self, backend="edge", voice="en-US-GuyNeural")

# British accent
configure_voiceover(self, backend="edge", voice="en-GB-SoniaNeural")
```

### Option 2: Create a new scene file

Copy `01_hello_manim_voice.py` and experiment!

---

## 📊 Quality Settings

```bash
# Low quality (480p, FAST) - for testing
python3 -m manim -pql FILE.py SCENE

# Medium quality (720p) - balanced
python3 -m manim -pqm FILE.py SCENE

# High quality (1080p) - production
python3 -m manim -pqh FILE.py SCENE

# 4K quality (slow!) - premium
python3 -m manim -pqk FILE.py SCENE
```

**Tip:** Always start with `-pql` for testing!

---

## 🔍 Verify Audio is Working

```bash
# Check video has audio stream
ffmpeg -i media/videos/01_hello_manim_voice/480p15/HelloManimVoice.mp4 2>&1 | grep Audio

# Expected output:
# Stream #0:1[0x2](und): Audio: aac ...
```

If you see audio stream ✅, voice is working!

---

## 📂 Where Are My Videos?

```bash
# List all rendered videos
find media/videos -name "*.mp4" -type f

# View most recent video
ls -lt media/videos/*/480p15/*.mp4 | head -1
```

**Default location pattern:**
```
media/videos/<lesson_file>/<quality>/<SceneName>.mp4
```

**Example:**
```
media/videos/01_hello_manim_voice/480p15/HelloManimVoice.mp4
```

---

## 🎯 Create Your Own Voiced Scene

### Step 1: Create a new file

```bash
nano my_voiced_scene.py
```

### Step 2: Copy this template

```python
from manim import *
from manim_voiceover import VoiceoverScene
from voiceover_config import configure_voiceover

class MyFirstVoice(VoiceoverScene):
    def construct(self):
        # Setup voice
        configure_voiceover(self, backend="gtts", lang="en")
        
        # Create object
        circle = Circle(color=BLUE)
        
        # Add narration
        with self.voiceover(text="This is my first voiced animation!") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
        
        with self.voiceover(text="Goodbye!") as tracker:
            self.play(FadeOut(circle), run_time=tracker.duration)
```

### Step 3: Render it!

```bash
python3 -m manim -pql my_voiced_scene.py MyFirstVoice
```

---

## 🛠️ Troubleshooting

### Problem: No audio in video

**Solution:**
```bash
# Check ffmpeg installed
ffmpeg -version

# If missing on macOS
brew install ffmpeg
```

### Problem: Voice sounds robotic

**Solution:** Use Edge TTS instead of GTTS
```python
configure_voiceover(self, backend="edge", voice="en-US-AriaNeural")
```

### Problem: Rendering is slow

**Solution:** Use low quality for testing
```bash
python3 -m manim -pql FILE.py SCENE  # Fast
```

### Problem: "Module not found" error

**Solution:**
```bash
cd /Users/apple/manim_with_voice
pip3 install -r requirements.txt
```

### Problem: Cache taking space

**Solution:** Clear cache (will regenerate)
```bash
rm -rf media/voiceovers/
```

---

## 🎓 Learning Path

### Beginner (Day 1)
1. ✅ Render `HelloManimVoice`
2. ✅ Watch the video with audio
3. ✅ Read the code comments
4. ✅ Try changing narration text
5. ✅ Re-render and compare

### Intermediate (Day 2-3)
1. ✅ Render all 10 scenes
2. ✅ Try Edge TTS for better quality
3. ✅ Create your own voiced scene
4. ✅ Experiment with timing
5. ✅ Add your own animations

### Advanced (Day 4+)
1. ✅ Create multi-scene lessons
2. ✅ Add background music
3. ✅ Create subtitle-optimized narration
4. ✅ Try multiple languages
5. ✅ Build a course playlist

---

## 📚 Examples

### Example 1: Math Lesson
```python
class PythagoreanVoice(VoiceoverScene):
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        equation = MathTex("a^2 + b^2 = c^2")
        
        with self.voiceover(text="The Pythagorean theorem") as tracker:
            self.play(Write(equation), run_time=tracker.duration)
```

### Example 2: Multi-step Animation
```python
class StepsVoice(VoiceoverScene):
    def construct(self):
        configure_voiceover(self, backend="edge", voice="en-US-AriaNeural")
        
        circle = Circle()
        square = Square()
        
        with self.voiceover(text="First, a circle appears") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
        
        with self.voiceover(text="Then it becomes a square") as tracker:
            self.play(Transform(circle, square), run_time=tracker.duration)
        
        with self.voiceover(text="Finally, it disappears") as tracker:
            self.play(FadeOut(circle), run_time=tracker.duration)
```

---

## 🚀 Next Steps

1. **Render your first scene** (5 min)
2. **Watch it** - verify audio works
3. **Read the code** - understand the pattern
4. **Modify narration** - make it yours
5. **Create new scene** - build something unique!

---

## 📖 More Resources

- **README.md** - Complete documentation
- **SETUP_CHECKLIST.md** - Verify installation
- **PROJECT_SUMMARY.md** - Project overview
- **Example scenes** - 3 lesson files with 10 scenes

---

## ✨ Pro Tips

1. **Always use low quality for testing** (`-pql`)
2. **Keep narration short** (one sentence per action)
3. **Use `tracker.duration`** for perfect sync
4. **Edge TTS sounds better** than GTTS
5. **Cache saves time** on re-renders
6. **Subtitles are free** (.srt auto-generated)
7. **Start simple** and add complexity gradually

---

## 🎊 Ready to Start!

```bash
cd /Users/apple/manim_with_voice
python3 -m manim -pql 01_hello_manim_voice.py HelloManimVoice
```

**Your first voiced animation awaits! 🎙️✨**


