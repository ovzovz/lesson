def f(d):
    s=0
    print (d)
    print(s)
    if type(d) in (list,dict,tuple):
        for i in d:
           if type(i)==int :
               s+=i
           elif type(i)==str:
               s+=len(i)
           else:
               return s + f(i)


#data_structure \
ds= [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]
result=f(ds)
    #result = calculate_structure_sum(data_structure)
print(result)

