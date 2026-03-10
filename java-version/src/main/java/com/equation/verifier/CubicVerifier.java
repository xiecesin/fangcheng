package com.equation.verifier;

import com.equation.Complex;

/**
 * A verifier for cubic equation solutions.
 * Substitutes the found roots back into the original equation to verify correctness.
 */
public class CubicVerifier {

    /**
     * Verifies that the given roots satisfy the cubic equation ax^3 + bx^2 + cx + d = 0.
     * @param a coefficient of x^3
     * @param b coefficient of x^2
     * @param c coefficient of x
     * @param d constant term
     * @param roots the roots to verify
     * @return true if all roots are verified within tolerance
     */
    public static boolean verify(double a, double b, double c, double d, Complex[] roots) {
        System.out.println("验证三次方程解:");
        System.out.println("原方程: " + formatEquation(a, b, c, d));

        boolean allVerified = true;
        for (int i = 0; i < roots.length; i++) {
            Complex root = roots[i];
            // 计算 ax^3 + bx^2 + cx + d
            Complex xSquared = root.multiply(root);
            Complex xCubed = xSquared.multiply(root);
            Complex axCubed = new Complex(a).multiply(xCubed);
            Complex bxSquared = new Complex(b).multiply(xSquared);
            Complex cx = new Complex(c).multiply(root);
            Complex result = axCubed.add(bxSquared).add(cx).add(new Complex(d));

            boolean isZero = Math.abs(result.getReal()) < 1e-8 && Math.abs(result.getImaginary()) < 1e-8;
            System.out.println("根 " + (i + 1) + ": " + root + " → " + result + " = 0? " + isZero);

            if (!isZero) {
                allVerified = false;
            }
        }

        System.out.println("验证结果: " + (allVerified ? "通过" : "失败"));
        return allVerified;
    }

    /**
     * Formats the cubic equation as a string for verification display.
     */
    private static String formatEquation(double a, double b, double c, double d) {
        StringBuilder sb = new StringBuilder();

        if (Math.abs(a - 1.0) < 1e-10) {
            sb.append("x^3");
        } else if (Math.abs(a + 1.0) < 1e-10) {
            sb.append("-x^3");
        } else {
            sb.append(String.format("%.6g", a)).append("x^3");
        }

        if (Math.abs(b) > 1e-10) {
            if (b > 0 && sb.length() > 0) {
                sb.append(" + ");
            } else if (b < 0) {
                sb.append(" - ");
                b = -b;
            }

            if (Math.abs(b - 1.0) < 1e-10) {
                sb.append("x^2");
            } else {
                sb.append(String.format("%.6g", b)).append("x^2");
            }
        }

        if (Math.abs(c) > 1e-10) {
            if (c > 0 && sb.length() > 0) {
                sb.append(" + ");
            } else if (c < 0) {
                sb.append(" - ");
                c = -c;
            }

            if (Math.abs(c - 1.0) < 1e-10) {
                sb.append("x");
            } else {
                sb.append(String.format("%.6g", c)).append("x");
            }
        }

        if (Math.abs(d) > 1e-10) {
            if (d > 0 && sb.length() > 0) {
                sb.append(" + ");
            } else if (d < 0) {
                sb.append(" - ");
                d = -d;
            }
            sb.append(String.format("%.6g", d));
        }

        return sb.toString();
    }
}