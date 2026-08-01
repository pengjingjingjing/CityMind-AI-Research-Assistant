# CityMind AI Research Assistant

**SEO/GEO Content Optimization Case + Live AI Research Tool**

CityMind is a lightweight AI research assistant for urban planning, city research and policy analysis. It turns an early-stage research question into a structured starting brief containing an executive summary, research framework, preliminary findings, data gaps, presentation outline and next-step tasks.

## Live links

- Product website: https://pengjingjingjing.github.io/CityMind-AI-Research-Assistant/
- Streamlit demo: https://citymind-ai-research-assistant-i2bqorzpfcccwe7gr3ra87.streamlit.app/
- Repository: https://github.com/pengjingjingjing/CityMind-AI-Research-Assistant

## Why this project matches an SEO/GEO content role

This repository combines two connected parts:

1. **A real, runnable product**
   - Streamlit interface
   - Demo mode
   - OpenAI-compatible API mode
   - Structured prompt
   - Markdown export
   - Accuracy and data-gap notices

2. **A publishable SEO/GEO content website**
   - Descriptive title, meta description and headings
   - Independent URLs for product, workflow, limitations and case study
   - Direct-answer modules for AI search
   - Internal links and content cluster
   - `robots.txt` and `sitemap.xml`
   - WebApplication and Article structured data
   - Clear author, update date and project limitations

## Important project boundary

The Streamlit tool is real and runnable. The keyword research and page-optimization work are an independently initiated SEO/GEO practice project. The repository does **not** claim real ranking, traffic or conversion growth before Search Console and GA4 data are collected.

The current application uses a **single-stage structured prompt**. A two-stage process — outline validation followed by section expansion — is listed as a future iteration, not an existing feature.

## Repository structure

```text
.
├── app.py                         # Streamlit application
├── requirements.txt
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml.example
├── docs/                          # GitHub Pages website
│   ├── index.html
│   ├── how-it-works.html
│   ├── accuracy-and-limitations.html
│   ├── seo-geo-case-study.html
│   ├── articles/
│   ├── assets/styles.css
│   ├── robots.txt
│   └── sitemap.xml
├── PRD_CityMind.md
├── Prompt_Design.md
├── SEO_GEO_Case_Study.md
├── UPLOAD_TO_GITHUB.md
└── SECURITY_NOTICE.md
```

## Run the Streamlit app locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Demo mode works without an API key.

For live API mode, copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and add your own key. Never commit `secrets.toml`.

## Deploy the Streamlit app

In Streamlit Community Cloud:

1. Select this GitHub repository.
2. Set the main file to `app.py`.
3. Open **App settings → Secrets**.
4. Add:

```toml
LLM_API_KEY = "your_new_key"
LLM_API_URL = "your_openai_compatible_chat_completions_url"
LLM_MODEL = "your_model_name"
```

5. Choose a descriptive custom subdomain when available.

## Publish the SEO/GEO website with GitHub Pages

Open the repository on GitHub:

1. Go to **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select the `main` branch.
4. Select the `/docs` folder.
5. Save.

The expected site address is:

```text
https://pengjingjingjing.github.io/CityMind-AI-Research-Assistant/
```

## After publishing

- Add the GitHub Pages site to Google Search Console.
- Submit `sitemap.xml`.
- Inspect and request indexing for the homepage.
- Add GA4 only after creating a real property.
- Record real impressions, clicks, queries and content changes.
- Do not add invented user counts, rankings, reviews or traffic results.

## Suggested interview reading order

1. Product website
2. SEO/GEO case-study page
3. Live Streamlit demo
4. GitHub source and prompt documentation

## Author

Peng Jing  
Content Operations · SEO/GEO · AI Content
