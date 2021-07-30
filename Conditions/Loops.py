"""
Loops:
1. for loop
2. while loop
3. do while *
"""

# for <i var> in <range>:
#    <statements>
print("Before for loop")

for i in range(10):
    print(f"i val is: {i}")

print("After for loop")

t_data = (
    "Harishkumar",
    "EP-00123",
    "2-sep-1986",
    '30000'
)

for item in t_data:
    print(f"item is: {item}")

x_dict = {
    "set1": [1,2,2,3,4,4], # => ("set1", [1,2,2,3,4,4])
    "list1": [1,2,2,3,4,4,[0,5,3]],
}

# for item in x_dict:
#     print(f"dict item is: {item}: {x_dict[item]}")
#     n=0
#     for s_item in x_dict[item]:
#         print(f"access {s_item} with x_dict['{item}']['{n}']")
#         n+=1

for item,i_value in x_dict.items():
    print(f"dict item is: {item}: {i_value}")
    n=0
    for s_item in i_value:
        print(f"access {s_item} with x_dict['{item}']['{n}']")
        n+=1

