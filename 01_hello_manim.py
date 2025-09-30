"""
Lesson 1: Hello Manim - Your First Animation

This is your first Manim scene! We'll create a simple circle and animate it.

To render this:
    manim -pql 01_hello_manim.py HelloManim

Breakdown:
- -p : play the video after rendering
- -ql : low quality (faster for learning)
- 01_hello_manim.py : this file
- HelloManim : the scene class name
"""

# Import everything from the manim library
# The * means "import all classes and functions"
from manim import *


# Define a new class called HelloManim
# It inherits from Scene (the base class for all animations)
class HelloManim(Scene):
    """
    Scene is the base class for all Manim animations.
    The construct() method is where you define what happens in the scene.
    """
    
    # The construct method is required - this is where your animation code goes
    def construct(self):
        # Create a circle object
        # Circle() creates a default circle (radius 1, white color)
        circle = Circle()
        
        # self.play() runs an animation
        # Create() is an animation that draws the object on screen
        # This will draw the circle from start to finish
        self.play(Create(circle))
        
        # self.wait() pauses the animation
        # The number (1) is how many seconds to wait
        self.wait(1)
        
        # FadeOut() is an animation that makes the object disappear
        # The circle will gradually fade away
        self.play(FadeOut(circle))
        
        # Wait another second before the animation ends
        self.wait(1)


class ColorfulCircle(Scene):
    """
    Let's make it more interesting with color and size!
    
    To render this:
        manim -pql 01_hello_manim.py ColorfulCircle
    """
    
    def construct(self):
        # Create a circle with custom properties:
        # - radius=2 makes it bigger (default is 1)
        # - color=BLUE sets the outline color to blue
        # BLUE is a built-in color constant in Manim
        circle = Circle(radius=2, color=BLUE)
        
        # set_fill() fills the inside of the circle
        # First parameter: color to fill with (BLUE)
        # opacity parameter: 0.5 means 50% transparent (0=invisible, 1=solid)
        circle.set_fill(BLUE, opacity=0.5)
        
        # Play the Create animation
        # run_time=2 means the animation takes 2 seconds (default is 1)
        self.play(Create(circle), run_time=2)
        
        # Pause for 1 second
        self.wait(1)
        
        # Fade out the circle
        self.play(FadeOut(circle))
        
        # Final pause
        self.wait(1)


class MultipleAnimations(Scene):
    """
    Multiple circles with different animations!
    
    To render this:
        manim -pql 01_hello_manim.py MultipleAnimations
    """
    
    def construct(self):
        # Create the first circle
        # .shift(LEFT * 2) moves it 2 units to the left
        # LEFT is a built-in direction vector in Manim
        circle1 = Circle(radius=1, color=RED).shift(LEFT * 2)
        
        # Create the second circle at the center (no shift)
        circle2 = Circle(radius=1, color=GREEN)
        
        # Create the third circle
        # .shift(RIGHT * 2) moves it 2 units to the right
        circle3 = Circle(radius=1, color=BLUE).shift(RIGHT * 2)
        
        # Fill each circle with its respective color
        # opacity=0.5 makes them semi-transparent
        circle1.set_fill(RED, opacity=0.5)
        circle2.set_fill(GREEN, opacity=0.5)
        circle3.set_fill(BLUE, opacity=0.5)
        
        # Animate all three circles at the same time
        # When you pass multiple animations to self.play(), they run together
        # run_time=2 applies to all animations in this play() call
        self.play(
            Create(circle1),
            Create(circle2),
            Create(circle3),
            run_time=2
        )
        
        # Pause for 1 second
        self.wait(1)
        
        # Fade them out one by one (sequential animations)
        # Each self.play() waits for the previous one to finish
        self.play(FadeOut(circle1))
        self.play(FadeOut(circle2))
        self.play(FadeOut(circle3))
        
        # Final pause
        self.wait(1) 