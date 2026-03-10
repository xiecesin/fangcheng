package com.equation;

/**
 * Demo application to test cubic equations with symbolic solutions.
 */
public class CubicTest {

    public static void main(String[] args) {
        System.out.println("三次方程求解器符号解演示");
        System.out.println("==================================================");
        
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
        
        System.out.println("\n=== 演示完成 ===");
    }
}