class Student:
  college_name="anonymous"

  def __init__(self,name,age,marks):
    self.name=name
    self.age=age
    self.marks=marks

  
  def welcome(self):
    print("Welcome to our college student...")

  def get_marks(self):
    return self.marks


s1=Student("Taha",23,97)
print(s1.name,s1.age)
print("Marks are : ",s1.get_marks())
s1.welcome()
