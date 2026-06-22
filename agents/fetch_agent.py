
import os
import sys
import feedparser
import pandas as pd

from utils.logger import logger
from utils.exception import CustomException

os.makedirs("data", exist_ok=True)

RSS_FEEDS = [
    "https://www.foodbusinessnews.net/rss",
    "https://www.just-food.com/feed/"
]


def fetch_news(state):

    try:

        logger.info("Fetching articles")

        articles = []

        for feed in RSS_FEEDS:

            parsed = feedparser.parse(feed)

            for item in parsed.entries:

                articles.append(
                    {
                        "title": item.get("title", ""),
                        "summary": item.get("summary", ""),
                        "link": item.get("link", "")
                    }
                )

        df = pd.DataFrame(articles)

        # SAVE RAW CSV
        df.to_csv(
            "data/raw_news.csv",
            index=False
        )

        state["raw_news"] = df

        logger.info(
            f"Fetched {len(df)} articles"
        )

        return state

    except Exception as e:

        raise CustomException(
            e,
            sys
        )

