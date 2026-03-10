# 快速开始指南

## 两个工程的完整对比

### 1. Python版本

**位置**: `python-version/`

**核心文件**:
- `src/equation_solver.py` - 求解器核心逻辑
  - `ComplexNumber` - 复数类
  - `EquationSolver` - 静态方法求解各类方程
  - `EquationSolution` - 解的封装

- `src/verifier.py` - 验证器
  - `SolutionVerifier` - 验算逻辑
  - `VerificationResult` - 验证结果封装

**运行方式**:
```bash
cd python-version
python3 src/main.py
```

**示例代码**:
```python
from src.equation_solver import EquationSolver
from src.verifier import SolutionVerifier

# 求解并验证
solution = EquationSolver.solve_quadratic(1, -5, 6)
verifier = SolutionVerifier()
results = verifier.verify_quadratic(1, -5, 6, solution.roots)

# 打印详细步骤
EquationSolver.print_solution(solution)
verifier.print_verification_results(results)
```

---

### 2. Java版本

**位置**: `java-version/`

**核心文件**:
- `src/main/java/com/equation/Complex.java` - 复数类
- `src/main/java/com/equation/QuadraticSolver.java` - 二次方程求解器
- `src/main/java/com/equation/CubicSolver.java` - 三次方程求解器
- `src/main/java/com/equation/QuarticSolver.java` - 四次方程求解器
- `src/main/java/com/equation/verifier/*.java` - 各类验证器

**运行方式**:
```bash
cd java-version
mvn exec:java -Prun
```

**示例代码**:
```java
import com.equation.*;
import com.equation.verifier.*;

// 求解
Complex[] roots = QuadraticSolver.solve(1, -5, 6);

// 验证
boolean verified = QuadraticVerifier.verify(1, -5, 6, roots);
```

---

## 对比表格

| 特性 | Python版本 | Java版本 |
|------|-----------|---------|
| **复数支持** | `ComplexNumber`类 | `Complex`类 |
| **求解器结构** | 静态方法集 | 独立类 |
| **验证器结构** | 统一类 | 各类型独立类 |
| **依赖** | NumPy | 无外部依赖 |
| **构建工具** | pip | Maven |
| **测试框架** | pytest | 手动测试用例 |
| **代码行数** | ~500行 | ~800行 |
| **精确表达式** | 支持 | 支持 |
| **详细步骤** | 支持 | 支持 |

---

## 常见问题

### Q1: 如何添加新的测试方程？

**Python**:
编辑 `src/main.py` 中的 `main()` 函数，添加测试用例。

**Java**:
编辑 `src/main/java/com/equation/Main.java`，在 `main()` 中添加测试。

### Q2: 如何查看详细的数学推导？

参考原始文档：
- `二次、三次、四次方程求解详解与代码实现-python版.md`
- `二次、三次、四次方程求解详解与代码实现-java版.md`

### Q3: 精度问题如何处理？

- **Python**: 使用 `1e-10` 作为误差阈值
- **Java**: 使用 `1e-8` 作为误差阈值
- 验证器会显示每个根的误差值

### Q4: 复数输出格式？

**Python**: `a + bi` 格式
**Java**: `a + bi` 格式（实部和虚部保留6位小数）

---

## 下一步

1. **阅读详细文档**: `python-version/README.md` 和 `java-version/README.md`
2. **运行示例**: 使用各自的 `run.sh` 脚本
3. **查看源码**: 两个版本的核心算法实现
4. **自定义测试**: 修改 `main.py` 或 `Main.java` 添加自己的测试方程
