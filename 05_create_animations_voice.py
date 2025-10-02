"""
Lesson 5 with Voice: Create Animations

All 4 scenes about different ways to create and introduce objects with voice.

To render:
    python3 -m manim -pql 05_create_animations_voice.py CreateMethodsVoice
"""

from manim import *
from manim_voiceover import VoiceoverScene
from voiceover_config import configure_voiceover


class CreateMethodsVoice(VoiceoverScene):
    """Different creation animation styles."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle = Circle(color=BLUE)
        circle.shift(LEFT * 3)
        
        with self.voiceover(text="The Create animation draws the object's border from start to finish.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
        
        square = Square(color=GREEN)
        square.shift(ORIGIN)
        
        with self.voiceover(text="FadeIn gradually increases opacity, making the object appear.") as tracker:
            self.play(FadeIn(square), run_time=tracker.duration)
        
        triangle = Triangle(color=RED)
        triangle.shift(RIGHT * 3)
        
        with self.voiceover(text="GrowFromCenter makes the object expand from a tiny point.") as tracker:
            self.play(GrowFromCenter(triangle), run_time=tracker.duration)
        
        with self.voiceover(text="Each method creates a different visual effect.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing all objects.") as tracker:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=tracker.duration)


class MoreCreateAnimationsVoice(VoiceoverScene):
    """More creative ways to introduce objects."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle = Circle(color=BLUE)
        circle.set_fill(BLUE, opacity=0.5)
        circle.shift(UP * 2)
        
        with self.voiceover(text="DrawBorderThenFill first draws the outline, then fills it in.") as tracker:
            self.play(DrawBorderThenFill(circle), run_time=tracker.duration)
        
        square = Square(color=GREEN)
        square.set_fill(GREEN, opacity=0.5)
        
        with self.voiceover(text="SpinInFromNothing spins and grows the object simultaneously.") as tracker:
            self.play(SpinInFromNothing(square), run_time=tracker.duration)
        
        rect = Rectangle(width=3, height=1, color=YELLOW)
        rect.set_fill(YELLOW, opacity=0.5)
        rect.shift(DOWN * 2)
        
        with self.voiceover(text="GrowFromEdge expands the object from a specific edge.") as tracker:
            self.play(GrowFromEdge(rect, LEFT), run_time=tracker.duration)
        
        with self.voiceover(text="These animations add variety to your presentations.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Clearing the scene.") as tracker:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=tracker.duration)


class WriteAnimationVoice(VoiceoverScene):
    """Write animation is special for text."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        text = Text("This text is being written!")
        
        with self.voiceover(text="The Write animation writes text letter by letter, like typing.") as tracker:
            self.play(Write(text), run_time=tracker.duration)
        
        with self.voiceover(text="It creates a natural writing effect.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing the text.") as tracker:
            self.play(FadeOut(text), run_time=tracker.duration)
        
        circle = Circle(color=BLUE)
        
        with self.voiceover(text="Write also works on shapes, tracing their outline.") as tracker:
            self.play(Write(circle), run_time=tracker.duration)
        
        with self.voiceover(text="It's a versatile animation.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing the circle.") as tracker:
            self.play(FadeOut(circle), run_time=tracker.duration)


class UncreateAnimationsVoice(VoiceoverScene):
    """Animations for removing objects."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle = Circle(color=BLUE).shift(LEFT * 2)
        square = Square(color=GREEN)
        triangle = Triangle(color=RED).shift(RIGHT * 2)
        
        with self.voiceover(text="Let's create three shapes to demonstrate removal animations.") as tracker:
            self.play(Create(circle), Create(square), Create(triangle), run_time=tracker.duration)
        
        with self.voiceover(text="Uncreate is the reverse of Create, it un-draws the object.") as tracker:
            self.play(Uncreate(circle), run_time=tracker.duration)
        
        with self.voiceover(text="FadeOut gradually makes the object transparent.") as tracker:
            self.play(FadeOut(square), run_time=tracker.duration)
        
        with self.voiceover(text="ShrinkToCenter shrinks the object to a point, opposite of GrowFromCenter.") as tracker:
            self.play(ShrinkToCenter(triangle), run_time=tracker.duration)


