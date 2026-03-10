package com.equation;

/**
 * A solver for cubic equations of the form ax^3 + bx^2 + cx + d = 0.
 * Uses Cardano's method to find all three roots (real or complex).
 */
public class CubicSolver {

    /**
     * Solves a cubic equation ax^3 + bx^2 + cx + d = 0.
     * @param a coefficient of x^3
     * @param b coefficient of x^2
     * @param c coefficient of x
     * @param d constant term
     * @return array of three Complex roots
     */
    public static Complex[] solve(double a, double b, double c, double d) {
        System.out.println("Solving cubic equation: " + formatEquation(a, b, c, d));

        if (Math.abs(a) < 1e-10) {
            throw new IllegalArgumentException("Coefficient 'a' cannot be zero for a cubic equation");
        }

        // Step 1: Normalize to monic polynomial (divide by a)
        double aNorm = 1.0;
        double bNorm = b / a;
        double cNorm = c / a;
        double dNorm = d / a;

        System.out.println("Step 1: Normalize to monic polynomial (divide by a = " + a + ")");
        System.out.println("        x^3 + (" + bNorm + ")x^2 + (" + cNorm + ")x + (" + dNorm + ") = 0");

        // Step 2: Depress the cubic (eliminate x^2 term) using substitution x = t - b/(3a)
        double p = cNorm - bNorm * bNorm / 3.0;
        double q = (2.0 * bNorm * bNorm * bNorm - 9.0 * bNorm * cNorm + 27.0 * dNorm) / 27.0;

        System.out.println("Step 2: Depress the cubic using substitution x = t - b/(3a)");
        System.out.println("        Resulting in: t^3 + pt + q = 0");
        System.out.println("        where p = " + p + ", q = " + q);

        // Step 3: Calculate discriminant
        double discriminant = (q * q) / 4.0 + (p * p * p) / 27.0;
        System.out.println("Step 3: Calculate discriminant Δ = (q/2)^2 + (p/3)^3 = " + discriminant);

        Complex[] roots = new Complex[3];

        if (Math.abs(discriminant) < 1e-10) {
            // Multiple roots case
            System.out.println("        Discriminant is zero - multiple roots");
            if (Math.abs(p) < 1e-10) {
                // Triple root
                Complex tRoot = new Complex(-q / 2.0).cbrt();
                roots[0] = tRoot.subtract(new Complex(bNorm / 3.0));
                roots[1] = roots[0];
                roots[2] = roots[0];
                System.out.println("        Triple root at t = " + tRoot);
            } else {
                // One simple root and one double root
                Complex tRoot1 = new Complex(-3.0 * q / p);
                Complex tRoot2 = new Complex(3.0 * q / (2.0 * p));
                roots[0] = tRoot1.subtract(new Complex(bNorm / 3.0));
                roots[1] = tRoot2.subtract(new Complex(bNorm / 3.0));
                roots[2] = roots[1];
                System.out.println("        Simple root at t = " + tRoot1 + ", double root at t = " + tRoot2);
            }
        } else if (discriminant > 0) {
            // One real root, two complex conjugate roots
            System.out.println("        Discriminant positive - one real root, two complex roots");
            Complex sqrtDiscriminant = new Complex(discriminant).sqrt();
            Complex u = new Complex(-q / 2.0).add(sqrtDiscriminant).cbrt();
            Complex v = new Complex(-q / 2.0).subtract(sqrtDiscriminant).cbrt();

            Complex tRoot1 = u.add(v);
            Complex omega = new Complex(-0.5, Math.sqrt(3.0) / 2.0); // primitive cube root of unity
            Complex tRoot2 = u.multiply(omega).add(v.multiply(omega.multiply(omega)));
            Complex tRoot3 = u.multiply(omega.multiply(omega)).add(v.multiply(omega));

            roots[0] = tRoot1.subtract(new Complex(bNorm / 3.0));
            roots[1] = tRoot2.subtract(new Complex(bNorm / 3.0));
            roots[2] = tRoot3.subtract(new Complex(bNorm / 3.0));

            System.out.println("        t1 = " + tRoot1);
            System.out.println("        t2 = " + tRoot2);
            System.out.println("        t3 = " + tRoot3);
        } else {
            // Three distinct real roots (casus irreducibilis)
            System.out.println("        Discriminant negative - three distinct real roots");
            double rho = Math.sqrt(-(p * p * p) / 27.0);
            double theta = Math.acos(-q / (2.0 * rho));

            Complex tRoot1 = new Complex(2.0 * Math.cbrt(rho) * Math.cos(theta / 3.0));
            Complex tRoot2 = new Complex(2.0 * Math.cbrt(rho) * Math.cos((theta + 2.0 * Math.PI) / 3.0));
            Complex tRoot3 = new Complex(2.0 * Math.cbrt(rho) * Math.cos((theta + 4.0 * Math.PI) / 3.0));

            roots[0] = tRoot1.subtract(new Complex(bNorm / 3.0));
            roots[1] = tRoot2.subtract(new Complex(bNorm / 3.0));
            roots[2] = tRoot3.subtract(new Complex(bNorm / 3.0));

            System.out.println("        t1 = " + tRoot1);
            System.out.println("        t2 = " + tRoot2);
            System.out.println("        t3 = " + tRoot3);
        }

        // Convert back from t to x
        System.out.println("Step 4: Convert back from t to x using x = t - b/(3a)");
        System.out.println("        Final roots:");
        for (int i = 0; i < 3; i++) {
            System.out.println("        x" + (i + 1) + " = " + roots[i]);
        }

        return roots;
    }

    /**
     * Formats the cubic equation as a string.
     */
    private static String formatEquation(double a, double b, double c, double d) {
        StringBuilder sb = new StringBuilder();

        // Handle x^3 term
        if (Math.abs(a - 1.0) < 1e-10) {
            sb.append("x^3");
        } else if (Math.abs(a + 1.0) < 1e-10) {
            sb.append("-x^3");
        } else {
            sb.append(String.format("%.6g", a)).append("x^3");
        }

        // Handle x^2 term
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

        // Handle x term
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

        // Handle constant term
        if (Math.abs(d) > 1e-10) {
            if (d > 0 && sb.length() > 0) {
                sb.append(" + ");
            } else if (d < 0) {
                sb.append(" - ");
                d = -d;
            }
            sb.append(String.format("%.6g", d));
        }

        sb.append(" = 0");
        return sb.toString();
    }
}