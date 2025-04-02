# Heap Sort

def functie(v,n,ind):
    poz = ind
    st=2*ind + 1
    dr=2*ind + 2

    if(st<n and v[st]>v[poz]):
        poz=st
    
    if(dr<n and v[dr]>v[poz]):
        poz=dr
    
    if(poz != ind):
        # swap elements at ind and pos
        v[ind], v[poz] = v[poz], v[ind]
        functie(v, n, poz)

def heap_sort(v):
    n = len(v)
    for i in range(n//2 - 1, -1, -1):
        functie(v, n, i)

    for i in range(n-1, 0, -1):
        #swap elements at 0 and i
        v[0], v[i] = v[i], v[0]
        functie(v, i, 0)