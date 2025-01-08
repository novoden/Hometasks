first = int(input('Первое число: '))
second = int(input('Второе число: '))
third = int(input('Третье число: '))

if first == second and first == third:
    print('\n'+'Три числа равны')
elif first == second or first == third or second == third:
    print('\n'+'Два числа равны')
else:
    print (int(not 1), 'Равных чисел нет!')
