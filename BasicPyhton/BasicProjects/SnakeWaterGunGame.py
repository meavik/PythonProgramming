import random
options =['s','w','g']
choice = 0
pc_point = 0
human_point = 0
while choice < 10:
    error_flag = False
    print(f'Round {choice+1}')
    pc = random.choice(options)
    human = input('Enter your choice(s/w/g): ')
    human.lower()
    try:
        if human  in ('s','w','g'):
            if pc == human:
                pc_point += 0
                human_point += 0
                print("Draw!")
                print(f'Nobody wins this round!\nComputer\'s point: {pc_point}\nYour point: {human_point}')
            elif (pc == 's' and human == 'w') or (pc == 'w' and human == 'g') or (pc == 'g' and human == 's'):
                pc_point += 1
                print(f'Computer win!\nComputer\'s point: {pc_point}\nYour point: {human_point}')
            elif (pc == 'w' and human == 's') or (pc == 'g' and human == 'w') or (pc == 's' and human == 'g'):
                human_point += 1
                print(f'You win!\nComputer point: {pc_point}\nYour point: {human_point}')
        else:
            print("Invalid input")
            error_flag = True
    finally:
        if error_flag is False:
            choice += 1
print("Game Over!")
if pc_point > human_point:
    print("You Lost!")
    print(f'Computer got {pc_point} points\nYou got {human_point} points\n')
else:
    print("You Win!")
    print(f'Computer got {pc_point} points\nYou got {human_point} points\n')
