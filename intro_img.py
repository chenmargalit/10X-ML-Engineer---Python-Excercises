from manim import *

class a(Scene):
    def construct(self):
        arrow_1 = Arrow(start=RIGHT, end=LEFT, color=GOLD)
        arrow_2 = Arrow(start=RIGHT, end=LEFT, color=GOLD, tip_shape=ArrowSquareTip).shift(DOWN)
        g1 = Group(arrow_1, arrow_2)

        square = Square(color=GREEN)
        arrow_3 = Arrow(start=LEFT, end=RIGHT, color=RED)
        arrow_4 = Arrow(start=LEFT, end=RIGHT, buff=0).next_to(arrow_1, UP)
        g2 = Group(arrow_3, arrow_4, square)
        #
        # # a shorter arrow has a shorter tip and smaller stroke width
        arrow_5 = Arrow(start=ORIGIN, end=config.top)
        arrow_6 = Arrow(start=config.top + DOWN, end=config.top).shift(LEFT * 3)
        g3 = Group(arrow_5, arrow_6)

        # self.add(Group(g1, g2, g3).arrange(buff=2))
        self.add(Group(g1, g2, g3).arrange(buff=2))
