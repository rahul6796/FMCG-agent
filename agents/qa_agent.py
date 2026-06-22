
import pandas as pd
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)

def answer_question(question: str):

    try:

        df = pd.read_csv(
            "data/processed_news.csv"
        )

        context = ""

        for _, row in df.iterrows():

            context += f"""
            Title: {row['title']}

            Summary: {row['summary']}
            """

            prompt = f"""
            You are an FMCG industry analyst.

            Use the articles below to answer the question.

            Articles:
            {context}

            Question:
            {question}"""

        response = llm.invoke(prompt)

        return response.content

    except Exception as e:

        return f"Error: {str(e)}"
