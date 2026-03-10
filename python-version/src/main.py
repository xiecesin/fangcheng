#!/usr/bin/env python3
"""
方程求解器主程序
提供命令行界面，支持符号计算和详细的步骤显示
支持一次性输入系数，自动保存求解过程到 Markdown 文件
"""

import sys
import re
import os
from sympy import sympify, N
from equation_solver import SymbolicSolver, MarkdownExporter
from datetime import datetime


def parse_coefficients(input_str: str):
    """
    解析系数，支持数字和符号表达式
    支持中英文逗号和空格分隔
    """
    try:
        # 替换中文逗号为英文逗号
        input_str = input_str.replace(',', ',')
        # 用逗号或空格分割
        parts = re.split(r'[,\s]+', input_str.strip())
        # 过滤空字符串并解析
        coeffs = []
        for part in parts:
            part = part.strip()
            if part:
                # 再次确保没有中文逗号
                part = part.replace(',', ',')
                coeffs.append(sympify(part))
        return coeffs
    except Exception as e:
        raise ValueError(f"无法解析系数 '{input_str}': {e}")


def generate_output_filename(equation_type: str, coeffs: list) -> str:
    """生成输出文件名"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # 创建输出目录
    output_dir = "solutions"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 根据方程类型生成文件名
    if equation_type == "quadratic":
        eq_type = "quadratic"
    elif equation_type == "cubic":
        eq_type = "cubic"
    elif equation_type == "quartic":
        eq_type = "quartic"
    else:
        eq_type = "equation"
    
    # 生成文件名
    filename = f"{output_dir}/{eq_type}_{timestamp}.md"
    return filename


def print_verification(equation_type, coeffs, roots):
    """验证解的正确性"""
    print("\n" + "="*70)
    print("验证解的正确性")
    print("="*70)

    # 将系数转换为数值
    coeffs_numeric = [float(N(c)) for c in coeffs]

    for i, root in enumerate(roots, 1):
        # 将根转换为高精度数值
        root_numeric = complex(N(root, 50))

        # 使用霍纳法（Horner's method）计算多项式的值
        # 这种方法比直接代入更稳定
        if equation_type == "quadratic":
            a, b, c = coeffs_numeric
            # P(x) = ax² + bx + c
            result = a * root_numeric**2 + b * root_numeric + c
        elif equation_type == "cubic":
            a, b, c, d = coeffs_numeric
            # P(x) = ax³ + bx² + cx + d
            result = a * root_numeric**3 + b * root_numeric**2 + c * root_numeric + d
        elif equation_type == "quartic":
            a, b, c, d, e = coeffs_numeric
            # P(x) = ax⁴ + bx³ + cx² + dx + e
            result = a * root_numeric**4 + b * root_numeric**3 + c * root_numeric**2 + d * root_numeric + e

        print(f"\n验证 x{i}:")
        print(f"  根值: {root_numeric}")
        print(f"  代入结果: {result}")

        # 判断是否接近 0
        if abs(result) < 1e-6:
            print(f"  ✓ 验证通过")
        else:
            print(f"  ✗ 验证失败（结果不为 0）")

    print("\n" + "="*70)


def solve_quadratic_interactive():
    """交互式求解二次方程"""
    print("\n求解二次方程：ax² + bx + c = 0")
    print("-" * 50)
    print("请输入系数 a, b, c（可以用中文逗号、英文逗号或空格分隔）")
    
    try:
        coeffs_input = input("系数：").strip()
        coeffs = parse_coefficients(coeffs_input)
        
        if len(coeffs) != 3:
            print(f"错误：二次方程需要恰好 3 个系数，您输入了 {len(coeffs)} 个")
            return
        
        a, b, c = coeffs
        
        if a == 0:
            print("错误：系数 a 不能为 0（否则不是二次方程）")
            return
        
        # 生成输出文件名
        output_file = generate_output_filename("quadratic", coeffs)
        
        # 求解
        solution = SymbolicSolver.solve_quadratic(a, b, c, verbose=True, output_file=output_file)
        
        # 验证
        print_verification("quadratic", [a, b, c], solution.roots)
        
    except Exception as e:
        print(f"错误：{e}")


def solve_cubic_interactive():
    """交互式求解三次方程"""
    print("\n求解三次方程：ax³ + bx² + cx + d = 0")
    print("-" * 50)
    print("请输入系数 a, b, c, d（可以用中文逗号、英文逗号或空格分隔）")
    
    try:
        coeffs_input = input("系数：").strip()
        coeffs = parse_coefficients(coeffs_input)
        
        if len(coeffs) != 4:
            print(f"错误：三次方程需要恰好 4 个系数，您输入了 {len(coeffs)} 个")
            return
        
        a, b, c, d = coeffs
        
        if a == 0:
            print("错误：系数 a 不能为 0（否则不是三次方程）")
            return
        
        # 生成输出文件名
        output_file = generate_output_filename("cubic", coeffs)
        
        # 求解
        solution = SymbolicSolver.solve_cubic(a, b, c, d, verbose=True, output_file=output_file)
        
        # 验证
        print_verification("cubic", [a, b, c, d], solution.roots)
        
    except Exception as e:
        print(f"错误：{e}")


def solve_quartic_interactive():
    """交互式求解四次方程"""
    print("\n求解四次方程：ax⁴ + bx³ + cx² + dx + e = 0")
    print("-" * 50)
    print("请输入系数 a, b, c, d, e（可以用中文逗号、英文逗号或空格分隔）")
    
    try:
        coeffs_input = input("系数：").strip()
        coeffs = parse_coefficients(coeffs_input)
        
        if len(coeffs) != 5:
            print(f"错误：四次方程需要恰好 5 个系数，您输入了 {len(coeffs)} 个")
            return
        
        a, b, c, d, e = coeffs
        
        if a == 0:
            print("错误：系数 a 不能为 0（否则不是四次方程）")
            return
        
        # 生成输出文件名
        output_file = generate_output_filename("quartic", coeffs)
        
        # 求解
        solution = SymbolicSolver.solve_quartic(a, b, c, d, e, verbose=True, output_file=output_file)
        
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
    output_file = "solutions/demo_quadratic.md"
    SymbolicSolver.solve_quadratic(1, -5, 6, verbose=True, output_file=output_file)
    
    # 示例 2: 二次方程（有复根）
    print("\n\n【示例 2】二次方程：x² + 2x + 5 = 0（有复根）")
    output_file = "solutions/demo_quadratic_complex.md"
    SymbolicSolver.solve_quadratic(1, 2, 5, verbose=True, output_file=output_file)
    
    # 示例 3: 三次方程
    print("\n\n【示例 3】三次方程：x³ - 6x² + 11x - 6 = 0")
    output_file = "solutions/demo_cubic.md"
    SymbolicSolver.solve_cubic(1, -6, 11, -6, verbose=True, output_file=output_file)
    
    # 示例 4: 四次方程
    print("\n\n【示例 4】四次方程：x⁴ - 5x² + 4 = 0（双二次方程）")
    output_file = "solutions/demo_quartic.md"
    SymbolicSolver.solve_quartic(1, 0, -5, 0, 4, verbose=True, output_file=output_file)


def main():
    """主函数"""
    print("="*70)
    print(" " * 20 + "方程求解器")
    print(" " * 15 + "使用 SymPy 进行符号计算")
    print("="*70)
    print()
    print("本程序可以求解二次、三次和四次方程，并显示详细的手推步骤。")
    print("系数支持整数、分数（如 1/2）、小数和符号表达式。")
    print("输入系数时可以用中文逗号、英文逗号或空格分隔。")
    print("求解过程会自动保存到 solutions/ 目录下的 Markdown 文件中。")
    print()
    
    # 确保输出目录存在
    if not os.path.exists("solutions"):
        os.makedirs("solutions")
    
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
