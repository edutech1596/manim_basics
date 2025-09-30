"""
Lesson 6: Transform Animations

Learn how to transform one object into another.

To render:
    manim -pql 06_transform_animations.py BasicTransform
"""

# Import all Manim functionality
from manim import *


class BasicTransform(Scene):
    """
    Basic transformation from one shape to another.
    """
    
    def construct(self):
        # Transform() morphs one shape into another
        # Start with a blue circle
        circle = Circle(color=BLUE)
        
        # Fill the circle
        circle.set_fill(BLUE, opacity=0.5)
        
        # Show the circle
        self.play(Create(circle))
        
        # Wait 1 second
        self.wait(1)
        
        # Create a target square (what we want to transform INTO)
        # Note: we're not showing this yet, just creating it
        square = Square(color=GREEN)
        
        # Fill the square
        square.set_fill(GREEN, opacity=0.5)
        
        # Transform() morphs circle into square shape
        # Note: the circle object remains, but looks like square now
        self.play(Transform(circle, square))
        
        # Wait 1 second
        self.wait(1)
        
        # Create another target shape (triangle)
        triangle = Triangle(color=RED)
        
        # Fill the triangle
        triangle.set_fill(RED, opacity=0.5)
        
        # Transform the circle (which looks like a square) into triangle
        # We still reference "circle" because that's the object that exists
        self.play(Transform(circle, triangle))
        
        # Wait 1 second
        self.wait(1)
        
        # Remove the circle (which now looks like a triangle)
        self.play(FadeOut(circle))


class ReplacementTransformExample(Scene):
    """
    ReplacementTransform actually replaces the object.
    
    To render:
        manim -pql 06_transform_animations.py ReplacementTransformExample
    """
    
    def construct(self):
        # ReplacementTransform actually swaps objects
        # Create a blue circle
        circle = Circle(color=BLUE)
        
        # Fill it
        circle.set_fill(BLUE, opacity=0.5)
        
        # Show the circle
        self.play(Create(circle))
        
        # Wait 1 second
        self.wait(1)
        
        # Create a square to replace the circle
        square = Square(color=GREEN)
        
        # Fill the square
        square.set_fill(GREEN, opacity=0.5)
        
        # ReplacementTransform removes circle and adds square
        # After this, "circle" no longer exists, "square" does
        self.play(ReplacementTransform(circle, square))
        
        # Wait 1 second
        self.wait(1)
        
        # Create a triangle
        # Now we use "square" because that's what exists
        triangle = Triangle(color=RED)
        
        # Fill the triangle
        triangle.set_fill(RED, opacity=0.5)
        
        # Replace square with triangle
        # After this, "square" is gone, "triangle" exists
        self.play(ReplacementTransform(square, triangle))
        
        # Wait 1 second
        self.wait(1)
        
        # Remove the triangle (not circle or square - they're gone!)
        self.play(FadeOut(triangle))


class TextTransform(Scene):
    """
    Transforming text is very useful for explanations.
    
    To render:
        manim -pql 06_transform_animations.py TextTransform
    """
    
    def construct(self):
        # Transform works great with text too
        # Create the first text
        text1 = Text("Hello")
        
        # Write the text
        self.play(Write(text1))
        
        # Wait 1 second
        self.wait(1)
        
        # Create different text to transform into
        text2 = Text("World")
        
        # Transform "Hello" into "World"
        # The letters morph from one to the other
        self.play(Transform(text1, text2))
        
        # Wait 1 second
        self.wait(1)
        
        # Create longer text
        text3 = Text("Manim is awesome!")
        
        # Transform into the longer text
        # text1 still exists but now looks like text3
        self.play(Transform(text1, text3))
        
        # Wait 2 seconds to read it
        self.wait(2)
        
        # Remove text1 (which displays as "Manim is awesome!")
        self.play(FadeOut(text1))


class TransformMatchingShapesExample(Scene):
    """
    TransformMatchingShapes for smooth transitions.
    
    To render:
        manim -pql 06_transform_animations.py TransformMatchingShapesExample
    """
    
    def construct(self):
        # TransformMatchingShapes is advanced - it matches similar objects
        # Create first group of shapes
        # Blue circle on the left
        circle = Circle(color=BLUE).shift(LEFT)
        
        # Green square on the right
        square = Square(color=GREEN).shift(RIGHT)
        
        # VGroup combines multiple objects into one group
        group1 = VGroup(circle, square)
        
        # Show the first group
        self.play(Create(group1))
        
        # Wait 1 second
        self.wait(1)
        
        # Create second group with different shapes
        # Red triangle at the top
        triangle = Triangle(color=RED).shift(UP)
        
        # Yellow star at the bottom
        star = Star(color=YELLOW).shift(DOWN)
        
        # Group them together
        group2 = VGroup(triangle, star)
        
        # TransformMatchingShapes intelligently morphs between groups
        # It tries to match up corresponding objects
        self.play(TransformMatchingShapes(group1, group2))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove the second group
        self.play(FadeOut(group2)) 