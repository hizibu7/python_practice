def isPrime(num, L):
    
    for i in range(2, num):
        if num%i == 0:
            L.append(i)
    if L == []:
        return 'True'
    else:
        L.append(1)
        L.append(num)
        print(L)
        return False
        
        
    
ans = isPrime(23967169,[]) 
print(ans)      
