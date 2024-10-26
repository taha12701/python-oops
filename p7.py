class Team:
  print("Welcome to Pakistan Cricket Team.....")

  def __init__(self,ply1,ply2,ply3):
    self.ply1=ply1
    self.ply2=ply2
    self.ply3=ply3

  @staticmethod
  def select_ply():
    print("Squad for Champions Trophy 2025")


t1=Team("Sajid Khan","Noman Ali","Saud Shakeel")
print(t1.ply1,t1.ply2,t1.ply3)
t1.select_ply()
