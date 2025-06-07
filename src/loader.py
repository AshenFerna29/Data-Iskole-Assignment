# src/loader.py
import pandas as pd
import logging

# Configure logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def load_superheroes(filepath):
    try:
        df = pd.read_csv(filepath, dtype={"id": int})
        df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
        return df
    except FileNotFoundError:
        print(f"Error: '{filepath}' not found.")
        logger.error(f"File not found: {filepath}")
        return pd.DataFrame(columns=["id", "name", "created_at"])
    except Exception as e:
        logger.error(f"Failed to load superheroes: {e}")
        return pd.DataFrame(columns=["id", "name", "created_at"])

def load_links(filepath):
    try:
        return pd.read_csv(filepath, dtype={"source": int, "target": int})
    except FileNotFoundError:
        print(f"Error: '{filepath}' not found.")
        logger.error(f"File not found: {filepath}")
        return pd.DataFrame(columns=["source", "target"])
    except Exception as e:
        logger.error(f"Failed to load links: {e}")
        return pd.DataFrame(columns=["source", "target"])
