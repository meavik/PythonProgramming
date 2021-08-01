def bubbleSort(li, n):
    flag = 0
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                flag = 1
        if flag == 0:
            break


li =[]
n = int(input("Enter the number of elements: "))
print("Enter the elements: ")
for i in range(n):
    x = int(input())
    li.append(x)
print("List elements are: ")
for i in li:
    print(i,end=" ")

print("\nPerforming sorting")
bubbleSort(li,n)
print("After sorting: ")
for i in li:
    print(i,end=" ")
