#Object Oriented Programming


#creating class
# class Student:
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age
#     print("Adding new members in database....")
 
# #creating object
# s1=Student("Taha",23)
# print(s1.name)
# print(s1.age)
# print(s1.name)

# s2=Student()
# print(s2.name)



# class Car:
#   color="blue"
#   brand="Toyota"

# c1=Car()
# print(c1.color)
# print(c1.brand)

class Car:

  def __init__(self,name,model,color):
    self.name=name
    self.color=color
    self.model=model

    print("New cars are adding in the database....")


c1=Car("Civic",2024,"Black")
print(c1.name,c1.color,c1.model)

c2=Car("Bmw",2024,"Gray")
print(c1.name,c1.color,c1.model)
