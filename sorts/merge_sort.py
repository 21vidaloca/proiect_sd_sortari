# Merge Sort

def merge(st,mij,dr,v):
    dim1 = mij-st+1
    dim2 = dr-mij

    # merge the sorted arrays A and B
    A=v[st:(mij+1)]
    B=v[(mij+1):(dr+1)]
    i, j = 0, 0
    ind = st
    
    while i < dim1 and j < dim2:
        if(A[i]<=B[j]):
            v[ind]=A[i]
            i += 1
        else:
            v[ind]=B[j]
            j += 1
        ind += 1

    while i < dim1:
        v[ind]=A[i]
        i += 1
        ind += 1

    while(j < dim2):
        v[ind]=B[j]
        j += 1
        ind += 1

def merge_sort_helper(st, dr, v):
    if(st < dr):
        mij=(st+dr)//2
        merge_sort_helper(st,mij,v)
        merge_sort_helper(mij+1,dr,v)

        merge(st,mij,dr,v)

def merge_sort(v):
    merge_sort_helper(0, len(v)-1, v)
