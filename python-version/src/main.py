#!/usr/bin/env python3
"""
方程求解器主程序
提供命令行界面，支持符号计算和详细的步骤显示
"""

import sys
from sympy import sympify, N
from equation_solver import SymbolicSolver


def parse_coefficient(input_str: str):
    """解析系数，支持数字和符号表达式"""
    try:
        # 使用 sympy 解析，支持整数、分数、符号等
        coeff = sympify(input_str.strip())
        return coeff
    except Exception as e:
        raise ValueError(f"无法解析系数 '{input_str}': {e}")


def print_verification(equation_type, coeffs, roots):
    """验证解的正确性"""
    print("\n" + "="*70)
    print("验证解的正确性")
    print("="*70)
    
    x = sympify('x')
    
    # 构建原方程
    if equation_type == "quadratic":
        a, b, c = coeffs
        equation = a*x**2 + b*x + c
    elif equation_type == "cubic":
        a, b, c, d = coeffs
        equation = a*x**3 + b*x**2 + c*x + d
    elif equation_type == "quartic":
        a, b, c, d, e = coeffs
        equation = a*x**4 + b*x**3 + c*x**2 + d*x + e
    
    for i, root in enumerate(roots, 1):
        # 代入验证
        result = equation.subs(x, root)
        result_simplified = result.simplify()
        result_numeric = N(result)
        
        print(f"\n验证 x{i} = {root}:")
        print(f"  代入原方程：{result_simplified}")
        print(f"  数值结果：≈ {result_numeric}")
        
        # 判断是否接近 0
        if abs(complex(result_numeric)) < 1e-10:
            print(f"  ✓ 验证通过（结果接近 0）")
        else:
            print(f"  ✗ 验证失败（结果不为 0）")
    
    print("\n" + "="*70)


def solve_quadratic_interactive():
    """交互式求解二次方程"""
    print("\n求解二次方程：ax² + bx + c = 0")
    print("-" * 50)
    
    try:
        a_str = input("请输入系数 a: ").strip()
        b_str = input("请输入系数 b: ").strip()
        c_str = input("请输入系数 c: ").strip()
        
        a = parse_coefficient(a_str)
        b = parse_coefficient(b_str)
        c = parse_coefficient(c_str)
        
        if a == 0:
            print("错误：系数 a 不能为 0（否则不是二次方程）")
            return
        
        # 求解
        solution = SymbolicSolver.solve_quadratic(a, b, c, verbose=True)
        
        # 验证
        print_verification("quadratic", [a, b, c], solution.roots)
        
    except Exception as e:
        print(f"错误：{e}")


def solve_cubic_interactive():
    """交互式求解三次方程"""
    print("\n求解三次方程：ax³ + bx² + cx + d = 0")
    print("-" * 50)
    
    try:
        a_str = input("请输入系数 a: ").strip()
        b_str = input("请输入系数 b: ").strip()
        c_str = input("请输入系数 c: ").strip()
        d_str = input("请输入系数 d: ").strip()
        
        a = parse_coefficient(a_str)
        b = parse_coefficient(b_str)
        c = parse_coefficient(c_str)
        d = parse_coefficient(d_str)
        
        if a == 0:
            print("错误：系数 a 不能为 0（否则不是三次方程）")
            return
        
        # 求解
        solution = SymbolicSolver.solve_cubic(a, b, c, d, verbose=True)
        
        # 验证
        print_verification("cubic", [a, b, c, d], solution.roots)
        
    except Exception as e:
        print(f"错误：{e}")


def solve_quartic_interactive():
    """交互式求解四次方程"""
    print("\n求解四次方程：ax⁴ + bx³ + cx² + dx + e = 0")
    print("-" * 50)
    
    try:
        a_str = input("请输入系数 a: ").strip()
        b_str = input("请输入系数 b: ").strip()
        c_str = input("请输入系数 c: ").strip()
        d_str = input("请输入系数 d: ").strip()
        e_str = input("请输入系数 e: ").strip()
        
        a = parse_coefficient(a_str)
        b = parse_coefficient(b_str)
        c = parse_coefficient(c_str)
        d = parse_coefficient(d_str)
        e = parse_coefficient(e_str)
        
        if a == 0:
            print("错误：系数 a 不能为 0（否则不是四次方程）")
            return
        
        # 求解
        solution = SymbolicSolver.solve_quartic(a, b, c, d, e, verbose=True)
        
        # 验证
        print_verification("quartic", [a, b, c, d, e], solution.roots)
        
    except Exception as e:
        print(f"错误：{e}")


def demo_examples():
    """演示示例"""
    print("\n" + "="*70)
    print("演示示例")
    print("="*70)
    
    # 示例 1: 二次方程
    print("\n\n【示例 1】二次方程：x² - 5x + 6 = 0")
    SymbolicSolver.solve_quadratic(1, -5, 6, verbose=True)
    
    # 示例 2: 二次方程（有复根）
    print("\n\n【示例 2】二次方程：x² + 2x + 5 = 0（有复根）")
    SymbolicSolver.solve_quadratic(1, 2, 5, verbose=True)
    
    # 示例 3: 三次方程
    print("\n\n【示例 3】三次方程：x³ - 6x² + 11x - 6 = 0")
    SymbolicSolver.solve_cubic(1, -6, 11, -6, verbose=True)
    
    # 示例 4: 四次方程
    print("\n\n【示例 4】四次方程：x⁴ - 5x² + 4 = 0（双二次方程）")
    SymbolicSolver.solve_quartic(1, 0, -5, 0, 4, verbose=True)


def main():
    """主函数"""
    print("="*70)
    print(" " * 20 + "方程求解器")
    print(" " * 15 + "使用 SymPy 进行符号计算")
    print("="*70)
    print()
    print("本程序可以求解二次、三次和四次方程，并显示详细的手推步骤。")
    print("系数支持整数、分数（如 1/2）、小数和符号表达式。")
    print()
    
    while True:
        print("\n请选择操作:")
        print("1. 求解二次方程 (ax² + bx + c = 0)")
        print("2. 求解三次方程 (ax³ + bx² + cx + d = 0)")
        print("3. 求解四次方程 (ax⁴ + bx³ + cx² + dx + e = 0)")
        print("4. 查看演示示例")
        print("5. 退出")
        
        choice = input("\n请输入您的选择 (1-5): ").strip()
        
        if choice == '5':
            print("\n再见！")
            break
        
        if choice == '4':
            demo_examples()
            continue
        
        if choice not in ['1', '2', '3']:
            print("无效选择。请输入 1, 2, 3, 4 或 5。")
            continue
        
        try:
            if choice == '1':
                solve_quadratic_interactive()
            elif choice == '2':
                solve_cubic_interactive()
            elif choice == '3':
                solve_quartic_interactive()
        except KeyboardInterrupt:
            print("\n\n操作已取消。")
        except Exception as e:
            print(f"\n发生错误：{e}")
        
        print("\n" + "-"*70)


if __name__ == "__main__":
    main()
