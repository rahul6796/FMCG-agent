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

# Author

Rahul Prajapati
Data Science | GenAI | Agentic AI
GitHub: <your-github-link>
LinkedIn: <your-linkedin-link>

