import random


def bubble(a):
    while True:
        for k in range(len(a)):
            for i in range(len(a) - 1, 0, -1):
                if a[i - 1] > a[i]:
                    a[i - 1], a[i] = a[i], a[i - 1]
        break
    return a


def insertion(a):
    for i in range(len(a)):
        k = i - 1
        b = a[i]
        while b < a[k] and k >= 0:
            a[k + 1] = a[k]
            k -= 1
        a[k + 1] = b
    return a


def quicksort(a):
    if len(a) > 1:
        x = a[random.randint(0, len(a) - 1)]
        smaller = [i for i in a if i < x]
        bigger = [i for i in a if i > x]
        equal = [i for i in a if i == x]
        a = quicksort(smaller) + equal + quicksort(bigger)
    return a
