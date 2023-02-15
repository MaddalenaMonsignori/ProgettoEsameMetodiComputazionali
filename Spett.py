import numpy as np
import math
import sys
import matplotlib.pyplot as plt





############### VALORI UTILI

q=1.602176634*(10**(-19)) # + carica elettrone

massa_p_n= (1.67262192369*(10**(-27))+1.674927351*(10**(-27)))/2 #MEDIA DELLA MASSA IN KG DEI PROTONI E NEUTRONI





############### FUNZIONI UTILI

# La funzione troncamento immagina che lo spettrometro adatti i valori di numeri di massa in ingresso alla risoluzione mediante l'operazione di troncamento. Immagino che lo spettrometro non riesca a rilevare particelle che arrivano in tempi minori della risoluzione sui tempi delta_t e che i numeri di massa corrispondenti a queste particelle vengano scartati. Visto che la risoluzione dei tempi è direttamente proporzionale a quella delle masse che è a sua volta direttamente proporzionale a quella del numero di massa, eseguo il troncamento sui numeri di massa così che risulti conseguentemente sui tempi di volo

def troncamento(arr, risol):
    
    a_troncati=np.zeros(1)
    a_troncati=a_troncati[:-1] # L'array finale delle masse a_troncamenti che tiene conto della risoluzione rrisol(delta_a) --> a differenza del caso precedente non so a priori che dimensione abbia. Lo setto inzialmente vuoto

#Mediante un ciclo for valuto se i numeri di massa in input siano più o meno distanti della risoluzione dello strumento risol(delta_a). Nel caso un numero di massa disti dal successivo meno della risoluzione allora lo spettrometro non lo vede, altrimenti si
    for i in range(len(arr)):
        if i==0: # Il primo numero di massa è sempre rilevato dallo spettrometro
            a_troncati= np.append(a_troncati, arr[i])
        else:
            if(abs(arr[i]-arr[i-1])>=risol):
                a_troncati=np.append(a_troncati, arr[i])
    return a_troncati



# La funzione arrotondamento immagina che lo spettrometro adatti i valori di numeri di massa in ingresso alla risoluzione mediante l'operazione di arrotondamento. Immagino lo spettrometro come uno strumento a tacche per la misura della massa

def arrotondamento(aarr, rrisol):

    s=len(aarr)
    aarr_ordine=np.sort(aarr) #Ordino in ordine crescente i numeri di massa
    print('I numeri di massa ordinati sono: ', aarr_ordine)
    
# Immagino il mio spettrometro come uno strumento a tacche, dove la risoluzione coincide con la tacca. L'array tacche contiene i valori di tutte le tacche presenti cioè tutti i valori da 1 a 210(211 non è incluso in quanto ultimo estremo) e ha intervallo pari alla risoluzione del numero di massa rrisol (delta_a). Questo servirà per poter procedere all'arrotondamento dei valori dei numeri di massa in input così che siano coerenti con la risoluzione del mio spettrometro

    tacche=np.arange(1, 211, rrisol)
    print('Le tacche disponibili sono: ', tacche)
#L'array finale delle masse a_arrotondamenti che tiene conto della risoluzione rrisol(delta_a) ha dimensione pari a quella dell'array in input aarr. Lo setto inzialmente come array di tutti zeri per comodità    
    a_arrotondati=np.zeros(s)
    
#Mediante 2 cicli for indentati confronto i valori dei numeri di massa in input con quelli delle tacche dello strumento e arrotondandone opportunamente i valori e assegnandogli la corrispettiva tacca di tacche. Se il numero di massa coincide con il valore di una tacca gli viene assegnata la stessa mentre se il numero di massa generato è tra due tacche verrà arrotondato alla tacca precedente o successiva in base al suo valore assoluto. Il risultato finale dei numeri di massa approssimati viene salvato in a_arrotondati

    for i in range(s):
        for j in range(len(tacche)):
            if(abs(aarr_ordine[i]-tacche[j])<=rrisol):
                    if(j!=len(tacche)-1):
                        if(abs(aarr_ordine[i]-tacche[j])<abs(aarr_ordine[i]-tacche[j+1])):
                            a_arrotondati[i]=tacche[j]
                            #print('1')
                            break
            
                        elif(abs(aarr_ordine[i]-tacche[j])>=abs(aarr_ordine[i]-tacche[j+1])):
                            m=j+1
                            a_arrotondati[i]=tacche[m]
                            #print('2')
                            break
                    elif(j==len(tacche)-1): #visto che scorro fino all'indice dell'ultimo elemento di tacche devo trattare separatamente il caso in cui j è pari all'ultimo indice (se non facessi così riacadrei nelle 2 condizioni sopra dove devo fare il confronro con il j+1simo elemento che in questo caso non ho)
                        a_arrotondati[i]=tacche[j]
                        #print('3')
                        break
    return a_arrotondati



# La funzione round_num_prima_cifra_non_nulla approssima un numero decimale non noto alla prima cifra decimale non nulla 

def round_num_prima_cifra_non_nulla(numero):
    
    cifre_decimali= -int(math.floor(math.log10(numero))) +1 #calcolo la posizione della prima cifra decimale non nulla facendo il logaritmo in base 10 del numero, arrotondandone il risulato all'intero inferiore con math.floor, cambiandogli segno (log di numeri tra 0 e 1 è negativo) e sommandogli 1
    return round(numero, cifre_decimali)



# La funzione round_array_prima_cifra_non_nulla approssima gli elementi di un array non noto alla prima cifra decimale non nulla --> mi serve principalmente per arrotondare array_masse e array_tempi che sono (anche per A massimo=210) valori compresi tra 0 e 1 e in cui la prima cifra decimale non nulla occupa una posizione variabile

def round_array_prima_cifra_non_nulla(array):
    
    cifre_decimali= -int(np.floor(np.log10(array))) +1
    return np.round(array, cifre_decimali)



# La funzione è_un_array_o_int prende in input un parametro; se il parametro in input è un array restituisce True, se il parametro in input è un intero restituisce False, e se il parametro in input non è nè array nè int restituisce un messaggio di errore ed esce dal programma 

def è_un_array_o_int(parametro_input):
    if(type(parametro_input)==np.ndarray):
        return True
    elif(type(parametro_input)==int):
        return False
    else:
        print('Errore è_un_array_o_int: inserire o un array o un numero intero')
        sys.exit()

        


        
############### CLASSE SpettrometroTOF --> spettrometro di massa TOF che analizza ioni con numeri di massa generati random da 1 a 210 o ioni con numeri di massa inseriti tramite array

'''   
Definisco il costruttore dello spettrometro inizializzando i valori di:
-L
-V
-delta_a: risoluzione del numero di massa/errore sul numero di massa
-arr_int: è o numero di particelle in ingresso nel caso in cui si richieda una generazione random dei numeri di massa, o l'array che contiene i numeri di massa nel caso in cui si proceda per inserimento diretto
-at: il tipo di operazione utilizzato per calcolare la risoluzione sul numero di massa.
Nel caso in cui arr_int sia un intero il costruttore genera casualmente i numeri di massa A delle particelle che entrano nello spettrometro (e quindi anche le masse) adattandoli compatibilmente alla risoluzione dello strumento delta_a secondo l'operazione scelta (arrotondamento/troncamento).
Nel caso in cui arr_int sia un array il costruttore addatta i valori di quest'ultimo compatibilmente alloa risoluzione dello strumento delta_a secondo l'oeprazione scelta(arrotondamento/troncamento)
A partire dalla risoluzione del numero di massa delta_a, ricavo sia la risoluzione sulla massa delta_m sia la risoluzione sul tempo delta_t con la propagazione degli errori (formula derivate parziali)
Visto che per ipotesi le particelle che entrano nello spettrometro hanno carica +e il costruttore mi genera un array contenente n_part valori di carica+e.
'''

class SpettrometroTOF():
    
    def __init__(self, L, V, delta_a, arr_int, artr):

        self.L=L
        self.V=V
        self.delta_a=delta_a
        self.arr_int=arr_int
        self.artr=artr


        if(è_un_array_o_int(self.arr_int)==True):
            self.a_in=self.arr_int
            self.n_part=len(self.a_in)
            self.tipo=('inserimento con array dei numeri di massa')
            self.sigla_tipo='inserimento'
            print('\nNUOVO SPETTROMETRO TOF con', self.tipo)
            print('\nI numeri di massa inseriti sono: ', self.a_in)

        elif(è_un_array_o_int(self.arr_int)==False):

            self.n_part=self.arr_int
            self.tipo=('generazione random dei numeri di massa')
            self.sigla_tipo='random'
            print('\nNUOVO SPETTROMETRO TOF: ', self.tipo)
            print('\nInizio simulazione masse...')
            self.a_in=(np.random.uniform(low=1, high=210, size=self.n_part)).astype(int) # Genero casualmete i numeri di massa interi
            print('I numeri di massa generati sono: ', self.a_in)
    

            
        if(self.artr=='ar'):
            self.a= arrotondamento(self.a_in, self.delta_a)
            self.operazione='arrotondamento'
        elif(self.artr=='tr'):
            self.a=troncamento(self.a_in, self.delta_a)
            self.n_part=len(self.a)
            self.operazione='troncamento'
        else:
            print('\nInserire come quinto parametro ar (arrotondamento)/ tr (troncamento)\n')
            sys.exit()
            
        print('\nI numeri di massa secondo la sensibilità spettrometro, regolati per', self.operazione, ', sono: ', self.a)

        
        self.array_delta_a=(np.ones(self.n_part))*self.delta_a # Array con errori su numero di massa
        self.delta_m=self.delta_a*massa_p_n # Per calcolare l'errore sulla massa delta_m uso la propagazione degli errori con la formula delle derivate parziali in cui considero la massa_p_n un numero esatto
        self.array_delta_m=(np.ones(self.n_part))*self.delta_m #Array con errori su masse
        
        self.array_masse=self.a*massa_p_n # Si ottiene moltiplicando il numero di massa(protoni+neutroni) per la massa dei protoni/neutroni
        print('\nArray masse in Kg è: ', self.array_masse)
        
        self.array_q=(np.ones(self.n_part))*q # Visto che gli ioni sono tutti carichi +e l'array delle cariche avrà tutti valori uguali pari a +e
        print('\nLe cariche in Coulomb sono: ', self.array_q)
        
        self.array_tempi=np.sqrt((self.array_masse*(self.L)**2)/(2*self.V*q))
        print('\nArray dei tempi in s è: ', self.array_tempi)
        self.delta_t=0.5*math.sqrt((self.L)**2/(2*self.V*q))*((self.array_masse)**(-1/2))*(self.delta_m) # Per calcolare l'errore sul tempo delta_t (È UN ARRAY) uso la fomrula della propagazione degli errori con le derivate parziali dove L, V, q li considero come valori esatti (infatti L, V visto che costruisco io il mio sistema li sceglierò con errori di oridini di grandezza molto più piccoli che non vanno a incidere su misura finale)
        print('\nGli errori sull array dei tempi sono: ', self.delta_t)
        
        print('\nPer visualizzare i metodi della classe disponibili chiamare Metodi_disponibili_TOF\n' )


        
# Metodo che grafica A in funzione di t con errori sia su A sia su t

    def GraficoTOF_A_t(self):

        print('\nGrafico A-t spettrometro TOF', self.tipo, 'con', self.operazione)
        plt.figure(figsize=(12, 6))
        col=input('Inserisci un colore tra i seguenti:\n-red\n-coral\n-salmon\n-sienna\n-darkorange\n-yellow\n-limegreen\n-darkgreen\n-aqua\n-darkblue\n-darkviolet\n-purple\n-hotpink\n')
        titolo='Spettrometro TOF '+self.sigla_tipo+' '+self.artr+': A-t'
        plt.errorbar(self.a, self.array_tempi, xerr=self.array_delta_m,yerr=self.delta_t, fmt='o', color=col, ecolor='grey', label='ΔA={}'.format(self.delta_a))
        plt.title(titolo, fontsize=15, color=col)
        plt.xlabel('Numero di massa', fontsize=12)
        plt.ylabel('Tempi di volo particelle [s]', fontsize=12)
        plt.legend(fontsize=14)
        #plt.savefig(titolo+'.png')
        plt.show()
        print('\n')

        

# Metodo che grafica m in funzione di t con errori sia su m che su t

    def GraficoTOF_m_t(self):

        print('\nGrafico m-t Spettrometro TOF', self.tipo, 'con', self.operazione)
        plt.figure(figsize=(12, 6))
        col=input('Inserisci un colore tra i seguenti:\n-red\n-coral\n-salmon\n-sienna\n-darkorange\n-yellow\n-limegreen\n-darkgreen\n-aqua\n-darkblue\n-darkviolet\n-purple\n-hotpink\n')
        plt.errorbar(self.array_masse, self.array_tempi, xerr=self.array_delta_m, yerr=self.delta_t, fmt='o', ecolor='grey', color=col, label='ΔA={}'.format(self.delta_a))
        titolo='Spettrometro TOF '+self.sigla_tipo+' '+self.artr+': m-t'
        plt.title(titolo, fontsize=15, color=col)
        plt.xlabel('Masse particelle [Kg]', fontsize=12)
        plt.ylabel('Tempi di volo particelle [s]', fontsize=12)
        plt.legend(fontsize=14)
        #plt.savefig(titolo+'.png')
        plt.show()
        print('\n')


        
# Metodo che fa i subplots di più Spettrometri TOF

    def SubplotsTOF_m_t (self, array_oggetti, titolo_complessivo): # Il metodo prende in input un array di oggetti (array_oggetti) della classe

        print('\nSubplots di più spettrometri TOF: m-t\n')
        if(len(array_oggetti)%2==0): # Se l'array_oggetti ha lunghezza pari allora dispongono i subplots a griglia (colonne della griglia sono un numero uguale alla metà della lunghezza dell'array mentre le righe della griglia sono in un numero uguale a lunghezza dell'array diviso il numero di colonne )
            colonne=int((len(array_oggetti)/2))
            righe=int(len(array_oggetti)/colonne)
            fig, ax =plt.subplots(righe , colonne, figsize=(12, 6))
            fig.suptitle(str(titolo_complessivo))
            ax=ax.flatten() # Restituisce una copia piatta dell'array multidimensionale ax (che ha come dimensioni righe, colonne del subplot) che contiene tutti i valori di ax riga per riga. Quindi ax finale sarà monodimensionale, così da poter compilare i plot del subplot con più facilità (quando ax era bidimensionale mi dava problemi)
        
        else:
            
            num_plots=len(array_oggetti) # Se l'array_oggetti ha lunghezza dispari allora dispongono i subplots tutti in un unica in colonna per comodità
            fig, ax = plt.subplots(num_plots, figsize=(10, 20))
            #ax=ax.flatten()

        # Creo un colormap di matplotlib
        cmap=plt.get_cmap("plasma")
        cmap1=plt.get_cmap("inferno")
        # Creo un oggetto ScalrMappable utilizzando il colormap cmap
        sm=plt.cm.ScalarMappable(cmap=cmap)
        sm1=plt.cm.ScalarMappable(cmap=cmap)
        # Creo i valori che corrispondono a colori diversi da mappare --> i valori consentiti sono solo tra 0 e 1 e per averne in un numero uguale alla lunghezza dell'array imposto come passo dell'intervallo 1/lunghezza array_oggetti
        value=np.arange(0, 1, 1/len(array_oggetti)) 
        value1=np.arange(0, 1, 1/len(array_oggetti))
        # Mappo i valori numerici di value/value1 con i colori contenuti nell'array color/color1--> questo mi permette che i grafici dei subplots e gli errori dei subplots abbiano ciascuno un colore diverso
        color=sm.to_rgba(value)
        color1=sm1.to_rgba(value1)

            
        for i, obj in enumerate(array_oggetti):# Enumerate mi crea una tupla costituita da coppie di elementi (indice, oggetto) dove per  ogni elemento oggetto dell'array array_oggetti, i rappresenta l'indice corrente dell'elemento nella lista, mentre obj rapprensenta l'elemento corrente. Quindi con questo ciclo for scorro contemporaneamente sull'indice e e su obj
                
            ax[i].errorbar(obj.array_masse, obj.array_tempi, xerr=obj.array_delta_m, yerr=obj.delta_t, fmt='o', ecolor=color1[i],color=color[i],label='Δm={}'.format(round_num_prima_cifra_non_nulla(obj.delta_m)))
            titolo='TOF '+obj.sigla_tipo+' '+obj.artr+': m-t'
            ax[i].set_title(titolo, fontsize=13, color=color[i])
            ax[i].set_xlabel('Massa particelle [Kg]')
            ax[i].set_ylabel('Tempi di volo particelle[s]')
            ax[i].legend()
            #plt.tight.
            
        #plt.savefig('Subplots-m-t.png')
        plt.show()

        

# Metodo che fa i subplots di più Spettrometri TOF

    def SubplotsTOF_A_t (self, array_oggetti, titolo_complessivo): # Il metodo prende in input un array di oggetti (array_oggetti) della classe

        print('\nSubplots di più spettrometri TOF: A-t\n')
        if(len(array_oggetti)%2==0): # Se l'array_oggetti ha lunghezza pari allora dispongono i subplots a griglia (colonne della griglia sono un numero uguale alla metà della lunghezza dell'array mentre le righe della griglia sono in un numero uguale a lunghezza dell'array diviso il numero di colonne )
            colonne=int((len(array_oggetti)/2))
            righe=int(len(array_oggetti)/colonne)
            fig, ax =plt.subplots(righe , colonne, figsize=(12, 6))
            fig.suptitle(str(titolo_complessivo))
            ax=ax.flatten() # Restituisce una copia piatta dell'array multidimensionale ax (che ha come dimensioni righe, colonne del subplot) che contiene tutti i valori di ax riga per riga. Quindi ax finale sarà monodimensionale, così da poter compilare i plot del subplot con più facilità (quando ax era bidimensionale mi dava problemi)
        
        else:
            
            num_plots=len(array_oggetti) # Se l'a'TOF Δm={}rray_oggetti ha lunghezza dispari allora dispongono i subplots tutti in un unica in colonna per comodità
            fig, ax = plt.subplots(num_plots, figsize=(10, 20))
            #ax=ax.flatten()

        # Creo un colormap di matplotlib
        cmap=plt.get_cmap("plasma")
        cmap1=plt.get_cmap("inferno")
        # Creo un oggetto ScalrMappable utilizzando il colormap cmap
        sm=plt.cm.ScalarMappable(cmap=cmap)
        sm1=plt.cm.ScalarMappable(cmap=cmap)
        # Creo i valori che corrispondono a colori diversi da mappare --> i valori consentiti sono solo tra 0 e 1 e per averne in un numero uguale alla lunghezza dell'array imposto come passo dell'intervallo 1/lunghezza array_oggetti
        value=np.arange(0, 1, 1/len(array_oggetti)) 
        value1=np.arange(0, 1, 1/len(array_oggetti))
        # Mappo i valori numerici di value/value1 con i colori contenuti nell'array color/color1--> questo mi permette che i grafici dei subplots e gli errori dei subplots abbiano ciascuno un colore diverso
        color=sm.to_rgba(value)
        color1=sm1.to_rgba(value1)
        

            
        for i, obj in enumerate(array_oggetti):# Enumerate mi crea una tupla costituita da coppie di elementi (indice, oggetto) dove per  ogni elemento oggetto dell'array array_oggetti, i rappresenta l'indice corrente dell'elemento nella lista, mentre obj rapprensenta l'elemento corrente. Quindi con questo ciclo for scorro contemporaneamente sull'indice e e su obj
                
            ax[i].errorbar(obj.a, obj.array_tempi, xerr=obj.array_delta_a, yerr=obj.delta_t, fmt='o', ecolor=color1[i], color=color[i], label='ΔA={}'.format(round_num_prima_cifra_non_nulla(obj.delta_a)))
            titolo='TOF '+obj.sigla_tipo+' '+obj.artr+': A-t'
            ax[i].set_title(titolo, fontsize=13, color=color[i])
            ax[i].set_xlabel('Numero di massa')
            ax[i].set_ylabel('Tempi di volo particelle[s]')
            ax[i].legend()
            #plt.tight.
            
        #plt.savefig('Subplots-A-t.png')
        plt.show()


        
# Metodo che mi stampa i metodi disponibili della classe

    def Metodi_disponibili_TOF(self):
        print('\nNella classe SpettrometroTOF è possibile chiamare i seguenti metodi \n0) Metodi_disponibili_TOF: restituisce i metodi della classe disponibili \n1) GraficoTOF_A_t: grafica il tempo di volo in funzione del numero di massa delle particelle \n2) GraficoTOF_m_t: grafica tempo di volo in funzione della massa delle particelle \n3) SubplotsTOF_m_t: fa subplots del tempo di volo in funzione della massa per più spettrometri \n4) SubplotsTOF_A_t: fa subplots del tempo di volo in funzione del numero di massa per più spettrometri \n')
    
