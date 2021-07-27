
# List
import datetime

l_employe = [
    "Harishkumar",
    "EP-00123",
    # datetime.date(day=2, month=9, year=1986),
    "2-sep-1986",
    '30000'
]

print(type(l_employe))
print(l_employe)
print(l_employe[1])
print(l_employe[-1])
print(l_employe[::-1])

l_employe.append("STL")
l_employe.append("new Project")
print(l_employe)


sliced = l_employe.pop(1)
print(l_employe)

print(sliced)

my_string = "Hello world! This is so beautifully"
my_string_list = my_string.split(" ")
print(my_string_list)

new_string = ",".join(my_string_list)
print(new_string)

l_employe[0] = "Harishkumar Reddy"
print(l_employe)

# my_string_list.extend(l_employe)
new_list = my_string_list+l_employe
print(new_list)

new_list.sort()
print(new_list)
new_list.sort(reverse=True)
print(new_list)
new_list.insert(3, "New String")
print(new_list)

print(l_employe)
abc= []
abc.append(int(l_employe[2]) * 12)

print(abc)

