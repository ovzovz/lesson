immutable_var=(1, 2, 'a', 'b',[5,6,7])
print("Immutable tuple: ",immutable_var)
#immutable_var[0]=-111  #вызывает ошибку, т.к. кортеж - неизменяемый тип данных
# TypeError: 'tuple' object does not support item assignment
# Но если элементом кортежа является список, то возможно изменение элементов даного списка;
immutable_var[4][0]=-111
print("Immutable tuple: ",immutable_var)

mutable_list =[1, 2, 'a', 'b', 'initial']
print ('Mutable list:', mutable_list)
mutable_list[4]='Modified'
print ('Mutable list:', mutable_list)
