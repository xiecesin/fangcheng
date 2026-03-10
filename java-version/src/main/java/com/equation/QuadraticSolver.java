package com.equation;

/**
 * A solver for quadratic equations of the form ax^2 + bx + c = 0.
 * Provides detailed step-by-step solutions and handles all cases including complex roots.
 */
public class QuadraticSolver {

    /**
     * Solves a quadratic equation ax^2 + bx + c = 0.
     * @param a coefficient of x^2
     * @param b coefficient of x
     * @param c constant term
     * @return array of two Complex roots
     */
    public static Complex[] solve(double a, double b, double c) {
        System.out.println("Solving quadratic equation: " + formatEquation(a, b, c));

        if (Math.abs(a) < 1e-10) {
            throw new IllegalArgumentException("Coefficient 'a' cannot be zero for a quadratic equation");
        }

        // Step 1: Calculate discriminant
        double discriminantValue = b * b - 4 * a * c;
        Complex discriminant = new Complex(discriminantValue);
        System.out.println("Step 1: Calculate discriminant D = b^2 - 4ac");
        System.out.println("        D = (" + b + ")^2 - 4 * (" + a + ") * (" + c + ") = " + discriminantValue);

        // Step 2: Calculate square root of discriminant
        Complex sqrtDiscriminant = discriminant.sqrt();
        System.out.println("Step 2: Calculate sqrt(D) = " + sqrtDiscriminant);

        // Step 3: Apply quadratic formula
        Complex numerator1 = new Complex(-b).add(sqrtDiscriminant);
        Complex numerator2 = new Complex(-b).subtract(sqrtDiscriminant);
        Complex denominator = new Complex(2 * a);

        Complex root1 = numerator1.divide(denominator);
        Complex root2 = numerator2.divide(denominator);

        System.out.println("Step 3: Apply quadratic formula x = (-b ± sqrt(D)) / (2a)");
        System.out.println("        x1 = (" + (-b) + " + " + sqrtDiscriminant + ") / " + (2 * a) + " = " + root1);
        System.out.println("        x2 = (" + (-b) + " - " + sqrtDiscriminant + ") / " + (2 * a) + " = " + root2);

        return new Complex[]{root1, root2};
    }

    /**
     * Formats the quadratic equation as a string.
     */
    private static String formatEquation(double a, double b, double c) {
        StringBuilder sb = new StringBuilder();

        // Handle x^2 term
        if (Math.abs(a - 1.0) < 1e-10) {
            sb.append("x^2");
        } else if (Math.abs(a + 1.0) < 1e-10) {
            sb.append("-x^2");
        } else {
            sb.append(String.format("%.6g", a)).append("x^2");
        }

        // Handle x term
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

        // Handle constant term
        if (Math.abs(c) > 1e-10) {
            if (c > 0 && sb.length() > 0) {
                sb.append(" + ");
            } else if (c < 0) {
                sb.append(" - ");
                c = -c;
            }
            sb.append(String.format("%.6g", c));
        }

        sb.append(" = 0");
        return sb.toString();
    }
}