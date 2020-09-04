def prime_number_generator(start, stop):
    primelist = []
    while start < stop:
        not_primelist = []
        for i in range(2,start):
            if start%i == 0:
                not_primelist.append(i)
        if not_primelist == []:
            primelist.append(start)
        start += 1
    yield from primelist
                

start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
for i in g:
    print(i, end = ' ')
