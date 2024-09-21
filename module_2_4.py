numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []
is_prime = True
for item in numbers:
    if item == 1:
        continue
    is_prime = True
    for i in range(2, item):
        if item % i == 0:
            is_prime = False
            break
    if is_prime == False:
        not_primes.append(item)
    else:
        primes.append(item)

print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')