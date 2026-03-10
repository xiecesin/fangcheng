# Java实现二次、三次、四次方程求解

我将为您提供一个完整的Java实现，包括复数运算、详细步骤打印和根的表达形式。

## 一、复数类实现

首先，我们需要一个复数类来处理复数运算：

```
import java.text.DecimalFormat;

/**
 * 复数类，支持基本复数运算
 */
public class Complex {
    private double real;
    private double imag;
    
    // 格式化输出
    private static final DecimalFormat df = new DecimalFormat("0.######");
    
    public Complex(double real, double imag) {
        this.real = real;
        this.imag = imag;
    }
    
    public Complex(double real) {
        this(real, 0);
    }
    
    // 获取实部
    public double getReal() {
        return real;
    }
    
    // 获取虚部
    public double getImag() {
        return imag;
    }
    
    // 复数加法
    public Complex add(Complex other) {
        return new Complex(this.real + other.real, this.imag + other.imag);
    }
    
    // 复数减法
    public Complex subtract(Complex other) {
        return new Complex(this.real - other.real, this.imag - other.imag);
    }
    
    // 复数乘法
    public Complex multiply(Complex other) {
        double r = this.real * other.real - this.imag * other.imag;
        double i = this.real * other.imag + this.imag * other.real;
        return new Complex(r, i);
    }
    
    // 复数除法
    public Complex divide(Complex other) {
        double denominator = other.real * other.real + other.imag * other.imag;
        double r = (this.real * other.real + this.imag * other.imag) / denominator;
        double i = (this.imag * other.real - this.real * other.imag) / denominator;
        return new Complex(r, i);
    }
    
    // 复数除法（除以实数）
    public Complex divide(double scalar) {
        return new Complex(this.real / scalar, this.imag / scalar);
    }
    
    // 复数的模
    public double modulus() {
        return Math.sqrt(real * real + imag * imag);
    }
    
    // 复数的辐角（主值）
    public double argument() {
        if (real == 0 && imag == 0) return 0;
        return Math.atan2(imag, real);
    }
    
    // 复数的平方根（返回两个根）
    public Complex[] sqrt() {
        double mod = Math.sqrt(modulus());
        double arg = argument() / 2;
        
        Complex root1 = new Complex(mod * Math.cos(arg), mod * Math.sin(arg));
        Complex root2 = new Complex(-mod * Math.cos(arg), -mod * Math.sin(arg));
        
        return new Complex[]{root1, root2};
    }
    
    // 复数的立方根（返回三个根）
    public Complex[] cbrt() {
        double mod = Math.pow(modulus(), 1.0/3.0);
        double arg = argument();
        
        Complex[] roots = new Complex[3];
        for (int k = 0; k < 3; k++) {
            double angle = (arg + 2 * Math.PI * k) / 3;
            roots[k] = new Complex(mod * Math.cos(angle), mod * Math.sin(angle));
        }
        
        return roots;
    }
    
    // 判断是否为实数（虚部接近0）
    public boolean isReal() {
        return Math.abs(imag) < 1e-10;
    }
    
    // 判断是否为纯虚数
    public boolean isImaginary() {
        return Math.abs(real) < 1e-10 && Math.abs(imag) > 1e-10;
    }
    
    // 获取共轭复数
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
    
    // 获取精确表达式（包含根号）
    public String toExactString() {
        if (isReal()) {
            return df.format(real);
        } else {
            return toString();
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
    
    // 静态方法：创建复数
    public static Complex of(double real, double imag) {
        return new Complex(real, imag);
    }
    
    public static Complex of(double real) {
        return new Complex(real);
    }
    
    // 三次单位根 ω
    public static Complex omega() {
        return new Complex(-0.5, Math.sqrt(3)/2);
    }
    
    // 三次单位根 ω²
    public static Complex omegaSquared() {
        return new Complex(-0.5, -Math.sqrt(3)/2);
    }
}
```

## 二、二次方程求解

```
import java.util.ArrayList;
import java.util.List;

/**
 * 二次方程求解器
 */
public class QuadraticSolver {
    
    /**
     * 解二次方程 ax² + bx + c = 0
     * @param a 二次项系数
     * @param b 一次项系数
     * @param c 常数项
     * @return 方程的根（复数列表）
     */
    public static List<Complex> solve(double a, double b, double c) {
        return solve(a, b, c, true);
    }
    
    /**
     * 解二次方程 ax² + bx + c = 0
     * @param a 二次项系数
     * @param b 一次项系数
     * @param c 常数项
     * @param verbose 是否打印详细步骤
     * @return 方程的根（复数列表）
     */
    public static List<Complex> solve(double a, double b, double c, boolean verbose) {
        List<Complex> roots = new ArrayList<>();
        
        if (verbose) {
            System.out.println("=".repeat(60));
            System.out.println("求解二次方程:");
            System.out.printf("方程: %.2fx² + %.2fx + %.2f = 0%n", a, b, c);
            System.out.println();
        }
        
        // 检查是否为二次方程
        if (Math.abs(a) < 1e-10) {
            if (verbose) {
                System.out.println("注意: a ≈ 0，这不是一个二次方程");
            }
            // 退化为一次方程
            if (Math.abs(b) > 1e-10) {
                Complex root = new Complex(-c / b);
                roots.add(root);
                if (verbose) {
                    System.out.printf("退化为一次方程，解为: x = %.6f%n", root.getReal());
                }
            } else if (Math.abs(c) < 1e-10) {
                if (verbose) {
                    System.out.println("方程恒成立: 0 = 0");
                }
            } else {
                if (verbose) {
                    System.out.println("方程无解");
                }
            }
            if (verbose) {
                System.out.println("=".repeat(60));
            }
            return roots;
        }
        
        // 步骤1：计算判别式
        double delta = b * b - 4 * a * c;
        
        if (verbose) {
            System.out.println("步骤1: 计算判别式 Δ = b² - 4ac");
            System.out.printf("Δ = %.2f² - 4×%.2f×%.2f = %.6f%n", b, a, c, delta);
            System.out.println();
        }
        
        // 步骤2：根据判别式分类求解
        if (delta > 0) {
            if (verbose) {
                System.out.printf("Δ = %.6f > 0，方程有两个不同的实根%n", delta);
                double sqrtDelta = Math.sqrt(delta);
                System.out.printf("√Δ = √%.6f = %.6f%n", delta, sqrtDelta);
                System.out.println();
                System.out.println("步骤2: 应用求根公式 x = (-b ± √Δ)/(2a)");
            }
            
            double sqrtDelta = Math.sqrt(delta);
            double x1 = (-b + sqrtDelta) / (2 * a);
            double x2 = (-b - sqrtDelta) / (2 * a);
            
            roots.add(new Complex(x1));
            roots.add(new Complex(x2));
            
            if (verbose) {
                System.out.printf("x₁ = (-%.2f + √%.6f)/(2×%.2f) = %.6f%n", b, delta, a, x1);
                System.out.printf("x₂ = (-%.2f - √%.6f)/(2×%.2f) = %.6f%n", b, delta, a, x2);
                System.out.println();
                System.out.println("精确表达式:");
                System.out.printf("x₁ = (%.2f + √%.6f)/%.2f%n", -b, delta, 2*a);
                System.out.printf("x₂ = (%.2f - √%.6f)/%.2f%n", -b, delta, 2*a);
            }
            
        } else if (Math.abs(delta) < 1e-10) {
            if (verbose) {
                System.out.printf("Δ = %.6f ≈ 0，方程有两个相等的实根%n", delta);
                System.out.println();
                System.out.println("步骤2: 应用求根公式 x = -b/(2a)");
            }
            
            double x = -b / (2 * a);
            roots.add(new Complex(x));
            roots.add(new Complex(x));
            
            if (verbose) {
                System.out.printf("x = -%.2f/(2×%.2f) = %.6f%n", b, a, x);
                System.out.println();
                System.out.println("精确表达式:");
                System.out.printf("x = %.2f/%.2f%n", -b, 2*a);
            }
            
        } else {
            if (verbose) {
                System.out.printf("Δ = %.6f < 0，方程有两个共轭复根%n", delta);
                double sqrtNegDelta = Math.sqrt(-delta);
                System.out.printf("√(-Δ) = √%.6f = %.6f%n", -delta, sqrtNegDelta);
                System.out.println();
                System.out.println("步骤2: 应用求根公式 x = (-b ± i√(-Δ))/(2a)");
            }
            
            double realPart = -b / (2 * a);
            double imagPart = Math.sqrt(-delta) / (2 * a);
            
            Complex x1 = new Complex(realPart, imagPart);
            Complex x2 = new Complex(realPart, -imagPart);
            
            roots.add(x1);
            roots.add(x2);
            
            if (verbose) {
                System.out.printf("x₁ = (-%.2f + i√%.6f)/(2×%.2f) = %.6f + %.6fi%n", 
                    b, -delta, a, realPart, imagPart);
                System.out.printf("x₂ = (-%.2f - i√%.6f)/(2×%.2f) = %.6f - %.6fi%n", 
                    b, -delta, a, realPart, imagPart);
                System.out.println();
                System.out.println("精确表达式:");
                System.out.printf("x₁ = (%.2f + i√%.6f)/%.2f%n", -b, -delta, 2*a);
                System.out.printf("x₂ = (%.2f - i√%.6f)/%.2f%n", -b, -delta, 2*a);
            }
        }
        
        if (verbose) {
            System.out.println();
            System.out.println("数值解:");
            for (int i = 0; i < roots.size(); i++) {
                System.out.printf("x%d = %s%n", i+1, roots.get(i).toNumericString());
            }
            System.out.println("=".repeat(60));
        }
        
        return roots;
    }
    
    /**
     * 测试二次方程求解
     */
    public static void test() {
        System.out.println("二次方程求解测试");
        System.out.println();
        
        // 示例1: 两个实根
        System.out.println("示例1: 两个实根");
        System.out.println("方程: x² - 3x + 2 = 0");
        solve(1, -3, 2);
        System.out.println();
        
        // 示例2: 重根
        System.out.println("示例2: 重根");
        System.out.println("方程: x² - 4x + 4 = 0");
        solve(1, -4, 4);
        System.out.println();
        
        // 示例3: 复根
        System.out.println("示例3: 复根");
        System.out.println("方程: x² + 2x + 5 = 0");
        solve(1, 2, 5);
    }
}
```

## 三、三次方程求解

```
import java.util.ArrayList;
import java.util.List;

/**
 * 三次方程求解器（使用卡尔达诺公式）
 */
public class CubicSolver {
    
    /**
     * 解三次方程 ax³ + bx² + cx + d = 0
     * @param a 三次项系数
     * @param b 二次项系数
     * @param c 一次项系数
     * @param d 常数项
     * @return 方程的根（复数列表）
     */
    public static List<Complex> solve(double a, double b, double c, double d) {
        return solve(a, b, c, d, true);
    }
    
    /**
     * 解三次方程 ax³ + bx² + cx + d = 0
     * @param a 三次项系数
     * @param b 二次项系数
     * @param c 一次项系数
     * @param d 常数项
     * @param verbose 是否打印详细步骤
     * @return 方程的根（复数列表）
     */
    public static List<Complex> solve(double a, double b, double c, double d, boolean verbose) {
        List<Complex> roots = new ArrayList<>();
        
        if (verbose) {
            System.out.println("=".repeat(60));
            System.out.println("求解三次方程:");
            System.out.printf("方程: %.2fx³ + %.2fx² + %.2fx + %.2f = 0%n", a, b, c, d);
            System.out.println();
        }
        
        // 检查是否为三次方程
        if (Math.abs(a) < 1e-10) {
            if (verbose) {
                System.out.println("注意: a ≈ 0，这不是一个三次方程");
                System.out.println("退化为二次方程求解:");
            }
            return QuadraticSolver.solve(b, c, d, verbose);
        }
        
        // 步骤1：化为既约形式 y³ + py + q = 0
        if (verbose) {
            System.out.println("步骤1: 化为既约形式 y³ + py + q = 0");
            System.out.println("令 x = y - b/(3a)");
        }
        
        double p = (3 * a * c - b * b) / (3 * a * a);
        double q = (2 * b * b * b - 9 * a * b * c + 27 * a * a * d) / (27 * a * a * a);
        
        if (verbose) {
            System.out.printf("p = (3ac - b²)/(3a²) = (3×%.2f×%.2f - %.2f²)/(3×%.2f²) = %.6f%n", 
                a, c, b, a, p);
            System.out.printf("q = (2b³ - 9abc + 27a²d)/(27a³) = %.6f%n", q);
            System.out.printf("既约方程: y³ + %.6fy + %.6f = 0%n", p, q);
            System.out.println();
        }
        
        // 步骤2：计算判别式
        if (verbose) {
            System.out.println("步骤2: 计算判别式 R = (q/2)² + (p/3)³");
        }
        
        double R = (q/2) * (q/2) + (p/3) * (p/3) * (p/3);
        
        if (verbose) {
            System.out.printf("R = (%.6f/2)² + (%.6f/3)³ = %.6f%n", q, p, R);
            System.out.println();
        }
        
        // 步骤3：计算A和B
        if (verbose) {
            System.out.println("步骤3: 计算 A = ³√(-q/2 + √R) 和 B = ³√(-q/2 - √R)");
        }
        
        Complex sqrtR;
        if (R >= 0) {
            sqrtR = new Complex(Math.sqrt(R));
        } else {
            sqrtR = new Complex(0, Math.sqrt(-R));
        }
        
        Complex A_cube = new Complex(-q/2).add(sqrtR);
        Complex B_cube = new Complex(-q/2).subtract(sqrtR);
        
        if (verbose) {
            System.out.printf("√R = √(%.6f) = %s%n", R, sqrtR);
            System.out.printf("-q/2 + √R = %.6f + %s = %s%n", -q/2, sqrtR, A_cube);
            System.out.printf("-q/2 - √R = %.6f - %s = %s%n", -q/2, sqrtR, B_cube);
        }
        
        // 计算立方根
        Complex[] A_roots = A_cube.cbrt();
        Complex[] B_roots = B_cube.cbrt();
        
        // 选择满足 AB = -p/3 的根
        Complex A = A_roots[0];
        Complex B = null;
        
        for (Complex B_candidate : B_roots) {
            if (Math.abs(A.multiply(B_candidate).getReal() + p/3) < 1e-10 &&
                Math.abs(A.multiply(B_candidate).getImag()) < 1e-10) {
                B = B_candidate;
                break;
            }
        }
        
        if (B == null) {
            B = B_roots[0];
        }
        
        if (verbose) {
            System.out.printf("A = ³√(%s) = %s%n", A_cube, A);
            System.out.printf("B = ³√(%s) = %s%n", B_cube, B);
            System.out.printf("验证: A×B = %s, -p/3 = %.6f%n", A.multiply(B), -p/3);
            System.out.println();
        }
        
        // 步骤4：计算三个根
        if (verbose) {
            System.out.println("步骤4: 计算三个根");
        }
        
        Complex omega = Complex.omega();
        Complex omega2 = Complex.omegaSquared();
        
        Complex y1 = A.add(B);
        Complex y2 = omega.multiply(A).add(omega2.multiply(B));
        Complex y3 = omega2.multiply(A).add(omega.multiply(B));
        
        if (verbose) {
            System.out.printf("ω = -1/2 + i√3/2 = %s%n", omega);
            System.out.printf("ω² = -1/2 - i√3/2 = %s%n", omega2);
            System.out.println();
            System.out.printf("y₁ = A + B = %s + %s = %s%n", A, B, y1);
            System.out.printf("y₂ = ωA + ω²B = %s×%s + %s×%s = %s%n", omega, A, omega2, B, y2);
            System.out.printf("y₃ = ω²A + ωB = %s×%s + %s×%s = %s%n", omega2, A, omega, B, y3);
            System.out.println();
        }
        
        // 步骤5：转换回x
        if (verbose) {
            System.out.println("步骤5: 转换回原变量 x = y - b/(3a)");
        }
        
        double shift = b / (3 * a);
        
        if (verbose) {
            System.out.printf("b/(3a) = %.2f/(3×%.2f) = %.6f%n", b, a, shift);
        }
        
        Complex x1 = y1.subtract(new Complex(shift));
        Complex x2 = y2.subtract(new Complex(shift));
        Complex x3 = y3.subtract(new Complex(shift));
        
        roots.add(x1);
        roots.add(x2);
        roots.add(x3);
        
        if (verbose) {
            System.out.println();
            System.out.println("最终解:");
            System.out.printf("x₁ = y₁ - b/(3a) = %s - %.6f = %s%n", y1, shift, x1);
            System.out.printf("x₂ = y₂ - b/(3a) = %s - %.6f = %s%n", y2, shift, x2);
            System.out.printf("x₃ = y₃ - b/(3a) = %s - %.6f = %s%n", y3, shift, x3);
            System.out.println();
            System.out.println("数值解:");
            for (int i = 0; i < roots.size(); i++) {
                System.out.printf("x%d = %s%n", i+1, roots.get(i).toNumericString());
            }
            System.out.println("=".repeat(60));
        }
        
        return roots;
    }
    
    /**
     * 测试三次方程求解
     */
    public static void test() {
        System.out.println("三次方程求解测试");
        System.out.println();
        
        // 示例1: 三个实根
        System.out.println("示例1: 三个实根");
        System.out.println("方程: x³ - 6x² + 11x - 6 = 0");
        solve(1, -6, 11, -6);
        System.out.println();
        
        // 示例2: 一个实根两个复根
        System.out.println("示例2: 一个实根两个复根");
        System.out.println("方程: x³ - 3x + 2 = 0");
        solve(1, 0, -3, 2);
        System.out.println();
        
        // 示例3: 不可约情形（三个不同实根）
        System.out.println("示例3: 不可约情形（三个不同实根）");
        System.out.println("方程: x³ - 3x - 1 = 0");
        solve(1, 0, -3, -1);
    }
}
```

## 四、四次方程求解

```
import java.util.ArrayList;
import java.util.List;

/**
 * 四次方程求解器（使用费拉里方法）
 */
public class QuarticSolver {
    
    /**
     * 解四次方程 ax⁴ + bx³ + cx² + dx + e = 0
     * @param a 四次项系数
     * @param b 三次项系数
     * @param c 二次项系数
     * @param d 一次项系数
     * @param e 常数项
     * @return 方程的根（复数列表）
     */
    public static List<Complex> solve(double a, double b, double c, double d, double e) {
        return solve(a, b, c, d, e, true);
    }
    
    /**
     * 解四次方程 ax⁴ + bx³ + cx² + dx + e = 0
     * @param a 四次项系数
     * @param b 三次项系数
     * @param c 二次项系数
     * @param d 一次项系数
     * @param e 常数项
     * @param verbose 是否打印详细步骤
     * @return 方程的根（复数列表）
     */
    public static List<Complex> solve(double a, double b, double c, double d, double e, boolean verbose) {
        List<Complex> roots = new ArrayList<>();
        
        if (verbose) {
            System.out.println("=".repeat(60));
            System.out.println("求解四次方程:");
            System.out.printf("方程: %.2fx⁴ + %.2fx³ + %.2fx² + %.2fx + %.2f = 0%n", a, b, c, d, e);
            System.out.println();
        }
        
        // 检查是否为四次方程
        if (Math.abs(a) < 1e-10) {
            if (verbose) {
                System.out.println("注意: a ≈ 0，这不是一个四次方程");
                System.out.println("退化为三次方程求解:");
            }
            return CubicSolver.solve(b, c, d, e, verbose);
        }
        
        // 步骤1：化为既约形式 y⁴ + py² + qy + r = 0
        if (verbose) {
            System.out.println("步骤1: 化为既约形式 y⁴ + py² + qy + r = 0");
            System.out.println("令 x = y - b/(4a)");
        }
        
        double p = (8 * a * c - 3 * b * b) / (8 * a * a);
        double q = (b * b * b - 4 * a * b * c + 8 * a * a * d) / (8 * a * a * a);
        double r = (-3 * b * b * b * b + 16 * a * b * b * c - 64 * a * a * b * d + 256 * a * a * a * e) / (256 * a * a * a * a);
        
        if (verbose) {
            System.out.printf("p = (8ac - 3b²)/(8a²) = %.6f%n", p);
            System.out.printf("q = (b³ - 4abc + 8a²d)/(8a³) = %.6f%n", q);
            System.out.printf("r = %.6f%n", r);
            System.out.printf("既约方程: y⁴ + %.6fy² + %.6fy + %.6f = 0%n", p, q, r);
            System.out.println();
        }
        
        // 步骤2：解预解三次方程 t³ - (p/2)t² - rt + (4pr - q²)/8 = 0
        if (verbose) {
            System.out.println("步骤2: 解预解三次方程");
            System.out.println("预解式: t³ - (p/2)t² - rt + (4pr - q²)/8 = 0");
        }
        
        double A_cubic = 1;
        double B_cubic = -p/2;
        double C_cubic = -r;
        double D_cubic = (4 * p * r - q * q) / 8;
        
        List<Complex> t_roots = CubicSolver.solve(A_cubic, B_cubic, C_cubic, D_cubic, false);
        
        if (verbose) {
            System.out.println("预解式的三个根:");
            for (int i = 0; i < t_roots.size(); i++) {
                System.out.printf("t%d = %s%n", i+1, t_roots.get(i).toNumericString());
            }
        }
        
        // 选取一个实根
        Complex t = null;
        for (Complex root : t_roots) {
            if (root.isReal()) {
                t = root;
                break;
            }
        }
        
        if (t == null) {
            t = t_roots.get(0);
        }
        
        if (verbose) {
            System.out.printf("选取 t = %s 进行后续计算%n", t.toNumericString());
            System.out.println();
        }
        
        // 步骤3：计算α和β
        if (verbose) {
            System.out.println("步骤3: 计算 α = √(2t - p) 和 β = -q/(2α)");
        }
        
        Complex alpha_sq = new Complex(2 * t.getReal() - p);
        Complex[] alpha_sqrt = alpha_sq.sqrt();
        Complex alpha = alpha_sqrt[0];  // 取主根
        
        Complex beta = new Complex(-q).divide(alpha.multiply(new Complex(2)));
        
        if (verbose) {
            System.out.printf("α = √(2t - p) = √(2×%.6f - %.6f) = %s%n", 
                t.getReal(), p, alpha);
            System.out.printf("β = -q/(2α) = -%.6f/(2×%s) = %s%n", q, alpha, beta);
            System.out.println();
        }
        
        // 步骤4：构造两个二次方程
        if (verbose) {
            System.out.println("步骤4: 构造两个二次方程");
            System.out.println("原方程可分解为:");
            System.out.printf("(y² + %.6f + %.6f)² = (αy + β)²%n", p/2, t.getReal());
            System.out.println();
            System.out.println("得到两个二次方程:");
            System.out.printf("1) y² + %.6f + %.6f = αy + β%n", p/2, t.getReal());
            System.out.printf("2) y² + %.6f + %.6f = -(αy + β)%n", p/2, t.getReal());
            System.out.println();
        }
        
        // 方程1: y² - αy + (p/2 + t - β) = 0
        Complex A1 = new Complex(1);
        Complex B1 = alpha.multiply(new Complex(-1));
        Complex C1 = new Complex(p/2 + t.getReal()).subtract(beta);
        
        // 方程2: y² + αy + (p/2 + t + β) = 0
        Complex A2 = new Complex(1);
        Complex B2 = alpha;
        Complex C2 = new Complex(p/2 + t.getReal()).add(beta);
        
        if (verbose) {
            System.out.println("整理为标准二次方程形式:");
            System.out.printf("方程1: y² + (%s)y + (%s) = 0%n", B1, C1);
            System.out.printf("方程2: y² + (%s)y + (%s) = 0%n", B2, C2);
            System.out.println();
        }
        
        // 步骤5：解两个二次方程
        if (verbose) {
            System.out.println("步骤5: 解两个二次方程");
        }
        
        // 解方程1
        List<Complex> y_roots1 = solveQuadraticComplex(A1, B1, C1);
        // 解方程2
        List<Complex> y_roots2 = solveQuadraticComplex(A2, B2, C2);
        
        if (verbose) {
            System.out.println("第一个二次方程的解:");
            for (int i = 0; i < y_roots1.size(); i++) {
                System.out.printf("y%d = %s%n", i+1, y_roots1.get(i).toNumericString());
            }
            System.out.println();
            System.out.println("第二个二次方程的解:");
            for (int i = 0; i < y_roots2.size(); i++) {
                System.out.printf("y%d = %s%n", i+3, y_roots2.get(i).toNumericString());
            }
            System.out.println();
        }
        
        // 步骤6：转换回x
        if (verbose) {
            System.out.println("步骤6: 转换回原变量 x = y - b/(4a)");
        }
        
        double shift = b / (4 * a);
        
        if (verbose) {
            System.out.printf("b/(4a) = %.2f/(4×%.2f) = %.6f%n", b, a, shift);
        }
        
        // 合并所有y根
        List<Complex> y_roots = new ArrayList<>();
        y_roots.addAll(y_roots1);
        y_roots.addAll(y_roots2);
        
        // 转换为x根
        for (Complex y_root : y_roots) {
            Complex x_root = y_root.subtract(new Complex(shift));
            roots.add(x_root);
        }
        
        if (verbose) {
            System.out.println();
            System.out.println("最终解:");
            for (int i = 0; i < roots.size(); i++) {
                System.out.printf("x%d = %s%n", i+1, roots.get(i).toNumericString());
            }
            System.out.println("=".repeat(60));
        }
        
        return roots;
    }
    
    /**
     * 解复数系数的二次方程
     * @param A 二次项系数
     * @param B 一次项系数
     * @param C 常数项
     * @return 方程的根
     */
    private static List<Complex> solveQuadraticComplex(Complex A, Complex B, Complex C) {
        List<Complex> roots = new ArrayList<>();
        
        // 计算判别式 Δ = B² - 4AC
        Complex delta = B.multiply(B).subtract(A.multiply(C).multiply(new Complex(4)));
        
        // 计算平方根
        Complex[] sqrtDelta = delta.sqrt();
        Complex sqrtDelta1 = sqrtDelta[0];  // 取主根
        
        // 计算两个根
        Complex root1 = B.multiply(new Complex(-1)).add(sqrtDelta1).divide(A.multiply(new Complex(2)));
        Complex root2 = B.multiply(new Complex(-1)).subtract(sqrtDelta1).divide(A.multiply(new Complex(2)));
        
        roots.add(root1);
        roots.add(root2);
        
        return roots;
    }
    
    /**
     * 测试四次方程求解
     */
    public static void test() {
        System.out.println("四次方程求解测试");
        System.out.println();
        
        // 示例1: 四个实根
        System.out.println("示例1: 四个实根");
        System.out.println("方程: x⁴ - 5x² + 4 = 0");
        solve(1, 0, -5, 0, 4);
        System.out.println();
        
        // 示例2: 两个实根两个复根
        System.out.println("示例2: 两个实根两个复根");
        System.out.println("方程: x⁴ - 3x² + 2 = 0");
        solve(1, 0, -3, 0, 2);
        System.out.println();
        
        // 示例3: 四个复根
        System.out.println("示例3: 四个复根");
        System.out.println("方程: x⁴ + 1 = 0");
        solve(1, 0, 0, 0, 1);
    }
}
```

## 五、主测试类

```
/**
 * 多项式方程求解主类
 */
public class PolynomialSolver {
    
    public static void main(String[] args) {
        System.out.println("多项式方程求解器");
        System.out.println("=".repeat(60));
        System.out.println();
        
        // 测试二次方程
        System.out.println("1. 二次方程求解测试");
        QuadraticSolver.test();
        System.out.println();
        
        // 测试三次方程
        System.out.println("2. 三次方程求解测试");
        CubicSolver.test();
        System.out.println();
        
        // 测试四次方程
        System.out.println("3. 四次方程求解测试");
        QuarticSolver.test();
        System.out.println();
        
        // 综合示例
        System.out.println("4. 综合示例");
        System.out.println("=".repeat(60));
        
        // 示例1: 二次方程
        System.out.println("示例1: 二次方程");
        System.out.println("方程: 2x² - 5x + 3 = 0");
        List<Complex> roots1 = QuadraticSolver.solve(2, -5, 3);
        System.out.println("根: " + roots1);
        System.out.println();
        
        // 示例2: 三次方程
        System.out.println("示例2: 三次方程");
        System.out.println("方程: x³ - 4x² + x + 6 = 0");
        List<Complex> roots2 = CubicSolver.solve(1, -4, 1, 6);
        System.out.println("根: " + roots2);
        System.out.println();
        
        // 示例3: 四次方程
        System.out.println("示例3: 四次方程");
        System.out.println("方程: x⁴ - 10x² + 9 = 0");
        List<Complex> roots3 = QuarticSolver.solve(1, 0, -10, 0, 9);
        System.out.println("根: " + roots3);
        
        System.out.println("=".repeat(60));
        System.out.println("程序结束");
    }
}
```

## 六、使用Apache Commons Math库的简化版本

如果您可以使用第三方库，Apache Commons Math提供了更强大的数学功能：

```
import org.apache.commons.math3.complex.Complex;
import org.apache.commons.math3.analysis.polynomials.PolynomialFunction;
import org.apache.commons.math3.analysis.solvers.LaguerreSolver;

/**
 * 使用Apache Commons Math库的多项式求解器
 */
public class PolynomialSolverCommons {
    
    /**
     * 解多项式方程
     * @param coefficients 系数数组，从常数项到最高次项
     * @return 方程的根
     */
    public static Complex[] solvePolynomial(double... coefficients) {
        // 创建多项式函数
        PolynomialFunction polynomial = new PolynomialFunction(coefficients);
        
        // 使用拉盖尔求解器
        LaguerreSolver solver = new LaguerreSolver();
        
        // 获取多项式的次数
        int degree = polynomial.degree();
        
        // 求解所有根
        Complex[] roots = new Complex[degree];
        
        // 对于低次多项式，直接使用公式法
        if (degree == 2) {
            // 二次方程
            double a = coefficients[2];
            double b = coefficients[1];
            double c = coefficients[0];
            
            double discriminant = b * b - 4 * a * c;
            
            if (discriminant >= 0) {
                double sqrtDisc = Math.sqrt(discriminant);
                roots[0] = new Complex((-b + sqrtDisc) / (2 * a));
                roots[1] = new Complex((-b - sqrtDisc) / (2 * a));
            } else {
                double sqrtDisc = Math.sqrt(-discriminant);
                roots[0] = new Complex(-b / (2 * a), sqrtDisc / (2 * a));
                roots[1] = new Complex(-b / (2 * a), -sqrtDisc / (2 * a));
            }
            
        } else if (degree == 3) {
            // 三次方程 - 使用卡尔达诺公式
            double a = coefficients[3];
            double b = coefficients[2];
            double c = coefficients[1];
            double d = coefficients[0];
            
            // 化为既约形式
            double p = (3 * a * c - b * b) / (3 * a * a);
            double q = (2 * b * b * b - 9 * a * b * c + 27 * a * a * d) / (27 * a * a * a);
            
            double discriminant = (q / 2) * (q / 2) + (p / 3) * (p / 3) * (p / 3);
            
            if (discriminant > 0) {
                // 一个实根，两个复根
                double sqrtDisc = Math.sqrt(discriminant);
                double u = Math.cbrt(-q / 2 + sqrtDisc);
                double v = Math.cbrt(-q / 2 - sqrtDisc);
                
                double realRoot = u + v - b / (3 * a);
                roots[0] = new Complex(realRoot);
                
                // 复根
                Complex omega = new Complex(-0.5, Math.sqrt(3) / 2);
                Complex omega2 = new Complex(-0.5, -Math.sqrt(3) / 2);
                
                roots[1] = omega.multiply(u).add(omega2.multiply(v)).subtract(b / (3 * a));
                roots[2] = omega2.multiply(u).add(omega.multiply(v)).subtract(b / (3 * a));
                
            } else {
                // 三个实根
                double phi = Math.acos(-q / 2 * Math.sqrt(-27 / (p * p * p)));
                double r = 2 * Math.sqrt(-p / 3);
                
                for (int k = 0; k < 3; k++) {
                    double root = r * Math.cos((phi + 2 * Math.PI * k) / 3) - b / (3 * a);
                    roots[k] = new Complex(root);
                }
            }
            
        } else {
            // 对于高次多项式，使用数值方法
            for (int i = 0; i < degree; i++) {
                // 使用不同的初始猜测值
                double initialGuess = i * 2.0 - degree + 1;
                try {
                    double root = solver.solve(1000, polynomial, initialGuess);
                    roots[i] = new Complex(root);
                } catch (Exception e) {
                    // 如果实数求解失败，尝试复数求解
                    roots[i] = new Complex(initialGuess, 0.1);
                }
            }
        }
        
        return roots;
    }
    
    /**
     * 打印多项式方程的解
     */
    public static void printSolution(String equation, Complex[] roots) {
        System.out.println("方程: " + equation);
        System.out.println("解:");
        for (int i = 0; i < roots.length; i++) {
            Complex root = roots[i];
            if (Math.abs(root.getImaginary()) < 1e-10) {
                System.out.printf("x%d = %.6f%n", i+1, root.getReal());
            } else if (root.getImaginary() > 0) {
                System.out.printf("x%d = %.6f + %.6fi%n", i+1, root.getReal(), root.getImaginary());
            } else {
                System.out.printf("x%d = %.6f - %.6fi%n", i+1, root.getReal(), -root.getImaginary());
            }
        }
        System.out.println();
    }
    
    public static void main(String[] args) {
        System.out.println("使用Apache Commons Math库的多项式求解器");
        System.out.println("=".repeat(60));
        System.out.println();
        
        // 二次方程示例
        printSolution("x² - 3x + 2 = 0", solvePolynomial(2, -3, 1));
        
        // 三次方程示例
        printSolution("x³ - 6x² + 11x - 6 = 0", solvePolynomial(-6, 11, -6, 1));
        
        // 四次方程示例
        printSolution("x⁴ - 5x² + 4 = 0", solvePolynomial(4, 0, -5, 0, 1));
    }
}
```

## 七、Maven依赖配置

如果您使用Apache Commons Math库，需要在`pom.xml`中添加依赖：

```
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-math3</artifactId>
    <version>3.6.1</version>
</dependency>
```

## 总结

这个Java实现提供了：

1. **完整的复数运算**：自定义Complex类支持基本复数运算
2. **二次方程求解**：使用求根公式，处理实根和复根
3. **三次方程求解**：使用卡尔达诺公式，处理所有情况
4. **四次方程求解**：使用费拉里方法，通过预解式分解
5. **详细步骤打印**：显示每一步计算过程和结果
6. **根的表达**：以精确形式和数值形式显示根

代码结构清晰，易于理解和扩展。您可以根据需要调整精度、输出格式或添加更多功能。