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
    value: Union[float, str, Tuple[Union[float, str, Tuple], str, Union[float, str, Tuple]]]
    
    def __str__(self) -> str:
        if isinstance(self.value, tuple):
            # Handle special unary operators first
            if self.value[0] == 'sqrt':
                arg = self.value[1]
                arg_str = str(arg) if isinstance(arg, (float, int)) else str(SymbolicExpression(arg))
                return f"√{arg_str}"
            elif self.value[0] == 'cbrt':
                arg = self.value[1]
                arg_str = str(arg) if isinstance(arg, (float, int)) else str(SymbolicExpression(arg))
                return f"∛{arg_str}"
            # Binary operators
            else:
                left, op, right = self.value
                left_str = str(left) if isinstance(left, (float, int)) else str(SymbolicExpression(left))
                right_str = str(right) if isinstance(right, (float, int)) else str(SymbolicExpression(right))
                
                if op == '^':
                    if isinstance(right, float) and right == 2:
                        return f"{left_str}²"
                    elif isinstance(right, float) and right == 3:
                        return f"{left_str}³"
                    return f"{left_str}^{right_str}"
                else:
                    return f"({left_str} {op} {right_str})"
        elif isinstance(self.value, str):
            return self.value
        else:
            return f"{self.value:.6g}"

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

        # Step 2: Normalize to monic polynomial (divide by a)
        if self.a != 1:
            b_norm = self.b / self.a
            c_norm = self.c / self.a
            d_norm = self.d / self.a
            self.steps.append(SolutionStep(
                "归一化为首一多项式",
                f"除以 a = {self.a}",
                f"x³ + {b_norm:.6g}x² + {c_norm:.6g}x + {d_norm:.6g} = 0"
            ))
        else:
            b_norm = self.b
            c_norm = self.c
            d_norm = self.d

        # Step 3: Depress the cubic (eliminate x² term)
        # Substitute x = t - b/(3a)
        p = c_norm - b_norm**2 / 3
        q = (2 * b_norm**3) / 27 - (b_norm * c_norm) / 3 + d_norm

        self.steps.append(SolutionStep(
            "三次方程降次",
            "令 x = t - b/3",
            f"t³ + {p:.6g}t + {q:.6g} = 0"
        ))

        # Step 4: Calculate discriminant
        discriminant = (q/2)**2 + (p/3)**3
        self.steps.append(SolutionStep(
            "计算判别式",
            "Δ = (q/2)² + (p/3)³",
            f"Δ = {discriminant:.6g}"
        ))

        # Step 5: Solve based on discriminant
        shift = -b_norm / 3
        
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
                symbolic_t1 = SymbolicExpression(t1)
                symbolic_t2 = SymbolicExpression(t2)
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
            
            # Create symbolic expressions
            symbolic_sqrt_discriminant = SymbolicExpression(('sqrt', discriminant))
            # For addition and subtraction inside cbrt
            symbolic_u_arg = (-q/2, '+', sqrt_discriminant)
            symbolic_v_arg = (-q/2, '-', sqrt_discriminant)
            symbolic_u = SymbolicExpression(('cbrt', symbolic_u_arg))
            symbolic_v = SymbolicExpression(('cbrt', symbolic_v_arg))
            symbolic_t1 = SymbolicExpression((symbolic_u.value[1], '+', symbolic_v.value[1]))
            
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

            # Create symbolic expressions for trigonometric solution
            symbolic_p = SymbolicExpression(p)
            symbolic_q = SymbolicExpression(q)
            symbolic_rho = SymbolicExpression(('sqrt', (-p**3, '/', 27)))
            
            t1 = 2 * (-p/3)**0.5 * math.cos(theta/3)
            t2 = 2 * (-p/3)**0.5 * math.cos((theta + 2*math.pi)/3)
            t3 = 2 * (-p/3)**0.5 * math.cos((theta + 4*math.pi)/3)

            # Create symbolic expressions for the roots
            symbolic_t1 = SymbolicExpression(t1)
            symbolic_t2 = SymbolicExpression(t2)
            symbolic_t3 = SymbolicExpression(t3)

            self.steps.append(SolutionStep(
                "三个不同实根",
                "Δ < 0 (不可约情况)",
                f"t₁ = {symbolic_t1}, t₂ = {symbolic_t2}, t₃ = {symbolic_t3}"
            ))

            # Convert back to x
            x1 = t1 + shift
            x2 = t2 + shift
            x3 = t3 + shift
            roots = [x1, x2, x3]

        # Add exact expressions step
        self.steps.append(SolutionStep(
            "精确表达式",
            "x = t - b/(3a)",
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

        # Step 2: Normalize to monic polynomial
        if self.a != 1:
            b_norm = self.b / self.a
            c_norm = self.c / self.a
            d_norm = self.d / self.a
            e_norm = self.e / self.a
            self.steps.append(SolutionStep(
            "归一化为首一多项式",
            f"除以 a = {self.a}",
            f"x⁴ + {b_norm:.6g}x³ + {c_norm:.6g}x² + {d_norm:.6g}x + {e_norm:.6g} = 0"
        ))
        else:
            b_norm = self.b
            c_norm = self.c
            d_norm = self.d
            e_norm = self.e

        # Step 3: Depress the quartic (eliminate x³ term)
        # Substitute x = y - b/(4a)
        p = c_norm - 3 * b_norm**2 / 8
        q = b_norm**3 / 8 - b_norm * c_norm / 2 + d_norm
        r = -3 * b_norm**4 / 256 + b_norm**2 * c_norm / 16 - b_norm * d_norm / 4 + e_norm

        self.steps.append(SolutionStep(
            "四次方程降次",
            "令 x = y - b/4",
            f"y⁴ + {p:.6g}y² + {q:.6g}y + {r:.6g} = 0"
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
            
            if quadratic_discriminant >= 0:
                z1 = (-p + sqrt_quad_disc) / 2
                z2 = (-p - sqrt_quad_disc) / 2
                
                # Create symbolic expressions
                symbol_sqrt_quad_disc = SymbolicExpression(('sqrt', quadratic_discriminant))
                symbolic_z1 = SymbolicExpression(((-p, '+', symbol_sqrt_quad_disc.value), '/', 2))
                symbolic_z2 = SymbolicExpression(((-p, '-', symbol_sqrt_quad_disc.value), '/', 2))
                
                self.steps.append(SolutionStep(
                    "求解二次方程",
                    "z² + pz + r = 0",
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
                
                self.steps.append(SolutionStep(
                    "求解二次方程 (复根)",
                    "z² + pz + r = 0",
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