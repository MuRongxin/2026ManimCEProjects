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
