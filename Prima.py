import time
import threading

lista=[]
a=0
val=0

print(lista)

def everyfour():
        print(a)
        if (a < 10):
                w = open('G:\My Drive\e-mote\Val.txt','r')
                val = w.read()
                time.sleep(4)
                a += 1
                w.close()

print(val)

every4seconds = threading.Thread(everyfour())
every4seconds.start()