a = [1, 2, 3]
try:
    print("Second element = ", a[1])
    print("Fourth element = ", a[3])
except:
    print("An error occurred")
print()
b = [3, 2, 1]
try:
    a == b
except:
    print("They are not equal")
else:
    print("Both Equal")

print()

try:
    k = 5 / 0
    print(k)
except ZeroDivisionError:
    print("Can't divide by zero")