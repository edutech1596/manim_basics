"""
Lesson 1 with Voice: Hello Manim - Your First Narrated Animation

All 3 scenes from the original lesson, now with professional voice narration.

To render:
    python3 -m manim -pql 01_hello_manim_voice.py HelloManimVoice
"""

from manim import *
from manim_voiceover import VoiceoverScene
from voiceover_config import configure_voiceover


class HelloManimVoice(VoiceoverScene):
    """Your first Manim scene with voice narration!"""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle = Circle()
        
        with self.voiceover(text="Welcome to Manim! We create a simple circle.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
        
        with self.voiceover(text="We pause for a moment to observe it.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Now the circle fades away.") as tracker:
            self.play(FadeOut(circle), run_time=tracker.duration)
        
        with self.voiceover(text="This was your first Manim animation!") as tracker:
            self.wait(tracker.duration)


class ColorfulCircleVoice(VoiceoverScene):
    """Colorful circle with detailed narration."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle = Circle(radius=2, color=BLUE)
        circle.set_fill(BLUE, opacity=0.5)
        
        with self.voiceover(text="Let's create a larger blue circle with a semi-transparent fill.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
        
        with self.voiceover(text="Notice the circle has both an outline and a filled interior.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Now we'll make it disappear.") as tracker:
            self.play(FadeOut(circle), run_time=tracker.duration)


class MultipleAnimationsVoice(VoiceoverScene):
    """Multiple circles with synchronized narration."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle1 = Circle(radius=1, color=RED).shift(LEFT * 2)
        circle2 = Circle(radius=1, color=GREEN)
        circle3 = Circle(radius=1, color=BLUE).shift(RIGHT * 2)
        
        circle1.set_fill(RED, opacity=0.5)
        circle2.set_fill(GREEN, opacity=0.5)
        circle3.set_fill(BLUE, opacity=0.5)
        
        with self.voiceover(text="Watch as three circles appear: red on the left, green in center, and blue on the right.") as tracker:
            self.play(
                Create(circle1),
                Create(circle2),
                Create(circle3),
                run_time=tracker.duration
            )
        
        with self.voiceover(text="All three circles stay visible for a moment.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Now they fade out one by one: red, green, then blue.") as tracker:
            total = tracker.duration
            self.play(FadeOut(circle1), run_time=total * 0.34)
            self.play(FadeOut(circle2), run_time=total * 0.33)
            self.play(FadeOut(circle3), run_time=total * 0.33)