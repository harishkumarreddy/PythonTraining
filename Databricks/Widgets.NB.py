# Databricks notebook source
# MAGIC %md # Widgets
# MAGIC 
# MAGIC * Text
# MAGIC * Dropdown
# MAGIC * Combobox
# MAGIC * Multiselect

# COMMAND ----------

dbutils.widgets.help()
# dbutils.widgets.help("text")

# COMMAND ----------

dbutils.widgets.text(name="myText", defaultValue="", label= "My Text")
# dbutils.widgets.dropdown(name="myDropDown", defaultValue="1", label= "My DropDown", choices=[str(x) for x in range(1, 10)] )
# dbutils.widgets.combobox(name="myCombo", defaultValue="1", label= "My Combo", choices=[str(x) for x in range(1, 10)] )
# dbutils.widgets.multiselect(name="myMultiselect", defaultValue="1", label= "My Multiselect", choices=[str(x) for x in range(1, 10)] )

# COMMAND ----------

myText_val = dbutils.widgets.get("myText")
myDropDown_val = dbutils.widgets.get("myDropDown")
myCombo_val = dbutils.widgets.get("myCombo")
myMultiselect_val = dbutils.widgets.get("myMultiselect")

# COMMAND ----------

print(myText_val)
print(myDropDown_val)
print(myCombo_val)
print(myMultiselect_val)

# COMMAND ----------

# dbutils.widgets.remove("myText")
dbutils.widgets.removeAll()

# COMMAND ----------

import sys
sys.version_info

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from xyz using delta

# COMMAND ----------


