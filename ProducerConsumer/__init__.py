import threading
import time
from numpy import random

p = 0
c = 0


class producer(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        # import numpy
        counter = 0
        while True:
            try:
                f = open("com.txt", "x")
            except:
                f = open("com.txt", "w")

            ran1 = random.randint(1, 10)
            ran2 = random.randint(1, 10)

            ranOperation = random.randint(3)
            operation = ""
            if ranOperation == 1:
                operation = "/"
            elif ranOperation == 2:
                operation = "*"
            elif ranOperation == 3:
                operation = "+"
            else:
                operation = "-"

            ran1 = str(ran1)
            ran2 = str(ran2)

            f.write(ran1)
            f.write(ran2)
            f.write(operation)

            # time.sleep(1)
            # print(operation)

            ran1 = int(ran1)
            ran2 = int(ran2)

            global p
            if operation == "*":
                p = ran1 * ran2
            elif operation == "-":
                p = ran1 - ran2
            elif operation == "/":
                p = ran1 / ran2
            else:
                p = ran1 + ran2

            print(c, "from producers ", counter)
            # time.sleep(2)
            counter = counter + 1
            # break


class consumer(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        counter = 0
        while True:
            f = open("com.txt", "r")

            str = f.read()

            if len(str) < 2:
                continue

            # print(str)

            ran1 = str[0]
            ran2 = str[1]
            operation = str[2]

            ran1 = int(ran1)
            ran2 = int(ran2)

            global c
            if operation == "*":
                c = ran1 * ran2
            elif operation == "-":
                c = ran1 - ran2
            elif operation == "/":
                c = ran1 / ran2
            else:
                c = ran1 + ran2
            # f.close()
            print(c, "from consumer ", counter)
            # f.open("com.txt", "w")
            # f.truncate()
            # time.sleep(2)
            # print(c)
            # break
            counter = counter + 1



t1 = producer(1, "", 1)
t2 = consumer(2, "", 1)

t1.start()
t2.start()
