"""
Lesson 7: Movement Animations

Learn how to move objects around the scene.

To render:
    manim -pql 07_movement.py ShiftMovement
"""

# Import all Manim functionality
from manim import *


class ShiftMovement(Scene):
    """
    Moving objects with shift.
    """
    
    def construct(self):
        # shift() moves an object by a certain amount
        # Create a blue circle at the center
        circle = Circle(color=BLUE)
        
        # Fill it
        circle.set_fill(BLUE, opacity=0.5)
        
        # Show the circle
        self.play(Create(circle))
        
        # Wait 1 second
        self.wait(1)
        
        # Move the circle 2 units to the right
        # .animate makes the movement animated (smooth)
        # WITHOUT .animate, it would just jump instantly
        self.play(circle.animate.shift(RIGHT * 2))
        
        # Short pause
        self.wait(0.5)
        
        # Move up by 2 units
        # UP is a vector pointing upward
        self.play(circle.animate.shift(UP * 2))
        
        # Short pause
        self.wait(0.5)
        
        # Move left by 4 units
        # This will move it past its starting position
        self.play(circle.animate.shift(LEFT * 4))
        
        # Short pause
        self.wait(0.5)
        
        # Move down by 2 units
        # DOWN is a vector pointing downward
        self.play(circle.animate.shift(DOWN * 2))
        
        # Wait 1 second
        self.wait(1)
        
        # Remove the circle
        self.play(FadeOut(circle))


class MoveToPosition(Scene):
    """
    Moving objects to specific positions.
    
    To render:
        manim -pql 07_movement.py MoveToPosition
    """
    
    def construct(self):
        # move_to() moves an object to an absolute position
        # Create a green square
        square = Square(color=GREEN)
        
        # Fill it
        square.set_fill(GREEN, opacity=0.5)
        
        # Show the square at center
        self.play(Create(square))
        
        # Wait 1 second
        self.wait(1)
        
        # Move to a specific position: top-left
        # UP * 2 means 2 units up
        # LEFT * 3 means 3 units left
        # + combines these vectors
        self.play(square.animate.move_to(UP * 2 + LEFT * 3))
        
        # Short pause
        self.wait(0.5)
        
        # Move to bottom-right
        # DOWN * 2 + RIGHT * 3
        self.play(square.animate.move_to(DOWN * 2 + RIGHT * 3))
        
        # Short pause
        self.wait(0.5)
        
        # Move back to center
        # ORIGIN is the center point (0, 0, 0)
        self.play(square.animate.move_to(ORIGIN))
        
        # Wait 1 second
        self.wait(1)
        
        # Remove the square
        self.play(FadeOut(square))


class ToEdgeMovement(Scene):
    """
    Moving objects to edges of the screen.
    
    To render:
        manim -pql 07_movement.py ToEdgeMovement
    """
    
    def construct(self):
        # to_edge() moves an object to the edge of the screen
        # Create a red circle
        circle = Circle(color=RED)
        
        # Fill it
        circle.set_fill(RED, opacity=0.5)
        
        # Show the circle
        self.play(Create(circle))
        
        # Wait 1 second
        self.wait(1)
        
        # Move to the top edge
        # to_edge(UP) moves it all the way to the top
        self.play(circle.animate.to_edge(UP))
        
        # Short pause
        self.wait(0.5)
        
        # Move to the right edge
        self.play(circle.animate.to_edge(RIGHT))
        
        # Short pause
        self.wait(0.5)
        
        # Move to the bottom edge
        self.play(circle.animate.to_edge(DOWN))
        
        # Short pause
        self.wait(0.5)
        
        # Move to the left edge
        self.play(circle.animate.to_edge(LEFT))
        
        # Wait 1 second
        self.wait(1)
        
        # Remove the circle
        self.play(FadeOut(circle))


class NextToPosition(Scene):
    """
    Positioning objects next to other objects.
    
    To render:
        manim -pql 07_movement.py NextToPosition
    """
    
    def construct(self):
        # next_to() positions an object relative to another object
        # Create a yellow square in the center
        square = Square(color=YELLOW)
        
        # Fill it
        square.set_fill(YELLOW, opacity=0.5)
        
        # Show the square
        self.play(Create(square))
        
        # Wait 1 second
        self.wait(1)
        
        # Create four circles to surround the square
        # Blue circle - will be positioned above the square
        circle_up = Circle(radius=0.5, color=BLUE)
        circle_up.set_fill(BLUE, opacity=0.5)
        # next_to(square, UP) puts it directly above the square
        circle_up.next_to(square, UP)
        
        # Green circle - will be below the square
        circle_down = Circle(radius=0.5, color=GREEN)
        circle_down.set_fill(GREEN, opacity=0.5)
        # next_to(square, DOWN) puts it directly below
        circle_down.next_to(square, DOWN)
        
        # Red circle - will be left of the square
        circle_left = Circle(radius=0.5, color=RED)
        circle_left.set_fill(RED, opacity=0.5)
        # next_to(square, LEFT) puts it to the left
        circle_left.next_to(square, LEFT)
        
        # Purple circle - will be right of the square
        circle_right = Circle(radius=0.5, color=PURPLE)
        circle_right.set_fill(PURPLE, opacity=0.5)
        # next_to(square, RIGHT) puts it to the right
        circle_right.next_to(square, RIGHT)
        
        # Show all four circles at once
        self.play(
            Create(circle_up),
            Create(circle_down),
            Create(circle_left),
            Create(circle_right),
        )
        
        # Wait 2 seconds to view the arrangement
        self.wait(2)
        
        # Remove all objects
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class RotationMovement(Scene):
    """
    Rotating objects.
    
    To render:
        manim -pql 07_movement.py RotationMovement
    """
    
    def construct(self):
        # Rotate() spins an object around its center
        # Create an orange square
        square = Square(color=ORANGE)
        
        # Fill it
        square.set_fill(ORANGE, opacity=0.5)
        
        # Show the square
        self.play(Create(square))
        
        # Wait 1 second
        self.wait(1)
        
        # Rotate by 90 degrees (PI/2 radians)
        # In Manim, angles are in radians, not degrees
        # PI/2 radians = 90 degrees
        self.play(Rotate(square, angle=PI/2))
        
        # Short pause
        self.wait(0.5)
        
        # Rotate another 90 degrees
        # The square is now rotated 180 degrees from start
        self.play(Rotate(square, angle=PI/2))
        
        # Short pause
        self.wait(0.5)
        
        # Rotate a full circle
        # 2*PI radians = 360 degrees = full rotation
        self.play(Rotate(square, angle=2*PI))
        
        # Wait 1 second
        self.wait(1)
        
        # Remove the square
        self.play(FadeOut(square)) 