# 方程求解器 (Fangcheng Equation Solver)

这是一个完整的二次、三次、四次方程求解系统，包含Python和Java两个完整可运行的版本。

## 项目结构

```
fangcheng/
├── python-version/      # Python版本工程（SymPy符号计算）
│   ├── src/
│   │   ├── equation_solver.py  # 符号求解器核心
│   │   ├── verifier.py         # 验算器（保留）
│   │   └── main.py             # 主程序（交互式CLI）
│   ├── solutions/              # 自动生成的求解结果
│   ├── tests/                  # 测试文件
│   ├── requirements.txt        # Python依赖
│   ├── run.sh                  # 运行脚本
│   └── README.md               # Python版本说明
│
├── java-version/        # Java版本工程
│   ├── src/main/java/com/equation/
│   │   ├── Complex.java        # 复数类
│   │   ├── QuadraticSolver.java
│   │   ├── CubicSolver.java
│   │   ├── QuarticSolver.java
│   │   └── verifier/           # 验证器
│   ├── pom.xml                 # Maven配置
│   ├── run.sh                  # 运行脚本
│   └── README.md               # Java版本说明
│
├── README.md                    # 本文件
└── [原始文档文件...]
```

## 功能特性

两个版本均支持：

### 1. 二次方程求解
- 标准形式：`ax² + bx + c = 0`
- 显示判别式计算过程
- 支持实根、复根、重根
- 使用求根公式：`x = (-b ± √Δ)/(2a)`

### 2. 三次方程求解
- 标准形式：`ax³ + bx² + cx + d = 0`
- 使用卡尔达诺公式 (Cardano's method)
- 显示既约三次方程转换过程
- 支持三个实根、一个实根+两个复根等情况

### 3. 四次方程求解
- 标准形式：`ax⁴ + bx³ + cx² + dx + e = 0`
- 使用费拉里方法 (Ferrari's method)
- 显示预解三次方程求解过程
- 支持四个实根、复根组合等情况

### 4. 验算功能
- 将每个根代入原方程验证
- 显示逐项计算过程
- 误差分析（< 1e-10 视为通过）
- 支持精确表达式验证

## 使用方法

### Python版本

```bash
# 进入Python工程目录
cd python-version

# 运行（会自动创建虚拟环境并安装依赖）
./run.sh

# 或手动运行
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 src/main.py
```

### Java版本

```bash
# 进入Java工程目录
cd java-version

# 运行（需要Java 11+ 和 Maven）
./run.sh

# 或手动构建运行
mvn clean compile
mvn exec:java -Prun

# 打包成jar
mvn package
java -jar target/equation-solver-1.0.0.jar
```

## 测试用例

两个版本都包含以下测试用例：

### 二次方程
1. `x² - 5x + 6 = 0` → 根：2, 3（两个实根）
2. `x² + 1 = 0` → 根：i, -i（复根）
3. `x² - 4x + 4 = 0` → 根：2, 2（重根）

### 三次方程
1. `x³ - 6x² + 11x - 6 = 0` → 根：1, 2, 3（三个实根）
2. `x³ - 1 = 0` → 根：1, -0.5±0.866i（一个实根+两个复根）
3. `x³ - 3x² + 3x - 1 = 0` → 根：1, 1, 1（三重根）

### 四次方程
1. `x⁴ - 5x² + 4 = 0` → 根：±1, ±2（四个实根）
2. `x⁴ - 10x³ + 35x² - 50x + 24 = 0` → 根：1, 2, 3, 4
3. `x⁴ + 1 = 0` → 四个复根

## 技术特点

### Python版本
- **符号计算**：使用SymPy进行符号计算，返回精确解
- **Markdown导出**：自动将求解过程导出为带LaTeX公式的Markdown文件
- **交互式CLI**：支持中英文逗号和空格分隔的系数输入
- **内置验证**：求解后自动验证所有根的正确性
- **详细步骤**：显示完整的数学推导过程

### Java版本
- 完整的复数类实现
- 每个求解器都是独立类，便于维护
- 详细的步骤输出，便于教学
- Maven构建系统
- 无外部依赖（纯Java实现）

## 原始文档

原始的详细推导和代码实现文档：
- `二次、三次、四次方程求解详解与代码实现-python版.md`
- `二次、三次、四次方程求解详解与代码实现-java版.md`
- `python和java实现再给出方法来验算解，也是要用精确表达式，并且打印每一步计算过程.md`

## 系统要求

- **Python版本**: Python 3.8+，SymPy
- **Java版本**: Java 11+，Maven 3.6+

## 许可证

MIT License
