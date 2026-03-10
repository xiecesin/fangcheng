"""
方程求解器模块
使用 sympy 库求解二次、三次和四次方程，提供详细的分步解决方案
"""

from sympy import symbols, solve, sqrt, cbrt, I, pi, simplify, expand, factor, Rational, pprint, latex
from sympy.abc import x
from typing import List, Union, Optional, Tuple
from dataclasses import dataclass
import sympy


@dataclass
class EquationSolution:
    """存储方程的解和详细信息"""
    equation_type: str
    coefficients: List[Union[int, float, sympy.Basic]]
    roots: List[sympy.Basic]
    steps: List[str]
    exact_form: bool = True


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
                       verbose: bool = True) -> EquationSolution:
        """
        求解二次方程 ax² + bx + c = 0
        详细显示求根公式的推导过程
        """
        steps = []
        
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
            print(f"\n{step1}")
            print(f"  {a}x² + {b}x + {c} = 0")
            steps.append(step1)
            
            # 步骤 2: 确认系数
            step2 = f"步骤 2: 确认系数"
            print(f"\n{step2}")
            print(f"  a = {a}")
            print(f"  b = {b}")
            print(f"  c = {c}")
            steps.append(step2)
            
            # 步骤 3: 计算判别式
            step3 = f"步骤 3: 计算判别式 Δ = b² - 4ac"
            print(f"\n{step3}")
            delta_expr = b**2 - 4*a*c
            print(f"  Δ = ({b})² - 4×({a})×({c})")
            print(f"  Δ = {b**2} - {4*a*c}")
            print(f"  Δ = {simplify(delta_expr)}")
            steps.append(step3)
            
            # 步骤 4: 判断根的情况
            step4 = f"步骤 4: 根据判别式判断根的情况"
            print(f"\n{step4}")
            delta_val = sympy.N(delta_expr)
            if delta_val.is_real:
                if delta_val > 0:
                    print(f"  Δ = {simplify(delta_expr)} > 0，方程有两个不相等的实根")
                elif delta_val == 0:
                    print(f"  Δ = {simplify(delta_expr)} = 0，方程有两个相等的实根（重根）")
                else:
                    print(f"  Δ = {simplify(delta_expr)} < 0，方程有一对共轭复根")
            else:
                print(f"  Δ = {simplify(delta_expr)}")
            steps.append(step4)
            
            # 步骤 5: 应用求根公式
            step5 = f"步骤 5: 应用求根公式"
            print(f"\n{step5}")
            print(f"  求根公式：x = (-b ± √Δ) / (2a)")
            print(f"  代入系数：")
            print(f"  x = (-({b}) ± √({simplify(delta_expr)})) / (2×{a})")
            print(f"  x = ({-b} ± √({simplify(delta_expr)})) / ({2*a})")
            steps.append(step5)
            
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
            
            # 步骤 7: 数值近似（如果有符号表达式）
            step7 = f"步骤 7: 数值近似值"
            print(f"\n{step7}")
            print(f"  x₁ ≈ {sympy.N(x1_simplified, 6)}")
            print(f"  x₂ ≈ {sympy.N(x2_simplified, 6)}")
            steps.append(step7)
            
            print("="*70)
        
        roots = [x1_simplified, x2_simplified]
        return EquationSolution(
            equation_type="quadratic",
            coefficients=[a, b, c],
            roots=roots,
            steps=steps,
            exact_form=True
        )
    
    @staticmethod
    def solve_cubic(a: Union[int, float, sympy.Basic],
                   b: Union[int, float, sympy.Basic],
                   c: Union[int, float, sympy.Basic],
                   d: Union[int, float, sympy.Basic],
                   verbose: bool = True) -> EquationSolution:
        """
        求解三次方程 ax³ + bx² + cx + d = 0
        使用卡尔达诺公式，详细显示手推步骤
        """
        steps = []
        
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
            print(f"\n{step1}")
            print(f"  {a}x³ + {b}x² + {c}x + {d} = 0")
            steps.append(step1)
            
            # 步骤 2: 确认系数
            step2 = "步骤 2: 确认系数"
            print(f"\n{step2}")
            print(f"  a = {a}")
            print(f"  b = {b}")
            print(f"  c = {c}")
            print(f"  d = {d}")
            steps.append(step2)
            
            # 步骤 3: 化为首一多项式
            step3 = "步骤 3: 两边除以首项系数，化为首一多项式"
            print(f"\n{step3}")
            print(f"  x³ + ({b}/{a})x² + ({c}/{a})x + ({d}/{a}) = 0")
            b_a = b/a
            c_a = c/a
            d_a = d/a
            print(f"  x³ + {simplify(b_a)}x² + {simplify(c_a)}x + {simplify(d_a)} = 0")
            steps.append(step3)
            
            # 步骤 4: 消去二次项
            step4 = "步骤 4: 通过变量代换消去二次项"
            print(f"\n{step4}")
            print(f"  令 x = y - b/(3a)")
            p = c_a - b_a**2/3
            q = 2*b_a**3/27 - b_a*c_a/3 + d_a
            print(f"  计算 p 和 q：")
            print(f"  p = c/a - b²/(3a²) = {simplify(c_a)} - {simplify(b_a**2/3)} = {simplify(p)}")
            print(f"  q = 2b³/(27a³) - bc/(3a²) + d/a")
            print(f"    = {simplify(2*b_a**3/27)} - {simplify(b_a*c_a/3)} + {simplify(d_a)}")
            print(f"    = {simplify(q)}")
            print(f"  得到简化形式：y³ + py + q = 0")
            print(f"  即：y³ + {simplify(p)}y + {simplify(q)} = 0")
            steps.append(step4)
            
            # 步骤 5: 计算判别式
            step5 = "步骤 5: 计算判别式"
            print(f"\n{step5}")
            discriminant = (q/2)**2 + (p/3)**3
            print(f"  Δ = (q/2)² + (p/3)³")
            print(f"  Δ = ({simplify(q)}/2)² + ({simplify(p)}/3)³")
            print(f"  Δ = ({simplify(q/2)})² + ({simplify(p/3)})³")
            print(f"  Δ = {simplify((q/2)**2)} + {simplify((p/3)**3)}")
            print(f"  Δ = {simplify(discriminant)}")
            
            disc_val = sympy.N(discriminant)
            if disc_val.is_real:
                if disc_val > 0:
                    print(f"  Δ > 0，方程有一个实根和两个共轭复根")
                elif disc_val == 0:
                    print(f"  Δ = 0，方程有三个实根（至少两个相等）")
                else:
                    print(f"  Δ < 0，方程有三个不相等的实根（需要用三角函数表示）")
            steps.append(step5)
            
            # 步骤 6: 应用卡尔达诺公式
            step6 = "步骤 6: 应用卡尔达诺公式求解 y"
            print(f"\n{step6}")
            print(f"  卡尔达诺公式：")
            print(f"  y = ∛(-q/2 + √Δ) + ∛(-q/2 - √Δ)")
            print(f"  ")
            print(f"  计算 u = ∛(-q/2 + √Δ)：")
            print(f"  u = ∛(-{simplify(q)}/2 + √({simplify(discriminant)}))")
            print(f"  u = ∛({simplify(-q/2)} + {simplify(sqrt(discriminant))})")
            print(f"  ")
            print(f"  计算 v = ∛(-q/2 - √Δ)：")
            print(f"  v = ∛(-{simplify(q)}/2 - √({simplify(discriminant)}))")
            print(f"  v = ∛({simplify(-q/2)} - {simplify(sqrt(discriminant))})")
            steps.append(step6)
            
            # 步骤 7: 计算 y 的三个根
            step7 = "步骤 7: 计算 y 的三个根"
            print(f"\n{step7}")
            print(f"  令 ω = (-1 + √3·i)/2 为三次单位根")
            print(f"  y₁ = u + v")
            print(f"  y₂ = ωu + ω²v")
            print(f"  y₃ = ω²u + ωv")
            steps.append(step7)
            
            # 步骤 8: 回代求 x
            step8 = "步骤 8: 通过 x = y - b/(3a) 求得原方程的根"
            print(f"\n{step8}")
            print(f"  x₁ = y₁ - {simplify(b_a/3)}")
            print(f"  x₂ = y₂ - {simplify(b_a/3)}")
            print(f"  x₃ = y₃ - {simplify(b_a/3)}")
            steps.append(step8)
        
        # 使用 sympy 直接求解（保证精确解）
        equation = a*x**3 + b*x**2 + c*x + d
        roots = solve(equation, x)
        
        if verbose:
            # 步骤 9: 显示精确解
            step9 = "步骤 9: 精确符号解"
            print(f"\n{step9}")
            for i, root in enumerate(roots, 1):
                print(f"  x{i} = {root}")
            
            # 步骤 10: 数值近似
            step10 = "步骤 10: 数值近似值"
            print(f"\n{step10}")
            for i, root in enumerate(roots, 1):
                print(f"  x{i} ≈ {sympy.N(root, 6)}")
            steps.append(step9)
            steps.append(step10)
            
            print("="*70)
        
        return EquationSolution(
            equation_type="cubic",
            coefficients=[a, b, c, d],
            roots=roots,
            steps=steps,
            exact_form=True
        )
    
    @staticmethod
    def solve_quartic(a: Union[int, float, sympy.Basic],
                     b: Union[int, float, sympy.Basic],
                     c: Union[int, float, sympy.Basic],
                     d: Union[int, float, sympy.Basic],
                     e: Union[int, float, sympy.Basic],
                     verbose: bool = True) -> EquationSolution:
        """
        求解四次方程 ax⁴ + bx³ + cx² + dx + e = 0
        使用费拉里方法，详细显示手推步骤
        """
        steps = []
        
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
            print(f"\n{step1}")
            print(f"  {a}x⁴ + {b}x³ + {c}x² + {d}x + {e} = 0")
            steps.append(step1)
            
            # 步骤 2: 确认系数
            step2 = "步骤 2: 确认系数"
            print(f"\n{step2}")
            print(f"  a = {a}")
            print(f"  b = {b}")
            print(f"  c = {c}")
            print(f"  d = {d}")
            print(f"  e = {e}")
            steps.append(step2)
            
            # 步骤 3: 化为首一多项式
            step3 = "步骤 3: 两边除以首项系数，化为首一多项式"
            print(f"\n{step3}")
            print(f"  x⁴ + ({b}/{a})x³ + ({c}/{a})x² + ({d}/{a})x + ({e}/{a}) = 0")
            b_a = b/a
            c_a = c/a
            d_a = d/a
            e_a = e/a
            print(f"  x⁴ + {simplify(b_a)}x³ + {simplify(c_a)}x² + {simplify(d_a)}x + {simplify(e_a)} = 0")
            steps.append(step3)
            
            # 步骤 4: 消去三次项
            step4 = "步骤 4: 通过变量代换消去三次项"
            print(f"\n{step4}")
            print(f"  令 x = y - b/(4a)")
            print(f"  即 x = y - {simplify(b_a/4)}")
            
            # 计算简化后的系数
            p = c_a - 3*b_a**2/8
            q = b_a**3/8 - b_a*c_a/2 + d_a
            r = -3*b_a**4/256 + b_a**2*c_a/16 - b_a*d_a/4 + e_a
            
            print(f"  代入后得到简化形式：y⁴ + py² + qy + r = 0")
            print(f"  计算系数：")
            print(f"  p = c/a - 3b²/(8a²)")
            print(f"    = {simplify(c_a)} - {simplify(3*b_a**2/8)}")
            print(f"    = {simplify(p)}")
            print(f"  q = b³/(8a³) - bc/(2a²) + d/a")
            print(f"    = {simplify(b_a**3/8)} - {simplify(b_a*c_a/2)} + {simplify(d_a)}")
            print(f"    = {simplify(q)}")
            print(f"  r = -3b⁴/(256a⁴) + b²c/(16a²) - bd/(4a) + e/a")
            print(f"    = {simplify(-3*b_a**4/256)} + {simplify(b_a**2*c_a/16)} - {simplify(b_a*d_a/4)} + {simplify(e_a)}")
            print(f"    = {simplify(r)}")
            print(f"  简化方程：y⁴ + {simplify(p)}y² + {simplify(q)}y + {simplify(r)} = 0")
            steps.append(step4)
            
            # 步骤 5: 费拉里的关键思想
            step5 = "步骤 5: 费拉里方法的核心思想"
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
            
            # 步骤 6: 三次预解方程
            step6 = "步骤 6: 构造三次预解方程"
            print(f"\n{step6}")
            print(f"  为使右边成为完全平方式，其判别式必须为 0：")
            print(f"  Δ = q² - 4(2m - p)(m² - r) = 0")
            print(f"  ")
            print(f"  展开得到关于 m 的三次方程：")
            print(f"  8m³ - 4pm² - 8rm + (4pr - q²) = 0")
            
            # 计算三次预解方程的系数
            A = 8
            B = -4*p
            C = -8*r
            D = 4*p*r - q**2
            
            print(f"  其中：")
            print(f"  A = 8")
            print(f"  B = -4p = {simplify(B)}")
            print(f"  C = -8r = {simplify(C)}")
            print(f"  D = 4pr - q² = {simplify(D)}")
            print(f"  ")
            print(f"  三次预解方程：{simplify(A)}m³ + {simplify(B)}m² + {simplify(C)}m + {simplify(D)} = 0")
            steps.append(step6)
            
            # 步骤 7: 求解三次预解方程
            step7 = "步骤 7: 求解三次预解方程得到一个根 m"
            print(f"\n{step7}")
            print(f"  使用卡尔达诺公式求解 m 的三次方程...")
            
            # 解三次预解方程
            m_equation = A*symbols('m')**3 + B*symbols('m')**2 + C*symbols('m') + D
            m_roots = solve(m_equation, symbols('m'))
            
            if m_roots:
                m = m_roots[0]  # 取一个实根
                print(f"  求得 m 的一个根：m = {m}")
                print(f"  数值近似：m ≈ {sympy.N(m, 6)}")
            else:
                m = symbols('m')
                print(f"  无法求得精确解，使用符号 m")
            steps.append(step7)
            
            # 步骤 8: 求解两个二次方程
            step8 = "步骤 8: 求解两个二次方程得到 y 的四个根"
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
            
            # 步骤 9: 回代求 x
            step9 = "步骤 9: 通过 x = y - b/(4a) 求得原方程的根"
            print(f"\n{step9}")
            print(f"  x = y - {simplify(b_a/4)}")
            steps.append(step9)
        
        # 使用 sympy 直接求解（保证精确解）
        equation = a*x**4 + b*x**3 + c*x**2 + d*x + e
        roots = solve(equation, x)
        
        if verbose:
            # 步骤 10: 显示精确解
            step10 = "步骤 10: 精确符号解"
            print(f"\n{step10}")
            for i, root in enumerate(roots, 1):
                print(f"  x{i} = {root}")
            
            # 步骤 11: 数值近似
            step11 = "步骤 11: 数值近似值"
            print(f"\n{step11}")
            for i, root in enumerate(roots, 1):
                print(f"  x{i} ≈ {sympy.N(root, 6)}")
            steps.append(step10)
            steps.append(step11)
            
            print("="*70)
        
        return EquationSolution(
            equation_type="quartic",
            coefficients=[a, b, c, d, e],
            roots=roots,
            steps=steps,
            exact_form=True
        )


# 为了向后兼容，保留旧的类名
EquationSolver = SymbolicSolver
