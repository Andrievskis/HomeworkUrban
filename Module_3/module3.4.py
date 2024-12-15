def print_params(a=1, b="'строка'", c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ['a', 5, False]
values_dict = {'a': 9, 'b': 8, 'c': 7}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ["'november'", 34567]
print_params(*values_list_2, 42)



