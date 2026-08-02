import os
from datetime import date
from typing import Any

import requests
import streamlit as st


SITE_URL = "https://pengjingjingjing.github.io/CityMind-AI-Research-Assistant/"
GITHUB_URL = "https://github.com/pengjingjingjing/CityMind-AI-Research-Assistant"

st.set_page_config(
    page_title="CityMind AI Research Assistant for Urban Planning",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .block-container {max-width: 1120px; padding-top: 2rem; padding-bottom: 4rem;}
    .hero {
        padding: 2.1rem 2.2rem;
        border-radius: 24px;
        background: linear-gradient(135deg, #112448 0%, #174d62 100%);
        color: white;
        margin-bottom: 1.5rem;
    }
    .hero h1 {font-size: 2.45rem; line-height: 1.15; margin: 0 0 .7rem 0;}
    .hero p {font-size: 1.05rem; line-height: 1.75; color: #d7edf2; margin: .4rem 0;}
    .eyebrow {font-size: .82rem; letter-spacing: .1em; font-weight: 700; color: #37d3cc;}
    .answer-card {
        padding: 1.15rem 1.3rem;
        border: 1px solid #d9e7ea;
        border-left: 5px solid #17aaa6;
        border-radius: 14px;
        background: #f7fbfc;
        margin: .8rem 0 1.3rem 0;
    }
    .small-note {font-size: .88rem; color: #667883;}
    .feature-card {
        border: 1px solid #e3eaee;
        border-radius: 16px;
        padding: 1rem 1.1rem;
        min-height: 138px;
        background: white;
    }
    .feature-card h4 {margin: 0 0 .45rem 0; color: #143b53;}
    .feature-card p {margin: 0; color: #536873; line-height: 1.55;}
    .trust-card {
        padding: 1rem 1.2rem;
        border-radius: 14px;
        background: #fff8f2;
        border: 1px solid #f1dfcf;
        color: #694d35;
    }
    .footer-card {
        margin-top: 2.5rem;
        padding: 1.1rem 1.3rem;
        border-radius: 14px;
        background: #10213f;
        color: #d9e7ef;
    }
    .footer-card a {color: #45d5ce; text-decoration: none; margin-right: 1rem;}
    div[data-testid="stMetric"] {
        border: 1px solid #e0e9ed;
        padding: .8rem;
        border-radius: 12px;
        background: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="hero">
      <div class="eyebrow">FREE AI RESEARCH TOOL · URBAN PLANNING · POLICY ANALYSIS</div>
      <h1>CityMind AI Research Assistant</h1>
      <p><strong>Turn urban planning and policy questions into structured research briefs.</strong></p>
      <p>Generate a research framework, key findings, data gaps, presentation outline and next-step research tasks from one focused question.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="answer-card">
      <strong>What is CityMind?</strong><br>
      CityMind is a lightweight AI research assistant for urban planning, city research and
      policy analysis. It turns an early-stage research question into a structured starting brief.
      The output is designed to support — not replace — original-source reading, professional
      judgment or formal research.
    </div>
    """,
    unsafe_allow_html=True,
)

top_left, top_mid, top_right = st.columns(3)
with top_left:
    st.markdown(
        '<div class="feature-card"><h4>Structured Output</h4><p>Fixed sections make results easier to review, compare and reuse in reports or presentations.</p></div>',
        unsafe_allow_html=True,
    )
with top_mid:
    st.markdown(
        '<div class="feature-card"><h4>Data-Gap Awareness</h4><p>The prompt asks the model to mark uncertain claims, missing evidence and items requiring verification.</p></div>',
        unsafe_allow_html=True,
    )
with top_right:
    st.markdown(
        '<div class="feature-card"><h4>Content Iteration</h4><p>Prompt versions, test cases and feedback can be recorded to improve clarity and usefulness.</p></div>',
        unsafe_allow_html=True,
    )

st.divider()
st.subheader("Create a structured research brief")

with st.form("research_form"):
    col1, col2 = st.columns(2)

    with col1:
        topic = st.text_input(
            "Research topic *",
            value="How can old urban communities improve public service accessibility?",
            help="Use one focused research question.",
        )
        region = st.text_input(
            "Region or target area",
            value="Guangzhou, China",
        )
        scenario = st.selectbox(
            "Use scenario",
            [
                "Planning consultancy — early research",
                "Policy analysis — briefing note",
                "Graduate research — topic exploration",
                "Urban renewal — project preparation",
                "Content creation — research outline",
            ],
        )

    with col2:
        audience = st.selectbox(
            "Target reader",
            [
                "Planning or policy professionals",
                "Project client / decision-maker",
                "Graduate students",
                "General readers",
            ],
        )
        output_language = st.selectbox(
            "Output language",
            ["English", "简体中文"],
        )
        materials = st.text_area(
            "Available materials or constraints",
            placeholder=(
                "Paste policy names, notes, statistics, source excerpts or known constraints. "
                "Do not include confidential information."
            ),
            height=124,
        )

    output_options = st.multiselect(
        "Requested output",
        [
            "Executive summary",
            "Research framework",
            "Key findings",
            "Policy / industry / spatial dimensions",
            "Presentation outline",
            "Data gaps and verification list",
            "Next-step research tasks",
        ],
        default=[
            "Executive summary",
            "Research framework",
            "Key findings",
            "Presentation outline",
            "Data gaps and verification list",
            "Next-step research tasks",
        ],
    )

    submitted = st.form_submit_button(
        "Generate research brief",
        type="primary",
        use_container_width=True,
    )


def read_config(name: str, default: str = "") -> str:
    """Read a value from Streamlit secrets first, then environment variables."""
    try:
        if name in st.secrets:
            return str(st.secrets[name])
    except Exception:
        pass
    return os.getenv(name, default)


def make_demo_output(
    research_topic: str,
    research_region: str,
    use_scenario: str,
    target_audience: str,
    language: str,
    source_materials: str,
) -> str:
    region_text = research_region.strip() or "the selected study area"
    evidence_note = (
        "The user supplied preliminary materials; each claim should still be checked against the original source."
        if source_materials.strip()
        else "No source materials were supplied. The following is a planning framework, not a factual conclusion."
    )

    if language == "简体中文":
        return f"""# CityMind 研究简报（演示模式）

> **演示说明：** 本结果由内置模板生成，用于展示内容结构，并非实时大模型研究结论。

## 1. 主题理解
本研究围绕“**{research_topic}**”展开，研究对象为 **{region_text}**。当前使用场景为“{use_scenario}”，主要读者为“{target_audience}”。

## 2. 执行摘要
建议先明确目标人群、服务类型、空间尺度和评价指标，再结合政策文本、设施分布、人口结构与实际使用反馈形成判断。现阶段应避免在缺少官方统计或一手调研的情况下给出精确结论。

## 3. 研究框架
1. **问题定义：** 明确研究边界、目标人群和核心矛盾。
2. **政策环境：** 核验国家、省、市及区级相关政策。
3. **现状分析：** 整理人口、设施、交通、土地使用和公共服务数据。
4. **用户需求：** 通过访谈、问卷或观察识别实际使用障碍。
5. **案例比较：** 选择条件相近的国内外案例进行机制比较。
6. **策略形成：** 按近期、长期和实施主体提出建议。
7. **评估指标：** 建立可达性、公平性、使用率、成本和满意度指标。

## 4. 初步判断
- 研究结论应区分“政策目标”“空间供给”和“真实使用体验”。
- 单纯增加设施数量不一定改善服务可达性，还需考虑步行网络、开放时间、费用和特殊人群需求。
- 策略应明确责任主体、实施顺序和数据更新机制。

## 5. 数据缺口与核验清单
- 最新人口与年龄结构数据；
- 设施位置、等级、服务范围和开放时间；
- 公共交通与步行网络数据；
- 目标用户的真实使用反馈；
- 相关政策的有效期与适用范围；
- 对比案例的实施条件与实际成效。

## 6. PPT 目录建议
1. 研究背景与问题定义
2. 目标人群与需求
3. 政策与规划要求
4. 现状设施及空间分布
5. 可达性与公平性分析
6. 关键问题与证据缺口
7. 优化策略与实施路径
8. 评估指标与下一步工作

## 7. 下一步任务
- 建立资料清单和来源台账；
- 下载并核验官方政策与统计资料；
- 绘制设施和人口空间分布图；
- 设计 3—5 个目标用户访谈问题；
- 形成“证据—判断—建议”对应表。

## 8. 准确性说明
{evidence_note}
"""
    return f"""# CityMind Research Brief — Demo Mode

> **Demo notice:** This result is generated from an internal template to demonstrate the content structure. It is not a live model-generated research conclusion.

## 1. Topic Interpretation
The study examines **{research_topic}** in **{region_text}**. The selected use scenario is “{use_scenario},” and the intended reader is “{target_audience}.”

## 2. Executive Summary
Start by defining the target population, service category, spatial scale and evaluation criteria. Evidence should then be assembled from policy documents, facility locations, demographic data and user feedback. Avoid precise conclusions until official data and primary sources have been checked.

## 3. Research Framework
1. **Problem definition:** Define the study boundary, target users and central research question.
2. **Policy environment:** Verify relevant national, provincial, municipal and district policies.
3. **Baseline conditions:** Review population, facilities, transport, land use and service data.
4. **User needs:** Identify real access barriers through interviews, surveys or observation.
5. **Comparable cases:** Select cases with similar institutional and spatial conditions.
6. **Strategy design:** Separate short-term actions, long-term actions and responsible actors.
7. **Evaluation:** Track accessibility, equity, use, cost and satisfaction.

## 4. Preliminary Findings
- Distinguish policy intent, spatial supply and actual user experience.
- Increasing facility counts alone may not improve access; opening hours, walking connections, cost and special-needs access also matter.
- Recommendations should specify ownership, sequence and data-update mechanisms.

## 5. Data Gaps and Verification List
- Current population and age structure;
- Facility location, level, service area and opening hours;
- Public transport and pedestrian-network data;
- Direct feedback from target users;
- Effective dates and scope of relevant policies;
- Implementation conditions and measured outcomes of comparison cases.

## 6. Presentation Outline
1. Background and problem definition
2. Target users and needs
3. Policy and planning requirements
4. Current facility and spatial pattern
5. Accessibility and equity analysis
6. Key problems and evidence gaps
7. Strategy and implementation pathway
8. Evaluation and next steps

## 7. Next Research Tasks
- Create a source and evidence register;
- Verify official policies and statistics;
- Map facilities and population distribution;
- Prepare 3–5 user interview questions;
- Build an evidence–finding–recommendation table.

## 8. Accuracy Notice
{evidence_note}
"""


def build_messages(
    research_topic: str,
    research_region: str,
    use_scenario: str,
    target_audience: str,
    language: str,
    source_materials: str,
    requested_outputs: list[str],
) -> list[dict[str, str]]:
    system_prompt = """
You are CityMind, an urban research and planning consultancy assistant.

Your purpose is to turn an early-stage research question into a structured starting brief.
You must not invent precise statistics, policy clauses, project names, citations or research findings.
When evidence is missing, explicitly label it as a data gap or item requiring verification.
Do not claim that a source has been checked unless the user supplied that source.
Separate evidence, preliminary judgment and recommendation.
Use clear headings, concise paragraphs and actionable bullet points.

This is the current single-stage structured-prompt version of CityMind.
The output is a research starting point, not a substitute for original-source reading,
professional judgment or formal research.
""".strip()

    requested = ", ".join(requested_outputs) if requested_outputs else "A concise structured brief"
    user_prompt = f"""
Research topic: {research_topic}
Region or target area: {research_region or "Not specified"}
Use scenario: {use_scenario}
Target reader: {target_audience}
Output language: {language}
Requested output: {requested}

User-provided materials:
{source_materials.strip() or "No materials supplied."}

Produce Markdown using the following order where relevant:
1. Topic Interpretation
2. Executive Summary
3. Research Framework
4. Key Findings or Preliminary Hypotheses
5. Policy / Industry / Spatial Dimensions
6. Presentation Outline
7. Data Gaps and Verification List
8. Next Research Tasks
9. Accuracy and Use Notice

Finish with a short reminder to verify policies, statistics, cases and citations against original sources.
""".strip()

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


def call_openai_compatible_api(
    api_url: str,
    api_key: str,
    model: str,
    messages: list[dict[str, str]],
) -> str:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload: dict[str, Any] = {
        "model": model,
        "messages": messages,
        "temperature": 0.25,
    }

    response = requests.post(
        api_url,
        headers=headers,
        json=payload,
        timeout=90,
    )
    response.raise_for_status()
    data = response.json()

    try:
        return str(data["choices"][0]["message"]["content"])
    except (KeyError, IndexError, TypeError) as exc:
        raise ValueError("The API response did not contain choices[0].message.content.") from exc


with st.sidebar:
    st.header("Generation settings")
    configured_key = read_config("LLM_API_KEY")
    configured_url = read_config(
        "LLM_API_URL",
        "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
    )
    configured_model = read_config("LLM_MODEL", "qwen-plus")

    default_mode = 1 if configured_key else 0
    mode = st.radio(
        "Mode",
        ["Demo mode", "Live API mode"],
        index=default_mode,
        help="Demo mode works without an API key. Live mode uses an OpenAI-compatible endpoint.",
    )

    with st.expander("Advanced API settings"):
        api_key = st.text_input(
            "API key",
            value=configured_key,
            type="password",
            help="Use Streamlit Secrets or enter a temporary key for this session.",
        )
        api_url = st.text_input("API URL", value=configured_url)
        model = st.text_input("Model", value=configured_model)

    st.markdown(f"[Product website]({SITE_URL})")
    st.markdown(f"[GitHub repository]({GITHUB_URL})")

if submitted:
    if not topic.strip():
        st.error("Please enter a research topic.")
    else:
        with st.spinner("Building the research brief..."):
            try:
                if mode == "Demo mode":
                    result = make_demo_output(
                        topic,
                        region,
                        scenario,
                        audience,
                        output_language,
                        materials,
                    )
                else:
                    if not api_key.strip():
                        raise ValueError(
                            "Live API mode requires an API key. Add it through Streamlit Secrets "
                            "or the advanced settings panel."
                        )
                    messages = build_messages(
                        topic,
                        region,
                        scenario,
                        audience,
                        output_language,
                        materials,
                        output_options,
                    )
                    result = call_openai_compatible_api(
                        api_url.strip(),
                        api_key.strip(),
                        model.strip(),
                        messages,
                    )

                st.session_state["citymind_result"] = result
            except requests.Timeout:
                st.error("The model request timed out. Please try again or use Demo mode.")
            except requests.RequestException as exc:
                st.error(f"The model request failed: {exc}")
            except (ValueError, TypeError) as exc:
                st.error(str(exc))
if not isinstance(result, str) or not result.strip():
    raise ValueError(
        "The generated research brief was empty. "
        "Please try again or check the selected generation mode."
    )

st.session_state["citymind_result"] = result


if isinstance(result, str) and result.strip():
    st.divider()

    st.success(
        f"Research brief generated successfully — "
        f"{len(result):,} characters. The full result is shown below."
    )

    with st.container(border=True):
        st.subheader("Generated research brief")
        st.markdown(result)

    st.download_button(
        "Download Markdown",
        data=result,
        file_name="citymind_research_brief.md",
        mime="text/markdown",
        use_container_width=True,
    )

elif "citymind_result" in st.session_state:
    st.error(
        "The research brief was created, but the returned content was empty. "
        "Please refresh the page and try again."
    )

st.divider()
st.subheader("How CityMind works")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Input", "Focused question")
m2.metric("Process", "Structured prompt")
m3.metric("Output", "Research brief")
m4.metric("Quality control", "Data-gap warnings")

st.markdown(
    """
    1. The user defines a focused topic, study area, use scenario and target reader.
    2. A structured single-stage prompt sets the role, output format and evidence boundaries.
    3. The model or demo template produces a fixed research-brief structure.
    4. The user verifies policies, statistics, cases and citations against original sources.
    """
)

st.markdown(
    """
    <div class="trust-card">
      <strong>Accuracy and limitations</strong><br>
      CityMind may produce incomplete, generic or inaccurate content. It currently does not use
      a local knowledge base or retrieval-augmented generation. Never treat generated text as
      verified policy, statistical or professional advice.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="footer-card">
      <strong>Project links</strong><br><br>
      <a href="{SITE_URL}" target="_blank">SEO/GEO Product Website</a>
      <a href="{GITHUB_URL}" target="_blank">GitHub Source</a>
      <br><br>
      Built by Peng Jing · Last updated {date.today().strftime("%B %Y")}
    </div>
    """,
    unsafe_allow_html=True,
)
