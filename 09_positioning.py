"""
Lesson 9: Advanced Positioning

Master precise positioning and alignment techniques.

To render:
    manim -pql 09_positioning.py AlignmentBasics
"""

# Import all Manim functionality
from manim import *


class AlignmentBasics(Scene):
    """
    Aligning objects to each other.
    """
    
    def construct(self):
        # align_to() aligns one object's edge to another object's edge
        
        # Create a reference square (this is what we'll align to)
        square = Square(side_length=2, color=BLUE)
        
        # Fill it lightly so we can see through it
        square.set_fill(BLUE, opacity=0.3)
        
        # Create four circles that will be aligned to the square's edges
        # Red circle - will align to the LEFT edge of the square
        circle1 = Circle(radius=0.5, color=RED).align_to(square, LEFT)
        
        # Green circle - will align to the RIGHT edge of the square
        circle2 = Circle(radius=0.5, color=GREEN).align_to(square, RIGHT)
        
        # Yellow circle - will align to the TOP (UP) edge of the square
        circle3 = Circle(radius=0.5, color=YELLOW).align_to(square, UP)
        
        # Purple circle - will align to the BOTTOM (DOWN) edge of the square
        circle4 = Circle(radius=0.5, color=PURPLE).align_to(square, DOWN)
        
        # Show the reference square first
        self.play(Create(square))
        
        # Wait 1 second
        self.wait(1)
        
        # Show all aligned circles at once
        self.play(
            Create(circle1),
            Create(circle2),
            Create(circle3),
            Create(circle4),
        )
        
        # Wait 2 seconds to see the alignment
        self.wait(2)
        
        # Remove everything
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class ArrangeInGrid(Scene):
    """
    Arranging multiple objects in a grid.
    
    To render:
        manim -pql 09_positioning.py ArrangeInGrid
    """
    
    def construct(self):
        # arrange_in_grid() automatically arranges objects in rows and columns
        
        # Create 9 circles using a list comprehension
        # This creates a VGroup (group of objects)
        circles = VGroup(*[
            Circle(radius=0.4, color=BLUE).set_fill(BLUE, opacity=0.5)
            for _ in range(9)  # Creates 9 circles
        ])
        
        # Arrange them in a 3x3 grid
        # rows=3 means 3 rows
        # cols=3 means 3 columns
        # buff=0.5 is the spacing between circles
        circles.arrange_in_grid(rows=3, cols=3, buff=0.5)
        
        # Show all circles at once
        self.play(Create(circles))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove the grid
        self.play(FadeOut(circles))


class ArrangeInRow(Scene):
    """
    Arranging objects in a row or column.
    
    To render:
        manim -pql 09_positioning.py ArrangeInRow
    """
    
    def construct(self):
        # arrange() lines up objects in a direction
        
        # Create different shapes in a group
        shapes = VGroup(
            Circle(radius=0.5, color=RED),
            Square(side_length=1, color=GREEN),
            Triangle(color=BLUE),
            Star(color=YELLOW),
        )
        
        # Arrange in a horizontal row
        # RIGHT means arrange from left to right
        # buff=0.5 is the spacing between shapes
        shapes.arrange(RIGHT, buff=0.5)
        
        # Show the row arrangement
        self.play(Create(shapes))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Rearrange in a vertical column
        # DOWN means arrange from top to bottom
        # .animate makes the rearrangement animated
        self.play(shapes.animate.arrange(DOWN, buff=0.5))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove the shapes
        self.play(FadeOut(shapes))


class CenterAndShift(Scene):
    """
    Centering and shifting objects.
    
    To render:
        manim -pql 09_positioning.py CenterAndShift
    """
    
    def construct(self):
        # move_to() places an object at a specific position
        
        # Create text
        text = Text("This is centered")
        
        # move_to(ORIGIN) centers the text
        # ORIGIN is the exact center of the screen (0, 0, 0)
        text.move_to(ORIGIN)
        
        # Write the text
        self.play(Write(text))
        
        # Wait 1 second
        self.wait(1)
        
        # Shift the text up by 2 units
        # shift() moves relative to current position
        self.play(text.animate.shift(UP * 2))
        
        # Short pause
        self.wait(0.5)
        
        # Move back to center (absolute position)
        # move_to() sets absolute position
        self.play(text.animate.move_to(ORIGIN))
        
        # Short pause
        self.wait(0.5)
        
        # Shift down by 2 units (relative movement)
        self.play(text.animate.shift(DOWN * 2))
        
        # Wait 1 second
        self.wait(1)
        
        # Remove the text
        self.play(FadeOut(text))


class GetCenter(Scene):
    """
    Using get_center() and positioning relative to centers.
    
    To render:
        manim -pql 09_positioning.py GetCenter
    """
    
    def construct(self):
        # get_center() returns the center point of an object
        
        # Create a large blue square
        large_square = Square(side_length=3, color=BLUE)
        
        # Fill it lightly
        large_square.set_fill(BLUE, opacity=0.2)
        
        # Show the large square
        self.play(Create(large_square))
        
        # Wait 1 second
        self.wait(1)
        
        # Create a small red circle
        small_circle = Circle(radius=0.3, color=RED)
        
        # Fill it
        small_circle.set_fill(RED, opacity=0.7)
        
        # Position the circle at the center of the square
        # get_center() gets the coordinates of the square's center
        # move_to() places the circle at those coordinates
        small_circle.move_to(large_square.get_center())
        
        # Show the circle (now centered on the square)
        self.play(Create(small_circle))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove everything
        self.play(*[FadeOut(mob) for mob in self.mobjects]) 