"""
Operators:
1. Arithmetic operators     ->  +, -, *, /, %, **, //
    NOTE: These will follow the BODMAS rule
2. Assignment operators     ->  =, +=, -=, *=, /=, %=, **=, //=
3. Comparison operators     ->  ==, !=, <, <=, >, >=
4. Logical operators        ->  and, or, not
5. Identity operators       ->  is, is not
6. Membership operators     ->  in, not in
7. Bitwise operators        ->  &, |, ^, ~, <<, >>


T-Table:
TRUE and TRUE = TRUE
TRUE and FALSE = FALSE
FALSE and TRUE = FALSE
FALSE and FALSE = FALSE

TRUE or TRUE = TRUE
TRUE or FALSE = TRUE
FALSE or TRUE = TRUE
FALSE or FALSE = FALSE

not TRUE = FALSE
not FALSE = TRUE

"""

# a = 2
# b = 3

a,b = 2,3
x = y = 5
print(x,y)
print(a,b)

print("+:", a+b)
print("-:", a-b)
print("*:", a*b)
print("/:", a/b)
print("**:", a**b)
print("%:", a%b)
print("%:", b%a)
print("//:", a//b)

c = a+b
print("C", c)
a = a+1
print("a+1",a)
a += 1
d = 5
print("d:", d)
d+=1
print("+=", d)
d -= 1
print("-=", d)
d *= 2
print("*=", d)
d /= 2
print("/=", d)
d **= 2
print("**=", d)
d %= 2
print("%=", d)
d //= 2
print("//=", d)

print(a,b)
print("==:", a == b)
print("!=:", a != b)
print(">:", a > b)
print(">=:", a >= b)
print("<:", a < b)
print("<=:", a <= b)

print("and:", a == b and a != b)
print("and:", a >= b and a != b)
print("and both false:",  a == b and a <= b)
print("and both false:", (not a == b))
print("and both false:", (not a <= b))
print("and both false:", (not a == b) and (not a <= b))
print("and both false:", not((not a == b) and (not a <= b)))

print("or:", a == b or a != b)

print("not:", not a == b)
print("not:", not a != b)

print("is:", 1 is "1")
print("is not:", 1 is not "1")

message = "Hello world!"
print("in:", "!" in message)
print("multiple in:", ("z" in message) and ("world" in message))
print("in:", "z" in message)
print("in:", "world" in message)
print("in:", "world#" in message)

print("not in:", "world" not in message)
print("not in:", "world#" not in message)
