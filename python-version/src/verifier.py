"""
Solution Verifier Module
Validates the correctness of equation solutions by substituting roots back into the original equation.
"""

from __future__ import annotations
from typing import List, Union, Optional
from dataclasses import dataclass
import math
import cmath


@dataclass(frozen=True)
class VerificationResult:
    """Represents the result of verifying a solution."""
    root_index: int
    root_value: Union[float, complex]
    substituted_value: Union[float, complex]
    is_valid: bool
    tolerance: float
    error_message: Optional[str] = None


class SolutionVerifier:
    """Verifies equation solutions by substitution."""

    def __init__(self, tolerance: float = 1e-10):
        self.tolerance = tolerance

    def verify_quadratic(self, a: float, b: float, c: float, roots: List[Union[float, complex]]) -> List[VerificationResult]:
        """Verify quadratic equation solutions."""
        results = []
        for i, root in enumerate(roots):
            try:
                if isinstance(root, complex) or (hasattr(root, 'imag') and root.imag != 0):
                    # Handle complex numbers
                    if hasattr(root, 'real') and hasattr(root, 'imag'):
                        actual_root = complex(root.real, root.imag)
                    else:
                        actual_root = root
                    value = a * actual_root**2 + b * actual_root + c
                    is_valid = abs(value) < self.tolerance
                else:
                    # Handle real numbers
                    actual_root = float(root)
                    value = a * actual_root**2 + b * actual_root + c
                    is_valid = abs(value) < self.tolerance

                results.append(VerificationResult(
                    root_index=i + 1,
                    root_value=actual_root,
                    substituted_value=value,
                    is_valid=is_valid,
                    tolerance=self.tolerance
                ))
            except Exception as e:
                results.append(VerificationResult(
                    root_index=i + 1,
                    root_value=root,
                    substituted_value=complex('nan'),
                    is_valid=False,
                    tolerance=self.tolerance,
                    error_message=str(e)
                ))

        return results

    def verify_cubic(self, a: float, b: float, c: float, d: float, roots: List[Union[float, complex]]) -> List[VerificationResult]:
        """Verify cubic equation solutions."""
        results = []
        for i, root in enumerate(roots):
            try:
                if isinstance(root, complex) or (hasattr(root, 'imag') and root.imag != 0):
                    if hasattr(root, 'real') and hasattr(root, 'imag'):
                        actual_root = complex(root.real, root.imag)
                    else:
                        actual_root = root
                    value = a * actual_root**3 + b * actual_root**2 + c * actual_root + d
                    is_valid = abs(value) < self.tolerance
                else:
                    actual_root = float(root)
                    value = a * actual_root**3 + b * actual_root**2 + c * actual_root + d
                    is_valid = abs(value) < self.tolerance

                results.append(VerificationResult(
                    root_index=i + 1,
                    root_value=actual_root,
                    substituted_value=value,
                    is_valid=is_valid,
                    tolerance=self.tolerance
                ))
            except Exception as e:
                results.append(VerificationResult(
                    root_index=i + 1,
                    root_value=root,
                    substituted_value=complex('nan'),
                    is_valid=False,
                    tolerance=self.tolerance,
                    error_message=str(e)
                ))

        return results

    def verify_quartic(self, a: float, b: float, c: float, d: float, e: float, roots: List[Union[float, complex]]) -> List[VerificationResult]:
        """Verify quartic equation solutions."""
        results = []
        for i, root in enumerate(roots):
            try:
                if isinstance(root, complex) or (hasattr(root, 'imag') and root.imag != 0):
                    if hasattr(root, 'real') and hasattr(root, 'imag'):
                        actual_root = complex(root.real, root.imag)
                    else:
                        actual_root = root
                    value = a * actual_root**4 + b * actual_root**3 + c * actual_root**2 + d * actual_root + e
                    is_valid = abs(value) < self.tolerance
                else:
                    actual_root = float(root)
                    value = a * actual_root**4 + b * actual_root**3 + c * actual_root**2 + d * actual_root + e
                    is_valid = abs(value) < self.tolerance

                results.append(VerificationResult(
                    root_index=i + 1,
                    root_value=actual_root,
                    substituted_value=value,
                    is_valid=is_valid,
                    tolerance=self.tolerance
                ))
            except Exception as e:
                results.append(VerificationResult(
                    root_index=i + 1,
                    root_value=root,
                    substituted_value=complex('nan'),
                    is_valid=False,
                    tolerance=self.tolerance,
                    error_message=str(e)
                ))

        return results

    def print_verification_results(self, results: List[VerificationResult]) -> None:
        """Print verification results in a formatted way."""
        print("\n验证结果")
        print("=" * 40)

        all_valid = True
        for result in results:
            status = "✓ 有效" if result.is_valid else "✗ 无效"
            if result.error_message:
                print(f"  根 {result.root_index}: {status} - 错误: {result.error_message}")
            else:
                print(f"  根 {result.root_index}: {status}")
                print(f"    根值: {result.root_value}")
                print(f"    代入值: {result.substituted_value}")

            if not result.is_valid:
                all_valid = False

        print(f"\n总体结果: {'所有解验证成功！' if all_valid else '部分解验证失败！'}")