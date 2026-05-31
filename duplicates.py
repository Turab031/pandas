#%%
import pandas as pd
# %%
df = pd.read_csv("raw_data.csv")

df.duplicated()
# %%
df.drop_duplicates()
# %%
df.dtypes
# %%
df2 = df.copy()
df2 = df2.fillna(0)

# %%


df2["age"] = df2["age"].astype("int64")

print(df2.dtypes)
# %%

