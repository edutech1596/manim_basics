#!/bin/bash

# Script to render all Manim scenes
echo "🎬 Starting to render all Manim scenes..."
echo "Output folder: rendered_videos/"
echo ""

# Lesson 01: Hello Manim
echo "📹 Rendering Lesson 01..."
python3 -m manim -ql 01_hello_manim.py HelloManim
python3 -m manim -ql 01_hello_manim.py ColorfulCircle
python3 -m manim -ql 01_hello_manim.py MultipleAnimations

# Lesson 02: Basic Shapes
echo "📹 Rendering Lesson 02..."
python3 -m manim -ql 02_basic_shapes.py ShapeGallery
python3 -m manim -ql 02_basic_shapes.py MoreShapes
python3 -m manim -ql 02_basic_shapes.py ShapeProperties
python3 -m manim -ql 02_basic_shapes.py Lines

# Lesson 03: Text Basics
echo "📹 Rendering Lesson 03..."
python3 -m manim -ql 03_text_basics.py SimpleText
python3 -m manim -ql 03_text_basics.py TextFormatting
python3 -m manim -ql 03_text_basics.py TextPositioning
python3 -m manim -ql 03_text_basics.py TextWithShapes

# Lesson 04: Colors
echo "📹 Rendering Lesson 04..."
python3 -m manim -ql 04_colors.py ColorBasics
python3 -m manim -ql 04_colors.py ColorShades
python3 -m manim -ql 04_colors.py CustomColors
python3 -m manim -ql 04_colors.py GradientColors

# Lesson 05: Create Animations
echo "📹 Rendering Lesson 05..."
python3 -m manim -ql 05_create_animations.py CreateMethods
python3 -m manim -ql 05_create_animations.py MoreCreateAnimations
python3 -m manim -ql 05_create_animations.py WriteAnimation
python3 -m manim -ql 05_create_animations.py UncreateAnimations

# Lesson 06: Transform Animations
echo "📹 Rendering Lesson 06..."
python3 -m manim -ql 06_transform_animations.py BasicTransform
python3 -m manim -ql 06_transform_animations.py ReplacementTransform
python3 -m manim -ql 06_transform_animations.py TextTransform
python3 -m manim -ql 06_transform_animations.py TransformMatchingShapes

# Lesson 07: Movement
echo "📹 Rendering Lesson 07..."
python3 -m manim -ql 07_movement.py ShiftMovement
python3 -m manim -ql 07_movement.py MoveToPosition
python3 -m manim -ql 07_movement.py ToEdgeMovement
python3 -m manim -ql 07_movement.py NextToPosition
python3 -m manim -ql 07_movement.py RotationMovement

# Lesson 08: Timing
echo "📹 Rendering Lesson 08..."
python3 -m manim -ql 08_timing.py RunTime
python3 -m manim -ql 08_timing.py WaitTiming
python3 -m manim -ql 08_timing.py SequentialTiming
python3 -m manim -ql 08_timing.py SimultaneousTiming
python3 -m manim -ql 08_timing.py RateFunction

# Lesson 09: Positioning
echo "📹 Rendering Lesson 09..."
python3 -m manim -ql 09_positioning.py AlignmentBasics
python3 -m manim -ql 09_positioning.py ArrangeInGrid
python3 -m manim -ql 09_positioning.py ArrangeInRow
python3 -m manim -ql 09_positioning.py CenterAndShift
python3 -m manim -ql 09_positioning.py GetCenter

# Lesson 10: Multiple Objects
echo "📹 Rendering Lesson 10..."
python3 -m manim -ql 10_multiple_objects.py MultipleCircles
python3 -m manim -ql 10_multiple_objects.py ListComprehension
python3 -m manim -ql 10_multiple_objects.py AnimateSuccession
python3 -m manim -ql 10_multiple_objects.py CopyingObjects
python3 -m manim -ql 10_multiple_objects.py UpdaterPattern

# Lesson 11: Groups
echo "📹 Rendering Lesson 11..."
python3 -m manim -ql 11_groups.py BasicGroup
python3 -m manim -ql 11_groups.py GroupOperations
python3 -m manim -ql 11_groups.py AddToGroup
python3 -m manim -ql 11_groups.py NestedGroups
python3 -m manim -ql 11_groups.py GroupWithText

# Lesson 12: Equations
echo "📹 Rendering Lesson 12..."
python3 -m manim -ql 12_equations.py SimpleEquation
python3 -m manim -ql 12_equations.py MultipleEquations
python3 -m manim -ql 12_equations.py ColoredEquation
python3 -m manim -ql 12_equations.py TransformEquation
python3 -m manim -ql 12_equations.py EquationWithText
python3 -m manim -ql 12_equations.py EquationArray

# Move all videos to rendered_videos folder
echo ""
echo "📦 Moving all videos to rendered_videos folder..."
cp -r media/videos/* rendered_videos/ 2>/dev/null || true

echo ""
echo "✅ All done! Videos saved in: rendered_videos/"
echo "📊 Total scenes rendered: 54" 