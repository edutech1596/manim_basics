"""
Lesson 11 with Voice: Grouping Objects with VGroup

All 5 scenes about grouping objects together for easier manipulation with voice.

To render:
    python3 -m manim -pql 11_groups_voice.py BasicGroupVoice
"""

from manim import *
from manim_voiceover import VoiceoverScene
from voiceover_config import configure_voiceover


class BasicGroupVoice(VoiceoverScene):
    """Creating and using basic VGroups."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle = Circle(radius=1, color=BLUE)
        square = Square(side_length=1.5, color=GREEN)
        triangle = Triangle(color=RED)
        
        shapes_group = VGroup(circle, square, triangle)
        shapes_group.arrange(RIGHT, buff=1)
        
        with self.voiceover(text="VGroup combines multiple objects into one. Here's a circle, square, and triangle grouped together.") as tracker:
            self.play(Create(shapes_group), run_time=tracker.duration)
        
        with self.voiceover(text="Now we can move the entire group as one unit.") as tracker:
            self.play(shapes_group.animate.shift(UP * 2), run_time=tracker.duration)
        
        with self.voiceover(text="Grouping simplifies working with related objects.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing the group.") as tracker:
            self.play(FadeOut(shapes_group), run_time=tracker.duration)


class GroupOperationsVoice(VoiceoverScene):
    """Operations you can perform on groups."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circles = VGroup(*[
            Circle(radius=0.5, color=BLUE)
            for _ in range(5)
        ])
        
        circles.arrange(RIGHT, buff=0.5)
        
        with self.voiceover(text="We have five blue circles in a group.") as tracker:
            self.play(Create(circles), run_time=tracker.duration)
        
        with self.voiceover(text="We can scale the entire group larger.") as tracker:
            self.play(circles.animate.scale(1.5), run_time=tracker.duration)
        
        with self.voiceover(text="Rotate all circles around their common center.") as tracker:
            self.play(Rotate(circles, angle=PI/4), run_time=tracker.duration)
        
        with self.voiceover(text="And change the color of the whole group to red.") as tracker:
            self.play(circles.animate.set_color(RED), run_time=tracker.duration)
        
        with self.voiceover(text="Group operations apply to all members simultaneously.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing the group.") as tracker:
            self.play(FadeOut(circles), run_time=tracker.duration)


class AddToGroupVoice(VoiceoverScene):
    """Adding objects to a group dynamically."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        group = VGroup()
        
        with self.voiceover(text="We can start with an empty group and add squares one by one.") as tracker:
            total_time = tracker.duration
            individual_time = total_time / 6
            for i in range(6):
                square = Square(side_length=0.5, color=GREEN)
                square.shift(UP * 2 + LEFT * 2.5 + RIGHT * i)
                group.add(square)
                self.play(Create(square), run_time=individual_time * 0.8)
            self.wait(total_time - (individual_time * 0.8 * 6))
        
        with self.voiceover(text="Now they're all grouped, so we can move them together.") as tracker:
            self.play(group.animate.shift(DOWN * 2), run_time=tracker.duration)
        
        with self.voiceover(text="Adding to groups dynamically is very flexible.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing the group.") as tracker:
            self.play(FadeOut(group), run_time=tracker.duration)


class NestedGroupsVoice(VoiceoverScene):
    """Creating groups within groups."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circles = VGroup(*[
            Circle(radius=0.3, color=BLUE)
            for _ in range(3)
        ])
        circles.arrange(RIGHT, buff=0.3)
        circles.shift(UP * 2)
        
        squares = VGroup(*[
            Square(side_length=0.6, color=GREEN)
            for _ in range(3)
        ])
        squares.arrange(RIGHT, buff=0.3)
        
        triangles = VGroup(*[
            Triangle(color=RED).scale(0.3)
            for _ in range(3)
        ])
        triangles.arrange(RIGHT, buff=0.3)
        triangles.shift(DOWN * 2)
        
        all_shapes = VGroup(circles, squares, triangles)
        
        with self.voiceover(text="We have three separate groups: blue circles, green squares, and red triangles.") as tracker:
            self.play(Create(all_shapes), run_time=tracker.duration)
        
        with self.voiceover(text="These three groups are nested inside a mega-group, so they can all rotate together.") as tracker:
            self.play(Rotate(all_shapes, angle=PI/6), run_time=tracker.duration)
        
        with self.voiceover(text="Nested groups allow complex hierarchies.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing everything.") as tracker:
            self.play(FadeOut(all_shapes), run_time=tracker.duration)


class GroupWithTextVoice(VoiceoverScene):
    """Combining shapes and text in groups."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle = Circle(radius=1, color=BLUE)
        circle.set_fill(BLUE, opacity=0.3)
        label = Text("Circle").scale(0.7)
        label.next_to(circle, DOWN)
        labeled_circle = VGroup(circle, label)
        labeled_circle.shift(LEFT * 3)
        
        square = Square(side_length=1.5, color=GREEN)
        square.set_fill(GREEN, opacity=0.3)
        label2 = Text("Square").scale(0.7)
        label2.next_to(square, DOWN)
        labeled_square = VGroup(square, label2)
        labeled_square.shift(RIGHT * 3)
        
        with self.voiceover(text="Groups are great for combining shapes with their labels. Here's a labeled circle and square.") as tracker:
            self.play(
                Create(labeled_circle),
                Create(labeled_square),
                run_time=tracker.duration
            )
        
        with self.voiceover(text="Each group includes both the shape and its text label.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing both groups.") as tracker:
            self.play(
                FadeOut(labeled_circle),
                FadeOut(labeled_square),
                run_time=tracker.duration
            )


