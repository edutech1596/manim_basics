"""
Lesson 8: Timing and Speed Control

Learn how to control animation timing, speed, and delays.

To render:
    manim -pql 08_timing.py RunTime
"""

# Import all Manim functionality
from manim import *


class RunTime(Scene):
    """
    Controlling animation speed with run_time.
    """
    
    def construct(self):
        # run_time controls how long an animation takes
        # Create a blue circle at the top
        circle1 = Circle(color=BLUE).shift(UP * 2)
        
        # Fast animation - only 0.5 seconds
        # run_time=0.5 makes it twice as fast as normal
        self.play(Create(circle1), run_time=0.5)
        
        # Create a green circle in the middle
        circle2 = Circle(color=GREEN)
        
        # Normal speed animation - 1 second (this is the default)
        self.play(Create(circle2), run_time=1)
        
        # Create a red circle at the bottom
        circle3 = Circle(color=RED).shift(DOWN * 2)
        
        # Slow animation - takes 3 seconds
        # run_time=3 makes it three times slower than normal
        self.play(Create(circle3), run_time=3)
        
        # Wait 1 second
        self.wait(1)
        
        # Remove all circles at once
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class WaitTiming(Scene):
    """
    Using wait() to add pauses.
    
    To render:
        manim -pql 08_timing.py WaitTiming
    """
    
    def construct(self):
        # wait() pauses the animation for a specified time
        # Create a blue circle
        circle = Circle(color=BLUE)
        
        # Show the circle
        self.play(Create(circle))
        
        # Wait 2 seconds - gives viewer time to see the circle
        # The number in wait() is the number of seconds to pause
        self.wait(2)
        
        # Change the circle's color to red
        # .animate allows us to animate property changes
        self.play(circle.animate.set_color(RED))
        
        # Wait 1 second - time to notice the color change
        self.wait(1)
        
        # Move the circle to the right
        self.play(circle.animate.shift(RIGHT * 2))
        
        # Wait before cleanup
        self.wait(1)
        
        # Remove the circle
        self.play(FadeOut(circle))


class SequentialTiming(Scene):
    """
    Animations happening one after another.
    
    To render:
        manim -pql 08_timing.py SequentialTiming
    """
    
    def construct(self):
        # Sequential = one after another
        # Each self.play() waits for the previous one to finish
        
        # Create three circles at different positions
        circle1 = Circle(color=RED).shift(LEFT * 2)
        circle2 = Circle(color=GREEN)
        circle3 = Circle(color=BLUE).shift(RIGHT * 2)
        
        # Animate them one by one (sequentially)
        # First circle appears
        self.play(Create(circle1))
        # Then second circle appears (after first is done)
        self.play(Create(circle2))
        # Then third circle appears (after second is done)
        self.play(Create(circle3))
        
        # Wait 1 second
        self.wait(1)
        
        # Move them up one by one (sequentially)
        # circle1 moves first
        self.play(circle1.animate.shift(UP))
        # circle2 moves after circle1 is done
        self.play(circle2.animate.shift(UP))
        # circle3 moves after circle2 is done
        self.play(circle3.animate.shift(UP))
        
        # Wait 1 second
        self.wait(1)
        
        # Remove all circles
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class SimultaneousTiming(Scene):
    """
    Animations happening at the same time.
    
    To render:
        manim -pql 08_timing.py SimultaneousTiming
    """
    
    def construct(self):
        # Simultaneous = at the same time
        # Pass multiple animations to one self.play() to run them together
        
        # Create three circles
        circle1 = Circle(color=RED).shift(LEFT * 2)
        circle2 = Circle(color=GREEN)
        circle3 = Circle(color=BLUE).shift(RIGHT * 2)
        
        # Animate all at once (simultaneously)
        # All three circles appear at the same time
        self.play(
            Create(circle1),
            Create(circle2),
            Create(circle3),
        )
        
        # Wait 1 second
        self.wait(1)
        
        # Move all at once (simultaneously)
        # All three circles move up at the same time
        self.play(
            circle1.animate.shift(UP),
            circle2.animate.shift(UP),
            circle3.animate.shift(UP),
        )
        
        # Wait 1 second
        self.wait(1)
        
        # Remove all circles together
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class RateFunction(Scene):
    """
    Using rate functions to control animation curves.
    
    To render:
        manim -pql 08_timing.py RateFunction
    """
    
    def construct(self):
        # rate_func controls HOW the animation progresses over time
        
        # Linear rate function (constant speed)
        # Create a blue circle at top-left
        circle1 = Circle(radius=0.5, color=BLUE).shift(UP * 2 + LEFT * 5)
        
        # Add it to the scene (without animation)
        self.add(circle1)
        
        # Move with linear rate (constant speed throughout)
        # rate_func=linear means steady speed from start to finish
        self.play(
            circle1.animate.shift(RIGHT * 10),
            rate_func=linear,
            run_time=2
        )
        
        # Short pause
        self.wait(0.5)
        
        # Smooth rate function (ease in and out)
        # Create a green circle at center-left
        circle2 = Circle(radius=0.5, color=GREEN).shift(LEFT * 5)
        
        # Add it to the scene
        self.add(circle2)
        
        # Move with smooth rate (slow start, fast middle, slow end)
        # rate_func=smooth creates a natural-looking motion
        self.play(
            circle2.animate.shift(RIGHT * 10),
            rate_func=smooth,
            run_time=2
        )
        
        # Short pause
        self.wait(0.5)
        
        # Rush into rate function (slow start, fast end)
        # Create a red circle at bottom-left
        circle3 = Circle(radius=0.5, color=RED).shift(DOWN * 2 + LEFT * 5)
        
        # Add it to the scene
        self.add(circle3)
        
        # Move with rush_into rate (accelerates toward the end)
        # rate_func=rush_into starts slow and speeds up
        self.play(
            circle3.animate.shift(RIGHT * 10),
            rate_func=rush_into,
            run_time=2
        )
        
        # Wait 1 second
        self.wait(1)
        
        # Remove all circles
        self.play(*[FadeOut(mob) for mob in self.mobjects]) 