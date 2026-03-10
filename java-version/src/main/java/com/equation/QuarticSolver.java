package com.equation;

/**
 * A solver for quartic equations of the form ax^4 + bx^3 + cx^2 + dx + e = 0.
 * Uses Ferrari's method to reduce to a cubic resolvent and then solve.
 */
public class QuarticSolver {

    /**
     * Solves a quartic equation ax^4 + bx^3 + cx^2 + dx + e = 0.
     * @param a coefficient of x^4
     * @param b coefficient of x^3
     * @param c coefficient of x^2
     * @param d coefficient of x
     * @param e constant term
     * @return array of four Complex roots
     */
    public static Complex[] solve(double a, double b, double c, double d, double e) {
        System.out.println("求解四次方程: " + formatEquation(a, b, c, d, e));

        if (Math.abs(a) < 1e-10) {
            throw new IllegalArgumentException("四次方程的系数 'a' 不能为零");
        }

        // 步骤1: 归一化为首一多项式（除以a）
        double aNorm = 1.0;
        double bNorm = b / a;
        double cNorm = c / a;
        double dNorm = d / a;
        double eNorm = e / a;

        System.out.println("步骤1: 归一化为首一多项式（除以a = " + a + "）");
        System.out.println("        x^4 + (" + bNorm + ")x^3 + (" + cNorm + ")x^2 + (" + dNorm + ")x + (" + eNorm + ") = 0");

        // 步骤2: 降次（消除x^3项），使用代换 x = y - b/(4a)
        double p = cNorm - 3.0 * bNorm * bNorm / 8.0;
        double q = bNorm * bNorm * bNorm / 8.0 - bNorm * cNorm / 2.0 + dNorm;
        double r = -3.0 * bNorm * bNorm * bNorm * bNorm / 256.0 + bNorm * bNorm * cNorm / 16.0 - bNorm * dNorm / 4.0 + eNorm;

        System.out.println("步骤2: 降次，使用代换 x = y - b/(4a)");
        System.out.println("        结果: y^4 + py^2 + qy + r = 0");
        System.out.println("        其中 p = " + p + ", q = " + q + ", r = " + r);

        // 步骤3: 处理特殊情况
        if (Math.abs(q) < 1e-10) {
            // 双二次情况: y^4 + py^2 + r = 0
            System.out.println("步骤3: 特殊情况 - 双二次方程 (q = 0)");
            return solveBiquadratic(p, r, bNorm);
        }

        // 步骤4: 求解三次预解方程: z^3 + (p/2)z^2 + ((p^2 - 4r)/16)z - q^2/64 = 0
        System.out.println("步骤4: 求解三次预解方程以找到参数m");
        double cubicA = 1.0;
        double cubicB = p / 2.0;
        double cubicC = (p * p - 4.0 * r) / 16.0;
        double cubicD = -q * q / 64.0;

        Complex[] cubicRoots = CubicSolver.solve(cubicA, cubicB, cubicC, cubicD);

        // 找到三次预解方程的实根（优先选择非负实根）
        Complex m = null;
        for (Complex root : cubicRoots) {
            if (root.isReal() && root.getReal() >= 0) {
                m = root;
                break;
            }
        }
        if (m == null) {
            // 如果没有非负实根，取第一个实根
            for (Complex root : cubicRoots) {
                if (root.isReal()) {
                    m = root;
                    break;
                }
            }
        }
        if (m == null) {
            // 如果没有实根，取第一个根
            m = cubicRoots[0];
        }

        System.out.println("        找到 m = " + m);

        // 步骤5: 使用m将四次方程分解为两个二次方程
        Complex sqrtM = m.sqrt();
        Complex alpha = new Complex(2.0).multiply(sqrtM);
        Complex beta = new Complex(p).add(new Complex(2.0).multiply(m));
        Complex gamma = new Complex(q).divide(new Complex(2.0).multiply(sqrtM));

        System.out.println("步骤5: 使用m将四次方程分解为两个二次方程");
        System.out.println("        第一个二次方程: y^2 + αy + β = 0");
        System.out.println("        其中 α = " + alpha + ", β = " + beta);
        System.out.println("        第二个二次方程: y^2 - αy + γ = 0");
        System.out.println("        其中 γ = " + gamma);

        // 步骤6: 求解两个二次方程
        Complex[] roots1 = QuadraticSolver.solve(1.0, alpha.getReal(), beta.getReal());
        Complex[] roots2 = QuadraticSolver.solve(1.0, -alpha.getReal(), gamma.getReal());

        // 步骤7: 从y转换回x
        Complex[] roots = new Complex[4];
        for (int i = 0; i < 2; i++) {
            roots[i] = roots1[i].subtract(new Complex(bNorm / 4.0));
            roots[i + 2] = roots2[i].subtract(new Complex(bNorm / 4.0));
        }

        System.out.println("步骤7: 使用 x = y - b/(4a) 从y转换回x");
        System.out.println("        最终根:");
        for (int i = 0; i < 4; i++) {
            System.out.println("        x" + (i + 1) + " = " + roots[i]);
        }

        return roots;
    }

    /**
     * Solves a biquadratic equation y^4 + py^2 + r = 0.
     */
    private static Complex[] solveBiquadratic(double p, double r, double bNorm) {
        System.out.println("        求解双二次方程 y^4 + (" + p + ")y^2 + (" + r + ") = 0");
        System.out.println("        令 z = y^2，得到 z^2 + pz + r = 0");

        Complex[] zRoots = QuadraticSolver.solve(1.0, p, r);
        Complex[] yRoots = new Complex[4];

        System.out.println("        z的解:");
        for (int i = 0; i < 2; i++) {
            System.out.println("        z" + (i + 1) + " = " + zRoots[i]);
        }

        System.out.println("        现在对每个z求解 y^2 = z:");
        for (int i = 0; i < 2; i++) {
            Complex sqrtZ = zRoots[i].sqrt();
            yRoots[i * 2] = sqrtZ;
            yRoots[i * 2 + 1] = new Complex(0).subtract(sqrtZ);
            System.out.println("        对于 z" + (i + 1) + " = " + zRoots[i] + ":");
            System.out.println("            y = ±" + sqrtZ);
        }

        // 从y转换回x
        Complex[] roots = new Complex[4];
        for (int i = 0; i < 4; i++) {
            roots[i] = yRoots[i].subtract(new Complex(bNorm / 4.0));
        }

        System.out.println("        转换回x = y - b/(4a):");
        for (int i = 0; i < 4; i++) {
            System.out.println("        x" + (i + 1) + " = " + roots[i]);
        }

        return roots;
    }

    /**
     * Formats the quartic equation as a string.
     */
    private static String formatEquation(double a, double b, double c, double d, double e) {
        StringBuilder sb = new StringBuilder();

        // Handle x^4 term
        if (Math.abs(a - 1.0) < 1e-10) {
            sb.append("x^4");
        } else if (Math.abs(a + 1.0) < 1e-10) {
            sb.append("-x^4");
        } else {
            sb.append(String.format("%.6g", a)).append("x^4");
        }

        // Handle x^3 term
        if (Math.abs(b) > 1e-10) {
            if (b > 0 && sb.length() > 0) {
                sb.append(" + ");
            } else if (b < 0) {
                sb.append(" - ");
                b = -b;
            }

            if (Math.abs(b - 1.0) < 1e-10) {
                sb.append("x^3");
            } else {
                sb.append(String.format("%.6g", b)).append("x^3");
            }
        }

        // Handle x^2 term
        if (Math.abs(c) > 1e-10) {
            if (c > 0 && sb.length() > 0) {
                sb.append(" + ");
            } else if (c < 0) {
                sb.append(" - ");
                c = -c;
            }

            if (Math.abs(c - 1.0) < 1e-10) {
                sb.append("x^2");
            } else {
                sb.append(String.format("%.6g", c)).append("x^2");
            }
        }

        // Handle x term
        if (Math.abs(d) > 1e-10) {
            if (d > 0 && sb.length() > 0) {
                sb.append(" + ");
            } else if (d < 0) {
                sb.append(" - ");
                d = -d;
            }

            if (Math.abs(d - 1.0) < 1e-10) {
                sb.append("x");
            } else {
                sb.append(String.format("%.6g", d)).append("x");
            }
        }

        // Handle constant term
        if (Math.abs(e) > 1e-10) {
            if (e > 0 && sb.length() > 0) {
                sb.append(" + ");
            } else if (e < 0) {
                sb.append(" - ");
                e = -e;
            }
            sb.append(String.format("%.6g", e));
        }

        sb.append(" = 0");
        return sb.toString();
    }
}