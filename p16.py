class Student:

  def __init__(self,math,phy,chem):
    self.math=math
    self.phy=phy
    self.chem=chem



  @property
  def percentage(self):
    return str((self.math + self.phy + self.chem)/3) + "%"
  

s1=Student(97,92,93)
s1.chem=56
print(s1.percentage)
