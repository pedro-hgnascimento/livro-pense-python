from math import sqrt

def compare(x, y):
    if(x > y):
        return 1
    elif(x == y):
        return 0
    else:
        return -1

def hypotenuse(a, b):
    return sqrt((a**2 + b**2))

def is_between(x, y, z):
    return (x <= y) and (y <= z)


# print(compare(1, 2))
# print(compare(2, 2))
# print(compare(2, 1))

# print(hypotenuse(3, 4))

# print(is_between(1, 2, 3))
# print(is_between(1, 3, 2))
