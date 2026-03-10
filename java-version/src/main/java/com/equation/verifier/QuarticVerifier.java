package com.equation.verifier;

import com.equation.Complex;

/**
 * A verifier for quartic equation solutions.
 * Substitutes the found roots back into the original equation to verify correctness.
 */
public class QuarticVerifier {

    /**
     * Verifies that the given roots satisfy the quartic equation ax^4 + bx^3 + cx^2 + dx + e = 0.
     * @param a coefficient of x^4
     * @param b coefficient of x^3
     * @param c coefficient of x^2
     * @param d coefficient of x
     * @param e constant term
     * @param roots the roots to verify
     * @return true if all roots are verified within tolerance
     */
    public static boolean verify(double a, double b, double c, double d, double e, Complex[] roots) {
        System.out.println("Verifying quartic equation solutions:");
        System.out.println("Original equation: " + formatEquation(a, b, c, d, e));

        boolean allVerified = true;
        for (int i = 0; i < roots.length; i++) {
            Complex root = roots[i];
            // Calculate ax^4 + bx^3 + cx^2 + dx + e
            Complex xSquared = root.multiply(root);
            Complex xCubed = xSquared.multiply(root);
            Complex xQuartic = xCubed.multiply(root);
            Complex axQuartic = new Complex(a).multiply(xQuartic);
            Complex bxCubed = new Complex(b).multiply(xCubed);
            Complex cxSquared = new Complex(c).multiply(xSquared);
            Complex dx = new Complex(d).multiply(root);
            Complex result = axQuartic.add(bxCubed).add(cxSquared).add(dx).add(new Complex(e));

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
     * Formats the quartic equation as a string for verification display.
     */
    private static String formatEquation(double a, double b, double c, double d, double e) {
        StringBuilder sb = new StringBuilder();

        if (Math.abs(a - 1.0) < 1e-10) {
            sb.append("x^4");
        } else if (Math.abs(a + 1.0) < 1e-10) {
            sb.append("-x^4");
        } else {
            sb.append(String.format("%.6g", a)).append("x^4");
        }

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

        if (Math.abs(e) > 1e-10) {
            if (e > 0 && sb.length() > 0) {
                sb.append(" + ");
            } else if (e < 0) {
                sb.append(" - ");
                e = -e;
            }
            sb.append(String.format("%.6g", e));
        }

        return sb.toString();
    }
}