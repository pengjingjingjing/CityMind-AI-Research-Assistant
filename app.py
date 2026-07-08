import os, json, requests, streamlit as st
from datetime import datetime

st.set_page_config(page_title="CityMind 城市研究助手", page_icon="🏙️", layout="wide")

SYSTEM_PROMPT = """你是 CityMind 城市研究助手，面向城市规划、产业研究、规划咨询和公共政策研究场景。
请把用户输入的政策资料、行业资料、片区信息和研究主题，转化为可用于研究报告、汇报 PPT 和项目方案讨论的结构化内容。
原则：1. 先识别研究主题、场景、目标用户和核心问题；2. 输出必须结构化，适合复制进 Word/PPT；
3. 给出判断依据、分析逻辑和下一步资料清单；4. 信息不足时明确指出缺口；5. 不编造精确数据；6. 语言专业、清晰、咨询化。"""

def build_prompt(topic, region, scenario, audience, material, output_type):
    return f"""【研究主题】{topic}
【研究区域/对象】{region}
【使用场景】{scenario}
【目标读者】{audience}
【用户提供资料】{material}
【希望输出类型】{output_type}

请输出：
1. 主题理解：3-5句话概括核心矛盾和切入点。
2. 研究框架：可用于报告或PPT的一级/二级目录。
3. 核心判断：4-6条可汇报观点，每条包含简短依据。
4. 分析维度：政策环境、产业链、空间载体、公共服务、实施路径。
5. PPT页标题建议：8-10页。
6. 下一步资料清单：需要补充的数据、案例、访谈或政策资料。
7. 风险与注意事项：需要核验或避免过度判断的地方。"""

def call_llm(api_key, api_url, model, prompt, temperature):
    headers = {"Content-Type":"application/json", "Authorization":f"Bearer {api_key}"}
    payload = {
        "model": model,
        "messages": [{"role":"system","content":SYSTEM_PROMPT}, {"role":"user","content":prompt}],
        "temperature": temperature
    }
    r = requests.post(api_url, headers=headers, data=json.dumps(payload), timeout=90)
    r.raise_for_status()
    data = r.json()
    return data["choices"][0]["message"]["content"]

def demo_output(topic):
    return f"""## 1. 主题理解

“{topic}”的核心不是简单判断某个产业是否适合进入片区，而是评估该产业与城市空间、政策导向、人才供给、企业生态和公共服务之间的匹配关系。对于城市更新片区而言，智能机器人等科技产业通常更适合以研发设计、展示体验、测试验证、场景应用等轻资产环节切入。

## 2. 研究框架

### 一、政策背景与发展趋势
- 国家及地方对人工智能、机器人、高端装备制造的支持方向
- 大湾区科技创新、智能制造和产业升级相关政策导向

### 二、产业链与技术路线拆解
- 核心零部件：减速器、传感器、控制器
- 本体制造：工业机器人、服务机器人、特种机器人
- 系统集成：场景解决方案、行业应用开发
- 应用场景：制造、医疗、养老、物流、城市治理

### 三、片区适配性分析
- 空间载体：旧厂房、研发办公、测试空间
- 交通条件：轨道站点、城市主干路、物流通达性
- 人才资源：高校、科研机构、工程技术人才
- 配套服务：商务、居住、展示、公共服务

## 3. 核心判断

1. 城市更新片区适合优先导入机器人产业的轻资产环节，例如研发、展示、测试和应用服务。
2. 产业导入应从真实应用场景切入，而不是只做概念招商。
3. 高校和科研资源是判断片区能否承接科技产业的重要条件。
4. 公共服务和生活配套会影响科技人才留存。
5. 短期应先形成示范应用，中长期再推动企业集聚。

## 4. PPT 页标题建议

1. 研究背景：智能机器人产业成为城市科技更新的重要抓手
2. 政策趋势：国家与湾区政策持续支持智能装备和人工智能发展
3. 产业链拆解：从核心零部件到场景应用的价值环节
4. 片区基础：空间、交通、人才和配套条件初步研判
5. 适配判断：片区更适合承接研发、展示、测试和应用服务
6. 导入路径：场景试点—平台建设—企业集聚—生态运营
7. 重点场景：养老、物流、园区治理和智能制造示范
8. 风险识别：产业定位空泛、企业资源不足和配套短板
9. 行动建议：建立场景清单、企业库和政策工具包
10. 下一步工作：补充数据、访谈企业、筛选标杆案例

## 5. 下一步资料清单

- 机器人、人工智能、智能制造政策文件
- 重点企业名录、融资事件和产业园区案例
- 片区土地、交通、人口、租金、产业载体和公共服务数据
- 周边高校、科研平台、孵化器和创新团队信息
- 企业访谈、政府部门访谈和运营主体访谈材料

## 6. 风险与注意事项

- 当前信息不足以判断具体招商成效，需要进一步核验企业资源和政策支持力度。
- 不建议直接使用“打造机器人产业高地”等过强表述，应先基于片区条件确定可落地环节。
- 需要区分“产业概念可行”和“项目运营可行”，避免停留在宏观叙事。"""

st.title("🏙️ CityMind 城市研究助手")
st.caption("面向规划咨询、产业研究与城市更新场景的 AI 研究报告生成助手")

with st.sidebar:
    st.header("API 设置")
    st.info("填写 API Key 后可真实调用大模型；未填写可使用 Demo 模式。")
    api_key = st.text_input("API Key", value=os.getenv("LLM_API_KEY",""), type="password")
    api_url = st.text_input("API URL", value=os.getenv("LLM_API_URL","https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"))
    model = st.text_input("Model", value=os.getenv("LLM_MODEL","qwen-plus"))
    temperature = st.slider("Temperature", 0.0, 1.0, 0.35, 0.05)
    use_demo = st.toggle("Demo 模式：不调用 API", value=not bool(api_key))
    st.divider()
    st.markdown("**产品定位**：把零散资料转化为研究框架、汇报观点和 PPT 目录。")

left, right = st.columns([0.92, 1.08], gap="large")
with left:
    st.subheader("输入信息")
    topic = st.text_input("研究主题", "智能机器人产业在城市更新片区中的导入路径")
    region = st.text_input("研究区域/对象", "大湾区某城市更新片区")
    scenario = st.selectbox("使用场景", ["规划咨询项目前期研究","产业研究报告","城市更新项目汇报","园区策划方案","政策研究辅助"])
    audience = st.selectbox("目标读者", ["项目经理/咨询顾问","政府部门","产业园区运营方","企业客户","作品集评审"])
    output_type = st.multiselect("希望输出内容", ["研究框架","核心判断","PPT 目录","资料清单","风险提示","政策/产业/空间分析"], default=["研究框架","核心判断","PPT 目录","资料清单","风险提示"])
    material = st.text_area("资料摘要 / 政策材料 / 片区信息", "国家与地方政策持续支持智能制造、机器人、人工智能与高端装备产业发展。部分城市更新片区希望通过产业导入提升空间价值，但存在产业定位不清、上下游企业不足、公共服务配套不完善、招商路径不明确等问题。片区周边有高校和旧工业厂房，租金较低，政府正在推动科技产业导入。", height=220)
    generate = st.button("生成 AI 研究结果", type="primary", use_container_width=True)

with right:
    st.subheader("AI 输出结果")
    if generate:
        if use_demo:
            result = demo_output(topic)
        else:
            if not api_key:
                st.error("请先填写 API Key，或打开 Demo 模式。")
                st.stop()
            prompt = build_prompt(topic, region, scenario, audience, material, "、".join(output_type))
            try:
                with st.spinner("正在调用大模型生成结构化研究结果..."):
                    result = call_llm(api_key, api_url, model, prompt, temperature)
            except Exception as e:
                st.error(f"API 调用失败：{e}")
                st.stop()
        st.markdown(result)
        st.download_button("下载 Markdown 结果", result, f"CityMind_研究结果_{datetime.now().strftime('%Y%m%d_%H%M')}.md", "text/markdown", use_container_width=True)
    else:
        st.markdown("点击左侧按钮后，这里会生成研究框架、核心判断、PPT 目录、资料清单和风险提示。")

st.divider()
st.subheader("产品经理视角")
c1,c2,c3,c4 = st.columns(4)
c1.metric("目标用户", "规划/产业研究")
c2.metric("核心场景", "资料→报告")
c3.metric("AI 能力", "结构化生成")
c4.metric("验证方式", "真实 API Demo")
st.markdown("""
### 指标设计
| 指标 | 含义 |
|---|---|
| 报告初稿生成时长 | 从输入资料到生成框架的时间 |
| 输出可用率 | 生成结果中可直接进入报告/PPT 的比例 |
| 二次编辑率 | 用户需要大幅修改的程度 |
| 资料缺口识别率 | 是否能提出有效补充资料清单 |
| 功能复用率 | 用户是否在多个议题中重复使用 |

### 后续迭代
1. 支持上传 PDF、Word、Excel 并自动解析；
2. 接入政策库、产业报告库和企业数据库；
3. 增加引用溯源，降低模型幻觉风险；
4. 加入用户反馈按钮，用真实反馈优化 Prompt；
5. 支持一键生成 PPT 初稿。
""")
