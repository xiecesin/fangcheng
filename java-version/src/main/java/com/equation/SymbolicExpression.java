package com.equation;

/**
 * Represents a symbolic mathematical expression.
 * Can handle basic arithmetic operations, square roots, cube roots, and powers.
 */
public class SymbolicExpression {
    private Object value;
    private OperationType operationType;
    private SymbolicExpression leftOperand;
    private SymbolicExpression rightOperand;
    
    /**
     * Types of operations supported by symbolic expressions.
     */
    private enum OperationType {
        CONSTANT, VARIABLE, SQRT, CBRT, ADD, SUBTRACT, MULTIPLY, DIVIDE, POWER
    }
    
    /**
     * Creates a symbolic expression for a constant value.
     * @param value the constant value
     */
    public SymbolicExpression(double value) {
        this.value = value;
        this.operationType = OperationType.CONSTANT;
    }
    
    /**
     * Creates a symbolic expression for a variable.
     * @param variableName the name of the variable
     */
    public SymbolicExpression(String variableName) {
        this.value = variableName;
        this.operationType = OperationType.VARIABLE;
    }
    
    /**
     * Creates a symbolic expression for a unary operation (sqrt, cbrt).
     * @param operationType the type of operation
     * @param operand the operand
     */
    private SymbolicExpression(OperationType operationType, SymbolicExpression operand) {
        this.operationType = operationType;
        this.leftOperand = operand;
        this.value = null;
    }
    
    /**
     * Creates a symbolic expression for a binary operation (+, -, *, /, ^).
     * @param operationType the type of operation
     * @param leftOperand the left operand
     * @param rightOperand the right operand
     */
    private SymbolicExpression(OperationType operationType, SymbolicExpression leftOperand, SymbolicExpression rightOperand) {
        this.operationType = operationType;
        this.leftOperand = leftOperand;
        this.rightOperand = rightOperand;
        this.value = null;
    }
    
    /**
     * Creates a symbolic expression representing a square root.
     * @param expression the expression under the square root
     * @return the symbolic expression
     */
    public static SymbolicExpression sqrt(SymbolicExpression expression) {
        return new SymbolicExpression(OperationType.SQRT, expression);
    }
    
    /**
     * Creates a symbolic expression representing a cube root.
     * @param expression the expression under the cube root
     * @return the symbolic expression
     */
    public static SymbolicExpression cbrt(SymbolicExpression expression) {
        return new SymbolicExpression(OperationType.CBRT, expression);
    }
    
    /**
     * Creates a symbolic expression representing addition.
     * @param left the left operand
     * @param right the right operand
     * @return the symbolic expression
     */
    public static SymbolicExpression add(SymbolicExpression left, SymbolicExpression right) {
        return new SymbolicExpression(OperationType.ADD, left, right);
    }
    
    /**
     * Creates a symbolic expression representing subtraction.
     * @param left the left operand
     * @param right the right operand
     * @return the symbolic expression
     */
    public static SymbolicExpression subtract(SymbolicExpression left, SymbolicExpression right) {
        return new SymbolicExpression(OperationType.SUBTRACT, left, right);
    }
    
    /**
     * Creates a symbolic expression representing multiplication.
     * @param left the left operand
     * @param right the right operand
     * @return the symbolic expression
     */
    public static SymbolicExpression multiply(SymbolicExpression left, SymbolicExpression right) {
        return new SymbolicExpression(OperationType.MULTIPLY, left, right);
    }
    
    /**
     * Creates a symbolic expression representing division.
     * @param left the left operand
     * @param right the right operand
     * @return the symbolic expression
     */
    public static SymbolicExpression divide(SymbolicExpression left, SymbolicExpression right) {
        return new SymbolicExpression(OperationType.DIVIDE, left, right);
    }
    
    /**
     * Creates a symbolic expression representing a power operation.
     * @param base the base expression
     * @param exponent the exponent expression
     * @return the symbolic expression
     */
    public static SymbolicExpression power(SymbolicExpression base, SymbolicExpression exponent) {
        return new SymbolicExpression(OperationType.POWER, base, exponent);
    }
    
    /**
     * Evaluates the symbolic expression numerically.
     * @return the numeric value of the expression
     * @throws UnsupportedOperationException if the expression contains variables
     */
    public double evaluate() {
        switch (operationType) {
            case CONSTANT:
                return (double) value;
            case VARIABLE:
                throw new UnsupportedOperationException("Cannot evaluate expression with variable: " + value);
            case SQRT:
                return Math.sqrt(leftOperand.evaluate());
            case CBRT:
                return Math.cbrt(leftOperand.evaluate());
            case ADD:
                return leftOperand.evaluate() + rightOperand.evaluate();
            case SUBTRACT:
                return leftOperand.evaluate() - rightOperand.evaluate();
            case MULTIPLY:
                return leftOperand.evaluate() * rightOperand.evaluate();
            case DIVIDE:
                return leftOperand.evaluate() / rightOperand.evaluate();
            case POWER:
                return Math.pow(leftOperand.evaluate(), rightOperand.evaluate());
            default:
                throw new UnsupportedOperationException("Unsupported operation type: " + operationType);
        }
    }
    
    /**
     * Returns a string representation of the symbolic expression.
     * @return the string representation
     */
    @Override
    public String toString() {
        switch (operationType) {
            case CONSTANT:
                double val = (double) value;
                if (Math.abs(val - Math.round(val)) < 1e-10) {
                    return String.format("%.0f", val);
                } else {
                    return String.format("%.6g", val);
                }
            case VARIABLE:
                return (String) value;
            case SQRT:
                return "√(" + leftOperand.toString() + ")";
            case CBRT:
                return "∛(" + leftOperand.toString() + ")";
            case ADD:
                return "(" + leftOperand.toString() + " + " + rightOperand.toString() + ")";
            case SUBTRACT:
                return "(" + leftOperand.toString() + " - " + rightOperand.toString() + ")";
            case MULTIPLY:
                return "(" + leftOperand.toString() + " × " + rightOperand.toString() + ")";
            case DIVIDE:
                return "(" + leftOperand.toString() + " ÷ " + rightOperand.toString() + ")";
            case POWER:
                if (rightOperand.operationType == OperationType.CONSTANT) {
                    double exponent = (double) rightOperand.value;
                    if (Math.abs(exponent - 2) < 1e-10) {
                        return leftOperand.toString() + "²";
                    } else if (Math.abs(exponent - 3) < 1e-10) {
                        return leftOperand.toString() + "³";
                    }
                }
                return "(" + leftOperand.toString() + "^" + rightOperand.toString() + ")";
            default:
                throw new UnsupportedOperationException("Unsupported operation type: " + operationType);
        }
    }
}
