"""
Lesson 10 with Voice: Working with Multiple Objects

All 5 scenes about managing and animating many objects together with voice.

To render:
    python3 -m manim -pql 10_multiple_objects_voice.py MultipleCirclesVoice
"""

from manim import *
from manim_voiceover import VoiceoverScene
from voiceover_config import configure_voiceover


class MultipleCirclesVoice(VoiceoverScene):
    """Creating and animating multiple objects."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
        circles = []
        
        for i, color in enumerate(colors):
            circle = Circle(radius=0.5, color=color)
            circle.set_fill(color, opacity=0.5)
            circle.shift(LEFT * 3 + RIGHT * i * 1.2)
            circles.append(circle)
        
        with self.voiceover(text="When working with many objects, we use loops to create them efficiently. Here are six colored circles.") as tracker:
            self.play(*[Create(c) for c in circles], run_time=tracker.duration)
        
        with self.voiceover(text="They appear all at once using list comprehension.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing all circles.") as tracker:
            self.play(*[FadeOut(c) for c in circles], run_time=tracker.duration)


class ListComprehensionVoice(VoiceoverScene):
    """Using list comprehension to create multiple objects."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        squares = [
            Square(side_length=0.5, color=BLUE).shift(UP * 2 + LEFT * 4.5 + RIGHT * i)
            for i in range(10)
        ]
        
        with self.voiceover(text="List comprehension creates multiple objects in one line of code. Watch ten squares appear sequentially.") as tracker:
            total_time = tracker.duration
            individual_time = total_time / len(squares)
            for square in squares:
                self.play(Create(square), run_time=individual_time * 0.8)
            self.wait(total_time - (individual_time * 0.8 * len(squares)))
        
        with self.voiceover(text="This is an efficient way to create patterns.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing all squares.") as tracker:
            self.play(*[FadeOut(s) for s in squares], run_time=tracker.duration)


class AnimateSuccessionVoice(VoiceoverScene):
    """Animating objects in succession with AnimationGroup."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circles = [
            Circle(radius=0.5, color=RED).shift(LEFT * 2),
            Circle(radius=0.5, color=GREEN),
            Circle(radius=0.5, color=BLUE).shift(RIGHT * 2),
        ]
        
        with self.voiceover(text="AnimationGroup controls timing with lag ratio. These circles overlap their animations by fifty percent.") as tracker:
            self.play(
                AnimationGroup(
                    *[Create(c) for c in circles],
                    lag_ratio=0.5
                ),
                run_time=tracker.duration
            )
        
        with self.voiceover(text="This creates a cascading effect.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing the circles.") as tracker:
            self.play(*[FadeOut(c) for c in circles], run_time=tracker.duration)


class CopyingObjectsVoice(VoiceoverScene):
    """Creating copies of objects."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        original = Circle(radius=1, color=BLUE)
        original.set_fill(BLUE, opacity=0.5)
        original.shift(LEFT * 3)
        
        with self.voiceover(text="We start with an original blue circle on the left.") as tracker:
            self.play(Create(original), run_time=tracker.duration)
        
        copy1 = original.copy().shift(RIGHT * 3)
        
        with self.voiceover(text="Using copy, we create a duplicate and shift it.") as tracker:
            self.play(Create(copy1), run_time=tracker.duration)
        
        copy2 = original.copy().shift(RIGHT * 6)
        
        with self.voiceover(text="We can make multiple copies with all properties preserved.") as tracker:
            self.play(Create(copy2), run_time=tracker.duration)
        
        with self.voiceover(text="Copying is useful for creating patterns.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing all objects.") as tracker:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=tracker.duration)


class UpdaterExampleVoice(VoiceoverScene):
    """Using always_redraw for dynamic objects."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle = Circle(radius=0.5, color=BLUE)
        circle.set_fill(BLUE, opacity=0.5)
        circle.shift(LEFT * 3)
        
        dot = Dot(RIGHT * 3)
        
        line = always_redraw(
            lambda: Line(
                start=circle.get_center(),
                end=dot.get_center(),
                color=YELLOW
            )
        )
        
        self.add(circle, dot, line)
        
        with self.voiceover(text="The yellow line always connects the circle to the dot, even as they move.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Watch the line update automatically as the circle moves right.") as tracker:
            self.play(circle.animate.shift(RIGHT * 6), run_time=tracker.duration)
        
        with self.voiceover(text="And as it moves up, the line follows.") as tracker:
            self.play(circle.animate.shift(UP * 2), run_time=tracker.duration)
        
        with self.voiceover(text="Always redraw creates dynamic, responsive objects.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing everything.") as tracker:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=tracker.duration)


