"""
Lesson 11: Grouping Objects with VGroup

Learn to group objects together for easier manipulation.

To render:
    manim -pql 11_groups.py BasicGroup
"""

# Import all Manim functionality
from manim import *


class BasicGroup(Scene):
    """
    Creating and using basic VGroups.
    """
    
    def construct(self):
        # VGroup (Vector Group) combines multiple objects into one
        # This lets you animate them together as a single unit
        
        # Create individual shapes
        circle = Circle(radius=1, color=BLUE)
        square = Square(side_length=1.5, color=GREEN)
        triangle = Triangle(color=RED)
        
        # Group them together using VGroup
        # Now they act as one object
        shapes_group = VGroup(circle, square, triangle)
        
        # Arrange the group horizontally
        # arrange() works on the whole group at once
        # RIGHT means left-to-right, buff=1 is the spacing
        shapes_group.arrange(RIGHT, buff=1)
        
        # Animate the entire group at once
        # Create(shapes_group) creates all shapes together
        self.play(Create(shapes_group))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Move the entire group as one unit
        self.play(shapes_group.animate.shift(UP * 2))
        
        # Wait 1 second
        self.wait(1)
        
        # Remove the group
        self.play(FadeOut(shapes_group))


class GroupOperations(Scene):
    """
    Operations you can perform on groups.
    
    To render:
        manim -pql 11_groups.py GroupOperations
    """
    
    def construct(self):
        # Groups can be scaled, rotated, colored, etc. as a whole
        
        # Create a group of 5 circles using list comprehension
        # VGroup(*[...]) unpacks the list into VGroup
        circles = VGroup(*[
            Circle(radius=0.5, color=BLUE)
            for _ in range(5)  # underscore means we don't use the value
        ])
        
        # Arrange them in a row
        circles.arrange(RIGHT, buff=0.5)
        
        # Show all circles
        self.play(Create(circles))
        
        # Wait 1 second
        self.wait(1)
        
        # Scale the entire group larger
        # .animate makes it animated
        # scale(1.5) makes it 1.5 times bigger
        self.play(circles.animate.scale(1.5))
        
        # Wait 1 second
        self.wait(1)
        
        # Rotate the entire group
        # Rotate() spins all circles around the group's center
        # PI/4 radians = 45 degrees
        self.play(Rotate(circles, angle=PI/4))
        
        # Wait 1 second
        self.wait(1)
        
        # Change color of entire group
        # set_color() applies to all objects in the group
        self.play(circles.animate.set_color(RED))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove the group
        self.play(FadeOut(circles))


class AddToGroup(Scene):
    """
    Adding objects to a group dynamically.
    
    To render:
        manim -pql 11_groups.py AddToGroup
    """
    
    def construct(self):
        # You can start with an empty group and add to it
        
        # Create an empty VGroup
        group = VGroup()
        
        # Add 6 squares one by one
        for i in range(6):
            # Create a square
            square = Square(side_length=0.5, color=GREEN)
            
            # Position it
            square.shift(UP * 2 + LEFT * 2.5 + RIGHT * i)
            
            # Add it to the group
            # .add() adds an object to the group
            group.add(square)
            
            # Create the square with short animation
            self.play(Create(square), run_time=0.3)
        
        # Wait 1 second
        self.wait(1)
        
        # Now animate the whole group together
        # Even though we added squares individually, they're grouped now
        self.play(group.animate.shift(DOWN * 2))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove the group
        self.play(FadeOut(group))


class NestedGroups(Scene):
    """
    Creating groups within groups.
    
    To render:
        manim -pql 11_groups.py NestedGroups
    """
    
    def construct(self):
        # You can put groups inside other groups (nesting)
        
        # Create first group (3 blue circles)
        circles = VGroup(*[
            Circle(radius=0.3, color=BLUE)
            for _ in range(3)
        ])
        # Arrange them horizontally
        circles.arrange(RIGHT, buff=0.3)
        # Move the group up
        circles.shift(UP * 2)
        
        # Create second group (3 green squares)
        squares = VGroup(*[
            Square(side_length=0.6, color=GREEN)
            for _ in range(3)
        ])
        # Arrange them horizontally
        squares.arrange(RIGHT, buff=0.3)
        # This group stays at center
        
        # Create third group (3 red triangles)
        triangles = VGroup(*[
            Triangle(color=RED).scale(0.3)
            for _ in range(3)
        ])
        # Arrange them horizontally
        triangles.arrange(RIGHT, buff=0.3)
        # Move the group down
        triangles.shift(DOWN * 2)
        
        # Create a mega-group containing all three groups
        # This is a group of groups!
        all_shapes = VGroup(circles, squares, triangles)
        
        # Show everything at once
        self.play(Create(all_shapes))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Rotate the mega-group
        # All three groups rotate together around a common center
        self.play(Rotate(all_shapes, angle=PI/6))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove everything
        self.play(FadeOut(all_shapes))


class GroupWithText(Scene):
    """
    Combining shapes and text in groups.
    
    To render:
        manim -pql 11_groups.py GroupWithText
    """
    
    def construct(self):
        # Groups are great for combining shapes with their labels
        
        # Create a blue circle
        circle = Circle(radius=1, color=BLUE)
        circle.set_fill(BLUE, opacity=0.3)
        
        # Create a label for it
        label = Text("Circle").scale(0.7)
        
        # Position the label below the circle
        label.next_to(circle, DOWN)
        
        # Group the circle and its label together
        labeled_circle = VGroup(circle, label)
        
        # Move the whole labeled circle to the left
        labeled_circle.shift(LEFT * 3)
        
        # Create a green square with label
        square = Square(side_length=1.5, color=GREEN)
        square.set_fill(GREEN, opacity=0.3)
        
        # Create its label
        label2 = Text("Square").scale(0.7)
        
        # Position label below square
        label2.next_to(square, DOWN)
        
        # Group square and label
        labeled_square = VGroup(square, label2)
        
        # Move to the right
        labeled_square.shift(RIGHT * 3)
        
        # Animate both labeled groups
        # Each group includes both a shape and its text
        self.play(
            Create(labeled_circle),
            Create(labeled_square),
        )
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove both groups
        self.play(
            FadeOut(labeled_circle),
            FadeOut(labeled_square),
        ) 