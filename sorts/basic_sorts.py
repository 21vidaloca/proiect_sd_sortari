# Basic Sorts

def insertion_sort(v):
    for i in range(1, len(v)):
        j = i
        while j > 0 and v[j-1] > v[j]:
            v[j-1], v[j] = v[j], v[j-1]
            j -= 1
    