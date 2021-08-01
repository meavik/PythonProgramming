flag = True
while flag:
    print("Enter the operator: ")
    op = input()
    print("Enter first operand: ")
    op1 = int(input())
    print("Enter second operand: ")
    op2 = int(input())
    if op == '*' and ((op1 == 45 and op2 == 3) or (op2 == 45 and op1 == 3)):
        print(555)
    elif op == '+' and ((op1 == 56 and op2 == 9) or (op2 == 56 and op1 == 9)):
        print(77)
    elif op == '/' and op1 == 56 & op2 == 6:
        print(4)
    else:
        if op == '+':
            print(op1 + op2)
        elif op == '-':
            print(op1 - op2)
        elif op == '*':
            print(op1 * op2)
        elif op == '/':
            print(op1 / op2)
        else:
            print("Operation not supported")
    print("Do you want to continue?(y/n): ")
    x = input()
    if x == 'n':
        flag = False
        break
    else:
        flag = True
        continue
