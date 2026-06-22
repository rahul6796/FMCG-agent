from typing import TypedDict
import pandas as pd


class NewsletterState(TypedDict):
    raw_news: pd.DataFrame
    cleaned_news: pd.DataFrame
    relevant_news: list
    newsletter: str
