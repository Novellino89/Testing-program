import random as r
class PG:
  def __init__(self):
    self.forza = r.randint(2,12)+6
    self.costituzione = r.randint(2,12)+6
    self.destrezza = r.randint(2,12)+6
    self.intelligenza = r.randint(2,12)+6
    self.saggezza = r.randint(2,12)+6
    self.carisma = r.randint(2,12)+6

Gioele=PG()
print(Gioele.forza)
print(Gioele.costituzione)
print(Gioele.destrezza)
print(Gioele.intelligenza)
print(Gioele.saggezza)
print(Gioele.carisma)
