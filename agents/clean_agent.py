from utils.logger import logger

def clean_news(state):

    logger.info("Cleaning data")
    df = state["raw_news"]
    df = df.drop_duplicates()
    df = df.fillna("")
    state["cleaned_news"] = df
    logger.info(f"Cleaned rows={len(df)}")
    return state