def interclaseaza(st,mij,dr,v):
    dim1=mij-st+1
    dim2=dr-mij
    # interclasam A cu B
    A=v[st:(mij+1)]
    B=v[(mij+1):(dr+1)]
    i=0
    j=0
    ind=st
    while i<dim1 and j<dim2:
        if(A[i]<=B[j]):
            v[ind]=A[i]
            i=i+1
        else:
            v[ind]=B[j]
            j=j+1
        ind=ind+1
    while i<dim1:
        v[ind]=A[i]
        i=i+1
        ind=ind+1
    while(j<dim2):
        v[ind]=B[j]
        j=j+1
        ind=ind+1
def merge_sort(st, dr,v):
    if(st<dr):
        mij=(st+dr)//2
        merge_sort(st,mij,v)
        merge_sort(mij+1,dr,v)
        interclaseaza(st,mij,dr,v)
