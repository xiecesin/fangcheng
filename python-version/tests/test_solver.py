"""
Test suite for the equation solver.
"""

import pytest
import math
import cmath
from src.equation_solver import EquationSolver, QuadraticSolver, CubicSolver, ComplexNumber
from src.verifier import SolutionVerifier


class TestQuadraticSolver:
    """Test cases for quadratic equation solver."""

    @pytest.mark.unit
    def test_quadratic_real_roots(self):
        """Test quadratic equation with real roots."""
        # x² - 5x + 6 = 0 → (x-2)(x-3) = 0 → x = 2, 3
        solution = EquationSolver.solve_quadratic(1, -5, 6)
        assert len(solution.roots) == 2
        assert solution.roots[0] == 3.0 or solution.roots[0] == 2.0
        assert solution.roots[1] == 2.0 or solution.roots[1] == 3.0

    @pytest.mark.unit
    def test_quadratic_complex_roots(self):
        """Test quadratic equation with complex roots."""
        # x² + 1 = 0 → x = ±i
        solution = EquationSolver.solve_quadratic(1, 0, 1)
        assert len(solution.roots) == 2
        assert isinstance(solution.roots[0], ComplexNumber)
        assert isinstance(solution.roots[1], ComplexNumber)

    @pytest.mark.unit
    def test_quadratic_double_root(self):
        """Test quadratic equation with double root."""
        # x² - 4x + 4 = 0 → (x-2)² = 0 → x = 2 (double root)
        solution = EquationSolver.solve_quadratic(1, -4, 4)
        assert len(solution.roots) == 2
        assert solution.roots[0] == 2.0
        assert solution.roots[1] == 2.0

    @pytest.mark.unit
    def test_quadratic_zero_coefficient_error(self):
        """Test that zero 'a' coefficient raises error."""
        with pytest.raises(ValueError):
            QuadraticSolver(0, 1, 1)


class TestCubicSolver:
    """Test cases for cubic equation solver."""

    @pytest.mark.unit
    def test_cubic_simple_case(self):
        """Test simple cubic equation."""
        # x³ - 1 = 0 → x = 1, and two complex roots
        solution = EquationSolver.solve_cubic(1, 0, 0, -1)
        assert len(solution.roots) == 3
        # One real root should be 1
        real_roots = [root for root in solution.roots if not isinstance(root, ComplexNumber)]
        assert len(real_roots) >= 1
        # Check if any root is approximately 1
        assert any(abs(root - 1.0) < 1e-10 for root in solution.roots if not isinstance(root, ComplexNumber))

    @pytest.mark.unit
    def test_cubic_zero_coefficient_error(self):
        """Test that zero 'a' coefficient raises error."""
        with pytest.raises(ValueError):
            CubicSolver(0, 1, 1, 1)


class TestSolutionVerifier:
    """Test cases for solution verifier."""

    @pytest.mark.unit
    def test_quadratic_verification(self):
        """Test verification of quadratic solutions."""
        a, b, c = 1, -5, 6
        solution = EquationSolver.solve_quadratic(a, b, c)
        verifier = SolutionVerifier()
        results = verifier.verify_quadratic(a, b, c, solution.roots)

        assert len(results) == 2
        assert all(result.is_valid for result in results)

    @pytest.mark.unit
    def test_cubic_verification(self):
        """Test verification of cubic solutions."""
        a, b, c, d = 1, 0, 0, -1
        solution = EquationSolver.solve_cubic(a, b, c, d)
        verifier = SolutionVerifier()
        results = verifier.verify_cubic(a, b, c, d, solution.roots)

        assert len(results) == 3
        # At least one should be valid (the real root)
        assert any(result.is_valid for result in results)


class TestComplexNumber:
    """Test cases for ComplexNumber class."""

    @pytest.mark.unit
    def test_complex_number_string_representation(self):
        """Test string representation of complex numbers."""
        # Test real number
        c1 = ComplexNumber(3.0, 0.0)
        assert str(c1) == "3"

        # Test pure imaginary
        c2 = ComplexNumber(0.0, 1.0)
        assert str(c2) == "i"

        c3 = ComplexNumber(0.0, -1.0)
        assert str(c3) == "-i"

        c4 = ComplexNumber(0.0, 2.5)
        assert str(c4) == "2.5i"

        # Test general complex
        c5 = ComplexNumber(3.0, 4.0)
        assert str(c5) == "3 + 4i"

        c6 = ComplexNumber(3.0, -4.0)
        assert str(c6) == "3 - 4i"


class TestIntegration:
    """Integration tests for the complete system."""

    @pytest.mark.integration
    def test_complete_quadratic_workflow(self):
        """Test complete workflow for quadratic equation."""
        # Solve equation
        solution = EquationSolver.solve_quadratic(1, -5, 6)

        # Verify solution
        verifier = SolutionVerifier()
        verification_results = verifier.verify_quadratic(1, -5, 6, solution.roots)

        # Check that all results are valid
        assert all(result.is_valid for result in verification_results)

    @pytest.mark.integration
    def test_complete_cubic_workflow(self):
        """Test complete workflow for cubic equation."""
        # Solve equation
        solution = EquationSolver.solve_cubic(1, 0, 0, -8)  # x³ - 8 = 0

        # Verify solution
        verifier = SolutionVerifier()
        verification_results = verifier.verify_cubic(1, 0, 0, -8, solution.roots)

        # Should have at least one valid real root (x = 2)
        assert any(result.is_valid for result in verification_results)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])