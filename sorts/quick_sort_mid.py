def MidElement(v, start, end):
    return (start + end - 1) // 2

def Pivot(v, start, end):
    p = MidElement(v, start, end)
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