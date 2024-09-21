numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
len_num = len(numbers)

primes = []
not_primes = []
item = 0
i = 0

for item in numbers:
        for i in range(2, item):
            if (item % i) == 0:
                not_primes.append(item)
                break
            else:
                primes.append(item)
            break

print(f'Простые числа: {primes}')


print(f'Не простые числа: {not_primes}')
