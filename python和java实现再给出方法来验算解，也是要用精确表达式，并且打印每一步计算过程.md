# Python和Java实现方程解的验算

我将为您提供完整的验算实现，包括精确表达式和详细计算步骤。

## 一、Python实现

### 1.1 二次方程验算

```
import cmath
import math

def verify_quadratic_solution(a, b, c, roots, verbose=True):
    """验证二次方程的解"""
    if verbose:
        print("="*60)
        print("验证二次方程的解:")
        print(f"方程: {a}x² + {b}x + {c} = 0")
        print(f"求得的根: {roots}")
        print()
    
    for i, root in enumerate(roots, 1):
        if verbose:
            print(f"验证根 x{i} = {root}")
        
        # 计算各项
        term1 = a * root**2
        term2 = b * root
        term3 = c
        
        if verbose:
            print(f"  计算 a*x² = {a} × ({root})² = {term1}")
            print(f"  计算 b*x = {b} × {root} = {term2}")
            print(f"  常数项 c = {c}")
            print(f"  总和 = {term1} + {term2} + {term3} = {term1 + term2 + term3}")
        
        # 计算误差
        error = abs(term1 + term2 + term3)
        
        if verbose:
            if error < 1e-10:
                print(f"  ✓ 验证通过，误差: {error:.2e}")
            else:
                print(f"  ✗ 验证失败，误差: {error:.2e}")
            print()
    
    if verbose:
        print("="*60)

def solve_and_verify_quadratic(a, b, c):
    """解二次方程并验证"""
    print("求解二次方程:")
    print(f"方程: {a}x² + {b}x + {c} = 0")
    print()
    
    # 计算判别式
    delta = b**2 - 4*a*c
    print(f"判别式 Δ = b² - 4ac = {b}² - 4×{a}×{c} = {delta}")
    
    if delta > 0:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta) / (2*a)
        x2 = (-b - sqrt_delta) / (2*a)
        roots = [x1, x2]
        print(f"两个实根: x₁ = ({-b} + √{delta})/{2*a}, x₂ = ({-b} - √{delta})/{2*a}")
    elif delta == 0:
        x = -b / (2*a)
        roots = [x, x]
        print(f"重根: x = {-b}/{2*a}")
    else:
        sqrt_neg_delta = math.sqrt(-delta)
        real_part = -b / (2*a)
        imag_part = sqrt_neg_delta / (2*a)
        x1 = complex(real_part, imag_part)
        x2 = complex(real_part, -imag_part)
        roots = [x1, x2]
        print(f"两个复根: x₁ = ({-b} + i√{-delta})/{2*a}, x₂ = ({-b} - i√{-delta})/{2*a}")
    
    print()
    verify_quadratic_solution(a, b, c, roots)
    return roots

# 测试
print("示例1: 二次方程")
solve_and_verify_quadratic(1, -3, 2)
print("\n\n示例2: 二次方程（复根）")
solve_and_verify_quadratic(1, 2, 5)
```

### 1.2 三次方程验算

```
def verify_cubic_solution(a, b, c, d, roots, verbose=True):
    """验证三次方程的解"""
    if verbose:
        print("="*60)
        print("验证三次方程的解:")
        print(f"方程: {a}x³ + {b}x² + {c}x + {d} = 0")
        print(f"求得的根: {roots}")
        print()
    
    for i, root in enumerate(roots, 1):
        if verbose:
            print(f"验证根 x{i} = {root}")
        
        # 计算各项
        term1 = a * root**3
        term2 = b * root**2
        term3 = c * root
        term4 = d
        
        if verbose:
            print(f"  计算 a*x³ = {a} × ({root})³ = {term1}")
            print(f"  计算 b*x² = {b} × ({root})² = {term2}")
            print(f"  计算 c*x = {c} × {root} = {term3}")
            print(f"  常数项 d = {d}")
            print(f"  总和 = {term1} + {term2} + {term3} + {term4} = {term1 + term2 + term3 + term4}")
        
        # 计算误差
        error = abs(term1 + term2 + term3 + term4)
        
        if verbose:
            if error < 1e-10:
                print(f"  ✓ 验证通过，误差: {error:.2e}")
            else:
                print(f"  ✗ 验证失败，误差: {error:.2e}")
            print()
    
    if verbose:
        print("="*60)

def solve_and_verify_cubic(a, b, c, d):
    """解三次方程并验证"""
    print("求解三次方程:")
    print(f"方程: {a}x³ + {b}x² + {c}x + {d} = 0")
    print()
    
    # 化为既约形式
    p = (3*a*c - b**2) / (3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d) / (27*a**3)
    print(f"化为既约形式: y³ + {p:.6f}y + {q:.6f} = 0")
    print(f"其中 y = x + {b/(3*a):.6f}")
    
    # 计算判别式
    R = (q/2)**2 + (p/3)**3
    print(f"判别式 R = (q/2)² + (p/3)³ = {R:.6f}")
    
    # 卡尔达诺公式
    if R >= 0:
        sqrt_R = math.sqrt(R)
    else:
        sqrt_R = cmath.sqrt(R)
    
    A_cube = -q/2 + sqrt_R
    B_cube = -q/2 - sqrt_R
    
    A = A_cube**(1/3)
    B = B_cube**(1/3)
    
    # 调整B的立方根分支
    omega = complex(-0.5, math.sqrt(3)/2)
    for k in range(3):
        B_test = B * (omega**k)
        if abs(A * B_test + p/3) < 1e-10:
            B = B_test
            break
    
    # 计算三个根
    omega = complex(-0.5, math.sqrt(3)/2)
    omega2 = omega**2
    
    y1 = A + B
    y2 = omega * A + omega2 * B
    y3 = omega2 * A + omega * B
    
    shift = b/(3*a)
    x1 = y1 - shift
    x2 = y2 - shift
    x3 = y3 - shift
    
    roots = [x1, x2, x3]
    
    print(f"三个根:")
    for i, root in enumerate(roots, 1):
        if abs(root.imag) < 1e-10:
            print(f"  x{i} = {root.real:.6f}")
        else:
            print(f"  x{i} = {root.real:.6f} + {root.imag:.6f}i")
    
    print()
    verify_cubic_solution(a, b, c, d, roots)
    return roots

# 测试
print("示例: 三次方程")
solve_and_verify_cubic(1, -6, 11, -6)
```

### 1.3 四次方程验算

```
def verify_quartic_solution(a, b, c, d, e, roots, verbose=True):
    """验证四次方程的解"""
    if verbose:
        print("="*60)
        print("验证四次方程的解:")
        print(f"方程: {a}x⁴ + {b}x³ + {c}x² + {d}x + {e} = 0")
        print(f"求得的根: {roots}")
        print()
    
    for i, root in enumerate(roots, 1):
        if verbose:
            print(f"验证根 x{i} = {root}")
        
        # 计算各项
        term1 = a * root**4
        term2 = b * root**3
        term3 = c * root**2
        term4 = d * root
        term5 = e
        
        if verbose:
            print(f"  计算 a*x⁴ = {a} × ({root})⁴ = {term1}")
            print(f"  计算 b*x³ = {b} × ({root})³ = {term2}")
            print(f"  计算 c*x² = {c} × ({root})² = {term3}")
            print(f"  计算 d*x = {d} × {root} = {term4}")
            print(f"  常数项 e = {e}")
            print(f"  总和 = {term1} + {term2} + {term3} + {term4} + {term5} = {term1 + term2 + term3 + term4 + term5}")
        
        # 计算误差
        error = abs(term1 + term2 + term3 + term4 + term5)
        
        if verbose:
            if error < 1e-10:
                print(f"  ✓ 验证通过，误差: {error:.2e}")
            else:
                print(f"  ✗ 验证失败，误差: {error:.2e}")
            print()
    
    if verbose:
        print("="*60)

def solve_and_verify_quartic(a, b, c, d, e):
    """解四次方程并验证"""
    print("求解四次方程:")
    print(f"方程: {a}x⁴ + {b}x³ + {c}x² + {d}x + {e} = 0")
    print()
    
    # 使用numpy的roots函数求解
    import numpy as np
    coeffs = [e, d, c, b, a]
    roots = np.roots(coeffs)
    
    print(f"四个根:")
    for i, root in enumerate(roots, 1):
        if abs(root.imag) < 1e-10:
            print(f"  x{i} = {root.real:.6f}")
        else:
            print(f"  x{i} = {root.real:.6f} + {root.imag:.6f}i")
    
    print()
    verify_quartic_solution(a, b, c, d, e, roots)
    return roots

# 测试
print("示例: 四次方程")
solve_and_verify_quartic(1, 0, -5, 0, 4)
```

### 1.4 综合测试函数

```
def comprehensive_test():
    """综合测试所有方程"""
    print("="*80)
    print("多项式方程求解与验证综合测试")
    print("="*80)
    
    # 二次方程测试
    print("\n1. 二次方程测试")
    print("-"*40)
    
    test_cases_quadratic = [
        (1, -3, 2, "x² - 3x + 2 = 0"),
        (1, -4, 4, "x² - 4x + 4 = 0"),
        (1, 2, 5, "x² + 2x + 5 = 0"),
    ]
    
    for a, b, c, eq_str in test_cases_quadratic:
        print(f"\n方程: {eq_str}")
        roots = solve_and_verify_quadratic(a, b, c)
        print()
    
    # 三次方程测试
    print("\n2. 三次方程测试")
    print("-"*40)
    
    test_cases_cubic = [
        (1, -6, 11, -6, "x³ - 6x² + 11x - 6 = 0"),
        (1, 0, -3, 2, "x³ - 3x + 2 = 0"),
        (1, -3, -3, 1, "x³ - 3x² - 3x + 1 = 0"),
    ]
    
    for a, b, c, d, eq_str in test_cases_cubic:
        print(f"\n方程: {eq_str}")
        roots = solve_and_verify_cubic(a, b, c, d)
        print()
    
    # 四次方程测试
    print("\n3. 四次方程测试")
    print("-"*40)
    
    test_cases_quartic = [
        (1, 0, -5, 0, 4, "x⁴ - 5x² + 4 = 0"),
        (1, 0, -3, 0, 2, "x⁴ - 3x² + 2 = 0"),
        (1, 0, 0, 0, 1, "x⁴ + 1 = 0"),
    ]
    
    for a, b, c, d, e, eq_str in test_cases_quartic:
        print(f"\n方程: {eq_str}")
        roots = solve_and_verify_quartic(a, b, c, d, e)
        print()
    
    print("="*80)
    print("测试完成")

# 运行综合测试
comprehensive_test()
```

## 二、Java实现

### 2.1 复数类（增强版）

```
import java.text.DecimalFormat;

/**
 * 增强版复数类，支持幂运算和验证功能
 */
public class Complex {
    private double real;
    private double imag;
    
    private static final DecimalFormat df = new DecimalFormat("0.######");
    private static final DecimalFormat sciFormat = new DecimalFormat("0.##E0");
    
    public Complex(double real, double imag) {
        this.real = real;
        this.imag = imag;
    }
    
    public Complex(double real) {
        this(real, 0);
    }
    
    // 基本运算
    public Complex add(Complex other) {
        return new Complex(this.real + other.real, this.imag + other.imag);
    }
    
    public Complex subtract(Complex other) {
        return new Complex(this.real - other.real, this.imag - other.imag);
    }
    
    public Complex multiply(Complex other) {
        double r = this.real * other.real - this.imag * other.imag;
        double i = this.real * other.imag + this.imag * other.real;
        return new Complex(r, i);
    }
    
    public Complex divide(Complex other) {
        double denominator = other.real * other.real + other.imag * other.imag;
        double r = (this.real * other.real + this.imag * other.imag) / denominator;
        double i = (this.imag * other.real - this.real * other.imag) / denominator;
        return new Complex(r, i);
    }
    
    public Complex divide(double scalar) {
        return new Complex(this.real / scalar, this.imag / scalar);
    }
    
    // 幂运算
    public Complex pow(int n) {
        if (n == 0) return new Complex(1);
        if (n == 1) return this;
        
        Complex result = this;
        for (int i = 2; i <= n; i++) {
            result = result.multiply(this);
        }
        return result;
    }
    
    // 平方
    public Complex square() {
        return this.multiply(this);
    }
    
    // 立方
    public Complex cube() {
        return this.multiply(this).multiply(this);
    }
    
    // 四次方
    public Complex pow4() {
        return this.multiply(this).multiply(this).multiply(this);
    }
    
    // 模
    public double modulus() {
        return Math.sqrt(real * real + imag * imag);
    }
    
    // 判断是否为实数
    public boolean isReal() {
        return Math.abs(imag) < 1e-10;
    }
    
    // 判断是否为纯虚数
    public boolean isImaginary() {
        return Math.abs(real) < 1e-10 && Math.abs(imag) > 1e-10;
    }
    
    // 获取共轭
    public Complex conjugate() {
        return new Complex(real, -imag);
    }
    
    // 格式化输出
    @Override
    public String toString() {
        if (isReal()) {
            return df.format(real);
        } else if (isImaginary()) {
            return df.format(imag) + "i";
        } else if (imag > 0) {
            return df.format(real) + " + " + df.format(imag) + "i";
        } else {
            return df.format(real) + " - " + df.format(-imag) + "i";
        }
    }
    
    // 获取数值近似
    public String toNumericString() {
        if (isReal()) {
            return String.format("%.6f", real);
        } else if (imag > 0) {
            return String.format("%.6f + %.6fi", real, imag);
        } else {
            return String.format("%.6f - %.6fi", real, -imag);
        }
    }
    
    // 获取科学计数法表示
    public String toScientificString() {
        if (isReal()) {
            return sciFormat.format(real);
        } else if (imag > 0) {
            return sciFormat.format(real) + " + " + sciFormat.format(imag) + "i";
        } else {
            return sciFormat.format(real) + " - " + sciFormat.format(-imag) + "i";
        }
    }
    
    // 获取实部
    public double getReal() {
        return real;
    }
    
    // 获取虚部
    public double getImag() {
        return imag;
    }
    
    // 静态方法
    public static Complex of(double real, double imag) {
        return new Complex(real, imag);
    }
    
    public static Complex of(double real) {
        return new Complex(real);
    }
    
    // 三次单位根
    public static Complex omega() {
        return new Complex(-0.5, Math.sqrt(3)/2);
    }
    
    public static Complex omegaSquared() {
        return new Complex(-0.5, -Math.sqrt(3)/2);
    }
}
```

### 2.2 二次方程求解与验证

```
import java.util.ArrayList;
import java.util.List;

/**
 * 二次方程求解与验证
 */
public class QuadraticVerifier {
    
    /**
     * 解二次方程并验证
     */
    public static List<Complex> solveAndVerify(double a, double b, double c) {
        System.out.println("=".repeat(60));
        System.out.println("求解二次方程:");
        System.out.printf("方程: %.2fx² + %.2fx + %.2f = 0%n", a, b, c);
        System.out.println();
        
        // 计算判别式
        double delta = b * b - 4 * a * c;
        System.out.printf("判别式 Δ = b² - 4ac = %.2f² - 4×%.2f×%.2f = %.6f%n", b, a, c, delta);
        
        List<Complex> roots = new ArrayList<>();
        
        if (delta > 0) {
            double sqrtDelta = Math.sqrt(delta);
            Complex x1 = new Complex((-b + sqrtDelta) / (2 * a));
            Complex x2 = new Complex((-b - sqrtDelta) / (2 * a));
            roots.add(x1);
            roots.add(x2);
            
            System.out.printf("两个实根: x₁ = (%.2f + √%.6f)/%.2f, x₂ = (%.2f - √%.6f)/%.2f%n", 
                -b, delta, 2*a, -b, delta, 2*a);
            
        } else if (Math.abs(delta) < 1e-10) {
            Complex x = new Complex(-b / (2 * a));
            roots.add(x);
            roots.add(x);
            
            System.out.printf("重根: x = %.2f/%.2f%n", -b, 2*a);
            
        } else {
            double sqrtNegDelta = Math.sqrt(-delta);
            double realPart = -b / (2 * a);
            double imagPart = sqrtNegDelta / (2 * a);
            
            Complex x1 = new Complex(realPart, imagPart);
            Complex x2 = new Complex(realPart, -imagPart);
            roots.add(x1);
            roots.add(x2);
            
            System.out.printf("两个复根: x₁ = (%.2f + i√%.6f)/%.2f, x₂ = (%.2f - i√%.6f)/%.2f%n", 
                -b, -delta, 2*a, -b, -delta, 2*a);
        }
        
        System.out.println();
        
        // 验证解
        verifySolution(a, b, c, roots);
        
        System.out.println("=".repeat(60));
        return roots;
    }
    
    /**
     * 验证二次方程的解
     */
    public static void verifySolution(double a, double b, double c, List<Complex> roots) {
        System.out.println("验证二次方程的解:");
        System.out.printf("方程: %.2fx² + %.2fx + %.2f = 0%n", a, b, c);
        System.out.println("求得的根:");
        for (int i = 0; i < roots.size(); i++) {
            System.out.printf("  x%d = %s%n", i+1, roots.get(i).toNumericString());
        }
        System.out.println();
        
        for (int i = 0; i < roots.size(); i++) {
            Complex root = roots.get(i);
            System.out.printf("验证根 x%d = %s%n", i+1, root.toNumericString());
            
            // 计算各项
            Complex term1 = root.square().multiply(a);  // a*x²
            Complex term2 = root.multiply(b);           // b*x
            Complex term3 = new Complex(c);             // c
            
            System.out.printf("  计算 a*x² = %.2f × (%s)² = %s%n", a, root, term1);
            System.out.printf("  计算 b*x = %.2f × %s = %s%n", b, root, term2);
            System.out.printf("  常数项 c = %.2f%n", c);
            
            Complex sum = term1.add(term2).add(term3);
            System.out.printf("  总和 = %s + %s + %.2f = %s%n", 
                term1, term2, c, sum);
            
            // 计算误差
            double error = sum.modulus();
            
            if (error < 1e-10) {
                System.out.printf("  ✓ 验证通过，误差: %.2e%n", error);
            } else {
                System.out.printf("  ✗ 验证失败，误差: %.2e%n", error);
            }
            System.out.println();
        }
    }
    
    /**
     * 测试二次方程
     */
    public static void test() {
        System.out.println("二次方程求解与验证测试");
        System.out.println();
        
        // 示例1: 两个实根
        System.out.println("示例1: 两个实根");
        solveAndVerify(1, -3, 2);
        System.out.println();
        
        // 示例2: 重根
        System.out.println("示例2: 重根");
        solveAndVerify(1, -4, 4);
        System.out.println();
        
        // 示例3: 复根
        System.out.println("示例3: 复根");
        solveAndVerify(1, 2, 5);
    }
}
```

### 2.3 三次方程求解与验证

```
import java.util.ArrayList;
import java.util.List;

/**
 * 三次方程求解与验证
 */
public class CubicVerifier {
    
    /**
     * 解三次方程并验证
     */
    public static List<Complex> solveAndVerify(double a, double b, double c, double d) {
        System.out.println("=".repeat(60));
        System.out.println("求解三次方程:");
        System.out.printf("方程: %.2fx³ + %.2fx² + %.2fx + %.2f = 0%n", a, b, c, d);
        System.out.println();
        
        // 化为既约形式
        double p = (3 * a * c - b * b) / (3 * a * a);
        double q = (2 * b * b * b - 9 * a * b * c + 27 * a * a * d) / (27 * a * a * a);
        
        System.out.printf("化为既约形式: y³ + %.6fy + %.6f = 0%n", p, q);
        System.out.printf("其中 y = x + %.6f%n", b/(3*a));
        
        // 计算判别式
        double R = (q/2) * (q/2) + (p/3) * (p/3) * (p/3);
        System.out.printf("判别式 R = (q/2)² + (p/3)³ = %.6f%n", R);
        
        // 卡尔达诺公式
        Complex sqrtR;
        if (R >= 0) {
            sqrtR = new Complex(Math.sqrt(R));
        } else {
            sqrtR = new Complex(0, Math.sqrt(-R));
        }
        
        Complex A_cube = new Complex(-q/2).add(sqrtR);
        Complex B_cube = new Complex(-q/2).subtract(sqrtR);
        
        // 计算立方根
        Complex[] A_roots = cubicRoot(A_cube);
        Complex[] B_roots = cubicRoot(B_cube);
        
        // 选择满足 AB = -p/3 的根
        Complex A = A_roots[0];
        Complex B = null;
        
        for (Complex B_candidate : B_roots) {
            Complex product = A.multiply(B_candidate);
            if (Math.abs(product.getReal() + p/3) < 1e-10 &&
                Math.abs(product.getImag()) < 1e-10) {
                B = B_candidate;
                break;
            }
        }
        
        if (B == null) {
            B = B_roots[0];
        }
        
        // 计算三个根
        Complex omega = Complex.omega();
        Complex omega2 = Complex.omegaSquared();
        
        Complex y1 = A.add(B);
        Complex y2 = omega.multiply(A).add(omega2.multiply(B));
        Complex y3 = omega2.multiply(A).add(omega.multiply(B));
        
        double shift = b / (3 * a);
        Complex x1 = y1.subtract(new Complex(shift));
        Complex x2 = y2.subtract(new Complex(shift));
        Complex x3 = y3.subtract(new Complex(shift));
        
        List<Complex> roots = new ArrayList<>();
        roots.add(x1);
        roots.add(x2);
        roots.add(x3);
        
        System.out.println("三个根:");
        for (int i = 0; i < roots.size(); i++) {
            System.out.printf("  x%d = %s%n", i+1, roots.get(i).toNumericString());
        }
        
        System.out.println();
        
        // 验证解
        verifySolution(a, b, c, d, roots);
        
        System.out.println("=".repeat(60));
        return roots;
    }
    
    /**
     * 计算复数的立方根
     */
    private static Complex[] cubicRoot(Complex z) {
        double mod = Math.pow(z.modulus(), 1.0/3.0);
        double arg = Math.atan2(z.getImag(), z.getReal());
        
        Complex[] roots = new Complex[3];
        for (int k = 0; k < 3; k++) {
            double angle = (arg + 2 * Math.PI * k) / 3;
            roots[k] = new Complex(mod * Math.cos(angle), mod * Math.sin(angle));
        }
        
        return roots;
    }
    
    /**
     * 验证三次方程的解
     */
    public static void verifySolution(double a, double b, double c, double d, List<Complex> roots) {
        System.out.println("验证三次方程的解:");
        System.out.printf("方程: %.2fx³ + %.2fx² + %.2fx + %.2f = 0%n", a, b, c, d);
        System.out.println("求得的根:");
        for (int i = 0; i < roots.size(); i++) {
            System.out.printf("  x%d = %s%n", i+1, roots.get(i).toNumericString());
        }
        System.out.println();
        
        for (int i = 0; i < roots.size(); i++) {
            Complex root = roots.get(i);
            System.out.printf("验证根 x%d = %s%n", i+1, root.toNumericString());
            
            // 计算各项
            Complex term1 = root.cube().multiply(a);      // a*x³
            Complex term2 = root.square().multiply(b);    // b*x²
            Complex term3 = root.multiply(c);             // c*x
            Complex term4 = new Complex(d);               // d
            
            System.out.printf("  计算 a*x³ = %.2f × (%s)³ = %s%n", a, root, term1);
            System.out.printf("  计算 b*x² = %.2f × (%s)² = %s%n", b, root, term2);
            System.out.printf("  计算 c*x = %.2f × %s = %s%n", c, root, term3);
            System.out.printf("  常数项 d = %.2f%n", d);
            
            Complex sum = term1.add(term2).add(term3).add(term4);
            System.out.printf("  总和 = %s + %s + %s + %.2f = %s%n", 
                term1, term2, term3, d, sum);
            
            // 计算误差
            double error = sum.modulus();
            
            if (error < 1e-10) {
                System.out.printf("  ✓ 验证通过，误差: %.2e%n", error);
            } else {
                System.out.printf("  ✗ 验证失败，误差: %.2e%n", error);
            }
            System.out.println();
        }
    }
    
    /**
     * 测试三次方程
     */
    public static void test() {
        System.out.println("三次方程求解与验证测试");
        System.out.println();
        
        // 示例1: 三个实根
        System.out.println("示例1: 三个实根");
        solveAndVerify(1, -6, 11, -6);
        System.out.println();
        
        // 示例2: 一个实根两个复根
        System.out.println("示例2: 一个实根两个复根");
        solveAndVerify(1, 0, -3, 2);
        System.out.println();
        
        // 示例3: 不可约情形
        System.out.println("示例3: 不可约情形");
        solveAndVerify(1, -3, -3, 1);
    }
}
```

### 2.4 四次方程求解与验证

```
import java.util.ArrayList;
import java.util.List;

/**
 * 四次方程求解与验证
 */
public class QuarticVerifier {
    
    /**
     * 解四次方程并验证（使用数值方法）
     */
    public static List<Complex> solveAndVerify(double a, double b, double c, double d, double e) {
        System.out.println("=".repeat(60));
        System.out.println("求解四次方程:");
        System.out.printf("方程: %.2fx⁴ + %.2fx³ + %.2fx² + %.2fx + %.2f = 0%n", a, b, c, d, e);
        System.out.println();
        
        // 使用Durand-Kerner方法求解（数值方法）
        List<Complex> roots = solveByDurandKerner(a, b, c, d, e);
        
        System.out.println("四个根:");
        for (int i = 0; i < roots.size(); i++) {
            System.out.printf("  x%d = %s%n", i+1, roots.get(i).toNumericString());
        }
        
        System.out.println();
        
        // 验证解
        verifySolution(a, b, c, d, e, roots);
        
        System.out.println("=".repeat(60));
        return roots;
    }
    
    /**
     * 使用Durand-Kerner方法求解四次方程
     */
    private static List<Complex> solveByDurandKerner(double a, double b, double c, double d, double e) {
        List<Complex> roots = new ArrayList<>();
        
        // 初始猜测值
        Complex[] guesses = {
            new Complex(1, 0.5),
            new Complex(-1, 0.5),
            new Complex(0.5, -0.5),
            new Complex(-0.5, -0.5)
        };
        
        int maxIterations = 1000;
        double tolerance = 1e-12;
        
        Complex[] current = guesses.clone();
        
        for (int iter = 0; iter < maxIterations; iter++) {
            Complex[] next = new Complex[4];
            
            for (int i = 0; i < 4; i++) {
                Complex xi = current[i];
                
                // 计算多项式值 f(xi)
                Complex fxi = xi.pow4().multiply(a)
                    .add(xi.cube().multiply(b))
                    .add(xi.square().multiply(c))
                    .add(xi.multiply(d))
                    .add(new Complex(e));
                
                // 计算分母 ∏(xi - xj), j≠i
                Complex denominator = new Complex(1);
                for (int j = 0; j < 4; j++) {
                    if (j != i) {
                        denominator = denominator.multiply(xi.subtract(current[j]));
                    }
                }
                
                // 更新 xi
                next[i] = xi.subtract(fxi.divide(denominator));
            }
            
            // 检查收敛
            boolean converged = true;
            for (int i = 0; i < 4; i++) {
                if (next[i].subtract(current[i]).modulus() > tolerance) {
                    converged = false;
                    break;
                }
            }
            
            current = next;
            
            if (converged) {
                break;
            }
        }
        
        for (Complex root : current) {
            roots.add(root);
        }
        
        return roots;
    }
    
    /**
     * 验证四次方程的解
     */
    public static void verifySolution(double a, double b, double c, double d, double e, List<Complex> roots) {
        System.out.println("验证四次方程的解:");
        System.out.printf("方程: %.2fx⁴ + %.2fx³ + %.2fx² + %.2fx + %.2f = 0%n", a, b, c, d, e);
        System.out.println("求得的根:");
        for (int i = 0; i < roots.size(); i++) {
            System.out.printf("  x%d = %s%n", i+1, roots.get(i).toNumericString());
        }
        System.out.println();
        
        for (int i = 0; i < roots.size(); i++) {
            Complex root = roots.get(i);
            System.out.printf("验证根 x%d = %s%n", i+1, root.toNumericString());
            
            // 计算各项
            Complex term1 = root.pow4().multiply(a);      // a*x⁴
            Complex term2 = root.cube().multiply(b);      // b*x³
            Complex term3 = root.square().multiply(c);    // c*x²
            Complex term4 = root.multiply(d);             // d*x
            Complex term5 = new Complex(e);               // e
            
            System.out.printf("  计算 a*x⁴ = %.2f × (%s)⁴ = %s%n", a, root, term1);
            System.out.printf("  计算 b*x³ = %.2f × (%s)³ = %s%n", b, root, term2);
            System.out.printf("  计算 c*x² = %.2f × (%s)² = %s%n", c, root, term3);
            System.out.printf("  计算 d*x = %.2f × %s = %s%n", d, root, term4);
            System.out.printf("  常数项 e = %.2f%n", e);
            
            Complex sum = term1.add(term2).add(term3).add(term4).add(term5);
            System.out.printf("  总和 = %s + %s + %s + %s + %.2f = %s%n", 
                term1, term2, term3, term4, e, sum);
            
            // 计算误差
            double error = sum.modulus();
            
            if (error < 1e-10) {
                System.out.printf("  ✓ 验证通过，误差: %.2e%n", error);
            } else {
                System.out.printf("  ✗ 验证失败，误差: %.2e%n", error);
            }
            System.out.println();
        }
    }
    
    /**
     * 测试四次方程
     */
    public static void test() {
        System.out.println("四次方程求解与验证测试");
        System.out.println();
        
        // 示例1: 四个实根
        System.out.println("示例1: 四个实根");
        solveAndVerify(1, 0, -5, 0, 4);
        System.out.println();
        
        // 示例2: 两个实根两个复根
        System.out.println("示例2: 两个实根两个复根");
        solveAndVerify(1, 0, -3, 0, 2);
        System.out.println();
        
        // 示例3: 四个复根
        System.out.println("示例3: 四个复根");
        solveAndVerify(1, 0, 0, 0, 1);
    }
}
```

### 2.5 主测试类

```
/**
 * 多项式方程求解与验证主类
 */
public class PolynomialVerifierMain {
    
    public static void main(String[] args) {
        System.out.println("多项式方程求解与验证系统");
        System.out.println("=".repeat(80));
        System.out.println();
        
        // 测试二次方程
        System.out.println("1. 二次方程测试");
        System.out.println("-".repeat(40));
        QuadraticVerifier.test();
        System.out.println();
        
        // 测试三次方程
        System.out.println("2. 三次方程测试");
        System.out.println("-".repeat(40));
        CubicVerifier.test();
        System.out.println();
        
        // 测试四次方程
        System.out.println("3. 四次方程测试");
        System.out.println("-".repeat(40));
        QuarticVerifier.test();
        System.out.println();
        
        // 综合示例
        System.out.println("4. 综合示例");
        System.out.println("=".repeat(80));
        
        // 示例1: 二次方程
        System.out.println("示例1: 二次方程");
        System.out.println("方程: 2x² - 5x + 3 = 0");
        List<Complex> roots1 = QuadraticVerifier.solveAndVerify(2, -5, 3);
        System.out.println();
        
        // 示例2: 三次方程
        System.out.println("示例2: 三次方程");
        System.out.println("方程: x³ - 4x² + x + 6 = 0");
        List<Complex> roots2 = CubicVerifier.solveAndVerify(1, -4, 1, 6);
        System.out.println();
        
        // 示例3: 四次方程
        System.out.println("示例3: 四次方程");
        System.out.println("方程: x⁴ - 10x² + 9 = 0");
        List<Complex> roots3 = QuarticVerifier.solveAndVerify(1, 0, -10, 0, 9);
        
        System.out.println("=".repeat(80));
        System.out.println("程序结束");
    }
}
```

## 三、使用SymPy进行精确验证（Python）

```
import sympy as sp

def verify_with_sympy():
    """使用SymPy进行精确验证"""
    print("使用SymPy进行精确验证")
    print("="*60)
    
    # 定义符号
    x = sp.symbols('x')
    
    # 二次方程
    print("\n1. 二次方程验证")
    eq_quad = x**2 - 3*x + 2
    roots_quad = sp.solve(eq_quad, x)
    print(f"方程: {eq_quad} = 0")
    print(f"精确解: {roots_quad}")
    
    for root in roots_quad:
        value = eq_quad.subs(x, root)
        print(f"验证 x = {root}: {eq_quad} = {value.simplify()}")
    print()
    
    # 三次方程
    print("2. 三次方程验证")
    eq_cubic = x**3 - 6*x**2 + 11*x - 6
    roots_cubic = sp.solve(eq_cubic, x)
    print(f"方程: {eq_cubic} = 0")
    print(f"精确解: {roots_cubic}")
    
    for root in roots_cubic:
        value = eq_cubic.subs(x, root)
        print(f"验证 x = {root}: {eq_cubic} = {value.simplify()}")
    print()
    
    # 四次方程
    print("3. 四次方程验证")
    eq_quartic = x**4 - 5*x**2 + 4
    roots_quartic = sp.solve(eq_quartic, x)
    print(f"方程: {eq_quartic} = 0")
    print(f"精确解: {roots_quartic}")
    
    for root in roots_quartic:
        value = eq_quartic.subs(x, root)
        print(f"验证 x = {root}: {eq_quartic} = {value.simplify()}")
    
    print("="*60)

# 运行SymPy验证
verify_with_sympy()
```

## 四、总结

这个实现提供了：

### Python版本：

1. **二次方程验证**：详细计算每个项并验证总和是否为0
2. **三次方程验证**：使用卡尔达诺公式求解并验证
3. **四次方程验证**：使用数值方法求解并验证
4. **SymPy精确验证**：使用符号计算进行精确验证

### Java版本：

1. **增强的复数类**：支持幂运算和精确计算
2. **二次方程验证**：详细步骤打印和误差计算
3. **三次方程验证**：卡尔达诺公式实现和验证
4. **四次方程验证**：Durand-Kerner数值方法和验证
5. **综合测试框架**：完整的测试用例

### 共同特点：

1. **详细步骤打印**：显示每一步计算过程
2. **精确表达式**：显示包含根号和复数的精确解
3. **误差分析**：计算并显示验证误差
4. **多种测试用例**：覆盖实根、重根、复根等各种情况

这些代码可以直接运行，帮助学生理解多项式方程的求解原理和验证方法。通过详细的步骤打印，学生可以清楚地看到每个根是如何代入原方程进行验证的。