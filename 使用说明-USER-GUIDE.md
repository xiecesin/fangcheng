# 🎯 如何使用这两个方程求解工程

## 快速开始

### 选择适合你的版本

| 需求 | 推荐版本 |
|------|---------|
| 喜欢Python，快速上手 | ✅ **Python版本** |
| 学习Java，面向对象实践 | ✅ **Java版本** |
| 科学计算，数值分析 | ✅ Python + NumPy |
| 纯手工实现，理解原理 | ✅ Java（无外部依赖） |
| 需要测试框架 | ✅ Python（pytest） |
| 需要Maven构建 | ✅ Java |

---

## Python版本使用指南

### 1️⃣ 运行方式

```bash
# 方式1: 使用运行脚本（推荐）
cd python-version
./run.sh

# 方式2: 手动运行
cd python-version
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 src/main.py
```

### 2️⃣ 交互式使用

运行后会看到：

```
Equation Solver
========================================
Solve quadratic, cubic, and quartic equations with detailed steps

Select equation type:
1. Quadratic (ax² + bx + c = 0)
2. Cubic (ax³ + bx² + cx + d = 0)
3. Quartic (ax⁴ + bx³ + cx² + dx + e = 0)
4. Exit
```

按提示输入即可。

### 3️⃣ 编程方式使用

```python
from src.equation_solver import EquationSolver
from src.verifier import SolutionVerifier

# 求解二次方程 x² - 5x + 6 = 0
solution = EquationSolver.solve_quadratic(1, -5, 6)

# 打印详细步骤
EquationSolver.print_solution(solution)

# 验证解
verifier = SolutionVerifier()
results = verifier.verify_quadratic(1, -5, 6, solution.roots)
verifier.print_verification_results(results)
```

### 4️⃣ 运行测试

```bash
cd python-version
pytest tests/
# 或带覆盖率
pytest --cov=src --cov-report=term-missing tests/
```

---

## Java版本使用指南

### 1️⃣ 运行方式

```bash
# 方式1: 使用运行脚本（推荐）
cd java-version
./run.sh

# 方式2: 使用Maven
cd java-version
mvn exec:java -Prun

# 方式3: 打包后运行
mvn package
java -jar target/equation-solver-1.0.0.jar
```

### 2️⃣ 直接查看输出

运行后会自动执行所有测试用例，输出类似：

```
========================================
Quadratic Equation Tests
========================================
Test 1: x² - 5x + 6 = 0
Roots: [2.0, 3.0]
Verification: All roots verified!

Test 2: x² + 1 = 0
Roots: [0.0+1.0i, 0.0-1.0i]
Verification: All roots verified!
...
```

### 3️⃣ 编程方式使用

```java
import com.equation.*;
import com.equation.verifier.*;

public class MyApp {
    public static void main(String[] args) {
        // 求解二次方程 x² - 5x + 6 = 0
        Complex[] roots = QuadraticSolver.solve(1, -5, 6);

        // 验证解
        boolean verified = QuadraticVerifier.verify(1, -5, 6, roots);
        System.out.println("Verified: " + verified);
    }
}
```

### 4️⃣ 编译和构建

```bash
# 编译
mvn compile

# 运行测试（如果有）
mvn test

# 打包
mvn package

# 清理
mvn clean
```

---

## 两个版本的核心功能对比

### 功能完全一致

| 功能 | Python | Java |
|------|--------|------|
| 二次方程求解 | ✅ | ✅ |
| 三次方程求解 | ✅ | ✅ |
| 四次方程求解 | ✅ | ✅ |
| 复数支持 | ✅ | ✅ |
| 详细步骤 | ✅ | ✅ |
| 精确表达式 | ✅ | ✅ |
| 验证功能 | ✅ | ✅ |
| 误差分析 | ✅ | ✅ |

---

## 常见使用场景

### 场景1: 学习方程求解

运行程序，输入不同的系数，观察详细的求解步骤。

**推荐**: 两个版本都可以，根据你的编程语言偏好选择。

### 场景2: 验证数学作业答案

使用验证功能，将你手算的答案代入验证。

```python
# Python示例
verifier.verify_quadratic(1, -5, 6, [2, 3])  # 验证 x=2 和 x=3
```

```java
// Java示例
QuadraticVerifier.verify(1, -5, 6, new Complex[]{new Complex(2), new Complex(3)});
```

### 场景3: 集成到其他项目

两个版本都设计为模块化，可以轻松集成。

**Python**: 直接 `import` 使用
**Java**: 将类文件复制到你的项目中，或打包成jar

### 场景4: 教学演示

使用详细步骤输出功能，向学生展示完整的求解过程。

---

## 输入系数说明

### 二次方程: ax² + bx + c = 0

输入: `a, b, c`

示例: `1, -5, 6` 对应 `x² - 5x + 6 = 0`

### 三次方程: ax³ + bx² + cx + d = 0

输入: `a, b, c, d`

示例: `1, -6, 11, -6` 对应 `x³ - 6x² + 11x - 6 = 0`

### 四次方程: ax⁴ + bx³ + cx² + dx + e = 0

输入: `a, b, c, d, e`

示例: `1, 0, -5, 0, 4` 对应 `x⁴ - 5x² + 4 = 0`

---

## 输出说明

### 解的形式

- **实数**: `3.0` 或 `-2.5`
- **复数**: `1.0 + 2.0i` 或 `-1.5 - 0.5i`
- **精确表达式**: `(5 + √1)/2` 或 `(-2 + 4i)/2`

### 验证结果

- **通过**: `✓ Verified! Error: 0.0`
- **失败**: `✗ Failed! Error: 0.00123`
- 误差 < 1e-10 视为通过

---

## 故障排除

### Python版本

**问题**: `ModuleNotFoundError: No module named 'numpy'`
```
解决: 安装依赖
pip install -r requirements.txt
```

**问题**: `SyntaxError` 或版本问题
```
解决: 确保使用Python 3.8+
python3 --version
```

### Java版本

**问题**: `command not found: mvn`
```
解决: 安装Maven
```

**问题**: `error: invalid source release: 11`
```
解决: 确保Java版本 >= 11
java --version
```

---

## 下一步学习

1. **阅读源码**: 两个版本的实现都很清晰，适合学习
2. **修改算法**: 尝试实现不同的求解方法
3. **添加功能**: 比如绘图、更高级的验证等
4. **对比学习**: 同时看两个版本，理解不同语言的实现差异

---

## 获取帮助

- 阅读详细的README文档
- 查看示例输出文档
- 检查原始的数学推导文档
- 运行测试用例理解行为

**两个工程都是完整可运行的，祝你使用愉快！** 🎉
