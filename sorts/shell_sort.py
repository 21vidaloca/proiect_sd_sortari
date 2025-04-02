# Shell Sort

def gap_sort(v, gap):
    for i in range(gap, len(v)):
        curr = v[i]
        j = i

        #insertion in the gap-sorted list
        while j >= gap and v[j - gap] > curr:
            v[j] = v[j - gap]
            j -= gap

        v[j] = curr


def shell_sort(v):
    n = len(v)
    gap = n // 2

    while gap > 0:
        gap_sort(v, gap)
        gap //= 2



