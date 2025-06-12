import random
computer = random.randint(1, 3)
player = int(input("Select a number, 1 - 3 to choose rock, paper, or scissors!"))
print(f'1) ✊')
print(f'2) ✋')
print(f'3) ✌️')

if player == 1:
    choice = '✊'
elif player == 2:
    choice = '✋'
elif player == 3:
    choice = '✌️'
else:
    print ("Invalid Choice. Must be 1 - 3 for a valid selection.")
    exit()

if computer == 1:
    comp_choice = '✊'
elif computer == 2:
    comp_choice = '✋'
elif computer == 3:
    comp_choice = '✌️'

if computer == player:
    winner = "It's a tie!"
elif computer == 2 and player == 1:
    winner = "The computer won!"
elif computer == 3 and player == 1:
    winner = "The player won!"
elif computer == 1 and player == 2:
    winner = "The player won!"
elif computer == 1 and player == 3:
    winner = "The computer won!"
elif computer == 2 and player == 3:
    winner = "The player won!"
elif computer == 3 and player == 2:
    winner = "The computer won!"
        

print('You chose: ' + choice)
print('CPU chose: ' + comp_choice)
print(winner)