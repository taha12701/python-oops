class Bank:
  def __init__(self,bal,acc):
    self.bal=bal
    self.acc=acc
    print("Your total balance is : ",self.bal)

  def message(self):
    print("Welcome to Standard Charted....")

  def debit(self,amount):
    self.bal -=amount
    self.amount=amount
    print("Amount debit : ",self.amount)

  def credit(self,amount):
    self.bal +=amount
    self.amount=amount
    print("Amount credit : ",self.amount)
  
  def total_bal(self):
    return self.total_bal

b1=Bank(10000,12701)
b1.message()
print("Total amount : ",b1.bal)
b1.debit(3500)
b1.credit(2500)

