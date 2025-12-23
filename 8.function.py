def search(f):
    x = 0
    while not f(x):
        x += 1
    return x
    
def square(x):
    return x * x

def inverse(f):
    return lambda y: search(lambda x: f(x) == y)

"""
>>> sqrt = inverse(square)
>>> square(16)
256
>>> sqrt(256)
16
"""

def horse(mask):
    horse = mask
    def mask(horse):
        return horse
    return horse(mask)

mask = lambda horse: horse(2)

print(horse(mask))

def remove(n, digit):
    """Return all digits of non-negative N
    that are not DIGIT, for some
    non-negative DIGIT less than 10.

    >>> remove(231, 3)
    21
    >>> remove(243132, 2)
    4313
    """
    kept, digits = 0, 0
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept = kept + last * 10 ** digits
            digits = digits + 1
    return kept

def split(x):
    return x // 10, x % 10
def sum_digits(n):
    if n < 10:
        return n
    else:
        abl, last = split(n)
    return sum_digits(abl) + last

print(sum_digits(2025))

def fact_1(n):
    f = 1
    while n > 1:
        f, n = f * n, n - 1
    return f

def fact_2(n):
    if n == 0:
        return 1
    else:
        return n * fact_2(n-1)
    
print(fact_1(5))
print(fact_2(5))

"""Luhn Algorithm for checking credit card numbers"""
def luhn(n):
    if n < 10:
        return n
    else:
        abl, last = split(n)
        return sum_digits(abl) + last
    
def luhn_2(n):
    abl, last = split(n)
    luhn_digits = sum_digits(2 * last)
    if n <10:
        return n
    else:
        return luhn(abl) + luhn_digits
    
def even(n):
    if n == 0:
        return True
    else:
        return odd(n-1)
    
def odd(n):
    if n == 0:
        return False
    else:
        return even(n-1)

print(odd(789))

def cascade(n):
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)

def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n, m-1) + count_partitions(n-m, m)
    
print(count_partitions(18, 9))

from math import gcd

def rational(n, d):
    g = gcd(n, d)
    return [n//g, d//g]

def numer(x):
    return x[0]

def denom(x):
    return x[1]

def add_rational(x, y):
    a, b = numer(x) * denom(y) + numer(y) * denom(x), denom(x) * denom(y)
    return rational(a, b)

half = rational(1, 2)
third = rational(1, 3)

print(add_rational(half, third))
print(add_rational(third, third))

numbers_1 = [1, 2, 3, 4, 5]
print(len(numbers_1))
numbers_2 = [6, 7, 8]
print(numbers_1 + numbers_2 * 2)

lists = [[11, 12], [13, 14, 15]]
print(lists[1][2])

s = [2, 2, 3, 4, 2, 1, 2, 5, 5, 6, 9]
def count_w(s, n):
    t, i = 0, 0
    while i < len(s):
        if s[i] == n:
            t += 1
        i += 1
    return t

def count_f(s, n):
    t = 0
    for i in s:
        if i == n:
            t += 1
    return t

print(count_w(s, 2))
print(count_f(s, 2))

pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
def cheek(list):
    t = 0
    for x, y in list:
        if x == y:
            t += 1
    return t
print(cheek(pairs))

odd_list = list(range(2, 9, 2))
print(odd_list)

even_list = [x-1 for x in odd_list]
print(even_list)

def division(n):
    return [1] + [x for x in range(2, n) if n % x == 0]
print(division(12))
perfect_nums = [x for x in range(1, 10001) if sum(division(x)) == x]
print(perfect_nums)

def width(area, length):
    assert area % length == 0
    return area // length
def perimeter(width, length):
    return 2 * (width + length)
def min_perimeter(x):
    length = division(x)
    perimeters = [perimeter(width(x, l), l) for l in length]
    return min(perimeters)

area = 120
print(min_perimeter(area))