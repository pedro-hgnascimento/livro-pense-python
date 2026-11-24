# Exercício 6.2
def ack(m, n):
    if(m == 0):
        return n + 1
    elif(m > 0 and n == 0):
        return ack(m - 1, 1)
    elif(m > 0 and n > 0):
        return ack(m - 1, ack(m, n - 1))

# print(ack(3, 4))

# Exercício 6.3
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif first(word) != last(word):
        return False
    else:
        return is_palindrome(middle(word))

# print(is_palindrome("radar"))
# print(is_palindrome("python"))
# print(is_palindrome("level"))

def is_power(a, b):
    if a == 1:
        return True
    elif a < b or b == 0:
        return False
    else:
        return is_power(a / b, b)

# print(is_power(27, 3))  # True
# print(is_power(16, 2))  # True
# print(is_power(20, 2))  # False

def gdc(a, b):
    if(b == 0):
        return a
    else:   
        return gdc(b, a % b)

print(gdc(48, 18))  # 6
print(gdc(56, 98))  # 14
print(gdc(101, 10))  # 1