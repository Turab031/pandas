#%%
import pandas as pd


df = pd.read_csv("employee_data.csv")
 
df
# %%
df["Salary"].hist()
# %%

df.plot(kind="scatter",x="Age",y="Salary")

# %%
