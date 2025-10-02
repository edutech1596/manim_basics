"""
Lesson 2 with Voice: Basic Shapes

All 4 scenes with voice narration explaining different geometric shapes.

To render:
    python3 -m manim -pql 02_basic_shapes_voice.py ShapeGalleryVoice
"""

from manim import *
from manim_voiceover import VoiceoverScene
from voiceover_config import configure_voiceover


class ShapeGalleryVoice(VoiceoverScene):
    """Display various basic shapes with narration."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle = Circle(radius=0.5, color=RED)
        square = Square(side_length=1, color=BLUE)
        triangle = Triangle(color=GREEN)
        
        circle.shift(LEFT * 3)
        square.shift(ORIGIN)
        triangle.shift(RIGHT * 3)
        
        circle.set_fill(RED, opacity=0.5)
        square.set_fill(BLUE, opacity=0.5)
        triangle.set_fill(GREEN, opacity=0.5)
        
        with self.voiceover(text="Here are three basic shapes: a red circle, a blue square, and a green triangle.") as tracker:
            self.play(
                Create(circle),
                Create(square),
                Create(triangle),
                run_time=tracker.duration
            )
        
        with self.voiceover(text="Each shape has its own color and is semi-transparent.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Now let's remove them all.") as tracker:
            self.play(
                FadeOut(circle),
                FadeOut(square),
                FadeOut(triangle),
                run_time=tracker.duration
            )


class MoreShapesVoice(VoiceoverScene):
    """More shapes: rectangles, ellipses, and polygons."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        rectangle = Rectangle(width=4, height=2, color=YELLOW)
        rectangle.shift(UP * 2)
        ellipse = Ellipse(width=3, height=1.5, color=PURPLE)
        hexagon = RegularPolygon(n=6, color=ORANGE)
        hexagon.shift(DOWN * 2)
        
        rectangle.set_fill(YELLOW, opacity=0.3)
        ellipse.set_fill(PURPLE, opacity=0.3)
        hexagon.set_fill(ORANGE, opacity=0.3)
        
        with self.voiceover(text="Let's explore more shapes. First, a yellow rectangle at the top.") as tracker:
            self.play(Create(rectangle), run_time=tracker.duration)
        
        with self.voiceover(text="Next, a purple ellipse in the middle.") as tracker:
            self.play(Create(ellipse), run_time=tracker.duration)
        
        with self.voiceover(text="Finally, an orange hexagon at the bottom.") as tracker:
            self.play(Create(hexagon), run_time=tracker.duration)
        
        with self.voiceover(text="These are slightly more complex shapes than basic circles and squares.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Let's clear the screen.") as tracker:
            self.play(
                FadeOut(rectangle),
                FadeOut(ellipse),
                FadeOut(hexagon),
                run_time=tracker.duration
            )


class ShapePropertiesVoice(VoiceoverScene):
    """Exploring shape properties: stroke, fill, and size."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle1 = Circle(radius=1, color=BLUE, stroke_width=8)
        circle1.shift(LEFT * 3)
        
        circle2 = Circle(radius=1, color=GREEN, stroke_width=2)
        circle2.set_fill(GREEN, opacity=0.7)
        circle2.shift(ORIGIN)
        
        circle3 = Circle(radius=1, stroke_width=0)
        circle3.set_fill(RED, opacity=1)
        circle3.shift(RIGHT * 3)
        
        with self.voiceover(text="These three circles demonstrate different stroke and fill properties.") as tracker:
            self.play(
                Create(circle1),
                Create(circle2),
                Create(circle3),
                run_time=tracker.duration
            )
        
        with self.voiceover(text="The left has a thick blue outline. The middle has a thin outline with fill. The right has no outline, only fill.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Let's remove them.") as tracker:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=tracker.duration)


class LinesVoice(VoiceoverScene):
    """Working with lines, arrows, and paths."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        line = Line(start=LEFT * 2, end=RIGHT * 2, color=WHITE)
        arrow = Arrow(start=LEFT * 2 + DOWN, end=RIGHT * 2 + DOWN, color=YELLOW)
        double_arrow = DoubleArrow(
            start=LEFT * 2 + DOWN * 2,
            end=RIGHT * 2 + DOWN * 2,
            color=GREEN
        )
        
        with self.voiceover(text="First, a simple white line.") as tracker:
            self.play(Create(line), run_time=tracker.duration)
        
        with self.voiceover(text="Next, a yellow arrow pointing to the right.") as tracker:
            self.play(Create(arrow), run_time=tracker.duration)
        
        with self.voiceover(text="Finally, a green double-headed arrow.") as tracker:
            self.play(Create(double_arrow), run_time=tracker.duration)
        
        with self.voiceover(text="Lines and arrows are useful for connecting objects and showing directions.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Clearing the scene.") as tracker:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=tracker.duration)


