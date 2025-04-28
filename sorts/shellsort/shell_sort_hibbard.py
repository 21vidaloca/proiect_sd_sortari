# Shell Sort Hibbard

def gap_sort(v, gap):
    for i in range(gap, len(v)):
        curr = v[i]
        j = i
        #insertion in the gap-sorted list
        while j >= gap and v[j - gap] > curr:
            v[j] = v[j - gap]
            j -= gap

        v[j] = curr


def shell_sort_hibbard(v):
    n = len(v)
    gap = 1
    # 2^k - 1, de la k = 1
    while gap < n // 3:
        gap = 2 * gap + 1
    
    while gap > 0:
        gap_sort(v, gap)
        gap = (gap - 1) // 2



