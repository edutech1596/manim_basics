"""
Lesson 2 with Voice: Mathematical Equations with Narration

Learn how to create and transform equations with synchronized voice explanations.

To render:
    python3 -m manim -pql 02_equations_voice.py SimpleEquationVoice
"""

from manim import *
from manim_voiceover import VoiceoverScene
from voiceover_config import configure_voiceover


class SimpleEquationVoice(VoiceoverScene):
    """
    Create a simple mathematical equation with voice explanation.
    """
    
    def construct(self):
        # Configure voice backend
        configure_voiceover(self, backend="gtts", lang="en")
        
        # Create the Pythagorean theorem equation
        equation = MathTex("a^2 + b^2 = c^2")
        equation.scale(1.5)
        
        # Narration: Introduce the equation
        with self.voiceover(text=(
            "This is the famous Pythagorean theorem. "
            "It relates the sides of a right triangle."
        )) as tracker:
            self.play(Write(equation), run_time=tracker.duration)
        
        # Narration: Explain the parts
        with self.voiceover(text=(
            "A squared plus B squared equals C squared. "
            "Where C is the longest side, called the hypotenuse."
        )) as tracker:
            self.wait(tracker.duration)
        
        # Narration: Conclusion
        with self.voiceover(text="This theorem has been known for thousands of years.") as tracker:
            self.play(FadeOut(equation), run_time=tracker.duration)


class TransformEquationVoice(VoiceoverScene):
    """
    Transform one equation into another with narration.
    """
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        # Create equations
        eq1 = MathTex("x^2 + 2x + 1")
        eq2 = MathTex("(x + 1)^2")
        
        # Narration: Show first equation
        with self.voiceover(text="Let's start with this quadratic expression.") as tracker:
            self.play(Write(eq1), run_time=tracker.duration)
        
        # Narration: Explain transformation
        with self.voiceover(text=(
            "We can factor this expression into a perfect square. "
            "Watch how the equation transforms."
        )) as tracker:
            self.play(ReplacementTransform(eq1, eq2), run_time=tracker.duration)
        
        # Narration: Final form
        with self.voiceover(text="This is the factored form: X plus one, squared.") as tracker:
            self.wait(tracker.duration)
        
        # Narration: Cleanup
        with self.voiceover(text="And that completes our transformation.") as tracker:
            self.play(FadeOut(eq2), run_time=tracker.duration)


class ColoredEquationVoice(VoiceoverScene):
    """
    Highlight different parts of an equation with color and voice.
    """
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        # Create equation with colored parts
        equation = MathTex("E", "=", "m", "c^2")
        equation.scale(2)
        
        # Narration: Introduce Einstein's equation
        with self.voiceover(text="This is Einstein's famous equation: E equals M C squared.") as tracker:
            self.play(Write(equation), run_time=tracker.duration)
        
        # Narration: Explain E (Energy)
        with self.voiceover(text="E represents energy.") as tracker:
            self.play(equation[0].animate.set_color(YELLOW), run_time=tracker.duration)
        
        # Narration: Explain m (mass)
        with self.voiceover(text="M is mass.") as tracker:
            self.play(equation[2].animate.set_color(BLUE), run_time=tracker.duration)
        
        # Narration: Explain c^2 (speed of light squared)
        with self.voiceover(text="And C squared is the speed of light, squared.") as tracker:
            self.play(equation[3].animate.set_color(RED), run_time=tracker.duration)
        
        # Narration: Conclusion
        with self.voiceover(text=(
            "This equation shows that mass and energy are interchangeable. "
            "A revolutionary discovery in physics."
        )) as tracker:
            self.wait(tracker.duration)
        
        # Narration: Fade out
        with self.voiceover(text="Let's clear the screen.") as tracker:
            self.play(FadeOut(equation), run_time=tracker.duration)


