"""
Lesson 12: Mathematical Equations with LaTeX

Learn to create beautiful mathematical equations using MathTex.

To render:
    manim -pql 12_equations.py SimpleEquation
"""

# Import all Manim functionality
from manim import *


class SimpleEquation(Scene):
    """
    Creating basic mathematical equations.
    """
    
    def construct(self):
        # MathTex creates mathematical equations using LaTeX syntax
        # LaTeX is a typesetting system used for mathematical notation
        # The text inside quotes is LaTeX code
        equation = MathTex("E = mc^2")
        # "E = mc^2" becomes Einstein's famous equation
        # ^ means superscript (raised number)
        
        # Write the equation
        self.play(Write(equation))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove the equation
        self.play(FadeOut(equation))


class MultipleEquations(Scene):
    """
    Working with multiple equations.
    
    To render:
        manim -pql 12_equations.py MultipleEquations
    """
    
    def construct(self):
        # Create several mathematical equations
        
        # Pythagorean theorem
        # a^2 means a-squared, + is plus, = is equals
        eq1 = MathTex("a^2 + b^2 = c^2")
        
        # Move it to the top
        eq1.shift(UP * 2)
        
        # Gaussian integral (complex equation)
        # r" means raw string (for LaTeX special characters)
        # \int is integral symbol, _0 is lower limit, ^\infty is upper limit
        # \frac{a}{b} creates a fraction
        eq2 = MathTex(r"\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}")
        
        # Basel problem solution
        # \sum is summation symbol, _{n=1} is lower limit
        eq3 = MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}")
        
        # Move it to the bottom
        eq3.shift(DOWN * 2)
        
        # Show them one at a time
        self.play(Write(eq1))
        self.play(Write(eq2))
        self.play(Write(eq3))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove all equations
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class ColoredEquation(Scene):
    """
    Adding colors to equations.
    
    To render:
        manim -pql 12_equations.py ColoredEquation
    """
    
    def construct(self):
        # You can color different parts of an equation
        # Split the equation into parts (each string is one part)
        equation = MathTex(
            "x",                      # Part 0
            "=",                      # Part 1
            "{-b",                    # Part 2
            r"\pm",                   # Part 3 (plus-minus symbol)
            r"\sqrt{b^2 - 4ac}",     # Part 4 (square root)
            r"\over",                 # Part 5 (division bar)
            "2a}"                     # Part 6
        )
        # This is the quadratic formula
        
        # Color different parts using their index
        # Index starts at 0
        equation[0].set_color(YELLOW)  # x is yellow
        equation[2].set_color(RED)     # -b is red
        equation[4].set_color(BLUE)    # square root part is blue
        equation[6].set_color(GREEN)   # 2a is green
        
        # Show the colored equation
        self.play(Write(equation))
        
        # Wait 3 seconds to see the colors
        self.wait(3)
        
        # Remove the equation
        self.play(FadeOut(equation))


class TransformEquation(Scene):
    """
    Transforming one equation into another.
    
    To render:
        manim -pql 12_equations.py TransformEquation
    """
    
    def construct(self):
        # Show an equation transforming to its simplified form
        
        # Start with expanded form
        # x^2 means x-squared
        eq1 = MathTex("x^2 + 2x + 1")
        
        # Write the first equation
        self.play(Write(eq1))
        
        # Wait 1 second
        self.wait(1)
        
        # Create the factored form
        # (x + 1)^2 is the same as x^2 + 2x + 1
        eq2 = MathTex("(x + 1)^2")
        
        # Transform from expanded to factored form
        # Shows the algebraic simplification visually
        self.play(Transform(eq1, eq2))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove the equation
        self.play(FadeOut(eq1))


class EquationWithText(Scene):
    """
    Combining equations with explanatory text.
    
    To render:
        manim -pql 12_equations.py EquationWithText
    """
    
    def construct(self):
        # Combine regular text with equations for explanations
        
        # Create a title using Text (not MathTex)
        title = Text("The Pythagorean Theorem", color=YELLOW)
        
        # Move it to the top edge
        title.to_edge(UP)
        
        # Create the equation
        equation = MathTex("a^2 + b^2 = c^2")
        
        # Make it larger
        equation.scale(1.5)
        
        # Create descriptive text
        description = Text("For any right triangle", font_size=24)
        
        # Position it below the equation
        description.next_to(equation, DOWN, buff=1)
        # buff=1 means 1 unit of spacing
        
        # Show everything in sequence
        # First the title
        self.play(Write(title))
        
        # Wait 1 second
        self.wait(1)
        
        # Then the equation
        self.play(Write(equation))
        
        # Wait 1 second
        self.wait(1)
        
        # Finally the description
        self.play(Write(description))
        
        # Wait 2 seconds
        self.wait(2)
        
        # Remove everything
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class EquationArray(Scene):
    """
    Creating aligned equations (like in LaTeX align environment).
    
    To render:
        manim -pql 12_equations.py EquationArray
    """
    
    def construct(self):
        # Create multiple related equations aligned nicely
        
        # Group of three equations showing derivatives
        equations = VGroup(
            MathTex("f(x) = x^2"),        # Original function
            MathTex("f'(x) = 2x"),        # First derivative
            MathTex("f''(x) = 2"),        # Second derivative
        )
        # f' means first derivative, f'' means second derivative
        
        # Arrange them vertically
        # DOWN means stack from top to bottom
        # aligned_edge=LEFT means align on the left side
        # buff=0.5 is the spacing between equations
        equations.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        # Show them one by one
        for eq in equations:
            # Write each equation
            self.play(Write(eq))
            # Short pause between each
            self.wait(0.5)
        
        # Wait 2 seconds to view all equations
        self.wait(2)
        
        # Remove all equations
        self.play(FadeOut(equations)) 