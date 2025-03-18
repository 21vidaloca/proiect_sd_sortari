v=[7,8,5643,123,32,7.6,7.59,13,5555,99898,3,5,76]
from merge_sort import merge_sort
print(len(v))
merge_sort(0,len(v)-1,v)
print(v)