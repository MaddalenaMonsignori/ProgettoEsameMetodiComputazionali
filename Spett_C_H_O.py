import numpy as np
import math
import sys
import matplotlib.pyplot as plt
import pandas as pd
import Elemento as el





############### VALORI UTILI

massa_p_n= (1.67262192369*(10**(-27))+1.674927351*(10**(-27)))/2 #MEDIA DELLA MASSA IN KG DEI PROTONI E NEUTRONI

H= el.Elemento('H', np.array([1, 2]), np.array([99.985, 0.015]))
C= el.Elemento ('C', np.array([12]), np.array([100]))
O= el.Elemento ('O', np.array([16]), np.array([100]))





############### FUNZIONI UTILI

# str.maketrans() è un metodo della classe str che che restituisce una tabella di traduzione (da utilizzare con il metodo str.traslate()); str.maketrans() prende in input 2 argomenti, di cui il primo sono i caratteri da sostituire, mentre il secondo sono i caratteri di sostituzione. I caratteri da sostituire sono numeri interi positivi mentre i caratteri di sostituzione sono gli stessi nummri interi positivi in forma di pedici

# La funzione pedice (utilizza str.traslate()) prende in input un numero (non necessariamete intero e non necessariamente positivo) num e ne restituisce il corrispettivo pedice. Questo metodo chiama su num, prima convertito in stringa con str(num), il metodo della classe str str.traslate() che ha come parametro la tabella di sostituzione definita sopra (subscripts)

subscripts = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

def pedice(num):
    return (str(num).translate(subscripts))

    
subscripts1 = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

def apice(num):
    return (str(num).translate(subscripts1))


#### definisco 2 funzioni perchè ciasucna può avere un solo retutn

#La funzione esponenti_binomio_newton e addendi_binomio_newton mi calcolano rispettivamente gli esponenti e gli addendi del binomio di newton in input. In particolare la funzione esponenti_binomio_newton restituisce una matrice dove ogni riga la coppia di esponenti.(Definisco 2 funzioni perchè ciascuna può avere un solo return). Queste deu funzioni sono chiamate successivamente nel metodo Get_Abbondanze_H() per ottenere le probabilità(addendi del binomio di newton) di ciascuna possibile combinazione di isotopi(coppia di esponenti) di H nella molecola

def esponenti_binomio_newton(nn):
    
    if((type(nn)==int or type(nn)==np.int64) and nn>0):

        nk=np.zeros((nn+1, 2))
        for k in range(nn+1):
                nk[k][0]=nn-k
                nk[k][1]= k
        return nk.astype(int)      
    else:
      return None

  
def addendi_binomio_di_newton(a, b, n):

    if((type(n)==int or type(n)==np.int64) and n>1):

        coefficienti_binomiali=np.zeros(n+1)
        addendi=np.zeros(n+1)

        for k in range(n+1): # k va da 0 a n
            coefficienti_binomiali[k]= math.comb(n, k)
            addendi[k]=coefficienti_binomiali[k]*(a**(n-k))*(b**k)
        return addendi
    elif(n==1):
        coefficienti_binomiali=1
        addendi=np.array([a, b])
        return addendi
    else:
        return None





############### CLASSE SpettrometroTOF_C_H_O --> spettrometro di massa TOF che analizza molecole costituite solo da atomi di C, H, O. Il numero di atomi di ciascun elemento presente viene inserito dall'utente da console

'''   
Definisco il costruttore dello spettrometro in modo che acquisisce da console il numero di atomi per ciascun elemento. Se si verificano i seguenti casi il programma non va a buon fine e termina in anticipo:
-il numero di atomi non è di tipo int
-il numero di atomi è negativo o nullo
Se l'acquisizione è andata a buon fine il costruttore stampa a schermo la molecola
'''

class SpettrometroTOF_C_H_O():
    

    def __init__(self):

        print('\nNUOVO SPETTROMETRO DI MASSA INTERATTIVO\n')
        self.atomi=np.array(["C", "H", "O"])
        self.n_atomi_inseriti=np.zeros(3).astype(int)
        n_atomi=np.zeros(3).astype(int)
    
        for i in range (len(self.atomi)):
            
             print('Inserisci il numero di atomi di ', self.atomi[i], " : " )
             n_atomi[i] =input(' ') # Visto che ho definito sopra n_atomi[] come array di tipo int se in input inserisco un valore che non è intero mi dà errore
             
             if(n_atomi[i]>0):
                 self.n_atomi_inseriti[i]=n_atomi[i] # Visto che ho definito sopra n_atomi e self.n_atomi_inseriti come int self.n_atomi_inseriti sarà di tipo int anche dopo l'assegnamento
                 
             else:
                 print('Errore: hai inserito un numero di atomi negativo o nullo. Il programma non è andato a buon fine. \n')
                 sys.exit()

        print('\nInserimento andato a buon fine!')
        print('I tipi di atomi presenti nella molecola sono: ', self.atomi )
        print('I numeri di atomi per ogni atomo presente nella molecola sono: ', self.n_atomi_inseriti )
        
        #self.carbonio=self.atomi[0]+str(pedice(self.n_atomi_inseriti[0]))
        #self.idrogeno=self.atomi[1]+str(pedice(self.n_atomi_inseriti[1]))
        #self.ossigeno=self.atomi[2]+str(pedice(self.n_atomi_inseriti[2]))
        self.stringa_molecola=self.atomi[0]+str(pedice(self.n_atomi_inseriti[0]))+self.atomi[1]+str(pedice(self.n_atomi_inseriti[1]))+self.atomi[2]+str(pedice(self.n_atomi_inseriti[2]))
        print('La molecola inserita è ', self.stringa_molecola)
        print("\nPer ottenere tutte le possibili combinazioni, e le relative probabilità, in cui si possono presentare gli isotopi di H all'interno della molecola inserita, chiamare il metodo Get_Abbondanza_H()")
        print('\n')


# Metodo che calcola tutte le possibili combinazioni, e le relative probabilità, in cui si possono presentare gli isotopi di H all'interno della molecola inserita mediante distribuzione binomiale, e ne restituisce le probabilità. I dati vengono stampati a schermo, visualizzati (e salvati in .csv) in una tabella in cui sono presenti anche i numeri di massa e le masse della molecola per ogni combinazione di isotopi di H e rappresentati (e salvati .png) mediante lo spettro di massa che grafica in un diagramma a barre i numeri di massa della molecola in funzione della probabilità
        
    def Get_Abbondanza_H(self):
        
        c_12=str(apice(C.array_isotopi[0]))+self.atomi[0]
        o_16=str(apice(O.array_isotopi[0]))+self.atomi[2]
        
        print("\nQuesta funzione permette di calcolare tutte le possibili combinazioni, e le relative probabilità, in cui si possono presentare gli isotopi di H all'interno della molecola inserita", self.stringa_molecola)
        print("Questo partendo dal presupposto che gli elementi", self.atomi[0], "e", self.atomi[2], "sono presenti al 100% nel loro isotopo più abbondante", c_12, "e", o_16)

        self.combinazioni=esponenti_binomio_newton(self.n_atomi_inseriti[1])     
        self.probabilità_combinazioni=(addendi_binomio_di_newton((H.array_abbondanze[0])/100, (H.array_abbondanze[1])/100, self.n_atomi_inseriti[1]))*100 # abbondanza deve essere espressa come 0.0qualcosa sennò dà valori che sommati non danno 100
        self.a_molecola=np.zeros(len(self.probabilità_combinazioni)).astype(int)
        self.massa_molecola=np.zeros(len(self.probabilità_combinazioni))

        
        prozio=str(apice(H.array_isotopi[0])+self.atomi[1])
        deuterio=str(apice(H.array_isotopi[1])+self.atomi[1])

        for i in range (len(self.probabilità_combinazioni)):
            print ('La combinazione di', self.stringa_molecola  , 'che prevede la presenza di', self.combinazioni[i][0] , 'atomi di', prozio, 'e', self.combinazioni[i][1], 'atomi di',  deuterio , ' ha probabilità di esistere del', self.probabilità_combinazioni[i], '%'   )
            self.a_molecola[i]=H.array_isotopi[0]*self.combinazioni[i][0]+H.array_isotopi[1]*self.combinazioni[i][1]+C.array_isotopi[0]*self.n_atomi_inseriti[0]+O.array_isotopi[0]*self.n_atomi_inseriti[2]
            self.massa_molecola[i]=self.a_molecola[i]*massa_p_n
        print('\n')

        
        tabella_prozio='Numero di '+str(apice(H.array_isotopi[0]))+self.atomi[1]+' in '+self.stringa_molecola
        tabella_deuterio='Numero di '+str(apice(H.array_isotopi[1]))+self.atomi[1]+' in '+self.stringa_molecola
        tabella_a='Numero di massa di '+self.stringa_molecola
        tabella_massa='Massa di '+self.stringa_molecola+' [Kg]'
        df= pd.DataFrame(columns=[tabella_prozio, tabella_deuterio , 'Probabilità %', tabella_a, tabella_massa ])
        df[tabella_prozio]=self.combinazioni[:, 0]
        df[tabella_deuterio]=self.combinazioni[:, 1]
        df['Probabilità %']=self.probabilità_combinazioni
        df[tabella_a]=self.a_molecola
        df[tabella_massa]=self.massa_molecola
        df.to_csv('Probabilità-isotopi-H-in-molecola'+self.stringa_molecola+'.csv', index=False)
        print(df)
        print('\n')


        print('Spettro di massa di', self.stringa_molecola)
        col=input('Inserisci un colore tra i seguenti:\n-red\n-coral\n-salmon\n-sienna\n-darkorange\n-yellow\n-limegreen\n-darkgreen\n-aqua\n-darkblue\n-darkviolet\n-purple\n-hotpink\n')
        plt.figure(figsize=(12, 6))
        plt.bar(self.a_molecola, self.probabilità_combinazioni, color=col)
        plt.title('Spettro di massa '+self.stringa_molecola, fontsize=15, color=col)
        plt.xlabel('Numero di massa', fontsize=12)
        plt.ylabel('Abbondanze %', fontsize=12)
        plt.xticks(self.a_molecola)
        #plt.savefig('Spettro-di-massa-C-H-O.png')
        plt.show()
        print('\n')
        return self.probabilità_combinazioni

        
     
        
            

