# 1. List
# 2. Tuples
# 3. Sets
# 4. Dict

t_data = (
    "Harishkumar",
    "EP-00123",
    "2-sep-1986",
    '30000'
)

print(type(t_data))
print(t_data)
print(t_data[0])
# t_data[0] = "Harish"

tmp_list = list(t_data)
tmp_list[3] = int(t_data[3])
t_data = tuple(tmp_list)
tmp_list.clear()
print(t_data)

print("=" * 50)
print("Sets")
s_data = {
    "Harishkumar",
    "EP-00123",
    "2-sep-1986",
    '30000'
}

s_data2 = {
    "Harish",
    "EP-00123",
    "2-jun-1986",
    '40000'
}

print(s_data)
duplicates = s_data.intersection(s_data2)
print(duplicates)

full_set = s_data.union(s_data2)
print(full_set)


print("=" * 50)
print("Dict")
dict_data = {
    "name": "Harishkumar",
    "id": "EP-00123",
    "dob": "2-sep-1986",
    "sal": 30000
}
print(dict_data)
print(dict_data['name'])

dict_data['name'] = "Harish"
print(dict_data['name'])

dict_data['contact'] = "7801070710"
print(dict_data)

print(dict_data.keys())
print(dict_data.values())

print(dict_data.get('dob', "01-jan-2021"))
print(dict_data.get('doj', "01-jan-2021"))

x_lixt = [
    "val1",
    [1,2,3,4],
    [123,[456], {
        "a": "A",
        "b": "B"
    }],
]
print(x_lixt[0])
print(x_lixt[1][2])
print(x_lixt[2][2]['a'])


# x_dict = {
#     "set1": {1,2,2,3,4,4},
#     "list1": [1,2,2,3,4,4,[0,5,3]],
# }
