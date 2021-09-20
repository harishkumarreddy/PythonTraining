# Databricks notebook source
import pandas as pd

# COMMAND ----------

data = {
  "stuname":["a","b", "c","d","e"],
  "grade":[3,5,1,2,4]
}

# COMMAND ----------

df = pd.DataFrame(data)
df

# COMMAND ----------

htno = [2654,4568,4578,4568,4875]
htno_sr = pd.Series(htno)
htno_sr
htno_sr = pd.Series(htno, index=["a","b", "c","d","e"])
htno_sr
htno_sr = pd.Series(htno, index=None)
htno_sr

# COMMAND ----------

df.loc[0]
df.iloc[1]
df.iloc[1]['stuname'].upper()


# COMMAND ----------

# MAGIC %fs 
# MAGIC cp dbfs:/FileStore/tables/dirtydata.csv file:/tmp/tables/dirtydata.csv

# COMMAND ----------

# MAGIC %fs 
# MAGIC ls file:/tmp/tables/

# COMMAND ----------

# df1 = pd.read_csv("/dbfs/FileStore/tables/dirtydata.csv")
df1 = pd.read_csv("file:/tmp/tables/dirtydata.csv")
df1.tail()

# COMMAND ----------

df1.info()


# COMMAND ----------

df1.count()

# COMMAND ----------

df1.describe()

# COMMAND ----------

df1.loc[7, 'Duration'] = 45
df1

# COMMAND ----------

df1[df1.duplicated()]

# COMMAND ----------

df1=df1.drop_duplicates(inplace=False)
df1

# COMMAND ----------

m = df1['Calories'].mean()
print(m)
df1['Calories'].fillna(value=m, inplace=True)
df1

# COMMAND ----------

df1.dropna(subset=["Date"], inplace=True)
df1

# COMMAND ----------

df1['Date'] = pd.to_datetime(df1['Date'])
df1

# COMMAND ----------

df1.info()

# COMMAND ----------

import matplotlib.pyplot as plt
df1.plot()
plt.show()

# COMMAND ----------

df1.plot(kind="hist")
plt.show()
