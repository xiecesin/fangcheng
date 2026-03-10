#!/usr/bin/env python3
"""
Test script to verify symbolic solutions for cubic and quartic equations.
"""

import sys
import os
sys.path.append(os.path.abspath('src'))

from equation_solver import QuadraticSolver, CubicSolver, QuarticSolver, EquationSolution


def test_cubic_symbolic_solution():
    """Test cubic solver with symbolic solution."""
    print("\n=== 测试三次方程符号解 ===")
    
    # Test case 1: x³ - 6x² + 11x - 6 = 0 (roots: 1, 2, 3)
    print("\n1. 测试方程: x³ - 6x² + 11x - 6 = 0")
    solver = CubicSolver(1, -6, 11, -6)
    solution = solver.solve()
    
    print("解:")
    for i, root in enumerate(solution.roots):
        print(f"x{i+1} = {root}")
    
    # Test case 2: x³ + 2x² + 3x + 4 = 0 (one real root, two complex)
    print("\n2. 测试方程: x³ + 2x² + 3x + 4 = 0")
    solver = CubicSolver(1, 2, 3, 4)
    solution = solver.solve()
    
    print("解:")
    for i, root in enumerate(solution.roots):
        print(f"x{i+1} = {root}")


def test_quartic_symbolic_solution():
    """Test quartic solver with symbolic solution."""
    print("\n=== 测试四次方程符号解 ===")
    
    # Test case 1: x⁴ - 10x³ + 35x² - 50x + 24 = 0 (roots: 1, 2, 3, 4)
    print("\n1. 测试方程: x⁴ - 10x³ + 35x² - 50x + 24 = 0")
    solver = QuarticSolver(1, -10, 35, -50, 24)
    solution = solver.solve()
    
    print("解:")
    for i, root in enumerate(solution.roots):
        print(f"x{i+1} = {root}")
    
    # Test case 2: x⁴ + 1 = 0 (biquadratic equation)
    print("\n2. 测试方程: x⁴ + 1 = 0")
    solver = QuarticSolver(1, 0, 0, 0, 1)
    solution = solver.solve()
    
    print("解:")
    for i, root in enumerate(solution.roots):
        print(f"x{i+1} = {root}")


if __name__ == "__main__":
    print("方程求解器符号解测试")
    print("=" * 50)
    
    try:
        test_cubic_symbolic_solution()
        test_quartic_symbolic_solution()
        print("\n=== 所有测试完成 ===")
    except Exception as e:
        print(f"\n测试失败: {e}")
        import traceback
        traceback.print_exc()
