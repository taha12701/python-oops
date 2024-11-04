class items:
  pay_rate=0.90

  def __init__(self,name:str,price:int,quantity:int):
    self.name=name
    self.price=price
    self.quantity=quantity


  def actual_amount(self):
    self.act_amt=self.price * self.quantity
    print(f"Price of {self.name} is : $ {self.act_amt:.1f}")

  def discount_amount(self):
    self.disc_amt=self.act_amt * self.pay_rate
    print(f"The discounted amount is : $ {self.disc_amt:.1f}")

  def amount_detect(self):
    self.amount=self.act_amt - self.disc_amt
    print(f"The amount detect from after discount is : $ {self.amount:.2f}")
    


i1=items("Atomic Habits",35,8)
i1.actual_amount()
i1.discount_amount()
i1.amount_detect()

i2=items("State of Overconfidence",39,17)
i2.actual_amount()
items.pay_rate=0.87
i2.discount_amount()
i2.amount_detect()