# Write code below 💖
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
    return self.balance

  def withdraw(self, amount):
    self.balance = self.balance - amount
    return self.balance

  def display_balance(self):
    print (self.balance)

checking_account = BankAccount("Jax", "Lemons", 123456, "Checkings", 1234, 2200.50)
checking_account.deposit(50)
checking_account.withdraw(2000)
checking_account.display_balance()