# Java Equation Solver

A comprehensive Java library for solving polynomial equations of degrees 2, 3, and 4 (quadratic, cubic, and quartic equations). The solver provides detailed step-by-step solutions and includes verification functionality to ensure correctness.

## Features

- **Quadratic Solver**: Solves equations of the form `ax² + bx + c = 0`
- **Cubic Solver**: Solves equations of the form `ax³ + bx² + cx + d = 0` using Cardano's method
- **Quartic Solver**: Solves equations of the form `ax⁴ + bx³ + cx² + dx + e = 0` using Ferrari's method
- **Complex Number Support**: Handles both real and complex roots seamlessly
- **Step-by-Step Solutions**: Shows detailed mathematical steps for each solution
- **Verification**: Automatically verifies solutions by substituting back into the original equation
- **Multiple Test Cases**: Includes comprehensive test cases covering various scenarios

## Mathematical Methods Used

### Quadratic Equations
Uses the standard quadratic formula: `x = (-b ± √(b² - 4ac)) / (2a)`

### Cubic Equations
Uses Cardano's method:
1. Normalize to monic polynomial
2. Depress the cubic (eliminate x² term)
3. Solve using the depressed cubic formula
4. Handle all cases: three real roots, one real + two complex, or multiple roots

### Quartic Equations
Uses Ferrari's method:
1. Normalize to monic polynomial
2. Depress the quartic (eliminate x³ term)
3. Solve the cubic resolvent
4. Factor into two quadratics and solve

## Installation

### Prerequisites
- Java 11 or higher
- Maven 3.6 or higher (for building)

### Building the Project
```bash
# Clone the repository
cd /path/to/equation-solver

# Build the project
mvn clean package

# Run the application
mvn exec:java -Prun
# or
java -jar target/equation-solver-1.0.0.jar
```

## Usage Examples

### Quadratic Equation
```java
// Solve x² - 5x + 6 = 0
Complex[] roots = QuadraticSolver.solve(1, -5, 6);
```

### Cubic Equation
```java
// Solve x³ - 6x² + 11x - 6 = 0
Complex[] roots = CubicSolver.solve(1, -6, 11, -6);
```

### Quartic Equation
```java
// Solve x⁴ - 5x² + 4 = 0
Complex[] roots = QuarticSolver.solve(1, 0, -5, 0, 4);
```

### Verification
```java
// Verify quadratic solutions
boolean verified = QuadraticVerifier.verify(1, -5, 6, roots);

// Verify cubic solutions
boolean verified = CubicVerifier.verify(1, -6, 11, -6, roots);

// Verify quartic solutions
boolean verified = QuarticVerifier.verify(1, 0, -5, 0, 4, roots);
```

## Test Cases Included

The main application includes the following test cases:

### Quadratic Tests
1. `x² - 5x + 6 = 0` → roots: 2, 3
2. `x² + 1 = 0` → roots: i, -i
3. `x² - 4x + 4 = 0` → repeated root: 2

### Cubic Tests
1. `x³ - 6x² + 11x - 6 = 0` → roots: 1, 2, 3
2. `x³ - 1 = 0` → roots: 1, -0.5±0.866i
3. `x³ - 3x² + 3x - 1 = 0` → triple root: 1

### Quartic Tests
1. `x⁴ - 5x² + 4 = 0` → roots: ±1, ±2
2. `x⁴ - 10x³ + 35x² - 50x + 24 = 0` → roots: 1, 2, 3, 4
3. `x⁴ + 1 = 0` → four complex roots

## Project Structure

```
src/
├── main/
│   └── java/
│       └── com/
│           └── equation/
│               ├── Complex.java          # Complex number implementation
│               ├── QuadraticSolver.java  # Quadratic equation solver
│               ├── CubicSolver.java      # Cubic equation solver
│               ├── QuarticSolver.java    # Quartic equation solver
│               ├── Main.java             # Main application with test cases
│               └── verifier/             # Verification classes
│                   ├── QuadraticVerifier.java
│                   ├── CubicVerifier.java
│                   └── QuarticVerifier.java
pom.xml                                   # Maven build configuration
README.md                                 # This documentation
```

## Accuracy and Limitations

- **Precision**: Uses double-precision floating point arithmetic
- **Tolerance**: Verification uses tolerance of 1e-8 for floating-point comparisons
- **Edge Cases**: Handles special cases like multiple roots, complex roots, and degenerate cases
- **Performance**: Optimized for clarity and educational purposes rather than extreme performance

## License

This project is open source and available under the MIT License.

## Author

Created as part of the Fangcheng (方程) equation solving project.