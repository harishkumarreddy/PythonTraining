# Databricks notebook source
message = "Hello World"
print(message)

# COMMAND ----------

rev_message = message[::-1]
print(rev_message)

# COMMAND ----------

new_message = message.replace("World", "Dunia")
print(new_message)

# COMMAND ----------

print(new_message.find("Dunia"))
print(new_message.find("Dunias"))

# COMMAND ----------

print(new_message[6:])

print("before:", new_message)
new_message = message
print("after: ", new_message)

# Naming Conventions:
# SnakeCase: NewMessage
# CamelCase: newMessage
# Consent/Fat Case: NEW_MESSAGE
# Lean Case: new_message
