#!/bin/bash
# 运行Python方程求解器的脚本

echo "========================================"
echo "Python方程求解器"
echo "========================================"

# 检查Python版本
if ! command -v python3 &> /dev/null; then
    echo "错误: Python 3 未安装"
    exit 1
fi

# 检查是否在虚拟环境中
if [ -z "$VIRTUAL_ENV" ]; then
    echo "未检测到虚拟环境，尝试创建..."
    python3 -m venv venv
    source venv/bin/activate
    echo "虚拟环境已激活"
    pip install -q -r requirements.txt
else
    echo "虚拟环境已激活: $VIRTUAL_ENV"
fi

echo ""
echo "运行方程求解器..."
python3 src/main.py
