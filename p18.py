class item:
  pay_rate=0.8

  def __init__(self,name:str,price:int,quantity:int):
    assert price >=0 , f"Price {price} should be greater or equal to zero!!!"
    assert quantity >=0 , f"Quantity {quantity} should be zero or greater than zero !!!"
    self.name=name
    self.price=price
    self.quantity=quantity
    
    

  def cal_quantity(self):
    print("The total amount is : ",self.price*self.quantity)
  



i1=item("S24 ultra",1500.5,6)
i2=item("iphone 16 pro max",3500,4)
print(item.pay_rate)
print(i1.pay_rate)
print(i2.pay_rate)
# i1.cal_quantity()
# i2.cal_quantity()
