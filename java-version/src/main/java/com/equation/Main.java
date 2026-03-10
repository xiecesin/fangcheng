package com.equation;

import com.equation.verifier.QuadraticVerifier;
import com.equation.verifier.CubicVerifier;
import com.equation.verifier.QuarticVerifier;

/**
 * Main entry point for the equation solver application.
 * Demonstrates solving quadratic, cubic, and quartic equations with verification.
 */
public class Main {

    public static void main(String[] args) {
        System.out.println("=== Java Equation Solver ===\n");

        // Test quadratic equations
        testQuadraticEquations();

        // Test cubic equations
        testCubicEquations();

        // Test quartic equations
        testQuarticEquations();

        System.out.println("\n=== All tests completed ===");
    }

    private static void testQuadraticEquations() {
        System.out.println("1. TESTING QUADRATIC EQUATIONS\n");

        // Test case 1: Real roots
        System.out.println("Test 1: x^2 - 5x + 6 = 0 (should have roots 2, 3)");
        Complex[] roots1 = QuadraticSolver.solve(1, -5, 6);
        QuadraticVerifier.verify(1, -5, 6, roots1);
        System.out.println();

        // Test case 2: Complex roots
        System.out.println("Test 2: x^2 + 1 = 0 (should have roots i, -i)");
        Complex[] roots2 = QuadraticSolver.solve(1, 0, 1);
        QuadraticVerifier.verify(1, 0, 1, roots2);
        System.out.println();

        // Test case 3: Repeated root
        System.out.println("Test 3: x^2 - 4x + 4 = 0 (should have repeated root 2)");
        Complex[] roots3 = QuadraticSolver.solve(1, -4, 4);
        QuadraticVerifier.verify(1, -4, 4, roots3);
        System.out.println();
    }

    private static void testCubicEquations() {
        System.out.println("2. TESTING CUBIC EQUATIONS\n");

        // Test case 1: Three real roots
        System.out.println("Test 1: x^3 - 6x^2 + 11x - 6 = 0 (should have roots 1, 2, 3)");
        Complex[] roots1 = CubicSolver.solve(1, -6, 11, -6);
        CubicVerifier.verify(1, -6, 11, -6, roots1);
        System.out.println();

        // Test case 2: One real root, two complex roots
        System.out.println("Test 2: x^3 - 1 = 0 (should have roots 1, -0.5±0.866i)");
        Complex[] roots2 = CubicSolver.solve(1, 0, 0, -1);
        CubicVerifier.verify(1, 0, 0, -1, roots2);
        System.out.println();

        // Test case 3: Multiple roots
        System.out.println("Test 3: x^3 - 3x^2 + 3x - 1 = 0 (should have triple root 1)");
        Complex[] roots3 = CubicSolver.solve(1, -3, 3, -1);
        CubicVerifier.verify(1, -3, 3, -1, roots3);
        System.out.println();
    }

    private static void testQuarticEquations() {
        System.out.println("3. TESTING QUARTIC EQUATIONS\n");

        // Test case 1: Biquadratic equation
        System.out.println("Test 1: x^4 - 5x^2 + 4 = 0 (should have roots ±1, ±2)");
        Complex[] roots1 = QuarticSolver.solve(1, 0, -5, 0, 4);
        QuarticVerifier.verify(1, 0, -5, 0, 4, roots1);
        System.out.println();

        // Test case 2: General quartic with real roots
        System.out.println("Test 2: x^4 - 10x^3 + 35x^2 - 50x + 24 = 0 (should have roots 1, 2, 3, 4)");
        Complex[] roots2 = QuarticSolver.solve(1, -10, 35, -50, 24);
        QuarticVerifier.verify(1, -10, 35, -50, 24, roots2);
        System.out.println();

        // Test case 3: Quartic with complex roots
        System.out.println("Test 3: x^4 + 1 = 0 (should have four complex roots)");
        Complex[] roots3 = QuarticSolver.solve(1, 0, 0, 0, 1);
        QuarticVerifier.verify(1, 0, 0, 0, 1, roots3);
        System.out.println();
    }
}