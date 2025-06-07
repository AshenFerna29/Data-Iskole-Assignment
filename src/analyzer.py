# src/analyzer.py
from collections import Counter
import pandas as pd
from datetime import datetime, timedelta

def get_total_counts(superheroes_df, links_df):
    try:
        return len(superheroes_df), len(links_df)
    except Exception as e:
        print(f"Error counting totals: {e}")
        return 0, 0

def get_recent_heroes(superheroes_df, days=3):
    try:
        cutoff = datetime.now() - timedelta(days=days)
        return superheroes_df[superheroes_df["created_at"] >= cutoff].sort_values(by="created_at", ascending=False)
    except Exception as e:
        print(f"Error filtering recent heroes: {e}")
        return pd.DataFrame(columns=["id", "name", "created_at"])

def get_most_connected(links_df, superheroes_df, top_n=3):
    try:
        connections = pd.concat([links_df['source'], links_df['target']])
        counts = Counter(connections).most_common(top_n)
        results = []
        for hero_id, count in counts:
            name_series = superheroes_df.loc[superheroes_df["id"] == hero_id, "name"]
            if not name_series.empty:
                name = name_series.values[0]
            else:
                name = "Unknown"
            results.append((name, hero_id, count))
        return results
    except Exception as e:
        print(f"Error calculating most connected superheroes: {e}")
        return []

def get_dataiskole_info(superheroes_df, links_df):
    try:
        df = superheroes_df[superheroes_df["name"].str.lower() == "dataiskole"]
        if df.empty:
            return None, []

        hero_id = df.iloc[0]["id"]
        date_added = df.iloc[0]["created_at"]

        friends_from = links_df[links_df["source"] == hero_id]["target"]
        friends_to = links_df[links_df["target"] == hero_id]["source"]
        friend_ids = pd.concat([friends_from, friends_to]).unique()

        friend_names = superheroes_df[superheroes_df["id"].isin(friend_ids)]["name"].tolist()
        return date_added, friend_names
    except Exception as e:
        print(f"Error retrieving info for 'dataiskole': {e}")
        return None, []
