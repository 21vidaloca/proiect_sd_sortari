def MidElement(v, start, end):
    return (start + end) // 2

def Pivot(v, start, end):
    p = MidElement(v, start, end)
    v[start], v[p] = v[p], v[start] 

    left = start + 1
    right = end

    while True:

        while left <= right and v[left] <= v[start]:
            left += 1

        while left <= right and v[right] >= v[start]:
            right -= 1
        
        if left <= right:
            v[left], v[right] = v[right], v[left]
        else:
            break

    v[start], v[right] = v[right], v[start]
    return right

def QuickSort(v, start, end):
    if start < end:
        p = Pivot(v, start, end)
        QuickSort(v, start, p - 1)
        QuickSort(v, p + 1, end)

def quick_sort_mid(v):
    QuickSort(v, 0, len(v) - 1)