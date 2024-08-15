def calculate_structure_sum(*ds):
    summ = 0
    for a in ds:
        if isinstance(a, (tuple, set, list)):
            summ = summ + calculate_structure_sum(*a)
        elif isinstance(a, int):
            summ += a
        elif isinstance(a, str):
            summ += len(a)
        elif isinstance(a, dict):
            a = list(a.items())
            summ = summ + calculate_structure_sum(*a)
    return summ

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
