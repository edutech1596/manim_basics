"""
Lesson 5: Create Animations

Different ways to create and introduce objects.

To render:
    manim -pql 05_create_animations.py CreateMethods
"""

# Import all Manim functionality
from manim import *


class CreateMethods(Scene):
    """
    Different creation animation styles.
    """
    
    def construct(self):
        # Create() animation draws the object's border
        # Start with a blue circle
        circle = Circle(color=BLUE)
        
        # Move it 3 units to the left
        circle.shift(LEFT * 3)
        
        # Create() draws the shape from start to finish
        self.play(Create(circle))
        
        # Pause for 1 second
        self.wait(1)
        
        # FadeIn() makes the object gradually appear
        # Create a green square
        square = Square(color=GREEN)
        
        # Keep it at the center (ORIGIN)
        square.shift(ORIGIN)
        
        # FadeIn gradually increases opacity from 0 to 1
        self.play(FadeIn(square))
        
        # Pause for 1 second
        self.wait(1)
        
        # GrowFromCenter() makes the object grow from a point
        # Create a red triangle
        triangle = Triangle(color=RED)
        
        # Move it 3 units to the right
        triangle.shift(RIGHT * 3)
        
        # The triangle starts tiny and grows to full size
        self.play(GrowFromCenter(triangle))
        
        # Pause for 1 second
        self.wait(1)
        
        # Remove all objects from screen
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class MoreCreateAnimations(Scene):
    """
    More creative ways to introduce objects.
    
    To render:
        manim -pql 05_create_animations.py MoreCreateAnimations
    """
    
    def construct(self):
        # DrawBorderThenFill draws the outline first, then fills it in
        # Create a blue circle
        circle = Circle(color=BLUE)
        
        # Set the fill color and opacity
        circle.set_fill(BLUE, opacity=0.5)
        
        # Move it up by 2 units
        circle.shift(UP * 2)
        
        # First draws the border, then the fill appears
        self.play(DrawBorderThenFill(circle))
        
        # Pause for 1 second
        self.wait(1)
        
        # SpinInFromNothing spins and scales the object simultaneously
        # Create a green square
        square = Square(color=GREEN)
        
        # Fill it
        square.set_fill(GREEN, opacity=0.5)
        
        # The square will spin and grow from nothing
        self.play(SpinInFromNothing(square))
        
        # Pause for 1 second
        self.wait(1)
        
        # GrowFromEdge grows the object from a specific edge
        # Create a yellow rectangle
        rect = Rectangle(width=3, height=1, color=YELLOW)
        
        # Fill it
        rect.set_fill(YELLOW, opacity=0.5)
        
        # Move it down by 2 units
        rect.shift(DOWN * 2)
        
        # Grows from the LEFT edge to the right
        self.play(GrowFromEdge(rect, LEFT))
        
        # Pause for 1 second
        self.wait(1)
        
        # Remove all objects
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class WriteAnimation(Scene):
    """
    Write animation is special for text.
    
    To render:
        manim -pql 05_create_animations.py WriteAnimation
    """
    
    def construct(self):
        # Write() is designed for text - it writes letter by letter
        # Create text
        text = Text("This text is being written!")
        
        # Write the text as if typing it
        self.play(Write(text))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove the text
        self.play(FadeOut(text))
        
        # Write() also works on shapes (draws their path)
        # Create a blue circle
        circle = Circle(color=BLUE)
        
        # Write traces the circle's outline
        self.play(Write(circle))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove the circle
        self.play(FadeOut(circle))


class UncreateAnimations(Scene):
    """
    Animations for removing objects (opposite of create).
    
    To render:
        manim -pql 05_create_animations.py UncreateAnimations
    """
    
    def construct(self):
        # Create three shapes to demonstrate removal animations
        # Blue circle on the left
        circle = Circle(color=BLUE).shift(LEFT * 2)
        
        # Green square in the center
        square = Square(color=GREEN)
        
        # Red triangle on the right
        triangle = Triangle(color=RED).shift(RIGHT * 2)
        
        # Show all three shapes at once
        self.play(Create(circle), Create(square), Create(triangle))
        
        # Wait 1 second
        self.wait(1)
        
        # Uncreate() is the reverse of Create()
        # It "un-draws" the object
        self.play(Uncreate(circle))
        
        # Short pause
        self.wait(0.5)
        
        # FadeOut() gradually makes the object transparent
        self.play(FadeOut(square))
        
        # Short pause
        self.wait(0.5)
        
        # ShrinkToCenter() shrinks the object to a point
        # Opposite of GrowFromCenter()
        self.play(ShrinkToCenter(triangle))
        
        # Final pause
        self.wait(1) 