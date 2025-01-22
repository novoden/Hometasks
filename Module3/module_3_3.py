def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params() # 1 строка True
print_params(b=25) # 1 25 True
print_params(c = [1,2,3]) # 1 строка [1, 2, 3]

values_list = [11.22, False, 'Text']
print_params(values_list) # (11.22, False, 'Text') строка True
print_params(*values_list) # 11.22 False Text

values_duct = {'a': 20, 'b': 21, 'c': 22}
print_params(values_duct) # {'a': 20, 'b': 21, 'c': 22} строка True
print_params(**values_duct) # 20 21 22

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42) # 54.32 Строка 42

values_list = [11.22]
values_duct = {'c' : 3}
values_list_2 = ['Строка']
print_params(*values_list, *values_list_2, **values_duct) # 11.22 Строка 3
