def tira():
    r.seed()
    a=r.randint(1,6)
    return a
#creazione funzione calcolo risultato
def calcola_risultato(tiro):
   coppia=0
   tris=0
   somma=0
   vincente=0
   checkcoppia=0
   checktris=0
   due=0
   tre=0
   for i in range(1,7):
      if (tiro.count(i) == 5):
            numero=i
            somma=numero*5
            vincente=8
            return vincente,somma
            break
      if(tiro.count(i) == 4):
            numero=i
            somma=numero*4
            vincente=7
            return vincente,somma
            break
      if(tiro.count(i) == 3):
           numero=i
           tre=1
           tris=i
      if(tiro.count(i) == 2):
           numero=i
           due+=1
           coppia=i
      if tre==1 and checktris==0:
           checktris=1
           vincente=3
           somma=i*3
      if tre==1 and due==1 and checktris==1:
           somma=(tris*3)+(coppia*2)
           vincente=6
           return vincente,somma
           break
      if due==1 and checkcoppia==0:
           checkcoppia=1
           numero=i
           somma=numero*2
           vincente=1
      if due==2 and checkcoppia==1:
           somma=somma+(i*2)
           vincente=2
           return vincente,somma
           break
      if (tiro[0]==1 and tiro[1]==2 and tiro[2]==3 and tiro[3]==4 and tiro[4]==5):
            vincente=4
            return vincente,somma
            break
      elif (tiro[0]==2 and tiro[1]==3 and tiro[2]==4 and tiro[3]==5 and tiro[4]==6):
            vincente=5
            return vincente,somma
            break
   return vincente,somma

def Visualizza_Ottenuto(vincente,avversario):
    if vincente==0 and avversario==0:
        print('purtroppo il tuo lancio non vale nulla \n')
    elif vincente==1 and avversario==0:
        print('Hai ottenuto una coppia\n')
    elif vincente==2 and avversario==0:
        print('Hai ottenuto una doppia coppia\n')
    elif vincente==3 and avversario==0:
        print('Hai ottenuto un tris\n')
    elif vincente==4 and avversario==0:
        print('Hai ottenuto una scala di 5\n')
    elif vincente==5 and avversario==0:
        print('Hai ottenuto una scala di 6\n')
    elif vincente==6 and avversario==0:
        print('Hai ottenuto un full\n')
    elif vincente==7 and avversario==0:
        print('Hai ottenuto 4 dadi uguali\n')
    elif vincente==8 and avversario==0:
        print('Hai ottenuto 5 dadi uguali, è strabiliante\n')
    elif vincentea==0 and avversario==1:
        print('Il tuo avversario non ha ottenuto nulla\n')
    elif vincentea==1 and avversario==1:
        print('Il tuo avversario ha una coppia\n')
    elif vincentea==2 and avversario==1 :
        print('Il tuo avversario ha una doppia coppia\n')
    elif vincentea==3 and avversario==1:
        print('Il tuo avversario ha un tris\n')
    elif vincentea==4 and avversario==1:
        print('Il tuo avversario ha una scala di 5\n')
    elif vincentea==5 and avversario==1:
        print('Il tuo avversario ha una scala di 6\n')
    elif vincentea==6 and avversario==1:
        print('Il tuo avversario ha un full\n')
    elif vincentea==7 and avversario==1:
        print('Il tuo avversario ha 4 dadi uguali\n')
    elif vincentea==8 and avversario==1:
        print('Il tuo avversario ha 5 dadi uguali, spera nella tua buona stella\n')
