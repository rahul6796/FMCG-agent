
from langchain_openai import ChatOpenAI
from utils.logger import logger
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)

def relevance_check(state):

    logger.info(
        "Relevance checking"
    )

    df = state["cleaned_news"]

    relevant = []

    for _, row in df.iterrows():

        prompt = f"""
Determine if this article is about:

- Acquisition
- Merger
- Investment
- Funding
- Stake purchase
- FMCG expansion

Return ONLY:

YES

or

NO

Title:
{row['title']}

Summary:
{row['summary']}
"""

        result = llm.invoke(
            prompt
        )

        answer = (
            result.content
            .strip()
            .upper()
        )

        if answer.startswith(
            "YES"
        ):
            relevant.append(
                row.to_dict()
            )

    logger.info(
        f"Relevant articles={len(relevant)}"
    )

    # fallback
    if len(relevant) == 0:

        logger.info(
            "No relevant articles found. Using first 10 articles."
        )

        relevant = (
            df.head(10)
            .to_dict(
                orient="records"
            )
        )

    state["relevant_news"] = relevant

    return state

