def print_params(a=1, b='строка', c=True):
    print("a=", a, "  b=", b, "  c=", c)


print('1.Функция с параметрами по умолчанию:')
print_params()
print_params(4, {5, 78, 87})
print_params(a="asdfg")
print_params(b=25)
print_params(c=[1, 2, 3])
print('2.Распаковка параметров:')
values_list = [125, "abcde", (7, 89)]
values_dict = {'a': "111111", "b": "22", 'c': "333"}
print_params(*values_list)
print_params(**values_dict)
print("3.Распаковка + отдельные параметры:")
values_list_2=[True,(1,2,3)]
print_params( *values_list_2, 42)
