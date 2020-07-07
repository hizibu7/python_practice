n = int(input())
m = list(input().split(' '))
m = list(map(int, m))
a = list(0 for i in range(23))

for j in range(1, 24):
    b = m.count(j)
    a[j-1] = b

print(a)
