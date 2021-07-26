
# List
import datetime

l_employe = [
    "Harishkumar",
    "EP-00123",
    datetime.date(day=2, month=9, year=1986),
    30000
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
