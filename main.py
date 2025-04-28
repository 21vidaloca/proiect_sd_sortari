import sys
import json
import os
sys.setrecursionlimit(10000) 

#import sorting algorithms
from sorts.merge_sort import merge_sort
from sorts.heap_sort import heap_sort
from sorts.basic_sorts import insertion_sort

from sorts.quicksort.quick_sort_3med import quick_sort_3med
from sorts.quicksort.quick_sort_5med import quick_sort_5med
from sorts.quicksort.quick_sort_first import quick_sort_first
from sorts.quicksort.quick_sort_mid import quick_sort_mid

from sorts.timsort.tim_sort_128run import timsort128
from sorts.timsort.tim_sort_512run import timsort512
from sorts.timsort.tim_sort_32run import timsort32

from sorts.shellsort.shell_sort import shell_sort
from sorts.shellsort.shell_sort_hibbard import shell_sort_hibbard
from sorts.shellsort.shell_sort_sedgewick import shell_sort_sedgewick

from sorts.radix_sort import radix_sort_base10
from sorts.radix_sort import radix_sort_base16
from sorts.radix_sort import radix_sort_base16bit

#import tester 
from tester import Tester


sorting_name = {
    'Shell Sort': shell_sort,
    'Shell Sort Hibbard': shell_sort_hibbard,
    'Shell Sort Sedgewick': shell_sort_sedgewick,
    'Tim Sort 32': timsort32,
    'Tim Sort 128': timsort128,
    #'Tim Sort 512': timsort512,
    'Built In Tim Sort': lambda arr: arr.sort(),
    'Merge Sort': merge_sort,
    'Heap Sort': heap_sort,
    #'Quick Sort 3Med': quick_sort_3med,
    #'Quick Sort 5Med': quick_sort_5med,
    #'Quick Sort First': quick_sort_first,
    #'Quick Sort Mid': quick_sort_mid,
    'Radix Sort 10': radix_sort_base10,
    'Radix Sort 16': radix_sort_base16,
    'Radix Sort 16bit': radix_sort_base16bit
}

input_files = []
for filename in os.listdir('data'):
    input_files.append('./data/' + filename)

tester = Tester(*tuple(input_files))

if __name__ == '__main__':
    ans = tester.measure_sorting_algorithms(sorting_name)
    print(ans)

    with open('./results/data.json', 'w') as f:
        json.dump(ans, f, indent=4)

