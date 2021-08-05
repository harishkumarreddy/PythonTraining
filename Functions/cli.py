import sys

inputs = sys.argv[1:]


def calc(num1, num2, opr=""):
    if num1 is not int:
        num1 = int(num1)

    if num2 is not int:
        num2 = int(num2)

    output = None
    if opr == "+":
        output = num1 + num2
    elif opr == "-":
        output = num1 - num2
    elif opr == "*":
        output = num1 * num2
    elif opr == "/":
        output = num1 / num2

    return output


n1, opr, n2 = inputs
res = calc(num1=inputs[0], opr=inputs[1], num2=inputs[2])
res1 = calc(num1=n1, opr=opr, num2=n2)
res2 = calc(n1, n2, opr)

print(res)
print(res1)
print(res2)

