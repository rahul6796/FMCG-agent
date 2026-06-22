
import os

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from utils.logger import logger

os.makedirs("data", exist_ok=True)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def deduplicate_news(state):

    logger.info(
        "Deduplication started"
    )

    df = state["cleaned_news"]

    if len(df) == 0:

        state["cleaned_news"] = df

        return state

    texts = (
        df["title"].fillna("")
        + " "
        + df["summary"].fillna("")
    ).tolist()

    embeddings = model.encode(
        texts
    )

    similarity = cosine_similarity(
        embeddings
    )

    keep = []

    for i in range(len(df)):

        duplicate = False

        for j in keep:

            if similarity[i][j] > 0.90:

                duplicate = True

                break

        if not duplicate:

            keep.append(i)

    processed_df = (
        df.iloc[keep]
        .reset_index(drop=True)
    )

    # SAVE PROCESSED CSV
    processed_df.to_csv(
        "data/processed_news.csv",
        index=False
    )

    state["cleaned_news"] = processed_df

    logger.info(
        f"After dedup = {len(processed_df)}"
    )

    return state
