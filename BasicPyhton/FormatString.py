print("Hello, user!\nPlease enter your information")
print("Name: ")
x = input()
print("Age: ")
y = int(input())
print("User id: ")
z = input()
info = "Hello, {}!\nAge: {}\nID: {}"
print(info.format(x,y,z))
