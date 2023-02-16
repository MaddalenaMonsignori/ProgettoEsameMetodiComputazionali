# ProgettoEsameMetodiComputazionali

Il progetto è costituito da 3 classi principali SpettrometroTOF, SpettrometroTOF_Composti, Spettrometro_TOF_C_H_O rispettivamente appartenenti ai moduli 
Spett.py, SpettC.py, e Spett_C_H_O e da un unico Main contenuto nel file Main.py in cui vengono importati i suddetti moduli. Inoltre è stata definita 
anche una classe supporto, chiamata Elemento e presente nel modulo Elemento.py, che viene talvolta richiamata nel Main.py o dai moduli dei vari spettrometri..
Main.py è suddiviso in 3 sezioni delimitate dai costruitti if(True)/if(False) "sbloccabili" in modo tale da poter scegliere se analizzare separatamente le 
richieste del progetto assegnato o meno.

In particolare sbloccando il primo if(True) è possibile accedere alla prima parte del codice che lavora con oggetti di tipo SpettrometroTOF; la classe
SpettrometroTOF simula uno spettrometro di massa a tempo di volo che analizza ioni con numeri di massa generati random da 1 a 210 o ioni con numeri 
di massa inseriti tramite array in base al loro tempo di volo; è possibile settarne caratteristiche costruttive, risoluzione, modalità di calcolo della risoluzione.
Nel corrispettivo blocco del Main.py vengono definiti più oggetti SpettrometroTOF che analizzano gli stessi ioni in input ma a partire da 
risoluzione, e/o modalità di calcolo della risoluzione differenti; il confronto viene mostrato mediante vari plot e subplot del numero di massa in funzione del
tempo di volo delle particelle.

Sbloccando il secondo if(True) è possibile accedere alla seconda parte del codice che lavora con oggetti di tipo SpettrometroTOF_Composti;  la classe
SpettrometroTOF_Composti simula uno spettrometro di massa in cui è possibile inserire da console numeri di massa degli elementi presenti nel composto e 
la corrispettiva percentuale di abbondanza nel composto. Mediante il metodo Get_Abbondanze_Isotopiche è possibile ottenere le abbondanze isotopiche 
degli elementi che hanno tutti gli isotopi presenti nel composto, le quali vengono stampate a schermo e inserite in una tabella. Inoltre tramite il metodo
Spettro_Di_Massa è possibile ottenere un grafico a barre che sulle ascisse ha i numeri di massa e sulle ordinate l'abbondanza isotopica percentuale nel 
composto.

Sbloccando il terzo if(True) è possibile accedere all'ultima parte del codice che lavora con oggetti di tipo SpettrometroTOF_C_H_O;  la classe
SpettrometroTOF_C_H_O simula uno spettrometro di massa che analizza molecole del tipo CxHxOx in cui è possibile inserire da console il numero di atomi
per ciascun elemento presente. Il metodo Get_Abbondanza_H calcola tutte le possibili combinazioni (supponendo che gli atomi di C e O siano tutti C-12 e O-16)
, e le relative probabilità, in cui si possono presentare gli isotopi di H all'interno della molecola inserita mediante distribuzione binomiale, 
e ne restituisce le probabilità. 
I dati vengono stampati a schermo, visualizzati (e salvati in .csv) in una tabella in cui sono presenti anche i numeri di massa e le masse della molecola 
per ogni combinazione di isotopi di H e rappresentati (e salvati .png) mediante lo spettro di massa che grafica in un diagramma a barre 
i numeri di massa della molecola in funzione della probabilità
