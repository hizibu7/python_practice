counter = 0
ptr = 0
num = 0
prime = [None]*500

prime[ptr] = 2
ptr += 1

for n in range(3, 1001, 2):
    for i in range(1, ptr): #어차피 홀수만 따지므로 2로 나눌필요 없어서 i=1부터
        counter += 1
        if n%prime[i] == 0:
            num += 1
    if num == 0:
        prime[ptr] = n
        ptr += 1
    num = 0
            
print(counter)
for i in prime:
    if i != None:
        print(i, end = ' ')
        
