# 使用说明

## 🎯 项目介绍

这是一个基于 Streamlit 的互动演示应用，展示了 AI-Coding 的核心理念、分级体系和实践方法。

## 📦 快速启动

### 方式一：一键启动（推荐）

```bash
chmod +x start.sh
./start.sh
```

### 方式二：手动启动

1. 安装依赖：
```bash
pip3 install -r requirements.txt
```

2. 启动应用：
```bash
streamlit run ai_coding_demo.py
```

或者：
```bash
python3 -m streamlit run ai_coding_demo.py
```

3. 访问应用：
打开浏览器访问 `http://localhost:8501`

## 🔧 端口配置

默认端口为 **8501**（适配云平台健康检查）。

如需修改端口，编辑 `.streamlit/config.toml`：
```toml
[server]
port = 你的端口号
```

## 📚 章节概览

### 1. 🎯 开场 & 核心理念
- 核心金句与反直觉结论
- 我们今天不追求什么
- AI-Coding 的甜蜜区（三个特征）
- 三条警示线（什么不适合）
- 场景判断练习题（基础题+进阶题）

### 2. 📊 AI-Coding 的方式
- 一刀切的判断问题：需不需要把「规则写出来」
- 三种方式的核心差异
- 如何判断该用哪种

### 3. 💬 Prompt-Coding
- 一句话定义与特点
- 适用场景判断标准
- 图书馆预约展示页面案例（四步流程）
- Prompt-Coding 的止损线

### 4. 🔧 Vibe-Coding 1.0 - 正确姿势
- 核心原则：人负责想清楚，AI 负责执行
- 两步法：锁目标 + 拆小步
- 图书馆预约系统案例
- 锁目标三步骤（互动式展开）
- 拆小步示例（互动式任务列表）

### 5. 👥 Vibe-Coding 1.0 - 分组研讨
- 研讨目标与规则
- 讨论要点
- 参考模板（可复制）

### 6. 🚀 Vibe-Coding 2.0
- 为什么要 2.0
- 2.0 做的三件事
- 什么时候真的需要 2.0

### 7. ✅ 分享总结 & 金句
- 三种方法核心对比表格
- 四条核心金句
- 三条行动建议

## ⚙️ 技术栈

- **Python** 3.8+
- **Streamlit** 1.28.0+（Web 框架）
- **Pandas** 2.0.0+（数据处理）
- **Plotly** 5.17.0+（图表可视化）

## 📁 项目结构

```
260122-vibe_coding分享2.0/
├── ai_coding_demo.py        # 主应用（7个互动章节）
├── requirements.txt         # Python 依赖
├── start.sh                 # 一键启动脚本
├── USAGE.md                 # 本文件：使用说明
├── Tasks.md                 # 任务拆解（开发参考）
├── definations.md           # 分享稿定义文档
└── .streamlit/
    └── config.toml          # Streamlit 配置
```

## 💡 使用建议

- **演示场景**：适合 40 分钟的分享会
- **自学场景**：可以按章节顺序学习
- **参考场景**：提示词框架可直接复制使用

## 🚀 开发时间

- 使用 AI-Coding 方式开发
- 从需求到可运行原型：约半天
- 完整测试与优化：约 30 分钟

## ❓ FAQ

### Q: 为什么用 8501 端口？
A: 云平台健康检查默认访问 8501，使用该端口便于通过部署校验。

### Q: 如何修改内容？
A: 直接编辑 `ai_coding_demo.py`，所有内容都在对应的章节 if/elif 块中。

### Q: 依赖安装失败怎么办？
A: 尝试使用国内镜像源：
```bash
pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Q: 应用无法启动？
A: 检查以下几点：
1. Python 版本是否 >= 3.8
2. 依赖是否正确安装
3. 端口 8501 是否被占用

### Q: 如何停止应用？
A: 在终端中按 `Ctrl+C`

## 📧 反馈

如有问题或建议，欢迎反馈！

---

💡 **这个 Demo 本身就是用 AI-Coding 方式制作的 —— 快速、够用、可验证！**
