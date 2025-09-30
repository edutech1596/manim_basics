"""
Lesson 3: Text Basics

Learn how to add and animate text in Manim.

To render:
    manim -pql 03_text_basics.py SimpleText
"""

# Import all Manim classes and functions
from manim import *


class SimpleText(Scene):
    """
    Basic text creation and display.
    """
    
    def construct(self):
        # Create a text object with the string "Hello, Manim!"
        # Text() creates text using the system font
        text = Text("Hello, Manim!")
        
        # Write() is an animation that writes text letter by letter
        # It looks like someone is typing the text
        self.play(Write(text))
        
        # Wait for 2 seconds so we can read the text
        self.wait(2)
        
        # Fade out the text
        self.play(FadeOut(text))


class TextFormatting(Scene):
    """
    Different text sizes, colors, and fonts.
    
    To render:
        manim -pql 03_text_basics.py TextFormatting
    """
    
    def construct(self):
        # Create blue-colored text
        # color parameter changes the text color
        colored_text = Text("Colored Text", color=BLUE)
        
        # Move the text up by 2 units
        colored_text.shift(UP * 2)
        
        # Create large text
        # font_size=72 makes the text bigger (default is 48)
        big_text = Text("Big Text", font_size=72)
        
        # Create small text
        # font_size=24 makes the text smaller
        small_text = Text("Small Text", font_size=24)
        
        # Move the small text down by 2 units
        small_text.shift(DOWN * 2)
        
        # Show the colored text first
        self.play(Write(colored_text))
        
        # Show the big text second
        self.play(Write(big_text))
        
        # Show the small text third
        self.play(Write(small_text))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove all text objects from the screen
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class TextPositioning(Scene):
    """
    Positioning text in different locations.
    
    To render:
        manim -pql 03_text_basics.py TextPositioning
    """
    
    def construct(self):
        # Create a yellow title text
        title = Text("Title at Top", color=YELLOW)
        
        # to_edge(UP) moves the text to the top edge of the screen
        # This is different from shift() - it goes all the way to the edge
        title.to_edge(UP)
        
        # Create text for the center
        center_text = Text("Center Text")
        
        # move_to(ORIGIN) places the text at the exact center
        # ORIGIN is the point (0, 0, 0)
        center_text.move_to(ORIGIN)
        
        # Create green text for the bottom
        bottom_text = Text("Bottom Text", color=GREEN)
        
        # to_edge(DOWN) moves the text to the bottom edge
        bottom_text.to_edge(DOWN)
        
        # Write the title
        self.play(Write(title))
        
        # Write the center text
        self.play(Write(center_text))
        
        # Write the bottom text
        self.play(Write(bottom_text))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove all text
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class TextWithShapes(Scene):
    """
    Combining text with shapes.
    
    To render:
        manim -pql 03_text_basics.py TextWithShapes
    """
    
    def construct(self):
        # Create a blue circle with radius 1.5
        circle = Circle(radius=1.5, color=BLUE)
        
        # Fill the circle with blue at 30% opacity
        circle.set_fill(BLUE, opacity=0.3)
        
        # Create text that will label the circle
        label = Text("Circle", color=WHITE)
        
        # Draw the circle
        self.play(Create(circle))
        
        # Write the text (it starts at the center, overlapping the circle)
        self.play(Write(label))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Move the label to above the circle
        # .animate is used to animate property changes
        # next_to(circle, UP) positions the text above the circle
        self.play(label.animate.next_to(circle, UP))
        
        # Wait 2 seconds to see the final result
        self.wait(2)
        
        # Remove everything
        self.play(*[FadeOut(mob) for mob in self.mobjects]) 