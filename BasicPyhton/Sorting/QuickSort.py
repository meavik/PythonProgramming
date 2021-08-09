def partitionArray(a,l,h):
    pivot = a[l]
    i = l+1
    j = h
    while i < j:
        while a[i] <= pivot and i<h:
            i += 1
        while a[j] > pivot and j>l :
            j -= 1
        if i < j:
            a[i],a[j] = a[j],a[i]
    if a[j] < pivot:
        a[l], a[j] = a[j], a[l]
    return j


def QuickSort(a,l,h):
    if l<h:
        loc = partitionArray(a,l,h)
        QuickSort(a,l,loc-1)
        QuickSort(a,loc+1,h)


test =[
    [1,2,3,4,5,6],
    [],
    [1],
    [1,2],
    [2,1],
    [6,5,4,3],
    [2,7,1,5,9,3]
]

for ele in test:
    QuickSort(ele,0,len(ele)-1)
    print(f'Sorted list: {ele}')
