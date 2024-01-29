# from manim import *
#
#
# class InheritanceAnimation(Scene):
#     def construct(self):
#         # Create a big square (parent class)
#         big_square = Square(side_length=2, color=YELLOW, fill_opacity=0.8)
#         big_square_label = Text("Parent Class", color=YELLOW).scale(0.5)
#         big_square_group = Group(big_square, big_square_label).arrange(DOWN).to_edge(UP)
#
#         # Create a small square (child class)
#         small_square = Square(side_length=1, color=BLUE, fill_opacity=0.8)
#         small_square_label = Text("Child Class", color=WHITE).scale(0.5)
#         small_square_group = (
#             Group(small_square, small_square_label)
#             .arrange(DOWN)
#             .next_to(big_square_group, DOWN)
#         )
#
#         # Show the arrow pointing from upper class to lower class
#         arrow = Arrow(
#             big_square_group.get_bottom() + DOWN * 0.1,
#             small_square_group.get_top(),
#             buff=0,
#             color=WHITE,
#             max_tip_length_to_length_ratio=0.1,  # Adjust this ratio for longer arrow
#         )
#         feeding_text = Text("Inherits", color=WHITE).scale(0.5).next_to(arrow, DOWN)
#
#         # Play the animation
#         self.play(Create(big_square), Create(big_square_label))
#         self.play(Create(small_square), Create(small_square_label))
#         self.play(Create(arrow), Write(feeding_text))
#
#         # Add growing and shrinking animations
#         self.play(
#             small_square_group.animate.scale(1.5),
#             FadeOut(arrow),
#             FadeOut(feeding_text),
#         )
#
#         self.wait(2)


from manim import *


class A(Scene):
    def construct(self):
        # Create a square at the top of the window
        square_top = Square(side_length=1, color=BLUE, fill_opacity=0.8)
        square_top_label = Text("Top Square", color=WHITE).scale(0.5)
        square_top_group = Group(square_top, square_top_label).move_to(UP * 3)

        # Create a square at the bottom of the window
        # square_bottom = Square(side_length=1, color=RED, fill_opacity=0.8)
        # square_bottom_label = Text("Bottom Square", color=WHITE).scale(0.5)
        # square_bottom_group = Group(square_bottom, square_bottom_label).move_to(
        #     DOWN * 3
        # )

        # Add squares to the scene
        self.play(Create(square_top_group))
        # self.play(Create(square_bottom_group))
        # self.wait(2)
