#%%
import pandas as pd
# %%
df = pd.read_csv("raw_data.csv")
df
# %%

df.isna()

# %%

df.isna().sum()
# %%
df.dropna()

# %%
df

# %%
age_mean = df["age"].mean()
df["age"].fillna(age_mean)
# %%

df.ffill()
# %%
df.bfill()
# %%
