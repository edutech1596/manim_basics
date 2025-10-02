"""
Lesson 12 with Voice: Mathematical Equations with LaTeX

All 6 scenes about creating beautiful mathematical equations with voice.

To render:
    python3 -m manim -pql 12_equations_voice.py SimpleEquationVoice
"""

from manim import *
from manim_voiceover import VoiceoverScene
from voiceover_config import configure_voiceover


class SimpleEquationVoice(VoiceoverScene):
    """Creating basic mathematical equations."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        equation = MathTex("E = mc^2")
        
        with self.voiceover(text="MathTex creates mathematical equations using LaTeX syntax. This is Einstein's famous equation.") as tracker:
            self.play(Write(equation), run_time=tracker.duration)
        
        with self.voiceover(text="E equals M C squared.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="LaTeX makes equations look professional.") as tracker:
            self.play(FadeOut(equation), run_time=tracker.duration)


class MultipleEquationsVoice(VoiceoverScene):
    """Working with multiple equations."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        eq1 = MathTex("a^2 + b^2 = c^2")
        eq1.shift(UP * 2)
        
        eq2 = MathTex(r"\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}")
        
        eq3 = MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}")
        eq3.shift(DOWN * 2)
        
        with self.voiceover(text="Here's the Pythagorean theorem at the top.") as tracker:
            self.play(Write(eq1), run_time=tracker.duration)
        
        with self.voiceover(text="The Gaussian integral in the middle.") as tracker:
            self.play(Write(eq2), run_time=tracker.duration)
        
        with self.voiceover(text="And the Basel problem solution at the bottom.") as tracker:
            self.play(Write(eq3), run_time=tracker.duration)
        
        with self.voiceover(text="Multiple equations can be displayed together.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing all equations.") as tracker:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=tracker.duration)


class ColoredEquationVoice(VoiceoverScene):
    """Adding colors to equations."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        equation = MathTex(
            "x", "=", "{-b", r"\pm", r"\sqrt{b^2 - 4ac}", r"\over", "2a}"
        )
        
        equation[0].set_color(YELLOW)
        equation[2].set_color(RED)
        equation[4].set_color(BLUE)
        equation[6].set_color(GREEN)
        
        with self.voiceover(text="This is the quadratic formula with color-coded parts for clarity.") as tracker:
            self.play(Write(equation), run_time=tracker.duration)
        
        with self.voiceover(text="Different colors highlight different components: yellow X, red negative B, blue square root, and green denominator.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Colors make complex equations easier to understand.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing the equation.") as tracker:
            self.play(FadeOut(equation), run_time=tracker.duration)


class TransformEquationVoice(VoiceoverScene):
    """Transforming one equation into another."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        eq1 = MathTex("x^2 + 2x + 1")
        
        with self.voiceover(text="We start with the expanded form: X squared plus two X plus one.") as tracker:
            self.play(Write(eq1), run_time=tracker.duration)
        
        eq2 = MathTex("(x + 1)^2")
        
        with self.voiceover(text="Watch it transform into the factored form: X plus one, squared.") as tracker:
            self.play(Transform(eq1, eq2), run_time=tracker.duration)
        
        with self.voiceover(text="This shows algebraic simplification visually.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing the equation.") as tracker:
            self.play(FadeOut(eq1), run_time=tracker.duration)


class EquationWithTextVoice(VoiceoverScene):
    """Combining equations with explanatory text."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        title = Text("The Pythagorean Theorem", color=YELLOW)
        title.to_edge(UP)
        
        equation = MathTex("a^2 + b^2 = c^2")
        equation.scale(1.5)
        
        description = Text("For any right triangle", font_size=24)
        description.next_to(equation, DOWN, buff=1)
        
        with self.voiceover(text="Here's a title explaining what theorem we're showing.") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        with self.voiceover(text="The equation itself, nicely sized.") as tracker:
            self.play(Write(equation), run_time=tracker.duration)
        
        with self.voiceover(text="And a description providing context below.") as tracker:
            self.play(Write(description), run_time=tracker.duration)
        
        with self.voiceover(text="Combining text and equations creates complete explanations.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Clearing the screen.") as tracker:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=tracker.duration)


class EquationArrayVoice(VoiceoverScene):
    """Creating aligned equations."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        equations = VGroup(
            MathTex("f(x) = x^2"),
            MathTex("f'(x) = 2x"),
            MathTex("f''(x) = 2"),
        )
        
        equations.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        with self.voiceover(text="Here's a sequence showing a function and its derivatives. First, F of X equals X squared.") as tracker:
            self.play(Write(equations[0]), run_time=tracker.duration)
        
        with self.voiceover(text="The first derivative: F prime of X equals two X.") as tracker:
            self.play(Write(equations[1]), run_time=tracker.duration)
        
        with self.voiceover(text="The second derivative: F double prime of X equals two.") as tracker:
            self.play(Write(equations[2]), run_time=tracker.duration)
        
        with self.voiceover(text="Aligned equations show mathematical progressions clearly.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing all equations.") as tracker:
            self.play(FadeOut(equations), run_time=tracker.duration)


