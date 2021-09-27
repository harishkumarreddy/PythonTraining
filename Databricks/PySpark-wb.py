# Databricks notebook source
# MAGIC %md # Dataframes

# COMMAND ----------

# MAGIC %fs ls "/databricks-datasets/samples/"

# COMMAND ----------

df = spark.read \
.format("csv") \
.option("header", "true") \
.option("inferSchema", "true") \
.load("/databricks-datasets/samples/population-vs-price/data_geo.csv")

# COMMAND ----------

display(df.head(5))
df.dtypes

# COMMAND ----------

df.columns

# COMMAND ----------

df = df.withColumnRenamed("2014 rank", "Rank") \
.withColumnRenamed("2014 Population estimate","Population")\
.withColumnRenamed("2015 median sales price","Price")\
.withColumnRenamed("State Code","State_code")
display(df)

# COMMAND ----------

pdf = df.toPandas()
print(type(pdf))
pdf

# COMMAND ----------

import numpy as np
pdf['Price'] = pdf['Price'].fillna(0)
pdf['Population'] = pdf['Population'].fillna(0)
prices = pdf['Price']
prices = np.array(prices)
price_mean = prices.mean()
print(price_mean)

Populations = pdf['Population']
Populations = np.array(Populations)
Pop_mean = Populations.mean()
print(Pop_mean)

# COMMAND ----------

# df = df.fillna(0,['Population', "Price"])
df = df.na.fill({
  "Population":Pop_mean,
  "Price": price_mean
})
df.show()

# COMMAND ----------

from pyspark.sql.functions import col , column
df = df.withColumn("bus_val", df['Price'] * df['Population'])
df.show()

# COMMAND ----------

mydf = df.select(["State_code", "Price"]).groupBy("State_code").mean().orderBy("State_code")
mydf.show()

# COMMAND ----------

df.where("City='Springfield'").show()

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df = df.withColumn("bus_val", df.bus_val.cast("int"))
df.show()

# COMMAND ----------

# UDF
def getPercentage(value=None, percentage=None):
  if value is None or value == "" or value == 0:
    return 0
  
  if percentage is None or percentage == "" or percentage == 0:
    return value
  
  final_val = ((value*percentage) / 100)
  return int(final_val)


# Unit testing
print(getPercentage(value=100, percentage=10))
print(getPercentage(value="", percentage=""))
print(getPercentage(value=0, percentage=0))
print(getPercentage(value=10, percentage=0))
print(getPercentage(value=0, percentage=10))
print(getPercentage(value=None, percentage=None))
print(getPercentage(value=10, percentage=None))
print(getPercentage(value=None, percentage=10))

# COMMAND ----------

spark.udf.register("udf_getPercentage", getPercentage)

# COMMAND ----------

df.createOrReplaceTempView("df_view")

# COMMAND ----------

# MAGIC %sql
# MAGIC -- show views
# MAGIC select *, udf_getPercentage(bus_val, 60) as est_cost, udf_getPercentage(bus_val, 30) as opt_cost from df_view

# COMMAND ----------

mdf = spark.sql('select *, udf_getPercentage(bus_val, 60) as est_cost, udf_getPercentage(bus_val, 30) as opt_cost from df_view')
mdf.show()

# COMMAND ----------

mdf.write.saveAsTable("bus_est")

# COMMAND ----------

import os
os.listdir("/tmp/")

# COMMAND ----------

# mdf.write.repartition(1).format("csv").mode("overwrite").save("/temp/df/mdf.csv")
mdf.write.format("csv").save("/tmp/zipco1")

# COMMAND ----------

# MAGIC %fs rm "dbfs:/temp/df/mdf/part-00000-tid-111925865517233280-485573fd-6ac9-498d-ac71-a0befe2698ca-31-1-c000.csv"

# COMMAND ----------

# MAGIC %fs ls "dbfs:/temp/df/mdf"

# COMMAND ----------



# COMMAND ----------

dbutils.fs.rm("dbfs:/temp/")

# COMMAND ----------

# MAGIC %md # DBUTILS

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.widgets.help()
# %fs

# COMMAND ----------

# MAGIC %fs cp "/data/student_scores.csv" "/data/student.csv"

# COMMAND ----------

# MAGIC %fs rm /data/student.csv

# COMMAND ----------

# MAGIC %fs 
# MAGIC 
# MAGIC ls "/data/"

# COMMAND ----------

# MAGIC %sh
# MAGIC ls -ll /mnt

# COMMAND ----------

# MAGIC %md ## Mount
# MAGIC 
# MAGIC Help : [https://docs.databricks.com/data/data-sources/azure/azure-storage.html#mount-azure-blob-storage-containers-to-dbfs]

# COMMAND ----------

storage_account_name = "adalsmanojdemo"
container_name = "input"
key_name = "OWLpKpR7VLha0sJH/UwReLeLBjvE9L7Sb1T0sFUmOrUp9uzCl+/Jpu6YU+Zmf89v2JTSbOzEtykZ+GwIF4y+0w==" # Accesskey of the container
conf_key = f"fs.azure.account.key.{storage_account_name}.blob.core.windows.net"
mount_name ="demo_input"

dbutils.fs.mount(
  source = f"wasbs://{container_name}@{storage_account_name}.blob.core.windows.net",
  mount_point = f"/mnt/{mount_name}",
  extra_configs = {"fs.azure.account.key.adalsmanojdemo.blob.core.windows.net":"OWLpKpR7VLha0sJH/UwReLeLBjvE9L7Sb1T0sFUmOrUp9uzCl+/Jpu6YU+Zmf89v2JTSbOzEtykZ+GwIF4y+0w=="})

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /mnt/demo_input/abcd_test.csv

# COMMAND ----------

adf = spark.read.csv("dbfs:/mnt/demo_input/ABCD.csv", header=True)
adf.show()

# COMMAND ----------

adf.write.csv("/mnt/demo_input/abcd_test.csv")

# COMMAND ----------

from pyspark.sql import *

# COMMAND ----------

constr="jdbc:sqlserver://harish-123.database.windows.net:1433;database=harish_db;user=dbadmin@harish-123;password=Welcome@123;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.database.windows.net;loginTimeout=30;"
mfrf = DataFrameWriter(mdf)
mfrf.jdbc(url=constr, table="bus_est")

# COMMAND ----------

sqldf = spark.read.format('jdbc').option("url", constr).option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver").option('dbtable', "bus_est").load()
sqldf.show()

# COMMAND ----------

sqldf2 = spark.read.format('jdbc').option("url", constr).option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver").option('query', "select * from bus_est where State_code='AL'").load()
sqldf2.show()

# COMMAND ----------

dbutils.secrets.get("scope", "name")
