class item:
  pay_rate=0.8 #pay rate after 20% discount

  def __init__(self,name:str,price:float,quantity:int):
    assert price >=0, f"Price {self.price} should not be less than zero"
    assert quantity >=0 , f"Quantity {self.quantity} should not be less than zero"

    self.name=name
    self.price=price
    self.quantity=quantity

  def calc_price(self):
    self.actual_amnt=self.price * self.quantity
    print("The total amount is : ",self.actual_amnt)

  #applying the discount 

  def cal_discount(self):
    self.disc=self.actual_amnt * self.pay_rate
    print("Amount after discount is : ",self.disc)

  
i1=item("The Book",347,8)
i1.calc_price()
i1.cal_discount()

i2=item("Cricket Bat",250,9)
i2.pay_rate=0.6
i2.calc_price()
i2.cal_discount()

# print(i1.pay_rate)
# print(item.pay_rate)

# print(i1.__dict__)
# print(item.__dict__)



#so if we want to change the class attribute value than:
#we can use the self keyword in one of the methods in the calculate price