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
        System.out.println("=== Java方程求解器 ===\n");

        // 测试二次方程
        testQuadraticEquations();

        // 测试三次方程
        testCubicEquations();

        // 测试四次方程
        testQuarticEquations();

        System.out.println("\n=== 所有测试完成 ===");
    }

    private static void testQuadraticEquations() {
        System.out.println("1. 测试二次方程\n");

        // 测试用例1: 实根
        System.out.println("测试1: x^2 - 5x + 6 = 0 (应有根 2, 3)");
        Complex[] roots1 = QuadraticSolver.solve(1, -5, 6);
        QuadraticVerifier.verify(1, -5, 6, roots1);
        System.out.println();

        // 测试用例2: 复根
        System.out.println("测试2: x^2 + 1 = 0 (应有根 i, -i)");
        Complex[] roots2 = QuadraticSolver.solve(1, 0, 1);
        QuadraticVerifier.verify(1, 0, 1, roots2);
        System.out.println();

        // 测试用例3: 重根
        System.out.println("测试3: x^2 - 4x + 4 = 0 (应有重根 2)");
        Complex[] roots3 = QuadraticSolver.solve(1, -4, 4);
        QuadraticVerifier.verify(1, -4, 4, roots3);
        System.out.println();
    }

    private static void testCubicEquations() {
        System.out.println("2. 测试三次方程\n");

        // 测试用例1: 三个实根
        System.out.println("测试1: x^3 - 6x^2 + 11x - 6 = 0 (应有根 1, 2, 3)");
        Complex[] roots1 = CubicSolver.solve(1, -6, 11, -6);
        CubicVerifier.verify(1, -6, 11, -6, roots1);
        System.out.println();

        // 测试用例2: 一个实根，两个复根
        System.out.println("测试2: x^3 - 1 = 0 (应有根 1, -0.5±0.866i)");
        Complex[] roots2 = CubicSolver.solve(1, 0, 0, -1);
        CubicVerifier.verify(1, 0, 0, -1, roots2);
        System.out.println();

        // 测试用例3: 多重根
        System.out.println("测试3: x^3 - 3x^2 + 3x - 1 = 0 (应有三重根 1)");
        Complex[] roots3 = CubicSolver.solve(1, -3, 3, -1);
        CubicVerifier.verify(1, -3, 3, -1, roots3);
        System.out.println();
    }

    private static void testQuarticEquations() {
        System.out.println("3. 测试四次方程\n");

        // 测试用例1: 双二次方程
        System.out.println("测试1: x^4 - 5x^2 + 4 = 0 (应有根 ±1, ±2)");
        Complex[] roots1 = QuarticSolver.solve(1, 0, -5, 0, 4);
        QuarticVerifier.verify(1, 0, -5, 0, 4, roots1);
        System.out.println();

        // 测试用例2: 一般四次方程（实根）
        System.out.println("测试2: x^4 - 10x^3 + 35x^2 - 50x + 24 = 0 (应有根 1, 2, 3, 4)");
        Complex[] roots2 = QuarticSolver.solve(1, -10, 35, -50, 24);
        QuarticVerifier.verify(1, -10, 35, -50, 24, roots2);
        System.out.println();

        // 测试用例3: 含复根的四次方程
        System.out.println("测试3: x^4 + 1 = 0 (应有四个复根)");
        Complex[] roots3 = QuarticSolver.solve(1, 0, 0, 0, 1);
        QuarticVerifier.verify(1, 0, 0, 0, 1, roots3);
        System.out.println();
    }
}