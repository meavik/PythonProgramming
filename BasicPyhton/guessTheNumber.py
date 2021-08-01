realNum = int(input("Enter the real number: "))
guessCount = 5
flag = 0
while guessCount:
    guessNumber = int(input("Guess the number: "))
    if guessNumber>realNum:
        print("Number is smaller.Try again")
        guessCount -=1
        continue
    elif guessNumber<realNum:
        print("Number is larger.Try again")
        guessCount -=1
        continue
    elif guessNumber == realNum:
        print("Congratulations!","\nYou guessed the number in ",guessCount," try")
        flag =1
        break

if flag == 0:
    print("Game Over!")
