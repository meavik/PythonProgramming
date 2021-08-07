def fac(n):
    if n == 0 | n == 1:
        return 1
    else:
        return n * fac(n-1)


num = int(input("Enter a number: "))
print(fac(num))
