def is_prime(func):
   def wrapper(*a):
       res = func(*a)
       if len([x for x in range(2, res) if res % x == 0]) == 0:
           print ('Простое')
       else:
           print('Составное')
       return res
   return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
