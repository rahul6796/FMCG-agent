
import os
import pandas as pd

from utils.logger import logger

TRUSTED_DOMAINS = [
    "reuters.com",
    "bloomberg.com",
    "foodbusinessnews.net",
    "just-food.com"
]

os.makedirs(
    "data",
    exist_ok=True
)

def credibility_agent(state):

    logger.info(
        "Credibility scoring"
    )

    updated = []

    for row in state["relevant_news"]:

        score = 0.5

        for domain in TRUSTED_DOMAINS:

            if domain in row["link"]:

                score = 1.0

        row["credibility_score"] = score

        updated.append(row)

    state["relevant_news"] = updated

    # Save final processed output

    pd.DataFrame(
        updated
    ).to_csv(
        "data/processed_news.csv",
        index=False
    )

    logger.info(
        f"Saved processed_news.csv with {len(updated)} rows"
    )

    return state

