v=[7,8,5643,123, 123, 32,32,7.6,7.59,13,5555,99898,3,5,76]
n=len(v)
maxx=max(v)
from merge_sort import merge_sort
from heap_sort import heapsort
# print(len(v))
# merge_sort(0,len(v)-1,v)
heapsort(v)
print(v)