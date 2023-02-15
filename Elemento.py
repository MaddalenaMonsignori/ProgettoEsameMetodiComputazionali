import numpy as np
import pandas as pd
import sys
import matplotlib as plt





############### La classe Elemento contiene le informazioni relative agli isopi di un elemento e alle corrispettive abbondanze

'''
Definisco il costruttore dell'elemento che, nel caso caso in cui non siano verificate le condizioni di uscita anticipata dal programma, inizializza i valori di:
-nome: nome elemento
-array_isotopi: array contenente i numeri di massa dei vari isotopi dell'elemento
-array_abbondanze: array contenente le rispettive abbondanze isotopiche dei numeri di massa dell'elemento
-array_nomi: array che contiene il nome dell'elemento un numero di volte pari al numero degli isotopi
Se si verificano i seguenti casi il programma si interrompe e termina in anticipo:
-il numero di numeri di massa è diverso dal numero dal numero di abbondanze
-i numeri di massa inseriti non sono compreso tra 1 e 210(inclusi)
-è presente 2 volte lo stesso numero di massa
-la percentuale di abbondanza di un certo numero di massa è negativa
-la somma finale di tutte le percentuali dei numeri di massa inseriti è diversa da 100%

'''

class Elemento():

    
    def __init__(self, nome, array_isotopi, array_abbondanze):

        
        if(len(array_isotopi)!=len(array_abbondanze)):
            print('Errore: hai inserito un numero di isotopi diverso dal numero di abbondanze. Il programma si interromperà.')
            sys.exit()

        for j in (array_isotopi):
            if(j<0 or j>210):
                print('Errore: hai inserito un valore di numero di massa non valido. Il programma si interromperà')
                sys.exit()
                
        for l in range (len(array_isotopi)):
             for m in range (len(array_isotopi)):
                if(array_isotopi[l]==array_isotopi[m] and l!=m):
                    print('Errore: non è possibile avere due volte lo stesso numero di massa. Il programma si interromperà.\n')
                    sys.exit()
            
        somma=0
        for i in (array_abbondanze):
            if(i<0):
                print('Errore: percentuale di abbondanza non può essere negativa. Il programma si interromperà')
                sys.exit()
            somma=somma+i
            
        if(somma!=100):
               print('Errore: la somma delle percentuali non è 100. Il programma si interromperà.')
               sys.exit()

        self.nome=nome
        self.array_isotopi=array_isotopi.astype(int)
        self.array_abbondanze=array_abbondanze.astype(float)
        self.array_nomi=np.full(len(array_isotopi), self.nome)
      

#Metodo che restituisce informazioni su un elemento

    def Info_Elemento(self):
        
        print('\nNome elemento: ' , self.nome)
        print('Isotopi elemento: ', self.array_isotopi)
        print('Abbondanze isotopi %: ', self.array_abbondanze, '\n')


# Metodo che prende in input un array con tipo Elemento, stampa una tabella e la salva in file.csv. Le colonne della tabella contengono rispettivamente i nomi degli elementi, i numeri di massa degli isotopi degli elementi e le abbondanze isotopiche degli isotopi degli elementi
        
    def Tabella_Elementi_Isotopi_Abbondanze(self, array_elementi):

        array_tab_nomi=np.zeros(1)
        array_tab_isotopi=np.zeros(1)
        array_tab_abbondanze=np.zeros(1)
        tab_nomi=np.zeros(1)
        tab_nomi=tab_nomi[:-1]
        array_tab_nomi=array_tab_nomi[:-1]
        array_tab_isotopi=array_tab_isotopi[:-1]
        array_tab_abbondanze=array_tab_abbondanze[:-1]
     
        for i in range (len(array_elementi)):
        
            array_tab_nomi=np.append(array_tab_nomi, array_elementi[i].array_nomi)
            array_tab_isotopi=np.append(array_tab_isotopi, array_elementi[i].array_isotopi)
            array_tab_abbondanze=np.append(array_tab_abbondanze, array_elementi[i].array_abbondanze)

        
        mydf= pd.DataFrame(columns=['Elementi', 'Numeri di massa', 'Abbondanze isotopiche %'])
        mydf['Elementi']=array_tab_nomi
        mydf['Numeri di massa']=(array_tab_isotopi).astype(int)
        mydf['Abbondanze isotopiche %']=array_tab_abbondanze

        mydf.to_csv('Elementi-Isotopi-Abbondanze.csv', index=False)
        print(mydf)


