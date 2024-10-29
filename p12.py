class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  
  def introduce(self):
    print(f"Hello, my name is {self.name} and my age is {self.age}")

class Student(Person):
  def __init__(self, student_id,name,age):
    super().__init__(name,age)
    self.student_id=student_id

  def introduce2(self):
    print(f"Hello my name is {self.name} and my age is {self.age} and my student id is {self.student_id}")

class Teacher(Person):
  
  def __init__(self,name,age,subject):

    super().__init__(name,age)
    self.subject=subject

  
  def introduce2(self):
    self.introduce()

    print(f"and my teaching subject is {self.subject}")
    

# p1=Person("Taha",23)
# p2=Student(44,"Taha","23")
# p2.introduce2()
p3=Teacher("Taha",23,"Python Programming")
p3.introduce2()


  