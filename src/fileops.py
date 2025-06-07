import pandas as pd

def save_superheroes(df, path="data/superheroes.csv"):
    try:
        df.to_csv(path, index=False)
        
    except Exception as e:
        print(f" Error saving superheroes: {e}")

def save_links(df, path="data/links.csv"):
    try:
        df.to_csv(path, index=False)
        
    except Exception as e:
        print(f" Error saving links: {e}")
