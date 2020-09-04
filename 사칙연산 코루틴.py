def calc():
    total = 0
    while True:
        x = (yield total)

        x = x.split(' ')
        a = int(x[0])
        b = x[1]
        c = int(x[2])
        if  b == '+':
            total = a+c
        elif b == '-':
            total = a-c
        elif b == '*':
            total = a*c
        elif b == '/':
            total = a/c      
            

expressions = input().split(', ')

c = calc()
next(c)

for e in expressions:
    print(c.send(e))

c.close()

# 입력형식
# ex) 3 * 2, 10 / 2 (한칸씩 띄워야함)
