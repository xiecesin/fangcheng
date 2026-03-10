package com.equation;

/**
 * A solver for cubic equations of the form ax^3 + bx^2 + cx + d = 0.
 * Uses Cardano's method to find all three roots (real or complex).
 */
public class CubicSolver {

    /**
     * Solves a cubic equation ax^3 + bx^2 + cx + d = 0.
     * @param a coefficient of x^3
     * @param b coefficient of x^2
     * @param c coefficient of x
     * @param d constant term
     * @return array of three Complex roots
     */
    public static Complex[] solve(double a, double b, double c, double d) {
        System.out.println("求解三次方程: " + formatEquation(a, b, c, d));

        if (Math.abs(a) < 1e-10) {
            throw new IllegalArgumentException("三次方程的系数 'a' 不能为零");
        }

        // 创建符号表达式 - 基于原始系数
        SymbolicExpression aExpr = new SymbolicExpression(a);
        SymbolicExpression bExpr = new SymbolicExpression(b);
        SymbolicExpression cExpr = new SymbolicExpression(c);
        SymbolicExpression dExpr = new SymbolicExpression(d);
        
        // 归一化系数的符号表达式
        SymbolicExpression aNormExpr = new SymbolicExpression(1.0);
        SymbolicExpression bNormExpr = SymbolicExpression.divide(bExpr, aExpr);
        SymbolicExpression cNormExpr = SymbolicExpression.divide(cExpr, aExpr);
        SymbolicExpression dNormExpr = SymbolicExpression.divide(dExpr, aExpr);

        // 步骤1: 归一化为首一多项式（除以a）
        double aNorm = 1.0;
        double bNorm = b / a;
        double cNorm = c / a;
        double dNorm = d / a;

        System.out.println("步骤1: 归一化为首一多项式（除以a = " + a + "）");
        System.out.println("        x^3 + (" + bNormExpr + ")x^2 + (" + cNormExpr + ")x + (" + dNormExpr + ") = 0");
        
        // 步骤2: 降次（消除x^2项），使用代换 x = t - b/(3a)
        double p = cNorm - bNorm * bNorm / 3.0;
        double q = (2.0 * bNorm * bNorm * bNorm - 9.0 * bNorm * cNorm + 27.0 * dNorm) / 27.0;
        
        // 符号表达式 for p and q (基于原始系数)
        // p = cNorm - bNorm² / 3
        SymbolicExpression symbolP = SymbolicExpression.subtract(
            cNormExpr,
            SymbolicExpression.divide(
                SymbolicExpression.power(bNormExpr, new SymbolicExpression(2.0)),
                new SymbolicExpression(3.0)
            )
        );
        
        // q = (2bNorm³ - 9bNorm cNorm + 27dNorm) / 27
        // 或者等价于：q = (2b³ - 9abc + 27a²d) / (27a³)
        SymbolicExpression numeratorQ = SymbolicExpression.add(
            SymbolicExpression.subtract(
                SymbolicExpression.multiply(new SymbolicExpression(2.0), SymbolicExpression.power(bExpr, new SymbolicExpression(3.0))),
                SymbolicExpression.multiply(
                    new SymbolicExpression(9.0),
                    SymbolicExpression.multiply(
                        SymbolicExpression.multiply(aExpr, bExpr),
                        cExpr
                    )
                )
            ),
            SymbolicExpression.multiply(
                new SymbolicExpression(27.0),
                SymbolicExpression.multiply(
                    SymbolicExpression.power(aExpr, new SymbolicExpression(2.0)),
                    dExpr
                )
            )
        );
        
        SymbolicExpression denominatorQ = SymbolicExpression.multiply(
            new SymbolicExpression(27.0),
            SymbolicExpression.power(aExpr, new SymbolicExpression(3.0))
        );
        
        SymbolicExpression symbolQ = SymbolicExpression.divide(numeratorQ, denominatorQ);

        System.out.println("步骤2: 降次，使用代换 x = t - b/(3a)");
        System.out.println("        结果: t^3 + pt + q = 0");
        System.out.println("        其中 p = " + symbolP + ", q = " + symbolQ);

        // 步骤3: 计算判别式
        double discriminant = (q * q) / 4.0 + (p * p * p) / 27.0;
        
        // 判别式的符号表达式
        SymbolicExpression symbolDiscriminant = SymbolicExpression.add(
            SymbolicExpression.power(SymbolicExpression.divide(symbolQ, new SymbolicExpression(2.0)), new SymbolicExpression(2.0)),
            SymbolicExpression.power(SymbolicExpression.divide(symbolP, new SymbolicExpression(3.0)), new SymbolicExpression(3.0))
        );

        System.out.println("步骤3: 计算判别式 Δ = (q/2)^2 + (p/3)^3 = " + symbolDiscriminant);

        Complex[] roots = new Complex[3];

        if (Math.abs(discriminant) < 1e-10) {
            // 重根情况
            System.out.println("        判别式为零 - 存在重根");
            if (Math.abs(p) < 1e-10) {
                // 三重根
                Complex tRoot = new Complex(-q / 2.0).cbrt();
                roots[0] = tRoot.subtract(new Complex(bNorm / 3.0));
                roots[1] = roots[0];
                roots[2] = roots[0];
                
                // 符号解
                SymbolicExpression symbolTRoot = SymbolicExpression.cbrt(SymbolicExpression.divide(SymbolicExpression.subtract(new SymbolicExpression(0), symbolQ), new SymbolicExpression(2.0)));
                System.out.println("        t = " + symbolTRoot + " = " + tRoot + " 处存在三重根");
            } else {
                // 一个单根和一个二重根
                Complex tRoot1 = new Complex(-3.0 * q / p);
                Complex tRoot2 = new Complex(3.0 * q / (2.0 * p));
                roots[0] = tRoot1.subtract(new Complex(bNorm / 3.0));
                roots[1] = tRoot2.subtract(new Complex(bNorm / 3.0));
                roots[2] = roots[1];
                
                // 符号解
                SymbolicExpression symbolTRoot1 = SymbolicExpression.divide(
                    SymbolicExpression.multiply(new SymbolicExpression(-3.0), symbolQ),
                    symbolP
                );
                SymbolicExpression symbolTRoot2 = SymbolicExpression.divide(
                    SymbolicExpression.multiply(new SymbolicExpression(3.0), symbolQ),
                    SymbolicExpression.multiply(new SymbolicExpression(2.0), symbolP)
                );
                System.out.println("        t = " + symbolTRoot1 + " = " + tRoot1 + " 处存在单根, t = " + symbolTRoot2 + " = " + tRoot2 + " 处存在二重根");
            }
        } else if (discriminant > 0) {
            // 一个实根，两个共轭复根
            System.out.println("        判别式为正 - 一个实根，两个复根");
            Complex sqrtDiscriminant = new Complex(discriminant).sqrt();
            Complex u = new Complex(-q / 2.0).add(sqrtDiscriminant).cbrt();
            Complex v = new Complex(-q / 2.0).subtract(sqrtDiscriminant).cbrt();

            Complex tRoot1 = u.add(v);
            Complex omega = new Complex(-0.5, Math.sqrt(3.0) / 2.0); // 三次单位根
            Complex tRoot2 = u.multiply(omega).add(v.multiply(omega.multiply(omega)));
            Complex tRoot3 = u.multiply(omega.multiply(omega)).add(v.multiply(omega));

            roots[0] = tRoot1.subtract(new Complex(bNorm / 3.0));
            roots[1] = tRoot2.subtract(new Complex(bNorm / 3.0));
            roots[2] = tRoot3.subtract(new Complex(bNorm / 3.0));

            // 符号解
            SymbolicExpression symbolSqrtDiscriminant = SymbolicExpression.sqrt(symbolDiscriminant);
            SymbolicExpression symbolU = SymbolicExpression.cbrt(
                SymbolicExpression.add(
                    SymbolicExpression.divide(SymbolicExpression.subtract(new SymbolicExpression(0), symbolQ), new SymbolicExpression(2.0)),
                    symbolSqrtDiscriminant
                )
            );
            SymbolicExpression symbolV = SymbolicExpression.cbrt(
                SymbolicExpression.subtract(
                    SymbolicExpression.divide(SymbolicExpression.subtract(new SymbolicExpression(0), symbolQ), new SymbolicExpression(2.0)),
                    symbolSqrtDiscriminant
                )
            );
            SymbolicExpression symbolTRoot1 = SymbolicExpression.add(symbolU, symbolV);
            
            System.out.println("        t1 = " + symbolTRoot1 + " = " + tRoot1);
            System.out.println("        t2 = " + tRoot2);
            System.out.println("        t3 = " + tRoot3);
        } else {
            // 三个不同的实根（不可约情况）
            System.out.println("        判别式为负 - 三个不同的实根");
            double rho = Math.sqrt(-(p * p * p) / 27.0);
            double theta = Math.acos(-q / (2.0 * rho));

            Complex tRoot1 = new Complex(2.0 * Math.cbrt(rho) * Math.cos(theta / 3.0));
            Complex tRoot2 = new Complex(2.0 * Math.cbrt(rho) * Math.cos((theta + 2.0 * Math.PI) / 3.0));
            Complex tRoot3 = new Complex(2.0 * Math.cbrt(rho) * Math.cos((theta + 4.0 * Math.PI) / 3.0));

            roots[0] = tRoot1.subtract(new Complex(bNorm / 3.0));
            roots[1] = tRoot2.subtract(new Complex(bNorm / 3.0));
            roots[2] = tRoot3.subtract(new Complex(bNorm / 3.0));

            // 符号解
            SymbolicExpression symbolRho = SymbolicExpression.sqrt(
                SymbolicExpression.subtract(
                    new SymbolicExpression(0),
                    SymbolicExpression.power(SymbolicExpression.divide(symbolP, new SymbolicExpression(3.0)), new SymbolicExpression(3.0))
                )
            );
            SymbolicExpression symbol2Rho = SymbolicExpression.multiply(new SymbolicExpression(2.0), SymbolicExpression.cbrt(symbolRho));
            
            System.out.println("        t1 = 2∛(ρ)cos(θ/3) = " + tRoot1);
            System.out.println("        t2 = 2∛(ρ)cos((θ+2π)/3) = " + tRoot2);
            System.out.println("        t3 = 2∛(ρ)cos((θ+4π)/3) = " + tRoot3);
            System.out.println("        其中 ρ = " + symbolRho + " = " + rho + ", θ = arccos(-q/(2ρ)) = " + theta);
        }

        // 从t转换回x
        SymbolicExpression symbolBOver3A = SymbolicExpression.divide(bNormExpr, new SymbolicExpression(3.0));
        System.out.println("步骤4: 使用 x = t - b/(3a) 从t转换回x");
        System.out.println("        其中 b/(3a) = " + symbolBOver3A);
        System.out.println("        最终根:");
        for (int i = 0; i < 3; i++) {
            System.out.println("        x" + (i + 1) + " = " + roots[i]);
        }

        return roots;
    }

    /**
     * Formats the cubic equation as a string.
     */
    private static String formatEquation(double a, double b, double c, double d) {
        StringBuilder sb = new StringBuilder();

        // Handle x^3 term
        if (Math.abs(a - 1.0) < 1e-10) {
            sb.append("x^3");
        } else if (Math.abs(a + 1.0) < 1e-10) {
            sb.append("-x^3");
        } else {
            sb.append(String.format("%.6g", a)).append("x^3");
        }

        // Handle x^2 term
        if (Math.abs(b) > 1e-10) {
            if (b > 0 && sb.length() > 0) {
                sb.append(" + ");
            } else if (b < 0) {
                sb.append(" - ");
                b = -b;
            }

            if (Math.abs(b - 1.0) < 1e-10) {
                sb.append("x^2");
            } else {
                sb.append(String.format("%.6g", b)).append("x^2");
            }
        }

        // Handle x term
        if (Math.abs(c) > 1e-10) {
            if (c > 0 && sb.length() > 0) {
                sb.append(" + ");
            } else if (c < 0) {
                sb.append(" - ");
                c = -c;
            }

            if (Math.abs(c - 1.0) < 1e-10) {
                sb.append("x");
            } else {
                sb.append(String.format("%.6g", c)).append("x");
            }
        }

        // Handle constant term
        if (Math.abs(d) > 1e-10) {
            if (d > 0 && sb.length() > 0) {
                sb.append(" + ");
            } else if (d < 0) {
                sb.append(" - ");
                d = -d;
            }
            sb.append(String.format("%.6g", d));
        }

        sb.append(" = 0");
        return sb.toString();
    }
}