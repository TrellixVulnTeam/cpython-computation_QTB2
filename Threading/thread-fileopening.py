import threading
import sys
import time

l=0
length=[]
def File_Opener(keys,l):
    for lines in keys:
        l = l + len(lines)-1
    length.append(l)
    l=0
if __name__ == "__main__":
    start=time.time()
    f=open(sys.argv[1],"r")
    print %sys.argv[1]
    Threads=[]
    keys=[]
    for i in range(100):
        try:
            for j in range(200000):
                keys.append(f.next())
        except:
            pass
        t = threading.Thread(target=File_Opener,args=(keys,l))
        t.start()
        keys=[]
        print %i
        Threads.append(t)
    for thread in Threads:
        thread.join()
print (sum(length))
print (time.time()-start)
print('completed')