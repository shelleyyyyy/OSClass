import threading
import time
from numpy import random


if __name__ == '__main__':

    arr = []

    for i in range(10):
        arr.append(random.randint(100))

    # print(arr)

    class avg(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)

        def run(self):
            sum = 0
            for i in arr:
                sum = sum + i

            avg = sum/len(arr)

            # print("The average is: ", avg)

            try:
                avgF = open("avg.txt", "x")
            except:
                avgF = open("avg.txt", "w")

            avgF.write(str(avg))


    class min(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)

        def run(self):
            min = arr[0]
            for x in arr:
                if x < min:
                    min = x
                else:
                    continue

            # print("The min is: ", min)

            try:
                minF = open("min.txt", "x")
            except:
                minF = open("min.txt", "w")

            minF.write(str(min))


    class max(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)

        def run(self):
            max = arr[0]
            for y in arr:
                if y > max:
                    max = y
                else:
                    continue

            # print("The max is: ", max)

            try:
                maxF = open("max.txt", "x")
            except:
                maxF = open("max.txt", "w")

            maxF.write(str(max))

    t1 = avg()
    t2 = min()
    t3 = max()

    t1.start()
    t2.start()
    t3.start()

    time.sleep(1)

    read_max = open("max.txt", "r")
    read_min = open("min.txt", "r")
    read_avg = open("avg.txt", "r")

    print("max: ", read_max.readline())
    print("min: ", read_min.readline())
    print("avg: ", read_avg.readline())
