import pandas as pd
import os

folder = "data/processed/library_clean"

files = [f for f in os.listdir(folder) if f.endswith(".csv")]

df = pd.concat([pd.read_csv(f"{folder}/{f}") for f in files])

df.to_csv("data/processed/library_final.csv", index=False)

print("Library merged")