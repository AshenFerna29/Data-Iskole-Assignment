# src/fileops.py
import pandas as pd
from logger import logger

def save_superheroes(df, path="data/superheroes.csv"):
    try:
        df.to_csv(path, index=False)
    except Exception as e:
        logger.error(f"Error saving superheroes: {e}")

def save_links(df, path="data/links.csv"):
    try:
        df.to_csv(path, index=False)
    except Exception as e:
        logger.error(f"Error saving links: {e}")
