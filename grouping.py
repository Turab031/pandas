#%%
import pandas as pd
# %%

df = pd.read_csv("raw_data.csv")
# %%
df
# %%

df.groupby("country")
# %%
df.groupby("country")["income"].mean()

# %%
df.groupby("gender")["income"].mean()
# %%
df.groupby("country")["income"].agg(["mean","max","min"])
# %%
