# 快速开始指南

## 两个工程的完整对比

### 1. Python版本

**位置**: `python-version/`

**核心文件**:
- `src/equation_solver.py` - 求解器核心逻辑
  - `SymbolicSolver` - 符号求解器（使用SymPy）
  - `MarkdownExporter` - Markdown导出器
  - `EquationSolution` - 解的封装

- `src/main.py` - 主程序
  - 交互式CLI界面
  - 内置验证功能

**运行方式**:
```bash
cd python-version
python3 src/main.py
```

**示例代码**:
```python
from src.equation_solver import SymbolicSolver, MarkdownExporter

# 求解二次方程
solution = SymbolicSolver.solve_quadratic(1, -5, 6, verbose=True)

# 求解三次方程
solution = SymbolicSolver.solve_cubic(1, -6, 11, -6, verbose=True)

# 求解四次方程
solution = SymbolicSolver.solve_quartic(1, 0, -5, 0, 4, verbose=True)

# 导出为Markdown文件
MarkdownExporter.export_solution(solution, "solution.md")
```

**说明**：
- 使用SymPy进行符号计算，返回精确解
- `verbose=True` 会打印详细的求解步骤
- 验证功能已内置，求解后自动验证
- 结果自动保存到 `solutions/` 目录下的Markdown文件

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
| **复数支持** | SymPy内置复数 | `Complex`类 |
| **求解器结构** | `SymbolicSolver`类 | 独立类 |
| **验证器结构** | 内置验证 | 各类型独立类 |
| **依赖** | SymPy | 无外部依赖 |
| **构建工具** | pip | Maven |
| **测试框架** | pytest | 手动测试用例 |
| **代码行数** | ~700行 | ~800行 |
| **精确表达式** | SymPy符号计算 | 支持 |
| **详细步骤** | 支持 | 支持 |
| **Markdown导出** | 支持 | 不支持 |

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
