def fact(x):
    result = 1
    i = 1
    while i <= x:
        result *= i
        i += 1
    return result

x = int(input())
print(fact(x))
