first = int(input('Первое число: '))
second = int(input('Второе число: '))
third = int(input('Третье число: '))

if first == second and first == third:
    print('\n'+'Равных чисел: 3')
elif first == second or first == third or second == third:
    print('\n'+'Равных чисел: 2')
else:
    print('\n'+'Равных чисел:', int(not 1))
