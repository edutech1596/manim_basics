"""
Lesson 10: Working with Multiple Objects

Learn to manage and animate many objects together.

To render:
    manim -pql 10_multiple_objects.py MultipleCircles
"""

# Import all Manim functionality
from manim import *


class MultipleCircles(Scene):
    """
    Creating and animating multiple objects.
    """
    
    def construct(self):
        # When working with many objects, use loops to create them
        
        # Create an empty list to store our circles
        circles = []
        
        # List of colors to use
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
        
        # Loop through colors with their index
        # enumerate() gives us both position (i) and color
        for i, color in enumerate(colors):
            # Create a circle with the current color
            circle = Circle(radius=0.5, color=color)
            
            # Fill the circle
            circle.set_fill(color, opacity=0.5)
            
            # Position each circle horizontally
            # LEFT * 3 starts at the left, RIGHT * i * 1.2 spaces them out
            circle.shift(LEFT * 3 + RIGHT * i * 1.2)
            
            # Add the circle to our list
            circles.append(circle)
        
        # Animate all circles appearing at once
        # *[Create(c) for c in circles] creates a Create animation for each
        # The * unpacks the list into separate arguments
        self.play(*[Create(c) for c in circles])
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove all circles at once
        self.play(*[FadeOut(c) for c in circles])


class ListComprehension(Scene):
    """
    Using list comprehension to create multiple objects.
    
    To render:
        manim -pql 10_multiple_objects.py ListComprehension
    """
    
    def construct(self):
        # List comprehension is a Python shortcut for creating lists
        
        # Create 10 squares in one line using list comprehension
        # [expression for variable in range(n)] creates n items
        squares = [
            Square(side_length=0.5, color=BLUE).shift(UP * 2 + LEFT * 4.5 + RIGHT * i)
            for i in range(10)  # i goes from 0 to 9
        ]
        
        # Animate them appearing one by one
        # Loop through each square
        for square in squares:
            # Create each square with a faster run_time
            self.play(Create(square), run_time=0.2)
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove all squares at once
        self.play(*[FadeOut(s) for s in squares])


class AnimateSuccession(Scene):
    """
    Animating objects in succession with AnimationGroup.
    
    To render:
        manim -pql 10_multiple_objects.py AnimateSuccession
    """
    
    def construct(self):
        # AnimationGroup lets you control timing of multiple animations
        
        # Create three circles at different positions
        circles = [
            Circle(radius=0.5, color=RED).shift(LEFT * 2),
            Circle(radius=0.5, color=GREEN),
            Circle(radius=0.5, color=BLUE).shift(RIGHT * 2),
        ]
        
        # Animate with lag ratio
        # AnimationGroup groups animations together
        self.play(
            AnimationGroup(
                *[Create(c) for c in circles],
                lag_ratio=0.5  # 0.5 = 50% overlap between animations
                # 0 = all at once, 1 = completely sequential
            )
        )
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove all circles
        self.play(*[FadeOut(c) for c in circles])


class CopyingObjects(Scene):
    """
    Creating copies of objects.
    
    To render:
        manim -pql 10_multiple_objects.py CopyingObjects
    """
    
    def construct(self):
        # .copy() creates a duplicate of an object
        
        # Create an original blue circle
        original = Circle(radius=1, color=BLUE)
        
        # Fill it
        original.set_fill(BLUE, opacity=0.5)
        
        # Position it on the left
        original.shift(LEFT * 3)
        
        # Show the original
        self.play(Create(original))
        
        # Wait 1 second
        self.wait(1)
        
        # Create a copy of the original
        # .copy() duplicates the circle with all its properties
        # .shift() then moves the copy to a different position
        copy1 = original.copy().shift(RIGHT * 3)
        
        # Create another copy
        copy2 = original.copy().shift(RIGHT * 6)
        
        # Show first copy
        self.play(Create(copy1))
        
        # Show second copy
        self.play(Create(copy2))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove all objects
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class UpdaterExample(Scene):
    """
    Using always_redraw for dynamic objects.
    
    To render:
        manim -pql 10_multiple_objects.py UpdaterExample
    """
    
    def construct(self):
        # always_redraw() creates objects that update automatically
        
        # Create a moving circle
        circle = Circle(radius=0.5, color=BLUE)
        
        # Fill it
        circle.set_fill(BLUE, opacity=0.5)
        
        # Position it on the left
        circle.shift(LEFT * 3)
        
        # Create a stationary dot on the right
        dot = Dot(RIGHT * 3)
        
        # Create a line that always connects circle to dot
        # always_redraw() makes the line redraw every frame
        # lambda: creates an anonymous function
        line = always_redraw(
            lambda: Line(
                start=circle.get_center(),  # Always get circle's current position
                end=dot.get_center(),       # Always get dot's position
                color=YELLOW
            )
        )
        
        # Add all objects to the scene
        # .add() puts objects on screen without animation
        self.add(circle, dot, line)
        
        # Wait 1 second
        self.wait(1)
        
        # Move the circle - the line automatically follows!
        # The line redraws itself to stay connected
        self.play(circle.animate.shift(RIGHT * 6))
        
        # Wait 1 second
        self.wait(1)
        
        # Move the circle up - line still follows
        self.play(circle.animate.shift(UP * 2))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove everything
        self.play(*[FadeOut(mob) for mob in self.mobjects]) 