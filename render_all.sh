#!/usr/bin/env bash
set -euo pipefail

# Render all 54 voiced scenes from manim_basics (now with voice)
# Usage: ./render_all.sh [quality]
# Example: ./render_all.sh pqh (for high quality)

QUALITY=${1:-pql} # default preview quality low

echo "🎙️ Rendering all 54 voiced scenes with quality: $QUALITY"
echo ""

# Lesson 01 - Hello Manim (3 scenes)
echo "📹 Lesson 01: Hello Manim"
python3 -m manim -$QUALITY 01_hello_manim_voice.py HelloManimVoice
python3 -m manim -$QUALITY 01_hello_manim_voice.py ColorfulCircleVoice
python3 -m manim -$QUALITY 01_hello_manim_voice.py MultipleAnimationsVoice

# Lesson 02 - Basic Shapes (4 scenes)
echo "📹 Lesson 02: Basic Shapes"
python3 -m manim -$QUALITY 02_basic_shapes_voice.py ShapeGalleryVoice
python3 -m manim -$QUALITY 02_basic_shapes_voice.py MoreShapesVoice
python3 -m manim -$QUALITY 02_basic_shapes_voice.py ShapePropertiesVoice
python3 -m manim -$QUALITY 02_basic_shapes_voice.py LinesVoice

# Lesson 03 - Text Basics (4 scenes)
echo "📹 Lesson 03: Text Basics"
python3 -m manim -$QUALITY 03_text_basics_voice.py SimpleTextVoice
python3 -m manim -$QUALITY 03_text_basics_voice.py TextFormattingVoice
python3 -m manim -$QUALITY 03_text_basics_voice.py TextPositioningVoice
python3 -m manim -$QUALITY 03_text_basics_voice.py TextWithShapesVoice

# Lesson 04 - Colors (4 scenes)
echo "📹 Lesson 04: Colors"
python3 -m manim -$QUALITY 04_colors_voice.py ColorBasicsVoice
python3 -m manim -$QUALITY 04_colors_voice.py ColorShadesVoice
python3 -m manim -$QUALITY 04_colors_voice.py CustomColorsVoice
python3 -m manim -$QUALITY 04_colors_voice.py GradientColorsVoice

# Lesson 05 - Create Animations (4 scenes)
echo "📹 Lesson 05: Create Animations"
python3 -m manim -$QUALITY 05_create_animations_voice.py CreateMethodsVoice
python3 -m manim -$QUALITY 05_create_animations_voice.py MoreCreateAnimationsVoice
python3 -m manim -$QUALITY 05_create_animations_voice.py WriteAnimationVoice
python3 -m manim -$QUALITY 05_create_animations_voice.py UncreateAnimationsVoice

# Lesson 06 - Transform Animations (4 scenes)
echo "📹 Lesson 06: Transform Animations"
python3 -m manim -$QUALITY 06_transform_animations_voice.py BasicTransformVoice
python3 -m manim -$QUALITY 06_transform_animations_voice.py ReplacementTransformExampleVoice
python3 -m manim -$QUALITY 06_transform_animations_voice.py TextTransformVoice
python3 -m manim -$QUALITY 06_transform_animations_voice.py TransformMatchingShapesExampleVoice

# Lesson 07 - Movement (5 scenes)
echo "📹 Lesson 07: Movement"
python3 -m manim -$QUALITY 07_movement_voice.py ShiftMovementVoice
python3 -m manim -$QUALITY 07_movement_voice.py MoveToPositionVoice
python3 -m manim -$QUALITY 07_movement_voice.py ToEdgeMovementVoice
python3 -m manim -$QUALITY 07_movement_voice.py NextToPositionVoice
python3 -m manim -$QUALITY 07_movement_voice.py RotationMovementVoice

# Lesson 08 - Timing (5 scenes)
echo "📹 Lesson 08: Timing"
python3 -m manim -$QUALITY 08_timing_voice.py RunTimeVoice
python3 -m manim -$QUALITY 08_timing_voice.py WaitTimingVoice
python3 -m manim -$QUALITY 08_timing_voice.py SequentialTimingVoice
python3 -m manim -$QUALITY 08_timing_voice.py SimultaneousTimingVoice
python3 -m manim -$QUALITY 08_timing_voice.py RateFunctionVoice

# Lesson 09 - Positioning (5 scenes)
echo "📹 Lesson 09: Positioning"
python3 -m manim -$QUALITY 09_positioning_voice.py AlignmentBasicsVoice
python3 -m manim -$QUALITY 09_positioning_voice.py ArrangeInGridVoice
python3 -m manim -$QUALITY 09_positioning_voice.py ArrangeInRowVoice
python3 -m manim -$QUALITY 09_positioning_voice.py CenterAndShiftVoice
python3 -m manim -$QUALITY 09_positioning_voice.py GetCenterVoice

# Lesson 10 - Multiple Objects (5 scenes)
echo "📹 Lesson 10: Multiple Objects"
python3 -m manim -$QUALITY 10_multiple_objects_voice.py MultipleCirclesVoice
python3 -m manim -$QUALITY 10_multiple_objects_voice.py ListComprehensionVoice
python3 -m manim -$QUALITY 10_multiple_objects_voice.py AnimateSuccessionVoice
python3 -m manim -$QUALITY 10_multiple_objects_voice.py CopyingObjectsVoice
python3 -m manim -$QUALITY 10_multiple_objects_voice.py UpdaterExampleVoice

# Lesson 11 - Groups (5 scenes)
echo "📹 Lesson 11: Groups"
python3 -m manim -$QUALITY 11_groups_voice.py BasicGroupVoice
python3 -m manim -$QUALITY 11_groups_voice.py GroupOperationsVoice
python3 -m manim -$QUALITY 11_groups_voice.py AddToGroupVoice
python3 -m manim -$QUALITY 11_groups_voice.py NestedGroupsVoice
python3 -m manim -$QUALITY 11_groups_voice.py GroupWithTextVoice

# Lesson 12 - Equations (6 scenes)
echo "📹 Lesson 12: Equations"
python3 -m manim -$QUALITY 12_equations_voice.py SimpleEquationVoice
python3 -m manim -$QUALITY 12_equations_voice.py MultipleEquationsVoice
python3 -m manim -$QUALITY 12_equations_voice.py ColoredEquationVoice
python3 -m manim -$QUALITY 12_equations_voice.py TransformEquationVoice
python3 -m manim -$QUALITY 12_equations_voice.py EquationWithTextVoice
python3 -m manim -$QUALITY 12_equations_voice.py EquationArrayVoice

echo ""
echo "✅ All 54 voiced scenes rendered!"
echo "📂 Videos are in: media/videos/"
echo "🎙️ Audio cache is in: media/voiceovers/"