package com.equation;

/**
 * Test class to verify symbolic solutions for cubic and quartic equations.
 */
public class SymbolicSolverTest {

    public void testCubicSymbolicSolution() {
        System.out.println("\n=== 测试三次方程符号解 ===");
        
        // Test case 1: x³ - 6x² + 11x - 6 = 0 (roots: 1, 2, 3)
        System.out.println("\n1. 测试方程: x³ - 6x² + 11x - 6 = 0");
        Complex[] roots1 = CubicSolver.solve(1, -6, 11, -6);
        System.out.println("根:");
        for (int i = 0; i < roots1.length; i++) {
            System.out.println("x" + (i+1) + " = " + roots1[i]);
        }
        
        // Test case 2: x³ + 2x² + 3x + 4 = 0 (one real root, two complex)
        System.out.println("\n2. 测试方程: x³ + 2x² + 3x + 4 = 0");
        Complex[] roots2 = CubicSolver.solve(1, 2, 3, 4);
        System.out.println("根:");
        for (int i = 0; i < roots2.length; i++) {
            System.out.println("x" + (i+1) + " = " + roots2[i]);
        }
    }
    
    public void testQuarticSymbolicSolution() {
        System.out.println("\n=== 测试四次方程符号解 ===");
        
        // Test case 1: x⁴ - 10x³ + 35x² - 50x + 24 = 0 (roots: 1, 2, 3, 4)
        System.out.println("\n1. 测试方程: x⁴ - 10x³ + 35x² - 50x + 24 = 0");
        Complex[] roots1 = QuarticSolver.solve(1, -10, 35, -50, 24);
        System.out.println("根:");
        for (int i = 0; i < roots1.length; i++) {
            System.out.println("x" + (i+1) + " = " + roots1[i]);
        }
        
        // Test case 2: x⁴ + 1 = 0 (biquadratic equation)
        System.out.println("\n2. 测试方程: x⁴ + 1 = 0");
        Complex[] roots2 = QuarticSolver.solve(1, 0, 0, 0, 1);
        System.out.println("根:");
        for (int i = 0; i < roots2.length; i++) {
            System.out.println("x" + (i+1) + " = " + roots2[i]);
        }
    }
    
    public static void main(String[] args) {
        SymbolicSolverTest test = new SymbolicSolverTest();
        test.testCubicSymbolicSolution();
        test.testQuarticSymbolicSolution();
        System.out.println("\n=== 所有测试完成 ===");
    }
}
