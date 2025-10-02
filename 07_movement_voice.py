"""
Lesson 7 with Voice: Movement Animations

All 5 scenes about moving objects around the scene with voice.

To render:
    python3 -m manim -pql 07_movement_voice.py ShiftMovementVoice
"""

from manim import *
from manim_voiceover import VoiceoverScene
from voiceover_config import configure_voiceover


class ShiftMovementVoice(VoiceoverScene):
    """Moving objects with shift."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle = Circle(color=BLUE)
        circle.set_fill(BLUE, opacity=0.5)
        
        with self.voiceover(text="We create a blue circle at the center.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
        
        with self.voiceover(text="Now it shifts two units to the right.") as tracker:
            self.play(circle.animate.shift(RIGHT * 2), run_time=tracker.duration)
        
        with self.voiceover(text="Then it moves up two units.") as tracker:
            self.play(circle.animate.shift(UP * 2), run_time=tracker.duration)
        
        with self.voiceover(text="Now it shifts four units to the left.") as tracker:
            self.play(circle.animate.shift(LEFT * 4), run_time=tracker.duration)
        
        with self.voiceover(text="Finally, it moves down two units.") as tracker:
            self.play(circle.animate.shift(DOWN * 2), run_time=tracker.duration)
        
        with self.voiceover(text="Shift moves objects by a relative amount from their current position.") as tracker:
            self.play(FadeOut(circle), run_time=tracker.duration)


class MoveToPositionVoice(VoiceoverScene):
    """Moving objects to specific positions."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        square = Square(color=GREEN)
        square.set_fill(GREEN, opacity=0.5)
        
        with self.voiceover(text="We have a green square at the center.") as tracker:
            self.play(Create(square), run_time=tracker.duration)
        
        with self.voiceover(text="MoveT o places it at an absolute position, like the top-left corner.") as tracker:
            self.play(square.animate.move_to(UP * 2 + LEFT * 3), run_time=tracker.duration)
        
        with self.voiceover(text="Now to the bottom-right corner.") as tracker:
            self.play(square.animate.move_to(DOWN * 2 + RIGHT * 3), run_time=tracker.duration)
        
        with self.voiceover(text="And back to the exact center.") as tracker:
            self.play(square.animate.move_to(ORIGIN), run_time=tracker.duration)
        
        with self.voiceover(text="Move to is useful for precise positioning.") as tracker:
            self.play(FadeOut(square), run_time=tracker.duration)


class ToEdgeMovementVoice(VoiceoverScene):
    """Moving objects to edges of the screen."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle = Circle(color=RED)
        circle.set_fill(RED, opacity=0.5)
        
        with self.voiceover(text="We create a red circle.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
        
        with self.voiceover(text="To edge moves it all the way to the top edge.") as tracker:
            self.play(circle.animate.to_edge(UP), run_time=tracker.duration)
        
        with self.voiceover(text="Then to the right edge.") as tracker:
            self.play(circle.animate.to_edge(RIGHT), run_time=tracker.duration)
        
        with self.voiceover(text="To the bottom edge.") as tracker:
            self.play(circle.animate.to_edge(DOWN), run_time=tracker.duration)
        
        with self.voiceover(text="And to the left edge.") as tracker:
            self.play(circle.animate.to_edge(LEFT), run_time=tracker.duration)
        
        with self.voiceover(text="To edge is perfect for placing objects at screen boundaries.") as tracker:
            self.play(FadeOut(circle), run_time=tracker.duration)


class NextToPositionVoice(VoiceoverScene):
    """Positioning objects next to other objects."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        square = Square(color=YELLOW)
        square.set_fill(YELLOW, opacity=0.5)
        
        with self.voiceover(text="We have a yellow square in the center.") as tracker:
            self.play(Create(square), run_time=tracker.duration)
        
        circle_up = Circle(radius=0.5, color=BLUE)
        circle_up.set_fill(BLUE, opacity=0.5)
        circle_up.next_to(square, UP)
        
        circle_down = Circle(radius=0.5, color=GREEN)
        circle_down.set_fill(GREEN, opacity=0.5)
        circle_down.next_to(square, DOWN)
        
        circle_left = Circle(radius=0.5, color=RED)
        circle_left.set_fill(RED, opacity=0.5)
        circle_left.next_to(square, LEFT)
        
        circle_right = Circle(radius=0.5, color=PURPLE)
        circle_right.set_fill(PURPLE, opacity=0.5)
        circle_right.next_to(square, RIGHT)
        
        with self.voiceover(text="Now four circles appear, positioned next to each side of the square.") as tracker:
            self.play(
                Create(circle_up),
                Create(circle_down),
                Create(circle_left),
                Create(circle_right),
                run_time=tracker.duration
            )
        
        with self.voiceover(text="Next to positions objects relative to other objects.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Clearing everything.") as tracker:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=tracker.duration)


class RotationMovementVoice(VoiceoverScene):
    """Rotating objects."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        square = Square(color=ORANGE)
        square.set_fill(ORANGE, opacity=0.5)
        
        with self.voiceover(text="We have an orange square.") as tracker:
            self.play(Create(square), run_time=tracker.duration)
        
        with self.voiceover(text="Watch as it rotates ninety degrees.") as tracker:
            self.play(Rotate(square, angle=PI/2), run_time=tracker.duration)
        
        with self.voiceover(text="Another ninety degrees.") as tracker:
            self.play(Rotate(square, angle=PI/2), run_time=tracker.duration)
        
        with self.voiceover(text="Now a full three hundred sixty degree rotation.") as tracker:
            self.play(Rotate(square, angle=2*PI), run_time=tracker.duration)
        
        with self.voiceover(text="Rotation adds dynamic motion to animations.") as tracker:
            self.play(FadeOut(square), run_time=tracker.duration)


