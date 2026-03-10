# 方程求解器

一个功能全面的Python库，用于求解二次、三次和四次方程，提供详细的分步解决方案和验证功能。

## 功能特性

- **二次方程**: 求解形如 `ax² + bx + c = 0` 的方程
- **三次方程**: 使用卡尔达诺公式求解形如 `ax³ + bx² + cx + d = 0` 的方程
- **四次方程**: 使用数值方法求解形如 `ax⁴ + bx³ + cx² + dx + e = 0` 的方程
- **分步解决方案**: 显示每个解的详细数学步骤
- **精确表达式显示**: 正确格式化复数和数学表达式
- **解验证**: 通过将解代入原方程自动验证解的正确性
- **面向对象设计**: 遵循Python最佳实践的清晰、模块化架构

## 安装

```bash
# 克隆仓库
git clone https://github.com/yourusername/equation-solver.git
cd equation-solver

# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Windows上：venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

## 使用方法

### 命令行界面

运行主程序以交互式方式求解方程：

```bash
python src/main.py
```

CLI将引导您选择方程类型并输入系数。

### 程序化使用

```python
from src.equation_solver import EquationSolver
from src.verifier import SolutionVerifier

# 求解二次方程：x² - 5x + 6 = 0
solution = EquationSolver.solve_quadratic(1, -5, 6)

# 打印详细解决方案
EquationSolver.print_solution(solution)

# 验证解
verifier = SolutionVerifier()
verification_results = verifier.verify_quadratic(1, -5, 6, solution.roots)
verifier.print_verification_results(verification_results)
```

## 支持的方程类型

### 二次方程
- 形式: `ax² + bx + c = 0`
- 使用二次公式: `x = (-b ± √(b² - 4ac)) / (2a)`
- 处理实根和复根

### 三次方程
- 形式: `ax³ + bx² + cx + d = 0`
- 使用带降次变换的卡尔达诺公式
- 处理所有情况: 三个实根、一个实根+两个复根或重根

### 四次方程
- 形式: `ax⁴ + bx³ + cx² + dx + e = 0`
- 使用数值方法实际求解
- 返回所有四个根（实根和/或复根）

## 测试

运行测试套件以验证功能：

```bash
# 运行所有测试
pytest tests/

# 带覆盖率运行
pytest --cov=src --cov-report=term-missing tests/
```

## 示例输出

对于二次方程 `x² - 5x + 6 = 0`：

```
二次方程解决方案
==================================================

原方程：
  公式：x² - 5x + 6 = 0

计算判别式：
  公式：D = b² - 4ac = (-5)² - 4(1)(6)
  结果：D = 1

应用二次公式：
  公式：x = (-b ± √D) / (2a)
  结果：x₁ = 3, x₂ = 2

最终根：
  x1 = 3
  x2 = 2

验证结果
========================================
  根 1: ✓ 有效
    根值: 3.0
    代入值: 0.0
  根 2: ✓ 有效
    根值: 2.0
    代入值: 0.0

总体结果: 所有解验证成功！
```

## 依赖

- **Python 3.8+**
- **NumPy** (用于四次方程求解器中的数值计算)
- **pytest** (用于测试)

## 开发

该项目遵循PEP 8编码标准，并使用：
- **black** 用于代码格式化
- **isort** 用于导入排序
- **ruff** 用于代码检查
- **mypy** 用于类型检查

## 许可证

MIT许可证