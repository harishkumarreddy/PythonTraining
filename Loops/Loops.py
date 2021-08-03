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


print("While block")
x = 10
xi =0
y = 0
while xi<=x:
    while 3 <= xi <= 5:
        print(f"The y number is: {y}")
        y += 5
        xi += 1
    print(f"The xi number is: {xi}")
    xi += 1


print("Short hand:")
s1 = [i for i in range(10) if i%2 == 0] # => fill with 10 numbers from 0 to 10
s2 = [i for i in range(10) if i%2 == 1]
s3 = [chr(i) for i in range(ord("a"), ord("z")+1)]
s4 = [{"char":chr(i), "ASCI": i }for i in range(ord("a"), ord("z")+1)]

# for i in range(10):
#     s1.append(i)
print(s1)
print(s2)
print(s3)
print(s4)

print("additional")
for i in range(10):
    if i == 3:
        continue

    if i == "7":
        break

    print(i)
else:
    print("Else triggered")
