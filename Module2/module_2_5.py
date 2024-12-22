def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

n = int(input('Строк (n):'))
m = int(input('Столбцов (m):'))
value = input('Значение (value): ')
matrix = get_matrix(n, m, value)

if n <= 0:
    print ('')
elif m <=0:
    print('')
