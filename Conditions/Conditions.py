"""
### Conditional statements:
1. if
2. if...else
3. if...elif...else
4. Nested if's
5. Ternary
"""

a,b,c = 2,3,"5"

print(a,b,c)
# print(a+c)
print(c+c)

# if <condition> :
#    <statements>
print("before", type(c))

if type(c) is str:
    c = int(c)
    print("before", type(c))

print(c+c)

a = 3
if a % 2 == 0:
    print(f"{a} is Even.")
else:
    print(f"{a} is Odd.")

# 1-> muti checks for same actions
c = ""
if type(c) is str and c != "":
    c = int(c)
    print("before", type(c))
else:
    c = 0


# message = "Apple"
message = "Banana"
ovels = ["a", "e", "i", "o", "u"]

# print("a" != "A")
# print("_".upper() and "_".upper())
print(message[0].lower() < "a")
print(message[0].lower() > "z")

if message[0].lower() < "a" or message[0].lower() > "z":
    print(f"{message} is not started with alphabets")
elif message[0].lower() in ovels:
    print(f"{message} is an ovel")
else:
    print(f"{message} is not an ovel")


if message[0].lower() >= "a" and message[0].lower() <= "z":
    if message[0].lower() in ovels:
        print(f"{message} is an ovel")
    else:
        print(f"{message} is not an ovel")
else:
    print(f"{message} is not started with alphabets")


d = "6"
cat = "is Alphabet" if d >= "a" and d <= "z"  else "not an Alphabet"
print(cat)
