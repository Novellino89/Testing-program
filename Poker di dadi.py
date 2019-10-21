import random as r
import os


#creazione funzione tira
def tira():
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
            #print(numero)
            somma=numero*5
            vincente=8
            return vincente,somma
            break
      if(tiro.count(i) == 4):
            numero=i
            #print(numero)
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
           #Se trova prima una coppia e poi un tris il programma si blocca e vede solo la coppia.
      if tre==1 and checktris==0:
           #print('Hai un tris di ' + str(tris))
           checktris=1
           vincente=3
           somma=i*3
      if tre==1 and due==1 and checktris==1:
          # print('Hai un full')
           somma=(tris*3)+(coppia*2)
           vincente=6
           return vincente,somma
           break
      if due==1 and checkcoppia==0:
           #print('Hai una coppia di ' +str(coppia))
           checkcoppia=1
           numero=i
           somma=numero*2
           vincente=1
      if due==2 and checkcoppia==1:
          # print('Hai una doppia coppia')
           somma=somma+(i*2)
           vincente=2
           return vincente,somma
           break
      if (tiro[0]==1 and tiro[1]==2 and tiro[2]==3 and tiro[3]==4 and tiro[4]==5):
            #print('Hai effettuato una scala di 5!')
            vincente=4
            return vincente,somma
            break
      elif (tiro[0]==2 and tiro[1]==3 and tiro[2]==4 and tiro[3]==5 and tiro[4]==6):
            #print('Hai effettuato una scala di 6!')
            vincente=5
            return vincente,somma
            break
   return vincente,somma
#Inizio programma
while True:
    #print (’\n’ * 100)
    #inizializzazione liste
    tiroa=[]
    tiro=[]
    valore=[]
    try:
        scelta=input('Vuoi giocare a poker di dadi? S/N ')
    except:
        print('Inserisci o S per giocare ancora o N per uscire')
    if scelta=='s' or scelta=='S':
        os.system('cls')
        #lancio dei dadi e ordinamento
        for i in range(5):
            tiro.append(tira())
        tiro.sort()
        print(tiro)
        #conteggio valori
        vincente,somma=calcola_risultato(tiro)
        if vincente==0:
            print('purtroppo il tuo lancio non vale nulla')
        elif vincente==1:
            print('Hai ottenuto una coppia')
        elif vincente==2:
            print('Hai ottenuto una doppia coppia')
        elif vincente==3:
            print('Hai ottenuto un tris')
        elif vincente==4:
            print('Hai ottenuto una scala di 5')
        elif vincente==5:
            print('Hai ottenuto una scala di 6')
        elif vincente==6:
            print('Hai ottenuto un full')
        elif vincente==7:
            print('Hai ottenuto 4 dadi uguali')
        elif vincente==8:
            print('Hai ottenuto 5 dadi uguali, è strabiliante')
        try:
            scelta=input('Vuoi Ritirare qualche dado? ')
        except:
            print('Inserisci o S per ritirare o N per per continuare.')
        if scelta=='s' or scelta=='S':
            print('che dado vuoi ritirare?')
            #istruzioni della scelta
        else:

        #lancio dei dadi e ordinamento del tuo avversario
            for i in range(5):
                tiroa.append(tira())
            tiroa.sort()
            print('Questo è il tiro del tuo avversario')
            print(tiroa)
            #conteggio valori avversario
            vincentea,sommaa=calcola_risultato(tiroa)
            if vincentea==0:
                print('Il tuo avversario non ha ottenuto nulla')
            elif vincentea==1:
                print('Il tuo avversario ha una coppia')
            elif vincentea==2:
                print('Il tuo avversario ha una doppia coppia')
            elif vincentea==3:
                print('Il tuo avversario ha un tris')
            elif vincentea==4:
                print('Il tuo avversario ha una scala di 5')
            elif vincentea==5:
                print('Il tuo avversario ha una scala di 6')
            elif vincentea==6:
                print('Il tuo avversario ha un full')
            elif vincentea==7:
                print('Il tuo avversario ha 4 dadi uguali')
            elif vincentea==8:
                print('Il tuo avversario ha 5 dadi uguali, spera nella tua buona stella')
            if vincente>vincentea:
                print('Congratulazioni, hai vinto!')
            elif vincente<vincentea:
                print('Peccato, hai perso!')
            else:
                if somma>sommaa:
                        print('Congratulazioni, hai vinto!')
                elif somma<sommaa:
                        print('Peccato, hai perso!')
                else:
                    print('Il punteggio è finito in parità, è molto raro ma può capitare. Giocate ancora per spareggiare.')
               #aggiungo commento per la sincronizzazione di Github.
    elif scelta=='n' or scelta=='N':
        print('grazie per aver giocato al poker di dadi')
        break
    else:
        print('Inserisci o S per giocare ancora o N per uscire')
        continue
