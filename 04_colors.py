"""
Lesson 4: Colors in Manim

Learn about colors and gradients in Manim.

To render:
    manim -pql 04_colors.py ColorBasics
"""

# Import all Manim classes and functions
from manim import *


class ColorBasics(Scene):
    """
    Basic color usage with Manim's built-in colors.
    """
    
    def construct(self):
        # Create a list of built-in Manim colors
        # These are predefined constants you can use anywhere
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
        
        # Create an empty list to store our circles
        circles = []
        
        # Loop through each color using enumerate
        # enumerate gives us both the index (i) and the value (color)
        for i, color in enumerate(colors):
            # Create a circle with the current color
            # radius=0.5 makes small circles
            circle = Circle(radius=0.5, color=color)
            
            # Fill the circle with the same color at 70% opacity
            circle.set_fill(color, opacity=0.7)
            
            # Position each circle horizontally
            # Start at LEFT * 3, then move right by i * 1.2 for each circle
            circle.shift(LEFT * 3 + RIGHT * i * 1.2)
            
            # Add this circle to our list
            circles.append(circle)
        
        # Animate all circles appearing at once
        # *[Create(c) for c in circles] creates a Create animation for each circle
        # The * unpacks the list so each animation is a separate argument
        self.play(*[Create(c) for c in circles])
        
        # Wait 2 seconds to view the colors
        self.wait(2)
        
        # Remove all circles at once
        self.play(*[FadeOut(c) for c in circles])


class ColorShades(Scene):
    """
    Different shades of colors.
    
    To render:
        manim -pql 04_colors.py ColorShades
    """
    
    def construct(self):
        # Manim provides 5 shades for many colors (A=lightest, E=darkest)
        # RED_A is the lightest red, RED_E is the darkest
        red_shades = [RED_A, RED_B, RED_C, RED_D, RED_E]
        
        # Create an empty list for the squares
        squares = []
        
        # Loop through each shade with its index
        for i, shade in enumerate(red_shades):
            # Create a square for this shade
            square = Square(side_length=1, color=shade)
            
            # Fill the square with this shade at 80% opacity
            square.set_fill(shade, opacity=0.8)
            
            # Position squares in a row
            # Start at LEFT * 2.5, move right by i * 1.3 for each square
            square.shift(LEFT * 2.5 + RIGHT * i * 1.3)
            
            # Add to our list
            squares.append(square)
        
        # Show all red shade squares
        self.play(*[Create(s) for s in squares])
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove the red squares
        self.play(*[FadeOut(s) for s in squares])
        
        # Now do the same with blue shades
        # BLUE_A through BLUE_E
        blue_shades = [BLUE_A, BLUE_B, BLUE_C, BLUE_D, BLUE_E]
        
        # Reset the squares list
        squares = []
        
        # Create squares for blue shades
        for i, shade in enumerate(blue_shades):
            square = Square(side_length=1, color=shade)
            square.set_fill(shade, opacity=0.8)
            square.shift(LEFT * 2.5 + RIGHT * i * 1.3)
            squares.append(square)
        
        # Show all blue shade squares
        self.play(*[Create(s) for s in squares])
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove the blue squares
        self.play(*[FadeOut(s) for s in squares])


class CustomColors(Scene):
    """
    Creating custom colors with hex codes or RGB.
    
    To render:
        manim -pql 04_colors.py CustomColors
    """
    
    def construct(self):
        # Define a custom color using hex code (like in web design)
        # Hex codes start with # followed by 6 characters
        # Format: #RRGGBB (Red, Green, Blue in hexadecimal)
        custom_color1 = "#FF6B6B"
        
        # Create a circle with this custom color
        circle1 = Circle(radius=1, color=custom_color1)
        
        # Fill with the same custom color
        circle1.set_fill(custom_color1, opacity=0.5)
        
        # Move left
        circle1.shift(LEFT * 2)
        
        # Another custom color (turquoise)
        custom_color2 = "#4ECDC4"
        circle2 = Circle(radius=1, color=custom_color2)
        circle2.set_fill(custom_color2, opacity=0.5)
        # This one stays at center
        
        # Another custom color (mint green)
        custom_color3 = "#95E1D3"
        circle3 = Circle(radius=1, color=custom_color3)
        circle3.set_fill(custom_color3, opacity=0.5)
        
        # Move right
        circle3.shift(RIGHT * 2)
        
        # Show all three custom colored circles
        self.play(Create(circle1), Create(circle2), Create(circle3))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove all circles
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class GradientColors(Scene):
    """
    Creating gradients and color transitions.
    
    To render:
        manim -pql 04_colors.py GradientColors
    """
    
    def construct(self):
        # Create a rectangle
        rect = Rectangle(width=6, height=3)
        
        # set_fill with a list of colors creates a gradient
        # The colors blend from RED to YELLOW to GREEN
        # opacity=0.8 applies to the entire gradient
        rect.set_fill([RED, YELLOW, GREEN], opacity=0.8)
        
        # Show the gradient rectangle
        self.play(Create(rect))
        
        # Wait 2 seconds to admire the gradient
        self.wait(2)
        
        # Remove the rectangle
        self.play(FadeOut(rect)) 