# Shell Sort Sedgewick

def gap_sort(v, gap):
    for i in range(gap, len(v)):
        curr = v[i]
        j = i
        #insertion in the gap-sorted list
        while j >= gap and v[j - gap] > curr:
            v[j] = v[j - gap]
            j -= gap

        v[j] = curr

def shell_sort_sedgewick(v):
    n = len(v)
    #Sedgewick's sequence (1, 5, 19, 41, ...)
    gaps = []
    k = 0
    while True:
        gap = 9 * (4 ** k - 1) + 1
        if gap >= n:
            break
        gaps.append(gap)
        k += 1
    
    for gap in reversed(gaps):
        gap_sort(v, gap)




