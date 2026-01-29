## Design.md（设计思路）

### 目标与范围
- **目标**：用一个可运行的 Streamlit Web 应用，把「第一次就能跑起来 —— AI-Coding 实战分享」做成 **6 个可切换章节**，涵盖核心理念、分级体系、Prompt-Coding、Vibe-Coding 1.0/2.0，并提供轻量互动（选择题/练习/对比展示）来辅助讲解。
- **非目标**：不做生产级系统（账号、权限、持久化存储、审计、性能优化、监控、部署流水线等）。
- **约束**：
  - 单文件实现（`ai_coding_demo.py`），便于复制、演示、快速修改。
  - 所有数据均为**示例数据**，运行时内存生成，不依赖外部服务。
  - 端口设置为 8502（避免与其他应用冲突）。

### 技术栈与依赖
- **Python**：3.8+
- **UI 框架**：Streamlit（页面渲染、交互组件）
- **数据结构**：Pandas DataFrame（表格/图表数据）
- **可视化**：Plotly Graph Objects（对比图表）

对应依赖：`requirements.txt`

### 目录结构与职责
```text
260122-vibe_coding分享2.0/
├── ai_coding_demo.py        # 主应用：6 个页面 + 互动
├── requirements.txt         # 依赖
├── start.sh                 # 本地一键启动
├── README.md                # 使用说明
├── Design.md                # 本文件：架构设计
├── Tasks.md                 # 任务列表（开发参考）
├── readme.md                # 原始分享稿（参考）
└── .streamlit/config.toml   # Streamlit 配置（端口 8502）
```

### 运行与配置
- **启动方式**：
  - `./start.sh`：检查 `python3` 与 `streamlit`，缺失则 `pip3 install --user streamlit pandas plotly` 后启动。
  - 或手动：`pip3 install -r requirements.txt` + `streamlit run ai_coding_demo.py`
- **Streamlit 配置**：`.streamlit/config.toml`
  - `address = "0.0.0.0"`：允许外部访问（局域网演示用）
  - `port = 8502`：避免端口冲突
  - `gatherUsageStats = false`：关闭统计

### 总体架构（页面路由 + 组件拼装）
该 Demo 采用 **"单入口 + 路由变量 + if/elif 渲染"** 的结构：

```text
启动 -> Streamlit 载入脚本
  -> st.set_page_config() 设置标题/布局/侧边栏
  -> st.markdown(<style>) 注入全局 CSS（highlight/warning/success 盒子）
  -> st.sidebar.radio() 选择 page（6 选 1）
  -> if/elif 根据 page 渲染对应章节内容与互动
  -> 页脚（固定展示）
```

### UI 设计（可复用的表现层套路）
- **全局 CSS 类**（在 `ai_coding_demo.py` 顶部注入）：
  - `.highlight-box`：主强调信息（蓝色基调）
  - `.warning-box`：风险/反例/警示（黄色基调）
  - `.success-box`：正例/结论/完成状态（绿色基调）
  - `.quote-box`：引用/金句（灰色边框）
- **布局模式**：
  - `st.columns()`：左右对比（例如"适合 vs 不适合"、"1.0 vs 2.0"）
  - `st.tabs()`：同一章节内多视角切换
  - `st.expander()`：折叠详细案例，避免主线过长

### 交互设计（"短、快、可验证"）
交互全部基于 Streamlit 原生控件，强调"10–20 秒内完成一次互动"：

- **章节切换**：`st.sidebar.radio("选择章节", [...6项...])`
- **场景选择**：`st.selectbox(...)` 或 `st.radio(...)` 展示不同文本/示例
  - 页面 1（核心理念）：甜蜜区/三条红线展示 + 练习题
  - 页面 2（分级）：显式逻辑判断说明
  - 页面 3（Prompt-Coding）：房源宣传案例演示
  - 页面 4（Vibe-Coding 1.0）：刚需购房评估案例 + 提示词框架
  - 页面 5（Vibe-Coding 2.0）：规格化迭代流程
  - 页面 6（总结）：核心对比与金句
- **按钮触发**：`st.button(...)` 显示/隐藏解释或结论
- **代码示例**：`st.code(...)` 展示提示词和代码片段

### 数据与可视化（Plotly Graph Objects）
该 Demo 的图表使用 "小样本 + 直观对比" 作为设计原则：

- **对比表格**：使用 Pandas DataFrame + `st.dataframe` 展示不同方案对比
- **流程图示**：使用 Markdown 图示展示步骤流程

### 状态管理与可维护性取舍
- **状态**：不引入额外状态管理；依赖 Streamlit 控件的 key 来维持交互状态。
- **取舍**：
  - **优点**：单文件、低心智成本、改动快，适合演示场景。
  - **缺点**：代码体量大后可读性一般；复用性弱。
- **可演进方向（不强制）**：
  - 把每个章节抽成 `render_xxx()` 函数，形成"路由表"，减少 if/elif 巨块。
  - 把示例数据/文案抽到常量区，便于修改与国际化。

### 扩展指南（新增一个章节怎么做）
1. 在侧边栏 `radio` 的选项列表中追加新章节标题。
2. 在 `if/elif` 路由中新增一个 `elif page == "新标题":` 块。
3. 按既有模板组织内容：
   - 标题（`st.title`）+ 重点盒子（`highlight-box`）
   - 1 个以内互动（`selectbox`/`button`/`tabs` 三选一即可）
   - 若有图表：先用 dict/df 明确数据，再用 Plotly 绘制，最后 `st.plotly_chart`
4. 运行自测：至少点一遍所有控件，确保 key 不冲突、页面无异常。

### 章节概览（6个）
1. 🎯 开场 & 核心理念 - AI-Coding 的甜蜜区与三条红线
2. 📊 AI-Coding的分级 - 显式逻辑的分水岭
3. 💬 Prompt-Coding - 一句话AI自己跑
4. 🔧 Vibe-Coding 1.0 - 按我定的规则跑
5. 🚀 Vibe-Coding 2.0 - 按我定的规则迭代
6. ✅ 总结 - 核心对比与金句

### 核心设计原则
1. **渐进式呈现**：从最简单的 Prompt-Coding 到复杂的 Vibe-Coding 2.0
2. **实例驱动**：每个概念都有具体案例（房源宣传、刚需购房评估）
3. **对比强化**：通过对比表格和案例强化理解
4. **互动验证**：提供练习题和选择题让用户自测
5. **可操作性**：提供提示词框架，可直接复制使用
