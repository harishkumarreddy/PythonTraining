# String.
message = "Hello World!. It is beautiful"
print(message)
print("Data Type : ", type(message))
print("Length: ", len(message))

# Uncomment these three lines to check the datatype change instently
# message = 25.5
# print(message)
# print(type(message))

print("Ass Upper case: ", message.upper())
print("Ass Lower case: ", message.lower())
print("simple split: ", message.split())
print("Split with " ": ", message.split(" "))
print("Single Split: ", message.split(maxsplit=1))

print("Char at 1'th index in the message: ", message[1])
print("String in the range: ", message[2:5])

# It has a cross collision so this line will not work
print("Reverse order(in range) in string: [start: Stop]( - reverse direction): ", message[-2:-5])

# To make it work, keep negative value right side. but not both sides
# this will get the position from reverse order
print("Reverse order(in range) in string: [start: Stop]( - reverse direction): ", message[2:-5])
