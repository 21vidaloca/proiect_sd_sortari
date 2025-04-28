
# def MedianOfFive(v, start, end):
#     end -= 1
#     mid = (start + end) // 2
#     smallMid = (start + mid) // 2
#     bigMid = (mid + end) // 2

#     median = max([(v[x], x) for x in (start, smallMid, mid, bigMid, end)])[1]

#     if median == start:
#         return max([(v[x], x) for x in (smallMid, mid, bigMid, end)])[1]

#     if median == smallMid:
#         return max([(v[x], x) for x in (start, mid, bigMid, end)])[1]

#     if median == mid:
#         return max([(v[x], x) for x in (start, smallMid, bigMid, end)])[1]

#     if median == bigMid:
#         return max([(v[x], x) for x in (start, smallMid, mid, end)])[1]

#     if median == end:
#         return max([(v[x], x) for x in (start, smallMid, mid, bigMid)])[1]
    
# def Pivot(v, start, end):
#     p = MedianOfFive(v, start, end)
#     v[start], v[p] = v[p], v[start]

#     left = start
#     right = end - 1

#     stepLeft = 0
#     stepRight = 1

#     while left < right:
#         if v[left] > v[right]:
#             v[left], v[right] = v[right], v[left]
#             stepLeft, stepRight = stepRight, stepLeft

#         left += stepLeft
#         right -= stepRight

#     if stepLeft == 0:
#         return left
#     return right

# def QuickSort(v, start, end):
#     if start >= end:
#         return
    
#     p = Pivot(v, start, end)
#     QuickSort(v, start, p)
#     QuickSort(v, p + 1, end)

# def quick_sort_5med(v):
#     QuickSort(v, 0, len(v))


def MedianOfFive(v, start, end):
    mid = (start + end) // 2
    smallMid = (start + mid) // 2
    bigMid = (mid + end) // 2


    values = [(v[start], start), (v[smallMid], smallMid), (v[mid], mid), (v[bigMid], bigMid), (v[end], end)]
    values.sort()
    

    return values[2][1]

def Pivot(v, start, end):
    p = MedianOfFive(v, start, end)
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

def quick_sort_5med(v):
    QuickSort(v, 0, len(v) - 1)
