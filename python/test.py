import math


def golden_ratio():
    list = [1, 1]

    for i in range(1000):
        list.append(list[-1] + list[-2])
        print(list[-1] / list[-2])

    print(list)

def eulers_number():
    e = lambda x : math.pow(1 + 1/x, x)
    for i in range(1, 1000):
        print(e(i))

eulers_number()
