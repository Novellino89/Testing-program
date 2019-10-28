import random as r
def calcolo_modificatore(numero):
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
        modificatore=4
        return modificatore
class PG:
  def __init__(self):
    self.nome=input('Inserisci il nome del tuo eroe: ')
    self.difesa= 10 + self.mdestrezza
    self.forza = r.randint(2,12)+6
    self.mforza=calcolo_modificatore(self.forza)
    self.costituzione = r.randint(2,12)+6
    self.mcostituzione=calcolo_modificatore(self.costituzione)
    self.destrezza = r.randint(2,12)+6
    self.mdestrezza=calcolo_modificatore(self.destrezza)
    self.intelligenza = r.randint(2,12)+6
    self.mintelligenza=calcolo_modificatore(self.intelligenza)
    self.saggezza = r.randint(2,12)+6
    self.msaggezza=calcolo_modificatore(self.saggezza)
    self.carisma = r.randint(2,12)+6
    self.mcarisma=calcolo_modificatore(self.carisma)

Gioele=PG()
print(Gioele.nome)
print("La tua difesa è di ",Gioele.difesa)
print("La tua forza è di",Gioele.forza,"il modificatore è quindi di",Gioele.mforza)
print("La tua costituzione è di",Gioele.costituzione,"il modificatore è quindi di",Gioele.mcostituzione)
print("La tua destrezza è di",Gioele.destrezza,"il modificatore è quindi di",Gioele.mdestrezza)
print("La tua intelligenza è di",Gioele.intelligenza,"il modificatore è quindi di",Gioele.mintelligenza)
print("La tua saggezza è di",Gioele.saggezza,"il modificatore è quindi di",Gioele.msaggezza)
print("Il tuo carisma è di",Gioele.carisma,"il modificatore è quindi di",Gioele.mcarisma)
