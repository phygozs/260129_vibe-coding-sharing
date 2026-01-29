"""
第一次就能跑起来 —— AI-Coding 实战分享
一个用 AI-Coding 方式制作的关于 AI-Coding 的演示
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 页面配置
st.set_page_config(
    page_title="AI-Coding 实战分享",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义 CSS
st.markdown("""
<style>
    .big-font {
        font-size: 24px !important;
        font-weight: bold;
        color: #1f77b4;
    }
    .highlight-box {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 10px 0;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ffc107;
        margin: 10px 0;
    }
    .success-box {
        background-color: #d4edda;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin: 10px 0;
    }
    .quote-box {
        background-color: #f9f9f9;
        padding: 15px 20px;
        border-radius: 8px;
        border-left: 4px solid #666;
        margin: 15px 0;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# 侧边栏导航
st.sidebar.title("📚 导航")
page = st.sidebar.radio(
    "选择章节",
    ["🎯 开场 & 核心理念", "📊 AI-Coding 方式", "💬 Prompt-Coding", 
     "🔧 Vibe-Coding 1.0", "👥 思考题", 
     "🚀 Vibe-Coding 2.0", "✅ 分享总结"]
)

# ============================================
# 页面 1: 开场 & 核心理念
# ============================================
if page == "🎯 开场 & 核心理念":
    st.title("第一次就能跑起来：AI-Coding 实战分享")
    
    st.markdown("""
    <div class="highlight-box" style="padding: 30px;">
    <b>🎤 开始前，先抛一个反直觉的结论:</b>
    </p>
    <p style="font-size: 18px; line-height: 1.8; margin-bottom: 25px;">
    虽然今天我们讲的是 AI-Coding，但这场分享的目标，不是把你变成程序员<br><br>
    <h4 style="margin-bottom: 20px;">你只需要会一件事：把你真正想做的事情，说清楚。</h4>
    </p>
    <p style="font-size: 32px; text-align: center; font-weight: bold; color: #1f77b4; line-height: 1.5; padding: 20px; background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    让真正懂业务的人，第一次就能把想法直接「跑起来」
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="warning-box">
        <h4 style="text-align: center;">❌ 不追求长期</h4>
        <p style="text-align: center;">你是业务人员、老师、运营、产品<br>而不是工程师</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="warning-box">
        <h4 style="text-align: center;">❌ 不追求完美</h4>
        <p style="text-align: center;">第一次交付<br>只要能用、能判断对错就够</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="success-box">
        <h4 style="text-align: center;">✅ 追求讲清楚</h4>
        <p style="text-align: center;">跑起来，更形象<br>而不是"看起来好高级"</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 左右分栏：甜蜜区 + 警示线
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div style="border-left: 8px solid #28a745; background: #f0f8ff; padding: 30px 25px; border-radius: 10px; height: 100%;">
        <h3 style="margin-bottom: 25px; display: flex; align-items: center;"><span style="font-size: 24px; margin-right: 10px;">✅</span>AI-Coding 的「甜蜜区」</h3>
        
        <h4 style="margin-top: 25px; margin-bottom: 12px;">目标是验证</h4>
        <ul style="font-size: 16px; line-height: 1.8; margin-bottom: 25px;">
            <li>这个需求值不值得做？</li>
            <li>流程顺不顺？</li>
            <li>学生/用户会不会真的用？</li>
        </ul>
        
        <h4 style="margin-top: 25px; margin-bottom: 12px;">短周期、低成本</h4>
        <ul style="font-size: 16px; line-height: 1.8; margin-bottom: 25px;">
            <li>半天～几天就能看到结果</li>
            <li>做坏了，直接丢掉重来</li>
        </ul>
        
        <h4 style="margin-top: 25px; margin-bottom: 12px;">需求可描述</h4>
        <ul style="font-size: 16px; line-height: 1.8;">
            <li>你能说清楚什么算成功，什么算失败</li>
            <li>哪怕你完全不懂技术</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="border-left: 8px solid #ffc107; background: #fffbf0; padding: 30px 25px; border-radius: 10px; height: 100%;">
        <h3 style="margin-bottom: 25px; display: flex; align-items: center;"><span style="font-size: 24px; margin-right: 10px;">⚠️</span>AI-Coding 的三条「警示」线</h3>
        
        <h4 style="margin-top: 25px; margin-bottom: 12px;">❌ 核心业务系统</h4>
        <ul style="font-size: 16px; line-height: 1.8; margin-bottom: 25px;">
            <li>真实交易</li>
            <li>计费、学籍、权限核心链路</li>
        </ul>
        
        <h4 style="margin-top: 25px; margin-bottom: 12px;">❌ 长期运行系统</h4>
        <ul style="font-size: 16px; line-height: 1.8; margin-bottom: 25px;">
            <li>要稳定跑 3-5 年</li>
            <li>多人长期维护</li>
        </ul>
        
        <h4 style="margin-top: 25px; margin-bottom: 12px;">❌ 高风险场景</h4>
        <ul style="font-size: 16px; line-height: 1.8;">
            <li>高并发</li>
            <li>高安全</li>
            <li>高合规</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="quote-box">
    <h4>🤔 为什么？</h4>
    <p style="font-size: 18px;">
    <b>AI 更擅长「拼装」，而不是「打地基」</b>
    </p>
    <ul style="font-size: 16px;">
        <li>很适合快速做一个「能用的样子」</li>
        <li>在验证阶段用 AI 快速跑一轮，就像先做一次公开课或内测班；一旦发现不合适，可以马上调整，而不是等正式上线后再推倒重来</li>
        <li>前期没有清晰结构和标准，后期会变成"没人敢改、没人能接"的系统，就像没有统一教案的课程，越教越乱</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 练习题
    st.markdown("### 🎯 场景判断练习")
    st.write("判断以下场景是否适合用 AI-Coding：")
    
    quiz_type = st.radio(
        "选择题目类型：",
        ["基础题（明确适合/不适合）", "进阶题（灰区判断）"],
        horizontal=True
    )
    
    if quiz_type == "基础题（明确适合/不适合）":
        scenarios = {
            "做一个内部数据看板，验证团队是否真的需要": "✅ 适合",
            "开发公司核心 ERP 系统": "❌ 不适合",
            "临时活动报名页面（活动结束就下线）": "✅ 适合",
            "客户数据管理系统（长期使用）": "❌ 不适合",
            "做一个新审批流程演示，让 10 个人试用找卡点": "✅ 适合",
            "公司官网的在线客服系统（7×24 小时）": "❌ 不适合"
        }
        
        for i, (scenario, answer) in enumerate(scenarios.items()):
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"**{scenario}**")
            with col2:
                if st.button("适合", key=f"yes_{i}"):
                    if answer == "✅ 适合":
                        st.success("✅ 正确")
                    else:
                        st.error("❌ 错误")
            with col3:
                if st.button("不适合", key=f"no_{i}"):
                    if answer == "❌ 不适合":
                        st.success("✅ 正确")
                    else:
                        st.error("❌ 错误")
    
    else:  # 进阶题
        st.info("💡 **这些场景需要你判断如何收束范围，才能用 AI-Coding**")
        
        gray_scenarios = [
            {
                "question": "产品/业务方一句话说：我们也要做一个\"AI 智能体平台\"",
                "answer": "❌ 暂不适合",
                "explanation": "**目标过大过虚，暂不适合：**\n- ❌ \"平台 / 智能体\"本身不是可验证目标\n- ✅ 必须先拆成具体动作：比如\"帮课程运营自动生成跟练任务\"\n- ✅ 每次只选一个高频、低风险、可 1–2 天验证的场景\n- ✅ 用 AI-Coding 验证\"是否真有用\"，而不是\"看起来很先进\""
            },
            {
                "question": "基于公司真实业务数据做内部 AI 分析 / 决策 / 助手工具",
                "answer": "⚠️ 视情况而定",
                "explanation": "**关键看数据和影响范围：**\n- ✅ 如果是脱敏数据、汇总数据、样本数据：可以先做验证\n- ❌ 如果涉及客户隐私、收入、合同、关键决策链路：不适合直接用\n- ⚠️ 一旦进入真实业务决策，必须引入工程与安全评估"
            },
            {
                "question": "做一个团队内部用的文档整理工具",
                "answer": "✅ 适合",
                "explanation": "**适合，但要明确使用周期：**\n- ✅ 验证阶段：快速做一个，看团队是否真的会用\n- ✅ 如果只用 1-2 个月：AI-Coding 可以撑住\n- ⚠️ 如果要长期使用（1年+）：验证后交给研发重构\n- ✅ 关键是：先验证价值，再决定投入"
            }
        ]
        
        for i, scenario in enumerate(gray_scenarios):
            st.markdown(f"#### 场景 {i+1}：{scenario['question']}")
            
            if st.button("查看答案", key=f"gray_{i}"):
                if scenario['answer'].startswith("✅"):
                    st.success(f"**{scenario['answer']}**")
                elif scenario['answer'].startswith("❌"):
                    st.error(f"**{scenario['answer']}**")
                else:
                    st.warning(f"**{scenario['answer']}**")
                st.markdown(scenario['explanation'])

# ============================================
# 页面 2: AI-Coding 的方式
# ============================================
elif page == "📊 AI-Coding 方式":
    st.title("AI-Coding 的方式：到底选哪种？")
    
    st.markdown("""
    <div class="highlight-box">
    <h4>🔑 一刀切的判断问题：</h4>
    <p style="font-size: 30px; text-align: center; font-weight: bold; color: #1f77b4;">
    需不需要把「规则写出来」
    </p>
    </div>
    """, unsafe_allow_html=True)
        
    st.markdown("#### 📊 从这一刀下去，三种方式自然分开")
    
    # 三列对比
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
        <h4 style="text-align: center;">💬 Prompt-Coding</h4>
        <p style="text-align: center; font-size: 20px;">
        <b>只关注结果像不像</b><br><br>
        我说清楚要什么<br>
        AI 直接给结果<br><br>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
        <h4 style="text-align: center;">🔧 Vibe-Coding 1.0</h4>
        <p style="text-align: center; font-size: 20px;">
        <b>我要 AI 严格按规则跑</b><br><br>
        我把规则说清楚<br>
        AI 按规则执行<br><br>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="highlight-box">
        <h4 style="text-align: center;">🚀 Vibe-Coding 2.0</h4>
        <p style="text-align: center; font-size: 20px;">
        <b>规则单独存放、反复使用</b><br><br>
        规则从 prompt 中拆出<br>
        可追踪、可迭代<br><br>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.info("""
    ### 💡 如何判断该用哪种？
    
    问自己一个问题：
    > **我能不能凭直觉判断这个结果好不好？**
    
    - ✅ **能** → 用 Prompt-Coding（文案、页面、展示类）
    - ❌ **不能** → 需要写规则
        - 如果规则简单、一次性验证 → Vibe-Coding 1.0
        - 如果规则复杂、需要反复使用 → Vibe-Coding 2.0
    """)

# ============================================
# 页面 3: Prompt-Coding
# ============================================
elif page == "💬 Prompt-Coding":
    st.title("Prompt-Coding：一句话 AI 自己跑")
    
    st.markdown("### 🎯 1. 什么是 Prompt-Coding？")
    
    st.markdown("""
    <div class="quote-box">
    <p style="font-size: 20px;">
    <b>我把需求说清楚，AI 直接给我一个「看起来能用」的结果。</b>
    </p>
    <b>✅ 不写代码，不管怎么算</b>
    </p>
    <b>💡 当成一个：反应极快、不会嫌你烦的展示助手</b>
    </div>
    """, unsafe_allow_html=True)


    st.markdown("---")
    
    st.markdown("### 🎯 2. 什么场景适合 Prompt-Coding？")
    
    st.markdown("""
    <div class="highlight-box">
    <h5>💡 判断标准非常简单</h5>
    <p style="font-size: 20px; text-align: center;">
    <b>我能不能凭直觉判断这个结果好不好？</b>
    </p>
    <p style="font-size: 16px; text-align: center; color: #666;">
    如果能，那就适合 Prompt-Coding
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.success("""
    #### ✅ 所以：
    
    ## 80% 的日常工作，其实用 Prompt-Coding 就够了
    
    比如：
    - 页面文案顺不顺
    - 流程说明清不清楚
    - Demo 页面好不好看
    """)
    
    st.markdown("---")
    
    # 案例示例
    st.markdown("### 📝 3. 示例：图书馆预约展示页面")
    
    st.markdown("""
    <div class="highlight-box">
    <p style="font-size: 18px;">
    我们来看一个非常典型的例子：<b>图书馆预约展示页面</b>
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    step = st.radio(
        "选择步骤查看详情：",
        ["第一步：编写内容文案", "第二步：生成 Coding 指令", "第三步：用工具把页面跑出来", "第四步：Prompt-Coding 的止损线"]
    )
    
    if step == "第一步：编写内容文案":
        st.markdown("#### 📝 第一步：编写内容文案")
        
        st.info("💡 不是让 AI「自己想」，而是提供**清楚的业务事实**。")
        
        st.code("""图书馆预约说明文案：
- 开放对象：在校学员
- 可预约时间：每天 9:00-17:00，每小时一个时段
- 预约规则：
  1. 每人每天最多预约1个时段
  2. 提前1天开放预约
  3. 预约成功后不可取消
  
要求：
- 每条规则一句话说清楚
- 不要加"智能推荐"或"温馨提示"
- 语言简洁、直白""", language=None)
        
        st.success("👉 这一步，**你是「业务专家」，不要让 AI 自由发挥情绪，要约束结构。**")
    
    elif step == "第二步：生成 Coding 指令":
        st.markdown("#### 🎨 第二步：生成指令（Prompt 套 Prompt）")
        
        st.markdown("""
        <h4 style="color: #0c5460; margin-bottom: 15px;">💡 最简提示词：</h4>
        <div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; font-family: monospace; margin-bottom: 20px; white-space: pre-wrap; line-height: 1.6;">根据下方提示词，
+
生成互动式的 html 网页的 vibe-coding 提示词（简要描述应用形式和布局）
+
强化"涟漪"视觉导向（描述视觉风格偏好或其他偏好，非必需）
+
（粘贴根据内容文案生成的提示词）</div>
        """, unsafe_allow_html=True)

        with st.expander("📐 应用布局举例"):
            st.markdown("""
            **Bento 网格布局：** 所有内容都组织在不同的方框或单元格中。这种布局最适合功能丰富的网站。
            
            **滚动叙事：** 网站就像一块巨大的画布。随着滚动，元素会逐渐出现或淡入淡出。这种形式最适合故事性较强的网站。
            
            **分屏显示：** 屏幕被一分为二。一侧固定显示文字，另一侧可移动显示图片。这种显示方式最适合以产品为主的网站。
            """)
        
        with st.expander("🎨 视觉风格举例"):
            st.markdown("""
            **科技与信任：** 玻璃变形（磨砂玻璃）或极光渐变（柔和的光线）。
            
            **奢华与故事性：** 暗黑学院风（忧郁的衬线字体）、生态极简主义（大地色调）或单色（黑白）。
            
            **创意十足且大胆：** 新粗野主义（粗犷的轮廓、冲突的色彩）、Y2K 或蒸汽波（复古美学）。
            """)

        
        st.markdown("""
        <div style="border-left: 8px solid #28a745; background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%); padding: 25px 30px; border-radius: 10px; margin-top: 30px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <p style="font-size: 20px; color: #155724; margin-bottom: 10px;">
        这一步，本质是：
        </p>
        <p style="font-size: 26px; font-weight: bold; color: #155724; line-height: 1.5;">
        「用 AI，放大你已经做对的事情」
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    elif step == "第三步：用工具把页面跑出来":
        st.markdown("#### ✨ 第三步：用工具把页面跑出来")
                
        st.success("""
        ✅ **生成成功！**
        
        你得到了：
        - 完整的预约展示页面
        - 清晰的时间段列表
        - 简洁的规则说明
        """)
    
    else:  # 第四步：止损线
        st.markdown("#### 🛑 第四步：Prompt-Coding 的止损线")
        
        st.markdown("""
        <div class="success-box">
        <h4>我们做对了什么？</h4>
        <p style="font-size: 18px;">
        <b>把已知信息，表达到位。</b>
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("""
        <div class="warning-box">
        <h4>⚠️ 一旦你开始关心这些规则类问题：</h4>
        <ul style="font-size: 16px;">
            <li>「这个时间段会不会被重复预约？」</li>
            <li>「名额到底算不算占用？」</li>
        </ul>
        <p style="font-size: 18px; font-weight: bold; color: #d9534f;">
        立刻停。
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="quote-box">
        <p style="font-size: 18px;">
        这不是 Prompt-coding 能够实现的问题，<br>
        <b>是场景升级了。</b>
        </p>
        </div>
        """, unsafe_allow_html=True)

# ============================================
# 页面 4: Vibe-Coding 1.0 - 正确姿势
# ============================================
elif page == "🔧 Vibe-Coding 1.0":
    st.title("Vibe-Coding 1.0：按我定的规则跑")
    
    st.markdown("""
    <div class="highlight-box">
    <h4>💡 从这里开始，你第一次不再是：</h4>
    <p style="font-size: 20px; text-align: center;">
    「祈祷 AI 足够聪明」
    </p>
    <p style="font-size: 20px; text-align: center; font-weight: bold; color: #1f77b4;">
    而是变成：<b>规则制定者</b>
    </p>
    </div>
    """, unsafe_allow_html=True)
        
    # 核心原则
    st.markdown("### 🔑 核心原则")
    st.success("""
    ## 人负责想清楚，AI 负责执行
    
    ⚠️ AI 最大的问题不是笨，而是——**太爱替你做决定**
    """)
    
    st.markdown("---")
    
    # 两步法
    st.markdown("### 📋 两步法")
    
    step = st.selectbox(
        "选择步骤查看详情：",
        ["概览", "第一步：先锁目标（人做）", "第二步：拆小步（人做）"]
    )
    
    if step == "概览":
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="highlight-box">
            <h3 style="text-align: center;">1️⃣ 先锁目标</h3>
            <p style="text-align: center;">想清楚要什么<br>更重要的是<b>不要什么</b></p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="highlight-box">
            <h3 style="text-align: center;">2️⃣ 拆小步</h3>
            <p style="text-align: center;">分步骤<br>一次只让 AI做<b>一件小事</b></p>
            </div>
            """, unsafe_allow_html=True)
    
    elif step == "第一步：先锁目标（人做）":
        st.markdown("""
        <div class="highlight-box">
        <h3>🎯 第一步：先锁目标</h3>
        <p style="font-size: 18px;">回答三个问题：</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("❓ 1. 我要解决什么问题？"):
            st.write("**反面案例：**")
            st.error("「帮我做一个预约管理系统」（太模糊）")
            st.write("**正面案例：**")
            st.success("「我需要一个工具，让读者能快速看到今天还能预约的参观时间，并完成预约」")
        
        with st.expander("❓ 2. 什么是成功？什么算失败？"):
            # 创建子标签选择
            success_tab = st.radio(
                "选择题目类型：",
                ["示例", "提示词"],
                horizontal=True,
                key="success_failure_tab"
            )
            
            if success_tab == "示例":
                st.write("**反面案例：**")
                st.error("「功能完善就是成功」（不直观）")
                st.write("**正面案例：**")
                st.success("""
                **成功标准：**
                - 读者打开页面就能看到当天可预约的时间段
                - 可以轻松找到空闲时间，不需要猜测
                - 能一键完成预约，无需填写太多信息
                
                **失败标准：**
                - 打开页面后，不知道哪些时间还能预约
                - 点击预约后找不到确认信息
                - 读者必须多次点击或返回才完成预约

                **公式抽象：**
                - 成功 = 用户在【场景】下，能【无需思考地完成某动作】，并【立刻确认结果】
                - 失败 = 在关键路径上的任一节点，用户产生不确定感（状态/路径结果）
                """)
            
            else:  # 提示词
                st.markdown("""
                <div class="highlight-box">
                <p style="font-size: 16px;">
                以下是一组提示词，帮助你从用户视角定义「成功与失败」。<br>
                </p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("---")
                
                # Prompt 1
                st.markdown("##### 📌 Prompt 1：禁止抽象成功（破坏性提问）")
                st.markdown('**使用场景：** 当你开始定义成功标准时，先用这个 prompt 破除"看起来很专业但无法感知"的假标准。')
                st.code("""你先不要给解决方案。

针对这个产品 / 功能：
【一句话描述功能】

请先列出 3–5 种「看起来很专业，但对用户不可感知」的成功定义，
并解释为什么它们是无效的成功标准。""", language=None)
                
                st.markdown("---")
                
                # Prompt 2
                st.markdown('##### 📌 Prompt 2：生成"可感知成功标准"')
                st.markdown("**使用场景：** 在破除抽象定义后，用这个 prompt 从用户视角生成可直接感知的成功标准。")
                st.code("""现在请只从「用户视角」思考。

用户是谁：【用户画像】
使用场景是：【具体场景】

请用「用户能直接描述的句子」
写出 3–5 条成功标准，要求：
- 不出现"系统 / 功能 / 模块"等词
- 每条都能被用户说成："我一打开就……"
""", language=None)
                
                st.markdown("---")
                
                # Prompt 3
                st.markdown("##### 📌 Prompt 3：失败不是 Bug，是不确定感")
                st.markdown("**使用场景：** 基于成功标准，推导用户在哪些时刻会产生「不确定感」，即使功能本身可用。")
                st.code("""基于上面的成功标准，
请推导用户在哪些时刻会产生「不确定感」。

请用以下句式输出：
- 用户打开页面后，可能会……
- 用户点击操作后，可能会……
- 用户完成操作后，可能会……

这些都算失败,即使功能本身是可用的。""", language=None)
                
                st.markdown("---")
                
                
        
        with st.expander("❓ 3. 明确说：哪些不做"):
            success_tab = st.radio(
                "选择题目类型：",
                ["示例", "提示词"],
                horizontal=True,
                key="scope_not_doing_tab"
            )
            
            if success_tab == "示例":
                st.write("**为什么这个最重要？**")
                st.warning("👉 如果不写清楚，AI 会自己加功能或流程，反而复杂")
                st.write("**正面案例：**")
                st.success("""
                **这个版本不做：**
                - ❌ 不做读者注册/登录
                - ❌ 不做图书馆管理员管理功能
                - ❌ 不做统计或报表
                - ❌ 只做查看可预约时间和提交预约，其他都不做
                """)
            
            else:  # 提示词
                st.markdown("""
                <div class="highlight-box">
                <p style="font-size: 16px;">
                以下是一组提示词，帮助你思考「哪些不做」。<br>
                </p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("---")
                
                # Prompt 4
                st.markdown("##### 📌 Prompt 4：用成功/失败反推最小实现")
                st.markdown("**使用场景：** 最后一步：反推最小实现。明确哪些元素必须有，哪些可以晚点做，哪些反而会增加不确定感。")
                st.code("""现在请你反过来思考：

如果我只允许保留：
- 让成功标准"成立"的最少元素
- 避免失败标准出现的必要提示

页面/流程中：
1. 哪些元素是必须的？
2. 哪些元素可以晚点再做？
3. 哪些元素反而会增加不确定感？""", language=None)
    
     
    
    else:  # 第二步：拆小步
        st.markdown("""
        <div class="highlight-box">
        <h3>🔨 第二步：拆小步</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.warning("### ❌ 不要说：")
        st.code('"帮我做一个图书馆预约管理系统"', language=None)
        
        st.success("### ✅ 而是：")
        
        # 互动式拆解示例
        tasks = [
            "第 1 步：先有一个页面，显示「图书馆预约系统」标题",
            "第 2 步：很好，现在在下面加 3 个可预约时间段，先用静态展示",
            "第 3 步：每个时间段加一个「预约」按钮，先不处理逻辑",
            "第 4 步：点击按钮弹出预约确认信息",
            "第 5 步：预约后显示预约成功提示"
        ]
        
        completed = []
        for i, task in enumerate(tasks):
            if st.checkbox(task, key=f"task_{i}"):
                completed.append(i)
        
        if completed:
            progress = len(completed) / len(tasks)
            st.progress(progress)
            st.write(f"已完成：{len(completed)}/{len(tasks)} 步")
        
        st.markdown("---")
        st.info("""
        ### 💡 核心原则：
        # 一次只允许 AI 做一件小事
        
        为什么？
        - 每一步都能验证
        - 出错了容易定位
        - 可以随时调整方向
        """)
        
        st.markdown("---")
        
        st.markdown("""
        <div class="quote-box">
        <h3 style="text-align: center; color: #1f77b4;">特别想强调一句话</h3>
        <p style="font-size: 26px; text-align: center; font-weight: bold;">
        拆得越细，AI 越像计算器，你越像决策者
        </p>
        <p style="font-size: 18px; text-align: center; color: #666;">
        这就是 Vibe-Coding 1.0 的精髓
        </p>
        </div>
        """, unsafe_allow_html=True)

# ============================================
# 页面 5: Vibe-Coding 1.0 - 分组研讨
# ============================================
elif page == "👥 思考题":
    st.title("思考题")
    
    st.markdown("""
    <div class="highlight-box">
    <h3>🎯 目标</h3>
    <p style="font-size: 18px;">
    练习"锁目标 + 拆小步"的逻辑，形成提示词
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 📋 规则")
    
    st.info("""
    **选择一个简单业务场景**
    
    **步骤：**
    1. 先明确**目标任务**（不能模糊）
    2. 明确**成功与失败**：列出 2-3 条"能直观判断成功/失败"的标准
    3. 明确**禁止事项**：列出至少 3 项不允许 AI 做的事情
    4. **拆小步**：把目标任务拆成 3-5 个最小执行步骤
    
    **输出：** 形成一个简单提示词
    """)
        
    st.markdown("### 💡 思考要点")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
        <h4 style="text-align: center;">目标是否清晰？</h4>
        <p style="text-align: center; font-size: 14px;">
        能不能一句话说明白要解决什么问题
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
        <h4 style="text-align: center;">标准是否直观？</h4>
        <p style="text-align: center; font-size: 14px;">
        成功/失败标准能否直观判断
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="highlight-box">
        <h4 style="text-align: center;">步骤是否可执行？</h4>
        <p style="text-align: center; font-size: 14px;">
        拆的小步 AI 是否能够独立执行
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 📝 参考模板")
    
    st.code("""## 【场景名称】

### 1️⃣ 目标任务
> 描述：______

### 2️⃣ 成功与失败标准

**成功标准：**
- [ ] 标准1：______
- [ ] 标准2：______
- [ ] 标准3：______

**失败标准：**
- [ ] 标准1：______
- [ ] 标准2：______

### 3️⃣ 禁止事项（至少3项）
- ❌ 不做：______
- ❌ 不做：______
- ❌ 不做：______

### 4️⃣ 拆小步（3-5步）
- Step 1：______
- Step 2：______
- Step 3：______
- Step 4：______
- Step 5：______

---

## 【最终提示词】

（根据以上内容整理成完整提示词）
""", language=None)

# ============================================
# 页面 6: Vibe-Coding 2.0
# ============================================
elif page == "🚀 Vibe-Coding 2.0":
    st.title("Vibe-Coding 2.0：规则从 prompt 中拆出，形成可复用判断")
    
    st.markdown("### 🤔 1. 为什么要 2.0？")
    
    st.markdown("""
    <div class="highlight-box">
    <p style="font-size: 18px;">
    在 1.0 阶段，我们已经做对了两件事：
    </p>
    <ol style="font-size: 16px;">
        <li>人先想清楚目标、成功/失败、禁止行为</li>
        <li>AI 严格按规则执行，不替人做决定</li>
    </ol>
    <p style="font-size: 18px;">
    只要你能够想清楚这些，其实你已经站在 1.0 的<b>「天花板」</b>上了。
    </p>
    </div>
    """, unsafe_allow_html=True)
        
    st.markdown("**在 1.0 阶段，我们通常是这样做的：**")
    st.markdown("""
    - 把页面怎么展示写在 prompt 里
    - 把流程写在 prompt 里
    - 顺便把特殊规则也写在 prompt 里
    """)
    
    st.info("一开始完全没问题，甚至非常高效。")
        
    st.markdown("**但慢慢你会发现三件事：**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="warning-box">
        <h4 style="text-align: center;">1️⃣ 判断变多了</h4>
        <p style="text-align: center; font-size: 14px;">
        原来只判断"预约满不满"<br>
        后来又多了"预约是否超时/是否重复"
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="warning-box">
        <h4 style="text-align: center;">2️⃣ 判断开始复用</h4>
        <p style="text-align: center; font-size: 14px;">
        不只是“提交”按钮在用<br>
        子页面或流程都会用到同一套判断
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="warning-box">
        <h4 style="text-align: center;">3️⃣ 判断开始互相影响</h4>
        <p style="text-align: center; font-size: 14px;">
        改一个规则<br>
        别的地方的结果也会变
        </p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("""
    <div class="quote-box">
    <p style="font-size: 20px;">
    这时候你会有一个非常真实的感受：
    </p>
    <p style="font-size: 18px; text-align: center;">
    我不会写 prompt 了么？
    </p>
    <p style="font-size: 20px; font-weight: bold; color: #1f77b4;">
    其实是 prompt 开始装不下这些判断了
    </p>
    <p style="font-size: 18px;">
    <b>2.0 不是让你写更复杂的东西，而是承认：有些判断，不适合继续放在 prompt 里了。</b>
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 📋 2. 2.0 做的三件事")
    
    # 创建交互式选择
    action = st.selectbox(
        "选择查看详情：",
        ["概览", "第一件事：把「影响对错的句子」拆出来", "第二件事：把判断写成 Spec", "第三件事：把 Spec 放进 IDE"]
    )
    
    if action == "概览":
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="highlight-box">
            <h4 style="text-align: center;">1️⃣ 拆出判断</h4>
            <p style="text-align: center; font-size: 14px;">
            把「影响对错的句子」<br>
            从 prompt 中拆出来
            </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="highlight-box">
            <h4 style="text-align: center;">2️⃣ 写成 Spec</h4>
            <p style="text-align: center; font-size: 14px;">
            把判断固定成<br>
            「防止被改写的说明书」
            </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="highlight-box">
            <h4 style="text-align: center;">3️⃣ 放进 IDE</h4>
            <p style="text-align: center; font-size: 14px;">
            让规则有自己的「房间」<br>
            页面只能用，不能改
            </p>
            </div>
            """, unsafe_allow_html=True)
    
    elif action == "第一件事：把「影响对错的句子」拆出来":
        st.markdown("#### 📝 第一件事：把「影响对错的句子」拆出来")
        
        st.markdown("""
        在图书馆预约这个例子中，有一类句子很特殊：
        - 能不能预约？
        - 为什么不能预约？
        - 成功和失败是怎么判定的？
        """)
        
        st.markdown("""
        <div class="success-box">
        <p style="font-size: 18px;">
        这些句子有一个共同点：
        </p>
        <p style="font-size: 20px; font-weight: bold; text-align: center;">
        它们不决定页面长什么样，<br>
        只决定结果对不对
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("在 2.0 里，这类句子不再和页面描述混在一起，而是被**单独拎出来**。")
    
    elif action == "第二件事：把判断写成 Spec":
        st.markdown("#### 📋 第二件事：把判断写成 Spec")
        
        st.markdown("""
        <div class="quote-box">
        <p style="font-size: 20px; text-align: center;">
        <b>Spec 就是一份「防止判断被改写的说明书」</b>
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("在 2.0 里，我们不再用一句话说：")
        st.code("「判断这个时间段能不能预约」", language=None)
        
        st.markdown("而是把它固定成一个形态，比如：")
        
        st.markdown("""
        <div class="success-box">
        <ul style="font-size: 16px;">
            <li>输入是什么（时间段、当前时间、已有预约）</li>
            <li>输出是什么（成功 / 失败 + 原因）</li>
            <li>哪些情况一定失败</li>
            <li>明确说：不要推荐、不补规则、不加判断</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("""
        **一旦写成这种形态，判断就不再依赖 AI 的"理解能力"，而是有了边界。**
        """)
    
    elif action == "第三件事：把 Spec 放进 IDE":
        st.markdown("#### 🏠 第三件事：把 Spec 放进 IDE（让判断有「房间」）")
        
        st.markdown("""
        你可以把 IDE （集成开发环境）理解成让"规则有自己房间"的地方：
        """)
        
        st.markdown("**我们可以用图书馆预约的例子来解释：**")
        
        with st.expander("1️⃣ 页面在一个房间", expanded=True):
            st.markdown("""
            - 页面负责展示时间段、按钮、交互效果
            - 例如：用户看到 9:00–10:00 还能预约，并能点击"预约"按钮
            """)
        
        with st.expander("2️⃣ 判断规则在另一个房间", expanded=True):
            st.markdown("""
            - 判断规则负责回答"能不能预约"
            - 例如：9:00–10:00 已经被预约满了 → 失败
            - 这里的规则独立存放，不随页面改动而改
            """)
        
        with st.expander("3️⃣ 页面只能「用」规则，不能「改」规则", expanded=True):
            st.markdown("""
            - 页面调用规则来判断是否可预约
            - 页面不需要关心规则怎么写、规则里面有哪些判断
            - 避免因为页面改动导致规则逻辑被误改
            """)
    
    st.markdown("---")
    
    st.markdown("### 🎯 3. 什么时候你真的需要 2.0？")
    
    st.markdown("""
    <div class="highlight-box">
    <h4>💡 一个非常可操作的判断标准</h4>
    <p style="font-size: 18px;">
    只问自己一句话：
    </p>
    <p style="font-size: 22px; text-align: center; font-weight: bold; color: #1f77b4;">
    我是不是已经在 prompt 里，<br>
    反复强调同一批判断，<br>
    生怕 AI 哪次「理解错」？
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        ✅ **如果还没有**
        
        1.0 完全够用
        """)
    
    with col2:
        st.info("""
        ⚠️ **如果已经是了**
        
        你其实已经走到 2.0 门口了
        """)

# ============================================
# 页面 7: 分享总结 & 金句
# ============================================
elif page == "✅ 分享总结":
    st.title("分享总结")
    
    st.markdown("""
    <div class="highlight-box">
    <h2 style="text-align: center;">🎯 三种方法核心对比</h2>
    </div>
    """, unsafe_allow_html=True)
        
    # 对比表格
    comparison_data = {
        "方法": ["Prompt-Coding", "Vibe-Coding 1.0", "Vibe-Coding 2.0"],
        "核心特征": [
            "一句话 AI 自己跑",
            "按我定的规则跑",
            "规则单独存放、反复使用"
        ],
        "需要写规则": ["❌ 不需要", "✅ 需要", "✅ 需要 + Spec"],
        "适用场景": [
            "文案、页面、展示类",
            "一次性验证",
            "规则复杂、需反复使用"
        ],
        "判断标准": [
            "凭直觉能判断好坏",
            "需要明确规则",
            "在 prompt 里反复强调同一批判断"
        ],
        "典型案例": [
            "图书馆预约展示页面",
            "图书馆预约系统",
            "规则复杂的预约系统"
        ]
    }
    
    df = pd.DataFrame(comparison_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # 行动建议
    st.markdown("### 🚀 3 条行动建议")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="success-box">
        <h4>1️⃣ 从简单开始</h4>
        <p style="font-size: 16px;">
        先用 Prompt-Coding<br>
        处理 80% 的日常工作<br>
        <br>
        文案、页面、展示<br>
        都可以试试
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="success-box">
        <h4>2️⃣ 理解边界</h4>
        <p style="font-size: 16px;">
        记住三条警示线<br>
        知道什么不能做<br>
        <br>
        验证用 AI<br>
        生产找专业人士
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="success-box">
        <h4>3️⃣ 逐步进阶</h4>
        <p style="font-size: 16px;">
        熟练后尝试<br>
        Vibe-Coding 1.0<br>
        <br>
        规则复杂时<br>
        再升级到 2.0
        </p>
        </div>
        """, unsafe_allow_html=True)

# 页脚
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p>📧 这个 Demo 本身就是用 AI-Coding 方式制作的</p>
    <p>⏱️ 开发时间：约半天（包含完整的 7 个章节）</p>
    <p>💡 功能完整，够用但不完美 —— 正是 AI-Coding 的精髓！</p>
</div>
""", unsafe_allow_html=True)
