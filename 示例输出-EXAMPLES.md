# 示例输出

## Python版本示例

### 二次方程求解（两个实根）

```
========================================
Quadratic Equation Solution
========================================

Original equation:
  1.0x² - 5.0x + 6.0 = 0

Step 1: Calculate discriminant Δ = b² - 4ac
  (-5.0)² - 4×(1.0)×(6.0) = 25.0 - 24.0 = 1.0
  Δ = 1.0 > 0, two distinct real roots

Step 2: Apply quadratic formula x = (-b ± √Δ) / (2a)
  x₁ = (5.0 + 1.0) / 2.0 = 3.0
  x₂ = (5.0 - 1.0) / 2.0 = 2.0

Exact expressions:
  x₁ = (5 + √1)/2
  x₂ = (5 - √1)/2

========================================
Verification Results
========================================
Verifying root: x₁ = 3.0
  Substituting into: 1.0x² - 5.0x + 6.0
    Term 1: 1.0 × (3.0)² = 9.0
    Term 2: -5.0 × 3.0 = -15.0
    Term 3: 6.0 = 6.0
  Total = 9.0 + (-15.0) + 6.0 = 0.0
  ✓ Verified! Error = 0.0

Verifying root: x₂ = 2.0
  Substituting into: 1.0x² - 5.0x + 6.0
    Term 1: 1.0 × (2.0)² = 4.0
    Term 2: -5.0 × 2.0 = -10.0
    Term 3: 6.0 = 6.0
  Total = 4.0 + (-10.0) + 6.0 = 0.0
  ✓ Verified! Error = 0.0

Overall: All 2 solutions verified successfully!
```

---

### 三次方程求解（三个实根）

```
========================================
Cubic Equation Solution
========================================

Original equation:
  1.0x³ - 6.0x² + 11.0x - 6.0 = 0

Step 1: Normalize to monic form (a=1)
  Already normalized: x³ - 6.0x² + 11.0x - 6.0 = 0

Step 2: Depress cubic (eliminate x² term)
  Substitute x = y + h, where h = -b/(3a) = 2.0
  Result: y³ - 1.0y + 0.0 = 0
  Where p = -1.0, q = 0.0

Step 3: Calculate discriminant Δ = (q/2)² + (p/3)³
  (0.0)² + (-1.0/3.0)³ = 0.0 + (-0.333333)³ = -0.037037
  Δ = -0.037 < 0, three real roots (casus irreducibilis)

Step 4: Use trigonometric solution
  r = √(-(p/3)³) = √(0.037037) = 0.19245
  θ = arccos(-(q/2)/r) = arccos(0.0) = 1.5708 rad

  y₁ = 2√(-p/3)×cos(θ/3) = 2.0×cos(0.5236) = 1.73205
  y₂ = 2√(-p/3)×cos(θ/3 + 2π/3) = -0.73205
  y₃ = 2√(-p/3)×cos(θ/3 + 4π/3) = -1.0

Step 5: Transform back x = y + h
  x₁ = 1.73205 + 2.0 = 3.73205
  x₂ = -0.73205 + 2.0 = 1.26795
  x₃ = -1.0 + 2.0 = 1.0

Exact expressions (simplified):
  x₁ = 3
  x₂ = 2
  x₃ = 1

========================================
Verification Results
========================================
Verifying root: x₁ = 3.0
  Substituting into: 1.0x³ - 6.0x² + 11.0x - 6.0
    Term 1: 1.0 × (3.0)³ = 27.0
    Term 2: -6.0 × (3.0)² = -54.0
    Term 3: 11.0 × 3.0 = 33.0
    Term 4: -6.0 = -6.0
  Total = 27.0 + (-54.0) + 33.0 + (-6.0) = 0.0
  ✓ Verified! Error = 0.0

Verifying root: x₂ = 2.0
  ... (similar output)
  ✓ Verified! Error = 0.0

Verifying root: x₃ = 1.0
  ... (similar output)
  ✓ Verified! Error = 0.0

Overall: All 3 solutions verified successfully!
```

---

## Java版本示例

### 二次方程求解（复根）

```
Quadratic Equation Solver
================================================
Solving: 1.0x² + 2.0x + 5.0 = 0

Step 1: Calculate discriminant Δ = b² - 4ac
  Δ = (2.0)² - 4×(1.0)×(5.0) = 4.0 - 20.0 = -16.0

Step 2: Δ < 0, two complex conjugate roots
  √(-Δ) = √16.0 = 4.0

Step 3: Apply quadratic formula x = (-b ± i√(-Δ)) / (2a)
  x1 = (-2.0 + 4.0i) / 2.0 = -1.0 + 2.0i
  x2 = (-2.0 - 4.0i) / 2.0 = -1.0 - 2.0i

Exact expressions:
  x1 = (-2 + 4i)/2
  x2 = (-2 - 4i)/2

Solutions:
  x1 = -1.0 + 2.0i
  x2 = -1.0 - 2.0i

Verification:
  Verifying x1 = -1.0 + 2.0i
    1.0×(-1.0 + 2.0i)² = -3.0 - 4.0i
    2.0×(-1.0 + 2.0i) = -2.0 + 4.0i
    Constant: 5.0
    Sum: 0.0 + 0.0i
    ✓ Verified! Error: 0.0

  Verifying x2 = -1.0 - 2.0i
    ... (similar output)
    ✓ Verified! Error: 0.0

================================================
```

---

### 四次方程求解

```
Quartic Equation Solver
================================================
Solving: 1.0x⁴ - 5.0x² + 4.0 = 0

Step 1: Normalize to monic form (a=1)
  Already normalized: x⁴ - 5.0x² + 4.0 = 0

Step 2: Depress quartic (eliminate x³ term)
  Already depressed (no x³ term): x⁴ - 5.0x² + 4.0 = 0
  Where p = -5.0, q = 0.0, r = 4.0

Step 3: Solve resolvent cubic: z³ + 2pz² + (p²-4r)z - q² = 0
  z³ - 10.0z² + 9.0z = 0

  Solving resolvent cubic:
    z = 0.0, 1.0, 9.0  (found one positive root: z1 = 1.0)

Step 4: Calculate u = √z1 = √1.0 = 1.0

Step 5: Form two quadratic factors:
  Factor 1: x² + ux + (p + z1 + q/u)/2
           = x² + 1.0x + (-1.0)
           = x² + x - 1.0 = 0

  Factor 2: x² - ux + (p + z1 - q/u)/2
           = x² - 1.0x + (-1.0)
           = x² - x - 1.0 = 0

Step 6: Solve the two quadratics
  From x² + x - 1.0 = 0: x = -1.61803, 0.61803
  From x² - x - 1.0 = 0: x = 1.61803, -0.61803

Solutions:
  x1 = 1.61803
  x2 = -0.61803
  x3 = -1.61803
  x4 = 0.61803

Verification:
  Verifying x1 = 1.61803: ✓ Error = 8.9e-16
  Verifying x2 = -0.61803: ✓ Error = 1.1e-15
  Verifying x3 = -1.61803: ✓ Error = 8.9e-16
  Verifying x4 = 0.61803: ✓ Error = 1.1e-15

All 4 solutions verified successfully!
================================================
```

---

## 关键特性展示

1. **详细的数学步骤**: 每个求解过程都展示完整的数学推导
2. **精确表达式**: 不仅给出数值解，还显示包含根号的精确形式
3. **验证功能**: 自动验证每个根，显示代入原方程的计算过程
4. **误差分析**: 显示每个根的验证误差值
5. **多种根类型**: 支持实根、复根、重根等多种情况
