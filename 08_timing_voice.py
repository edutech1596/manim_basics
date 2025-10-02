"""
Lesson 8 with Voice: Timing and Speed Control

All 5 scenes about controlling animation timing, speed, and delays with voice.

To render:
    python3 -m manim -pql 08_timing_voice.py RunTimeVoice
"""

from manim import *
from manim_voiceover import VoiceoverScene
from voiceover_config import configure_voiceover


class RunTimeVoice(VoiceoverScene):
    """Controlling animation speed with run_time."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle1 = Circle(color=BLUE).shift(UP * 2)
        
        with self.voiceover(text="The top circle appears fast, in half a second.") as tracker:
            self.play(Create(circle1), run_time=0.5)
            self.wait(tracker.duration - 0.5)
        
        circle2 = Circle(color=GREEN)
        
        with self.voiceover(text="The middle circle appears at normal speed, one second.") as tracker:
            self.play(Create(circle2), run_time=1.0)
            self.wait(tracker.duration - 1.0)
        
        circle3 = Circle(color=RED).shift(DOWN * 2)
        
        with self.voiceover(text="The bottom circle appears slowly, taking three seconds.") as tracker:
            self.play(Create(circle3), run_time=min(3.0, tracker.duration))
            if tracker.duration > 3.0:
                self.wait(tracker.duration - 3.0)
        
        with self.voiceover(text="Run time controls the speed of animations.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing all circles.") as tracker:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=tracker.duration)


class WaitTimingVoice(VoiceoverScene):
    """Using wait to add pauses."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle = Circle(color=BLUE)
        
        with self.voiceover(text="We create a blue circle and pause to view it.") as tracker:
            self.play(Create(circle), run_time=tracker.duration * 0.4)
            self.wait(tracker.duration * 0.6)
        
        with self.voiceover(text="Now it changes to red.") as tracker:
            self.play(circle.animate.set_color(RED), run_time=tracker.duration)
        
        with self.voiceover(text="Then it moves to the right.") as tracker:
            self.play(circle.animate.shift(RIGHT * 2), run_time=tracker.duration)
        
        with self.voiceover(text="Wait gives viewers time to process what they see.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing the circle.") as tracker:
            self.play(FadeOut(circle), run_time=tracker.duration)


class SequentialTimingVoice(VoiceoverScene):
    """Animations happening one after another."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle1 = Circle(color=RED).shift(LEFT * 2)
        circle2 = Circle(color=GREEN)
        circle3 = Circle(color=BLUE).shift(RIGHT * 2)
        
        with self.voiceover(text="Sequential animations happen one after another. First the red circle.") as tracker:
            self.play(Create(circle1), run_time=tracker.duration)
        
        with self.voiceover(text="Then the green circle.") as tracker:
            self.play(Create(circle2), run_time=tracker.duration)
        
        with self.voiceover(text="Finally the blue circle.") as tracker:
            self.play(Create(circle3), run_time=tracker.duration)
        
        with self.voiceover(text="Now they move up one at a time. Red first.") as tracker:
            self.play(circle1.animate.shift(UP), run_time=tracker.duration)
        
        with self.voiceover(text="Then green.") as tracker:
            self.play(circle2.animate.shift(UP), run_time=tracker.duration)
        
        with self.voiceover(text="Finally blue.") as tracker:
            self.play(circle3.animate.shift(UP), run_time=tracker.duration)
        
        with self.voiceover(text="Sequential timing creates step-by-step narratives.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Clearing the scene.") as tracker:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=tracker.duration)


class SimultaneousTimingVoice(VoiceoverScene):
    """Animations happening at the same time."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle1 = Circle(color=RED).shift(LEFT * 2)
        circle2 = Circle(color=GREEN)
        circle3 = Circle(color=BLUE).shift(RIGHT * 2)
        
        with self.voiceover(text="Simultaneous animations happen all at once. All three circles appear together.") as tracker:
            self.play(
                Create(circle1),
                Create(circle2),
                Create(circle3),
                run_time=tracker.duration
            )
        
        with self.voiceover(text="Now they all move up at the same time.") as tracker:
            self.play(
                circle1.animate.shift(UP),
                circle2.animate.shift(UP),
                circle3.animate.shift(UP),
                run_time=tracker.duration
            )
        
        with self.voiceover(text="Simultaneous timing creates coordinated motion.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing everything together.") as tracker:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=tracker.duration)


class RateFunctionVoice(VoiceoverScene):
    """Using rate functions to control animation curves."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle1 = Circle(radius=0.5, color=BLUE).shift(UP * 2 + LEFT * 5)
        self.add(circle1)
        
        with self.voiceover(text="The top circle moves with linear speed, constant throughout.") as tracker:
            self.play(
                circle1.animate.shift(RIGHT * 10),
                rate_func=linear,
                run_time=min(2, tracker.duration)
            )
            if tracker.duration > 2:
                self.wait(tracker.duration - 2)
        
        circle2 = Circle(radius=0.5, color=GREEN).shift(LEFT * 5)
        self.add(circle2)
        
        with self.voiceover(text="The middle circle uses smooth rate function, slow at start and end, fast in middle.") as tracker:
            self.play(
                circle2.animate.shift(RIGHT * 10),
                rate_func=smooth,
                run_time=min(2, tracker.duration)
            )
            if tracker.duration > 2:
                self.wait(tracker.duration - 2)
        
        circle3 = Circle(radius=0.5, color=RED).shift(DOWN * 2 + LEFT * 5)
        self.add(circle3)
        
        with self.voiceover(text="The bottom circle rushes into the end, starting slow and speeding up.") as tracker:
            self.play(
                circle3.animate.shift(RIGHT * 10),
                rate_func=rush_into,
                run_time=min(2, tracker.duration)
            )
            if tracker.duration > 2:
                self.wait(tracker.duration - 2)
        
        with self.voiceover(text="Rate functions control how animations accelerate and decelerate.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Clearing the scene.") as tracker:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=tracker.duration)


