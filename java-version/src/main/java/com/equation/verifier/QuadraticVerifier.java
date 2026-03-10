package com.equation.verifier;

import com.equation.Complex;

/**
 * A verifier for quadratic equation solutions.
 * Substitutes the found roots back into the original equation to verify correctness.
 */
public class QuadraticVerifier {

    /**
     * Verifies that the given roots satisfy the quadratic equation ax^2 + bx + c = 0.
     * @param a coefficient of x^2
     * @param b coefficient of x
     * @param c constant term
     * @param roots the roots to verify
     * @return true if all roots are verified within tolerance
     */
    public static boolean verify(double a, double b, double c, Complex[] roots) {
        System.out.println("Verifying quadratic equation solutions:");
        System.out.println("Original equation: " + formatEquation(a, b, c));

        boolean allVerified = true;
        for (int i = 0; i < roots.length; i++) {
            Complex root = roots[i];
            // Calculate ax^2 + bx + c
            Complex xSquared = root.multiply(root);
            Complex axSquared = new Complex(a).multiply(xSquared);
            Complex bx = new Complex(b).multiply(root);
            Complex result = axSquared.add(bx).add(new Complex(c));

            boolean isZero = Math.abs(result.getReal()) < 1e-8 && Math.abs(result.getImaginary()) < 1e-8;
            System.out.println("Root " + (i + 1) + ": " + root + " → " + result + " = 0? " + isZero);

            if (!isZero) {
                allVerified = false;
            }
        }

        System.out.println("Verification result: " + (allVerified ? "PASSED" : "FAILED"));
        return allVerified;
    }

    /**
     * Formats the quadratic equation as a string for verification display.
     */
    private static String formatEquation(double a, double b, double c) {
        StringBuilder sb = new StringBuilder();

        if (Math.abs(a - 1.0) < 1e-10) {
            sb.append("x^2");
        } else if (Math.abs(a + 1.0) < 1e-10) {
            sb.append("-x^2");
        } else {
            sb.append(String.format("%.6g", a)).append("x^2");
        }

        if (Math.abs(b) > 1e-10) {
            if (b > 0 && sb.length() > 0) {
                sb.append(" + ");
            } else if (b < 0) {
                sb.append(" - ");
                b = -b;
            }

            if (Math.abs(b - 1.0) < 1e-10) {
                sb.append("x");
            } else {
                sb.append(String.format("%.6g", b)).append("x");
            }
        }

        if (Math.abs(c) > 1e-10) {
            if (c > 0 && sb.length() > 0) {
                sb.append(" + ");
            } else if (c < 0) {
                sb.append(" - ");
                c = -c;
            }
            sb.append(String.format("%.6g", c));
        }

        return sb.toString();
    }
}