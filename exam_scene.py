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

        s10_D2 = VGroup(
            MathTex(r"\because\; S_n=\frac{2a_1}{3}\left[1-\left(-\frac{1}{2}\right)^n\right]",
                    color=BLUE, stroke_width=1, font_size=25),
            MathTex(r"\therefore\; S_1+S_2+\cdots+S_n",
                    color=BLUE, stroke_width=1, font_size=25),
            MathTex(r"=\frac{2a_1}{3}\left\{n-\left[\left(-\frac{1}{2}\right)"
                    r"+\left(-\frac{1}{2}\right)^2+\cdots"
                    r"+\left(-\frac{1}{2}\right)^n\right]\right\}",
                    color=BLUE, stroke_width=1, font_size=25),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        s10_D2.next_to(s10_D1, DOWN, buff=0.5, aligned_edge=LEFT)

        s10_D3 = VGroup(
            Text("由等比数列求和公式：", font=FONT_CN, color=CLR_SKY, font_size=20),
            MathTex(r"\left(-\frac{1}{2}\right)+\cdots+\left(-\frac{1}{2}\right)^n"
                    r"=\frac{-\frac{1}{2}\left[1-\left(-\frac{1}{2}\right)^n\right]}"
                    r"{1+\frac{1}{2}}"
                    r"=-\frac{1}{3}\left[1-\left(-\frac{1}{2}\right)^n\right]",
                    color=CLR_SKY, stroke_width=1, font_size=25),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        s10_D3.next_to(s10_D2, DOWN, buff=0.2, aligned_edge=LEFT)

        s10_D4 = VGroup(
            MathTex(r"\therefore\; S_1+\cdots+S_n"
                    r"=\frac{2a_1}{3}\left\{n+\frac{1}{3}"
                    r"\left[1-\left(-\frac{1}{2}\right)^n\right]\right\}",
                    color=BLUE, stroke_width=1, font_size=25),
            MathTex(r"=\frac{2n}{3}a_1+\frac{2a_1}{9}\left[1-\left(-\frac{1}{2}\right)^n\right]",
                    color=BLUE, stroke_width=1, font_size=25),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        s10_D4.next_to(s10_D3, DOWN, buff=0.2, aligned_edge=LEFT)

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
            Write(s10_D1), Write(s10_D2), Write(s10_D3), Write(s10_D4),
            Write(s10_D5), Write(s10_D6),
            lag_ratio=.8))
        self.wait(2)
