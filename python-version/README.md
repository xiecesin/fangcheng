# Equation Solver

A comprehensive Python library for solving quadratic, cubic, and quartic equations with detailed step-by-step solutions and verification.

## Features

- **Quadratic Equations**: Solves equations of the form `ax² + bx + c = 0`
- **Cubic Equations**: Solves equations of the form `ax³ + bx² + cx + d = 0` using Cardano's method
- **Quartic Equations**: Solves equations of the form `ax⁴ + bx³ + cx² + dx + e = 0` using numerical methods
- **Step-by-Step Solutions**: Shows detailed mathematical steps for each solution
- **Exact Expression Display**: Properly formats complex numbers and mathematical expressions
- **Solution Verification**: Automatically verifies solutions by substituting back into the original equation
- **Object-Oriented Design**: Clean, modular architecture following Python best practices

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/equation-solver.git
cd equation-solver

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Command Line Interface

Run the main program to interactively solve equations:

```bash
python src/main.py
```

The CLI will guide you through selecting the equation type and entering coefficients.

### Programmatic Usage

```python
from src.equation_solver import EquationSolver
from src.verifier import SolutionVerifier

# Solve a quadratic equation: x² - 5x + 6 = 0
solution = EquationSolver.solve_quadratic(1, -5, 6)

# Print detailed solution
EquationSolver.print_solution(solution)

# Verify the solution
verifier = SolutionVerifier()
verification_results = verifier.verify_quadratic(1, -5, 6, solution.roots)
verifier.print_verification_results(verification_results)
```

## Equation Types Supported

### Quadratic Equations
- Form: `ax² + bx + c = 0`
- Uses the quadratic formula: `x = (-b ± √(b² - 4ac)) / (2a)`
- Handles real and complex roots

### Cubic Equations
- Form: `ax³ + bx² + cx + d = 0`
- Uses Cardano's method with depression transformation
- Handles all cases: three real roots, one real + two complex, or multiple roots

### Quartic Equations
- Form: `ax⁴ + bx³ + cx² + dx + e = 0`
- Uses numerical methods for practical solution finding
- Returns all four roots (real and/or complex)

## Testing

Run the test suite to verify functionality:

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=src --cov-report=term-missing tests/
```

## Example Output

For the quadratic equation `x² - 5x + 6 = 0`:

```
Quadratic Equation Solution
==================================================

Original equation:
  Formula: x² - 5x + 6 = 0

Calculate discriminant:
  Formula: D = b² - 4ac = (-5)² - 4(1)(6)
  Result: D = 1

Apply quadratic formula:
  Formula: x = (-b ± √D) / (2a)
  Result: x₁ = 3, x₂ = 2

Final roots:
  x1 = 3
  x2 = 2

Verification Results
========================================
  Root 1: ✓ VALID
    Root value: 3.0
    Substituted value: 0.0
  Root 2: ✓ VALID
    Root value: 2.0
    Substituted value: 0.0

Overall: All solutions verified successfully!
```

## Dependencies

- **Python 3.8+**
- **NumPy** (for numerical computations in quartic solver)
- **pytest** (for testing)

## Development

This project follows PEP 8 coding standards and uses:
- **black** for code formatting
- **isort** for import sorting
- **ruff** for linting
- **mypy** for type checking

## License

MIT License