import random
symbols = ['🍒',' 🍇', '🍉', '7️⃣']

def play():
  answer = 'Y'
  while answer == 'Y' or answer == 'y':
    results = random.choices(symbols, k=3)
    print(f'{results[0]}  |  {results[1]}  |  {results[2]}')
    if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
      print("Jackpot! 💰")
    else:
      print('Thanks for playing!')
    answer = (input('Would you like to play again? '))

play()