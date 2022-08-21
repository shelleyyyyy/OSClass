import threading
import time

from numpy import random

# shared memory
s = 0


class client(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global s

        while True:
            print("CLIENT listening... ")
            if s == -1:
                ran = random.randint(10)
                s = ran
                print("client set: ", s)
            elif s == 7:
                break
            else:
                time.sleep(1)


class server(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global s
        while True:
            print("SERVER listening... ")
            if s != -1:
                if s == 7:
                    print("7777777777777777")
                    break
                else:
                    s = -1
                    print("server set: ", s)
            else:
                time.sleep(1)


t1 = client()
t2 = server()

t1.start()
t2.start()
