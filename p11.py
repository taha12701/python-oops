#inheritance in oops
# class Car:
#   color="Black"
  
#   @staticmethod
#   def start():
#     print("Car has started...")

#   @staticmethod
#   def stop():
#     print("Car has stopped...")

# class ToyotaCar(Car):
#   def __init__(self,brand):
#     self.brand=brand

# class Fortuner(ToyotaCar):
#   def __init__(self,type):
#     self.type=type


# f1=Fortuner("Diesel")
# print(f1.start())



# c1=ToyotaCar("Fortuner")
# c2=ToyotaCar("Priusp")
# print(c1.brand)
# print(c1.start())
# print(c1.color)


#multiple parents method

class A:
  varA="Welcome to our class A"

class B:
  varB="Welcome to our class B"

class C(A,B):
  varC="Welcome to our class C"

c1=C()
print(c1.varC)
print(c1.varB)
print(c1.varA)
