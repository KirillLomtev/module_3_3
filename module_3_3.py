values_list = [11, 'строчка', 4,]
values_list_2 = [11, 'слово']
values_dict = {'a': 7, 'b': 8, 'c': 9}
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    return
print_params()
print_params(b = 25) # вызов работает
print_params(c = [1, 2, 3]) # вызов работает
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list)
print_params(*values_list_2, 42) # вызов работает