grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
st=sorted(list(students))
sr=[sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]) ,
sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]),
sum(grades[4])/len(grades[4])]
dict_=dict()
dict_.update({st[0]:sr[0],st[1]:sr[1],st[2]:sr[2],st[3]:sr[3],st[4]:sr[4]})
print (dict_)
# другой вариант подсчета среднего балла;
sr=list()
a=grades.pop(0)
sr.append(sum(a)/len(a))
a=grades.pop(0)
sr.append(sum(a)/len(a))
a=grades.pop(0)
sr.append(sum(a)/len(a))
a=grades.pop(0)
sr.append(sum(a)/len(a))
a=grades.pop(0)
sr.append(sum(a)/len(a))

