
import json
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from utils.logger import logger

load_dotenv()

os.makedirs("data", exist_ok=True)

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)


def generate_newsletter(state):

    logger.info(
        "Generating newsletter"
    )

    articles = ""

    for row in state["relevant_news"]:

        articles += f"""
Title:
{row['title']}

Summary:
{row['summary']}
"""

    prompt = f"""
Create a concise FMCG
M&A newsletter.

Sections:

1. Executive Summary
2. Major Deals
3. Investments
4. Insights
5. Outlook

Articles:

{articles}
"""

    response = llm.invoke(
        prompt
    )

    newsletter_text = (
        response.content
    )

    # SAVE JSON

    with open(
        "data/newsletter.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            {
                "newsletter": newsletter_text
            },
            f,
            indent=4,
            ensure_ascii=False
        )

    state["newsletter"] = (
        newsletter_text
    )

    logger.info(
    f"Articles passed to newsletter = {len(state['relevant_news'])}"
)
    return state

