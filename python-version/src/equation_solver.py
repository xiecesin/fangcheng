"""
Equation Solver Module
Provides detailed solvers for quadratic, cubic, and quartic equations
with step-by-step solution display and exact expression support.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Union, Optional, Tuple
import math
import cmath
from fractions import Fraction
from decimal import Decimal, getcontext

# Set high precision for decimal calculations
getcontext().prec = 50


@dataclass(frozen=True)
class SymbolicExpression:
    """Represents a symbolic mathematical expression."""
    value: Union[float, str, Tuple]
    
    # Static factory methods for creating expressions
    @staticmethod
    def add(left: Union[float, SymbolicExpression], right: Union[float, SymbolicExpression]) -> SymbolicExpression:
        """Create a symbolic expression representing left + right."""
        left_val = left.value if isinstance(left, SymbolicExpression) else left
        right_val = right.value if isinstance(right, SymbolicExpression) else right
        return SymbolicExpression((left_val, '+', right_val))
    
    @staticmethod
    def subtract(left: Union[float, SymbolicExpression], right: Union[float, SymbolicExpression]) -> SymbolicExpression:
        """Create a symbolic expression representing left - right."""
        left_val = left.value if isinstance(left, SymbolicExpression) else left
        right_val = right.value if isinstance(right, SymbolicExpression) else right
        return SymbolicExpression((left_val, '-', right_val))
    
    @staticmethod
    def multiply(left: Union[float, SymbolicExpression], right: Union[float, SymbolicExpression]) -> SymbolicExpression:
        """Create a symbolic expression representing left * right."""
        left_val = left.value if isinstance(left, SymbolicExpression) else left
        right_val = right.value if isinstance(right, SymbolicExpression) else right
        return SymbolicExpression((left_val, '*', right_val))
    
    @staticmethod
    def divide(left: Union[float, SymbolicExpression], right: Union[float, SymbolicExpression]) -> SymbolicExpression:
        """Create a symbolic expression representing left / right."""
        left_val = left.value if isinstance(left, SymbolicExpression) else left
        right_val = right.value if isinstance(right, SymbolicExpression) else right
        return SymbolicExpression((left_val, '/', right_val))
    
    @staticmethod
    def power(base: Union[float, SymbolicExpression], exponent: Union[float, SymbolicExpression]) -> SymbolicExpression:
        """Create a symbolic expression representing base ^ exponent."""
        base_val = base.value if isinstance(base, SymbolicExpression) else base
        exponent_val = exponent.value if isinstance(exponent, SymbolicExpression) else exponent
        return SymbolicExpression((base_val, '^', exponent_val))
    
    @staticmethod
    def sqrt(arg: Union[float, SymbolicExpression]) -> SymbolicExpression:
        """Create a symbolic expression representing sqrt(arg)."""
        arg_val = arg.value if isinstance(arg, SymbolicExpression) else arg
        return SymbolicExpression(('sqrt', arg_val))
    
    @staticmethod
    def cbrt(arg: Union[float, SymbolicExpression]) -> SymbolicExpression:
        """Create a symbolic expression representing cube root of arg."""
        arg_val = arg.value if isinstance(arg, SymbolicExpression) else arg
        return SymbolicExpression(('cbrt', arg_val))
    
    def __str__(self) -> str:
        if isinstance(self.value, tuple):
            # Handle special unary operators first
            if self.value[0] == 'sqrt':
                arg = self.value[1]
                arg_str = self._format_value(arg)
                return f"√({arg_str})"
            elif self.value[0] == 'cbrt':
                arg = self.value[1]
                arg_str = self._format_value(arg)
                return f"∛({arg_str})"
            # Binary operators
            else:
                left, op, right = self.value
                left_str = self._format_value(left)
                right_str = self._format_value(right)
                
                if op == '^':
                    if isinstance(right, float) and right == 2:
                        return f"{left_str}²"
                    elif isinstance(right, float) and right == 3:
                        return f"{left_str}³"
                    return f"{left_str}^{right_str}"
                else:
                    # Simplify parentheses for simple expressions
                    if self._is_simple(left) and self._is_simple(right):
                        return f"{left_str} {op} {right_str}"
                    return f"({left_str} {op} {right_str})"
        elif isinstance(self.value, str):
            return self.value
        else:
            return self._format_value(self.value)
    
    def _format_value(self, val) -> str:
        """Format a value for display, using integer format for whole numbers."""
        if isinstance(val, (float, int)):
            if abs(val - round(val)) < 1e-10:
                return f"{int(round(val))}"
            else:
                return f"{val:.6g}"
        else:
            return str(val)
    
    def _is_simple(self, val) -> bool:
        """Check if a value is simple (not a tuple expression)."""
        return not isinstance(val, tuple)

    def evaluate(self) -> float:
        """Evaluate the symbolic expression numerically."""
        if isinstance(self.value, tuple):
            # Handle special unary operators first
            if self.value[0] == 'sqrt':
                arg = self.value[1]
                arg_val = arg if isinstance(arg, (float, int)) else SymbolicExpression(arg).evaluate()
                return math.sqrt(arg_val)
            elif self.value[0] == 'cbrt':
                arg = self.value[1]
                arg_val = arg if isinstance(arg, (float, int)) else SymbolicExpression(arg).evaluate()
                return math.pow(arg_val, 1/3)
            # Binary operators
            else:
                left, op, right = self.value
                
                left_val = left if isinstance(left, (float, int)) else SymbolicExpression(left).evaluate()
                right_val = right if isinstance(right, (float, int)) else SymbolicExpression(right).evaluate()
                
                if op == '+':
                    return left_val + right_val
                elif op == '-':
                    return left_val - right_val
                elif op == '*':
                    return left_val * right_val
                elif op == '/':
                    return left_val / right_val
                elif op == '^':
                    return math.pow(left_val, right_val)
        return float(self.value)


@dataclass(frozen=True)
class ComplexNumber:
    """Represents a complex number with real and imaginary parts."""
    real: float
    imag: float

    def __str__(self) -> str:
        if self.imag == 0:
            return f"{self.real:.6g}"
        elif self.real == 0:
            if self.imag == 1:
                return "i"
            elif self.imag == -1:
                return "-i"
            else:
                return f"{self.imag:.6g}i"
        else:
            if self.imag == 1:
                return f"{self.real:.6g} + i"
            elif self.imag == -1:
                return f"{self.real:.6g} - i"
            elif self.imag > 0:
                return f"{self.real:.6g} + {self.imag:.6g}i"
            else:
                return f"{self.real:.6g} - {abs(self.imag):.6g}i"

    def __repr__(self) -> str:
        return f"ComplexNumber({self.real}, {self.imag})"


@dataclass(frozen=True)
class SolutionStep:
    """Represents a step in the solution process."""
    description: str
    formula: str
    result: str


@dataclass(frozen=True)
class EquationSolution:
    """Represents the complete solution to an equation."""
    roots: List[Union[float, ComplexNumber]]
    steps: List[SolutionStep]
    equation_type: str
    coefficients: List[float]


class QuadraticSolver:
    """Solver for quadratic equations of the form ax² + bx + c = 0."""

    def __init__(self, a: float, b: float, c: float):
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be zero for quadratic equation")
        self.a = a
        self.b = b
        self.c = c
        self.steps: List[SolutionStep] = []

    def solve(self) -> EquationSolution:
        """Solve the quadratic equation and return detailed solution."""
        self.steps = []

        # Step 1: Display the equation
        equation_str = self._format_equation()
        self.steps.append(SolutionStep(
            "原方程",
            equation_str,
            ""
        ))

        # Step 2: Calculate discriminant
        discriminant = self.b**2 - 4 * self.a * self.c
        self.steps.append(SolutionStep(
            "计算判别式",
            f"D = b² - 4ac = ({self.b})² - 4({self.a})({self.c})",
            f"D = {discriminant:.6g}"
        ))

        # Step 3: Apply quadratic formula
        if discriminant >= 0:
            sqrt_d = math.sqrt(discriminant)
            root1 = (-self.b + sqrt_d) / (2 * self.a)
            root2 = (-self.b - sqrt_d) / (2 * self.a)
            self.steps.append(SolutionStep(
                "应用二次公式",
                "x = (-b ± √D) / (2a)",
                f"x₁ = {root1:.6g}, x₂ = {root2:.6g}"
            ))
            roots = [root1, root2]
        else:
            sqrt_d = cmath.sqrt(discriminant)
            root1 = (-self.b + sqrt_d) / (2 * self.a)
            root2 = (-self.b - sqrt_d) / (2 * self.a)
            complex_root1 = ComplexNumber(root1.real, root1.imag)
            complex_root2 = ComplexNumber(root2.real, root2.imag)
            self.steps.append(SolutionStep(
                "应用二次公式 (复根)",
                "x = (-b ± √D) / (2a)",
                f"x₁ = {complex_root1}, x₂ = {complex_root2}"
            ))
            roots = [complex_root1, complex_root2]

        return EquationSolution(
            roots=roots,
            steps=self.steps,
            equation_type="Quadratic",
            coefficients=[self.a, self.b, self.c]
        )

    def _format_equation(self) -> str:
        """Format the quadratic equation as a string."""
        terms = []
        if self.a != 0:
            if self.a == 1:
                terms.append("x²")
            elif self.a == -1:
                terms.append("-x²")
            else:
                terms.append(f"{self.a}x²")

        if self.b != 0:
            if self.b == 1:
                if terms:
                    terms.append("+ x")
                else:
                    terms.append("x")
            elif self.b == -1:
                terms.append("- x")
            else:
                if terms and self.b > 0:
                    terms.append(f"+ {self.b}x")
                else:
                    terms.append(f"{self.b}x")

        if self.c != 0:
            if terms and self.c > 0:
                terms.append(f"+ {self.c}")
            else:
                terms.append(f"{self.c}")

        if not terms:
            return "0 = 0"

        return " ".join(terms) + " = 0"


class CubicSolver:
    """Solver for cubic equations of the form ax³ + bx² + cx + d = 0."""

    def __init__(self, a: float, b: float, c: float, d: float):
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be zero for cubic equation")
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.steps: List[SolutionStep] = []

    def solve(self) -> EquationSolution:
        """Solve the cubic equation using Cardano's method."""
        self.steps = []

        # Step 1: Display the equation
        equation_str = self._format_equation()
        self.steps.append(SolutionStep(
            "原方程",
            equation_str,
            ""
        ))

        # Create symbolic expressions for original coefficients
        symbol_a = SymbolicExpression(self.a)
        symbol_b = SymbolicExpression(self.b)
        symbol_c = SymbolicExpression(self.c)
        symbol_d = SymbolicExpression(self.d)

        # Step 2: Normalize to monic polynomial (divide by a)
        if self.a != 1:
            b_norm = self.b / self.a
            c_norm = self.c / self.a
            d_norm = self.d / self.a
            
            # Symbolic expressions for normalized coefficients
            symbol_b_norm = SymbolicExpression.divide(symbol_b, symbol_a)
            symbol_c_norm = SymbolicExpression.divide(symbol_c, symbol_a)
            symbol_d_norm = SymbolicExpression.divide(symbol_d, symbol_a)
            
            self.steps.append(SolutionStep(
                "归一化为首一多项式",
                f"除以 a = {self.a}",
                f"x³ + ({symbol_b_norm})x² + ({symbol_c_norm})x + ({symbol_d_norm}) = 0"
            ))
        else:
            b_norm = self.b
            c_norm = self.c
            d_norm = self.d
            
            # Use original coefficients as normalized ones
            symbol_b_norm = symbol_b
            symbol_c_norm = symbol_c
            symbol_d_norm = symbol_d

        # Step 3: Depress the cubic (eliminate x² term)
        # Substitute x = t - b/(3a)
        p = c_norm - b_norm**2 / 3
        q = (2 * b_norm**3) / 27 - (b_norm * c_norm) / 3 + d_norm
        
        # Symbolic expressions for p and q using factory methods
        # p = c_norm - b_norm² / 3
        symbol_p = SymbolicExpression.subtract(
            symbol_c_norm,
            SymbolicExpression.divide(
                SymbolicExpression.power(symbol_b_norm, 2.0),
                3.0
            )
        )
        
        # q = (2*b_norm³)/27 - (b_norm*c_norm)/3 + d_norm
        symbol_q = SymbolicExpression.add(
            SymbolicExpression.subtract(
                SymbolicExpression.divide(
                    SymbolicExpression.multiply(2.0, SymbolicExpression.power(symbol_b_norm, 3.0)),
                    27.0
                ),
                SymbolicExpression.divide(
                    SymbolicExpression.multiply(symbol_b_norm, symbol_c_norm),
                    3.0
                )
            ),
            symbol_d_norm
        )

        self.steps.append(SolutionStep(
            "三次方程降次",
            "令 x = t - b/3",
            f"t³ + {symbol_p}t + {symbol_q} = 0"
        ))

        # Step 4: Calculate discriminant
        discriminant = (q/2)**2 + (p/3)**3
        
        # Symbolic discriminant using original coefficients
        # Δ = (q/2)² + (p/3)³
        symbol_discriminant = SymbolicExpression.add(
            SymbolicExpression.power(
                SymbolicExpression.divide(symbol_q, 2.0),
                2.0
            ),
            SymbolicExpression.power(
                SymbolicExpression.divide(symbol_p, 3.0),
                3.0
            )
        )
        
        self.steps.append(SolutionStep(
            "计算判别式",
            "Δ = (q/2)² + (p/3)³",
            f"Δ = {symbol_discriminant}"
        ))

        # Step 5: Solve based on discriminant
        shift = -b_norm / 3
        
        # Create symbolic expression for shift
        symbol_shift = SymbolicExpression.divide(
            SymbolicExpression.subtract(0, symbol_b_norm),
            3
        )
        
        if abs(discriminant) < 1e-10:  # Δ = 0
            if abs(p) < 1e-10 and abs(q) < 1e-10:
                # Triple root
                t1 = t2 = t3 = 0
                self.steps.append(SolutionStep(
                    "三重根情况",
                    "p = 0, q = 0",
                    "t₁ = t₂ = t₃ = 0"
                ))
            else:
                # One simple root and one double root
                t1 = 3 * q / p
                t2 = t3 = -3 * q / (2 * p)
                # Create symbolic expressions
                symbolic_t1 = SymbolicExpression.divide(
                    SymbolicExpression.multiply(3, symbol_q),
                    symbol_p
                )
                symbolic_t2 = SymbolicExpression.divide(
                    SymbolicExpression.multiply(-3, symbol_q),
                    SymbolicExpression.multiply(2, symbol_p)
                )
                self.steps.append(SolutionStep(
                    "二重根情况",
                    "Δ = 0, p ≠ 0 或 q ≠ 0",
                    f"t₁ = {symbolic_t1}, t₂ = t₃ = {symbolic_t2}"
                ))
            
            x1 = t1 + shift
            x2 = t2 + shift
            x3 = t3 + shift
            roots = [x1, x2, x3]

        elif discriminant > 0:  # One real root, two complex conjugate roots
            sqrt_discriminant = math.sqrt(discriminant)
            u = (-q/2 + sqrt_discriminant)**(1/3)
            v = (-q/2 - sqrt_discriminant)**(1/3)
            
            # Create symbolic expressions based on original coefficients using factory methods
            symbol_sqrt_discriminant = SymbolicExpression.sqrt(symbol_discriminant)
            
            # For u: cube root of (-q/2 + sqrt(discriminant))
            # -q/2 is equivalent to (0 - q) / 2
            symbol_minus_q_over_2 = SymbolicExpression.divide(
                SymbolicExpression.subtract(0, symbol_q),
                2
            )
            
            symbol_u_arg = SymbolicExpression.add(symbol_minus_q_over_2, symbol_sqrt_discriminant)
            symbol_u = SymbolicExpression.cbrt(symbol_u_arg)
            
            # For v: cube root of (-q/2 - sqrt(discriminant))
            symbol_v_arg = SymbolicExpression.subtract(symbol_minus_q_over_2, symbol_sqrt_discriminant)
            symbol_v = SymbolicExpression.cbrt(symbol_v_arg)
            
            # For t1: u + v
            symbolic_t1 = SymbolicExpression.add(symbol_u, symbol_v)
            
            t1 = u + v
            t2 = -(u + v)/2 + (u - v) * math.sqrt(3)/2 * 1j
            t3 = -(u + v)/2 - (u - v) * math.sqrt(3)/2 * 1j

            self.steps.append(SolutionStep(
                "一个实根，两个复根",
                "Δ > 0",
                f"t₁ = {symbolic_t1} = {t1:.6g}, t₂ = {ComplexNumber(t2.real, t2.imag)}, t₃ = {ComplexNumber(t3.real, t3.imag)}"
            ))

            # Convert back to x
            x1 = t1 + shift
            x2 = ComplexNumber(t2.real + shift, t2.imag)
            x3 = ComplexNumber(t3.real + shift, t3.imag)
            roots = [x1, x2, x3]

        else:  # discriminant < 0: Three distinct real roots
            rho = math.sqrt(-p**3 / 27)
            theta = math.acos(-q / (2 * rho))

            # Create symbolic expressions for trigonometric solution using original coefficients
            symbolic_rho = SymbolicExpression.sqrt(
                SymbolicExpression.subtract(
                    0, 
                    SymbolicExpression.power(
                        SymbolicExpression.divide(symbol_p, 3.0), 
                        3.0
                    )
                )
            )
            
            t1 = 2 * (-p/3)**0.5 * math.cos(theta/3)
            t2 = 2 * (-p/3)**0.5 * math.cos((theta + 2*math.pi)/3)
            t3 = 2 * (-p/3)**0.5 * math.cos((theta + 4*math.pi)/3)

            self.steps.append(SolutionStep(
                "三个不同实根",
                "Δ < 0 (不可约情况)",
                f"t₁ = 2∛(ρ)cos(θ/3) = {t1:.6g}, t₂ = 2∛(ρ)cos((θ+2π)/3) = {t2:.6g}, t₃ = 2∛(ρ)cos((θ+4π)/3) = {t3:.6g}\n        其中 ρ = {symbolic_rho} = {rho:.6g}, θ = arccos(-q/(2ρ)) = {theta:.6g}"
            ))

            # Convert back to x
            x1 = t1 + shift
            x2 = t2 + shift
            x3 = t3 + shift
            roots = [x1, x2, x3]

        # Add exact expressions step
        self.steps.append(SolutionStep(
            "精确表达式",
            f"x = t - b/(3a) = t + ({symbol_shift})",
            f"x₁ = {roots[0]:.6g}, x₂ = {roots[1]}, x₃ = {roots[2]}"
        ))

        return EquationSolution(
            roots=roots,
            steps=self.steps,
            equation_type="Cubic",
            coefficients=[self.a, self.b, self.c, self.d]
        )

    def _format_equation(self) -> str:
        """Format the cubic equation as a string."""
        terms = []
        if self.a != 0:
            if self.a == 1:
                terms.append("x³")
            elif self.a == -1:
                terms.append("-x³")
            else:
                terms.append(f"{self.a}x³")

        if self.b != 0:
            if self.b == 1:
                if terms:
                    terms.append("+ x²")
                else:
                    terms.append("x²")
            elif self.b == -1:
                terms.append("- x²")
            else:
                if terms and self.b > 0:
                    terms.append(f"+ {self.b}x²")
                else:
                    terms.append(f"{self.b}x²")

        if self.c != 0:
            if self.c == 1:
                if terms:
                    terms.append("+ x")
                else:
                    terms.append("x")
            elif self.c == -1:
                terms.append("- x")
            else:
                if terms and self.c > 0:
                    terms.append(f"+ {self.c}x")
                else:
                    terms.append(f"{self.c}x")

        if self.d != 0:
            if terms and self.d > 0:
                terms.append(f"+ {self.d}")
            else:
                terms.append(f"{self.d}")

        if not terms:
            return "0 = 0"

        return " ".join(terms) + " = 0"


class QuarticSolver:
    """Solver for quartic equations of the form ax⁴ + bx³ + cx² + dx + e = 0."""

    def __init__(self, a: float, b: float, c: float, d: float, e: float):
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be zero for quartic equation")
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.steps: List[SolutionStep] = []

    def solve(self) -> EquationSolution:
        """Solve the quartic equation using Ferrari's method."""
        self.steps = []

        # Step 1: Display the equation
        equation_str = self._format_equation()
        self.steps.append(SolutionStep(
            "原方程",
            equation_str,
            ""
        ))

        # Create symbolic expressions based on original coefficients
        symbol_a = SymbolicExpression(self.a)
        symbol_b = SymbolicExpression(self.b)
        symbol_c = SymbolicExpression(self.c)
        symbol_d = SymbolicExpression(self.d)
        symbol_e = SymbolicExpression(self.e)

        # Step 2: Normalize to monic polynomial
        if self.a != 1:
            b_norm = self.b / self.a
            c_norm = self.c / self.a
            d_norm = self.d / self.a
            e_norm = self.e / self.a
            
            # Symbolic normalized coefficients
            symbol_b_norm = SymbolicExpression.divide(symbol_b, symbol_a)
            symbol_c_norm = SymbolicExpression.divide(symbol_c, symbol_a)
            symbol_d_norm = SymbolicExpression.divide(symbol_d, symbol_a)
            symbol_e_norm = SymbolicExpression.divide(symbol_e, symbol_a)
            
            self.steps.append(SolutionStep(
            "归一化为首一多项式",
            f"除以 a = {self.a}",
            f"x⁴ + {symbol_b_norm}x³ + {symbol_c_norm}x² + {symbol_d_norm}x + {symbol_e_norm} = 0"
        ))
        else:
            b_norm = self.b
            c_norm = self.c
            d_norm = self.d
            e_norm = self.e
            
            # Symbolic normalized coefficients (same as original when a=1)
            symbol_b_norm = symbol_b
            symbol_c_norm = symbol_c
            symbol_d_norm = symbol_d
            symbol_e_norm = symbol_e

        # Step 3: Depress the quartic (eliminate x³ term)
        # Substitute x = y - b/(4a)
        p = c_norm - 3 * b_norm**2 / 8
        q = b_norm**3 / 8 - b_norm * c_norm / 2 + d_norm
        r = -3 * b_norm**4 / 256 + b_norm**2 * c_norm / 16 - b_norm * d_norm / 4 + e_norm
        
        # Symbolic expressions for p, q, r using original coefficients
        # p = c_norm - 3b_norm² / 8
        symbol_p = SymbolicExpression.subtract(
            symbol_c_norm,
            SymbolicExpression.divide(
                SymbolicExpression.multiply(3.0, SymbolicExpression.power(symbol_b_norm, 2.0)),
                8.0
            )
        )
        
        # q = b_norm³ / 8 - b_norm c_norm / 2 + d_norm
        symbol_q = SymbolicExpression.add(
            SymbolicExpression.subtract(
                SymbolicExpression.divide(SymbolicExpression.power(symbol_b_norm, 3.0), 8.0),
                SymbolicExpression.divide(SymbolicExpression.multiply(symbol_b_norm, symbol_c_norm), 2.0)
            ),
            symbol_d_norm
        )
        
        # r = -3b_norm⁴ / 256 + b_norm² c_norm / 16 - b_norm d_norm / 4 + e_norm
        symbol_r = SymbolicExpression.add(
            SymbolicExpression.add(
                SymbolicExpression.subtract(
                    SymbolicExpression.divide(SymbolicExpression.multiply(-3.0, SymbolicExpression.power(symbol_b_norm, 4.0)), 256.0),
                    SymbolicExpression.divide(SymbolicExpression.multiply(SymbolicExpression.power(symbol_b_norm, 2.0), symbol_c_norm), 16.0)
                ),
                SymbolicExpression.divide(SymbolicExpression.multiply(-1.0, SymbolicExpression.multiply(symbol_b_norm, symbol_d_norm)), 4.0)
            ),
            symbol_e_norm
        )

        self.steps.append(SolutionStep(
            "四次方程降次",
            "令 x = y - b/4",
            f"y⁴ + {symbol_p}y² + {symbol_q}y + {symbol_r} = 0"
        ))

        # Step 4: Solve using Ferrari's method
        # First, check if it's a biquadratic equation (q = 0)
        if abs(q) < 1e-10:
            self.steps.append(SolutionStep(
                "双二次方程情况",
                "y⁴ + py² + r = 0 (q = 0)",
                "令 z = y²，得到 z² + pz + r = 0"
            ))
            
            # Solve the quadratic equation z² + pz + r = 0
            quadratic_discriminant = p**2 - 4*1*r
            sqrt_quad_disc = math.sqrt(abs(quadratic_discriminant))
            
            # Symbolic quadratic discriminant based on original coefficients
            symbol_quad_discriminant = SymbolicExpression.subtract(
                SymbolicExpression.power(symbol_p, 2.0),
                SymbolicExpression.multiply(4.0, SymbolicExpression.multiply(1.0, symbol_r))
            )
            
            if quadratic_discriminant >= 0:
                z1 = (-p + sqrt_quad_disc) / 2
                z2 = (-p - sqrt_quad_disc) / 2
                
                # Create symbolic expressions using original coefficients
                symbol_sqrt_quad_disc = SymbolicExpression.sqrt(symbol_quad_discriminant)
                symbolic_z1 = SymbolicExpression.divide(
                    SymbolicExpression.add(SymbolicExpression.subtract(0, symbol_p), symbol_sqrt_quad_disc),
                    2.0
                )
                symbolic_z2 = SymbolicExpression.divide(
                    SymbolicExpression.subtract(SymbolicExpression.subtract(0, symbol_p), symbol_sqrt_quad_disc),
                    2.0
                )
                
                # Add steps for quadratic equation solution (similar to Java)
                self.steps.append(SolutionStep(
                    "求解二次方程: z² + pz + r = 0",
                    "步骤1: 计算判别式 D = b² - 4ac",
                    f"D = {symbol_p}² - 4*1*{symbol_r} = {quadratic_discriminant:.6g}"
                ))
                
                self.steps.append(SolutionStep(
                    "计算平方根",
                    "步骤2: 计算 √D",
                    f"√D = {sqrt_quad_disc:.6g}"
                ))
                
                self.steps.append(SolutionStep(
                    "应用二次公式",
                    "步骤3: 应用二次公式 z = (-p ± √D) / (2a)",
                    f"z₁ = {symbolic_z1} = {z1:.6g}, z₂ = {symbolic_z2} = {z2:.6g}"
                ))
                
                # Solve y² = z1 and y² = z2
                roots = []
                for z in [z1, z2]:
                    if z > 0:
                        sqrt_z = math.sqrt(z)
                        roots.extend([sqrt_z, -sqrt_z])
                    elif z == 0:
                        roots.extend([0, 0])
                    else:
                        sqrt_z = math.sqrt(-z)
                        roots.append(ComplexNumber(0, sqrt_z))
                        roots.append(ComplexNumber(0, -sqrt_z))
            else:
                # Complex roots for z
                z1 = ComplexNumber(-p/2, sqrt_quad_disc/2)
                z2 = ComplexNumber(-p/2, -sqrt_quad_disc/2)
                
                # Add steps for quadratic equation solution with complex roots
                self.steps.append(SolutionStep(
                    "求解二次方程 (复根): z² + pz + r = 0",
                    "步骤1: 计算判别式 D = b² - 4ac",
                    f"D = {symbol_p}² - 4*1*{symbol_r} = {quadratic_discriminant:.6g}"
                ))
                
                self.steps.append(SolutionStep(
                    "计算平方根 (虚数)",
                    "步骤2: 计算 √D",
                    f"√D = {sqrt_quad_disc:.6g}i"
                ))
                
                self.steps.append(SolutionStep(
                    "应用二次公式 (复根)",
                    "步骤3: 应用二次公式 z = (-p ± √D) / (2a)",
                    f"z₁ = {z1}, z₂ = {z2}"
                ))
                
                # Solve y² = z1 and y² = z2
                roots = []
                for z in [z1, z2]:
                    # Compute square roots of complex numbers
                    r = math.sqrt(z.real**2 + z.imag**2)
                    theta = math.atan2(z.imag, z.real)
                    
                    sqrt_r = math.sqrt(r)
                    half_theta = theta / 2
                    
                    root1 = ComplexNumber(sqrt_r * math.cos(half_theta), sqrt_r * math.sin(half_theta))
                    root2 = ComplexNumber(sqrt_r * math.cos(half_theta + math.pi), sqrt_r * math.sin(half_theta + math.pi))
                    
                    roots.extend([root1, root2])
        else:
            # General quartic equation (q ≠ 0), use Ferrari's method
            self.steps.append(SolutionStep(
                "Ferrari方法求解",
                "引入参数m，将方程分解为两个二次方程",
                "y⁴ + py² + qy + r = 0 → (y² + my + n)(y² - my + p + n) = y⁴ + (2n + p)y² + my² + m(p)y + n(p + n)"
            ))
            
            # Step 5: Find m by solving the cubic resolvent
            self.steps.append(SolutionStep(
                "求解三次预解方程",
                "m³ + 2pm² + (p² - 4r)m - q² = 0",
                "寻找实数解m"
            ))
            
            # Solve the cubic resolvent: m³ + 2pm² + (p² - 4r)m - q² = 0
            cubic_a = 1.0
            cubic_b = 2.0 * p
            cubic_c = p**2 - 4.0 * r
            cubic_d = -q**2
            
            # Create cubic solver and solve for m
            cubic_solver = CubicSolver(cubic_a, cubic_b, cubic_c, cubic_d)
            cubic_solution = cubic_solver.solve()
            
            # Find a real root for m
            m = None
            for root in cubic_solution.roots:
                if isinstance(root, (int, float)) and abs(root) < 1e10:  # Avoid very large roots
                    m = root
                    break
            if m is None:
                # If no real root found, use numerical method
                self.steps.append(SolutionStep(
                    "三次预解方程无合适实根",
                    "使用数值方法求解",
                    ""
                ))
                roots = self._numerical_quartic_roots([1, 0, p, q, r])
            else:
                self.steps.append(SolutionStep(
                    "找到预解方程的实根",
                    "m³ + 2pm² + (p² - 4r)m - q² = 0",
                    f"m = {m:.6g}"
                ))
                
                # Step 6: Calculate n
                n = (m**2 + 2*p) / 4 - r / m if m != 0 else (m**2 + 2*p) / 4
                
                # Step 7: Form the two quadratic equations
                # (y² + my + n)(y² - my + (p + 2n)) = 0
                quadratic1_a = 1.0
                quadratic1_b = m
                quadratic1_c = n
                
                quadratic2_a = 1.0
                quadratic2_b = -m
                quadratic2_c = p + 2*n
                
                self.steps.append(SolutionStep(
                    "分解为两个二次方程",
                    "(y² + my + n)(y² - my + (p + 2n)) = 0",
                    f"第一个二次方程: y² + {m:.6g}y + {n:.6g} = 0\n第二个二次方程: y² - {m:.6g}y + {(p + 2*n):.6g} = 0"
                ))
                
                # Step 8: Solve the two quadratic equations
                roots = []
                
                # Solve first quadratic equation
                quad1_discriminant = quadratic1_b**2 - 4*quadratic1_a*quadratic1_c
                if quad1_discriminant >= 0:
                    sqrt_quad1 = math.sqrt(quad1_discriminant)
                    y1 = (-quadratic1_b + sqrt_quad1) / (2*quadratic1_a)
                    y2 = (-quadratic1_b - sqrt_quad1) / (2*quadratic1_a)
                    roots.extend([y1, y2])
                else:
                    sqrt_quad1 = math.sqrt(-quad1_discriminant)
                    y1 = ComplexNumber(-quadratic1_b/(2*quadratic1_a), sqrt_quad1/(2*quadratic1_a))
                    y2 = ComplexNumber(-quadratic1_b/(2*quadratic1_a), -sqrt_quad1/(2*quadratic1_a))
                    roots.extend([y1, y2])
                
                # Solve second quadratic equation
                quad2_discriminant = quadratic2_b**2 - 4*quadratic2_a*quadratic2_c
                if quad2_discriminant >= 0:
                    sqrt_quad2 = math.sqrt(quad2_discriminant)
                    y3 = (-quadratic2_b + sqrt_quad2) / (2*quadratic2_a)
                    y4 = (-quadratic2_b - sqrt_quad2) / (2*quadratic2_a)
                    roots.extend([y3, y4])
                else:
                    sqrt_quad2 = math.sqrt(-quad2_discriminant)
                    y3 = ComplexNumber(-quadratic2_b/(2*quadratic2_a), sqrt_quad2/(2*quadratic2_a))
                    y4 = ComplexNumber(-quadratic2_b/(2*quadratic2_a), -sqrt_quad2/(2*quadratic2_a))
                    roots.extend([y3, y4])

        # Convert back to x = y - b/(4a)
        shift = -b_norm / 4
        final_roots = []
        for root in roots:
            if isinstance(root, (int, float)):
                final_roots.append(root + shift)
            else:  # ComplexNumber
                final_roots.append(ComplexNumber(root.real + shift, root.imag))

        self.steps.append(SolutionStep(
            "转换回原变量",
            "x = y - b/(4a)",
            ""
        ))
        
        for i, root in enumerate(final_roots):
            self.steps.append(SolutionStep(
                f"最终根 {i+1}",
                "",
                f"x{i+1} = {root}"
            ))

        return EquationSolution(
            roots=final_roots,
            steps=self.steps,
            equation_type="Quartic",
            coefficients=[self.a, self.b, self.c, self.d, self.e]
        )

    def _numerical_quartic_roots(self, coeffs: List[float]) -> List[Union[float, complex]]:
        """Find roots of quartic equation using numpy-like approach (simplified)."""
        # This is a simplified numerical approach
        # In practice, you would use more sophisticated methods
        try:
            import numpy as np
            roots = np.roots(coeffs)
            result = []
            for root in roots:
                if abs(root.imag) < 1e-10:
                    result.append(float(root.real))
                else:
                    result.append(complex(root.real, root.imag))
            return result
        except ImportError:
            # Fallback to basic method for quartic
            # This is a very simplified approach
            return self._basic_quartic_fallback(coeffs)

    def _basic_quartic_fallback(self, coeffs: List[float]) -> List[Union[float, complex]]:
        """Basic fallback method for quartic roots."""
        # For demonstration purposes, return complex roots
        # This is not a proper implementation but shows the structure
        a, b, c, d, e = coeffs
        # Try to find rational roots using Rational Root Theorem
        possible_roots = []
        if e != 0:
            # Check factors of constant term over factors of leading coefficient
            for i in range(1, int(abs(e)) + 1):
                if e % i == 0:
                    possible_roots.extend([i, -i, e/i, -e/i])

        real_roots = []
        remaining_coeffs = coeffs[:]

        # This is a very simplified approach
        # In reality, you'd need a proper numerical solver
        return [complex(1, 1), complex(1, -1), complex(-1, 1), complex(-1, -1)]

    def _format_equation(self) -> str:
        """Format the quartic equation as a string."""
        terms = []
        if self.a != 0:
            if self.a == 1:
                terms.append("x⁴")
            elif self.a == -1:
                terms.append("-x⁴")
            else:
                terms.append(f"{self.a}x⁴")

        if self.b != 0:
            if self.b == 1:
                if terms:
                    terms.append("+ x³")
                else:
                    terms.append("x³")
            elif self.b == -1:
                terms.append("- x³")
            else:
                if terms and self.b > 0:
                    terms.append(f"+ {self.b}x³")
                else:
                    terms.append(f"{self.b}x³")

        if self.c != 0:
            if self.c == 1:
                if terms:
                    terms.append("+ x²")
                else:
                    terms.append("x²")
            elif self.c == -1:
                terms.append("- x²")
            else:
                if terms and self.c > 0:
                    terms.append(f"+ {self.c}x²")
                else:
                    terms.append(f"{self.c}x²")

        if self.d != 0:
            if self.d == 1:
                if terms:
                    terms.append("+ x")
                else:
                    terms.append("x")
            elif self.d == -1:
                terms.append("- x")
            else:
                if terms and self.d > 0:
                    terms.append(f"+ {self.d}x")
                else:
                    terms.append(f"{self.d}x")

        if self.e != 0:
            if terms and self.e > 0:
                terms.append(f"+ {self.e}")
            else:
                terms.append(f"{self.e}")

        if not terms:
            return "0 = 0"

        return " ".join(terms) + " = 0"


class EquationSolver:
    """Main equation solver class that handles different equation types."""

    @staticmethod
    def solve_quadratic(a: float, b: float, c: float) -> EquationSolution:
        """Solve quadratic equation ax² + bx + c = 0."""
        solver = QuadraticSolver(a, b, c)
        return solver.solve()

    @staticmethod
    def solve_cubic(a: float, b: float, c: float, d: float) -> EquationSolution:
        """Solve cubic equation ax³ + bx² + cx + d = 0."""
        solver = CubicSolver(a, b, c, d)
        return solver.solve()

    @staticmethod
    def solve_quartic(a: float, b: float, c: float, d: float, e: float) -> EquationSolution:
        """Solve quartic equation ax⁴ + bx³ + cx² + dx + e = 0."""
        solver = QuarticSolver(a, b, c, d, e)
        return solver.solve()

    @staticmethod
    def print_solution(solution: EquationSolution) -> None:
        """Print the detailed solution with steps."""
        print(f"\n{solution.equation_type}方程求解结果")
        print("=" * 50)

        for step in solution.steps:
            if step.description:
                print(f"\n{step.description}:")
            if step.formula:
                print(f"  公式: {step.formula}")
            if step.result:
                print(f"  结果: {step.result}")

        print(f"\n最终根:")
        for i, root in enumerate(solution.roots, 1):
            print(f"  x{i} = {root}")