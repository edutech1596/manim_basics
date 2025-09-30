# Manim Basics - Learning Path

Welcome to your Manim learning journey! This repository contains examples starting from the absolute basics.

## Setup

1. **Install Manim:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify Installation:**
   ```bash
   manim --version
   ```

## Learning Path

### Level 1: Fundamentals
- `01_hello_manim.py` - Your first animation with a simple shape
- `02_basic_shapes.py` - Circles, squares, and basic geometric objects
- `03_text_basics.py` - Adding text to animations
- `04_colors.py` - Working with colors

### Level 2: Animations
- `05_create_animations.py` - Basic creation animations
- `06_transform_animations.py` - Transforming objects
- `07_movement.py` - Moving objects around
- `08_timing.py` - Controlling animation speed and timing

### Level 3: Intermediate
- `09_positioning.py` - Advanced positioning techniques
- `10_multiple_objects.py` - Working with multiple objects
- `11_groups.py` - Grouping objects together
- `12_equations.py` - Mathematical equations with LaTeX

## How to Render

**Low Quality (Fast Preview):**
```bash
manim -pql filename.py SceneName
```

**High Quality:**
```bash
manim -pqh filename.py SceneName
```

**4K Quality:**
```bash
manim -pqk filename.py SceneName
```

### Command Flags:
- `-p` : Play the video after rendering
- `-ql` : Low quality (480p)
- `-qm` : Medium quality (720p)
- `-qh` : High quality (1080p)
- `-qk` : 4K quality
- `-s` : Save only the last frame (for static images)

## Tips for Beginners

1. Start with low quality (-ql) for faster iteration
2. Each file contains detailed comments explaining the code
3. Try modifying values to see what changes
4. Run examples in order for best learning experience
5. Check the official docs: https://docs.manim.community/

## Project Structure

```
manim_basics/
├── README.md
├── requirements.txt
├── 01_hello_manim.py
├── 02_basic_shapes.py
├── ... (other lesson files)
└── media/ (created automatically when you render)
```

Happy animating! 🎬 