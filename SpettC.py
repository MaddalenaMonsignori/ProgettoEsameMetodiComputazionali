import numpy as np
import pandas as pd
import sys
import Elemento as el
import matplotlib.pyplot as plt





# VALORI UTILI

# Definisco gli elementi (oggetti di tipo Elemento) principali di cui SpettrometroTOF_Composti conosce l'abbondanza isotopica in natura. Li definisco esternamente della classe in modo che siano variabili globali e non mi compaia ulteriore codice nei metodi. 

H= el.Elemento('H', np.array([1, 2]), np.array([99.985, 0.015]))
Be= el.Elemento('Be', np.array([9]), np.array([100]))
C= el.Elemento('C', np.array([12, 13]), np.array([98.893, 1.107]))
N= el.Elemento('N', np.array([14, 15]), np.array([99.634, 0.366]))
O= el.Elemento('O', np.array([16, 17, 18]), np.array([99.759, 0.037, 0.204]))
F= el.Elemento('F', np.array([19]), np.array([100]))
Al= el.Elemento('Al', np.array([27]), np.array([100]))
Si= el.Elemento('Si', np.array([28, 29, 30]), np.array([92.23, 4.67, 3.1]))
P= el.Elemento('P', np.array([31]), np.array([100]))
S= el.Elemento('S', np.array([32, 33, 34]), np.array([95.02, 0.75, 4.23]))
Cl= el.Elemento('Cl', np.array([35, 37]), np.array([75.77, 24.23]))
K= el.Elemento('K', np.array([39, 41]), np.array([93, 7]))
Cr= el.Elemento('Cr', np.array([50, 52, 53, 54]), np.array([4.345, 83.789, 9.501, 2.365]))
Br= el.Elemento('Br', np.array([79, 81]), np.array([50.69, 49.31]))
I= el.Elemento('I', np.array([127]), np.array([100]))

# Creo un array con tutti gli elementi(oggetti di tipo Elemento) di cui SpettrometroTOF_Composizioni conosce l'abbondanza isotopica in natura

elementi_ar=np.array([H, Be, C, N, O, F, Al, Si, P, S, Cl, K, Cr, Br, I])

# Chiamo il metodo Tabella_Elementi_Isotopi_Abbondanze per visualizzare una tabella con il nome degli elementi, i numeri di massa degli isotopi e l'abbondanza isotopica che SpettrometroTOF_Composti conosce

#I.Tabella_Elementi_Isotopi_Abbondanze(elementi_ar)





############### FUNZIONI UTILI

# La funzione get_elemento prende in input un array di numeri di massa array_a e lo confronta con i numeri di massa degli elementi tabulati nell'array di elementi ar_el. Se nell'array dei numeri di massa array_a sono presenti tutti i numeri di massa relativi a un certo elemento del'array ar_el[i].array_isotopi, la funzione restituisce un'array di tipo Elemento con gli elementi presenti

def get_elemento(array_a, ar_el):
    
    elementi_present=np.zeros(1)
    elementi_present=elementi_present[:-1]
    
    for i in range (len(ar_el)):
        if all(a in array_a for a in ar_el[i].array_isotopi):
            elementi_present=np.append(elementi_present, el.Elemento(ar_el[i].nome, ar_el[i].array_isotopi, ar_el[i].array_abbondanze))
    
    return elementi_present

      


  
############### CLASSE SpettrometroTOF_Composti --> spettrometro di massa TOF che analizza composti. I numeri di massa presenti nel composto e la rispettiva % di abbondanza sono inserite da console dall'utente

'''   
Definisco il costruttore dello spettrometro in modo che acquisisce da console i valori dei numeri di massa e le rispettive abbondanze nel composto finchè l'utente non scrive stop e poi le stampa a schermo. Se si verificano i seguenti casi il programma non va a buon fine e termina in anticipo:
-il numero di massa inserito non è compreso tra 1 e 210(inclusi)
-viene inserito 2 volte lo stesso numero di massa
-la percentuale di abbondanza di un certo numero di massa è negativa
-la somma finale di tutte le percentuali dei numeri di massa inseriti è diversa da 100%
Se l'acquisizione è andata a buon fine il costruttore stampa i numeri di massa e le corrispettive abbondanze
'''

class SpettrometroTOF_Composti():

    def __init__(self):

        print('\nNUOVO SPETTROMETRO DI MASSA INTERATTIVO\n')
        
        self.a_inseriti=[]
        self.abb_inserite=[]
        somma=0
        
        while True:
             self.in_a =input("Inserisci un numero di massa presente nel composto o scrivi stop per terminare: ")
             if(self.in_a=='stop'):
                 print('\n')
                 break
             else:
                 self.in_a_int=int(self.in_a)
                 if(self.in_a_int>=1 and self.in_a_int<=210):
                     self.a_inseriti=np.append(self.a_inseriti, self.in_a_int)
                     
                     for i in range (len(self.a_inseriti)):
                         for j in range (len(self.a_inseriti)):
                             if(self.a_inseriti[i]==self.a_inseriti[j] and i!=j):
                                 print('Errore: non è possibile inserire due volte lo stesso numero di massa. Il programma non è andato a buon fine.\n')
                                 sys.exit()
                                 
                     self.in_abb=input("Inserisci la percentuale di abbondanza del numero di massa presente nel composto: ")
                     self.in_abb_int=float(self.in_abb)
                     if(self.in_abb_int>=0):
                         somma=somma+self.in_abb_int
                         if((somma)<=100):
                             self.abb_inserite=np.append(self.abb_inserite, float(self.in_abb))
                         else:
                             print('Errore: la somma delle percentuali inserite ha superato 100%. Il programma non è andato a buon fine.\n')
                             sys.exit()
                     else:
                         print('Errore: percentuale di abbondanza non può essere negativa. Non verrà registrato nemmeno il corrispettivo numero di massa inserito')
                         self.a_inseriti=self.a_inseriti[:-1]
                         
                 else:
                     print('Errore: hai inserito un valore di numero di massa non valido.')

        if(somma==100 and len(self.a_inseriti)==len(self.abb_inserite)):
            
            self.a_inseriti=(np.array(self.a_inseriti)).astype(int) # Faccio il casting per assicurarmi che siano array e non liste
            self.abb_inserite=np.array(self.abb_inserite)
            print('Inserimento andato a buon fine!')
            print('I numeri di massa acquisiti sono: ', self.a_inseriti)
            print('Le abbondanze %  acquisite sono: ', self.abb_inserite)
            print('\nPer ottenere le abbondanze isotopiche in natura (ottenibili solo per elementi presenti nel composto con tutti i loro isotopi) chiamare la funzione Get_Abbondanze_Isotopiche; mentre per visualizzare lo spettro di massa del composto (ottenibile anche per composti che non hanno tutti gli isotopi degli elementi nel composto) chiamare le funzione Spettro_Di_Massa\n')
        else:
            print('\nErrore: la somma delle percentuali inserite è minore di 100%. Il programma non è andato a buon fine.\n')
            sys.exit()


           
# Metodo che restituisce le abbondanze isotopiche dei numeri di massa degli elementi che hanno tutti gli isotopi presenti nel composto
            
    def Get_Abbondanze_Isotopiche(self):

        print('\nQuesta funzione permette di ottenere le abbondanze isotopiche in natura per gli elementi presenti nel composto con tutti i loro isotopi registrati nella tabella inziale!')
        self.elementi_presenti=get_elemento(self.a_inseriti, elementi_ar)
        if(len(self.elementi_presenti)!=0):
            return_abbondanze=np.zeros(1) ###
            return_abbondanze=return_abbondanze[:-1] ###
            for i in range (len(self.elementi_presenti)):
                print('Elemento con tutti gli isotopi presenti nel composto: ', self.elementi_presenti[i].nome)
                print('I numeri di massa degli isotopi dell elemento ', self.elementi_presenti[i].nome, ' sono: ', self.elementi_presenti[i].array_isotopi )
                print('Le corrispettive abbondanze in natura degli isotopi dell elemento ', self.elementi_presenti[i].nome, ' sono: ', self.elementi_presenti[i].array_abbondanze )
                return_abbondanze=np.append(return_abbondanze, self.elementi_presenti[i].array_abbondanze) ###
            print('\n')
            self.elementi_presenti[0].Tabella_Elementi_Isotopi_Abbondanze(self.elementi_presenti)
            print('\n')
            return return_abbondanze
        
        else:
            print('Per nessun elemento del composto sono presenti tutti gli isotopi\n')
            return None


            
# Metodo che realizza lo spettro di massa cioè un diagramma a barre A-Abbondanza %
            
    def Spettro_Di_Massa(self):

        #a_inseriti_ordine=np.sort(self.a_inseriti)
        #massimo=a_inseriti_ordine[-1]
        #scala_x=(np.arange(1, massimo+1).astype(int))
        print('\nSpettro di massa di Spettrometro TOF Composto: diagramma a barre A-Abbondanza %')
        col=input('Inserisci un colore tra i seguenti:\n-red\n-coral\n-salmon\n-sienna\n-darkorange\n-yellow\n-limegreen\n-darkgreen\n-aqua\n-darkblue\n-darkviolet\n-purple\n-hotpink\n')
        plt.figure(figsize=(12, 6))
        plt.bar(self.a_inseriti, self.abb_inserite, color=col)
        plt.title('Spettro di massa', fontsize=15, color=col)
        plt.xlabel('Numero di massa', fontsize=12)
        plt.ylabel('Abbondanze % nel composto', fontsize=12)
        plt.xticks(self.a_inseriti)
        #plt.savefig('diagramma-a-barre.png')
        plt.show()
        print('\n')
            

       
                















































