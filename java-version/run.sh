#!/bin/bash
# 运行Java方程求解器的脚本

echo "========================================"
echo "Java方程求解器"
echo "========================================"

# 检查Java
if ! command -v java &> /dev/null; then
    echo "错误: Java 未安装"
    exit 1
fi

# 检查Maven
if ! command -v mvn &> /dev/null; then
    echo "错误: Maven 未安装"
    exit 1
fi

echo "Java版本: $(java -version 2>&1 | head -n 1)"
echo "Maven版本: $(mvn -version | head -n 1)"
echo ""

# 构建项目
echo "构建项目..."
mvn clean compile -q

if [ $? -eq 0 ]; then
    echo "构建成功！"
    echo ""
    echo "运行方程求解器..."
    mvn exec:java -Prun
else
    echo "构建失败！"
    exit 1
fi
