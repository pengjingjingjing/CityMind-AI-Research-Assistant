# CityMind SEO/GEO 内容优化案例

## 项目背景

CityMind 最初是一个偏 AI 产品原型展示的 Streamlit Demo。为匹配 SEO/GEO 内容运营岗位，本次改造没有更换主题，而是围绕已有真实产品建立完整内容承载体系。

## 改造目标

- 让面试官首先看到内容运营能力，而不是只看到技术 Demo；
- 建立可抓取、可内链、可监测的静态内容网站；
- 将关键词和搜索意图映射到具体页面；
- 增加适合搜索引擎和生成式搜索理解的直接回答模块；
- 明确模拟项目、真实功能和未来计划的边界。

## 修改前后

| 修改前 | 修改后 |
|---|---|
| AI 产品经理作品集定位 | SEO/GEO 内容增长实验 |
| 只有文档，没有完整 `app.py` | 补齐可运行 Streamlit 应用 |
| 首页突出产品经理视角 | 首页突出用户问题、内容结构和质量控制 |
| API 信息单独保存在文本文件 | 删除密钥文件，改用 Secrets |
| 单一 Streamlit 页面 | GitHub Pages 内容官网 + Streamlit Demo |
| 页面方案主要停留在作品集 | 部署 Title、Meta、H1-H3、内链、直接回答和结构化数据 |
| 两阶段流程表述不够准确 | 明确当前为单阶段，两阶段为计划 |
| 无技术 SEO 文件 | 增加 robots.txt 和 sitemap.xml |

## 目标关键词与页面

| 关键词 | 搜索意图 | 目标页面 |
|---|---|---|
| AI research assistant | 信息型 / 商业调查型 | 产品首页 |
| urban planning AI tool | 信息型 / 商业调查型 | 产品首页 |
| free AI research assistant online | 交易型 / 商业调查型 | 产品首页 + Demo |
| open source AI research assistant GitHub | 导航型 / 信息型 | GitHub + 产品首页 |
| Can AI help with urban planning research? | 信息型 | 专题文章 + FAQ |
| How accurate are AI research assistants? | 信息型 / 信任建设 | 准确性页面 |

## 页面集群

- `/`：产品首页；
- `/how-it-works.html`：工作流程与 Prompt 设计；
- `/accuracy-and-limitations.html`：准确性、来源与局限；
- `/seo-geo-case-study.html`：中文项目复盘；
- `/articles/what-is-an-ai-research-assistant.html`；
- `/articles/ai-for-urban-planning-research.html`；
- `/articles/citymind-prompt-design.html`。

## GEO 内容原则

- 页面开头提供明确直接答案；
- 每个问题先直接回答，再解释边界；
- 标注作者与更新时间；
- 明确产品是否使用 RAG、是否可引用来源；
- 不使用虚假用户量、排名、评价或增长数字；
- 把重要信息保留在可抓取文本中，而不是只放在图片里。

## 数据监测计划

上线后建立真实台账：

| 日期 | 页面 | 查询词/来源 | 展示 | 点击 | 发现问题 | 修改动作 |
|---|---|---|---:|---:|---|---|
| 待填写 | 首页 | 待收集 | 0 | 0 | 尚无真实数据 | 提交 Sitemap、请求收录 |

任何简历或作品集中的效果数字都必须来自真实后台截图和导出数据。
