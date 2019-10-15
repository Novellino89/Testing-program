import random as r
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
   valore=[]
   due=0
   tre=0
   for i in range(1,7):
       valore.append(tiro.count(i))
       if (tiro.count(i) == 5):
           #print('Hai cinque ' +str(i))
           somma=i*5
           vincente=8
           return vincente,somma
           break
       elif(tiro.count(i) == 4):
           #print('Hai quattro ' +str(i))
           somma=i*4
           vincente=7
           return vincente,somma
           break
       elif(tiro.count(i) == 3):
           tre=1
           tris=i
       elif(tiro.count(i) == 2):
           due+=1
           coppia=i
       if tre==1 and due==0:
           #print('Hai un tris di ' + str(tris))
           vincente=3
       elif tre==1 and due==1:
          # print('Hai un full')
           vincente=6
           return vincente,somma
           break
       elif due==1:
           #print('Hai una coppia di ' +str(coppia))
           vincente=1
       elif due==2:
          # print('Hai una doppia coppia')
           vincente=2
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
    #inizializzazione liste
    tiroa=[]
    tiro=[]
    valore=[]
    try:
        scelta=input('Vuoi giocare a poker di dadi? S/N ')
    except:
        print('Inserisci o S per giocare ancora o N per uscire')
    if scelta=='s' or scelta=='S':
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
        #lancio dei dadi e ordinamento del tuo avversario
        for i in range(5):
            tiroa.append(tira())
        tiroa.sort()
        print('Questo è il tiro del tuo avversario')
        print(tiroa)
        #conteggio valori avversario

        vincentea,sommaa=calcola_risultato(tiroa)

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
