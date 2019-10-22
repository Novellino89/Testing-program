import random as r
import os
#from Definizione_funzioni import tira,calcola_risultato,Visualizza_Ottenuto
#creazione funzione tira
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
checkfine=1
piatto=0
#Inizio programma
while True:
    if checkfine==1:
        denaro=r.randint(150,400)
        denaroa=r.randint(250,600)
        print('Attualmente hai nel portafoglio' , denaro,'Euro')
        print('Il tuo avversario ha nel portafoglio',denaroa,'Euro')
    else:

        print('Attualmente hai nel portafoglio' , denaro,'Euro')
        print('Il tuo avversario ha nel portafoglio',denaroa,'Euro')
    ripetizione=0
    tiroa=[]
    tiro=[]
    valore=[]
    try:
        scelta=input('Vuoi giocare a poker di dadi? S/N ')
    except:
        print('Inserisci o S per giocare ancora o N per uscire \n')
    if scelta=='s' or scelta=='S':
        os.system('cls')
        if denaro<=0:
            print('Non hai più soldi da scommettere e non possiamo più farti giocare. Ci spiace ma deve abbandonare l"edificio.')
            break
        if denaroa<=0:
            print('Hai mandato sul lastrico il tuo avversario! Ma si sta avvicinando un"altra persona al tavolo.')
            denaroa=r.randint(150,600)
            continue
        puntata=input('\n Inserisci quanto vuoi scommettere per questa puntata ')
        puntata=int(puntata)
        if puntata>denaro:
            print('Non hai abbastanza soldi')
            continue
        denaro-=puntata
        if denaroa<puntata:
            print('Il tuo avversario accetta ma ha meno soldi della tua posta, mette tutto quello che ha.')
            piatto=puntata+denaroa
            denaroa=0
        else:
            print("l'avversario accetta la posta \n")
            denaroa-=puntata
            piatto=puntata*2
        #lancio dei dadi e ordinamento
        for i in range(5):
            tiro.append(tira())
        tiro.sort()
        print(tiro,"\n")
        vincente,somma=calcola_risultato(tiro)
        Visualizza_Ottenuto(vincente,0)
        try:
            scelta1=input('Vuoi Ritirare qualche dado? ')
        except:
            print('Inserisci o S per ritirare o N per per continuare.')
        if scelta1=='s' or scelta1=='S' or scelta1=='Si' or scelta1=='S ' or scelta1=='s ':
                # taking multiple inputs at a time
            try:
                sostituisci = [int(x) for x in input("Che dadi vuoi ritirare?: ").split()]
                print("I dadi che vuoi ritirare sono: ", sostituisci,"\n")
            except:
                    print('Inserisci per favore almeno un valore numerico.')
            for item in range(0,len(sostituisci)):
                if sostituisci[item] in tiro:
                    tiro[tiro.index(sostituisci[item])]=tira()
            print('Il tuo nuovo tiro è \n ' )
            tiro.sort()
            print(tiro,"\n")
        if scelta1=='n' or scelta1=='N' or scelta1=='NO' or scelta1=='no' or scelta1=='n 'or scelta1=='N ':
            ripetizione=1
        #conteggio valori
        vincente,somma=calcola_risultato(tiro)
        if ripetizione!=1:
            Visualizza_Ottenuto(vincente,0)
        for i in range(5):
            tiroa.append(tira())
        tiroa.sort()
        print('Questo è il tiro del tuo avversario\n')
        print(tiroa,"\n")
        #conteggio valori avversario
        vincentea,sommaa=calcola_risultato(tiroa)
        Visualizza_Ottenuto(vincente,1)
        if vincente>vincentea:
            print('Congratulazioni, hai vinto!\n')
            denaro+=piatto
            checkfine=0
        elif vincente<vincentea:
            print('Peccato, hai perso!\n')
            denaroa+=piatto
            checkfine=0
        else:
            if somma>sommaa:
                    print('Congratulazioni, hai vinto!\n')
                    denaro+=piatto
                    checkfine=0
            elif somma<sommaa:
                    print('Peccato, hai perso!\n')
                    denaroa+=piatto
                    checkfine=0
            else:
                print('Il punteggio è finito in parità, è molto raro ma può capitare. Giocate ancora per spareggiare.\n')
                if casuale==1:
                    denaro+=piatto
                    denaroa+=piatto
                    checkfine=0
                elif casuale==2:
                    denaro+=piatto
                    denaroa+=(piatto+piattosuperiore)
                    checkfine=0
              #aggiungo commento per la sincronizzazione di Github.
    elif scelta=='n' or scelta=='N':
        print('grazie per aver giocato al poker di dadi')
        break
    else:
        print('Inserisci S per giocare ancora o N per uscire')
        continue
