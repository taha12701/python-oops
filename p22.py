class Item:
  pay_rate=0.9
  all=[]

  def __init__(self,name,price,quantity):
    self.name=name
    self.price=price
    self.quantity=quantity

    Item.all.append(self)


  def calculate_price(self):
    self.actual_amount=self.price*self.quantity
    print(f"The actual amount is : $ {self.actual_amount}")


  def discount_price(self):
    self.discount_amount=self.actual_amount*self.pay_rate
    print(f"The amount after discount is : $ {self.discount_amount}")


  def __repr__(self):
    return f"item '{self.name}', {self.quantity},{self.price})"
  

i1=Item("Atomic Habits",35,6)
# i1.calculate_price()
# i1.discount_price()

i2=Item("Progress Days",49,9)
i3=Item("Silency",42,8)
i4=Item("Beleiver",61,17)
i5=Item("Progression",30,10)

print(Item.all)

# for instance in Item.all:
#   print(instance.name,instance.quantity,instance.price)

# Item.pay_rate=0.98
# i2.calculate_price()
# i2.discount_price()