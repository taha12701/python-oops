class Student:
  college_name="Pakistan Cricket Board"
  name="anonymous"   #class attributes
  def __init__(self,name,age):
    self.name=name
    self.age=age
    print("New Members are adding...")

s1=Student("Taha",23)
# print(s1.name,s1.age)
# print(s1.college_name)    #both ways to access class attrib
# print(Student.college_name) # //
print(Student.name)

s2=Student("Babar",30)
print(s2.name,s2.age)
