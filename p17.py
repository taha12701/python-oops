class Complex:

  def __init__(self,real,img):
    self.real=real
    self.img=img

  def show_num(self):
    print(self.real,"i +",self.img,"j")

  def __add__(self,num2):
    newReal=self.real + num2.real
    newImg=self.img + num2.img
    return Complex(newReal,newImg)
  
  def __sub__(self,num2):
    newReal=self.real - num2.real
    newImg=self.img - num2.img
    return Complex(newReal,newImg)

c1=Complex(4,5)
c1.show_num()

c2=Complex(1,3)
c2.show_num()

# c3=c1+c2
c3=c1-c2
c3.show_num()

