# """
# Functions:
# 1. pre-def Functions
# 2. udf Functions
# 3. Lambda Function
# """
#
# # def <functionname>():
# #   pass
#
# # def wish():
# #     print("Hello World!")
#
# print("before the function")
#
#
# # def wish(w_name):
# #     print(f"Hello {w_name}!")
# #     return f"Hello {w_name}!"
#
# # def wish(w_name: dict):
# #     print(f"Hello {w_name}!")
# #     return f"Hello {w_name}!"
#
# def wish(w_name: dict) -> dict:
#     print(f"Hello {w_name}!")
#     return f"Hello {w_name}!"
#
#
# #
# # def wish(w_namee: dict):
# #     print(f"Hello __ {w_namee}!")
# #     return f"Hello __ {w_namee}!"
#
#
# def udf_print(msg):
#     print(f"your msg: {msg}")
#
#
# udf_print("After the function")
# em_name = "Hearishkumar"
# em_name = 123456
# message = wish([1, 2])
# print("After calling the function")
# print(message)
#
# get_remainder = lambda a, b: a / b
# get_index = lambda my_str, term: my_str.index(term)
# n = get_remainder(5, 2)
# print(n)
#
# print(get_index("hello world!", "rld"))
#


# def calc(num1, num2, opr=""):
#     output = None
#     if opr == "+":
#         output = num1 + num2
#     elif opr == "-":
#         output = num1 - num2
#     elif opr == "*":
#         output = num1 * num2
#     elif opr == "/":
#         output = num1 / num2
#
#     return output
#
#
# # res = calc(2, "+", 3)
# res = calc(num1=2, opr="*", num2=3)
# print(res)

"""
a. args -> *args
b. kwargs -> **kwargs / **args
"""
# a,b = 1,2
a, *b = [1, 2,3]

print(a, b)

# def read_inputs(key, *value):
#     print(f"key: {key} \nValue: {value}")


def read_inputs(key, **value):
    print(f"key: {key} \nValue: {value}")

read_inputs("filters", col1="%abc", col2="z%")

x =10
print(x)
def printX():
    x = 20
    print(x)


printX()
print(x)
