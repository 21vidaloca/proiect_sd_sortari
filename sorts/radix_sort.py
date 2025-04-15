import math

def RadixSort(v, k, b):
    if b ** k > max(v):
        return

    L = [[] for _ in range(b)]

    for x in v:
        L[(x // (b ** k)) % b].append(x)

    i = 0
    for l in L:
        for x in l:
            v[i] = x
            i += 1

    RadixSort(v, k + 1, b)