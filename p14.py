class Vehicle:

  def __init__(self,make,model,rental_rate):
    self.make=make
    self.model=model
    self.rental_rate=rental_rate

  
  def calculate_rent(self,days):
    return self.rental_rate * days

  
class car(Vehicle):

  def __init__(self, make, model, rental_rate,seating_capacity):
    super().__init__(make, model, rental_rate)
    self.seating_capacity=seating_capacity

  def calculate_rent(self, days):
    rent=super().calculate_rent(days)
    if days > 7:
      original_amnt= (self.rental_rate*days)
      print("Original amount before discount is : ",original_amnt)
      rent = self.rental_rate*0.05
      amount = (self.rental_rate - rent)*days
      print("Amount after the discount is : ",amount)

c1=car("Elantra","Electric",1500,5)
c1.calculate_rent(28)

