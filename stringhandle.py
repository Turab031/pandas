#%%
import pandas as pd
# %%
df = pd.read_csv("raw_data.csv")

df["gender"].str.upper()
# %%

df["name"].str.split(" ")
# %%

df["country"].str.contains("india",case=False)
# %%
