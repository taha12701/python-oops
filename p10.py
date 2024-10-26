# class Student:
#   def __init__(self,name):
#     self.name=name

# s1=Student("Taha")
# print(s1.name)
# del s1
# print(s1.name)


# class Bank:
#   def __init__(self,acc_no,acc_pass):
#     self.acc_no=acc_no
#     self.acc_pass=acc_pass

# b1=Bank("1234","abcd")
# print("Your password is:",b1.acc_pass)

# to make it private we can 

# class Bank:
#   def __init__(self,acc_no,acc_pass):
#     self.acc_no=acc_no
#     self.__acc_pass=acc_pass

#   def reset_pass(self):
#     print("Your previous password is:",self.__acc_pass)

# b1=Bank("1234","abcd")
# b1.reset_pass()
# print(b1.__acc_pass)
# print("Your password is:",b1.__acc_pass)
# print("Your password is:",b1.__acc_pass)


class Person:
  __name="anonymous"

  def __hello(self):
    print("Hello")

  def welcome(self):
    print(self.__hello())



# p1=Person()
p1=Person()
p1.welcome()

