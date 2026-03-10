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
        System.out.println("Solving quartic equation: " + formatEquation(a, b, c, d, e));

        if (Math.abs(a) < 1e-10) {
            throw new IllegalArgumentException("Coefficient 'a' cannot be zero for a quartic equation");
        }

        // Step 1: Normalize to monic polynomial (divide by a)
        double aNorm = 1.0;
        double bNorm = b / a;
        double cNorm = c / a;
        double dNorm = d / a;
        double eNorm = e / a;

        System.out.println("Step 1: Normalize to monic polynomial (divide by a = " + a + ")");
        System.out.println("        x^4 + (" + bNorm + ")x^3 + (" + cNorm + ")x^2 + (" + dNorm + ")x + (" + eNorm + ") = 0");

        // Step 2: Depress the quartic (eliminate x^3 term) using substitution x = y - b/(4a)
        double p = cNorm - 3.0 * bNorm * bNorm / 8.0;
        double q = bNorm * bNorm * bNorm / 8.0 - bNorm * cNorm / 2.0 + dNorm;
        double r = -3.0 * bNorm * bNorm * bNorm * bNorm / 256.0 + bNorm * bNorm * cNorm / 16.0 - bNorm * dNorm / 4.0 + eNorm;

        System.out.println("Step 2: Depress the quartic using substitution x = y - b/(4a)");
        System.out.println("        Resulting in: y^4 + py^2 + qy + r = 0");
        System.out.println("        where p = " + p + ", q = " + q + ", r = " + r);

        // Step 3: Handle special cases
        if (Math.abs(q) < 1e-10) {
            // Biquadratic case: y^4 + py^2 + r = 0
            System.out.println("Step 3: Special case - biquadratic equation (q = 0)");
            return solveBiquadratic(p, r, bNorm);
        }

        // Step 4: Solve the cubic resolvent: z^3 + (p/2)z^2 + ((p^2 - 4r)/16)z - q^2/64 = 0
        System.out.println("Step 4: Solve cubic resolvent to find parameter m");
        double cubicA = 1.0;
        double cubicB = p / 2.0;
        double cubicC = (p * p - 4.0 * r) / 16.0;
        double cubicD = -q * q / 64.0;

        Complex[] cubicRoots = CubicSolver.solve(cubicA, cubicB, cubicC, cubicD);

        // Find a real root of the cubic resolvent (preferably positive)
        Complex m = null;
        for (Complex root : cubicRoots) {
            if (root.isReal() && root.getReal() >= 0) {
                m = root;
                break;
            }
        }
        if (m == null) {
            // If no non-negative real root, take the first real root
            for (Complex root : cubicRoots) {
                if (root.isReal()) {
                    m = root;
                    break;
                }
            }
        }
        if (m == null) {
            // If no real root, take the first root
            m = cubicRoots[0];
        }

        System.out.println("        Found m = " + m);

        // Step 5: Use m to factor the quartic into two quadratics
        Complex sqrtM = m.sqrt();
        Complex alpha = new Complex(2.0).multiply(sqrtM);
        Complex beta = new Complex(p).add(new Complex(2.0).multiply(m));
        Complex gamma = new Complex(q).divide(new Complex(2.0).multiply(sqrtM));

        System.out.println("Step 5: Factor quartic into two quadratics using m");
        System.out.println("        First quadratic: y^2 + αy + β = 0");
        System.out.println("        where α = " + alpha + ", β = " + beta);
        System.out.println("        Second quadratic: y^2 - αy + γ = 0");
        System.out.println("        where γ = " + gamma);

        // Step 6: Solve the two quadratic equations
        Complex[] roots1 = QuadraticSolver.solve(1.0, alpha.getReal(), beta.getReal());
        Complex[] roots2 = QuadraticSolver.solve(1.0, -alpha.getReal(), gamma.getReal());

        // Step 7: Convert back from y to x
        Complex[] roots = new Complex[4];
        for (int i = 0; i < 2; i++) {
            roots[i] = roots1[i].subtract(new Complex(bNorm / 4.0));
            roots[i + 2] = roots2[i].subtract(new Complex(bNorm / 4.0));
        }

        System.out.println("Step 6: Convert back from y to x using x = y - b/(4a)");
        System.out.println("        Final roots:");
        for (int i = 0; i < 4; i++) {
            System.out.println("        x" + (i + 1) + " = " + roots[i]);
        }

        return roots;
    }

    /**
     * Solves a biquadratic equation y^4 + py^2 + r = 0.
     */
    private static Complex[] solveBiquadratic(double p, double r, double bNorm) {
        System.out.println("        Solving biquadratic equation y^4 + (" + p + ")y^2 + (" + r + ") = 0");
        System.out.println("        Substitute z = y^2, giving z^2 + pz + r = 0");

        Complex[] zRoots = QuadraticSolver.solve(1.0, p, r);
        Complex[] yRoots = new Complex[4];

        System.out.println("        Solutions for z:");
        for (int i = 0; i < 2; i++) {
            System.out.println("        z" + (i + 1) + " = " + zRoots[i]);
        }

        System.out.println("        Now solve y^2 = z for each z:");
        for (int i = 0; i < 2; i++) {
            Complex sqrtZ = zRoots[i].sqrt();
            yRoots[i * 2] = sqrtZ;
            yRoots[i * 2 + 1] = new Complex(0).subtract(sqrtZ);
            System.out.println("        For z" + (i + 1) + " = " + zRoots[i] + ":");
            System.out.println("            y = ±" + sqrtZ);
        }

        // Convert back from y to x
        Complex[] roots = new Complex[4];
        for (int i = 0; i < 4; i++) {
            roots[i] = yRoots[i].subtract(new Complex(bNorm / 4.0));
        }

        System.out.println("        Converting back to x = y - b/(4a):");
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