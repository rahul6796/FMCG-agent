# FMCG M&A Intelligence Newsletter Agent

## Overview

This project generates FMCG (Fast Moving Consumer Goods) industry intelligence newsletters focused on:

* Mergers & Acquisitions (M&A)
* Investments
* Funding Activities
* Strategic Expansions

The system automatically:

1. Collects FMCG-related news from public sources
2. Cleans and normalizes data
3. Removes duplicate and near-duplicate articles
4. Performs relevance filtering
5. Scores source credibility
6. Generates a concise executive newsletter
7. Supports question answering on processed articles

Built using:

* LangGraph
* LangChain
* OpenAI GPT-4o
* Streamlit
* Sentence Transformers

---

# Architecture

```text
News Sources
     |
     v
Fetch Agent
     |
     v
Clean Agent
     |
     v
Deduplication Agent
     |
     v
Relevance Agent
     |
     v
Credibility Agent
     |
     v
Newsletter Agent
     |
     v
Generated Newsletter
     |
     v
Streamlit UI
```

---

# Project Structure

```text
fmcg-newsletter-agent/
│
├── agents/
│   ├── fetch_agent.py
│   ├── clean_agent.py
│   ├── dedup_agent.py
│   ├── relevance_agent.py
│   ├── credibility_agent.py
│   └── newsletter_agent.py
│
├── graph/
│   ├── state.py
│   └── workflow.py
│
├── utils/
│   ├── logger.py
│   ├── exception.py
│   └── config.py
│
├── data/
│   ├── raw_news.csv
│   ├── processed_news.csv
│   └── newsletter.json
│
├── logs/
│   └── app.log
│
├── app.py
├── requirements.txt
├── .env.example
└── README.md
```

---

# Features

## Real-Time News Collection

Collects FMCG-related articles from publicly available RSS feeds.

## Data Cleaning

* Removes missing values
* Removes exact duplicates
* Standardizes article content

## Near-Duplicate Detection

Uses Sentence Transformers embeddings and cosine similarity.

Threshold:

```text
Cosine Similarity > 0.90
```

Articles above the threshold are treated as duplicates.

## Relevance Filtering

GPT-4o classifies articles as:

```text
YES
NO
```

Relevant categories include:

* Acquisition
* Merger
* Investment
* Funding
* Stake Purchase
* FMCG Expansion

## Credibility Scoring

Trusted sources receive higher scores.

Example:

```text
Reuters
Bloomberg
Food Business News
Just Food
```

## Newsletter Generation

Generates:

* Executive Summary
* Major Deals
* Investments
* Industry Insights
* Market Outlook

## Question Answering

Users can ask questions about:

* Acquisitions
* Investments
* Companies
* Regions
* Trends

---

# Installation

## Clone Repository

```bash
git clone <your-github-repository-url>

cd fmcg-newsletter-agent
```

---

## Create Conda Environment

```bash
conda create -n fmcg-agent python=3.11 -y

conda activate fmcg-agent
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

Example:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

# Running the Application

```bash
streamlit run app.py
```

Application will open automatically in the browser.

Default URL:

```text
http://localhost:8501
```

---

# Output Files

The pipeline automatically generates:

```text
data/raw_news.csv
```

Raw collected news articles.

```text
data/processed_news.csv
```

Deduplicated and relevant articles.

```text
data/newsletter.json
```

Generated newsletter content.

---

# Streamlit Dashboard

The dashboard provides:

* Newsletter Generation
* File Status Monitoring
* Processed Article View
* Question Answering Interface
* Downloadable Outputs

---

# Security Notes

## Important

Do NOT commit API keys to GitHub.

Add `.env` to `.gitignore`.

Example:

```gitignore
.env
__pycache__/
*.pyc
logs/
```

---

# OpenAI API Key for End Users

End users do NOT need an OpenAI API key when using the deployed application.

The API key is configured only on the server hosting the application.

Examples:

* Streamlit Cloud Secrets
* Azure App Service Environment Variables
* AWS Secrets Manager
* Docker Environment Variables

The API key is never exposed to users.

---

# Future Enhancements

* Multi-source news aggregation
* Google News integration
* Export to DOCX
* Export to PPTX
* Export to XLSX
* Vector Database Support
* RAG-based Question Answering
* Multi-Agent Review Workflow

---

# Tech Stack

* Python
* LangGraph
* LangChain
* OpenAI GPT-4o
* Streamlit
* Sentence Transformers
* Scikit-Learn
* Pandas

---




# Future Improvements & Production Enhancements

## Current Scope

This project is designed as a proof-of-concept (POC) demonstrating:

* Real-time FMCG news aggregation
* De-duplication
* Relevance filtering
* Credibility scoring
* Newsletter generation
* Interactive Streamlit dashboard

The implementation prioritizes simplicity, transparency, and explainability.

---

# Potential Enhancements for Production Deployment

## 1. Expanded News Coverage

Current implementation uses a limited number of RSS feeds.

Future improvements:

* Google News RSS
* Reuters Business
* Bloomberg Deals
* Crunchbase News
* FMCG company press releases
* Regulatory filings
* Financial news APIs

Benefits:

* Better coverage
* More accurate deal tracking
* Reduced risk of missing important announcements

---

## 2. Advanced Deal Detection

Current relevance filtering relies on GPT classification.

Production version could include:

* Fine-tuned classification models
* Industry-specific taxonomies
* Entity extraction
* Event extraction

Deal types:

* Acquisition
* Merger
* Joint Venture
* Investment
* Funding
* Divestiture
* Strategic Partnership

Benefits:

* Higher precision
* Lower false positives

---

## 3. RAG-Based Question Answering

Current implementation uses article context directly.

Future enhancement:

* Vector Database integration

Examples:

* Pinecone
* Chroma
* FAISS
* Azure AI Search

Benefits:

* Faster retrieval
* Improved accuracy
* Better handling of large news archives

---

## 4. Multi-Agent Review Workflow

Current workflow:
text
Fetch
→ Clean
→ Deduplicate
→ Relevance
→ Credibility
→ Newsletter
```

Future workflow:

```text
Research Agent
→ Fact Check Agent
→ Credibility Agent
→ Editorial Agent
→ Newsletter Agent
```

Benefits:

* Higher quality output
* Reduced hallucinations
* Better business summaries

---

## 5. Source Credibility Enhancement

Current credibility scoring uses trusted domain matching.

Production enhancement:

* Domain authority scoring
* Publisher reputation metrics
* Historical accuracy tracking
* Confidence scoring

Benefits:

* More reliable intelligence reports

---

## 6. Automated Scheduling

Current implementation requires manual execution.

Future enhancement:

* Daily newsletter generation
* Weekly executive summaries
* Automated report distribution

Technologies:

* Airflow
* Azure Data Factory
* AWS EventBridge
* GitHub Actions

Benefits:

* Fully automated intelligence pipeline

---

## 7. Email Distribution

Future enhancement:

* Automated newsletter delivery

Channels:

* Email
* Microsoft Teams
* Slack
* SharePoint

Benefits:

* Improved stakeholder adoption

---

## 8. Analytics Dashboard

Future enhancement:

* Deal trend analysis
* Geographic distribution
* Industry segmentation
* Company-level activity tracking

Benefits:

* Strategic decision support

---

## 9. Human-in-the-Loop Validation

Future enhancement:

* Analyst review workflow
* Approval before publication
* Feedback collection

Benefits:

* Higher confidence outputs
* Better governance

---

## 10. Enterprise Security & Compliance

Production deployment considerations:

* Secret management
* Role-based access control
* Audit logging
* Data retention policies
* GDPR compliance
* Enterprise authentication (SSO)

Benefits:

* Secure enterprise adoption

---

# Assumptions

This solution assumes:

1. Publicly available news sources provide sufficient deal information.
2. RSS feeds remain accessible.
3. OpenAI GPT-4o is available for relevance classification and newsletter generation.
4. Credibility scoring is based on predefined trusted domains.
5. Newsletter generation is intended for business intelligence purposes and should not be considered financial advice.

---

# Limitations

Current implementation limitations include:

* Limited source coverage
* No historical news archive
* No vector database
* Basic credibility scoring
* No analyst review workflow
* Dependence on external LLM services

These limitations can be addressed through the future enhancements described above.

---

# Business Value

The solution enables business users to:

* Monitor FMCG M&A activity
* Track investment trends
* Reduce manual research effort
* Receive concise executive summaries
* Quickly identify significant market developments

This creates a scalable foundation for an FMCG market intelligence platform.

# Author

Rahul Prajapati
Data Science | GenAI | Agentic AI
GitHub: <https://github.com/rahul6796>
LinkedIn: <https://www.linkedin.com/in/rahul-prajapati-728727175/>
