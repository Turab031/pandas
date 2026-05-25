#%%

import pandas as pd

# %%
df = pd.DataFrame({
    "country":["usa","usa","india","india"],
    "year":[2020,2021,2020,2021],
    "sales":[100,120,90,110],
    "profit":[20,25,18,22]

})


melted=df.melt(

    id_vars=["country","year"],
    value_vars=["sales","profit"],
    var_name="metrix",
    value_name="value"

)

df
# %%
print(melted)
# %%
original = melted.pivot(
    index=["country","year"],
    columns= "metrix",
    values="value"
)

original
# %%
