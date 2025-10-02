"""
Lesson 9 with Voice: Advanced Positioning

All 5 scenes about precise positioning and alignment techniques with voice.

To render:
    python3 -m manim -pql 09_positioning_voice.py AlignmentBasicsVoice
"""

from manim import *
from manim_voiceover import VoiceoverScene
from voiceover_config import configure_voiceover


class AlignmentBasicsVoice(VoiceoverScene):
    """Aligning objects to each other."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        square = Square(side_length=2, color=BLUE)
        square.set_fill(BLUE, opacity=0.3)
        
        circle1 = Circle(radius=0.5, color=RED).align_to(square, LEFT)
        circle2 = Circle(radius=0.5, color=GREEN).align_to(square, RIGHT)
        circle3 = Circle(radius=0.5, color=YELLOW).align_to(square, UP)
        circle4 = Circle(radius=0.5, color=PURPLE).align_to(square, DOWN)
        
        with self.voiceover(text="We have a blue reference square.") as tracker:
            self.play(Create(square), run_time=tracker.duration)
        
        with self.voiceover(text="Four circles are aligned to the square's edges: red left, green right, yellow top, purple bottom.") as tracker:
            self.play(
                Create(circle1),
                Create(circle2),
                Create(circle3),
                Create(circle4),
                run_time=tracker.duration
            )
        
        with self.voiceover(text="Align to positions objects precisely relative to other objects.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Clearing the scene.") as tracker:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=tracker.duration)


class ArrangeInGridVoice(VoiceoverScene):
    """Arranging multiple objects in a grid."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circles = VGroup(*[
            Circle(radius=0.4, color=BLUE).set_fill(BLUE, opacity=0.5)
            for _ in range(9)
        ])
        
        circles.arrange_in_grid(rows=3, cols=3, buff=0.5)
        
        with self.voiceover(text="Arrange in grid automatically positions objects in rows and columns. Here's a three by three grid.") as tracker:
            self.play(Create(circles), run_time=tracker.duration)
        
        with self.voiceover(text="This is perfect for creating structured layouts.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing the grid.") as tracker:
            self.play(FadeOut(circles), run_time=tracker.duration)


class ArrangeInRowVoice(VoiceoverScene):
    """Arranging objects in a row or column."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        shapes = VGroup(
            Circle(radius=0.5, color=RED),
            Square(side_length=1, color=GREEN),
            Triangle(color=BLUE),
            Star(color=YELLOW),
        )
        
        shapes.arrange(RIGHT, buff=0.5)
        
        with self.voiceover(text="These shapes are arranged in a horizontal row, from left to right.") as tracker:
            self.play(Create(shapes), run_time=tracker.duration)
        
        with self.voiceover(text="Now let's rearrange them in a vertical column.") as tracker:
            self.play(shapes.animate.arrange(DOWN, buff=0.5), run_time=tracker.duration)
        
        with self.voiceover(text="Arrange makes it easy to line up objects.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing the shapes.") as tracker:
            self.play(FadeOut(shapes), run_time=tracker.duration)


class CenterAndShiftVoice(VoiceoverScene):
    """Centering and shifting objects."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        text = Text("This is centered")
        text.move_to(ORIGIN)
        
        with self.voiceover(text="This text is centered at the origin.") as tracker:
            self.play(Write(text), run_time=tracker.duration)
        
        with self.voiceover(text="Now it shifts up two units.") as tracker:
            self.play(text.animate.shift(UP * 2), run_time=tracker.duration)
        
        with self.voiceover(text="Back to center using move to.") as tracker:
            self.play(text.animate.move_to(ORIGIN), run_time=tracker.duration)
        
        with self.voiceover(text="And down two units using shift.") as tracker:
            self.play(text.animate.shift(DOWN * 2), run_time=tracker.duration)
        
        with self.voiceover(text="Move to sets absolute position, shift moves relatively.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing the text.") as tracker:
            self.play(FadeOut(text), run_time=tracker.duration)


class GetCenterVoice(VoiceoverScene):
    """Using get_center and positioning relative to centers."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        large_square = Square(side_length=3, color=BLUE)
        large_square.set_fill(BLUE, opacity=0.2)
        
        with self.voiceover(text="We have a large blue square.") as tracker:
            self.play(Create(large_square), run_time=tracker.duration)
        
        small_circle = Circle(radius=0.3, color=RED)
        small_circle.set_fill(RED, opacity=0.7)
        small_circle.move_to(large_square.get_center())
        
        with self.voiceover(text="A small red circle is positioned at the square's exact center using get center.") as tracker:
            self.play(Create(small_circle), run_time=tracker.duration)
        
        with self.voiceover(text="Get center returns the coordinates of an object's center point.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Clearing everything.") as tracker:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=tracker.duration)


