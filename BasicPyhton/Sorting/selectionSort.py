def selectionSort(li):
    """This function applies Selection sort technique on data for performing sorting"""
    n = len(li)
    for i in range(0, n - 1):
        k = i
        for j in range(i, n):
            if li[j] < li[k]:
                k = j
        if k != i:
            temp = li[i]
            li[i] = li[k]
            li[k] = temp


def printList(li):
    """"This function prints the list"""
    for i in li:
        print(i,end=" ")


# print(selectionSort.__doc__)


li = []
n = int(input("Enter the number of list elements: "))
print("Enter the list elements")
for i in range(0, n):
    x = int(input())
    li.append(x)
print("\nList elements:", end=" ")
printList(li)
selectionSort(li)
print("\nAfter sorting:", end=" ")
printList(li)
