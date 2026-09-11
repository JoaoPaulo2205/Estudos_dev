def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)

number = 5

print(factorial(7))

