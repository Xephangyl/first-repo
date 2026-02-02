#Welcome to the Good Burger!

menu = ['🍔 Cheeseburger', 
        '🍟 Fries', 
        '🥤 Soda', 
        '🍦 Ice Cream', 
        '🍪 Cookie']

def get_item(m):
  return menu[m - 1]

def welcome():
  print('Welcome to the good burger, home of the good burger, can I take ya order?\n\n1) 🍔 Cheeseburger\n2) 🍟    Fries\n3) 🥤 Soda\n4) 🍦 Ice Cream\n5) 🍪 Cookie\n')

def main():
  welcome()
  order = int(input('Please enter the number for your order: '))
  while order > 5:
    order = int(input('The number you chose is not available. Please enter a valid order number: \n'))
  print(f'\n{get_item(order)} on the way!')

main()