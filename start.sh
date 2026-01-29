#!/bin/bash

# 检查 Python 是否安装
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装，请先安装 Python 3.8+"
    exit 1
fi

echo "✅ Python 版本: $(python3 --version)"

# 检查 streamlit 是否安装
if ! python3 -c "import streamlit" &> /dev/null; then
    echo "📦 Streamlit 未安装，正在安装依赖..."
    pip3 install --user -r requirements.txt
fi

# 启动应用
echo "🚀 启动 AI-Coding 演示应用 (端口: 8501)..."
streamlit run ai_coding_demo.py
