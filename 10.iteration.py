primes = [2, 3, 5, 7]
print(type(primes))
iterator = iter(primes)
print(type(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
except StopIteration:
    print('No more values')

