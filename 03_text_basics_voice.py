"""
Lesson 3 with Voice: Text Basics

All 4 scenes about text with voice narration.

To render:
    python3 -m manim -pql 03_text_basics_voice.py SimpleTextVoice
"""

from manim import *
from manim_voiceover import VoiceoverScene
from voiceover_config import configure_voiceover


class SimpleTextVoice(VoiceoverScene):
    """Basic text creation and display."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        text = Text("Hello, Manim!")
        
        with self.voiceover(text="We can write text that appears letter by letter.") as tracker:
            self.play(Write(text), run_time=tracker.duration)
        
        with self.voiceover(text="This is simple text rendering in Manim.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Now we'll fade it out.") as tracker:
            self.play(FadeOut(text), run_time=tracker.duration)


class TextFormattingVoice(VoiceoverScene):
    """Different text sizes, colors, and fonts."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        colored_text = Text("Colored Text", color=BLUE)
        colored_text.shift(UP * 2)
        
        big_text = Text("Big Text", font_size=72)
        small_text = Text("Small Text", font_size=24)
        small_text.shift(DOWN * 2)
        
        with self.voiceover(text="Text can be colored. This text is blue.") as tracker:
            self.play(Write(colored_text), run_time=tracker.duration)
        
        with self.voiceover(text="Text can be large, like this.") as tracker:
            self.play(Write(big_text), run_time=tracker.duration)
        
        with self.voiceover(text="Or text can be small, like this.") as tracker:
            self.play(Write(small_text), run_time=tracker.duration)
        
        with self.voiceover(text="Size and color give us control over text appearance.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing all text.") as tracker:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=tracker.duration)


class TextPositioningVoice(VoiceoverScene):
    """Positioning text in different locations."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        title = Text("Title at Top", color=YELLOW)
        title.to_edge(UP)
        
        center_text = Text("Center Text")
        center_text.move_to(ORIGIN)
        
        bottom_text = Text("Bottom Text", color=GREEN)
        bottom_text.to_edge(DOWN)
        
        with self.voiceover(text="We can position text at the top edge of the screen.") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        with self.voiceover(text="Or at the center.") as tracker:
            self.play(Write(center_text), run_time=tracker.duration)
        
        with self.voiceover(text="Or at the bottom edge.") as tracker:
            self.play(Write(bottom_text), run_time=tracker.duration)
        
        with self.voiceover(text="Positioning text is essential for creating clear presentations.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Clearing the scene.") as tracker:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=tracker.duration)


class TextWithShapesVoice(VoiceoverScene):
    """Combining text with shapes."""
    
    def construct(self):
        configure_voiceover(self, backend="gtts", lang="en")
        
        circle = Circle(radius=1.5, color=BLUE)
        circle.set_fill(BLUE, opacity=0.3)
        label = Text("Circle", color=WHITE)
        
        with self.voiceover(text="Let's create a blue circle.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
        
        with self.voiceover(text="We can add a label that appears in the center.") as tracker:
            self.play(Write(label), run_time=tracker.duration)
        
        with self.voiceover(text="Now we'll move the label above the circle for better clarity.") as tracker:
            self.play(label.animate.next_to(circle, UP), run_time=tracker.duration)
        
        with self.voiceover(text="Combining shapes with text labels makes diagrams more informative.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Removing everything.") as tracker:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=tracker.duration)


