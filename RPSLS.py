# Checkpoint Project: Rock Paper Scissors
import random

player = ""
computer = ""
pmote = ""
cmote = ""

print('================================')
print('Rock Paper Scissors Lizard Spock')
print('================================')
print('1) ✊')
print('2) ✋')
print('3) ✌️')
print('4) 🦎')
print('5) 🖖')

player = int(input('Pick a number: '))
computer = random.randint(1, 5)
print('\n')

if player == 1:
  pmote = '✊'
elif player == 2:
  pmote = '✋'
elif player == 3:
  pmote = '✌️'
elif player == 4:
  pmote = '🦎'
else:
  pmote = '🖖'

if computer == 1:
  cmote = '✊'
elif computer == 2:
  cmote = '✋'
elif computer == 3:
  cmote = '✌️'
elif computer == 4:
  cmote = '🦎'
else:
  cmote = '🖖'

print(f'You chose: {pmote}')
print(f'CPU chose: {cmote}')
print('\n')

if player == computer:
  print('Tie! Run it again!')
elif player == 1:
  if computer == 3 or computer == 4:
    print('The player won!')
  else:
    print('The player LAWST!')
elif player == 2:
  if computer == 1 or computer == 5:
    print('The player won!')
  else:
    print('The player LAWST!')
elif player == 3:
  if computer == 2 or computer == 4:
    print('The player won!')
  else:
    print('The player LAWST!')
elif player == 4:
  if computer == 2 or computer == 5:
    print('The player won!')
  else:
    print('The player LAWST!')
else:
  if computer == 1 or computer == 3:
    print('The player won!')
  else:
    print('The player LAWST!')
