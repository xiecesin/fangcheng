#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
四次方程双二次情况的符号解测试
测试方程: x⁴ - 10x³ + 35x² - 50x + 24 = 0
这个方程有四个实根: 1, 2, 3, 4
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from src.equation_solver import QuarticSolver, EquationSolution

def test_quartic_biquadratic():
    """测试四次方程双二次情况的符号解"""
    print("=== 四次方程双二次情况符号解测试 ===")
    print("测试方程: x⁴ - 10x³ + 35x² - 50x + 24 = 0")
    print("预期根: 1.0, 2.0, 3.0, 4.0")
    print()
    
    # 初始化四次方程求解器
    solver = QuarticSolver(1.0, -10.0, 35.0, -50.0, 24.0)
    
    # 求解方程
    solution = solver.solve()
    
    # 打印求解步骤
    print("求解步骤:")
    print()
    for step in solution.steps:
        print(f"{step.description}:")
        print(f"  公式: {step.formula}")
        print(f"  结果: {step.result}")
        print()
    
    # 打印最终根
    print("最终根:")
    for i, root in enumerate(solution.roots, 1):
        print(f"x{i} = {root}")

if __name__ == "__main__":
    test_quartic_biquadratic()
