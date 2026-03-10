#!/usr/bin/env python3
"""
Main program for the Equation Solver.
Provides a command-line interface for solving quadratic, cubic, and quartic equations.
"""

import sys
from typing import List, Union
from src.equation_solver import EquationSolver, EquationSolution, ComplexNumber
from src.verifier import SolutionVerifier, VerificationResult


def parse_coefficients(input_str: str) -> List[float]:
    """Parse coefficient string into list of floats."""
    try:
        coeffs = [float(x.strip()) for x in input_str.split(',')]
        return coeffs
    except ValueError as e:
        raise ValueError(f"Invalid coefficient format: {e}")


def main():
    """Main program entry point."""
    print("Equation Solver")
    print("=" * 40)
    print("Solve quadratic, cubic, and quartic equations with detailed steps")
    print()

    while True:
        print("Select equation type:")
        print("1. Quadratic (ax² + bx + c = 0)")
        print("2. Cubic (ax³ + bx² + cx + d = 0)")
        print("3. Quartic (ax⁴ + bx³ + cx² + dx + e = 0)")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == '4':
            print("Goodbye!")
            break

        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            continue

        try:
            if choice == '1':
                coeffs_input = input("Enter coefficients a, b, c (comma-separated): ")
                coeffs = parse_coefficients(coeffs_input)
                if len(coeffs) != 3:
                    raise ValueError("Quadratic requires exactly 3 coefficients")
                a, b, c = coeffs
                solution = EquationSolver.solve_quadratic(a, b, c)
                verifier = SolutionVerifier()
                verification_results = verifier.verify_quadratic(a, b, c, solution.roots)

            elif choice == '2':
                coeffs_input = input("Enter coefficients a, b, c, d (comma-separated): ")
                coeffs = parse_coefficients(coeffs_input)
                if len(coeffs) != 4:
                    raise ValueError("Cubic requires exactly 4 coefficients")
                a, b, c, d = coeffs
                solution = EquationSolver.solve_cubic(a, b, c, d)
                verifier = SolutionVerifier()
                verification_results = verifier.verify_cubic(a, b, c, d, solution.roots)

            elif choice == '3':
                coeffs_input = input("Enter coefficients a, b, c, d, e (comma-separated): ")
                coeffs = parse_coefficients(coeffs_input)
                if len(coeffs) != 5:
                    raise ValueError("Quartic requires exactly 5 coefficients")
                a, b, c, d, e = coeffs
                solution = EquationSolver.solve_quartic(a, b, c, d, e)
                verifier = SolutionVerifier()
                verification_results = verifier.verify_quartic(a, b, c, d, e, solution.roots)

            # Display solution
            EquationSolver.print_solution(solution)

            # Display verification
            verifier.print_verification_results(verification_results)

        except ValueError as e:
            print(f"Input error: {e}")
        except Exception as e:
            print(f"Error solving equation: {e}")

        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()