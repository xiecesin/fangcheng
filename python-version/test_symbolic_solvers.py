#!/usr/bin/env python3
"""
测试脚本 - 演示方程求解器的功能
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from equation_solver import SymbolicSolver

def test_quadratic_examples():
    """测试二次方程示例"""
    print("\n" + "="*80)
    print(" " * 30 + "二次方程测试")
    print("="*80)
    
    # 示例 1: 两个实根
    print("\n【测试 1】x² - 5x + 6 = 0")
    SymbolicSolver.solve_quadratic(1, -5, 6)
    
    # 示例 2: 复根
    print("\n【测试 2】x² + 2x + 5 = 0")
    SymbolicSolver.solve_quadratic(1, 2, 5)
    
    # 示例 3: 重根
    print("\n【测试 3】x² - 4x + 4 = 0")
    SymbolicSolver.solve_quadratic(1, -4, 4)
    
    # 示例 4: 分数系数
    print("\n【测试 4】(1/2)x² + 3x + 4 = 0")
    SymbolicSolver.solve_quadratic(1/2, 3, 4)


def test_cubic_examples():
    """测试三次方程示例"""
    print("\n" + "="*80)
    print(" " * 30 + "三次方程测试")
    print("="*80)
    
    # 示例 1: 三个实根
    print("\n【测试 1】x³ - 6x² + 11x - 6 = 0")
    SymbolicSolver.solve_cubic(1, -6, 11, -6)
    
    # 示例 2: 一个实根两个复根
    print("\n【测试 2】x³ - 1 = 0")
    SymbolicSolver.solve_cubic(1, 0, 0, -1)
    
    # 示例 3: 有重根
    print("\n【测试 3】x³ - 3x² + 3x - 1 = 0")
    SymbolicSolver.solve_cubic(1, -3, 3, -1)


def test_quartic_examples():
    """测试四次方程示例"""
    print("\n" + "="*80)
    print(" " * 30 + "四次方程测试")
    print("="*80)
    
    # 示例 1: 双二次方程
    print("\n【测试 1】x⁴ - 5x² + 4 = 0")
    SymbolicSolver.solve_quartic(1, 0, -5, 0, 4)
    
    # 示例 2: 四个实根
    print("\n【测试 2】x⁴ - 10x³ + 35x² - 50x + 24 = 0")
    SymbolicSolver.solve_quartic(1, -10, 35, -50, 24)
    
    # 示例 3: 简单的四次方程
    print("\n【测试 3】x⁴ - 1 = 0")
    SymbolicSolver.solve_quartic(1, 0, 0, 0, -1)


if __name__ == "__main__":
    print("\n" + "="*80)
    print(" " * 25 + "方程求解器测试套件")
    print(" " * 20 + "使用 SymPy 进行符号计算和详细步骤显示")
    print("="*80)
    
    test_quadratic_examples()
    test_cubic_examples()
    test_quartic_examples()
    
    print("\n" + "="*80)
    print(" " * 35 + "测试完成!")
    print("="*80 + "\n")
