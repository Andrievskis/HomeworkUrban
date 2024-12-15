immutable_var = 1, 2, 3, 'a', 's', 'R', False
print(immutable_var)
#immutable_var[0] = 34567
#print(immutable_var) #т.к. содержит разные типы данных

mutable_list = ([6, 9], 7)
print(mutable_list)
mutable_list[0][0] = 'LOST'
print(mutable_list)

mutable_list = ['1', '2', '3', 'U']
mutable_list[2] = 'cat'
print(mutable_list)


