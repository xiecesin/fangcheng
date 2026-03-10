# Java方程求解器

一个功能全面的Java库，用于求解2次、3次和4次多项式方程（二次、三次和四次方程）。该求解器提供详细的分步解决方案，并包含验证功能以确保正确性。

## 功能特性

- **二次求解器**: 求解形如 `ax² + bx + c = 0` 的方程
- **三次求解器**: 使用卡尔达诺公式求解形如 `ax³ + bx² + cx + d = 0` 的方程
- **四次求解器**: 使用法拉利方法求解形如 `ax⁴ + bx³ + cx² + dx + e = 0` 的方程
- **复数支持**: 无缝处理实根和复根
- **分步解决方案**: 显示每个解的详细数学步骤
- **验证功能**: 通过将解代入原方程自动验证解的正确性
- **多个测试用例**: 包含涵盖各种场景的综合测试用例

## 使用的数学方法

### 二次方程
使用标准二次公式：`x = (-b ± √(b² - 4ac)) / (2a)`

### 三次方程
使用卡尔达诺公式：
1. 归一化为首一多项式
2. 降次（消除x²项）
3. 使用降次三次方程公式求解
4. 处理所有情况：三个实根、一个实根+两个复根或重根

### 四次方程
使用费拉里方法：
1. 归一化为首一多项式
2. 降次（消除x³项）
3. 求解三次预解方程
4. 分解为两个二次方程并求解

## 安装

### 前置要求
- Java 11 或更高版本
- Maven 3.6 或更高版本（用于构建）

### 构建项目
```bash
# 进入项目目录
cd /path/to/equation-solver

# 构建项目
mvn clean package

# 运行应用程序
mvn exec:java -Prun
# 或
java -jar target/equation-solver-1.0.0.jar
```

## 使用示例

### 二次方程
```java
// 求解 x² - 5x + 6 = 0
Complex[] roots = QuadraticSolver.solve(1, -5, 6);
```

### 三次方程
```java
// 求解 x³ - 6x² + 11x - 6 = 0
Complex[] roots = CubicSolver.solve(1, -6, 11, -6);
```

### 四次方程
```java
// 求解 x⁴ - 5x² + 4 = 0
Complex[] roots = QuarticSolver.solve(1, 0, -5, 0, 4);
```

### 验证
```java
// 验证二次方程解
boolean verified = QuadraticVerifier.verify(1, -5, 6, roots);

// 验证三次方程解
boolean verified = CubicVerifier.verify(1, -6, 11, -6, roots);

// 验证四次方程解
boolean verified = QuarticVerifier.verify(1, 0, -5, 0, 4, roots);
```

## 包含的测试用例

主应用程序包含以下测试用例：

### 二次方程测试
1. `x² - 5x + 6 = 0` → 根: 2, 3
2. `x² + 1 = 0` → 根: i, -i
3. `x² - 4x + 4 = 0` → 重根: 2

### 三次方程测试
1. `x³ - 6x² + 11x - 6 = 0` → 根: 1, 2, 3
2. `x³ - 1 = 0` → 根: 1, -0.5±0.866i
3. `x³ - 3x² + 3x - 1 = 0` → 三重根: 1

### 四次方程测试
1. `x⁴ - 5x² + 4 = 0` → 根: ±1, ±2
2. `x⁴ - 10x³ + 35x² - 50x + 24 = 0` → 根: 1, 2, 3, 4
3. `x⁴ + 1 = 0` → 四个复根

## 项目结构

```
src/
├── main/
│   └── java/
│       └── com/
│           └── equation/
│               ├── Complex.java          # 复数类实现
│               ├── QuadraticSolver.java  # 二次方程求解器
│               ├── CubicSolver.java      # 三次方程求解器
│               ├── QuarticSolver.java    # 四次方程求解器
│               ├── Main.java             # 主应用程序，包含测试用例
│               └── verifier/             # 验证类
│                   ├── QuadraticVerifier.java
│                   ├── CubicVerifier.java
│                   └── QuarticVerifier.java
pom.xml                                   # Maven构建配置
README.md                                 # 本文档
```

## 精度和限制

- **精度**: 使用双精度浮点运算
- **容差**: 验证时使用1e-8的容差进行浮点比较
- **边界情况**: 处理特殊情况，如重根、复根和退化情况
- **性能**: 针对清晰度和教育目的进行了优化，而非极致性能

## 许可证

该项目是开源的，可在MIT许可证下使用。

## 作者

作为方程求解项目的一部分创建。