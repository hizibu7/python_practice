counter = 0
ptr = 0
num = 0
prime = [None]*500

prime[ptr] = 2
ptr += 1
prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):
    i = 1
    while prime[i] * prime[i] <= n:  
        counter += 2
        if n%prime[i] == 0:
            num += 1
        i += 1
    if num == 0:
        prime[ptr] = n
        ptr += 1
    num = 0
            
print(counter)
for i in prime:
    if i != None:
        print(i, end = ' ') 
