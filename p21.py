class item:
  pay_rate=0.8 #pay rate after 20% discount
  all=[]

  def __init__(self,name:str,price:float,quantity:int):
    assert price >=0, f"Price {self.price} should not be less than zero"
    assert quantity >=0 , f"Quantity {self.quantity} should not be less than zero"

    self.name=name
    self.price=price
    self.quantity=quantity

    #to add all the instances in the list
    item.all.append(self)

  def calc_price(self):
    self.actual_amnt=self.price * self.quantity
    print("The total amount is : ",self.actual_amnt)

  #applying the discount 

  def cal_discount(self):
    self.disc=self.actual_amnt * self.pay_rate
    print("Amount after discount is : ",self.disc)

  def __repr__(self):
    return f"item('{self.name},{self.price},{self.quantity}')"

 

 

  
i1=item("The Book",347,8)
i2=item("Cricket Bat",250,9)
i3=item("Cricket Gloves",78,12)
i4=item("Cricket Thighs",127,9)
i5=item("Cricket Pads",112,6)

print(item.all)

# for instance in item.all:
#   print(instance.name)


