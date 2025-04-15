
def MedianOfFive(v, start, end):
    end -= 1
    mid = (start + end) // 2
    smallMid = (start + mid) // 2
    bigMid = (mid + end) // 2

    median = max([(v[x], x) for x in (start, smallMid, mid, bigMid, end)])[1]

    if median == start:
        return max([(v[x], x) for x in (smallMid, mid, bigMid, end)])[1]

    if median == smallMid:
        return max([(v[x], x) for x in (start, mid, bigMid, end)])[1]

    if median == mid:
        return max([(v[x], x) for x in (start, smallMid, bigMid, end)])[1]

    if median == bigMid:
        return max([(v[x], x) for x in (start, smallMid, mid, end)])[1]

    if median == end:
        return max([(v[x], x) for x in (start, smallMid, mid, bigMid)])[1]
    
def Pivot(v, start, end):
    p = MedianOfFive(v, start, end)
    v[start], v[p] = v[p], v[start]

    left = start
    right = end - 1

    stepLeft = 0
    stepRight = 1

    while left < right:
        if v[left] > v[right]:
            v[left], v[right] = v[right], v[left]
            stepLeft, stepRight = stepRight, stepLeft

        left += stepLeft
        right -= stepRight

    if stepLeft == 0:
        return left
    return right

def QuickSort(v, start, end):
    if start >= end:
        return
    
    p = Pivot(v, start, end)
    QuickSort(v, start, p)
    QuickSort(v, p + 1, end)