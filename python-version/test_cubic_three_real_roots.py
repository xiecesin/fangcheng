#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
三次方程三个实根情况的符号解测试
测试方程: x³ - 6x² + 11x - 6 = 0
这个方程有三个实根: 1, 2, 3
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from src.equation_solver import CubicSolver, EquationSolution

def test_cubic_three_real_roots():
    """测试三次方程三个实根情况的符号解"""
    print("=== 三次方程三个实根情况符号解测试 ===")
    print("测试方程: x³ - 6x² + 11x - 6 = 0")
    print("预期根: 1.0, 2.0, 3.0")
    print()
    
    # 初始化三次方程求解器
    solver = CubicSolver(1.0, -6.0, 11.0, -6.0)
    
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
    test_cubic_three_real_roots()
