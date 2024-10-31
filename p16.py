class Result:

  def __init__(self,name,phy,chem,maths):
    self.name=name
    self.phy=phy
    self.chem=chem
    self.maths=maths

  @property
  def percentage(self):
    return str ((self.phy+self.chem+self.maths)/3) + "%"
  

r1=Result("Taha",90,97,99)
print(r1.percentage)
r1.phy=78
print(r1.percentage)
