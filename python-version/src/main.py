#!/usr/bin/env python3
"""
Main program for the Equation Solver.
Provides a command-line interface for solving quadratic, cubic, and quartic equations.
"""

import sys
from typing import List, Union
from equation_solver import EquationSolver, EquationSolution, ComplexNumber
from verifier import SolutionVerifier, VerificationResult


def parse_coefficients(input_str: str) -> List[float]:
    """Parse coefficient string into list of floats."""
    try:
        coeffs = [float(x.strip()) for x in input_str.split(',')]
        return coeffs
    except ValueError as e:
        raise ValueError(f"Invalid coefficient format: {e}")


def main():
    """Main program entry point."""
    print("方程求解器")
    print("=" * 40)
    print("求解二次、三次和四次方程，并显示详细步骤")
    print()

    while True:
        print("选择方程类型:")
        print("1. 二次方程 (ax² + bx + c = 0)")
        print("2. 三次方程 (ax³ + bx² + cx + d = 0)")
        print("3. 四次方程 (ax⁴ + bx³ + cx² + dx + e = 0)")
        print("4. 退出")

        choice = input("\n请输入您的选择 (1-4): ").strip()

        if choice == '4':
            print("再见!")
            break

        if choice not in ['1', '2', '3']:
            print("无效选择。请输入 1, 2, 3 或 4。")
            continue

        try:
            if choice == '1':
                coeffs_input = input("请输入系数 a, b, c (用逗号分隔): ")
                coeffs = parse_coefficients(coeffs_input)
                if len(coeffs) != 3:
                    raise ValueError("二次方程需要恰好 3 个系数")
                a, b, c = coeffs
                solution = EquationSolver.solve_quadratic(a, b, c)
                verifier = SolutionVerifier()
                verification_results = verifier.verify_quadratic(a, b, c, solution.roots)

            elif choice == '2':
                coeffs_input = input("请输入系数 a, b, c, d (用逗号分隔): ")
                coeffs = parse_coefficients(coeffs_input)
                if len(coeffs) != 4:
                    raise ValueError("三次方程需要恰好 4 个系数")
                a, b, c, d = coeffs
                solution = EquationSolver.solve_cubic(a, b, c, d)
                verifier = SolutionVerifier()
                verification_results = verifier.verify_cubic(a, b, c, d, solution.roots)

            elif choice == '3':
                coeffs_input = input("请输入系数 a, b, c, d, e (用逗号分隔): ")
                coeffs = parse_coefficients(coeffs_input)
                if len(coeffs) != 5:
                    raise ValueError("四次方程需要恰好 5 个系数")
                a, b, c, d, e = coeffs
                solution = EquationSolver.solve_quartic(a, b, c, d, e)
                verifier = SolutionVerifier()
                verification_results = verifier.verify_quartic(a, b, c, d, e, solution.roots)

            # Display solution
            EquationSolver.print_solution(solution)

            # Display verification
            verifier.print_verification_results(verification_results)

        except ValueError as e:
            print(f"输入错误: {e}")
        except Exception as e:
            print(f"解方程时出错: {e}")

        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()