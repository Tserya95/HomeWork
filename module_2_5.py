
def get_matrix(n, m, value):
    matrix = [] # Список по задаче
    ab = []  # Создал дополнительную пустой список
    if value > 0:
        for i in range(m):  # Добавляем в дополнительный список
            ab.append(value)     # число value в кол-ве m

        for i in range(n):  # При каждом проводке Добавляем в список matrix
            matrix.insert(n, ab)    # значения списка ab
        return matrix
    else:
        return matrix




result1 = get_matrix(2, 2, 0)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)



