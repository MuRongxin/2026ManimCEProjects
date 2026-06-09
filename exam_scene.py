from click import option
from matplotlib.axes import Axes
from matplotlib.sankey import DOWN

from manim import *
import problems

# ============================================================
# 全局配置
# ============================================================
FONT_CN = "得意黑"                   # 正文中文字体
FONT_SERIF = "文悦新青年体 (须授权)"   # 标题/强调中文字体


# ============================================================
# 颜色系统（统一 CLR_ 前缀）
# ============================================================
# ---- 基础色板：描述颜色本身 ----
CLR_TEAL        = ManimColor("#39c5bb")   # 初音绿 / 青绿
CLR_CRIMSON     = ManimColor("#C1003C")   # 深红 / 暗红
CLR_CYAN_DEEP   = ManimColor("#11999e")   # 深青色
CLR_ROSE        = ManimColor("#ff2e63")   # 玫红 / 亮粉
CLR_MINT        = ManimColor("#79D87E")   # 薄荷绿
CLR_CREAM       = ManimColor("#fff4e1")   # 奶油 / 米黄
CLR_SALMON      = ManimColor("#ffaaa5")   # 浅粉 / 三文鱼
CLR_SKY         = ManimColor("#b9d7ea")   # 天蓝
CLR_CORNFLOWER  = ManimColor("#7dace4")   # 矢车菊蓝




class ExamTitleScene(MovingCameraScene):
    """
    第一部分：标题 + 注意事项
    """

    def construct(self):
        self.camera.background_color = BLACK

        # ---------- 绝密 ★ 启用前 ----------
        top_secret = Text("绝密★启用前", font=FONT_SERIF, color=CLR_CRIMSON, font_size=21)
        top_secret.to_edge(UP, buff=.2)

        # ---------- 大标题 ----------
        title = Text("2026 年普通高等学校招生全国统一考试",
                     font=FONT_SERIF, color=CLR_CREAM, font_size=22)
        title.next_to(top_secret, DOWN, buff=0.2).to_edge(LEFT)

        top_secret.next_to(title, UP, buff=0.2)

        # ---------- "数学" ----------
        subject = Text("数  学", font=FONT_SERIF, color=CLR_CREAM, font_size=41)
        subject.next_to(title, DOWN, buff=0.2)

        # ---------- 注意事项标题 ----------
        notice_title = Text("2026新高考二卷", font=FONT_CN, color=CLR_CREAM, font_size=18)
        
        notice_title.next_to(subject, RIGHT, buff=.1,aligned_edge=DOWN)
        

        # ---------- 注意事项内容 ----------~
        notice_lines = [
            "1. 答卷前，考生务必将自己的姓名、考生号、考场号、座位号填写在答题卡上。",
            "2. 回答选择题时，选出每小题答案后，用铅笔把答题卡上对应题目的答案标号",
            "   涂黑。如需改动，用橡皮擦干净后，再选涂其它答案标号。回答非选择题时，",
            "   将答案写在答题卡上。写在本试卷上无效。",
            "3. 考试结束后，将本试卷和答题卡一并交回。",
        ]

        notice_texts = VGroup()
        for line in notice_lines:
            t = Text(line, font=FONT_CN, color=CLR_CREAM, font_size=19)
            notice_texts.add(t)

        notice_texts.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        notice_texts.next_to(notice_title, DOWN, buff=0.3)
        notice_texts.align_to(notice_title, LEFT)

        # ---------- 动画 ----------
        self.play(FadeIn(top_secret, shift=RIGHT * 0.3), run_time=0.3)
        self.wait(0.3)
        self.play(FadeIn(title, shift=RIGHT * 0.3), run_time=0.3)
        self.wait(0.3)
        self.play(FadeIn(subject, shift=RIGHT * 0.3), run_time=.3)
        self.wait(0.5)
        self.play(FadeIn(notice_title, shift=RIGHT * 0.2), run_time=0.3)

        

        self.wait(2)

        # ---------- 选择题标题 ----------
        section1 = Text(
            "一、选择题：本题共 8 小题，每小题 5 分，共 40 分。",            
            font=FONT_CN, color=CLR_CREAM, font_size=22, stroke_width=1
        ).scale(.8)
        section1.next_to(subject,DOWN,buff=.8).to_edge(LEFT,buff=.3)

        q1 = problems.problem_01(math_size=30).scale(.7)
        q1.next_to(section1, DOWN, buff=0.3, aligned_edge=LEFT)

        q2=problems.problem_02(
            math_size=30,
            option_layout="row").scale(.7)
        q2.next_to(q1, DOWN, buff=0.3,aligned_edge=LEFT)

        q3=problems.problem_03().scale(.7)
        q3.next_to(q2, DOWN, buff=0.3,aligned_edge=LEFT)

        q4=problems.problem_04(wrap_after=6).scale(.7)
        q4.next_to(q3, DOWN, buff=0.2,aligned_edge=LEFT)

        q5=problems.problem_05(wrap_after=3).scale(.7)
        q5.to_edge(UP,buff=.8).shift(RIGHT*3.3)

        q6=problems.problem_06(wrap_after=8).scale(.7)
        q6.next_to(q5, DOWN, buff=0.3,aligned_edge=LEFT)

        q7=problems.problem_07().scale(.7)
        q7.next_to(q6, DOWN, buff=0.3,aligned_edge=LEFT)

        q8=problems.problem_08(wrap_after=6,option_layout="grid").scale(.7)
        q8.next_to(q7, DOWN, buff=0.3,aligned_edge=LEFT)


        self.play(LaggedStart(
            Write(section1),
            Write(q1),
            Write(q2),
            Write(q3),
            Write(q4),
            Write(q5),
            Write(q6),
            Write(q7),
            Write(q8),
            lag_ratio=0.4,
        ))

        section2=Text(
            "二、多项选择题：本题共 3 小题，每小题 6 分，共 18 分。",
            font=FONT_CN, color=CLR_CYAN_DEEP, font_size=22, 
            stroke_width=1,stroke_color=CLR_CYAN_DEEP
        ).scale(.8)
        section2.next_to(q8, DOWN, buff=1,aligned_edge=LEFT)

        q9=problems.problem_09().scale(.7)
        q9.next_to(section2, DOWN, buff=0.3).align_to(q4,LEFT)


        q10=problems.problem_10(option_layout="grid", wrap_after=9).scale(.7)
        q10.next_to(q9, DOWN, buff=0.3).align_to(q9,LEFT)

        q11=problems.problem_11(wrap_after=8).scale(.7)
        q11.next_to(q10, DOWN, buff=0.3).align_to(q9,LEFT)

        section3=Text(
            "三、解答题：本题共 3 小题，每小题 5 分，共 15 分。",
            font=FONT_CN, color=CLR_CYAN_DEEP, font_size=20,
        )
        # section3.next_to(q11, DOWN, buff=.5).align_to(q11,LEFT)
        section3.next_to(q9, RIGHT, buff=1.3).align_to(q9,UP)

        q12=problems.problem_12().scale(.7)
        q12.next_to(section3, DOWN, buff=0.3,aligned_edge=LEFT)

        q13=problems.problem_13().scale(.7)
        q13.next_to(q12, DOWN, buff=0.3,aligned_edge=LEFT)
        q14=problems.problem_14(wrap_after=14).scale(.7)
        q14.next_to(q13, DOWN, buff=0.3,aligned_edge=LEFT)


        section4=Text(
            "四、解答题：本题共 5 小题，共 77 分。",
            font=FONT_CN, color=CLR_CYAN_DEEP, font_size=20,
        )
        section4.next_to(q14, DOWN, buff=.5).align_to(q14,LEFT)

        q15=problems.problem_15().scale(.7)
        q15.next_to(section4, DOWN, buff=.3).align_to(q14,LEFT)

        # ---------- 直方图 ----------
        # histogram = problems.problem_15_histogram().scale(.7)
        # histogram.next_to(q15, DOWN, buff=.3).align_to(q15, LEFT)

        q16=problems.problem_16(wrap_after=6).scale(.7)
        q16.next_to(q11, DOWN, buff=.5).align_to(q11, LEFT)

        q16Axes=Axes(
            x_range=[0, 4, 1],
            y_range=[0, 4, 1],
            x_length=2,
            y_length=2,            
        ).scale(1.2)
        # self.add(q16Axes)
        q16Axes.next_to(q16,DOWN).shift(UP+RIGHT*2.5)
        q16Graph=problems.problem_16_fig(q16Axes).scale(.7)
        

        q17=problems.problem_17().scale(.7)
        q17.next_to(q16, DOWN, buff=1.8).align_to(q16, LEFT)

        q18=problems.problem_18().scale(.7)
        q18.next_to(q16, RIGHT, buff=1.5).align_to(q16, UP)

        self.camera.frame.shift(DOWN*15)
        self.play(LaggedStart(
            Write(section2),
            Write(q9),
            Write(q10),
            Write(q11),

            Write(section3),
            Write(q12),
            Write(q13),
            Write(q14),

            Write(section4),
            Write(q15),
            Write(q16),
            Create(q16Graph),
            Write(q17),
            Write(q18),

        ))

# class Q1(Scene):
