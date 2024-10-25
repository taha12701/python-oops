# class Student:
#   college_name="anonymous"

#   def __init__(self,name,marks1,marks2,marks3):
#     self.name=name
#     self.marks1=marks1
#     self.marks2=marks2
#     self.marks3=marks3

#   def cal_avg(self):
#     return(self.marks1+self.marks2+self.marks3)/3
    
# s1=Student("Taha",90,96,95)
# print(s1.name,s1.cal_avg())


class Student:
  college_name='anonymous'

  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
  @staticmethod
  def hello():
    print("hello dunyaa!!!")

  def calc_avg(self):
    sum=0
    for item in self.marks:
      sum +=item
    print("hi,Taha.. Your score is  ",sum/3)

s1=Student('Taha',[45,46,47])
s1.calc_avg()
s1.hello()
