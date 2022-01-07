# Time / performance checking

from time import time

def add (x, y=50):
    return x + y

before = time()
print(before)
print('add(200)', add(50))
after = time()
print(after)
print('add(20, 30)', add(50))
print('add("a", "b")', add("a", "b"))


