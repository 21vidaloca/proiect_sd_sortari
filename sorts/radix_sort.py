import math

def RadixSort(v, k, b):
    """
    Recursive Radix Sort function that sorts the array `v` in-place
    for a given base `b` and digit position `k`.
    """
    if b ** k > max(v):
        return

    # Create `b` buckets (base number of buckets)
    L = [[] for _ in range(b)]

    # Place each element in the corresponding bucket
    for x in v:
        L[(x // (b ** k)) % b].append(x)

    # Rebuild the list by emptying all the buckets in order
    i = 0
    for l in L:
        for x in l:
            v[i] = x
            i += 1

    # Recursively call RadixSort on the next digit position
    RadixSort(v, k + 1, b)


def radix_sort_base16(v):
    RadixSort(v, 0, 16)

def radix_sort_base10(v):
    RadixSort(v, 0, 10)

def radix_sort_base16bit(v):
    RadixSort(v, 0, 1<<16)