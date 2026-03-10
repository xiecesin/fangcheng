package com.equation;

/**
 * A class to represent complex numbers and perform operations on them.
 * Supports both real and complex numbers with proper formatting.
 */
public class Complex {
    private final double real;
    private final double imaginary;

    /**
     * Constructs a complex number with given real and imaginary parts.
     * @param real the real part
     * @param imaginary the imaginary part
     */
    public Complex(double real, double imaginary) {
        this.real = real;
        this.imaginary = imaginary;
    }

    /**
     * Constructs a real number (imaginary part = 0).
     * @param real the real part
     */
    public Complex(double real) {
        this(real, 0.0);
    }

    /**
     * Returns the real part of the complex number.
     */
    public double getReal() {
        return real;
    }

    /**
     * Returns the imaginary part of the complex number.
     */
    public double getImaginary() {
        return imaginary;
    }

    /**
     * Adds another complex number to this one.
     * @param other the complex number to add
     * @return the sum as a new Complex object
     */
    public Complex add(Complex other) {
        return new Complex(this.real + other.real, this.imaginary + other.imaginary);
    }

    /**
     * Subtracts another complex number from this one.
     * @param other the complex number to subtract
     * @return the difference as a new Complex object
     */
    public Complex subtract(Complex other) {
        return new Complex(this.real - other.real, this.imaginary - other.imaginary);
    }

    /**
     * Multiplies this complex number by another.
     * @param other the complex number to multiply by
     * @return the product as a new Complex object
     */
    public Complex multiply(Complex other) {
        double newReal = this.real * other.real - this.imaginary * other.imaginary;
        double newImaginary = this.real * other.imaginary + this.imaginary * other.real;
        return new Complex(newReal, newImaginary);
    }

    /**
     * Divides this complex number by another.
     * @param other the complex number to divide by
     * @return the quotient as a new Complex object
     */
    public Complex divide(Complex other) {
        double denominator = other.real * other.real + other.imaginary * other.imaginary;
        if (Math.abs(denominator) < 1e-10) {
            throw new ArithmeticException("Division by zero");
        }
        double newReal = (this.real * other.real + this.imaginary * other.imaginary) / denominator;
        double newImaginary = (this.imaginary * other.real - this.real * other.imaginary) / denominator;
        return new Complex(newReal, newImaginary);
    }

    /**
     * Calculates the square root of this complex number.
     * @return the square root as a new Complex object
     */
    public Complex sqrt() {
        if (imaginary == 0) {
            if (real >= 0) {
                return new Complex(Math.sqrt(real));
            } else {
                return new Complex(0, Math.sqrt(-real));
            }
        }

        double magnitude = Math.sqrt(real * real + imaginary * imaginary);
        double newReal = Math.sqrt((magnitude + real) / 2);
        double newImaginary = Math.signum(imaginary) * Math.sqrt((magnitude - real) / 2);
        return new Complex(newReal, newImaginary);
    }

    /**
     * Calculates the cube root of this complex number using polar form.
     * @return the principal cube root as a new Complex object
     */
    public Complex cbrt() {
        if (real == 0 && imaginary == 0) {
            return new Complex(0);
        }

        double magnitude = Math.sqrt(real * real + imaginary * imaginary);
        double angle = Math.atan2(imaginary, real);
        double newMagnitude = Math.cbrt(magnitude);
        double newAngle = angle / 3;
        return new Complex(newMagnitude * Math.cos(newAngle), newMagnitude * Math.sin(newAngle));
    }

    /**
     * Checks if this complex number is approximately equal to another.
     * @param other the complex number to compare with
     * @param tolerance the tolerance for comparison
     * @return true if the numbers are approximately equal
     */
    public boolean equals(Complex other, double tolerance) {
        return Math.abs(this.real - other.real) < tolerance &&
               Math.abs(this.imaginary - other.imaginary) < tolerance;
    }

    /**
     * Checks if this complex number is real (imaginary part is zero).
     * @return true if the number is real
     */
    public boolean isReal() {
        return Math.abs(imaginary) < 1e-10;
    }

    /**
     * Returns a string representation of the complex number.
     * Formats as "a", "bi", or "a + bi" depending on the values.
     */
    @Override
    public String toString() {
        if (Math.abs(imaginary) < 1e-10) {
            return String.format("%.6g", real);
        }
        if (Math.abs(real) < 1e-10) {
            if (Math.abs(imaginary - 1.0) < 1e-10) {
                return "i";
            } else if (Math.abs(imaginary + 1.0) < 1e-10) {
                return "-i";
            } else {
                return String.format("%.6g", imaginary) + "i";
            }
        }

        String realPart = String.format("%.6g", real);
        String imagPart;
        if (Math.abs(imaginary - 1.0) < 1e-10) {
            imagPart = "i";
        } else if (Math.abs(imaginary + 1.0) < 1e-10) {
            imagPart = "-i";
        } else {
            imagPart = String.format("%.6g", Math.abs(imaginary)) + "i";
        }

        if (imaginary > 0) {
            return realPart + " + " + imagPart;
        } else {
            return realPart + " - " + imagPart;
        }
    }
}