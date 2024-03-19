import time

a=0
l=[]
while a<100:
    if len(l)==10:
        #G:\My Drive\e-mote
        w = open('C:\Users\user1\Dropbox\eremote\pod.txt', 'w')
        w.write(str(l))
        l=[]
    else:
        l.append(a)
        a+=1
    time.sleep(0.2)
w.close()