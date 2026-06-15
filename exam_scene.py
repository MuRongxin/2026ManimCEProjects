from turtle import color

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
CLR_CREAM       = ManimColor("#fffb1f")   # 奶油 / 米黄
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
        top_secret.to_edge(UP)

        # ---------- 大标题 ----------
        title = Text("2026 年普通高等学校招生全国统一考试",
                     font=FONT_SERIF, color=CLR_CREAM, font_size=22)
        title.next_to(top_secret, DOWN, buff=0.2).to_edge(LEFT)

        top_secret.to_corner(UL, buff=.2)

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
        self.play(Write(top_secret), run_time=0.3)
        self.wait(0.3)
        self.play(Write(title), run_time=0.3)
        self.play(Write(subject), run_time=.3)
        self.play(Write(notice_title), run_time=0.3)

        

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

        q18=problems.problem_18(wrap_after=8).scale(.7)
        q18.next_to(q16, RIGHT, buff=1.5).align_to(q16, UP)

        q19=problems.problem_19(wrap_after=6).scale(.7)
        q19.next_to(q18, DOWN, buff=1).align_to(q18, LEFT)

        
        self.play(AnimationGroup(
            self.camera.frame.animate.shift(DOWN*7.4),
            LaggedStart(
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
                lag_ratio=0.3,
            ),lag_ratio=0
        ), run_time=10)

        self.play(
            self.camera.frame.animate.shift(DOWN*7.7),
            LaggedStart(
                Write(q16),
                Create(q16Graph),
                Write(q17),
                Write(q18),
                Write(q19),
                lag_ratio=0.4,
            ),
         run_time=8)

        self.wait(2)

        self.play(self.camera.frame.animate.shift(UP*15),run_time=10)


def AddTitle(self,title="temp",font=FONT_SERIF ,color:str=CLR_TEAL,font_size=35,stroke_width=1.5,stroke_color=CLR_TEAL):
        title=Text(
            title,  # 标题文本内容    
            font=font,  
            font_size=font_size, 
            stroke_width=stroke_width,
            
        ).to_corner(UL)
        
        title_back=Rectangle(
            width=title.width,
            height=title.height,
            fill_opacity=1,
            color=color
        ).move_to(title.get_center()+LEFT*3+DOWN*.2)


        title_back_pos=title_back.animate.move_to(title.get_center()+DOWN*.2+RIGHT*.2)
        
        
        self.add(title_back)  

        return LaggedStart(
            Write(title),
            title_back_pos,
            lag_ratio=0.3,
        ) , title_back

def EmphasizeTexts(self,targets:Mobject,color:str=YELLOW,stroke_width=4,buff=0):
        animes=[]
        recs=VGroup()
        for target in targets:        
            rec_target=Circumscribe(target,color=color,stroke_width=stroke_width,buff=buff)
            animes.append(rec_target)
            rec2_target=SurroundingRectangle(target,color=color,
                                             stroke_width=stroke_width,
                                             buff=buff)
            animes.append(Create(rec2_target))
            recs.add(rec2_target)
        
        self.play(LaggedStart(*animes,lag_ratio=.3))
        return recs


class Q123(Scene):
    def construct(self):
        title,titlePos=AddTitle(self,"2026 新高考二卷 解析",font_size=31)        
        self.play(title)

        q1=problems.problem_01()
        q1.next_to(titlePos,DOWN,buff=.7).align_to(titlePos,LEFT)

        # q1 解答：接在等号后面，逐个写出
        stem1 = q1[0]
        eq1 = stem1[1]  # MathTex "(1-3i)^2 ="
        s1_1 = MathTex(r"= 1 - 6i + 9i^2", color=CLR_ROSE, stroke_width=1, font_size=33)
        s1_2 = MathTex(r"= 1 - 6i - 9", color=CLR_ROSE, stroke_width=1, font_size=33)
        s1_3 = MathTex(r"= -8 - 6i", color=CLR_ROSE, stroke_width=1, font_size=33)
        s1_1.next_to(eq1, RIGHT, buff=0.1, aligned_edge=ORIGIN)
        s1_2.next_to(s1_1, RIGHT, buff=0.15, aligned_edge=ORIGIN)
        s1_3.next_to(s1_2, RIGHT, buff=0.15, aligned_edge=ORIGIN)

        q2=problems.problem_02()
        q2.next_to(q1,DOWN,buff=.55).align_to(q1,LEFT)

        # q2 结果接在等号后面
        stem2 = q2[0]
        eq2 = stem2[5]  # MathTex "A \cap B ="
        ans2 = MathTex(r"\{0,1\}", color=CLR_ROSE, stroke_width=1, font_size=28)
        ans2.next_to(eq2, RIGHT, buff=0.1, aligned_edge=DOWN)

        # q2 求解过程放在题目下方，逐行排列
        s2_1 = MathTex(r"\sqrt{x}=x \Rightarrow x=x^2 \Rightarrow x(x-1)=0",
                       color=CLR_CREAM, stroke_width=1, font_size=33)
        s2_2 = MathTex(r"\Rightarrow x=0 \text{ or } x=1 \Rightarrow B=\{0,1\}",
                       color=CLR_CREAM, stroke_width=1, font_size=33)
        s2_3 = MathTex(r"A \cap B = \{0,1,3,6,9\} \cap \{0,1\} = \{0,1\}",
                       color=CLR_CREAM, stroke_width=1, font_size=33)

        s2_1.next_to(q2, DOWN, buff=0.2)
        s2_2.next_to(s2_1, DOWN, buff=0.15, aligned_edge=LEFT)
        s2_3.next_to(s2_1, RIGHT, buff=0.44)

        q3=problems.problem_03()
        q3.next_to(q2,DOWN,buff=1.5).align_to(q2,LEFT)

        # q3 结果接在等号后面
        stem3 = q3[0]
        eq3 = stem3[7]  # MathTex "\boldsymbol{a}\cdot\boldsymbol{b} ="
        ans3 = MathTex(r"-2", color=CLR_ROSE, stroke_width=1, font_size=33)
        ans3.next_to(eq3, RIGHT, buff=0.1, aligned_edge=DOWN)

        # q3 求解过程放在题目下方
        s3_1 = MathTex(r"|\boldsymbol{a}+\boldsymbol{b}|^2=1 \Rightarrow \boldsymbol{a}^2+2\boldsymbol{a}\cdot\boldsymbol{b}+\boldsymbol{b}^2=1",
                       color=CLR_CREAM, stroke_width=1, font_size=33)
        s3_2 = MathTex(r"|\boldsymbol{a}-\boldsymbol{b}|^2=9 \Rightarrow \boldsymbol{a}^2-2\boldsymbol{a}\cdot\boldsymbol{b}+\boldsymbol{b}^2=9",
                       color=CLR_CREAM, stroke_width=1, font_size=33)
        s3_3 = MathTex(r"\text{Subtract: } 4\boldsymbol{a}\cdot\boldsymbol{b}=-8 \Rightarrow \boldsymbol{a}\cdot\boldsymbol{b}=-2",
                       color=CLR_CREAM, stroke_width=1, font_size=33)
        s3_1.next_to(q3, DOWN, buff=0.1).align_to(stem3[1], LEFT)
        s3_2.next_to(s3_1, DOWN, buff=0.15, aligned_edge=LEFT)

        breace3 = Brace(VGroup(s3_1,s3_2), RIGHT, buff=0.15)
        s3_3.next_to(breace3, RIGHT, buff=0.2)

        self.play(Write(q1))
        self.play(Write(q2))
        self.play(Write(q3))

        self.play(LaggedStart(Write(s1_1), Write(s1_2), Write(s1_3), lag_ratio=0.4))
        self.wait(2)
        self.play(LaggedStart(Write(s2_1), Write(s2_2), Write(s2_3), Write(ans2), lag_ratio=0.4))
        self.wait(2)
        self.play(LaggedStart(Write(s3_1), Write(s3_2), Create(breace3), Write(s3_3), Write(ans3), lag_ratio=0.4))

        self.wait(2)

class Q4(Scene):
    def construct(self):
        title,titlePos=AddTitle(self,"求双曲线 渐近线方程",font_size=31)
        self.play(title)

        q4=problems.problem_04()
        q4.next_to(titlePos,DOWN,buff=.7).align_to(titlePos,LEFT)

        # q4 解答过程放在题目下方
        s4_1 = MathTex(r"(1,0) \in C \Rightarrow \frac{1}{a^2}=1 \Rightarrow a^2=1",
                       color=CLR_CREAM, stroke_width=1, font_size=33)
        s4_2 = MathTex(r"\left(\frac{\sqrt{7}}{2},3\right) \in C \Rightarrow \frac{7}{4} - \frac{9}{b^2}=1",
                       color=CLR_CREAM, stroke_width=1, font_size=33)
        s4_3 = MathTex(r"\Rightarrow \frac{9}{b^2}=\frac{3}{4} \Rightarrow b^2=12 \Rightarrow b=2\sqrt{3}",
                       color=CLR_CREAM, stroke_width=1, font_size=33)
        s4_4 = MathTex(r"y=\pm \frac{b}{a}x = \pm 2\sqrt{3}\,x",
                       color=CLR_ROSE, stroke_width=1, font_size=41)
                       
        s4_1.next_to(q4, DOWN, buff=0.3).align_to(q4[1], LEFT)
        s4_2.next_to(s4_1, DOWN, buff=0.15, aligned_edge=LEFT)
        s4_3.next_to(VGroup(s4_1,s4_2), RIGHT, buff=0.25, )
        s4_4.next_to(s4_3, DOWN, buff=0.7)

        self.play(Write(q4))
        self.play(LaggedStart(
            Write(s4_1), Write(s4_2), Write(s4_3), Write(s4_4),
            lag_ratio=1,
        ))
        self.wait(2)

class Q5(Scene):
    def construct(self):
        title,titlePos=AddTitle(self,"菱形面积公式  棱台体积公式",font_size=31)
        self.play(title)

        q5=problems.problem_05(wrap_after=3)
        q5.next_to(titlePos,DOWN,buff=.7).align_to(titlePos,LEFT)

        self.play(Write(q5))

        # q5 解答过程放在题目下方
        s5_1 = MathTex(r"S=a^2\sin 60^{\circ}=\frac{\sqrt{3}}{2}a^2",
                       color=CLR_CREAM, stroke_width=1, font_size=33)
        s5_2 = MathTex(r"S_1=\frac{\sqrt{3}}{2}\times 9=\frac{9\sqrt{3}}{2},\quad "
                       r"S_2=\frac{\sqrt{3}}{2}\times 4=2\sqrt{3}",
                       color=CLR_CREAM, stroke_width=1, font_size=33)
        s5_3 = MathTex(r"\sqrt{S_1 S_2}=\sqrt{\frac{9\sqrt{3}}{2}\times 2\sqrt{3}}"
                       r"=\sqrt{27}=3\sqrt{3}",
                       color=CLR_CREAM, stroke_width=1, font_size=33)
        s5_4 = MathTex(r"V=\frac{h}{3}\left(S_1+S_2+\sqrt{S_1 S_2}\right)"
                       r"=\frac{\sqrt{3}}{3}\left(\frac{9\sqrt{3}}{2}+2\sqrt{3}+3\sqrt{3}\right)",
                       color=CLR_CREAM, stroke_width=1, font_size=33)
        s5_5 = MathTex(r"=\frac{\sqrt{3}}{3}\times\frac{19\sqrt{3}}{2}=\frac{19}{2}",
                       color=CLR_ROSE, stroke_width=1, font_size=41)
        s5_1.next_to(q5[1], DOWN, buff=0.3).align_to(q5, LEFT)
        s5_2.next_to(s5_1, DOWN, buff=0.15, aligned_edge=LEFT)
        s5_3.next_to(s5_2, DOWN, buff=0.15, aligned_edge=LEFT)
        s5_4.next_to(s5_3, DOWN, buff=0.15, aligned_edge=LEFT)
        s5_5.next_to(s5_4, RIGHT, buff=0.15, )

        self.play(LaggedStart(
            Write(s5_1), Write(s5_2), Write(s5_3), Write(s5_4), Write(s5_5),
            lag_ratio=0.9,
        ))
        self.wait(2)


class Q6(Scene):
    def construct(self):
        title,titlePos=AddTitle(self,"排列组合 分组分配问题",font_size=31)
        self.play(title)

        q6=problems.problem_06(wrap_after=8)
        q6.next_to(titlePos,DOWN,buff=.7).align_to(titlePos,LEFT)
        self.play(Write(q6))
        self.wait(2)

        # === 文字步骤 ===
        s6_1 = Text("Step 1：甲、乙必在同一组，分两类——同在 A 或同在 B",
                    font=FONT_CN, color=CLR_CREAM, font_size=28)
        s6_2 = Text("Step 2：丙、丁不能同组，剩余 4 人选 1 人填充",
                    font=FONT_CN, color=CLR_CREAM, font_size=28)
        s6_1.next_to(q6[1], DOWN, buff=0.4).align_to(q6, LEFT)
        s6_2.next_to(s6_1, DOWN, buff=0.2, aligned_edge=LEFT)

        self.play(Write(s6_1), Write(s6_2))

        # === 右下角：A/B 两组位置示意图 ===
        slot_w = 0.25
        slots_A = VGroup(*[
            Line(LEFT * slot_w, RIGHT * slot_w, color=RED, stroke_width=3)
            for _ in range(4)
        ])
        slots_B = VGroup(*[
            Line(LEFT * slot_w, RIGHT * slot_w, color=BLUE, stroke_width=3)
            for _ in range(4)
        ])
        slots_A.arrange(RIGHT, buff=0.2)
        slots_B.arrange(RIGHT, buff=0.2)

        slots_B.to_corner(DR, buff=0.8).shift(UP * 0.3)
        slots_A.next_to(slots_B, LEFT, buff=0.8, aligned_edge=DOWN)

        brace_A = Brace(slots_A, DOWN, buff=0.15)
        brace_B = Brace(slots_B, DOWN, buff=0.15)
        lbl_A = Text("A", font=FONT_CN, color=RED, font_size=28).next_to(brace_A, DOWN, buff=0.1)
        lbl_B = Text("B", font=FONT_CN, color=BLUE, font_size=28).next_to(brace_B, DOWN, buff=0.1)

        self.play(
            LaggedStart(*[Create(s) for s in slots_A + slots_B], lag_ratio=0.1),
            Create(brace_A), Create(brace_B),
            Write(lbl_A), Write(lbl_B),
        )

        # === Case 1：甲、乙在 A ===
        jia = Text("甲", font=FONT_CN, color=RED, font_size=26)
        yi  = Text("乙", font=FONT_CN, color=RED, font_size=26)
        jia.next_to(slots_A[0], UP, buff=0.1)
        yi.next_to(slots_A[1], UP, buff=0.1)

        self.play(Write(jia), Write(yi))

        # 情况说明文字
        s6_3_a = Text("甲、乙在 A：丙去 A 则丁去 B → ", font=FONT_CN, color=CLR_CREAM, font_size=28)
        s6_3_m1 = MathTex(r"C_4^1", color=CLR_CREAM, stroke_width=1, font_size=33)
        s6_3_b = Text(" = 4；丁去 A 则丙去 B → ", font=FONT_CN, color=CLR_CREAM, font_size=28)
        s6_3_m2 = MathTex(r"C_4^1", color=CLR_CREAM, stroke_width=1, font_size=33)
        s6_3_c = Text(" = 4", font=FONT_CN, color=CLR_CREAM, font_size=28)
        s6_3 = VGroup(s6_3_a, s6_3_m1, s6_3_b, s6_3_m2, s6_3_c)
        s6_3.arrange(RIGHT, buff=0.08, aligned_edge=DOWN)
        s6_3.next_to(s6_2, DOWN, buff=0.2, aligned_edge=LEFT)

        self.play(Write(s6_3))

        # === 演示 丙→A, 丁→B ===
        bing = Text("丙", font=FONT_CN, color=RED, font_size=29)
        ding = Text("丁", font=FONT_CN, color=BLUE, font_size=29)
        bing.next_to(slots_A[2], UP, buff=0.1)
        ding.next_to(slots_B[0], UP, buff=0.1)

        # 圈出 A 组剩余的 1 个空位
        remain_A = SurroundingRectangle(slots_A[3], color=YELLOW, stroke_width=5, buff=0.1)

        self.play(Write(bing), Write(ding), Create(remain_A))
 
        self.wait(1)

        self.play(
             bing.animate.next_to(slots_B[0], UP, buff=0.1),
             ding.animate.next_to(slots_A[2], UP, buff=0.1),             
        )
        self.wait(0.5)

        # === 演示 丁→A, 丙→B（交换） ===
        bing2 = Text("丙", font=FONT_CN, color=RED, font_size=29)
        ding2 = Text("丁", font=FONT_CN, color=BLUE, font_size=29)
        bing2.next_to(slots_B[2], UP, buff=0.1)
        ding2.next_to(slots_A[3], UP, buff=0.1)

        remain_A2 = SurroundingRectangle(slots_B[3], color=YELLOW, stroke_width=5, buff=0.1)

        self.wait(2)
        

        # === s6_4 & s6_5 结论 ===
        s6_4 = Text("甲、乙在 B：同理，共 4+4 = 8",
                    font=FONT_CN, color=CLR_CREAM, font_size=28)
        s6_5 = Text("总计：8+8 = 16",
                    font=FONT_CN, color=CLR_ROSE, font_size=36)
        s6_4.next_to(s6_3, DOWN, buff=0.2, aligned_edge=LEFT)
        s6_5.next_to(s6_4, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(s6_4))
        self.play(
                    jia.animate.next_to(slots_B[0], UP, buff=0.1),
                    yi.animate.next_to(slots_B[1], UP, buff=0.1),
                    
                    FadeOut(bing), FadeOut(ding), FadeOut(remain_A),
                    Write(ding2), Write(bing2), Create(remain_A2),
                )

        
        self.wait(1)
        self.play(Write(s6_5))
        self.wait(2)


class Q7(Scene):
    def construct(self):
        title,titlePos=AddTitle(self,"三角函数化简求值",font_size=31)
        self.play(title)

        q7=problems.problem_07()
        q7.next_to(titlePos,DOWN,buff=.4).align_to(titlePos,LEFT)
        self.play(Write(q7))

        s7_1 = Text("Step 1：利用二倍角公式展开 sin2α = 2sinα cosα",
                    font=FONT_CN, color=CLR_CREAM, font_size=28)
        s7_2_a = Text("3 · 2sinα cosα · cosα = 8sinα cos2α  ⇒  ", font=FONT_CN, color=CLR_ROSE, font_size=28)
        s7_2_m = MathTex(r"6\sin\alpha\cos^2\alpha=8\sin\alpha\cos2\alpha",
                         color=CLR_ROSE, stroke_width=1, font_size=33)
        s7_2 = VGroup(s7_2_a, s7_2_m).arrange(RIGHT, buff=0.1).scale(1.1)

        s7_3 = Text("Step 2：α 在第二象限，sinα ≠ 0，两边约去 2sinα",
                    font=FONT_CN, color=CLR_CREAM, font_size=28)
        s7_4 = MathTex(r"3\cos^2\alpha=4\cos2\alpha=4(2\cos^2\alpha-1)",
                       color=CLR_ROSE, stroke_width=1, font_size=37)
        s7_5 = MathTex(r"\Rightarrow \cos^2\alpha=\frac{4}{5},\;"
                       r"\sin^2\alpha=1-\frac{4}{5}=\frac{1}{5}",
                       color=BLUE, stroke_width=1, font_size=37)
        s7_6_a = Text("Step 3：α 在第二象限：cosα < 0, sinα > 0  ⇒  ", font=FONT_CN, color=CLR_CREAM, font_size=28)
        s7_6_m = MathTex(r"\cos\alpha=-\frac{2}{\sqrt{5}},\;"
                         r"\sin\alpha=\frac{1}{\sqrt{5}}",
                         color=CLR_CREAM, stroke_width=1, font_size=33)
        s7_6 = VGroup(s7_6_a, s7_6_m).arrange(RIGHT, buff=0.1)

        s7_7 = MathTex(r"\frac{1+\sin\alpha}{2-\cos\alpha}"
                       r"=\frac{1+\frac{1}{\sqrt{5}}}{2+\frac{2}{\sqrt{5}}}"
                       r"=\frac{\sqrt{5}+1}{2(\sqrt{5}+1)}"
                       r"=\frac{1}{2}",
                       color=CLR_ROSE, stroke_width=1, font_size=36)

        s7_1.next_to(q7[1], DOWN, buff=0.4).align_to(q7[1], LEFT)
        s7_2.next_to(s7_1[5], DOWN, buff=0.2, aligned_edge=LEFT)
        s7_3.next_to(s7_2, DOWN, buff=0.2).align_to(s7_1, LEFT)
        s7_4.next_to(s7_3[5], DOWN, buff=0.2, aligned_edge=LEFT)
        s7_5.next_to(s7_4, RIGHT, buff=0.2, aligned_edge=ORIGIN)
        s7_6.next_to(s7_5, DOWN, buff=0.1).align_to(s7_3, LEFT)
        s7_7.next_to(s7_6, DOWN, buff=0.1)

        self.play(LaggedStart(
            Write(s7_1), Write(s7_2), Write(s7_3),
            lag_ratio=0.9,
        ))
        self.wait(1.5)
        self.play(LaggedStart(
            Write(s7_4), Write(s7_5), Write(s7_6),
            lag_ratio=0.9,
        ))
        self.play(Write(s7_7))
        self.wait(2)


class Q8(Scene):
    def construct(self):
        title,titlePos=AddTitle(self,"函数性质 周期与奇偶",font_size=31)
        self.play(title)

        q8=problems.problem_08()
        q8.next_to(titlePos,DOWN,buff=.4).align_to(titlePos,LEFT)
        self.play(Write(q8))

        # === Step 1 ===
        s8_1 = VGroup(
            Text("Step 1：", font=FONT_CN, color=CLR_CREAM, font_size=28),
            MathTex(r"f(x)+f(x-2)=0 \;\xrightarrow{x\to x+2}\; f(x+2)+f(x)=0 \Rightarrow f(x+2)=-f(x)",
                    color=BLUE, stroke_width=1, font_size=33),
        ).arrange(RIGHT, buff=0.1)
        s8_1.next_to(q8[1], DOWN, buff=0.4).align_to(q8, LEFT)

        e8_1 = VGroup(
            Text("将 x 换为 x+2：", font=FONT_CN, color=CLR_SKY, font_size=24),
            MathTex(r"f(x+2)+f(x)=0", color=CLR_ROSE, stroke_width=1, font_size=28),
            Text("，移项得 ", font=FONT_CN, color=CLR_SKY, font_size=24),
            MathTex(r"f(x+2)=-f(x)", color=CLR_ROSE, stroke_width=1, font_size=28),
        ).arrange(RIGHT, buff=0.08)
        e8_1.next_to(s8_1, DOWN, buff=0.15, aligned_edge=LEFT)

        self.play(Write(s8_1))
        self.wait(0.5)    
       
        self.play(Write(e8_1))
 
        self.wait(2)
        self.play(FadeOut(e8_1))

        # === Step 2 ===
        s8_2 = VGroup(
            Text("Step 2：", font=FONT_CN, color=CLR_CREAM, font_size=28),
            MathTex(r"f(x+4)=-f(x+2)=f(x)", color=BLUE, stroke_width=1, font_size=33),
            Text("，周期 T = 4", font=FONT_CN, color=CLR_CREAM, font_size=28),
        ).arrange(RIGHT, buff=0.1)
        s8_2.next_to(s8_1, DOWN, buff=0.2, aligned_edge=LEFT)

        e8_2 = VGroup(
            MathTex(r"x \Rightarrow x+2:\;",
                                color=BLUE, stroke_width=1, font_size=28),
            MathTex(r"f(x+4)=f((x+2)+2)=-f(x+2)=-(-f(x))=f(x)",
                    color=CLR_ROSE, stroke_width=1, font_size=28),
            Text("，周期 T = 4", font=FONT_CN, color=CLR_SKY, font_size=24),
        ).arrange(RIGHT, buff=0.08)
        e8_2.next_to(s8_2, DOWN, buff=0.15, aligned_edge=LEFT)

        self.play(Write(s8_2))
        self.wait(0.5)

        s8_emp1=EmphasizeTexts(self, [s8_1[1][0][-12:]],buff=.2, color=RED)
        self.play(Write(e8_2))
        self.wait(2)
        self.play(FadeOut(e8_2,s8_emp1))

        # === Step 3 ===
        s8_3 = VGroup(
            Text("Step 3：由周期和偶函数，", font=FONT_CN, color=CLR_CREAM, font_size=28),
            MathTex(r"f(\frac{3}{2})=f(-\frac{5}{2})=f(\frac{5}{2})",
                    color=BLUE, stroke_width=1, font_size=33),
        ).arrange(RIGHT, buff=0.1)
        s8_3.next_to(s8_2, DOWN, buff=0.2, aligned_edge=LEFT)

        e8_3 = VGroup(
            MathTex(r"f(\frac{3}{2})=f(\frac{3}{2}-4)=f(-\frac{5}{2})",
                    color=CLR_ROSE, stroke_width=1, font_size=28),
            Text("（周期 4）；再由偶函数 ", font=FONT_CN, color=CLR_SKY, font_size=24),
            MathTex(r"f(-\frac{5}{2})=f(\frac{5}{2})", color=CLR_ROSE, stroke_width=1, font_size=28),
        ).arrange(RIGHT, buff=0.08)
        e8_3.next_to(s8_3, DOWN, buff=0.15, aligned_edge=LEFT)

        self.play(Write(s8_3))
        self.wait(0.5)
        self.play(Write(e8_3))
        self.wait(2)
        self.play(FadeOut(e8_3))

        # === Step 4：代入公式求 a ===
        s8_4 = MathTex(r"\frac{9}{4}+\frac{3}{2}a+b = \frac{25}{4}+\frac{5}{2}a+b",
                       color=BLUE, stroke_width=1, font_size=33)
        s8_4.next_to(s8_3, DOWN, buff=0.2, aligned_edge=LEFT)
        

        self.play(Write(s8_4))
        self.wait(2)
        

        s8_5 = MathTex(r"\Rightarrow a=-4", color=BLUE, stroke_width=1, font_size=33)
        s8_5.next_to(s8_4, RIGHT, buff=0.2)
        self.play(Write(s8_5))
        self.wait(1)

        # === Step 5：求 f(1)=0 ===
        s8_6 = VGroup(
            Text("Step 4：原式令 x=1：", font=FONT_CN, color=CLR_CREAM, font_size=28),
            MathTex(r"f(1)+f(-1)=0", color=BLUE, stroke_width=1, font_size=33),
            Text("，偶函数 f(-1)=f(1) ⇒ ", font=FONT_CN, color=CLR_CREAM, font_size=28),
            MathTex(r"f(1)=0", color=BLUE, stroke_width=1, font_size=33),
        ).arrange(RIGHT, buff=0.1)
        s8_6.next_to(s8_4, DOWN, buff=0.3).align_to(s8_3, LEFT)

        e8_6 = VGroup(
            Text(" 令 x=1：f(1)+f(-1)=0。偶函数 f(-1)=f(1)，故 2f(1)=0 ⇒ f(1)=0",
                  font=FONT_CN, color=CLR_SKY, font_size=24),
        ).arrange(RIGHT, buff=0.08)
        e8_6.next_to(s8_6, DOWN, buff=0.15, aligned_edge=LEFT)

        self.play(Write(s8_6))
        self.wait(1)
        self.play(Write(e8_6))
        self.wait(2)
        self.play(FadeOut(e8_6))

        # === Step 6：由 f(3)=0 求 b ===
        s8_7 = VGroup(
            Text("Step 6：", font=FONT_CN, color=CLR_CREAM, font_size=28),
            MathTex(r"f(x+2)=-f(x)", color=BLUE, stroke_width=1, font_size=33),
            Text(" 令 x=1 ⇒ ", font=FONT_CN, color=CLR_CREAM, font_size=28),
            MathTex(r"f(3)=-f(1)=0", color=BLUE, stroke_width=1, font_size=33),
        ).arrange(RIGHT, buff=0.1)
        s8_7.next_to(s8_6, DOWN, buff=0.3, aligned_edge=LEFT)

        e8_7 = VGroup(
            Text("3∈[3/2,3]，代入公式：", font=FONT_CN, color=CLR_SKY, font_size=24),
            MathTex(r"f(3)=9+3a+b=0", color=CLR_ROSE, stroke_width=1, font_size=28),
            Text("，a=-4 ⇒ ", font=FONT_CN, color=CLR_SKY, font_size=24),
            MathTex(r"9-12+b=0 \Rightarrow b=3", color=CLR_ROSE, stroke_width=1, font_size=28),
        ).arrange(RIGHT, buff=0.08)
        e8_7.next_to(s8_7, DOWN, buff=0.15, aligned_edge=LEFT)

        self.play(Write(s8_7))
        self.wait(1)
        self.play(Write(e8_7))
        self.wait(2)
        self.play(FadeOut(e8_7))

        # === 结论 ===
        s8_8 = MathTex(r"a=-4,\;b=3", color=CLR_ROSE, stroke_width=1, font_size=41)
        s8_8.next_to(s8_7, DOWN, buff=0.1)

        self.play(Write(s8_8))
        self.wait(2)


class Q9(Scene):
    def construct(self):
        title,titlePos=AddTitle(self,"圆的方程 圆与圆的位置关系",font_size=31)
        self.play(title)

        q9=problems.problem_09()
        q9.next_to(titlePos,DOWN,buff=.7).align_to(titlePos,LEFT)
        self.play(Write(q9))

        # === 配方求 ⊙A 圆心半径 ===
        s9_1 = VGroup(
            Text("配方求 圆A 的圆心和半径", font=FONT_CN, color=CLR_CREAM, font_size=28),
        )
        s9_1.next_to(q9, RIGHT, buff=0.3).align_to(q9, UP)

        s9_2 = MathTex(r"\odot A:\; x^2+y^2-6x-8y+k=0",
                       color=BLUE, stroke_width=1, font_size=33)
        s9_2.next_to(s9_1, DOWN, buff=0.2, aligned_edge=LEFT)

        s9_3 = MathTex(r"\Rightarrow (x-3)^2+(y-4)^2=25-k",
                       color=BLUE, stroke_width=1, font_size=33)
        s9_3.next_to(s9_2, DOWN, buff=0.15, aligned_edge=LEFT)

        s9_4 = VGroup(
            Text("圆心 ", font=FONT_CN, color=CLR_CREAM, font_size=28),
            MathTex(r"A(3,4)", color=BLUE, stroke_width=1, font_size=33),
            Text("，半径 ", font=FONT_CN, color=CLR_CREAM, font_size=28),
            MathTex(r"r=\sqrt{25-k}", color=BLUE, stroke_width=1, font_size=33),
        ).arrange(RIGHT, buff=0.1)
        s9_4.next_to(s9_3, DOWN, buff=0.2, aligned_edge=LEFT)

        
        self.play(LaggedStart(
            Write(s9_1), Write(s9_2), 
            Write(s9_3), Write(s9_4),lag_ratio=.5))
        self.wait(2)

        
        circle_a=s9_3[0][1:].copy().scale(.9).set_color(CLR_ROSE).next_to(
            q9[0][4][0][3],DOWN,buff=.1,aligned_edge=LEFT)

        self.play(ReplacementTransform(
            VGroup(s9_1,s9_2,s9_3,s9_4),
            circle_a)
        )
        
        
        
        
        
        
        
        # === 逐项判断 ===
        # A
        s9_A =Text("✗ ", font=FONT_CN, color=RED, font_size=20)      
        s9_A.next_to(q9[1][0], RIGHT, buff=0.15)
        self.play(Write(s9_A))
        self.wait(1)

        # B        

        e9_B = VGroup(
            Text("k=9 ⇒ ", font=FONT_CN, color=CLR_SKY, font_size=24),
            MathTex(r"r=\sqrt{25-9}=4", color=CLR_ROSE, stroke_width=1, font_size=28),
            Text("，圆心 A(3,4) 到 x 轴距离 = |4| = 4 = r ⇒ 相切 ✓",
                  font=FONT_CN, color=CLR_SKY, font_size=24),
        ).scale(1.3).arrange(RIGHT, buff=0.08)
        e9_B.next_to(q9[1], DOWN, buff=0.7, aligned_edge=LEFT)

        optionB=Text("✓",font=FONT_CN, color=RED, font_size=20,
                     stroke_width=1,stroke_color=RED
                     ).next_to(q9[1][1], RIGHT, buff=0.15)

        self.play( Write(e9_B))
        self.wait(2)
        self.play(ReplacementTransform(e9_B,optionB))
        self.wait(1)



        # C
        e9_C = VGroup(
            Text("k=−11 ⇒ ", font=FONT_CN, color=CLR_SKY, font_size=24),
            MathTex(r"r_A=\sqrt{25-(-11)}=6", color=CLR_ROSE, stroke_width=1, font_size=28),
            Text("，两圆圆心距：|OA|=5，",
                  font=FONT_CN, color=CLR_SKY, font_size=24),
            MathTex(r"r_A-r_o=5=|OA|", color=CLR_ROSE, stroke_width=1, font_size=28),
            Text("，内切",
                              font=FONT_CN, color=CLR_SKY, font_size=24),
        ).arrange(RIGHT, buff=0.08).scale(1.3)
        e9_C.next_to(q9[1], DOWN, buff=0.5, aligned_edge=LEFT)

        optionC=Text("✓",font=FONT_CN, color=RED, font_size=20,
                     stroke_width=1,stroke_color=RED
                     ).next_to(q9[1][2], RIGHT, buff=0.15)

        self.play(Write(e9_C))
        self.wait(1.5)
        self.play(ReplacementTransform(e9_C,optionC))

        # D
        

        e9_D = VGroup(
            Text("两圆相减得根轴：", font=FONT_CN, color=CLR_SKY, font_size=24),
            MathTex(r"6x+8y-k-1=0", color=CLR_ROSE, stroke_width=1, font_size=28),
            Text("，非 k−2 ⇒ ✗", font=FONT_CN, color=CLR_SKY, font_size=24),
        ).arrange(RIGHT, buff=0.08).scale(1.3)
        e9_D.next_to(q9[1], DOWN, buff=0.5, aligned_edge=LEFT)

        optionD=Text("✗",font=FONT_CN, color=RED, font_size=20,
                     stroke_width=1,stroke_color=RED
                     ).next_to(q9[1][3], RIGHT, buff=0.15)
        self.play(Write(e9_D))
        self.wait(1.5)
        self.play(ReplacementTransform(e9_D,optionD))

        self.wait(2)


class Q10(Scene):
    def construct(self):
        title,titlePos=AddTitle(self,"等比数列 前 n 项和",font_size=31)
        self.play(title)

        q10=problems.problem_10(option_layout="row")
        q10.next_to(titlePos,DOWN,buff=.7).align_to(titlePos,LEFT)

        self.play(Write(q10))

        # === 求公比 q ===
        s10_1 = VGroup(
            Text("由 ", font=FONT_CN, color=CLR_CREAM, font_size=20),
            MathTex(r"2a_3=a_1+a_2", color=BLUE, stroke_width=1, font_size=30),
            Text(" 求公比", font=FONT_CN, color=CLR_CREAM, font_size=20),
        ).arrange(RIGHT, buff=0.1)
        s10_1.next_to(q10[1], DOWN, buff=0.4).align_to(q10, LEFT)

        s10_2 = MathTex(r"2a_1q^2=a_1+a_1q \;\xrightarrow{a_1>0}\; 2q^2=1+q",
                        color=BLUE, stroke_width=1, font_size=30)
        s10_2.next_to(s10_1, DOWN, buff=0.2, aligned_edge=LEFT)

        s10_3 = MathTex(r"2q^2-q-1=0 \;\Rightarrow\; (2q+1)(q-1)=0",
                        color=BLUE, stroke_width=1, font_size=30)
        s10_3.next_to(s10_2, DOWN, buff=0.2, aligned_edge=LEFT)

        s10_4 = VGroup(
            MathTex(r"\because q\neq1 \;\Rightarrow\; q=-\frac{1}{2}", color=CLR_SKY, stroke_width=1, font_size=30),
        )
        s10_4.next_to(s10_3, DOWN, buff=0.2, aligned_edge=LEFT)

        # === 通项与前 n 项和 ===
        s10_5 = MathTex(r"\therefore a_n=a_1\left(-\frac{1}{2}\right)^{n-1}",
                        color=CLR_ROSE, stroke_width=1, font_size=28)
        s10_5.next_to(s10_4, DOWN, buff=0.3,aligned_edge=LEFT)

        s10_6 = MathTex(r"\therefore S_n=\frac{a_1(1-q^n)}{1-q}"
                        r"=\frac{a_1\left[1-\left(-\frac{1}{2}\right)^n\right]}{\frac{3}{2}}"
                        r"=\frac{2a_1}{3}\left[1-\left(-\frac{1}{2}\right)^n\right]",
                        color=CLR_ROSE, stroke_width=1, font_size=20)
        s10_6.next_to(s10_5, DOWN, buff=0.2,aligned_edge=LEFT)

        

        self.play(LaggedStart(
            Write(s10_1), Write(s10_2), Write(s10_3), Write(s10_4),lag_ratio=.8))
        self.wait(1)
        self.play(Write(s10_5))
        self.wait(1)
        self.play(Write(s10_6))

        # === B 选项：右侧分析 ===
        s10_B1 = VGroup(
            Text("B. ", font=FONT_CN, color=CLR_CREAM, font_size=20),
            MathTex(r"S_n>\frac{2}{3}a_1", color=BLUE, stroke_width=1, font_size=25),
            Text(" ？", font=FONT_CN, color=CLR_CREAM, font_size=20),
        ).arrange(RIGHT, buff=0.1)
        s10_B1.next_to(s10_1, RIGHT, buff=4).align_to(s10_1, UP)

        s10_B1_1 = VGroup(
                    MathTex(r"\frac{2}{3}a_1 > 0", color=GOLD, stroke_width=1, font_size=25),
                    Text(" 恒成立。", font=FONT_CN, color=GOLD, font_size=20),
                ).arrange(RIGHT, buff=0.1)
        
        s10_B2 = MathTex(r"S_n=\frac{2a_1}{3}\left[1-\left(-\frac{1}{2}\right)^n\right]",
                         color=BLUE, stroke_width=1, font_size=25)
        s10_B2.next_to(s10_B1, DOWN, buff=0.2, aligned_edge=LEFT)
        s10_B1_1.next_to(s10_B2, RIGHT, buff=0.4)

        s10_B3 = VGroup(
            Text("当 n 为奇数：", font=FONT_CN, color=CLR_SKY, font_size=20),
            MathTex(
                r"\left(-\frac{1}{2}\right)^n<0 \;\Rightarrow\; ",
                r"1-\left(-\frac{1}{2}\right)^n >1 \;\Rightarrow\;",
                r"S_n>\frac{2a_1}{3}",
                    color=CLR_ROSE, stroke_width=1, font_size=25),
        ).arrange(RIGHT, buff=0.1)
        s10_B3.next_to(s10_B2, DOWN, buff=0.2, aligned_edge=LEFT)


        s10_B3_line1=Line(
            s10_B3[1][1][0:9].get_corner(DL), s10_B3[1][1][0:9].get_corner(DR),
            color=CLR_CREAM
        )

        s10_B3_line2=Line(
                    s10_B3[1][1][-2].get_corner(DL), s10_B3[1][1][-2].get_corner(DR),
                    color=CLR_CREAM
                ).align_to(s10_B3_line1, DOWN)

        s10_B3_text1=s10_B1_1[0][0][0:5].copy().next_to(s10_B3_line1, DOWN, buff=0.1)
        s10_B3_text2=s10_B1_1[0][0][0:5].copy().next_to(s10_B3_line2, DOWN, buff=0.1)

        s10_B4 = VGroup(
            Text("当 n 为偶数：", font=FONT_CN, color=CLR_SKY, font_size=20),
            MathTex(
                r"\left(-\frac{1}{2}\right)^n>0 \;\Rightarrow\; ",
                r"1-\left(-\frac{1}{2}\right)^n <1 \;\Rightarrow\;",
                r"S_n<\frac{2a_1}{3}",
                    color=CLR_ROSE, stroke_width=1, font_size=25),
        ).arrange(RIGHT, buff=0.1)
        s10_B4.next_to(s10_B3, DOWN, buff=0.8, aligned_edge=LEFT)
        

        self.play(Write(s10_B1))
        self.wait(1)
        self.play(LaggedStart(            
            Write(s10_B2),Write(s10_B1_1), Write(s10_B3), 
            lag_ratio=.9
        ))
        self.play(LaggedStart(
            Create(s10_B3_line1),
            Create(s10_B3_line2),
            Write(s10_B3_text1),
            Write(s10_B3_text2),
            lag_ratio=.3
            )
        )
        self.wait(.5)


        self.play(LaggedStart(
            Write(s10_B4),lag_ratio=.9
        ))
        self.wait(2)

        # === 清除 B，换 C ===
        b_elements = [s10_B1, s10_B2, s10_B1_1, s10_B3, s10_B3_line1,
                      s10_B3_line2, s10_B3_text1, s10_B3_text2, s10_B4]
        self.play(*[FadeOut(e, shift=RIGHT) for e in b_elements])

        # === C 选项 ===
        s10_C1 = VGroup(
            Text("C. ", font=FONT_CN, color=CLR_CREAM, font_size=20),
            MathTex(r"2S_n+2=S_{n+1}+S_n", color=BLUE, stroke_width=1, font_size=25),
            Text(" ？", font=FONT_CN, color=CLR_CREAM, font_size=20),
        ).arrange(RIGHT, buff=0.1)
        s10_C1.next_to(s10_1, RIGHT, buff=4).align_to(s10_1, UP)

        s10_C2 = VGroup(
            MathTex(r"\because\; 2S_n+2=S_{n+1}+S_n",
                    color=BLUE, stroke_width=1, font_size=25),
            MathTex(r"\therefore\; S_n+2=S_{n+1}",
                    color=BLUE, stroke_width=1, font_size=25),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        s10_C2.next_to(s10_C1, DOWN, buff=0.5, aligned_edge=LEFT)

        s10_C3 = MathTex(r"\therefore\; S_{n+1}-S_n=a_{n+1}=2",
                         color=BLUE, stroke_width=1, font_size=25)
        s10_C3.next_to(s10_C2, DOWN, buff=0.15, aligned_edge=LEFT)

        s10_C4 = VGroup(
            Text("但 ", font=FONT_CN, color=CLR_SKY, font_size=20),
            MathTex(r"a_{n+1}=a_1\left(-\frac{1}{2}\right)^n \neq 2", color=CLR_ROSE, stroke_width=1, font_size=25),
            Text("（与 a₁, n 有关）", font=FONT_CN, color=CLR_SKY, font_size=20),
        ).arrange(RIGHT, buff=0.1)
        s10_C4.next_to(s10_C3, DOWN, buff=0.2, aligned_edge=LEFT)

        s10_C5 = VGroup(
            MathTex(r"\times", color=CLR_CRIMSON, stroke_width=1, font_size=36),
            Text("C 不恒成立", font=FONT_CN, color=CLR_CRIMSON, font_size=24),
        ).arrange(RIGHT, buff=0.15)
        s10_C5.next_to(s10_C4, DOWN, buff=0.2, aligned_edge=LEFT)

        self.play(LaggedStart(
            Write(s10_C1), Write(s10_C2), Write(s10_C3), Write(s10_C4), 
            Write(s10_C5),lag_ratio=.8))
        self.wait(2)

        # === 清除 C，换 D ===
        c_elements = [s10_C1, s10_C2, s10_C3, s10_C4, s10_C5]
        self.play(*[FadeOut(e, shift=RIGHT) for e in c_elements])

        # === D 选项 ===
        s10_D1 = VGroup(
            Text("D. ", font=FONT_CN, color=CLR_CREAM, font_size=20),
            MathTex(r"S_1+S_2+\cdots+S_n>\frac{2n}{3}a_1", color=BLUE, stroke_width=1, font_size=25),
            Text(" ？", font=FONT_CN, color=CLR_CREAM, font_size=20),
        ).arrange(RIGHT, buff=0.1)
        self.play(q10.animate.shift(LEFT*6))
        s10_D1.next_to(q10, RIGHT, buff=0.8).align_to(q10, UP).shift(UP)

        s10_D2 = MathTex(
            r"\because\; S_n=\frac{2a_1}{3}\left[1-\left(-\frac{1}{2}\right)^n\right]",
            color=BLUE, stroke_width=1, font_size=25)
        s10_D2.next_to(s10_D1, DOWN, buff=0.5, aligned_edge=LEFT)

        s10_D2_sum = MathTex(
            r"\therefore\; S_1+S_2+\cdots+S_n",
            color=BLUE, stroke_width=1, font_size=25)
        s10_D2_sum.next_to(s10_D2, DOWN, buff=0.25, aligned_edge=LEFT)

        s10_D2_terms_row1 = VGroup(
            MathTex(r"S_1=\frac{2a_1}{3}\left[1-\left(-\frac{1}{2}\right)\right]",
                    color=BLUE, stroke_width=1, font_size=25),
            MathTex(r"S_2=\frac{2a_1}{3}\left[1-\left(-\frac{1}{2}\right)^2\right]",
                    color=BLUE, stroke_width=1, font_size=25),
        ).arrange(RIGHT, buff=0.6)

        s10_D2_terms_row2 = VGroup(
            MathTex(r"S_3=\frac{2a_1}{3}\left[1-\left(-\frac{1}{2}\right)^3\right]",
                    color=BLUE, stroke_width=1, font_size=25),
            MathTex(r"S_4=\frac{2a_1}{3}\left[1-\left(-\frac{1}{2}\right)^4\right]",
                    color=BLUE, stroke_width=1, font_size=25),
        ).arrange(RIGHT, buff=0.6)

        s10_D2_terms = VGroup(s10_D2_terms_row1, s10_D2_terms_row2)
        s10_D2_terms.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        s10_D2_terms.next_to(s10_D2_sum, DOWN, buff=0.2, aligned_edge=LEFT)

        s10_D2_expand = VGroup(
            MathTex(r"=\frac{2a_1}{3}\Big\{\left[1-\left(-\frac{1}{2}\right)\right]",
                    r"+\left[1-\left(-\frac{1}{2}\right)^2\right]",
                    r"+\cdots",
                    r"+\left[1-\left(-\frac{1}{2}\right)^n\right]\Big\}",
                    color=RED, stroke_width=1, font_size=25),
            MathTex(r"=\frac{2a_1}{3}\Big\{n-\Big[\left(-\frac{1}{2}\right)"
                    r"+\left(-\frac{1}{2}\right)^2"
                    r"+\left(-\frac{1}{2}\right)^3"
                    r"+\left(-\frac{1}{2}\right)^4"
                    r"+\cdots"
                    r"+\left(-\frac{1}{2}\right)^n\Big]\Big\}",
                    color=CLR_MINT, stroke_width=1, font_size=25),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        s10_D2_expand.next_to(s10_D2_terms, DOWN, buff=0.25, aligned_edge=LEFT).shift(LEFT*.8)

        s10_D2_underline_targets = VGroup(
            s10_D2_expand[0][0][10:16],
            s10_D2_expand[0][1][4:10],
            s10_D2_expand[0][3][4:10],
        )
        s10_D2_underline_lines = VGroup()
        for target in s10_D2_underline_targets:
            line = Underline(target, color=BLUE, stroke_width=5, buff=0.1)
            s10_D2_underline_lines.add(line)

        s10_D2_final = VGroup(
            MathTex(r"\therefore\; S_1+S_2+\cdots+S_n",
                    color=BLUE, stroke_width=1, font_size=25),
            MathTex(r"=\frac{2a_1}{3}\left\{n-\left[\left(-\frac{1}{2}\right)"
                    r"+\left(-\frac{1}{2}\right)^2+\cdots"
                    r"+\left(-\frac{1}{2}\right)^n\right]\right\}",
                    color=BLUE, stroke_width=1, font_size=25),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        s10_D2_final.next_to(s10_D2, DOWN, buff=0.15, aligned_edge=LEFT)

        s10_D3 = VGroup(
            Text("由等比数列求和公式：", font=FONT_CN, color=CLR_SKY, font_size=20),
            MathTex(r"\left(-\frac{1}{2}\right)+\cdots+\left(-\frac{1}{2}\right)^n"
                    r"=\frac{-\frac{1}{2}\left[1-\left(-\frac{1}{2}\right)^n\right]}"
                    r"{1+\frac{1}{2}}"
                    r"=-\frac{1}{3}\left[1-\left(-\frac{1}{2}\right)^n\right]",
                    color=CLR_SKY, stroke_width=1, font_size=25),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        s10_D3.next_to(s10_D2_final, DOWN, buff=0.2, aligned_edge=LEFT)

        s10_D4 = VGroup(
            MathTex(r"\therefore\; S_1+\cdots+S_n"
                    r"=\frac{2a_1}{3}\left\{n+\frac{1}{3}"
                    r"\left[1-\left(-\frac{1}{2}\right)^n\right]\right\}",
                    color=BLUE, stroke_width=1, font_size=25),
            MathTex(r"=\frac{2n}{3}a_1+\frac{2a_1}{9}\left[1-\left(-\frac{1}{2}\right)^n\right]",
                    color=BLUE, stroke_width=1, font_size=25),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        s10_D4.next_to(s10_D3, DOWN, buff=0.2, aligned_edge=LEFT)


        tmpText=MathTex(
            r"S_1+S_2+\cdots+S_n",
            color=CLR_CREAM, stroke_width=1, font_size=30
        ).next_to(s10_D4[0], DOWN, buff=0.3, aligned_edge=LEFT).align_to(s10_D4[1],ORIGIN)

        s10_D5 = VGroup(
            MathTex(r"\because\; 1-\left(-\frac{1}{2}\right)^n>0",
                    color=CLR_SKY, stroke_width=1, font_size=25),
            Text(" 且 ", font=FONT_CN, color=CLR_SKY, font_size=20),
            MathTex(r"a_1>0", color=CLR_SKY, stroke_width=1, font_size=25),
        ).arrange(RIGHT, buff=0.1)
        s10_D5.next_to(s10_D4, DOWN, buff=0.2, aligned_edge=LEFT)

        s10_D6 = VGroup(
            MathTex(r"\therefore\; S_1+\cdots+S_n>\frac{2n}{3}a_1",
                    color=CLR_ROSE, stroke_width=1, font_size=25),
            Text(" 恒成立", font=FONT_CN, color=CLR_ROSE, font_size=20),
        ).arrange(RIGHT, buff=0.1)
        s10_D6.next_to(s10_D5, RIGHT, buff=0.25)

        self.play(q10[1][3].animate.set_color(YELLOW))

        self.play(LaggedStart(
            Write(s10_D1), Write(s10_D2),
            lag_ratio=.8))
        self.wait(0.5)

        self.play(Write(s10_D2_sum))
        self.wait(0.3)

        self.play(LaggedStart(
            Write(s10_D2_terms_row1),
            Write(s10_D2_terms_row2),
            lag_ratio=.4))
        self.wait(1)

        self.play(
            Write(s10_D2_expand),
            )
        self.wait(2)

        s10_D2_expand_rec=EmphasizeTexts(self,
                    [s10_D2_expand[0][0][8],
                     s10_D2_expand[0][1][2],
                     s10_D2_expand[0][3][2]],color=CLR_CREAM,buff=.1
        )

        self.play(LaggedStart(
            *[Create(line) for line in s10_D2_underline_lines],
            lag_ratio=.5
        ))

        self.play(LaggedStart(
            FadeOut(s10_D2_sum, shift=RIGHT),
            FadeOut(s10_D2_terms, shift=RIGHT),
            Uncreate(s10_D2_expand_rec),
            Uncreate(s10_D2_underline_lines),
            FadeOut(s10_D2_expand, shift=RIGHT),
            Write(s10_D2_final),lag_ratio=.5)
        )
        self.wait(0.5)

        self.play(LaggedStart(
            Write(s10_D3), Write(s10_D4),            
            lag_ratio=.8))


        self.play(LaggedStart(
            s10_D4[1].animate.shift(RIGHT*2.8),
            Write(tmpText),
            lag_ratio=.5
        ))
        
        self.play(LaggedStart(
            Write(s10_D5), Write(s10_D6),
            lag_ratio=.8)
        )
        self.wait(2)


class Q11(Scene):
    def construct(self):
        title,titlePos=AddTitle(self,"抛物线性质 直线与抛物线",font_size=31)
        self.play(title)

        q11=problems.problem_11(wrap_after=9)
        q11.next_to(titlePos,DOWN,buff=.7).align_to(titlePos,LEFT)
        self.play(Write(q11))
        self.wait(2)

        # A        
        e11_A=VGroup(
            MathTex(r"y^2=8x, \; p=4 ;\;",color=CLR_ROSE,stroke_width=1,font_size=28),
            Text(" 准线: ",font=FONT_CN,color=CLR_SKY,font_size=24),
            MathTex(r"x=-\frac{p}{2}=-2",color=CLR_ROSE,stroke_width=1,font_size=28),
            Text(" ✓",font=FONT_CN,color=RED,font_size=20),
        ).arrange(RIGHT,buff=.08).scale(1.3)
        e11_A.next_to(q11[1][0],RIGHT,)
        self.play(Write(e11_A))
        self.wait(1)

        optionA=Text("✓",font=FONT_CN,color=RED,font_size=20,
                     stroke_width=1,stroke_color=RED
                     ).next_to(q11[1][0],RIGHT,buff=.15)
        self.play(ReplacementTransform(e11_A,optionA))
        q11.add(optionA)
        self.wait(1)

        self.play(LaggedStart(
                    FadeOut(q11[1][2],shift=LEFT), 
                    FadeOut(q11[1][3],shift=LEFT),            
                    lag_ratio=.5
                ))

        # B: 直线 l 与抛物线 C 无交点
        e11_B1 = VGroup(
            Text("B. ", font=FONT_CN, color=CLR_CREAM, font_size=20),
            Text("直线 ", font=FONT_CN, color=CLR_SKY, font_size=24),
            MathTex(r"l: y=k(x+1)", color=CLR_ROSE, stroke_width=1, font_size=28),
            Text(" 与抛物线 ", font=FONT_CN, color=CLR_SKY, font_size=24),
            MathTex(r"C: y^2=8x", color=CLR_ROSE, stroke_width=1, font_size=28),
        ).arrange(RIGHT, buff=0.08).scale(1.3)
        e11_B1.next_to(q11[1][1], DOWN, buff=0.4, aligned_edge=LEFT)

        e11_B2 = MathTex(
            r"\begin{cases} y=k(x+1) \\ y^2=8x \end{cases}",
            color=CLR_CREAM, stroke_width=1, font_size=28,
        ).scale(1.3)
        e11_B2.next_to(e11_B1, DOWN, buff=0.2, aligned_edge=LEFT)

        e11_B3 = VGroup(
            Text("消去 ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"y", color=CLR_CREAM, stroke_width=1, font_size=28),
            Text("：", font=FONT_CN, color=CLR_SKY, font_size=24),
            MathTex(r"[k(x+1)]^2=8x", color=CLR_CREAM, stroke_width=1, font_size=28),
        ).arrange(RIGHT, buff=0.08).scale(1.3)
        e11_B3.next_to(e11_B2, DOWN, buff=0.2,aligned_edge=LEFT)

        e11_B4 = MathTex(
            r"k^2(x^2+2x+1)=8x",
            color=CLR_CREAM, stroke_width=1, font_size=28,
        ).scale(1.3)
        e11_B4.next_to(e11_B3[3], DOWN, buff=0.15, aligned_edge=LEFT)

        e11_B5 = MathTex(
            r"k^2x^2+(2k^2-8)x+k^2=0",
            color=CLR_CREAM, stroke_width=1, font_size=28,
        ).scale(1.3)
        e11_B5.next_to(e11_B4, DOWN, buff=0.15, aligned_edge=LEFT)

        e11_B6 = VGroup(
            Text("无交点 ", font=FONT_CN, color=CLR_SKY, font_size=24),
            MathTex(r"\Rightarrow\; \Delta<0", color=CLR_ROSE, stroke_width=1, font_size=28),
        ).arrange(RIGHT, buff=0.08).scale(1.3)
        e11_B6.next_to(e11_B2, RIGHT, buff=4,aligned_edge=UP)

        e11_B7 = MathTex(
            r"\Delta = (2k^2-8)^2 - 4k^2\cdot k^2",
            color=CLR_CREAM, stroke_width=1, font_size=28,
        ).scale(1.3)
        e11_B7.next_to(e11_B6, DOWN, buff=0.15, aligned_edge=LEFT)

        e11_B8 = MathTex(
            r"= 4k^4-32k^2+64-4k^4 = -32k^2+64",
            color=CLR_CREAM, stroke_width=1, font_size=28,
        ).scale(1.3)
        e11_B8.next_to(e11_B7, DOWN, buff=0.15, aligned_edge=LEFT)

        e11_B9 = MathTex(
            r"\Delta < 0 \;\Rightarrow\; -32k^2+64 < 0 \;\Rightarrow\; k^2 > 2",
            color=CLR_CREAM, stroke_width=1, font_size=28,
        ).scale(1.3)
        e11_B9.next_to(e11_B8, DOWN, buff=0.2, aligned_edge=LEFT)

        e11_B10 = VGroup(
            Text("由题 ", font=FONT_CN, color=CLR_SKY, font_size=24),
            MathTex(r"k>0, ", color=CLR_CREAM, stroke_width=1, font_size=28),
            MathTex(r"\therefore\; k>\sqrt{2}", color=CLR_ROSE, stroke_width=1, font_size=28),
            Text(" ✓", font=FONT_CN, color=RED, font_size=20),
        ).arrange(RIGHT, buff=0.08).scale(1.3)
        e11_B10.next_to(e11_B9, DOWN, buff=0.2, aligned_edge=LEFT)

        self.play(LaggedStart(
            Write(e11_B1), Write(e11_B2), lag_ratio=.8))
        self.wait(0.5)
        self.play(LaggedStart(
            Write(e11_B3), Write(e11_B4), Write(e11_B5),
            lag_ratio=.8))
        self.wait(0.5)
        self.play(LaggedStart(
            Write(e11_B6), Write(e11_B7), Write(e11_B8), Write(e11_B9),
            lag_ratio=.8))
        self.wait(0.5)
        self.play(Write(e11_B10))
        self.wait(1.5)       

        optionB=Text("✓",font=FONT_CN,color=RED,font_size=20,
                             stroke_width=1,stroke_color=RED
                             ).next_to(q11[1][1],RIGHT,buff=.15)

        b_elements =VGroup (e11_B1, e11_B2, e11_B3, e11_B4, e11_B5,
                      e11_B6, e11_B7, e11_B8, e11_B9, e11_B10)
        self.play(ReplacementTransform(b_elements, optionB))
        q11.add(optionB)

        self.play(FadeIn(q11[1][2],shift=RIGHT))

        # C: l 与 C 相切时，AB 过焦点 F
        e11_C1 = VGroup(
            Text("由 ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"\Delta=-32k^2+64=0\;\Rightarrow\; k=\sqrt{2}", color=CLR_ROSE, stroke_width=1, font_size=28),
        ).arrange(RIGHT, buff=0.08).scale(1.1)

        self.play(q11.animate.shift(LEFT*5))
        e11_C1.next_to(q11, RIGHT, buff=0.5,aligned_edge=UP)

        e11_C2 = VGroup(
            MathTex(r"k=\sqrt{2}", color=CLR_ROSE, stroke_width=1, font_size=28),
            Text(" 代入联立方程可得：：", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"x^2-2x+1=0", color=CLR_CREAM, stroke_width=1, font_size=28),
        ).arrange(RIGHT, buff=0.08).scale(1.1)
        e11_C2.next_to(e11_C1, DOWN, buff=0.2, aligned_edge=LEFT)

        e11_C3 = VGroup(
            Text("解得：", font=FONT_CN, color=CLR_SKY, font_size=24),
            MathTex(r"x=1 \;\Rightarrow\;  y=\sqrt{2}(x+1)=2\sqrt{2}", color=CLR_CREAM, stroke_width=1, font_size=28),
        ).arrange(RIGHT, buff=0.08).scale(1.1)
        e11_C3.next_to(e11_C2, DOWN, buff=0.15, aligned_edge=LEFT)

        e11_C4 = VGroup(
            Text("B 即切点:  ", font=FONT_CN, color=CLR_SKY, font_size=24),
            MathTex(r"B(1,2\sqrt{2})", color=CLR_ROSE, stroke_width=1, font_size=28),
        ).arrange(RIGHT, buff=0.08).scale(1.1)
        e11_C4.next_to(e11_C3, DOWN, buff=0.15, aligned_edge=LEFT)

        # === 示意图：等边三角形 + 切线 l ===
        sketch_l = Line(LEFT * 1.8, RIGHT * 1.8, color=CLR_SKY, stroke_width=2.5)
        sketch_l.next_to(q11[1][2], RIGHT, buff=0.6).shift(DOWN * 0.3)
        lbl_l = MathTex(r"l", color=RED, font_size=29,stroke_width=1).next_to(sketch_l, UP, buff=0.1).shift(LEFT*.4)

        sketch_B = Dot(sketch_l.get_center() + LEFT * 0.9, color=CLR_SALMON, radius=0.09)
        sketch_C = Dot(sketch_l.get_center() + RIGHT * 0.9, color=CLR_SALMON, radius=0.09)
        lbl_B = MathTex(r"B", color=CLR_SALMON, font_size=26,stroke_width=1).next_to(sketch_B, DOWN, buff=0.12)
        lbl_C = MathTex(r"C", color=CLR_SALMON, font_size=26,stroke_width=1).next_to(sketch_C, DOWN, buff=0.12)

        sketch_A = Dot(sketch_l.get_center() + UP * 1.5, color=CLR_ROSE, radius=0.09)
        lbl_A = MathTex(r"A", color=CLR_ROSE, font_size=26,stroke_width=1).next_to(sketch_A, UP, buff=0.08)

        sketch_AB = Line(sketch_A.get_center(), sketch_B.get_center(), color=CLR_CREAM, stroke_width=4)
        sketch_AC = Line(sketch_A.get_center(), sketch_C.get_center(), color=CLR_CREAM, stroke_width=4)

        sketch_F = Dot(sketch_AB.point_from_proportion(0.35), color=YELLOW, radius=0.08)
        lbl_F = MathTex(r"F", color=YELLOW, font_size=26, stroke_width=1).next_to(sketch_F, DR, buff=0.08)

        sketch = VGroup(sketch_l, lbl_l, sketch_B, lbl_B, sketch_C, lbl_C,
                        sketch_A, lbl_A, sketch_AB, sketch_AC, sketch_F, lbl_F)

        # sketch plays moved after e11_C1-C4        
        e11_C5b = VGroup(
            Text("若 C 成立 ⇒ A,B,F 共线。", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"F(2,0),\; B(1,2\sqrt{2})", color=CLR_ROSE, stroke_width=1, font_size=28),
            Text(" 确定直线 BF", font=FONT_CN, color=CLR_SKY, font_size=22),
        ).arrange(RIGHT, buff=0.08).scale(1.1)
        e11_C5b.next_to(e11_C4, DOWN, buff=0.25, aligned_edge=LEFT)

        # === BF 与 E 求交点 ===
        e11_d1 = VGroup(
            Text("BF: ", font=FONT_CN, color=CLR_TEAL, font_size=22),
            MathTex(r"y=-2\sqrt{2}(x-2)", color=CLR_CREAM, stroke_width=1, font_size=26),
        ).arrange(RIGHT, buff=0.08).scale(.8)
        e11_d1.next_to(e11_C5b, DOWN, buff=0.15, aligned_edge=LEFT)

        e11_d2 = VGroup(
            Text("联立 ", font=FONT_CN, color=CLR_TEAL, font_size=22),
            MathTex(r"y^2=8x", color=CLR_CREAM, stroke_width=1, font_size=26),
            Text("：", font=FONT_CN, color=CLR_TEAL, font_size=22),
            MathTex(r"8(x-2)^2=8x \Rightarrow x^2-5x+4=0", color=CLR_CREAM, stroke_width=1, font_size=26),
        ).arrange(RIGHT, buff=0.08).scale(.8)
        e11_d2.next_to(e11_d1, DOWN, buff=0.12, aligned_edge=LEFT)

        e11_d3 = VGroup(
            Text("解得 ", font=FONT_CN, color=CLR_TEAL, font_size=22),
            MathTex(r"x=1", color=CLR_CREAM, stroke_width=1, font_size=26),
            Text("（即 B）或 ", font=FONT_CN, color=CLR_TEAL, font_size=22),
            MathTex(r"x=4 \Rightarrow A(4,-4\sqrt{2})", color=CLR_CREAM, stroke_width=1, font_size=26),
        ).arrange(RIGHT, buff=0.08).scale(.8)
        e11_d3.next_to(e11_d2, DOWN, buff=0.12, aligned_edge=LEFT)

        e11_d4 = VGroup(
            Text("|AB| = 9，等边 ⇒ |BC| = 9。C 在 l 上：", font=FONT_CN, color=CLR_TEAL, font_size=22),
            MathTex(r"C=(x,\sqrt{2}(x+1))", color=CLR_CREAM, stroke_width=1, font_size=26),
        ).arrange(RIGHT, buff=0.08).scale(.8)
        e11_d4.next_to(e11_d3, DOWN, buff=0.12, aligned_edge=LEFT)

        e11_d5 = VGroup(
            MathTex(r"|BC|^2=(x-1)^2+(\sqrt{2}(x+1)-2\sqrt{2})^2=3(x-1)^2=81", color=CLR_CREAM, stroke_width=1, font_size=26),
        ).arrange(RIGHT, buff=0.08).scale(.8)
        e11_d5.next_to(e11_d4, DOWN, buff=0.12, aligned_edge=LEFT)

        e11_d6 = VGroup(
            Text("⇒ ", font=FONT_CN, color=CLR_TEAL, font_size=22),
            MathTex(r"x=1\pm3\sqrt{3},\; C(1\pm3\sqrt{3},\;2\sqrt{2}\pm3\sqrt{6})", color=CLR_CREAM, stroke_width=1, font_size=26),
        ).arrange(RIGHT, buff=0.08).scale(.8)
        e11_d6.next_to(e11_d5, DOWN, buff=0.12, aligned_edge=LEFT)

        # derivation plays moved

        e11_C6 = VGroup(
            Text("验证 ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"|AC|^2=162+54\sqrt{3}\neq 81", color=CLR_ROSE, stroke_width=1, font_size=26),
            Text("，非等边！", font=FONT_CN, color=CLR_SKY, font_size=22),
        ).arrange(RIGHT, buff=0.08).scale(.9)
        e11_C6.next_to(e11_d6, DOWN, buff=0.2, aligned_edge=LEFT)

        e11_C7 = VGroup(
            MathTex(r"\times", color=CLR_CRIMSON, stroke_width=1, font_size=36),
            Text("C 不正确", font=FONT_CN, color=CLR_CRIMSON, font_size=24),
        ).arrange(RIGHT, buff=0.15).scale(1.1)
        e11_C7.next_to(e11_C6, DOWN, buff=0.2, aligned_edge=LEFT)


        # ① 切点 T
        self.play(LaggedStart(
            Write(e11_C1), Write(e11_C2), Write(e11_C3), Write(e11_C4),
            lag_ratio=.8))
        self.wait(0.5)

        # ② 示意图（1 秒画完）
        self.play(AnimationGroup(
            Create(sketch_l), Write(lbl_l),
            Create(sketch_B), Write(lbl_B), Create(sketch_C), Write(lbl_C),
            Create(sketch_A), Write(lbl_A),
            Create(sketch_AB), Create(sketch_AC),
            Create(sketch_F), Write(lbl_F),
        ), run_time=1)
        self.wait(0.5)

        # ③ 假设 C 成立 ⇒ A,B,F 共线
        self.play(LaggedStart(
            Write(e11_C5b),
            lag_ratio=.8))
        self.wait(0.5)
       

        self.play(Write(e11_d1))
        self.wait(0.3)
        self.play(Write(e11_d2))
        self.wait(0.3)
        self.play(Write(e11_d3))
        self.wait(0.3)
        self.play(Write(e11_d4))
        self.wait(0.3)
        self.play(Write(e11_d5))
        self.wait(0.3)
        self.play(Write(e11_d6))
        self.wait(1)

        # ⑤ 验证 |AC| → 矛盾
        self.play(LaggedStart(
            Write(e11_C6), Write(e11_C7),
            lag_ratio=.8))
        self.wait(2)

        # FadeOut C 选项全部内容
        c_all = VGroup(e11_C1, e11_C2, e11_C3, e11_C4, e11_C5b,
                       e11_d1, e11_d2, e11_d3, e11_d4, e11_d5, e11_d6,
                       e11_C6, e11_C7, sketch)
        self.play(FadeOut(c_all, shift=RIGHT))

        self.play(q11.animate.shift(RIGHT*5))
        self.wait(0.5)
        optionDpos=q11[1][0].get_center()
        self.play(LaggedStart(
            FadeOut(optionA,optionB),
            FadeOut(q11[1][0],shift=LEFT),
            FadeOut(q11[1][1],shift=LEFT),
            FadeOut(q11[1][2],shift=LEFT),
            q11[1][3].animate.move_to(optionDpos).set_color(CLR_SKY),
            lag_ratio=.3
        ))

        # === D 选项：k=2 时 △ABC 面积最小值 ===
        e11_D1 = VGroup(
            MathTex(r"k=2", color=CLR_ROSE, stroke_width=1, font_size=26),
            Text(" 时，", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"l:\; 2x-y+2=0", color=CLR_CREAM, stroke_width=1, font_size=26),
        ).arrange(RIGHT, buff=0.08).scale(1.1)
        e11_D1.next_to(q11[1][3], DOWN, buff=0.2, aligned_edge=LEFT)

        e11_D2 = VGroup(
            Text("设 A 点坐标：", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"A(2t^2,4t),", color=CLR_ROSE, stroke_width=1, font_size=26),
        ).arrange(RIGHT, buff=0.08).scale(1.1)
        e11_D2.next_to(e11_D1, DOWN, buff=0.2, aligned_edge=LEFT)

        e11_D3 = VGroup(
            Text(" 则 ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"A", color=CLR_ROSE, stroke_width=1, font_size=26),
            Text(" 到 ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"l", color=CLR_ROSE, stroke_width=1, font_size=26),
            Text(" 的距离：", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"d=\frac{|4t^2-4t+2|}{\sqrt{5}}",
                    color=CLR_CREAM, stroke_width=1, font_size=26),
        ).arrange(RIGHT, buff=0.08).scale(1.1)
        e11_D3.next_to(e11_D2, RIGHT, buff=0.2)

        e11_D4 = VGroup(
            MathTex(r"4t^2-4t+2=4\Big(t-\tfrac{1}{2}\Big)^2+1\ge 1>0",
                    color=CLR_CREAM, stroke_width=1, font_size=26),
        ).scale(1.1)
        e11_D4.next_to(e11_D3, RIGHT, buff=0.15)

        e11_D5 = VGroup(
            Text("等边三角形面积：", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"S=\tfrac{\sqrt{3}}{3}d^2",
                    color=CLR_ROSE, stroke_width=1, font_size=26),
        ).arrange(RIGHT, buff=0.08).scale(1.1)
        e11_D5.next_to(e11_D2, DOWN, buff=0.2, aligned_edge=LEFT)

        e11_D6 = VGroup(
            MathTex(r"S=\frac{\sqrt{3}}{15}\big(4t^2-4t+2\big)^2",
                    color=CLR_CREAM, stroke_width=1, font_size=26),
        ).scale(1.1)
        e11_D6.next_to(e11_D5, DOWN, buff=0.15, aligned_edge=LEFT)

        e11_D7 = VGroup(
            MathTex(r"4t^2-4t+2=4\Big(t-\tfrac{1}{2}\Big)^2+1",
                    color=CLR_SKY, stroke_width=1, font_size=26),
            Text("，当 ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"t=\tfrac{1}{2}", color=CLR_ROSE, stroke_width=1, font_size=26),
            Text(" 取最小值 ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"1", color=CLR_ROSE, stroke_width=1, font_size=26),
        ).arrange(RIGHT, buff=0.08).scale(1.1)
        e11_D7.next_to(e11_D6, DOWN, buff=0.2, aligned_edge=LEFT)

        e11_D8 = VGroup(
            MathTex(r"\therefore\; S_{\min}=\frac{\sqrt{3}}{15}",
                    color=CLR_ROSE, stroke_width=1, font_size=28),
            Text("，此时 ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"A\Big(\tfrac{1}{2},2\Big)", color=CLR_ROSE, stroke_width=1, font_size=26),
            Text(" ✓", font=FONT_CN, color=RED, font_size=20),
        ).arrange(RIGHT, buff=0.08).scale(1.1)
        e11_D8.next_to(e11_D7, DOWN, buff=0.2, aligned_edge=LEFT)

        self.play(Write(e11_D1))
        self.wait(0.3)
        self.play(LaggedStart(
            Write(e11_D2), Write(e11_D3), Write(e11_D4),
            lag_ratio=.8))
        self.wait(0.5)
        self.play(LaggedStart(
            Write(e11_D5), Write(e11_D6), Write(e11_D7),
            lag_ratio=.8))
        self.wait(0.5)
        self.play(Write(e11_D8))
        self.wait(2)


class Q12(Scene):
    def construct(self):
        title,titlePos=AddTitle(self,"等差数列 求和",font_size=31)
        self.play(title)

        q12=problems.problem_12()
        q12.next_to(titlePos,DOWN,buff=.7).align_to(titlePos,LEFT)
        self.play(Write(q12))

        s12_1 = VGroup(
            Text("由 ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"a_4=a_1+3d", color=CLR_ROSE, stroke_width=1, font_size=28),
            Text(" ⇒ ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"5=-1+3d \;\Rightarrow\; d=2", color=CLR_ROSE, stroke_width=1, font_size=28),
        ).arrange(RIGHT, buff=0.08)
        s12_1.next_to(q12, DOWN, buff=0.5, aligned_edge=LEFT)

        s12_2 = MathTex(r"S_6=\frac{6}{2}(2a_1+5d)=3(-2+10)=24",
                        color=CLR_ROSE, stroke_width=1, font_size=33)
        s12_2.next_to(s12_1, DOWN, buff=0.3, aligned_edge=LEFT)

        self.play(Write(s12_1))
        self.wait(0.5)
        self.play(Write(s12_2))
        self.wait(2)


class Q13(Scene):
    def construct(self):
        title,titlePos=AddTitle(self,"函数零点 换元",font_size=31)
        self.play(title)

        q13=problems.problem_13()
        q13.next_to(titlePos,DOWN,buff=.7).align_to(titlePos,LEFT)
        self.play(Write(q13))

        s13_1 = VGroup(
            Text("令 ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"t=2^x>0", color=CLR_ROSE, stroke_width=1, font_size=28),
            Text("，则 ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"f(x)=t+\frac{4}{t}-m", color=CLR_ROSE, stroke_width=1, font_size=28),
        ).arrange(RIGHT, buff=0.08)
        s13_1.next_to(q13, DOWN, buff=0.5, aligned_edge=LEFT)

        s13_2 = VGroup(
            Text("两零点 ⇔ ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"t+\frac{4}{t}=m", color=CLR_ROSE, stroke_width=1, font_size=28),
            Text(" 有两个正根", font=FONT_CN, color=CLR_SKY, font_size=22),
        ).arrange(RIGHT, buff=0.08)
        s13_2.next_to(s13_1, DOWN, buff=0.2, aligned_edge=LEFT)

        s13_3 = VGroup(
            Text("由均值不等式：", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"t+\frac{4}{t}\ge 2\sqrt{t\cdot\frac{4}{t}}=4", color=CLR_ROSE, stroke_width=1, font_size=28),
            Text("，t=2 时取等", font=FONT_CN, color=CLR_SKY, font_size=22),
        ).arrange(RIGHT, buff=0.08)
        s13_3.next_to(s13_2, DOWN, buff=0.2, aligned_edge=LEFT)

        s13_4 = MathTex(r"\therefore\; m>4",
                        color=CLR_ROSE, stroke_width=1, font_size=36)
        s13_4.next_to(s13_3, DOWN, buff=0.3, aligned_edge=LEFT)

        # === 函数图像 ===
        g_axes = Axes(
            x_range=[0, 7.2, 1], y_range=[0, 16, 4],
            x_length=3.5, y_length=2.5,
            axis_config={"color": GREY, "stroke_width": 3},
            tips=False,
        )
        g_axes.next_to(s13_4, RIGHT, buff=1).shift(DOWN * 0.3+RIGHT*4)

        curve = g_axes.plot(lambda t: t + 4/t, x_range=[.3, 6.9], color=CLR_SKY, stroke_width=4)
        min_dot = Dot(g_axes.c2p(2, 4), color=CLR_ROSE, radius=0.1)
        line_4 = DashedLine(g_axes.c2p(0, 4), g_axes.c2p(6.9, 4), color=GREY, stroke_width=2.5)
        lbl_4 = MathTex(r"4", color=GREY, font_size=30, stroke_width=1).next_to(line_4, LEFT, buff=0.08)

        line_m = DashedLine(g_axes.c2p(0, 6), g_axes.c2p(6.9, 6), color=CLR_ROSE, stroke_width=4)
        lbl_m = MathTex(r"m", color=CLR_ROSE, font_size=28, stroke_width=1).next_to(line_m, LEFT, buff=0.08)

        t1, t2 = 3 - np.sqrt(5), 3 + np.sqrt(5)
        dot1 = Dot(g_axes.c2p(t1, 6), color=BLUE, radius=0.1)
        dot2 = Dot(g_axes.c2p(t2, 6), color=BLUE, radius=0.1)

        # === 播放 ===
        self.play(
            LaggedStart(Write(s13_1), Write(s13_2), Write(s13_3), lag_ratio=0.8),
        )
        self.wait()
        self.play(
            LaggedStart(Create(g_axes), Create(curve), lag_ratio=0.5),
        )
        self.play(
            LaggedStart(Create(line_4), Write(lbl_4), Create(min_dot),
                        Create(line_m), Write(lbl_m), Create(dot1), Create(dot2),
                        lag_ratio=0.4),
        )
        self.play(Write(s13_4))
        self.wait(2)


class Q14(Scene):
    def construct(self):
        title,titlePos=AddTitle(self,"球内接正三角形",font_size=31)
        self.play(title)

        q14=problems.problem_14(wrap_after=14)
        q14.next_to(titlePos,DOWN,buff=.7).align_to(titlePos,LEFT)
        self.play(Write(q14))

        # === 用成熟方案重绘三维截面示意图（含动态演示）===
        ax = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            x_length=5.2,
            y_length=5.2,
            axis_config={"stroke_width": 0},
            tips=False,
        )
        ax.to_edge(RIGHT, buff=0.1).shift(DOWN * 0.25)
        unit = ax.x_axis.unit_size

        R = 1.8                      # 球半径（与 TrirPyrCir 一致）
        O = ax.c2p(0, 0)             # 球心
        D = ax.c2p(0, R)             # 顶点 D 在球最顶端

        # ---- 球体：前实后虚 ----
        sphere = Circle(radius=R * unit, color=CLR_SKY, stroke_width=3)
        sphere.move_to(O)
        sphere_back = Arc(radius=R * unit, start_angle=PI/2, angle=PI,
                          color=GREY, stroke_width=2)
        sphere_back.move_arc_center_to(O)
        sphere_back = DashedVMobject(sphere_back, num_dashes=30)

        # ---- 固定点与标签 ----
        dot_O = Dot(O, color=CLR_TEAL, radius=0.09)
        lbl_O = MathTex(r"O", color=CLR_TEAL, font_size=24).next_to(dot_O, LEFT, buff=0.1)
        dot_D = Dot(D, color=CLR_CRIMSON, radius=0.1)
        lbl_D = MathTex(r"D", color=CLR_CRIMSON, font_size=30).next_to(dot_D, UP, buff=0.1)

        # ---- 中心轴线 ----
        axis = DashedLine(ax.c2p(0, -R * 1.15), ax.c2p(0, R * 1.15),
                          color=GREY, stroke_width=1.5)

        # ---- 动态部分生成函数：所有会随 h 变化的元素 ----
        def make_dynamic(h):
            H = ax.c2p(0, h)
            r = np.sqrt(max(R**2 - h**2, 0))
            rx = r * unit
            ry = rx * 0.32

            def circle_point(phi):
                return H + RIGHT * (rx * np.cos(phi)) + UP * (ry * np.sin(phi))

            # 前半圆实线，后半圆虚线
            circum_front = ParametricFunction(
                lambda t: circle_point(PI + t),
                t_range=[0, PI],
                color=BLUE, stroke_width=2.5,
            )
            circum_back_raw = ParametricFunction(
                lambda t: circle_point(t),
                t_range=[0, PI],
                color=GREY, stroke_width=3,
            )
            circum_back = DashedVMobject(circum_back_raw, num_dashes=28)

            # A、B、C 三点
            angles = [3*PI/7, -PI/6, -5*PI/6]
            pts = [circle_point(a) for a in angles]
            pt_A, pt_B, pt_C = pts

            tri = Polygon(pt_A, pt_B, pt_C,
                          color=CLR_ROSE, stroke_width=3,
                          fill_opacity=0.22, fill_color=CLR_ROSE)

            dots_ABC = VGroup(*[
                Dot(p, color=CLR_ROSE, radius=0.07) for p in pts
            ])
            lbls_ABC = VGroup(
                MathTex(r"A", color=CLR_ROSE, font_size=30).next_to(pt_A, UL, buff=0.08),
                MathTex(r"B", color=CLR_ROSE, font_size=30).next_to(pt_B, RIGHT, buff=0.1),
                MathTex(r"C", color=CLR_ROSE, font_size=30).next_to(pt_C, DOWN, buff=0.1),
            )

            dot_H = Dot(H, color=CLR_CREAM, radius=0.07)
            lbl_H = MathTex(r"H", color=CLR_CREAM, font_size=22).next_to(dot_H, RIGHT, buff=0.08)

            # 关键辅助线
            seg_DH = Line(D, H, color=CLR_CREAM, stroke_width=2)
            seg_OH = Line(O, H, color=YELLOW, stroke_width=2)
            seg_OC = DashedLine(O, pt_C, color=CLR_CREAM, stroke_width=3)
            seg_DA = DashedLine(D, pt_A, color=CLR_SKY, stroke_width=3)
            seg_DB = Line(D, pt_B, color=CLR_SKY, stroke_width=2.5)
            seg_DC = Line(D, pt_C, color=CLR_SKY, stroke_width=2.5)
            seg_HC = DashedLine(H, pt_C, color=CLR_MINT, stroke_width=3)

            # 长度标注
            mid_OC = (O + pt_C) / 2
            lbl_R = MathTex(r"R", color=YELLOW, font_size=25,stroke_width=1).move_to(mid_OC + LEFT * 0.22 + UP * 0.08)
            mid_DA = (D + pt_A) / 2
            lbl_2 = MathTex(r"2", color=BLUE, font_size=25).move_to(mid_DA + RIGHT * 0.25)
            mid_HC = (H + pt_C) / 2
            lbl_r = MathTex(r"r", color=BLUE, font_size=30,stroke_width=1).move_to(mid_HC + RIGHT * 0.1 + UP * 0.1)

            # 图层顺序：后虚线圆 -> 三角形 -> 前实线圆 -> 点与标签 -> H -> 线段 -> 标注
            return VGroup(
                circum_back, tri, circum_front,
                dots_ABC, lbls_ABC,
                dot_H, lbl_H,
                seg_DH, seg_OH, seg_OC,
                seg_DA, seg_DB, seg_DC, seg_HC,
                lbl_R, lbl_2, lbl_r,
            )

        # ---- 动画控制 ----
        h_tracker = ValueTracker(-R / 3)
        dynamic = make_dynamic(h_tracker.get_value())
        dynamic.add_updater(lambda m: m.become(make_dynamic(h_tracker.get_value())))

        # 全部元素（固定 + 动态）
        elements = VGroup(
            sphere_back, sphere, axis,
            dot_O, lbl_O, dot_D, lbl_D,
            dynamic,
        )

        # 2 秒内一次性画出整个示意图
        self.play(LaggedStart(
            *[Create(element) for element in elements], 
            lag_ratio=.3),
            run_time=2)
        self.wait(0.5)

        # 底面沿轴线上下移动，直观展示 O 在内部/外部
        self.play(
            h_tracker.animate.set_value(0.75 * R),
            run_time=5,
            rate_func=there_and_back,
        )
        self.wait(0.5)

        # 移除 updater，定格到最终位置
        # dynamic.clear_updaters()
        self.wait(0.5)

        s14_1 = VGroup(
            Text("球体积：", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"\frac{4}{3}\pi R^3=4\sqrt{3}\pi \;\Rightarrow\; R=\sqrt{3}",
                    color=CLR_ROSE, stroke_width=1, font_size=28),
        ).arrange(RIGHT, buff=0.08)
        s14_1.next_to(q14, DOWN, buff=0.5, aligned_edge=LEFT)

        s14_2 = VGroup(
            Text("D 到 A,B,C 等距 ⇒ D 在 △ABC 的正上方，",
                  font=FONT_CN, color=CLR_SKY, font_size=22),
            Text("设 H 为 △ABC 中心。",
                  font=FONT_CN, color=CLR_SKY, font_size=22),
        ).arrange(RIGHT, buff=0.1)
        s14_2.next_to(s14_1, DOWN, buff=0.15, aligned_edge=LEFT)

        s14_3 = VGroup(
            Text(" 可得 O、H、D 共线。", font=FONT_CN, color=CLR_SKY, font_size=22),
            Text("设 △ABC 外接圆半径 r，OH=d", font=FONT_CN, color=CLR_SKY, font_size=22),
        ).arrange(RIGHT, buff=0.08)
        s14_3.next_to(s14_2, DOWN, buff=0.1, aligned_edge=LEFT)

        s14_4 = VGroup(
            Text("由勾股：", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"R^2=d^2+r^2 \;\Rightarrow\; 3=d^2+r^2", color=CLR_ROSE, stroke_width=1, font_size=28),
        ).arrange(RIGHT, buff=0.08)
        s14_4.next_to(s14_3, DOWN, buff=0.15, aligned_edge=LEFT)

        s14_5 = VGroup(
            MathTex(r"DC^2=DH^2+r^2 \;\Rightarrow\; 4=DH^2+r^2", color=CLR_ROSE, stroke_width=1, font_size=28),
        ).arrange(RIGHT, buff=0.08)
        s14_5.next_to(s14_4[1], DOWN, buff=0.15, aligned_edge=LEFT)

        s14_brace=Brace(VGroup(s14_4,s14_5),RIGHT,buff=.1,stroke_width=.1)
        
        s14_5b = VGroup(
            Text("相减得 ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"DH^2-d^2=1", color=CLR_CREAM, stroke_width=1, font_size=28),
        ).arrange(RIGHT, buff=0.08)
        s14_5b.next_to(s14_brace, RIGHT, buff=0.15)

        s14_5c = VGroup(
            Text("若 O 在 D,H 之间 ⇒ ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"DH=R+d=\sqrt{3}+d;", color=CLR_CREAM, stroke_width=1, font_size=26),
        ).arrange(RIGHT, buff=0.08)
        s14_5c.next_to(s14_5, DOWN, buff=0.1).align_to(s14_4, LEFT)

        s14_5d = VGroup(
            Text("代入得 ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"3+2\sqrt{3}d=1 \;\Rightarrow\; d<0", color=CLR_CREAM, stroke_width=1, font_size=26),
            Text("，矛盾！", font=FONT_CN, color=CLR_SKY, font_size=22),
        ).arrange(RIGHT, buff=0.08)
        s14_5d.next_to(s14_5c, RIGHT, buff=0.1)

        s14_5e = VGroup(
            Text("故 H 在 O,D 之间 ⇒ ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"DH=R-d=\sqrt{3}-d", color=CLR_ROSE, stroke_width=1, font_size=26),
            Text(" ⇒ ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"DH+d=\sqrt{3}", color=CLR_ROSE, stroke_width=1, font_size=28),
        ).arrange(RIGHT, buff=0.08)
        s14_5e.next_to(s14_5c, DOWN, buff=0.12, aligned_edge=LEFT)

        s14_6 = VGroup(
            Text("由 ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"DH^2-d^2=1", color=CLR_ROSE, stroke_width=1, font_size=28),
            Text(" 及 ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"DH+d=\sqrt{3}", color=CLR_ROSE, stroke_width=1, font_size=28),
            Text(" 解得：", font=FONT_CN, color=CLR_SKY, font_size=22),
        ).arrange(RIGHT, buff=0.08)
        s14_6.next_to(s14_5e, DOWN, buff=0.15, aligned_edge=LEFT)

        s14_7 = VGroup(
            Text("解得 ", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"r^2=\frac{8}{3}", color=CLR_ROSE, stroke_width=1, font_size=28),
            Text("，等边面积：", font=FONT_CN, color=CLR_SKY, font_size=22),
            MathTex(r"S=\frac{3\sqrt{3}}{4}r^2=\frac{3\sqrt{3}}{4}\cdot\frac{8}{3}=2\sqrt{3}",
                    color=CLR_ROSE, stroke_width=1, font_size=30),
        ).arrange(RIGHT, buff=0.08)
        s14_7.next_to(s14_6, DOWN, buff=0.2, aligned_edge=LEFT)

        self.play(LaggedStart(
            Write(s14_1), Write(s14_2), Write(s14_3),
            lag_ratio=0.7,
        ))
        self.play(LaggedStart(
            Write(s14_4), Write(s14_5),Create(s14_brace), Write(s14_5b),
            lag_ratio=0.8,
        ))
        self.wait()
               
        self.play(LaggedStart(
            Write(s14_5c), Write(s14_5d), 
            lag_ratio=0.6,
        ))
        self.wait()
        
        self.play(h_tracker.animate.set_value(0.55 * R)) 

        self.play(LaggedStart(
            Write(s14_5e),
            Write(s14_6), Write(s14_7),
            lag_ratio=0.9,
        ))
        self.wait(2)












class Q15(Scene):
    def construct(self):
        title, titlePos = AddTitle(self, "频率分布直方图", font_size=31)
        self.play(title)

        # ---- 题干（一行）+ (1)(2) 对齐题干首字 + (i)(ii) 对齐 (2) 题干首字 ----
        q15_stem = Text(
            "15.（13 分）某工厂抽取一批电子元件检测，记录第一次出现故障的时间（天），绘制成如下的频率分布直方图：",
            font=FONT_CN, font_size=20, color=WHITE,
        )

        q15_q1 = Text(
            "(1) 求第一次出现故障的时间的第一四分位数和中位数；",
            font=FONT_CN, font_size=20, color=WHITE,
        )

        q15_q2_label = Text("(2) ", font=FONT_CN, font_size=20, color=WHITE)
        q15_q2_body = VGroup(
            MathTex(r"\hat{p}", font_size=22, color=WHITE,stroke_width=1),
            Text(" 为首次故障时间小于 365 天的概率估计值．", font=FONT_CN, font_size=20, color=WHITE),
        ).arrange(RIGHT, buff=0.02)
        q15_q2 = VGroup(q15_q2_label, q15_q2_body).arrange(RIGHT, aligned_edge=LEFT)

        q15_q2i_label = Text("(i) 求", font=FONT_CN, font_size=20, color=WHITE)
        q15_q2i_body = MathTex(
            r"\hat{p} ",
            font_size=25, color=WHITE,stroke_width=1
        )
        q15_q2i = VGroup(q15_q2i_label, q15_q2i_body).arrange(RIGHT, aligned_edge=LEFT)
        q15_q2i.align_to(q15_q2_body, LEFT)

        q15_q2ii_label = Text("(ii)", font=FONT_CN, font_size=20, color=WHITE)
        q15_q2ii_body1 = Text("工厂向某用户销售 100 件电子元件，", font=FONT_CN, font_size=20, color=WHITE)
        q15_q2ii_body2 = VGroup(
            MathTex(r"X", font_size=22, color=WHITE,stroke_width=1),
            Text(" 为这 100 件产品首次出现故障小于 365 天的件数，", font=FONT_CN, font_size=20, color=WHITE),
        ).arrange(RIGHT, buff=0.02)
        q15_q2ii_line1 = VGroup(q15_q2ii_label, q15_q2ii_body1, q15_q2ii_body2).arrange(RIGHT,buff=.1)

        q15_q2ii_line2 = VGroup(
            Text("若 ", font=FONT_CN, font_size=20, color=WHITE),
            MathTex(r"X \sim B(100, \hat{p})", font_size=22, color=WHITE,stroke_width=1),
            Text("，求 ", font=FONT_CN, font_size=20, color=WHITE),
            MathTex(r"E(X)", font_size=22, color=WHITE,stroke_width=1),
            Text("，", font=FONT_CN, font_size=20, color=WHITE),
            MathTex(r"D(X)", font_size=22, color=WHITE,stroke_width=1),
            Text("．", font=FONT_CN, font_size=20, color=WHITE),
        ).arrange(RIGHT, buff=0.02)
        
        
        

        q15 = VGroup(
            q15_stem,
            q15_q1,
            q15_q2,
            q15_q2i,
            q15_q2ii_line1,
            q15_q2ii_line2,
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)

        q15_q1.align_to(q15_stem[3], LEFT)
        q15_q2.align_to(q15_q1, LEFT)
        q15_q2i.align_to(q15_q2_body[0], LEFT)

        q15_q2ii_line1.align_to(q15_q2i, LEFT)
        q15_q2ii_line2.align_to(q15_q2ii_body1, LEFT)

        q15.scale(0.9)
        q15.next_to(titlePos, DOWN, buff=.6).align_to(titlePos, LEFT)
        self.play(Write(q15))

        # ---- 频率分布直方图 ----
        hist = problems.problem_15_histogram().scale(0.85)
        hist.to_edge(RIGHT, buff=0.25).shift(DOWN * 1.2)
        self.play(LaggedStart(
            Create(hist[0]),  # axes
            Create(hist[3]),  # bars
            Write(hist[1]), Write(hist[2]),  # labels
            lag_ratio=0.3,
        ))
        self.wait(0.5)

        # ---- 解答 ----
        # 左列：(1) 第一四分位数和中位数
        s15_1 = VGroup(
            Text("组距为 10，各组频率：", font=FONT_CN, color=CLR_SKY, font_size=20),
            MathTex(r"0.05,0.10,0.20,0.25,0.15,0.15,0.05,0.05", color=CLR_ROSE,
                    stroke_width=1, font_size=22),
        ).arrange(RIGHT, buff=0.08)

        s15_2 = Text("第一四分位数：累积到 365 为 0.15，落在 [365,375) 内",
                     font=FONT_CN, color=CLR_SKY, font_size=20)

        s15_3 = MathTex(r"Q_1=365+10\times\frac{0.25-0.15}{0.20}=370",
                        color=CLR_ROSE, stroke_width=1, font_size=24)

        s15_4 = Text("中位数：累积到 375 为 0.35，落在 [375,385) 内",
                     font=FONT_CN, color=CLR_SKY, font_size=20)

        s15_4b = VGroup(
            Text("中位数 = ", font=FONT_CN, font_size=20, color=CLR_ROSE),
            MathTex(r"375+10\times\frac{0.50-0.35}{0.25}=381",
                    color=CLR_ROSE, stroke_width=1, font_size=24),
        ).arrange(RIGHT, buff=0.08)

        left_col = VGroup(s15_1, s15_2, s15_3, s15_4, s15_4b).arrange(
            DOWN, aligned_edge=LEFT, buff=0.12)
        left_col.next_to(q15, DOWN, buff=0.3).align_to(q15_q1, LEFT).shift(DOWN * 0.3)

        # 右列：(2) 概率估计与二项分布
        s15_5 = VGroup(
            Text("(i) ", font=FONT_CN, color=CLR_SKY, font_size=20),
            MathTex(r"\hat{p}=P(X<365)=0.05+0.10=0.15", color=CLR_ROSE,
                    stroke_width=1, font_size=24),
        ).arrange(RIGHT, buff=0.08)

        s15_6 = VGroup(
            Text("(ii) ", font=FONT_CN, color=CLR_SKY, font_size=20),
            MathTex(r"X\sim B(100,0.15)", color=CLR_ROSE, stroke_width=1, font_size=24),
        ).arrange(RIGHT, buff=0.08)

        s15_7 = MathTex(r"E(X)=100\times0.15=15", color=CLR_ROSE, stroke_width=1, font_size=26)
        s15_8 = MathTex(r"D(X)=100\times0.15\times0.85=12.75", color=CLR_ROSE,
                        stroke_width=1, font_size=26)

        right_col = VGroup(s15_5, s15_6, s15_7, s15_8).arrange(
            DOWN, aligned_edge=LEFT, buff=0.12)
        right_col.next_to(hist, UP, buff=0.3).align_to(hist, RIGHT)

        self.play(LaggedStart(
            Write(s15_1), Write(s15_2), Write(s15_3), Write(s15_4), Write(s15_4b),
            lag_ratio=0.4,
        ))
        self.wait(0.3)
        self.play(LaggedStart(
            Write(s15_5), Write(s15_6), Write(s15_7), Write(s15_8),
            lag_ratio=0.4,
        ))
        self.wait(2)


class Q16(Scene):
    def construct(self):
        title, titlePos = AddTitle(self, "三棱锥几何证明", font_size=31)
        self.play(title)

        q16 = problems.problem_16()
        q16.scale(0.9)
        q16.next_to(titlePos, DOWN, buff=.3).align_to(titlePos, LEFT)
        self.play(Write(q16))

        # ---- 三棱锥示意图（在 scene 内构建，方便证明时单独控制每条线/面）----
        ax = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 4, 1],
            x_length=3.5,
            y_length=3.5,
            axis_config={"stroke_width": 0},
            tips=False,
        )
        ax.to_edge(RIGHT, buff=0.6).shift(DOWN * 0.2)

        # 顶点（与 problems.problem_16_fig 保持一致）
        D = ax.c2p(0, 0)
        C = ax.c2p(3, 0)
        B = ax.c2p(2, 1.2)
        A = ax.c2p(1.5, 3.5)
        E = ax.c2p(1.1, 0.66)

        sw = 2.4  # 线宽

        # ---- 平面（默认透明，证明时可单独 FadeIn）----
        plane_ABC = Polygon(A, B, C, color=CLR_SKY, stroke_width=0,
                            fill_opacity=0, fill_color=CLR_SKY)
        plane_ACD = Polygon(A, C, D, color=CLR_MINT, stroke_width=0,
                            fill_opacity=0, fill_color=CLR_MINT)
        plane_ADE = Polygon(A, D, B, color=CLR_ROSE, stroke_width=0,
                            fill_opacity=0, fill_color=CLR_ROSE)
        plane_BCD = Polygon(B, C, D, color=CLR_CORNFLOWER, stroke_width=0,
                            fill_opacity=0, fill_color=CLR_CORNFLOWER)

        # ---- 棱（虚线放后，实线放前）----
        line_DB = DashedLine(D, B, color=WHITE, stroke_width=sw)
        line_CB = DashedLine(C, B, color=WHITE, stroke_width=sw)
        line_AB = DashedLine(A, B, color=WHITE, stroke_width=sw)
        line_AE = DashedLine(A, E, color=WHITE, stroke_width=sw)
        line_CE = DashedLine(C, E, color=WHITE, stroke_width=sw)

        line_DC = Line(D, C, color=WHITE, stroke_width=sw)
        line_AD = Line(A, D, color=WHITE, stroke_width=sw)
        line_AC = Line(A, C, color=WHITE, stroke_width=sw)

        # ---- 顶点与标签 ----
        dot_A = Dot(A, color=WHITE, radius=0.06)
        dot_B = Dot(B, color=WHITE, radius=0.06)
        dot_C = Dot(C, color=WHITE, radius=0.06)
        dot_D = Dot(D, color=WHITE, radius=0.06)
        dot_E = Dot(E, color=WHITE, radius=0.06)

        lbl_A = MathTex(r"A", color=WHITE, font_size=20, stroke_width=1).next_to(A, UP, buff=0.08)
        lbl_B = MathTex(r"B", color=WHITE, font_size=20, stroke_width=1).next_to(B, UR, buff=0.05)
        lbl_C = MathTex(r"C", color=WHITE, font_size=20, stroke_width=1).next_to(C, DR, buff=0.05)
        lbl_D = MathTex(r"D", color=WHITE, font_size=20, stroke_width=1).next_to(D, DL, buff=0.05)
        lbl_E = MathTex(r"E", color=WHITE, font_size=20, stroke_width=1).next_to(E, LEFT, buff=0.08)

        # 组装：平面在最底层 -> 虚线 -> 实线 -> 点和标签
        fig = VGroup(
            plane_ABC, plane_ACD, plane_ADE, plane_BCD,
            line_DB, line_CB, line_AB, line_AE, line_CE,
            line_DC, line_AD, line_AC,
            dot_A, dot_B, dot_C, dot_D, dot_E,
            lbl_A, lbl_B, lbl_C, lbl_D, lbl_E,
        )
        fig.scale(1.2)

        self.play(Create(fig), run_time=2)
        self.wait(0.5)

        # ============================================================
        # 第 (1) 问证明：CD ⊥ AB
        # ============================================================
        # 辅助函数：把若干对象高亮后恢复
        def highlight(*mobs, color=YELLOW, run_time=0.8):
            return AnimationGroup(*[
                mob.animate.set_color(color) for mob in mobs
            ], lag_ratio=0)

        def restore(*mobs, run_time=0.6):
            return AnimationGroup(*[
                mob.animate.set_color(WHITE) for mob in mobs
            ], lag_ratio=0)

        # ---- 步骤 1：摆出已知条件 ----
        s16_0 = Text("证明：", font=FONT_CN, color=CLR_SKY, font_size=22)
        s16_0.next_to(q16, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(Write(s16_0))

        known = VGroup(
            MathTex(r"AE \perp CE", color=CLR_ROSE, font_size=24, stroke_width=1),
            MathTex(r"AE \perp DE", color=CLR_ROSE, font_size=24, stroke_width=1),
            MathTex(r"CD \perp AD", color=CLR_ROSE, font_size=24, stroke_width=1),
        ).arrange(RIGHT, buff=0.4)
        known.next_to(s16_0, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(known))

        # 高亮 AE、CE、DE
        self.play(highlight(line_AE, line_CE, line_AE, line_AE))
        self.wait(0.3)
        self.play(restore(line_AE, line_CE))

        # ---- 步骤 2：AE ⊥ 平面 BCD ----
        s16_1 = VGroup(
            MathTex(r"\because", color=CLR_SKY, font_size=24, stroke_width=1),
            MathTex(r"AE \perp CE", color=CLR_ROSE, font_size=22, stroke_width=1),
            MathTex(r",\;", color=CLR_SKY, font_size=22, stroke_width=1),
            MathTex(r"AE \perp DE", color=CLR_ROSE, font_size=22, stroke_width=1),
            MathTex(r",\;", color=CLR_SKY, font_size=22, stroke_width=1),
            MathTex(r"CE \cap DE = E", color=CLR_ROSE, font_size=22, stroke_width=1),
        ).arrange(RIGHT, buff=0.06)
        s16_1.next_to(known, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(s16_1))

        s16_2 = VGroup(
            MathTex(r"\therefore", color=CLR_SKY, font_size=24, stroke_width=1),
            MathTex(r"AE \perp ", color=CLR_ROSE, font_size=22, stroke_width=1),
            Text("平面 ", font=FONT_CN, color=CLR_SKY, font_size=20),
            MathTex(r"BCD", color=CLR_ROSE, font_size=22, stroke_width=1),
        ).arrange(RIGHT, buff=0.06)
        s16_2.next_to(s16_1, DOWN, buff=0.15, aligned_edge=LEFT)

        plane_BCD.set_fill(opacity=0.22)
        self.play(FadeIn(plane_BCD))
        self.play(highlight(line_AE))
        self.play(Write(s16_2))
        self.play(restore(line_AE))

        # ---- 步骤 3：AE ⊥ CD ----
        s16_3 = VGroup(
            MathTex(r"\because", color=CLR_SKY, font_size=24, stroke_width=1),
            MathTex(r"CD \subset ", color=CLR_ROSE, font_size=22, stroke_width=1),
            Text("平面 ", font=FONT_CN, color=CLR_SKY, font_size=20),
            MathTex(r"BCD", color=CLR_ROSE, font_size=22, stroke_width=1),
            MathTex(r",\;\therefore", color=CLR_SKY, font_size=24, stroke_width=1),
            MathTex(r"AE \perp CD", color=CLR_ROSE, font_size=22, stroke_width=1),
        ).arrange(RIGHT, buff=0.06)
        s16_3.next_to(s16_2, DOWN, buff=0.15, aligned_edge=LEFT)

        self.play(highlight(line_DC))
        self.play(Write(s16_3))
        self.play(restore(line_DC))

        # ---- 步骤 4：CD ⊥ 平面 ADE ----
        s16_4 = VGroup(
            MathTex(r"\because", color=CLR_SKY, font_size=24, stroke_width=1),
            MathTex(r"CD \perp AD", color=CLR_ROSE, font_size=22, stroke_width=1),
            MathTex(r",\;", color=CLR_SKY, font_size=22, stroke_width=1),
            MathTex(r"AD \cap AE = A", color=CLR_ROSE, font_size=22, stroke_width=1),
        ).arrange(RIGHT, buff=0.06)
        s16_4.next_to(s16_3, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(s16_4))

        s16_5 = VGroup(
            MathTex(r"\therefore", color=CLR_SKY, font_size=24, stroke_width=1),
            MathTex(r"CD \perp ", color=CLR_ROSE, font_size=22, stroke_width=1),
            Text("平面 ", font=FONT_CN, color=CLR_SKY, font_size=20),
            MathTex(r"ADE", color=CLR_ROSE, font_size=22, stroke_width=1),
        ).arrange(RIGHT, buff=0.06)
        s16_5.next_to(s16_4, DOWN, buff=0.15, aligned_edge=LEFT)

        plane_ADE.set_fill(opacity=0.22)
        self.play(FadeIn(plane_ADE))
        self.play(highlight(line_DC))
        self.play(Write(s16_5))
        self.play(restore(line_DC))

        # ---- 步骤 5：CD ⊥ AB ----
        s16_6 = VGroup(
            MathTex(r"\because", color=CLR_SKY, font_size=24, stroke_width=1),
            MathTex(r"B \in BD", color=CLR_ROSE, font_size=22, stroke_width=1),
            MathTex(r",\;\therefore", color=CLR_SKY, font_size=24, stroke_width=1),
            MathTex(r"AB \subset ", color=CLR_ROSE, font_size=22, stroke_width=1),
            Text("平面 ", font=FONT_CN, color=CLR_SKY, font_size=20),
            MathTex(r"ADE", color=CLR_ROSE, font_size=22, stroke_width=1),
        ).arrange(RIGHT, buff=0.06)
        s16_6.next_to(s16_5, DOWN, buff=0.2, aligned_edge=LEFT)

        s16_7 = VGroup(
            MathTex(r"\therefore CD \perp AB", color=CLR_ROSE, font_size=28, stroke_width=1),
        )
        s16_7.next_to(s16_6, DOWN, buff=0.2, aligned_edge=LEFT)

        self.play(highlight(line_AB))
        self.play(Write(s16_6))
        self.play(Write(s16_7))
        self.play(restore(line_AB))

        self.wait(2)

        # ---- 清理第 (1) 问解答，恢复示意图 ----
        proof_objs = [s16_0, known, s16_1, s16_2, s16_3, s16_4, s16_5, s16_6, s16_7]
        self.play(
            AnimationGroup(*[FadeOut(m, shift=RIGHT) for m in proof_objs]),
            plane_BCD.animate.set_fill(opacity=0),
            plane_ADE.animate.set_fill(opacity=0),
        )
        self.wait(0.3)

        # ============================================================
        # 第 (2) 问：求 AD 与平面 ABC 所成角的正弦值
        # ============================================================
        s16_q2 = Text("（2）解：", font=FONT_CN, color=CLR_SKY, font_size=22)
        s16_q2.next_to(q16, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(Write(s16_q2))

        # 已知条件
        s16_q2_1 = MathTex(r"DE=2,\; BE=1,\; AE=\sqrt{2},\; CD=2\sqrt{3}",
                           color=CLR_CREAM, font_size=22, stroke_width=1)
        s16_q2_1.next_to(s16_q2, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(s16_q2_1))

        # AE \perp 平面 BCD \Rightarrow AE \perp DE \Rightarrow AD
        s16_q2_2 = VGroup(
            MathTex(r"\because AE \perp ", color=CLR_SKY, font_size=20, stroke_width=1),
            Text("平面 ", font=FONT_CN, color=CLR_SKY, font_size=18),
            MathTex(r"BCD", color=CLR_SKY, font_size=20, stroke_width=1),
            MathTex(r",\; AE \perp DE", color=CLR_SKY, font_size=20, stroke_width=1),
            MathTex(r"\Rightarrow AD=\sqrt{AE^2+DE^2}=\sqrt{6}",
                    color=CLR_ROSE, font_size=20, stroke_width=1),
        ).arrange(RIGHT, buff=0.08)
        s16_q2_2.next_to(s16_q2_1, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(s16_q2_2))

        # 建立坐标系
        s16_q2_3 = Text("以 D 为原点，DB、DC、AE 方向分别为 y、x、z 轴建系：",
                        font=FONT_CN, color=CLR_SKY, font_size=19)
        s16_q2_3.next_to(s16_q2_2, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(s16_q2_3))

        # 在示意图上画空间直角坐标系（空心三角箭头，尖端偏小）
        x_axis = Arrow(D, D + (C - D) * 1.35, color=RED, stroke_width=4, buff=0,
                       tip_length=0.15)
        y_axis = Arrow(D, D + (B - D) * 1.35, color=GREEN, stroke_width=4, buff=0,
                       tip_length=0.15)
        z_axis = Arrow(D, D + (A - E) * 1.6, color=BLUE, stroke_width=4, buff=0,
                       tip_length=0.15)
        lbl_x = MathTex(r"x", color=RED, font_size=22, stroke_width=1).next_to(x_axis.get_end(), DR, buff=0.05)
        lbl_y = MathTex(r"y", color=GREEN, font_size=22, stroke_width=1).next_to(y_axis.get_end(), UR, buff=0.05)
        lbl_z = MathTex(r"z", color=BLUE, font_size=22, stroke_width=1).next_to(z_axis.get_end(), UP, buff=0.05)
        # 标注 DC ⊥ DB，说明坐标系是直角坐标系
        axes_3d = VGroup(x_axis, y_axis, z_axis, lbl_x, lbl_y, lbl_z)
        axes_3d.scale(1.2)
        self.play(Create(axes_3d))

        s16_q2_4 = MathTex(r"D(0,0,0),\; C(2\sqrt{3},0,0),\; B(0,3,0),\; A(0,2,\sqrt{2})",
                           color=CLR_CREAM, font_size=19, stroke_width=1)
        s16_q2_4.next_to(s16_q2_3, DOWN, buff=0.15, aligned_edge=LEFT)
        self.play(Write(s16_q2_4))

        # 向量 AB、AC
        s16_q2_5 = VGroup(
            MathTex(r"\overrightarrow{AB}=(0,1,-\sqrt{2})", color=CLR_CREAM,
                    font_size=19, stroke_width=1),
            MathTex(r"\overrightarrow{AC}=(2\sqrt{3},-2,-\sqrt{2})", color=CLR_CREAM,
                    font_size=19, stroke_width=1),
        ).arrange(RIGHT, buff=0.3)
        s16_q2_5.next_to(s16_q2_4, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(s16_q2_5))

        # 法向量
        s16_q2_6 = MathTex(r"\boldsymbol{n}=\overrightarrow{AB}\times\overrightarrow{AC}"
                           r"=(3,2\sqrt{3},\sqrt{6})",
                           color=CLR_ROSE, font_size=19, stroke_width=1)
        s16_q2_6.next_to(s16_q2_5, DOWN, buff=0.15, aligned_edge=LEFT)
        self.play(Write(s16_q2_6))

        # 计算 sinθ
        s16_q2_7 = MathTex(r"\sin\theta=\frac{|\overrightarrow{AD}\cdot\boldsymbol{n}|}"
                           r"{|\overrightarrow{AD}||\boldsymbol{n}|}"
                           r"=\frac{6\sqrt{3}}{\sqrt{6}\cdot3\sqrt{3}}=\frac{\sqrt{6}}{3}",
                           color=CLR_ROSE, font_size=22, stroke_width=1)
        s16_q2_7.next_to(s16_q2_6, DOWN, buff=0.2, aligned_edge=LEFT)

        # 配合示意图：高亮 AD 和平面 ABC
        plane_ABC.set_fill(opacity=0.22)
        self.play(FadeIn(plane_ABC))
        self.play(highlight(line_AD))
        self.play(Write(s16_q2_7))
        self.play(restore(line_AD))

        self.wait(2)


class TrirPyrCir(Scene):
    """
    三棱锥外接球动态演示：底面 ABC 沿轴线上下移动，
    直观展示球心 O 在三棱锥 D-ABC 内部 / 外部两种情形。

    几何模型：
    - 球心 O 固定在坐标原点；
    - 球半径为 R，顶点 D 固定在球的最顶端 (0, R)；
    - 底面 ABC 是位于水平平面 z = h 上的正三角形；
    - A、B、C 都在球面上，因此底面外接圆半径 r = sqrt(R^2 - h^2)；
    - 当 h 从负值变为正值时，底面从 O 下方移动到 O 上方，
      观众可以看到 O 从三棱锥内部转移到外部。
    """

    def construct(self):
        # ============================================================
        # 1. 标题：说明本演示的主题
        # ============================================================
        title = Text("三棱锥外接球 · 底面移动演示", font=FONT_CN,
                     color=CLR_CREAM, font_size=28)
        title.to_corner(UL, buff=0.3)
        self.add(title)

        # ============================================================
        # 2. 坐标系 Axes：把所有几何量从“数学坐标”映射到“屏幕坐标”
        # ============================================================
        # x_range/y_range：数学坐标的范围；x_length/y_length：在屏幕上的总长度。
        # axis_config={"stroke_width": 0} 隐藏坐标轴本身，只用它做定位工具；
        # tips=False 关闭坐标轴末端的箭头。
        ax = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            x_length=5.2,
            y_length=5.2,
            axis_config={"stroke_width": 0},
            tips=False,
        )
        # 把坐标系放到画面右侧，留一些边距；再稍微下移，避免和左上角标题重叠。
        ax.to_edge(RIGHT, buff=0.6).shift(DOWN * 0.1)
        # unit：Axes 中一个单位长度对应多少像素，用于把 R 换算成屏幕长度。
        unit = ax.x_axis.unit_size

        # ============================================================
        # 3. 固定几何量：球半径 R、球心 O、顶点 D
        # ============================================================
        R = 1.8                      # 球半径（Axes 坐标系中的长度）
        O = ax.c2p(0, 0)             # 球心 O：Axes 原点对应的屏幕位置
        D = ax.c2p(0, R)             # 顶点 D：在球的最顶端 (0, R)

        # ============================================================
        # 4. 球体：前半实线 + 后半虚线，形成立体球效果
        # ============================================================
        # Circle 默认圆心在原点 (0,0)，所以创建后用 move_to(O) 把球心移到 O。
        sphere = Circle(radius=R * unit, color=CLR_SKY, stroke_width=4)
        sphere.move_to(O)

        # Arc 绘制左侧半圆（参数角从 PI/2 开始，扫过 PI 弧度），代表背向观众的半球。
        # 用 DashedVMobject 把它转成虚线，与前面的实线半球区分。
        sphere_back = Arc(radius=R * unit, start_angle=PI/2, angle=PI,
                          color=GREY, stroke_width=2)
        sphere_back.move_arc_center_to(O)
        sphere_back = DashedVMobject(sphere_back, num_dashes=30)

        # ============================================================
        # 5. 固定点 O、D 及其标签
        # ============================================================
        dot_O = Dot(O, color=CLR_TEAL, radius=0.09)
        # next_to(dot_O, LEFT, buff=0.1) 把标签放在 O 的左侧，间距 0.1。
        lbl_O = MathTex(r"O", color=CLR_TEAL, font_size=24).next_to(dot_O, LEFT, buff=0.1)

        dot_D = Dot(D, color=CLR_CRIMSON, radius=0.1)
        lbl_D = MathTex(r"D", color=CLR_CRIMSON, font_size=30).next_to(dot_D, UR, buff=0.2)

        # 穿过 O 与 D 的竖直中心轴线，作为底面上下移动的参考。
        axis = DashedLine(ax.c2p(0, -R * 1.15), ax.c2p(0, R * 1.15),
                          color=GREY, stroke_width=1.5)

        # ============================================================
        # 6. 动态底面生成函数 make_base(h)
        # ============================================================
        # 输入 h：底面中心 H 在 Axes 坐标系中的竖直高度。
        # 返回值 VGroup：包含该高度下底面 ABC 的所有图形元素。
        def make_base(h):
            """h：底面中心 H 在 Axes 坐标系中的 z 坐标（竖直高度）"""

            # ---- 6.1 底面中心 H 和底面外接圆半径 r ----
            H = ax.c2p(0, h)                       # H 在竖直轴上，高度为 h
            # A、B、C 都在球面上，H 是底面中心。由勾股定理：
            # OH^2 + HA^2 = OA^2  =>  h^2 + r^2 = R^2  =>  r = sqrt(R^2 - h^2)
            # max(..., 0) 防止浮点误差导致负数开方出错。
            r = np.sqrt(max(R**2 - h**2, 0))

            # ---- 6.2 透视椭圆参数 ----
            # 水平圆在透视下应画成椭圆。rx 是水平方向长半轴（真实长度），
            # ry 是竖直方向短半轴（压缩后），模拟近大远小的透视效果。
            rx = r * unit
            ry = rx * 0.32

            # ---- 6.3 底面外接圆参数方程 ----
            # phi 为参数角，circle_point(phi) 返回椭圆上一点的屏幕坐标。
            # phi=0      -> 椭圆最右端
            # phi=PI/2   -> 椭圆最上端
            # phi=PI     -> 椭圆最左端
            # phi=3PI/2  -> 椭圆最下端
            def circle_point(phi):
                return H + RIGHT * (rx * np.cos(phi)) + UP * (ry * np.sin(phi))

            # ---- 6.4 外接圆：前实后虚，制造立体层次 ----
            # 椭圆下半部分（phi ∈ [PI, 2PI]，sin(phi) < 0）朝向屏幕，是“前面”，画实线。
            circum_front = ParametricFunction(
                lambda t: circle_point(PI + t),    # phi = PI + t，范围 [PI, 2PI]
                t_range=[0, PI],
                color=CLR_MINT, stroke_width=2.5,
            )
            # 椭圆上半部分（phi ∈ [0, PI]，sin(phi) > 0）被三角形遮挡，是“后面”，画虚线。
            circum_back_raw = ParametricFunction(
                lambda t: circle_point(t),         # phi = t，范围 [0, PI]
                t_range=[0, PI],
                color=GREY, stroke_width=2,
            )
            circum_back = DashedVMobject(circum_back_raw, num_dashes=18)

            # ---- 6.5 正三角形 ABC 的三个顶点 ----
            # 三个角度相差 120°（即 2*PI/3），保证是正三角形。
            # A 在后上方（靠近背半球），B、C 在前下方两侧，避免标签和线条互相遮挡。
            angles = [3*PI/7, -PI/6, -5*PI/6]
            pts = [circle_point(ang) for ang in angles]
            pt_A, pt_B, pt_C = pts

            # ---- 6.6 三角形 ABC ----
            # Polygon 连接三点；fill_opacity 给半透明填充，增强立体感。
            tri = Polygon(pt_A, pt_B, pt_C,
                          color=CLR_ROSE, stroke_width=3,
                          fill_opacity=0.22, fill_color=CLR_ROSE)

            # ---- 6.7 三个顶点的小圆点和标签 ----
            dots_ABC = VGroup(*[
                Dot(p, color=CLR_ROSE, radius=0.06) for p in pts
            ])
            lbls_ABC = VGroup(
                MathTex(r"A", color=CLR_ROSE, font_size=30).next_to(pt_A, UR, buff=0.08),
                MathTex(r"B", color=CLR_ROSE, font_size=30).next_to(pt_B, RIGHT, buff=0.08),
                MathTex(r"C", color=CLR_ROSE, font_size=30).next_to(pt_C, DOWN, buff=0.08),
            )

            # ---- 6.8 底面中心 H ----
            dot_H = Dot(H, color=CLR_CREAM, radius=0.07)
            lbl_H = MathTex(r"H", color=CLR_CREAM, font_size=22).next_to(dot_H, RIGHT, buff=0.08)

            # ---- 6.9 关键辅助线段 ----
            # DH：三棱锥的高；OH：球心到底面中心的距离。
            # DA、DB、DC：三棱锥的侧棱，用不同线型突出几何关系。
            seg_DH = Line(D, H, color=CLR_CREAM, stroke_width=2)
            seg_OH = Line(O, H, color=YELLOW, stroke_width=2)
            seg_DA = DashedLine(D, pt_A, color=CLR_SKY, stroke_width=3)
            seg_DB = Line(D, pt_B, color=CLR_SKY, stroke_width=2.5)
            seg_DC = Line(D, pt_C, color=CLR_SKY, stroke_width=2.5)

            # ---- 6.10 状态文字：O 在三棱锥内部 / 外部 ----
            # h < 0：底面在球心下方，O 位于 D 与底面之间，故在内部。
            # h > 0：底面在球心上方，O 在三棱锥外部。
            # h ≈ 0：O 与底面共面。
            if h < -1e-3:
                status = Text("O 在三棱锥 D-ABC 内部", font=FONT_CN,
                              color=CLR_TEAL, font_size=22)
            elif h > 1e-3:
                status = Text("O 在三棱锥 D-ABC 外部", font=FONT_CN,
                              color=CLR_CRIMSON, font_size=22)
            else:
                status = Text("O 与底面 ABC 共面", font=FONT_CN,
                              color=YELLOW, font_size=22)
            status.next_to(ax, DOWN, buff=0.25)

            # ---- 6.11 图层顺序 ----
            # Manim 中后加入的对象会覆盖先加入的对象。
            # 顺序：后面虚线圆 → 三角形填充 → 前面实线圆 → 点与标签 → 线段 → 状态文字。
            # 这样前面的实线圆会盖住三角形边缘，三角形又会盖住后面的虚线圆，层次分明。
            return VGroup(
                circum_back, tri, circum_front,
                dots_ABC, lbls_ABC,
                dot_H, lbl_H,
                seg_DH, seg_OH,
                seg_DA, seg_DB, seg_DC,
                status,
            )

        # ============================================================
        # 7. 动画控制：用 ValueTracker 让底面沿轴线平滑移动
        # ============================================================
        # ValueTracker 创建一个可被动画驱动的数值，初始为 -0.75R，表示 H 在 O 下方。
        h_tracker = ValueTracker(-0.75 * R)

        # 生成初始底面。
        base = make_base(h_tracker.get_value())

        # add_updater：每一帧根据 h_tracker 的当前值重新生成底面。
        # m.become(...) 用新的 VGroup 替换原有内容，从而实现平滑连续变化。
        base.add_updater(lambda m: m.become(make_base(h_tracker.get_value())))

        # ============================================================
        # 8. 把静态元素加入场景
        # ============================================================
        # 注意顺序：背半球虚线在底层，前半球实线在上层，这样才有球的立体感。
        self.add(sphere_back, sphere, axis,
                 dot_O, lbl_O, dot_D, lbl_D, base)
        self.wait(0.5)

        # ============================================================
        # 9. 播放动画：h 从 -0.75R 移动到 +0.75R，再自动返回
        # ============================================================
        # there_and_back 会先正向再反向，省去写两个动画的麻烦。
        self.play(
            h_tracker.animate.set_value(0.75 * R),
            run_time=8,
            rate_func=there_and_back,
        )
        self.wait(1)
