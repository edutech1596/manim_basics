"""
Lesson 4 with Voice: Colors in Manim

All 4 scenes about colors and gradients with voice narration.

To render:
    python3 -m manim -pql 04_colors_voice.py ColorBasicsVoice
"""

from manim import *
from manim_voiceover import VoiceoverScene
from voiceover_config import configure_voiceover


class ColorBasicsVoice(VoiceoverScene):
    """Basic color usage with Manim's built-in colors."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
        circles = []
        
        for i, color in enumerate(colors):
            circle = Circle(radius=0.5, color=color)
            circle.set_fill(color, opacity=0.7)
            circle.shift(LEFT * 3 + RIGHT * i * 1.2)
            circles.append(circle)
        
        with self.voiceover(text="Manim has built-in colors: red, orange, yellow, green, blue, and purple.") as tracker:
            self.play(*[Create(c) for c in circles], run_time=tracker.duration)
        
        with self.voiceover(text="These colors can be used for any shape or object.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing the color palette.") as tracker:
            self.play(*[FadeOut(c) for c in circles], run_time=tracker.duration)


class ColorShadesVoice(VoiceoverScene):
    """Different shades of colors."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        red_shades = [RED_A, RED_B, RED_C, RED_D, RED_E]
        squares = []
        
        for i, shade in enumerate(red_shades):
            square = Square(side_length=1, color=shade)
            square.set_fill(shade, opacity=0.8)
            square.shift(LEFT * 2.5 + RIGHT * i * 1.3)
            squares.append(square)
        
        with self.voiceover(text="Manim provides five shades for each color, from lightest to darkest.") as tracker:
            self.play(*[Create(s) for s in squares], run_time=tracker.duration)
        
        with self.voiceover(text="Here are five shades of red.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Now let's see blue shades.") as tracker:
            self.play(*[FadeOut(s) for s in squares], run_time=tracker.duration)
        
        blue_shades = [BLUE_A, BLUE_B, BLUE_C, BLUE_D, BLUE_E]
        squares = []
        
        for i, shade in enumerate(blue_shades):
            square = Square(side_length=1, color=shade)
            square.set_fill(shade, opacity=0.8)
            square.shift(LEFT * 2.5 + RIGHT * i * 1.3)
            squares.append(square)
        
        with self.voiceover(text="Five shades of blue, from light to dark.") as tracker:
            self.play(*[Create(s) for s in squares], run_time=tracker.duration)
        
        with self.voiceover(text="Shades give us fine control over colors.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Clearing the scene.") as tracker:
            self.play(*[FadeOut(s) for s in squares], run_time=tracker.duration)


class CustomColorsVoice(VoiceoverScene):
    """Creating custom colors with hex codes."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        custom_color1 = "#FF6B6B"
        circle1 = Circle(radius=1, color=custom_color1)
        circle1.set_fill(custom_color1, opacity=0.5)
        circle1.shift(LEFT * 2)
        
        custom_color2 = "#4ECDC4"
        circle2 = Circle(radius=1, color=custom_color2)
        circle2.set_fill(custom_color2, opacity=0.5)
        
        custom_color3 = "#95E1D3"
        circle3 = Circle(radius=1, color=custom_color3)
        circle3.set_fill(custom_color3, opacity=0.5)
        circle3.shift(RIGHT * 2)
        
        with self.voiceover(text="We can create custom colors using hex codes.") as tracker:
            self.play(Create(circle1), Create(circle2), Create(circle3), run_time=tracker.duration)
        
        with self.voiceover(text="These are custom coral, turquoise, and mint colors.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Custom colors let us match any color scheme.") as tracker:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=tracker.duration)


class GradientColorsVoice(VoiceoverScene):
    """Creating gradients and color transitions."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        rect = Rectangle(width=6, height=3)
        rect.set_fill([RED, YELLOW, GREEN], opacity=0.8)
        
        with self.voiceover(text="We can create smooth color gradients by blending multiple colors.") as tracker:
            self.play(Create(rect), run_time=tracker.duration)
        
        with self.voiceover(text="This gradient transitions from red to yellow to green.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Gradients add visual appeal to shapes.") as tracker:
            self.play(FadeOut(rect), run_time=tracker.duration)


