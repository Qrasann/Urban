def print_params(a=1, b='string', c=True):
    print(f"Parameter a: {a}")
    print(f"Parameter b: {b}")
    print(f"Parameter c: {c}")
    print(' ')

print_params()
print_params(25)
print_params(25, [1, 2, 3])


values_list = [2018,'I love minecraft', False ]
values_dict = {'a': 52, 'b': 'Я люблю майкнрафт', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Майкнрафт это моя жизнь', 2024]
print_params(*values_list_2, 42)

