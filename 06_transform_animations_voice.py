"""
Lesson 6 with Voice: Transform Animations

All 4 scenes about transforming one object into another with voice.

To render:
    python3 -m manim -pql 06_transform_animations_voice.py BasicTransformVoice
"""

from manim import *
from manim_voiceover import VoiceoverScene
from voiceover_config import configure_voiceover


class BasicTransformVoice(VoiceoverScene):
    """Basic transformation from one shape to another."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle = Circle(color=BLUE)
        circle.set_fill(BLUE, opacity=0.5)
        
        with self.voiceover(text="We start with a blue circle.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
        
        square = Square(color=GREEN)
        square.set_fill(GREEN, opacity=0.5)
        
        with self.voiceover(text="Watch as it transforms into a green square.") as tracker:
            self.play(Transform(circle, square), run_time=tracker.duration)
        
        triangle = Triangle(color=RED)
        triangle.set_fill(RED, opacity=0.5)
        
        with self.voiceover(text="Now it becomes a red triangle.") as tracker:
            self.play(Transform(circle, triangle), run_time=tracker.duration)
        
        with self.voiceover(text="Transform morphs one shape into another smoothly.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing the shape.") as tracker:
            self.play(FadeOut(circle), run_time=tracker.duration)


class ReplacementTransformExampleVoice(VoiceoverScene):
    """ReplacementTransform actually replaces the object."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle = Circle(color=BLUE)
        circle.set_fill(BLUE, opacity=0.5)
        
        with self.voiceover(text="We begin with a blue circle.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
        
        square = Square(color=GREEN)
        square.set_fill(GREEN, opacity=0.5)
        
        with self.voiceover(text="ReplacementTransform actually swaps objects. The circle is replaced by a square.") as tracker:
            self.play(ReplacementTransform(circle, square), run_time=tracker.duration)
        
        triangle = Triangle(color=RED)
        triangle.set_fill(RED, opacity=0.5)
        
        with self.voiceover(text="Now the square is replaced by a triangle.") as tracker:
            self.play(ReplacementTransform(square, triangle), run_time=tracker.duration)
        
        with self.voiceover(text="Unlike Transform, each object is truly replaced.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing the triangle.") as tracker:
            self.play(FadeOut(triangle), run_time=tracker.duration)


class TextTransformVoice(VoiceoverScene):
    """Transforming text is very useful for explanations."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        text1 = Text("Hello")
        
        with self.voiceover(text="We write the word Hello.") as tracker:
            self.play(Write(text1), run_time=tracker.duration)
        
        text2 = Text("World")
        
        with self.voiceover(text="Now it transforms into World.") as tracker:
            self.play(Transform(text1, text2), run_time=tracker.duration)
        
        text3 = Text("Manim is awesome!")
        
        with self.voiceover(text="And finally it becomes a longer message: Manim is awesome!") as tracker:
            self.play(Transform(text1, text3), run_time=tracker.duration)
        
        with self.voiceover(text="Text transformations are great for storytelling.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Clearing the text.") as tracker:
            self.play(FadeOut(text1), run_time=tracker.duration)


class TransformMatchingShapesExampleVoice(VoiceoverScene):
    """TransformMatchingShapes for smooth transitions."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle = Circle(color=BLUE).shift(LEFT)
        square = Square(color=GREEN).shift(RIGHT)
        group1 = VGroup(circle, square)
        
        with self.voiceover(text="We have a group with a circle and a square.") as tracker:
            self.play(Create(group1), run_time=tracker.duration)
        
        triangle = Triangle(color=RED).shift(UP)
        star = Star(color=YELLOW).shift(DOWN)
        group2 = VGroup(triangle, star)
        
        with self.voiceover(text="TransformMatchingShapes intelligently morphs between groups, matching corresponding objects.") as tracker:
            self.play(TransformMatchingShapes(group1, group2), run_time=tracker.duration)
        
        with self.voiceover(text="This creates smooth transitions between complex arrangements.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing the shapes.") as tracker:
            self.play(FadeOut(group2), run_time=tracker.duration)


