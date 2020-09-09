# 해쉬검색은 파이썬으로 만들지 말자. 따로 포인터가 존재하지 않는다 ㅠㅠ;
from __future__ import annotations
import hashlib

class Node:

    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

class ChainedHash:

    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None]*self.capacity

    def hash_value(self, key):
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity) #라이브러리로 형변환을 해서 해쉬값을 얻음

    def search(self, key):
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next

        return None

    def add(self, key, value):
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False
            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True

    def remove(self, key):
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False

    def dump(self):
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end = '')
            while p is not None:
                print(f' -> {p.key} ({p.value})', end='')
                p = p.next
            print()
