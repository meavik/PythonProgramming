def insertionSort(li,n):
    for i in range(1,n):
        t = li[i]
        j = i-1
        while j>-1 and li[j]>t:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = t


li = []
n = int(input("Enter the number of array elements: "))
for i in range(n):
    x = int(input())
    li.append(x)
print("List elements: ")
for i in li:
    print(i,end=" ")
print("Performing sorting on list")
insertionSort(li,n)
print("After sorting: ")
for i in li:
    print(i,end=" ")
