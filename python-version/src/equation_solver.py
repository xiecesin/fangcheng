"""
方程求解器模块
使用 sympy 库求解二次、三次和四次方程，提供详细的分步解决方案
支持输出 Markdown 格式的求解过程，公式使用 LaTeX 格式
"""

from sympy import symbols, solve, sqrt, cbrt, I, pi, simplify, expand, factor, Rational, pprint, latex, S
from sympy.abc import x
from typing import List, Union, Optional, Tuple
from dataclasses import dataclass, field
import sympy
import os
from datetime import datetime


@dataclass
class EquationSolution:
    """存储方程的解和详细信息"""
    equation_type: str
    coefficients: List[Union[int, float, sympy.Basic]]
    roots: List[sympy.Basic]
    steps: List[str] = field(default_factory=list)
    latex_steps: List[str] = field(default_factory=list)
    exact_form: bool = True
    markdown_content: str = ""


class MarkdownExporter:
    """Markdown 导出器，支持 LaTeX 公式"""
    
    @staticmethod
    def export_solution(solution: EquationSolution, filename: str = None) -> str:
        """将求解过程导出为 Markdown 格式"""
        lines = []
        
        # 标题
        if solution.equation_type == "quadratic":
            title = "二次方程求解"
            equation = "ax^2 + bx + c = 0"
        elif solution.equation_type == "cubic":
            title = "三次方程求解（卡尔达诺公式）"
            equation = "ax^3 + bx^2 + cx + d = 0"
        elif solution.equation_type == "quartic":
            title = "四次方程求解（费拉里方法）"
            equation = "ax^4 + bx^3 + cx^2 + dx + e = 0"
        else:
            title = "方程求解"
            equation = ""
        
        lines.append(f"# {title}")
        lines.append("")
        lines.append(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")
        
        # 原方程
        lines.append("## 原方程")
        lines.append("")
        lines.append("$$")
        lines.append(equation)
        lines.append("$$")
        lines.append("")
        
        # 系数
        lines.append("## 系数")
        lines.append("")
        coeffs_latex = ", ".join([latex(coeff) for coeff in solution.coefficients])
        lines.append("$$")
        lines.append(f"a = {coeffs_latex}")
        lines.append("$$")
        lines.append("")
        
        # 求解步骤
        lines.append("## 求解步骤")
        lines.append("")
        
        for i, (step_text, latex_step) in enumerate(zip(solution.steps, solution.latex_steps)):
            # 提取步骤标题
            if "步骤" in step_text:
                step_title = step_text.split('\n')[0].strip()
                lines.append(f"### {step_title}")
                lines.append("")
            
            # 添加 LaTeX 内容（换行格式）
            if latex_step:
                lines.append("$$")
                lines.append(latex_step)
                lines.append("$$")
                lines.append("")
        
        # 最终结果
        lines.append("## 最终结果")
        lines.append("")
        lines.append("### 精确符号解")
        lines.append("")
        
        for i, root in enumerate(solution.roots, 1):
            lines.append("$$")
            lines.append(f"x_{i} = {latex(root)}")
            lines.append("$$")
            lines.append("")
        
        lines.append("### 数值近似值")
        lines.append("")
        for i, root in enumerate(solution.roots, 1):
            numeric_val = sympy.N(root, 6)
            lines.append("$$")
            lines.append(f"x_{i} \\approx {latex(numeric_val)}")
            lines.append("$$")
            lines.append("")
        
        # 合并内容
        markdown_content = "\n".join(lines)
        solution.markdown_content = markdown_content
        
        # 保存到文件
        if filename:
            # 确保输出目录存在
            output_dir = os.path.dirname(filename)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            print(f"\n求解过程已保存到：{filename}")
        
        return markdown_content


class SymbolicSolver:
    """符号方程求解器，提供详细的手推步骤"""
    
    @staticmethod
    def format_expr(expr: sympy.Basic) -> str:
        """格式化 sympy 表达式为易读的字符串"""
        return sympy.srepr(expr)
    
    @staticmethod
    def print_step(step: str, title: str = ""):
        """打印一个步骤"""
        if title:
            print(f"\n{'='*60}")
            print(f"{title}")
            print(f"{'='*60}")
        print(step)
        print()
    
    @staticmethod
    def solve_quadratic(a: Union[int, float, sympy.Basic], 
                       b: Union[int, float, sympy.Basic], 
                       c: Union[int, float, sympy.Basic],
                       verbose: bool = True,
                       output_file: str = None) -> EquationSolution:
        """
        求解二次方程 ax² + bx + c = 0
        详细显示求根公式的推导过程
        """
        steps = []
        latex_steps = []
        
        # 转换为 sympy 符号
        a = sympy.sympify(a)
        b = sympy.sympify(b)
        c = sympy.sympify(c)
        
        if verbose:
            print("\n" + "="*70)
            print("二次方程求解：ax² + bx + c = 0")
            print("="*70)
            
            # 步骤 1: 写出方程
            step1 = f"步骤 1: 写出标准形式的二次方程"
            latex1 = f"{{{a}}}x^2 + {{{b}}}x + {{{c}}} = 0"
            print(f"\n{step1}")
            print(f"  {a}x² + {b}x + {c} = 0")
            steps.append(step1)
            latex_steps.append(latex1)
            
            # 步骤 2: 确认系数
            step2 = f"步骤 2: 确认系数"
            latex2 = f"a = {latex(a)}, \\quad b = {latex(b)}, \\quad c = {latex(c)}"
            print(f"\n{step2}")
            print(f"  a = {a}")
            print(f"  b = {b}")
            print(f"  c = {c}")
            steps.append(step2)
            latex_steps.append(latex2)
            
            # 步骤 3: 计算判别式
            step3 = f"步骤 3: 计算判别式 $\\Delta = b^2 - 4ac$"
            delta_expr = b**2 - 4*a*c
            latex3 = f"\\Delta = b^2 - 4ac = ({latex(b)})^2 - 4({latex(a)})({latex(c)}) = {latex(simplify(delta_expr))}"
            print(f"\n{step3}")
            print(f"  Δ = ({b})² - 4×({a})×({c})")
            print(f"  Δ = {b**2} - {4*a*c}")
            print(f"  Δ = {simplify(delta_expr)}")
            steps.append(step3)
            latex_steps.append(latex3)
            
            # 步骤 4: 判断根的情况
            step4 = f"步骤 4: 根据判别式判断根的情况"
            delta_val = sympy.N(delta_expr)
            if delta_val.is_real:
                if delta_val > 0:
                    desc = "方程有两个不相等的实根"
                    latex_desc = "\\Delta > 0: \\text{方程有两个不相等的实根}"
                elif delta_val == 0:
                    desc = "方程有两个相等的实根（重根）"
                    latex_desc = "\\Delta = 0: \\text{方程有两个相等的实根（重根）}"
                else:
                    desc = "方程有一对共轭复根"
                    latex_desc = "\\Delta < 0: \\text{方程有一对共轭复根}"
            else:
                desc = ""
                latex_desc = ""
            
            latex4 = f"\\Delta = {latex(simplify(delta_expr))}, \\quad {latex_desc}"
            print(f"\n{step4}")
            print(f"  Δ = {simplify(delta_expr)} {desc}")
            steps.append(step4)
            latex_steps.append(latex4)
            
            # 步骤 5: 应用求根公式
            step5 = f"步骤 5: 应用求根公式"
            latex5 = f"x = \\frac{{-b \\pm \\sqrt{{\\Delta}}}}{{2a}} = \\frac{{-({latex(b)}) \\pm \\sqrt{{{latex(simplify(delta_expr))}}}}}{{2({latex(a)})}}"
            print(f"\n{step5}")
            print(f"  求根公式：x = (-b ± √Δ) / (2a)")
            print(f"  代入系数：")
            print(f"  x = (-({b}) ± √({simplify(delta_expr)})) / (2×{a})")
            print(f"  x = ({-b} ± √({simplify(delta_expr)})) / ({2*a})")
            steps.append(step5)
            latex_steps.append(latex5)
            
            # 步骤 6: 计算根
            step6 = f"步骤 6: 计算最终结果"
            print(f"\n{step6}")
        
        # 使用求根公式计算
        sqrt_delta = sqrt(delta_expr)
        x1 = (-b + sqrt_delta) / (2*a)
        x2 = (-b - sqrt_delta) / (2*a)
        
        # 化简结果
        x1_simplified = simplify(x1)
        x2_simplified = simplify(x2)
        
        if verbose:
            print(f"  x₁ = {x1_simplified}")
            print(f"  x₂ = {x2_simplified}")
            
            latex6 = f"x_1 = {latex(x1_simplified)}, \\quad x_2 = {latex(x2_simplified)}"
            latex_steps.append(latex6)
            
            # 步骤 7: 数值近似（如果有符号表达式）
            step7 = f"步骤 7: 数值近似值"
            print(f"\n{step7}")
            print(f"  x₁ ≈ {sympy.N(x1_simplified, 6)}")
            print(f"  x₂ ≈ {sympy.N(x2_simplified, 6)}")
            steps.append(step7)
            latex_steps.append("")
            
            print("="*70)
        
        roots = [x1_simplified, x2_simplified]
        solution = EquationSolution(
            equation_type="quadratic",
            coefficients=[a, b, c],
            roots=roots,
            steps=steps,
            latex_steps=latex_steps,
            exact_form=True
        )
        
        # 如果指定了输出文件，导出 Markdown
        if output_file:
            MarkdownExporter.export_solution(solution, output_file)
        
        return solution
    
    @staticmethod
    def solve_cubic(a: Union[int, float, sympy.Basic],
                   b: Union[int, float, sympy.Basic],
                   c: Union[int, float, sympy.Basic],
                   d: Union[int, float, sympy.Basic],
                   verbose: bool = True,
                   output_file: str = None) -> EquationSolution:
        """
        求解三次方程 ax³ + bx² + cx + d = 0
        使用卡尔达诺公式，详细显示手推步骤
        """
        steps = []
        latex_steps = []
        
        # 转换为 sympy 符号
        a = sympy.sympify(a)
        b = sympy.sympify(b)
        c = sympy.sympify(c)
        d = sympy.sympify(d)
        
        if verbose:
            print("\n" + "="*70)
            print("三次方程求解：ax³ + bx² + cx + d = 0（卡尔达诺公式）")
            print("="*70)
            
            # 步骤 1: 写出方程
            step1 = "步骤 1: 写出标准形式的三次方程"
            latex1 = f"{{{a}}}x^3 + {{{b}}}x^2 + {{{c}}}x + {{{d}}} = 0"
            print(f"\n{step1}")
            print(f"  {a}x³ + {b}x² + {c}x + {d} = 0")
            steps.append(step1)
            latex_steps.append(latex1)
            
            # 步骤 2: 确认系数
            step2 = "步骤 2: 确认系数"
            latex2 = f"a = {latex(a)}, \\quad b = {latex(b)}, \\quad c = {latex(c)}, \\quad d = {latex(d)}"
            print(f"\n{step2}")
            print(f"  a = {a}")
            print(f"  b = {b}")
            print(f"  c = {c}")
            print(f"  d = {d}")
            steps.append(step2)
            latex_steps.append(latex2)
            
            # 步骤 3: 化为首一多项式
            step3 = "步骤 3: 两边除以首项系数，化为首一多项式"
            b_a = b/a
            c_a = c/a
            d_a = d/a
            latex3 = f"x^3 + {latex(simplify(b_a))}x^2 + {latex(simplify(c_a))}x + {latex(simplify(d_a))} = 0"
            print(f"\n{step3}")
            print(f"  x³ + ({b}/{a})x² + ({c}/{a})x + ({d}/{a}) = 0")
            print(f"  x³ + {simplify(b_a)}x² + {simplify(c_a)}x + {simplify(d_a)} = 0")
            steps.append(step3)
            latex_steps.append(latex3)
            
            # 步骤 4: 消去二次项
            step4 = "步骤 4: 通过变量代换消去二次项"
            p = c_a - b_a**2/3
            q = 2*b_a**3/27 - b_a*c_a/3 + d_a
            latex4 = f"\\text{{令 }} x = y - \\frac{{b}}{{3a}} = y - {latex(simplify(b_a/3))}"
            latex4 += f"\\\\ p = \\frac{{c}}{{a}} - \\frac{{b^2}}{{3a^2}} = {latex(simplify(p))}"
            latex4 += f"\\\\ q = \\frac{{2b^3}}{{27a^3}} - \\frac{{bc}}{{3a^2}} + \\frac{{d}}{{a}} = {latex(simplify(q))}"
            latex4 += f"\\\\ \\text{{得到：}} y^3 + py + q = 0"
            print(f"\n{step4}")
            print(f"  令 x = y - b/(3a)")
            print(f"  计算 p 和 q：")
            print(f"  p = c/a - b²/(3a²) = {simplify(c_a)} - {simplify(b_a**2/3)} = {simplify(p)}")
            print(f"  q = 2b³/(27a³) - bc/(3a²) + d/a")
            print(f"    = {simplify(2*b_a**3/27)} - {simplify(b_a*c_a/3)} + {simplify(d_a)}")
            print(f"    = {simplify(q)}")
            print(f"  得到简化形式：y³ + py + q = 0")
            print(f"  即：y³ + {simplify(p)}y + {simplify(q)} = 0")
            steps.append(step4)
            latex_steps.append(latex4)
            
            # 步骤 5: 计算判别式
            step5 = "步骤 5: 计算判别式"
            discriminant = (q/2)**2 + (p/3)**3
            latex5 = f"\\Delta = \\left(\\frac{{q}}{{2}}\\right)^2 + \\left(\\frac{{p}}{{3}}\\right)^3 = {latex(simplify(discriminant))}"
            print(f"\n{step5}")
            print(f"  Δ = (q/2)² + (p/3)³")
            print(f"  Δ = ({simplify(q)}/2)² + ({simplify(p)}/3)³")
            print(f"  Δ = {simplify((q/2)**2)} + {simplify((p/3)**3)}")
            print(f"  Δ = {simplify(discriminant)}")
            
            disc_val = sympy.N(discriminant)
            if disc_val.is_real:
                if disc_val > 0:
                    desc = "方程有一个实根和两个共轭复根"
                elif disc_val == 0:
                    desc = "方程有三个实根（至少两个相等）"
                else:
                    desc = "方程有三个不相等的实根（需要用三角函数表示）"
                print(f"  Δ {desc}")
            steps.append(step5)
            latex_steps.append(latex5)
            
            # 步骤 6: 应用卡尔达诺公式
            step6 = "步骤 6: 应用卡尔达诺公式求解 y"
            latex6 = f"y = \\sqrt[3]{{-\\frac{{q}}{{2}} + \\sqrt{{\\Delta}}}} + \\sqrt[3]{{-\\frac{{q}}{{2}} - \\sqrt{{\\Delta}}}}"
            latex6 += f"\\\\ u = \\sqrt[3]{{-\\frac{{q}}{{2}} + \\sqrt{{\\Delta}}}} = \\sqrt[3]{{{latex(simplify(-q/2))} + {latex(simplify(sqrt(discriminant)))}}}"
            latex6 += f"\\\\ v = \\sqrt[3]{{-\\frac{{q}}{{2}} - \\sqrt{{\\Delta}}}} = \\sqrt[3]{{{latex(simplify(-q/2))} - {latex(simplify(sqrt(discriminant)))}}}"
            print(f"\n{step6}")
            print(f"  卡尔达诺公式：")
            print(f"  y = ∛(-q/2 + √Δ) + ∛(-q/2 - √Δ)")
            print(f"  ")
            print(f"  计算 u = ∛(-q/2 + √Δ)：")
            print(f"  u = ∛({simplify(-q/2)} + {simplify(sqrt(discriminant))})")
            print(f"  ")
            print(f"  计算 v = ∛(-q/2 - √Δ)：")
            print(f"  v = ∛({simplify(-q/2)} - {simplify(sqrt(discriminant))})")
            steps.append(step6)
            latex_steps.append(latex6)
            
            # 步骤 7: 计算 y 的三个根
            step7 = "步骤 7: 计算 y 的三个根"
            latex7 = f"\\omega = \\frac{{-1 + \\sqrt{{3}}i}}{{2}} \\quad (\\text{{三次单位根}})"
            latex7 += f"\\\\ y_1 = u + v"
            latex7 += f"\\\\ y_2 = \\omega u + \\omega^2 v"
            latex7 += f"\\\\ y_3 = \\omega^2 u + \\omega v"
            print(f"\n{step7}")
            print(f"  令 ω = (-1 + √3·i)/2 为三次单位根")
            print(f"  y₁ = u + v")
            print(f"  y₂ = ωu + ω²v")
            print(f"  y₃ = ω²u + ωv")
            steps.append(step7)
            latex_steps.append(latex7)
            
            # 步骤 8: 回代求 x
            step8 = "步骤 8: 通过 x = y - b/(3a) 求得原方程的根"
            latex8 = f"x = y - \\frac{{b}}{{3a}} = y - {latex(simplify(b_a/3))}"
            print(f"\n{step8}")
            print(f"  x₁ = y₁ - {simplify(b_a/3)}")
            print(f"  x₂ = y₂ - {simplify(b_a/3)}")
            print(f"  x₃ = y₃ - {simplify(b_a/3)}")
            steps.append(step8)
            latex_steps.append(latex8)
        
        # 使用 sympy 直接求解（保证精确解）
        equation = a*x**3 + b*x**2 + c*x + d
        roots = solve(equation, x)
        
        if verbose:
            # 步骤 9: 显示精确解
            step9 = "步骤 9: 精确符号解"
            print(f"\n{step9}")
            latex9 = ""
            for i, root in enumerate(roots, 1):
                print(f"  x{i} = {root}")
                latex9 += f"x_{i} = {latex(root)} \\\\ "
            latex_steps.append(latex9)
            
            # 步骤 10: 数值近似
            step10 = "步骤 10: 数值近似值"
            print(f"\n{step10}")
            for i, root in enumerate(roots, 1):
                print(f"  x{i} ≈ {sympy.N(root, 6)}")
            steps.append(step9)
            steps.append(step10)
            latex_steps.append("")
            
            print("="*70)
        
        solution = EquationSolution(
            equation_type="cubic",
            coefficients=[a, b, c, d],
            roots=roots,
            steps=steps,
            latex_steps=latex_steps,
            exact_form=True
        )
        
        # 如果指定了输出文件，导出 Markdown
        if output_file:
            MarkdownExporter.export_solution(solution, output_file)
        
        return solution
    
    @staticmethod
    def solve_quartic(a: Union[int, float, sympy.Basic],
                     b: Union[int, float, sympy.Basic],
                     c: Union[int, float, sympy.Basic],
                     d: Union[int, float, sympy.Basic],
                     e: Union[int, float, sympy.Basic],
                     verbose: bool = True,
                     output_file: str = None) -> EquationSolution:
        """
        求解四次方程 ax⁴ + bx³ + cx² + dx + e = 0
        使用费拉里方法，详细显示手推步骤
        """
        steps = []
        latex_steps = []
        
        # 转换为 sympy 符号
        a = sympy.sympify(a)
        b = sympy.sympify(b)
        c = sympy.sympify(c)
        d = sympy.sympify(d)
        e = sympy.sympify(e)
        
        if verbose:
            print("\n" + "="*70)
            print("四次方程求解：ax⁴ + bx³ + cx² + dx + e = 0（费拉里方法）")
            print("="*70)
            
            # 步骤 1: 写出方程
            step1 = "步骤 1: 写出标准形式的四次方程"
            latex1 = f"{{{a}}}x^4 + {{{b}}}x^3 + {{{c}}}x^2 + {{{d}}}x + {{{e}}} = 0"
            print(f"\n{step1}")
            print(f"  {a}x⁴ + {b}x³ + {c}x² + {d}x + {e} = 0")
            steps.append(step1)
            latex_steps.append(latex1)
            
            # 步骤 2: 确认系数
            step2 = "步骤 2: 确认系数"
            latex2 = f"a = {latex(a)}, \\quad b = {latex(b)}, \\quad c = {latex(c)}, \\quad d = {latex(d)}, \\quad e = {latex(e)}"
            print(f"\n{step2}")
            print(f"  a = {a}")
            print(f"  b = {b}")
            print(f"  c = {c}")
            print(f"  d = {d}")
            print(f"  e = {e}")
            steps.append(step2)
            latex_steps.append(latex2)
            
            # 步骤 3: 化为首一多项式
            step3 = "步骤 3: 两边除以首项系数，化为首一多项式"
            b_a = b/a
            c_a = c/a
            d_a = d/a
            e_a = e/a
            latex3 = f"x^4 + {latex(simplify(b_a))}x^3 + {latex(simplify(c_a))}x^2 + {latex(simplify(d_a))}x + {latex(simplify(e_a))} = 0"
            print(f"\n{step3}")
            print(f"  x⁴ + ({b}/{a})x³ + ({c}/{a})x² + ({d}/{a})x + ({e}/{a}) = 0")
            print(f"  x⁴ + {simplify(b_a)}x³ + {simplify(c_a)}x² + {simplify(d_a)}x + {simplify(e_a)} = 0")
            steps.append(step3)
            latex_steps.append(latex3)
            
            # 步骤 4: 消去三次项
            step4 = "步骤 4: 通过变量代换消去三次项"
            p = c_a - 3*b_a**2/8
            q = b_a**3/8 - b_a*c_a/2 + d_a
            r = -3*b_a**4/256 + b_a**2*c_a/16 - b_a*d_a/4 + e_a
            latex4 = f"\\text{{令 }} x = y - \\frac{{b}}{{4a}} = y - {latex(simplify(b_a/4))}"
            latex4 += f"\\\\ \\text{{得到：}} y^4 + py^2 + qy + r = 0"
            latex4 += f"\\\\ p = {latex(simplify(p))}, \\quad q = {latex(simplify(q))}, \\quad r = {latex(simplify(r))}"
            print(f"\n{step4}")
            print(f"  令 x = y - b/(4a)")
            print(f"  即 x = y - {simplify(b_a/4)}")
            print(f"  代入后得到简化形式：y⁴ + py² + qy + r = 0")
            print(f"  计算系数：")
            print(f"  p = {simplify(p)}")
            print(f"  q = {simplify(q)}")
            print(f"  r = {simplify(r)}")
            print(f"  简化方程：y⁴ + {simplify(p)}y² + {simplify(q)}y + {simplify(r)} = 0")
            steps.append(step4)
            latex_steps.append(latex4)
            
            # 步骤 5: 费拉里的关键思想
            step5 = "步骤 5: 费拉里方法的核心思想"
            latex5 = f"y^4 + {latex(simplify(p))}y^2 = -{latex(simplify(q))}y - {latex(simplify(r))}"
            latex5 += f"\\\\ \\text{{引入参数 }} m, \\text{{两边同时加上 }} 2my^2 + m^2"
            latex5 += f"\\\\ (y^2 + m)^2 = (2m - p)y^2 - qy + (m^2 - r)"
            print(f"\n{step5}")
            print(f"  将方程重写为：")
            print(f"  y⁴ + {simplify(p)}y² = -{simplify(q)}y - {simplify(r)}")
            print(f"  ")
            print(f"  引入参数 m，两边同时加上 2my² + m²：")
            print(f"  (y² + m)² = y⁴ + 2my² + m²")
            print(f"  ")
            print(f"  原方程变为：")
            print(f"  (y² + m)² = (2m - p)y² - qy + (m² - r)")
            steps.append(step5)
            latex_steps.append(latex5)
            
            # 步骤 6: 三次预解方程
            step6 = "步骤 6: 构造三次预解方程"
            A = 8
            B = -4*p
            C = -8*r
            D = 4*p*r - q**2
            latex6 = f"\\text{{判别式 }} \\Delta = q^2 - 4(2m - p)(m^2 - r) = 0"
            latex6 += f"\\\\ \\text{{展开得到：}} 8m^3 - 4pm^2 - 8rm + (4pr - q^2) = 0"
            latex6 += f"\\\\ A = {latex(A)}, \\quad B = {latex(simplify(B))}, \\quad C = {latex(simplify(C))}, \\quad D = {latex(simplify(D))}"
            print(f"\n{step6}")
            print(f"  为使右边成为完全平方式，其判别式必须为 0：")
            print(f"  Δ = q² - 4(2m - p)(m² - r) = 0")
            print(f"  ")
            print(f"  展开得到关于 m 的三次方程：")
            print(f"  8m³ - 4pm² - 8rm + (4pr - q²) = 0")
            print(f"  其中：")
            print(f"  A = 8")
            print(f"  B = -4p = {simplify(B)}")
            print(f"  C = -8r = {simplify(C)}")
            print(f"  D = 4pr - q² = {simplify(D)}")
            print(f"  ")
            print(f"  三次预解方程：{simplify(A)}m³ + {simplify(B)}m² + {simplify(C)}m + {simplify(D)} = 0")
            steps.append(step6)
            latex_steps.append(latex6)
            
            # 步骤 7: 求解三次预解方程
            step7 = "步骤 7: 求解三次预解方程得到一个根 m"
            print(f"\n{step7}")
            print(f"  使用卡尔达诺公式求解 m 的三次方程...")
            
            # 解三次预解方程
            m_equation = A*symbols('m')**3 + B*symbols('m')**2 + C*symbols('m') + D
            m_roots = solve(m_equation, symbols('m'))
            
            latex7 = ""
            if m_roots:
                m = m_roots[0]  # 取一个实根
                print(f"  求得 m 的一个根：m = {m}")
                print(f"  数值近似：m ≈ {sympy.N(m, 6)}")
                latex7 = f"m = {latex(m)} \\approx {latex(sympy.N(m, 6))}"
            else:
                m = symbols('m')
                print(f"  无法求得精确解，使用符号 m")
                latex7 = "m = \\text{符号}"
            steps.append(step7)
            latex_steps.append(latex7)
            
            # 步骤 8: 求解两个二次方程
            step8 = "步骤 8: 求解两个二次方程得到 y 的四个根"
            latex8 = f"(y^2 + m)^2 = \\left(\\sqrt{{2m-p}} \\cdot y - \\frac{{q}}{{2\\sqrt{{2m-p}}}}\\right)^2"
            latex8 += f"\\\\ \\text{{得到两个二次方程：}}"
            latex8 += f"\\\\ y^2 - \\sqrt{{2m-p}} \\cdot y + \\left(m + \\frac{{q}}{{2\\sqrt{{2m-p}}}}\\right) = 0"
            latex8 += f"\\\\ y^2 + \\sqrt{{2m-p}} \\cdot y + \\left(m - \\frac{{q}}{{2\\sqrt{{2m-p}}}}\\right) = 0"
            print(f"\n{step8}")
            print(f"  当右边为完全平方式时：")
            print(f"  (y² + m)² = (√(2m-p)·y - q/(2√(2m-p)))²")
            print(f"  ")
            print(f"  开方得到两个二次方程：")
            print(f"  y² + m = ±(√(2m-p)·y - q/(2√(2m-p)))")
            print(f"  ")
            print(f"  整理得：")
            print(f"  y² - √(2m-p)·y + (m + q/(2√(2m-p))) = 0")
            print(f"  y² + √(2m-p)·y + (m - q/(2√(2m-p))) = 0")
            steps.append(step8)
            latex_steps.append(latex8)
            
            # 步骤 9: 回代求 x
            step9 = "步骤 9: 通过 x = y - b/(4a) 求得原方程的根"
            latex9 = f"x = y - \\frac{{b}}{{4a}} = y - {latex(simplify(b_a/4))}"
            print(f"\n{step9}")
            print(f"  x = y - {simplify(b_a/4)}")
            steps.append(step9)
            latex_steps.append(latex9)
        
        # 使用 sympy 直接求解（保证精确解）
        equation = a*x**4 + b*x**3 + c*x**2 + d*x + e
        roots = solve(equation, x)
        
        if verbose:
            # 步骤 10: 显示精确解
            step10 = "步骤 10: 精确符号解"
            print(f"\n{step10}")
            latex10 = ""
            for i, root in enumerate(roots, 1):
                print(f"  x{i} = {root}")
                latex10 += f"x_{i} = {latex(root)} \\\\ "
            
            # 步骤 11: 数值近似
            step11 = "步骤 11: 数值近似值"
            print(f"\n{step11}")
            for i, root in enumerate(roots, 1):
                print(f"  x{i} ≈ {sympy.N(root, 6)}")
            steps.append(step10)
            steps.append(step11)
            latex_steps.append(latex10)
            latex_steps.append("")
            
            print("="*70)
        
        solution = EquationSolution(
            equation_type="quartic",
            coefficients=[a, b, c, d, e],
            roots=roots,
            steps=steps,
            latex_steps=latex_steps,
            exact_form=True
        )
        
        # 如果指定了输出文件，导出 Markdown
        if output_file:
            MarkdownExporter.export_solution(solution, output_file)
        
        return solution


# 为了向后兼容，保留旧的类名
EquationSolver = SymbolicSolver
