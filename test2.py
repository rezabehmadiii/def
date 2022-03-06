print("welcom")
print("1-sum")
print("2-sub")
print("3-mul")
print("4-div")

op = input()


a = int(input())
b = int(input())


if op == "+":
    result = a + b
elif op == "-":
    result = a - b

print(result)