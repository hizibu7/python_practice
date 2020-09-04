list1 = []

def html_tag(x):
    list1.append(x)
    if len(list1) == 2:
        def trace(func):
            def wrapper():
                print('<{}><{}>'.format(list1[1], list1[2]))
                r = func()
                print(r)
                print('</{}></{}>'.format(list1[1], list1[2]))
            return wrapper



a, b = input().split()

@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'

print(hello())
