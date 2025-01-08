import random

def pasw(k):
    calc = ''
    for i in range(1, k):
        for j in range(i +1, k +1):
            if k % (i +j) == 0:
                calc += str(i) + str(j)
    return f'{k} - {calc}'

initd = range(3, 20)
k = (random.choice(initd))
result = pasw(k)
print(result)
