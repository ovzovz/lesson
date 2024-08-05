numbers=list(range(1,16))
print (numbers)
primes=[]
not_primes=[]
for i in numbers:
    is_prime=1
    for j in range (2,i):
        if i%j==0:
            is_prime=0
            break
    if is_prime == 0:
        not_primes.append(i)
    else:
        primes.append(i)
print ('primes: ',primes)
print ('not_primes: ',not_primes)



