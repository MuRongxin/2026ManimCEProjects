from manim import *
import numpy as np

# ============================================================
# 字体 & 颜色（内联，不依赖外部文件）
# ============================================================
FONT_CN = "得意黑"
FONT_SERIF = "文悦新青年体 (须授权)"

CLR_TEAL       = ManimColor("#39c5bb")
CLR_CRIMSON    = ManimColor("#C1003C")
CLR_CYAN_DEEP  = ManimColor("#11999e")
CLR_ROSE       = ManimColor("#ff2e63")
CLR_MINT       = ManimColor("#79D87E")
CLR_CREAM      = ManimColor("#fff4e1")
CLR_SALMON     = ManimColor("#ffaaa5")
CLR_SKY        = ManimColor("#b9d7ea")
CLR_CORNFLOWER = ManimColor("#7dace4")

# ---- 默认字号（全局可调）----
DEFAULT_TEXT_SIZE  = 25   # Text 默认大小
DEFAULT_MATH_SIZE  = 30   # MathTex 默认大小

# ============================================================
# 公共工具函数
# ============================================================

def _T(text: str, font_size: int = DEFAULT_TEXT_SIZE, **kwargs) -> Text:
    """纯中文文本"""
    defaults = {"font": FONT_CN, "color": CLR_CREAM}
    defaults.update(kwargs)
    return Text(text, font_size=font_size, **defaults)


def _M(tex: str, font_size: int = DEFAULT_MATH_SIZE, **kwargs) -> MathTex:
    """纯数学公式"""
    defaults = {"color": CLR_CREAM}
    defaults.update(kwargs)
    return MathTex(tex, stroke_width=1, font_size=font_size, **defaults)


def _stem_vgroup(*mobjects) -> VGroup:
    """题干横向排列（题号+公式+文本混排），中线对齐"""
    grp = VGroup(*mobjects)
    grp.arrange(RIGHT, aligned_edge=ORIGIN, buff=0.08)
    return grp


def _opt_vgroup(*mobjects) -> VGroup:
    """选项横向排列（标签+内容混排），中线对齐"""
    grp = VGroup(*mobjects)
    grp.arrange(RIGHT, aligned_edge=ORIGIN, buff=0.08)
    return grp


def _choice_row(label: str, tex: str,
                  text_size: int = DEFAULT_TEXT_SIZE,
                  math_size: int = DEFAULT_MATH_SIZE,
                  color=CLR_CREAM) -> VGroup:
    """单个选项：字母标签 + 数学公式"""
    t = _T(label + " ", font_size=text_size, color=color)
    m = _M(tex, font_size=math_size, color=color)
    grp = VGroup(t, m)
    grp.arrange(RIGHT, aligned_edge=ORIGIN, buff=0.05)
    return grp


def _four_options(a_tex, b_tex, c_tex, d_tex,
                  text_size: int = DEFAULT_TEXT_SIZE,
                  math_size: int = DEFAULT_MATH_SIZE,
                  layout: str = "row",
                  colors=None) -> VGroup:
    """四个选项
    layout: "row" 横向一行 / "grid" 两行两列
    """
    if colors is None:
        colors = [CLR_CREAM] * 4

    a = _choice_row("A.", a_tex, text_size=text_size, math_size=math_size, color=colors[0])
    b = _choice_row("B.", b_tex, text_size=text_size, math_size=math_size, color=colors[1])
    c = _choice_row("C.", c_tex, text_size=text_size, math_size=math_size, color=colors[2])
    d = _choice_row("D.", d_tex, text_size=text_size, math_size=math_size, color=colors[3])

    if layout == "row":
        grp = VGroup(a, b, c, d)
        grp.arrange(RIGHT, buff=0.6)
    else:  # grid: 2x2
        row1 = VGroup(a, b)
        row1.arrange(RIGHT, buff=0.8, aligned_edge=UP)
        row2 = VGroup(c, d)
        row2.arrange(RIGHT, buff=0.8, aligned_edge=UP)
        grp = VGroup(row1, row2)
        grp.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        # 列对齐：B/D 推到同一竖线，且不覆盖 C
        col2_x = max(b.get_left()[0], c.get_right()[0] + 0.8)
        b.shift(RIGHT * (col2_x - b.get_left()[0]))
        d.shift(RIGHT * (col2_x - d.get_left()[0]))

    return grp


def _wrap_stem(stem: VGroup, break_at: int) -> VGroup:
    """题干换行：在 break_at 之后断行，第二行对齐到题号后第一个字"""
    line1 = VGroup(*stem[:break_at + 1])
    line1.arrange(RIGHT, aligned_edge=ORIGIN, buff=0.08)

    line2 = VGroup(*stem[break_at + 1:])
    line2.arrange(RIGHT, aligned_edge=ORIGIN, buff=0.08)

    wrapped = VGroup(line1, line2)
    wrapped.arrange(DOWN, aligned_edge=LEFT, buff=0.15)

    # 第二行对齐到题号后第一个字
    # 找到 stem[0] 中 "．" 的位置，其下一个字符就是第一个内容字
    if hasattr(stem[0], '__getitem__') and hasattr(stem[0], 'text'):
        dot_idx = stem[0].text.find('．')
        if dot_idx >= 0 and len(stem[0]) > dot_idx + 1:
            line2.align_to(stem[0][dot_idx + 1], LEFT)
        elif len(stem) > 1:
            line2.align_to(stem[1], LEFT)
        else:
            line2.align_to(stem[0], LEFT)
    elif len(stem) > 1:
        line2.align_to(stem[1], LEFT)
    elif len(stem) > 0:
        line2.align_to(stem[0], LEFT)

    # 保存对齐引用，供 _assemble_problem 使用
    # 换行后 stem 不再是原始平铺结构，需要保存 "．" 的引用
    if hasattr(stem[0], '__getitem__') and len(stem[0]) > 1:
        wrapped._dot_ref = stem[0][1]  # "．" submobject
    else:
        wrapped._dot_ref = stem[0]

    return wrapped


def _assemble_problem(stem: VGroup, opts: VGroup) -> VGroup:
    """组装题干+选项，选项对齐到题干第一个字"""
    problem = VGroup(stem, opts)
    problem.arrange(DOWN, buff=0.2)
    # 选项左边缘对齐到题号后第一个内容的左边缘
    ref = getattr(stem, '_dot_ref', None)
    if ref is None:
        ref = stem[0][1] if hasattr(stem[0], '__getitem__') and len(stem[0]) > 1 else stem[0]
    opts.align_to(ref, LEFT).shift(RIGHT * .3)
    return problem


def _assemble_multi(stem: VGroup, opt_a, opt_b, opt_c, opt_d,
                    option_layout: str = "col") -> VGroup:
    """组装多选题：题干 + 选项
    option_layout: "col" 纵向 / "row" 横向一行 / "grid" 两行两列
    """
    if option_layout == "row":
        opts_grp = VGroup(opt_a, opt_b, opt_c, opt_d)
        opts_grp.arrange(RIGHT, buff=0.5)
    elif option_layout == "grid":
        row1 = VGroup(opt_a, opt_b)
        row1.arrange(RIGHT, buff=0.8, aligned_edge=UP)
        row2 = VGroup(opt_c, opt_d)
        row2.arrange(RIGHT, buff=0.8, aligned_edge=UP)
        opts_grp = VGroup(row1, row2)
        opts_grp.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        # 列对齐：B/D 推到同一竖线，且不覆盖 C
        col2_x = max(opt_b.get_left()[0], opt_c.get_right()[0] + 0.8)
        opt_b.shift(RIGHT * (col2_x - opt_b.get_left()[0]))
        opt_d.shift(RIGHT * (col2_x - opt_d.get_left()[0]))
    else:  # col
        opts_grp = VGroup(opt_a, opt_b, opt_c, opt_d)
        opts_grp.arrange(DOWN, aligned_edge=LEFT, buff=0.2)

    problem = VGroup(stem, opts_grp)
    problem.arrange(DOWN, buff=0.4)
    # 选项组左边缘对齐到题号后第一个内容的左边缘
    if len(stem) > 1:
        # 选项 A 的第一个元素（标签 "A. "）左边缘对齐到 stem[1]（题号后第一个字）
        offset = stem[1].get_left()[0] - opt_a[0].get_left()[0]
        opts_grp.shift(RIGHT * offset)
    return problem


# ============================================================
# 第 1 题
# ============================================================
def problem_01(text_size: int = DEFAULT_TEXT_SIZE,
               math_size: int = DEFAULT_MATH_SIZE,
               option_layout: str = "row") -> VGroup:
    """$(1-3i)^2=$"""
    ts = text_size
    ms = math_size
    opt_ts = max(18, ts - 2)
    opt_ms = max(18, ms - 2)

    stem = _stem_vgroup(
        _T("1．", font_size=ts),
        _M(r"(1-3i)^2 =", font_size=ms),
    )
    opts = _four_options(
        r"-8+6i", r"-8-6i", r"8+6i", r"8-6i",
        text_size=opt_ts, math_size=opt_ms, layout=option_layout,
    )
    return _assemble_problem(stem, opts)


# ============================================================
# 第 2 题
# ============================================================
def problem_02(text_size: int = DEFAULT_TEXT_SIZE,
               math_size: int = DEFAULT_MATH_SIZE,
               option_layout: str = "row") -> VGroup:
    """集合运算"""
    ts = text_size
    ms = math_size
    opt_ts = max(18, ts - 2)
    opt_ms = max(18, ms - 2)

    stem = _stem_vgroup(
        _T("2．若 ", font_size=ts),
        _M(r"A = \{0,1,3,6,9\}", font_size=ms),
        _T("，", font_size=ts),
        _M(r"B = \{x \mid \sqrt{x}=x\}", font_size=ms),
        _T("，则 ", font_size=ts),
        _M(r"A \cap B =", font_size=ms),
    )
    opts = _four_options(
        r"\{0,1\}", r"\{3,6\}", r"\{0,1,9\}", r"\{3,6,9\}",
        text_size=opt_ts, math_size=opt_ms, layout=option_layout,
    )
    return _assemble_problem(stem, opts)


# ============================================================
# 第 3 题
# ============================================================
def problem_03(text_size: int = DEFAULT_TEXT_SIZE,
               math_size: int = DEFAULT_MATH_SIZE,
               option_layout: str = "row") -> VGroup:
    """向量点积"""
    ts = text_size
    ms = math_size
    opt_ts = max(18, ts - 2)
    opt_ms = max(18, ms - 2)

    stem = _stem_vgroup(
        _T("3．已知向量 ", font_size=ts),
        _M(r"\boldsymbol{a} ,\boldsymbol{b}", font_size=ms),
        _T(" 满足 ", font_size=ts),
        _M(r"|\boldsymbol{a}+\boldsymbol{b}|=1", font_size=ms),
        _T("，", font_size=ts),
        _M(r"|\boldsymbol{a}-\boldsymbol{b}|=3", font_size=ms),
        _T("，则 ", font_size=ts),
        _M(r"\boldsymbol{a}\cdot\boldsymbol{b} =", font_size=ms),
    )
    opts = _four_options(
        r"2", r"1", r"-\dfrac{1}{2}", r"-2",
        text_size=opt_ts, math_size=opt_ms, layout=option_layout,
    )
    return _assemble_problem(stem, opts)


# ============================================================
# 第 4 题
# ============================================================
def problem_04(text_size: int = DEFAULT_TEXT_SIZE,
               math_size: int = DEFAULT_MATH_SIZE,
               option_layout: str = "row",
               wrap_after: int = None) -> VGroup:
    """双曲线渐近线
    wrap_after: stem 元素索引，在该元素之后换行（如 6 = "，则 " 之后）
    """
    ts = text_size
    ms = math_size
    opt_ts = max(18, ts - 2)
    opt_ms = max(18, ms - 2)

    stem = _stem_vgroup(
        _T("4．双曲线 ", font_size=ts),
        _M(r"C:\frac{x^2}{a^2}-\frac{y^2}{b^2}=1\,(a>0,\,b>0)", font_size=ms),
        _T(" 过点 ", font_size=ts),
        _M(r"(1,0)", font_size=ms),
        _T(" 和 ", font_size=ts),
        _M(r"\left(\frac{\sqrt{7}}{2},3\right)", font_size=ms),
        _T("，则 ", font_size=ts),
        _M(r"C", font_size=ms),
        _T(" 的渐近线方程为", font_size=ts),
    )
    if wrap_after is not None:
        stem = _wrap_stem(stem, wrap_after)

    opts = _four_options(
        r"y=\pm3\sqrt{2}\,x",
        r"y=\pm2\sqrt{3}\,x",
        r"y=\pm\dfrac{\sqrt{6}}{3}x",
        r"y=\pm\dfrac{\sqrt{2}}{6}x",
        text_size=opt_ts, math_size=opt_ms, layout=option_layout,
    )
    return _assemble_problem(stem, opts)


# ============================================================
# 第 5 题
# ============================================================
def problem_05(text_size: int = DEFAULT_TEXT_SIZE,
               math_size: int = DEFAULT_MATH_SIZE,
               option_layout: str = "row",
               wrap_after: int = None) -> VGroup:
    """棱台体积
    wrap_after: stem 元素索引，在该元素之后换行（如 3 = "2,3" 之后）
    """
    ts = text_size
    ms = math_size
    opt_ts = max(18, ts - 2)
    opt_ms = max(18, ms - 2)

    stem = _stem_vgroup(
        _T("5．棱台上下底面均为有一个内角为 ", font_size=ts),
        _M(r"60^{\circ}", font_size=ms),
        _T(" 的菱形，且上下底面边长分别为 ", font_size=ts),
        _M(r"2,3 .", font_size=ms),
        _T("该棱台的高为 ", font_size=ts),
        _M(r"\sqrt 3", font_size=ms),
        _T("，则该棱台体积为", font_size=ts),
    )
    if wrap_after is not None:
        stem = _wrap_stem(stem, wrap_after)

    opts = _four_options(
        r"\dfrac{19}{12}", r"\dfrac{19}{6}", r"\dfrac{19}{4}", r"\dfrac{19}{2}",
        text_size=opt_ts, math_size=opt_ms, layout=option_layout,
    )
    return _assemble_problem(stem, opts)


# ============================================================
# 第 6 题
# ============================================================
def problem_06(text_size: int = DEFAULT_TEXT_SIZE,
               math_size: int = DEFAULT_MATH_SIZE,
               option_layout: str = "row",
               wrap_after: int = None) -> VGroup:
    """排列组合
    wrap_after: stem 元素索引，在该元素之后换行（如 8 = "甲、乙" 之后）
    """
    ts = text_size
    ms = math_size
    opt_ts = max(18, ts - 2)
    opt_ms = max(18, ms - 2)

    stem = _stem_vgroup(
        _T("6．甲、乙、丙、丁等 ", font_size=ts),
        _M(r"8", font_size=ms),
        _T(" 人分为 ", font_size=ts),
        _M(r"A", font_size=ms),
        _T("，", font_size=ts),
        _M(r"B", font_size=ms),
        _T(" 两技术小组，要求每组 ", font_size=ts),
        _M(r"4", font_size=ms),
        _T(" 人，且甲、乙", font_size=ts),
        _T("必须在一组，丙、丁不能在一组，则不同的分配方案种数为", font_size=ts),
    )
    if wrap_after is not None:
        stem = _wrap_stem(stem, wrap_after)

    opts = _four_options(
        r"10", r"12", r"16", r"24",
        text_size=opt_ts, math_size=opt_ms, layout=option_layout,
    )
    return _assemble_problem(stem, opts)


# ============================================================
# 第 7 题
# ============================================================
def problem_07(text_size: int = DEFAULT_TEXT_SIZE,
               math_size: int = DEFAULT_MATH_SIZE,
               option_layout: str = "row") -> VGroup:
    """三角函数"""
    ts = text_size
    ms = math_size
    opt_ts = max(18, ts - 2)
    opt_ms = max(18, ms - 2)

    stem = _stem_vgroup(
        _T("7．已知 ", font_size=ts),
        _M(r"\alpha", font_size=ms),
        _T(" 为第二象限角，且 ", font_size=ts),
        _M(r"3\sin2\alpha\cos\alpha=8\sin\alpha\cos2\alpha", font_size=ms),
        _T("，则 ", font_size=ts),
        _M(r"\frac{1+\sin\alpha}{2-\cos\alpha} =", font_size=ms),
    )
    opts = _four_options(
        r"\dfrac{3}{4}", r"\dfrac{3}{2}", r"\dfrac{1}{2}", r"\dfrac{5}{8}",
        text_size=opt_ts, math_size=opt_ms, layout=option_layout,
    )
    return _assemble_problem(stem, opts)


# ============================================================
# 第 8 题
# ============================================================
def problem_08(text_size: int = DEFAULT_TEXT_SIZE,
               math_size: int = DEFAULT_MATH_SIZE,
               option_layout: str = "row",
               wrap_after: int = None) -> VGroup:
    """函数性质
    wrap_after: stem 元素索引，在该元素之后换行（如 6 = " 时，" 之后）
    """
    ts = text_size
    ms = math_size
    opt_ts = max(18, ts - 2)
    opt_ms = max(18, ms - 2)

    stem = _stem_vgroup(
        _T("8．若 ", font_size=ts),
        _M(r"f(x)", font_size=ms),
        _T(" 为偶函数，且 ", font_size=ts),
        _M(r"f(x)+f(x-2)=0", font_size=ms),
        _T("．当 ", font_size=ts),
        _M(r"x\in\left[\frac{3}{2},3\right]", font_size=ms),
        _T(" 时，", font_size=ts),
        _M(r"f(x)=x^2+ax+b", font_size=ms),
        _T("，则", font_size=ts),
    )
    if wrap_after is not None:
        stem = _wrap_stem(stem, wrap_after)

    opts = _four_options(
        r"a=-2,\;b=-3", r"a=-2,\;b=3", r"a=-4,\;b=-3", r"a=-4,\;b=3",
        text_size=opt_ts, math_size=opt_ms, layout=option_layout,
    )
    return _assemble_problem(stem, opts)


# ============================================================
# 第 9 题（多选）
# ============================================================
def problem_09(text_size: int = DEFAULT_TEXT_SIZE,
               math_size: int = DEFAULT_MATH_SIZE,
               option_layout: str = "col") -> VGroup:
    """圆的方程"""
    ts = text_size
    ms = math_size
    opt_ts = max(18, ts - 2)
    opt_ms = max(18, ms - 2)

    stem = _stem_vgroup(
        _T("9．", font_size=ts),
        _T("已知 ", font_size=ts),
        _M(r"\odot O:x^2+y^2=1", font_size=ms),
        _T("，", font_size=ts),
        _M(r"\odot A:x^2+y^2-6x-8y+k=0", font_size=ms),
        _T("，则", font_size=ts),
    )
    opt_a = _opt_vgroup(
        _T("A. ", font_size=opt_ts),
        _T("点 ", font_size=opt_ts),
        _M("A", font_size=opt_ms),
        _T(" 的坐标为 ", font_size=opt_ts),
        _M("(-3,-4)", font_size=opt_ms),
    )
    opt_b = _opt_vgroup(
        _T("B. ", font_size=opt_ts),
        _T("当 ", font_size=opt_ts),
        _M("k=9", font_size=opt_ms),
        _T(" 时，", font_size=opt_ts),
        _M(r"\odot A", font_size=opt_ms),
        _T(" 与 ", font_size=opt_ts),
        _M("x", font_size=opt_ms),
        _T(" 轴相切", font_size=opt_ts),
    )
    opt_c = _opt_vgroup(
        _T("C. ", font_size=opt_ts),
        _T("当 ", font_size=opt_ts),
        _M("k=-11", font_size=opt_ms),
        _T(" 时，", font_size=opt_ts),
        _M(r"\odot A", font_size=opt_ms),
        _T(" 和 ", font_size=opt_ts),
        _M(r"\odot O", font_size=opt_ms),
        _T(" 相切", font_size=opt_ts),
    )
    opt_d = _opt_vgroup(
        _T("D. ", font_size=opt_ts),
        _T("当 ", font_size=opt_ts),
        _M(r"\odot O", font_size=opt_ms),
        _T(" 和 ", font_size=opt_ts),
        _M(r"\odot A", font_size=opt_ms),
        _T(" 相交时，两交点所在直线方程为 ", font_size=opt_ts),
        _M("6x+8y-k-2=0", font_size=opt_ms),
    )
    return _assemble_multi(stem, opt_a, opt_b, opt_c, opt_d, option_layout)


# ============================================================
# 第 10 题（多选）
# ============================================================
def problem_10(text_size: int = DEFAULT_TEXT_SIZE,
               math_size: int = DEFAULT_MATH_SIZE,
               option_layout: str = "col",
               wrap_after: int = None) -> VGroup:
    """等比数列
    wrap_after: stem 元素索引，在该元素之后换行（如 9 = "，" 之后，"记" 开始新行）
    """
    ts = text_size
    ms = math_size
    opt_ts = max(18, ts - 2)
    opt_ms = max(18, ms - 2)

    stem = _stem_vgroup(
        _T("10．", font_size=ts),
        _T("等比数列 ", font_size=ts),
        _M(r"\{a_n\}", font_size=ms),
        _T(" 的公比 ", font_size=ts),
        _M(r"q\neq1", font_size=ms),
        _T("，", font_size=ts),
        _M(r"a_1>0", font_size=ms),
        _T("，", font_size=ts),
        _M(r"2a_3=a_1+a_2", font_size=ms),
        _T("，", font_size=ts),
        _T("记 ", font_size=ts),
        _M(r"\{a_n\}", font_size=ms),
        _T(" 的前 ", font_size=ts),
        _M("n", font_size=ms),
        _T(" 项和为 ", font_size=ts),
        _M("S_n", font_size=ms),
        _T("，则", font_size=ts),
    )
    if wrap_after is not None:
        stem = _wrap_stem(stem, wrap_after)
    opt_a = _opt_vgroup(
        _T("A. ", font_size=opt_ts),
        _M(r"q=-\frac{1}{2}", font_size=opt_ms),
    )
    opt_b = _opt_vgroup(
        _T("B. ", font_size=opt_ts),
        _M(r"S_n>\frac{2}{3}a_1", font_size=opt_ms),
    )
    opt_c = _opt_vgroup(
        _T("C. ", font_size=opt_ts),
        _M(r"2S_n+2=S_{n+1}+S_n", font_size=opt_ms),
    )
    opt_d = _opt_vgroup(
        _T("D. ", font_size=opt_ts),
        _M(r"S_1+S_2+\cdots+S_n>\frac{2n}{3}a_1", font_size=opt_ms),
    )
    return _assemble_multi(stem, opt_a, opt_b, opt_c, opt_d, option_layout)


# ============================================================
# 第 11 题（多选）
# ============================================================
def problem_11(text_size: int = DEFAULT_TEXT_SIZE,
               math_size: int = DEFAULT_MATH_SIZE,
               option_layout: str = "col",
               wrap_after: int = None) -> VGroup:
    """抛物线与等边三角形
    wrap_after: stem 元素索引，在该元素之后换行（如 9 = "，" 之后，△ABC 开始新行）
    """
    ts = text_size
    ms = math_size
    opt_ts = max(18, ts - 2)
    opt_ms = max(18, ms - 2)

    stem = _stem_vgroup(
        _T("11．", font_size=ts),
        _T("已知抛物线 ", font_size=ts),
        _M(r"E:y^2=8x", font_size=ms),
        _T("，斜率为 ", font_size=ts),
        _M("k", font_size=ms),
        _M("(k>0)", font_size=ms),
        _T(" 的直线 ", font_size=ts),
        _M("l", font_size=ms),
        _T(" 过点 ", font_size=ts),
        _M("(-1,0),", font_size=ms),
        _M(r"\triangle ABC", font_size=ms),
        _T("为等边三角形，且 ", font_size=ts),
        _M("A", font_size=ms),
        _T(" 在 ", font_size=ts),
        _T("抛物线 ", font_size=ts),
        _M("E", font_size=ms),
        _T(" 上，", font_size=ts),
        _M("B", font_size=ms),
        _T("，", font_size=ts),
        _M("C", font_size=ms),
        _T(" 均在 ", font_size=ts),
        _M("l", font_size=ms),
        _T(" 上，则", font_size=ts),
    )
    if wrap_after is not None:
        stem = _wrap_stem(stem, wrap_after)
    opt_a = _opt_vgroup(
        _T("A. ", font_size=opt_ts),
        _T("抛物线 ", font_size=opt_ts),
        _M("E", font_size=opt_ms),
        _T(" 的准线方程为 ", font_size=opt_ts),
        _M("x=-2", font_size=opt_ms),
    )
    opt_b = _opt_vgroup(
        _T("B. ", font_size=opt_ts),
        _T("当 ", font_size=opt_ts),
        _M("l", font_size=opt_ms),
        _T(" 与 ", font_size=opt_ts),
        _M("E", font_size=opt_ms),
        _T(" 无交点时，", font_size=opt_ts),
        _M(r"k>\sqrt{2}", font_size=opt_ms),
    )
    opt_c = _opt_vgroup(
        _T("C. ", font_size=opt_ts),
        _T("当 ", font_size=opt_ts),
        _M("l", font_size=opt_ms),
        _T(" 与 ", font_size=opt_ts),
        _M("E", font_size=opt_ms),
        _T(" 相切于 ", font_size=opt_ts),
        _M("B", font_size=opt_ms),
        _T(" 时，", font_size=opt_ts),
        _M("AB", font_size=opt_ms),
        _T(" 过 ", font_size=opt_ts),
        _M("E", font_size=opt_ms),
        _T(" 的焦点 ", font_size=opt_ts),
        _M("F", font_size=opt_ms),
    )
    opt_d = _opt_vgroup(
        _T("D. ", font_size=opt_ts),
        _M("k=", font_size=opt_ms),
        _M("2", font_size=opt_ms),
        _T(" 时，", font_size=opt_ts),
        _M(r"\triangle ABC", font_size=opt_ms),
        _T(" 面积的最小值为 ", font_size=opt_ts),
        _M(r"\frac{\sqrt{3}}{15}", font_size=opt_ms),
    )
    return _assemble_multi(stem, opt_a, opt_b, opt_c, opt_d, option_layout)


# ============================================================
# 第 12 题（填空）
# ============================================================
def problem_12(text_size: int = DEFAULT_TEXT_SIZE,
               math_size: int = DEFAULT_MATH_SIZE) -> VGroup:
    """等差数列求和"""
    ts = text_size
    ms = math_size

    stem = _stem_vgroup(
        _T("12．记 ", font_size=ts),
        _M("S_n", font_size=ms),
        _T(" 为等差数列 ", font_size=ts),
        _M(r"\{a_n\}", font_size=ms),
        _T(" 的前 ", font_size=ts),
        _M("n", font_size=ms),
        _T(" 项和，若 ", font_size=ts),
        _M("a_1=-1", font_size=ms),
        _T("，", font_size=ts),
        _M("a_4=5", font_size=ms),
        _T("，则 ", font_size=ts),
        _M("S_6", font_size=ms),
        _T("=____", font_size=ts),
    )
    return stem


# ============================================================
# 第 13 题（填空）
# ============================================================
def problem_13(text_size: int = DEFAULT_TEXT_SIZE,
               math_size: int = DEFAULT_MATH_SIZE) -> VGroup:
    """函数零点"""
    ts = text_size
    ms = math_size

    stem = _stem_vgroup(
        _T("13．若函数 ", font_size=ts),
        _M(r"f(x)=2^x+2^{2-x}-m", font_size=ms),
        _T(" 有两个零点，则 ", font_size=ts),
        _M("m", font_size=ms),
        _T(" 的取值范围为______", font_size=ts),
    )
    return stem


# ============================================================
# 第 14 题（填空）
# ============================================================
def problem_14(text_size: int = DEFAULT_TEXT_SIZE,
               math_size: int = DEFAULT_MATH_SIZE,
               wrap_after: int = None) -> VGroup:
    """球的内接三角形
    wrap_after: stem 元素索引，在该元素之后换行（如 14 = " 为正三角形．" 之后）
    """
    ts = text_size
    ms = math_size

    stem = _stem_vgroup(
        _T("14．球 ", font_size=ts),
        _M("O", font_size=ms),
        _T(" 的体积为 ", font_size=ts),
        _M(r"4\sqrt{3}\pi", font_size=ms),
        _T("，点 ", font_size=ts),
        _M("A", font_size=ms),
        _T("，", font_size=ts),
        _M("B", font_size=ms),
        _T("，", font_size=ts),
        _M("C", font_size=ms),
        _T("，", font_size=ts),
        _M("D", font_size=ms),
        _T(" 均在球上，", font_size=ts),
        _M(r"\triangle ABC", font_size=ms),
        _T(" 为正三角形．", font_size=ts),
        _T("若 ", font_size=ts),
        _M("DA=DB=DC=2", font_size=ms),
        _T("，则 ", font_size=ts),
        _M(r"\triangle ABC", font_size=ms),
        _T(" 的面积为________", font_size=ts),
    )
    if wrap_after is not None:
        stem = _wrap_stem(stem, wrap_after)
    return stem
   

# ============================================================
# 解答题
# ============================================================

# ---- 第 15 题图形：频率分布直方图 ----
def problem_15_histogram() -> VGroup:
    """频率分布直方图：坐标轴 + 直方图 + 标签"""
    axes = Axes(
        x_range=[340, 430, 10], y_range=[0, 0.03, 0.005],
        x_length=5, y_length=2.5,
        axis_config={"color": CLR_CREAM, "stroke_width": 1},
        x_axis_config={"numbers_to_include": range(350, 430, 10)},
        y_axis_config={"numbers_to_include": np.arange(0, 0.031, 0.005)},
    )
    x_label = axes.get_x_axis_label(
        Text("时间（天）", font=FONT_CN, font_size=16, color=CLR_CREAM),
        edge=DOWN, buff=.2,
    )
    y_label = axes.get_y_axis_label(
        Text("频率/组距", font=FONT_CN, font_size=16, color=CLR_CREAM),
        edge=LEFT, buff=.2,
    )

    data = [
        (345, 355, 0.005),
        (355, 365, 0.010),
        (365, 375, 0.015),
        (375, 385, 0.020),
        (385, 395, 0.025),
        (395, 405, 0.015),
        (405, 415, 0.0075),
        (415, 425, 0.005),
    ]
    bars = VGroup()
    for left, right, height in data:
        bl = axes.c2p(left, 0)
        tr = axes.c2p(right, height)
        w = (axes.c2p(right, 0) - axes.c2p(left, 0))[0]
        h = (axes.c2p(0, height) - axes.c2p(0, 0))[1]
        bar = Rectangle(
            width=w, height=h,
            fill_opacity=0.5, fill_color=CLR_SKY,
            stroke_width=1, stroke_color=CLR_CREAM,
        )
        bar.move_to((bl + tr) / 2)
        bars.add(bar)

    return VGroup(axes, x_label, y_label, bars)


# ---- 第 15 题题干 ----
def problem_15(text_size: int = DEFAULT_TEXT_SIZE,
               math_size: int = DEFAULT_MATH_SIZE) -> VGroup:
    """频率分布直方图"""
    ts = text_size
    ms = math_size

    lines = VGroup()
    lines.add(_stem_vgroup(_T("15．", font_size=ts), _T("（13 分）", font_size=ts)))
    lines.add(_T("某工厂抽取一批电子元件检测，记录第一次出现故障的时间（天），", font_size=ts))
    lines.add(_T("绘制成如下的频率分布直方图：", font_size=ts))
    lines.add(_T("（1）求第一次出现故障的时间的第一四分位数和中位数；", font_size=ts))
    lines.add(_stem_vgroup(
        _T("（2）", font_size=ts),
        _M(r"\hat{p}", font_size=ms),
        _T(" 为首次故障时间小于 365 天的概率估计值．", font_size=ts),
    ))
    lines.add(_stem_vgroup(
        _T("（i）求 ", font_size=ts),
        _M(r"\hat{p}", font_size=ms),
        _T("；", font_size=ts),
    ))
    lines.add(_stem_vgroup(
        _T("（ii）工厂向某用户销售 ", font_size=ts),
        _M("100", font_size=ms),
        _T(" 件电子元件，", font_size=ts),
        _M("X", font_size=ms),
        _T(" 为这 ", font_size=ts),
        _M("100", font_size=ms),
        _T(" 件产品首次出现故障小于 365 天的件数，", font_size=ts),
    ))
    lines.add(_stem_vgroup(
        _T("若 ", font_size=ts),
        _M(r"X \sim B(100, \hat{p})", font_size=ms),
        _T("，求 ", font_size=ts),
        _M("E(X)", font_size=ms),
        _T("，", font_size=ts),
        _M("D(X)", font_size=ms),
        _T("．", font_size=ts),
    ))
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    return lines


# ---- 第 16 题图形：三棱锥 ----
def problem_16_fig(axes) -> VGroup:
    """三棱锥 A-BCD 示意图，使用传入的 axes 坐标定位"""
    D = axes.c2p(0, 0)
    C = axes.c2p(3, 0)
    B = axes.c2p(2, 1.2)       # 纵减小、横增大，不超 C
    A = axes.c2p(1.5, 3.5)
    E = axes.c2p(1.1, 0.66)    # 在 DB 连线上，往右上挪

    sw = 2  # 统一加粗

    fig = VGroup()
    fig.add(DashedLine(D, B, color=CLR_CREAM, stroke_width=sw))
    fig.add(Line(D, C, color=CLR_CREAM, stroke_width=sw))
    fig.add(DashedLine(C, B, color=CLR_CREAM, stroke_width=sw))     # BC 虚线
    fig.add(Line(A, D, color=CLR_CREAM, stroke_width=sw))
    fig.add(Line(A, C, color=CLR_CREAM, stroke_width=sw))
    fig.add(DashedLine(A, B, color=CLR_CREAM, stroke_width=sw))     # AB 虚线
    fig.add(DashedLine(A, E, color=CLR_CREAM, stroke_width=sw))
    fig.add(DashedLine(C, E, color=CLR_CREAM, stroke_width=sw))

    fig.add(MathTex("D", color=CLR_CREAM, font_size=17,stroke_width=1).move_to(D + DL * 0.2))
    fig.add(MathTex("C", color=CLR_CREAM, font_size=17,stroke_width=1).move_to(C + DR * 0.2))
    fig.add(MathTex("B", color=CLR_CREAM, font_size=17,stroke_width=1).move_to(B + UR * 0.1))
    fig.add(MathTex("A", color=CLR_CREAM, font_size=17,stroke_width=1).move_to(A + UP * 0.2))
    fig.add(MathTex("E", color=CLR_CREAM, font_size=17,stroke_width=1).move_to(E + LEFT * 0.2))
    return fig


# ---- 第 16 题题干 ----
def problem_16(text_size: int = DEFAULT_TEXT_SIZE,
               math_size: int = DEFAULT_MATH_SIZE,
               wrap_after: int = None) -> VGroup:
    """三棱锥几何证明
    wrap_after: 题干第二行在指定元素之后换行（如 6 = " 上，" 之后）
    """
    ts = text_size
    ms = math_size

    lines = VGroup()
    lines.add(_stem_vgroup(_T("16．", font_size=ts), _T("（15 分）", font_size=ts)))

    stem_body = _stem_vgroup(
        _T("如图，三棱锥 ", font_size=ts),
        _M("A-BCD", font_size=ms),
        _T(" 中，点 ", font_size=ts),
        _M("E", font_size=ms),
        _T(" 在 ", font_size=ts),
        _M("BD", font_size=ms),
        _T(" 上，", font_size=ts),
        _T("且 ", font_size=ts),
        _M(r"AE \perp CE", font_size=ms),
        _T("，", font_size=ts),
        _M(r"AE \perp DE", font_size=ms),
        _T("，", font_size=ts),
        _M(r"CD \perp AD", font_size=ms),
        _T("．", font_size=ts),
    )
    if wrap_after is not None:
        stem_body = _wrap_stem(stem_body, wrap_after)
    lines.add(stem_body)

    lines.add(_stem_vgroup(
        _T("（1）证明：", font_size=ts),
        _M(r"CD \perp AB", font_size=ms),
        _T("；", font_size=ts),
    ))

    subq2_line1 = _stem_vgroup(
        _T("（2）若 ", font_size=ts),
        _M("DE=2", font_size=ms),
        _T("，", font_size=ts),
        _M("BE=1", font_size=ms),
        _T("，", font_size=ts),
        _M("AE=2", font_size=ms),
        _T("，", font_size=ts),
        _M(r"CD=2\sqrt{3}", font_size=ms),
        _T("，", font_size=ts),
    )
    lines.add(subq2_line1)

    subq2_line2 = _stem_vgroup(
        _T("求直线 ", font_size=ts),
        _M("AD", font_size=ms),
        _T(" 与平面 ", font_size=ts),
        _M("ABC", font_size=ms),
        _T(" 所成角的正弦值．", font_size=ts),
    )
    lines.add(subq2_line2)

    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.2)

    # 对齐第(2)问续行："求" 对齐到 "若"
    if hasattr(subq2_line1[0], '__getitem__') and hasattr(subq2_line1[0], 'text'):
        paren_idx = subq2_line1[0].text.find('）')
        if paren_idx >= 0 and len(subq2_line1[0]) > paren_idx + 1:
            ref_x = subq2_line1[0][paren_idx + 1].get_left()[0]
            subq2_line2.shift(RIGHT * (ref_x - subq2_line2[0].get_left()[0]))

    return lines


# ---- 第 17 题 ----
def problem_17(text_size: int = DEFAULT_TEXT_SIZE,
               math_size: int = DEFAULT_MATH_SIZE) -> VGroup:
    """解三角形"""
    ts = text_size
    ms = math_size

    lines = VGroup()
    lines.add(_stem_vgroup(_T("17．", font_size=ts), _T("（15 分）", font_size=ts)))
    lines.add(_stem_vgroup(
        _T("在 ", font_size=ts),
        _M(r"\triangle ABC", font_size=ms),
        _T(" 中，已知 ", font_size=ts),
        _M(r"\cos B = \frac{3}{4}", font_size=ms),
        _T("，", font_size=ts),
        _M(r"\cos^2(A+C) + \sin A \sin C = 1", font_size=ms),
        _T("．", font_size=ts),
    ))
    lines.add(_stem_vgroup(
        _T("（1）证明：", font_size=ts),
        _M(r"\triangle ABC", font_size=ms),
        _T(" 为钝角三角形；", font_size=ts),
    ))
    lines.add(_stem_vgroup(
        _T("（2）若 ", font_size=ts),
        _M(r"\triangle ABC", font_size=ms),
        _T(" 的面积为 ", font_size=ts),
        _M(r"\frac{7}{4}", font_size=ms),
        _T("，求 ", font_size=ts),
        _M(r"\triangle ABC", font_size=ms),
        _T(" 的周长．", font_size=ts),
    ))
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    return lines


# ---- 第 18 题 ----
def problem_18(text_size: int = DEFAULT_TEXT_SIZE,
               math_size: int = DEFAULT_MATH_SIZE,
               wrap_after: int = None) -> VGroup:
    """椭圆与轨迹
    wrap_after: 题干第二行在指定元素之后换行（如 8 = " 截得的" 之后）
    """
    ts = text_size
    ms = math_size

    lines = VGroup()
    lines.add(_stem_vgroup(_T("18．", font_size=ts), _T("（17 分）", font_size=ts)))

    stem_body = _stem_vgroup(
        _T("椭圆 ", font_size=ts),
        _M(r"E: \frac{x^2}{a^2} + y^2 = 1\,(a>1)", font_size=ms),
        _T("，过 ", font_size=ts),
        _M("E", font_size=ms),
        _T(" 的右焦点且与 ", font_size=ts),
        _M("x", font_size=ms),
        _T(" 轴垂直的直线被 ", font_size=ts),
        _M("E", font_size=ms),
        _T(" 截得的", font_size=ts),
        _T("长度为 ", font_size=ts),
        _M("2", font_size=ms),
        _T("．", font_size=ts),
    )
    if wrap_after is not None:
        stem_body = _wrap_stem(stem_body, wrap_after)
    lines.add(stem_body)
    lines.add(_stem_vgroup(
        _T("（1）求 ", font_size=ts),
        _M("E", font_size=ms),
        _T(" 的离心率；", font_size=ts),
    ))
    lines.add(_stem_vgroup(
        _T("（2）", font_size=ts),
        _M("O", font_size=ms),
        _T(" 为坐标原点，给定点 ", font_size=ts),
        _M(r"G(t_0,0)\,(t_0 \neq 0)", font_size=ms),
        _T("，", font_size=ts),
        _M(r"A(x_0,y_0)\,(y_0 \neq 0)", font_size=ms),
        _T(" 在 ", font_size=ts),
        _M("E", font_size=ms),
        _T(" 上，", font_size=ts),
    ))
    lines.add(_stem_vgroup(
        _T("过点 ", font_size=ts),
        _M("A", font_size=ms),
        _T(" 作 ", font_size=ts),
        _M("y", font_size=ms),
        _T(" 轴的垂线，垂足为 ", font_size=ts),
        _M("B", font_size=ms),
        _T("，", font_size=ts),
        _M("AO", font_size=ms),
        _T(" 与 ", font_size=ts),
        _M("GB", font_size=ms),
        _T(" 交于点 ", font_size=ts),
        _M("P", font_size=ms),
        _T("，", font_size=ts),
    ))
    lines.add(_stem_vgroup(
        _T("当 ", font_size=ts),
        _M("A", font_size=ms),
        _T(" 在 ", font_size=ts),
        _M("E", font_size=ms),
        _T(" 上运动时，", font_size=ts),
        _M("P", font_size=ms),
        _T(" 的轨迹为 ", font_size=ts),
        _M("M", font_size=ms),
        _T("．", font_size=ts),
    ))
    lines.add(_stem_vgroup(
        _T("（i）求 ", font_size=ts),
        _M("M", font_size=ms),
        _T(" 的方程，并说明 ", font_size=ts),
        _M("M", font_size=ms),
        _T(" 是什么曲线；", font_size=ts),
    ))
    lines.add(_stem_vgroup(
        _T("（ii）", font_size=ts),
        _M("M", font_size=ms),
        _T(" 是否有中心点？当 ", font_size=ts),
        _M("t_0", font_size=ms),
        _T(" 为何值时，", font_size=ts),
        _M("M", font_size=ms),
        _T(" 有中心点？", font_size=ts),
    ))
    lines.add(_stem_vgroup(
        _T("当 ", font_size=ts),
        _M("M", font_size=ms),
        _T(" 有中心点时，平移 ", font_size=ts),
        _M("M", font_size=ms),
        _T(" 到 ", font_size=ts),
        _M(r"M'", font_size=ms),
        _T("，使 ", font_size=ts),
        _M("O", font_size=ms),
        _T(" 为 ", font_size=ts),
        _M(r"M'", font_size=ms),
        _T(" 的中心点，说明 ", font_size=ts),
        _M(r"M'", font_size=ms),
        _T(" 的形状．", font_size=ts),
    ))
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    return lines


# ---- 第 19 题 ----
def problem_19(text_size: int = DEFAULT_TEXT_SIZE,
               math_size: int = DEFAULT_MATH_SIZE,
               wrap_after: int = None) -> VGroup:
    """函数与导数
    wrap_after: 题干第二行在指定元素之后换行（如 6 = " 处的切线为 " 之后）
    """
    ts = text_size
    ms = math_size

    lines = VGroup()
    lines.add(_stem_vgroup(_T("19．", font_size=ts), _T("（17 分）", font_size=ts)))

    stem_body = _stem_vgroup(
        _T("已知函数 ", font_size=ts),
        _M(r"f(x) = xe^x + ax + b", font_size=ms),
        _T("，曲线 ", font_size=ts),
        _M("y=f(x)", font_size=ms),
        _T(" 在点 ", font_size=ts),
        _M("(0,f(0))", font_size=ms),
        _T(" 处的切线为 ", font_size=ts),
        _M("y=-2x+1", font_size=ms),
        _T("．", font_size=ts),
    )
    if wrap_after is not None:
        stem_body = _wrap_stem(stem_body, wrap_after)
    lines.add(stem_body)
    lines.add(_stem_vgroup(
        _T("（1）求 ", font_size=ts),
        _M("a", font_size=ms),
        _T("，", font_size=ts),
        _M("b", font_size=ms),
        _T("；", font_size=ts),
    ))
    lines.add(_stem_vgroup(
        _T("（2）当 ", font_size=ts),
        _M("x>0", font_size=ms),
        _T(" 时，", font_size=ts),
        _M("f(x+m)-f(x)>m", font_size=ms),
        _T("，求 ", font_size=ts),
        _M("m", font_size=ms),
        _T(" 的取值范围；", font_size=ts),
    ))
    lines.add(_stem_vgroup(
        _T("（3）当 ", font_size=ts),
        _M("x>0", font_size=ms),
        _T(" 时，", font_size=ts),
        _M("f(x+k)+f(k-x)>2f(k)", font_size=ms),
        _T("，求 ", font_size=ts),
        _M("k", font_size=ms),
        _T(" 的最小值．", font_size=ts),
    ))
    lines.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    return lines
