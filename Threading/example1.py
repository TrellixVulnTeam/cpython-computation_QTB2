import threading

def f(a , d, y):
    print(a + d + y)
    pass

t = threading.Thread(target=f, args=(10,45), kwargs={'y': 30})
t.start()