my_list=[42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
new_list=[]
i=0
while i<len(my_list):
    if my_list[i]>0:
        new_list.append(my_list[i])
    elif my_list[i]<0:
        break
    i+=1

print(my_list)
print (new_list)
