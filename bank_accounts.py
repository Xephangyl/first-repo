class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self, amount):
    self.balance = self.balance + amount
    print('Your balance is: ' + str(self.balance))


  def withdraw(self, amount):
    self.balance = self.balance - amount
    print('You have withdrawn: ' + str(25))

  def display_balance(self):
    print('Your current balance is: ' + str(self.balance))

devin = BankAccount('Devin', 'Roberts', 126, 'Checking', 8208, 10000)

devin.deposit(96)
devin.withdraw(25)
devin.display_balance()