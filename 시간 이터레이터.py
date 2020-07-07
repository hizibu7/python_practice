class TimeIterator:
    def __init__(self, start, stop, indexlist = []):
        self.start = start
        self.stop = stop
        self.indexlist = indexlist

    def __iter__(self):
        return self
        
    def __next__(self):
        if self.start < self.stop:
            r = self.start
            if r//3600 >= 24:
                r = r - 3600*24
            time = str(r//3600)
            minute = str((r%3600)//60)
            second = str(r%60)
            self.start += 1
            if int(time) < 10:
                time = '0' + time
            if int(minute) < 10:
                minute = '0' + minute
            if int(second) < 10:
                second ='0' + second
            self.indexlist.append(time+':'+minute+':'+second)
            return time+':'+minute+':'+second
        else:
            raise StopIteration

    def __getitem__(self, index):
        if index < self.stop:
            return self.indexlist[index]
        else:
            raise IndexError

start, stop, index = map(int, input().split())

for i in TimeIterator(start, stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep = '')
            
