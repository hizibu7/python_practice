def numlist(a,b):
    list1 = list(range(a, b+1))
    return list1

def prime(c):
    if c == 1:
        return 'False'
    else:
        for j in range(2, c):
            if c%j == 0:
                return 'False'
                break
        return 'True'

sum = 0
a = int(input())
b = int(input())
numlist(a,b)
for k in numlist(a,b):
    if prime(k) == 'True':
        sum += k

print(sum)


