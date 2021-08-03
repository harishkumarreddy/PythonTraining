import time

message=["Ricky","alex","David","gary"]
print("Input: ",message)

"""
Steps:
1. pick each item
2. compare with output list.
    2.1. if output list is empty, add it to output list.
    2.2. if output list is no empty, check the item with each item of output list 
    2.3. if item is lesser then the existed list items, append before the list
    2.4. if item is higher then the list, append at end of the list
3. update the input if required
4. print and exit.
"""
s = time.perf_counter()
output = []
# 1. pick each item
for item in message:
    # 2. compare with output list.
    if len(output) == 0:
        # 2.1. if output list is empty, add it to output list.
        output.append(item)
    else:
        # 2.2. if output list is no empty, check the item with each item of output list
        n = 0
        for o_item in output:
            # 2.3. if item is lesser then the existed list items, append before the list
            # or before the output item
            if item <= o_item:
                output.insert(n, item)
                break
            else:
                n += 1
                continue
        else:
            # 2.4. if item is higher then the list, append at end of the list
            output.append(item)
e = time.perf_counter()
# 4. print and exit.
print("Output with case sensitive: ", output)
print(f"elapsed time: {(e-s):0.10f} ")


output = []
s = time.perf_counter()
for item in message:
    if len(output) == 0:
        output.append(item)
    else:
        n = 0
        for o_item in output:
            if item.lower() <= o_item.lower():
                output.insert(n, item)
                break
            else:
                n += 1
                continue
e = time.perf_counter()
print("Output with case in-sensitive: ", output)
print(f"elapsed time: {(e-s):0.10f} ")

"""
1. Babble:
2. Quick:
**3. binary:
"""

# for i in range(0,3):
#     j=1
#     if message[i][0].lower() > message[j][0].lower():
#         message[i], message[j] = message[j], message[i]
#         k=2
#         if message[j][0].lower() > message[k][0].lower():
#             message[j], message[k] = message[k], message[j]
#             l=3
#             if message[k][0].lower() > message[l][0].lower():
#                 message[k], message[l] = message[l], message[k]
#             l+=1
#         k+=1
#     j+=1
# print(message)
