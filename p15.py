# class Person:
#   name="anonymous"

#   def changeName(self,name):
#     # self.name=name
#     Person.name=name

# p1=Person()
# p1.changeName("Taha")
# # print(p1.name)
# print(Person.name)


# class Person:
#   name="anonymous"

#   def changeName(self,name):
#     self.__class__.name="Babar"

# p1=Person()
# p1.changeName("Zimbabar")
# print(p1.name)
# print(Person.name)

class Person:

  name="anonymous"

  @classmethod                                  #by using this we are altering the class methods
  def changeName(cls,name):
    cls.name=name

p1=Person()
p1.changeName("Taha")
print(p1.name)
