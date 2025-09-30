"""
Lesson 2: Basic Shapes

Learn about different geometric shapes available in Manim.

To render:
    manim -pql 02_basic_shapes.py ShapeGallery
"""

# Import all classes and functions from Manim
from manim import *


class ShapeGallery(Scene):
    """
    Display various basic shapes that Manim provides.
    """
    
    def construct(self):
        # Create a circle with radius 0.5 and red color
        circle = Circle(radius=0.5, color=RED)
        
        # Create a square with side length 1 and blue color
        square = Square(side_length=1, color=BLUE)
        
        # Create a triangle with green color
        # Default size is automatic
        triangle = Triangle(color=GREEN)
        
        # Position the circle 3 units to the left
        # LEFT is a vector pointing left
        circle.shift(LEFT * 3)
        
        # Position the square at the origin (center of screen)
        # ORIGIN is (0, 0, 0) in 3D coordinates
        square.shift(ORIGIN)
        
        # Position the triangle 3 units to the right
        triangle.shift(RIGHT * 3)
        
        # Fill the circle with red color at 50% opacity
        # opacity ranges from 0 (transparent) to 1 (solid)
        circle.set_fill(RED, opacity=0.5)
        
        # Fill the square with blue color at 50% opacity
        square.set_fill(BLUE, opacity=0.5)
        
        # Fill the triangle with green color at 50% opacity
        triangle.set_fill(GREEN, opacity=0.5)
        
        # Animate all three shapes appearing at once
        # The comma separates multiple animations
        self.play(
            Create(circle),
            Create(square),
            Create(triangle),
        )
        
        # Wait for 2 seconds to view the shapes
        self.wait(2)
        
        # Remove all three shapes at once
        self.play(
            FadeOut(circle),
            FadeOut(square),
            FadeOut(triangle),
        )


class MoreShapes(Scene):
    """
    More shapes: rectangles, ellipses, and polygons.
    
    To render:
        manim -pql 02_basic_shapes.py MoreShapes
    """
    
    def construct(self):
        # Create a rectangle
        # width=4 means 4 units wide
        # height=2 means 2 units tall
        rectangle = Rectangle(width=4, height=2, color=YELLOW)
        
        # Move the rectangle up by 2 units
        # UP is a vector pointing upward
        rectangle.shift(UP * 2)
        
        # Create an ellipse (oval shape)
        # width=3 is the horizontal diameter
        # height=1.5 is the vertical diameter
        ellipse = Ellipse(width=3, height=1.5, color=PURPLE)
        
        # Create a regular polygon (hexagon in this case)
        # n=6 means 6 sides (hexagon)
        hexagon = RegularPolygon(n=6, color=ORANGE)
        
        # Move the hexagon down by 2 units
        hexagon.shift(DOWN * 2)
        
        # Fill the rectangle with yellow at 30% opacity
        rectangle.set_fill(YELLOW, opacity=0.3)
        
        # Fill the ellipse with purple at 30% opacity
        ellipse.set_fill(PURPLE, opacity=0.3)
        
        # Fill the hexagon with orange at 30% opacity
        hexagon.set_fill(ORANGE, opacity=0.3)
        
        # Show the rectangle first
        self.play(Create(rectangle))
        
        # Then show the ellipse
        self.play(Create(ellipse))
        
        # Finally show the hexagon
        self.play(Create(hexagon))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove all shapes at once
        self.play(
            FadeOut(rectangle),
            FadeOut(ellipse),
            FadeOut(hexagon),
        )


class ShapeProperties(Scene):
    """
    Exploring shape properties: stroke, fill, and size.
    
    To render:
        manim -pql 02_basic_shapes.py ShapeProperties
    """
    
    def construct(self):
        # Create a circle with thick outline and no fill
        # stroke_width=8 makes the outline very thick
        circle1 = Circle(radius=1, color=BLUE, stroke_width=8)
        
        # Move it 3 units to the left
        circle1.shift(LEFT * 3)
        
        # Create a circle with thin outline and 70% fill
        circle2 = Circle(radius=1, color=GREEN, stroke_width=2)
        
        # Add a green fill at 70% opacity
        circle2.set_fill(GREEN, opacity=0.7)
        
        # Keep it at the center
        circle2.shift(ORIGIN)
        
        # Create a circle with no outline
        # stroke_width=0 means no outline visible
        circle3 = Circle(radius=1, stroke_width=0)
        
        # Fill it completely (100% opacity) with red
        circle3.set_fill(RED, opacity=1)
        
        # Move it 3 units to the right
        circle3.shift(RIGHT * 3)
        
        # Show all three circles at the same time
        self.play(
            Create(circle1),
            Create(circle2),
            Create(circle3),
        )
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove all objects currently on screen
        # self.mobjects is a list of all objects (mobjects = mathematical objects)
        # *[FadeOut(mob) for mob in self.mobjects] creates FadeOut for each object
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class Lines(Scene):
    """
    Working with lines, arrows, and paths.
    
    To render:
        manim -pql 02_basic_shapes.py Lines
    """
    
    def construct(self):
        # Create a simple line
        # start: where the line begins (2 units left)
        # end: where the line ends (2 units right)
        line = Line(start=LEFT * 2, end=RIGHT * 2, color=WHITE)
        
        # Create an arrow pointing from left to right
        # The arrow will be 1 unit down from the line
        # DOWN is a vector pointing downward
        arrow = Arrow(start=LEFT * 2 + DOWN, end=RIGHT * 2 + DOWN, color=YELLOW)
        
        # Create a double-headed arrow
        # This has arrowheads on both ends
        # It will be 2 units down
        double_arrow = DoubleArrow(
            start=LEFT * 2 + DOWN * 2,
            end=RIGHT * 2 + DOWN * 2,
            color=GREEN
        )
        
        # Draw the line first
        self.play(Create(line))
        
        # Then draw the arrow
        self.play(Create(arrow))
        
        # Then draw the double arrow
        self.play(Create(double_arrow))
        
        # Wait 2 seconds to view them
        self.wait(2)
        
        # Remove all objects from the screen
        self.play(*[FadeOut(mob) for mob in self.mobjects]) 