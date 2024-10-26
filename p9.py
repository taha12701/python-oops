# class Bank:
#   def __init__(self,bal,acc):
#     self.bal=bal
#     self.acc=acc
#     print("Your total balance is : ",self.bal)

#   def message(self):
#     print("Welcome to Standard Charted....")

#   def debit(self,amount):
#     self.bal -=amount
#     self.amount=amount
#     print("Amount debit : ",self.amount)

#   def credit(self,amount):
#     self.bal +=amount
#     self.amount=amount
#     print("Amount credit : ",self.amount)
  
#   def total_bal(self):
#     return self.total_bal

# b1=Bank(10000,12701)
# b1.message()
# print("Total amount : ",b1.bal)
# b1.debit(3500)
# b1.credit(2500)


# class Bank:
#   def __init__(self,bal,acc_no):
#     self.bal=bal
#     self.acc_no=acc_no
#     print("You have a balance :",self.bal)
    

#   def welcome(self):
#     print("Welcome to our Bank.................")

#   def debit(self,debit):
#     self.debit=debit
#     self.bal +=self.debit
    
#     print("debit amount is :",self.debit)
  
#   def credit(self,credit):
#     self.credit=credit
#     self.bal -=self.credit
#     print("credit amount is :",self.credit)
  
#   def message(self):
#     print("Thank you for using our services................")


# b1=Bank(75000,1234)
# b1.debit(2700)
# b1.credit(0)
# print("The total balance is :",b1.bal)
# b1.message()



#banking system
class Bank:
  def __init__(self,bal,acc):
    self.bal=bal
    self.acc=acc
    print("Your current balance is: ",self.get_balance())

  def debit(self,amount):
    self.bal +=amount
    print("Amount", amount, " was debited")
    print("Your total balance is :", self.get_balance())

  
  def credit(self,amount):
    self.bal -=amount
    print("Amount", amount, " was credited")
    print("Your total balance is :", self.get_balance())

  def get_balance(self):
    return self.bal

  def message(self):
    print("Thank you for using our services.........")

b1=Bank(75000,12701)
b1.debit(500)
b1.credit(700)

    