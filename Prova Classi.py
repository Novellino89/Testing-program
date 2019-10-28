import random as r
calcolo_modificatore(numero):
    if numero==8 or numero==9:
        modificatore=-1
        return modificatore
    if numero==10 or numero==11:
        modificatore=0
        return modificatore
    if numero==12 or numero==13:
        modificatore=1
        return modificatore
    if numero==14 or numero==15:
        modificatore=2
        return modificatore
    if numero==16 or numero==17:
        modificatore=3
        return modificatore
    if numero==18 or numero==19:
        modificatore=3
        return modificatore
class PG:
  def __init__(self):
    self.nome=input('Inserisci il nome del tuo eroe: ')
    self.forza = r.randint(2,12)+6
    self.costituzione = r.randint(2,12)+6
    self.destrezza = r.randint(2,12)+6
    self.intelligenza = r.randint(2,12)+6
    self.saggezza = r.randint(2,12)+6
    self.carisma = r.randint(2,12)+6

Gioele=PG()
print(Gioele.nome)
print(Gioele.forza)
print(Gioele.costituzione)
print(Gioele.destrezza)
print(Gioele.intelligenza)
print(Gioele.saggezza)
print(Gioele.carisma)
