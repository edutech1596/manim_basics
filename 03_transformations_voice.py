"""
Lesson 3 with Voice: Shape Transformations with Narration

Learn about different types of transformations with voice explanations.

To render:
    python3 -m manim -pql 03_transformations_voice.py ShapeTransformVoice
"""

from manim import *
from manim_voiceover import VoiceoverScene
from voiceover_config import configure_voiceover


class ShapeTransformVoice(VoiceoverScene):
    """
    Transform shapes with synchronized narration.
    """
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        # Create shapes
        circle = Circle(color=BLUE)
        square = Square(color=RED)
        triangle = Triangle(color=GREEN)
        
        # Narration: Introduce circle
        with self.voiceover(text="We begin with a blue circle.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
        
        # Narration: Transform to square
        with self.voiceover(text="Watch as the circle transforms into a red square.") as tracker:
            self.play(Transform(circle, square), run_time=tracker.duration)
        
        # Narration: Transform to triangle
        with self.voiceover(text="Now the square becomes a green triangle.") as tracker:
            self.play(Transform(circle, triangle), run_time=tracker.duration)
        
        # Narration: Conclusion
        with self.voiceover(text="These are called shape transformations.") as tracker:
            self.wait(tracker.duration)
        
        # Narration: Cleanup
        with self.voiceover(text="Let's remove the shape.") as tracker:
            self.play(FadeOut(circle), run_time=tracker.duration)


class RotationVoice(VoiceoverScene):
    """
    Demonstrate rotation with voice narration.
    """
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        # Create a square
        square = Square(color=BLUE, fill_opacity=0.5)
        
        # Narration: Create square
        with self.voiceover(text="Here is a blue square.") as tracker:
            self.play(Create(square), run_time=tracker.duration)
        
        # Narration: Rotate 90 degrees
        with self.voiceover(text="Let's rotate it ninety degrees.") as tracker:
            self.play(Rotate(square, PI/2), run_time=tracker.duration)
        
        # Narration: Rotate 180 degrees
        with self.voiceover(text="Now rotate it one hundred and eighty degrees.") as tracker:
            self.play(Rotate(square, PI), run_time=tracker.duration)
        
        # Narration: Full rotation
        with self.voiceover(text="Finally, a complete three hundred sixty degree rotation.") as tracker:
            self.play(Rotate(square, 2*PI), run_time=tracker.duration)
        
        # Narration: Cleanup
        with self.voiceover(text="That demonstrates rotation animations.") as tracker:
            self.play(FadeOut(square), run_time=tracker.duration)


class ScalingVoice(VoiceoverScene):
    """
    Demonstrate scaling with voice narration.
    """
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        # Create a circle
        circle = Circle(radius=1, color=YELLOW, fill_opacity=0.7)
        
        # Narration: Create circle
        with self.voiceover(text="We start with a medium-sized yellow circle.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
        
        # Narration: Scale up
        with self.voiceover(text="Watch it grow to double its size.") as tracker:
            self.play(circle.animate.scale(2), run_time=tracker.duration)
        
        # Narration: Scale down
        with self.voiceover(text="Now it shrinks to half its original size.") as tracker:
            self.play(circle.animate.scale(0.25), run_time=tracker.duration)
        
        # Narration: Back to normal
        with self.voiceover(text="And back to normal size again.") as tracker:
            self.play(circle.animate.scale(2), run_time=tracker.duration)
        
        # Narration: Cleanup
        with self.voiceover(text="Scaling allows objects to grow or shrink smoothly.") as tracker:
            self.play(FadeOut(circle), run_time=tracker.duration)


