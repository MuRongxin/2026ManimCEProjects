from manim import *
from problems import FONT_CN, CLR_CREAM, problem_01, problem_04


class TestProblems(Scene):
    """测试题目包装：字体大小 + 选项布局 + 对齐方式"""

    def construct(self):
        self.camera.background_color = BLACK

        # 默认参数
        p1 = problem_01()
        p1.to_edge(UP, buff=0.6)
        p1.to_edge(LEFT, buff=0.6)

        # 大字体 + 两行选项
        p4 = problem_04(font_size=28, option_layout="grid")
        p4.next_to(p1, DOWN, buff=0.8)
        p4.align_to(p1, LEFT)

        self.play(FadeIn(p1), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(p4), run_time=1)
        self.wait(2)
