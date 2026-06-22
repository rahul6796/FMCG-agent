
import os
import json
import pandas as pd
import streamlit as st

from graph.workflow import graph
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


st.set_page_config(
    page_title="FMCG M&A Intelligence Agent",
    page_icon="📰",
    layout="wide"
)

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)


if "newsletter" not in st.session_state:
    st.session_state.newsletter = ""

if "answer" not in st.session_state:
    st.session_state.answer = ""

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title(
    "📰 FMCG M&A Intelligence Newsletter Agent"
)

st.markdown(
    """
Generate FMCG M&A intelligence newsletters
and ask business questions about
investments, acquisitions and trends.
"""
)


with st.sidebar:

    st.header("📊 System Status")

    if os.path.exists(
        "data/raw_news.csv"
    ):

        try:

            raw_df = pd.read_csv(
                "data/raw_news.csv"
            )

            st.success(
                f"Raw CSV ({len(raw_df)} rows)"
            )

        except:

            st.success(
                "Raw CSV Available"
            )

    else:

        st.error(
            "Raw CSV Missing"
        )

    if os.path.exists(
        "data/processed_news.csv"
    ):

        try:

            processed_df = pd.read_csv(
                "data/processed_news.csv"
            )

            st.success(
                f"Processed CSV ({len(processed_df)} rows)"
            )

        except:

            st.success(
                "Processed CSV Available"
            )

    else:

        st.error(
            "Processed CSV Missing"
        )

    if os.path.exists(
        "data/newsletter.json"
    ):

        st.success(
            "Newsletter JSON Available"
        )

    else:

        st.error(
            "Newsletter JSON Missing"
        )

if st.button(
    "🚀 Generate Newsletter",
    use_container_width=True
):

    progress = st.progress(0)

    status = st.empty()

    try:

        status.info(
            "📡 Fetching FMCG articles..."
        )
        progress.progress(20)

        status.info(
            "🧹 Cleaning articles..."
        )
        progress.progress(40)

        status.info(
            "🔍 Deduplicating articles..."
        )
        progress.progress(60)

        status.info(
            "🎯 Relevance filtering..."
        )
        progress.progress(80)

        status.info(
            "📝 Generating newsletter..."
        )
        progress.progress(90)

        result = graph.invoke({})

        # Debug Output

        st.write(
            "Workflow Result Keys:",
            list(result.keys())
        )

        if "relevant_news" in result:

            st.write(
                "Relevant Articles:",
                len(
                    result["relevant_news"]
                )
            )

        st.write(
            "Raw CSV Exists:",
            os.path.exists(
                "data/raw_news.csv"
            )
        )

        st.write(
            "Processed CSV Exists:",
            os.path.exists(
                "data/processed_news.csv"
            )
        )

        st.write(
            "Newsletter JSON Exists:",
            os.path.exists(
                "data/newsletter.json"
            )
        )

        st.session_state.newsletter = (
            result.get(
                "newsletter",
                "Newsletter generation failed."
            )
        )

        progress.progress(100)

        status.success(
            "Newsletter generated successfully!"
        )

    except Exception as e:

        st.error(
            f"Pipeline Error: {str(e)}"
        )


if st.session_state.newsletter:

    st.markdown("---")

    st.subheader(
        "📋 Generated Newsletter"
    )

    st.markdown(
        st.session_state.newsletter
    )

# ==========================================
# ASK QUESTIONS
# ==========================================

st.markdown("---")

st.subheader(
    "💬 Ask Questions"
)

question = st.text_input(
    "Ask about FMCG acquisitions, investments, trends..."
)

if st.button(
    "Ask Question",
    use_container_width=True
):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Analyzing FMCG articles..."
        ):

            try:

                context = ""

                if os.path.exists(
                    "data/processed_news.csv"
                ):

                    df = pd.read_csv(
                        "data/processed_news.csv"
                    )

                    for _, row in df.iterrows():

                        context += f"""
Title:
{row.get('title', '')}

Summary:
{row.get('summary', '')}

"""

                history_context = ""

                for chat in (
                    st.session_state.chat_history[-5:]
                ):

                    history_context += f"""
Question:
{chat['question']}

Answer:
{chat['answer']}
"""

                prompt = f"""
You are an FMCG Industry Analyst.

Use the processed FMCG articles
and previous conversation context.

Previous Conversation:

{history_context}

Articles:

{context}

Current Question:

{question}

Provide a concise,
business-friendly answer.
"""

                response = llm.invoke(
                    prompt
                )

                answer = (
                    response.content
                )

                st.session_state.chat_history.append(
                    {
                        "question": question,
                        "answer": answer
                    }
                )

                st.session_state.answer = (
                    answer
                )

            except Exception as e:

                st.session_state.answer = (
                    f"Error: {str(e)}"
                )

# ==========================================
# SHOW LATEST ANSWER ONLY
# ==========================================

if st.session_state.answer:

    st.markdown("---")

    st.subheader(
        "📌 Answer"
    )

    st.markdown(
        st.session_state.answer
    )

# ==========================================
# PROCESSED ARTICLES
# ==========================================

if os.path.exists(
    "data/processed_news.csv"
):

    st.markdown("---")

    st.subheader(
        "📄 Processed Articles"
    )

    try:

        df = pd.read_csv(
            "data/processed_news.csv"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    except Exception as e:

        st.error(
            str(e)
        )

# ==========================================
# DOWNLOADS
# ==========================================

st.markdown("---")

st.subheader(
    "⬇ Downloads"
)

col1, col2, col3 = st.columns(3)

with col1:

    if os.path.exists(
        "data/raw_news.csv"
    ):

        with open(
            "data/raw_news.csv",
            "rb"
        ) as f:

            st.download_button(
                "Download Raw CSV",
                f,
                file_name="raw_news.csv"
            )

with col2:

    if os.path.exists(
        "data/processed_news.csv"
    ):

        with open(
            "data/processed_news.csv",
            "rb"
        ) as f:

            st.download_button(
                "Download Processed CSV",
                f,
                file_name="processed_news.csv"
            )

with col3:

    if os.path.exists(
        "data/newsletter.json"
    ):

        with open(
            "data/newsletter.json",
            "rb"
        ) as f:

            st.download_button(
                "Download Newsletter JSON",
                f,
                file_name="newsletter.json"
            )
