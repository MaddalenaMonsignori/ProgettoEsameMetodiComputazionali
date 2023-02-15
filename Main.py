import Spett as s
import Elemento as el
import SpettC as sc
import Spett_C_H_O as scho
import numpy as np
import math
import matplotlib.pyplot as plt




############### MAIN 1

if(True):
    L=1.5 # Lunghezza di volo tipica dei TOF
    v=15000 # Differenza di potenziale nel TOF
    npar=100 # Numero ioni nel TOF

# Definisco un oggetto più oggetti di tipo SpettrometroTOF del modulo Spett a cui assegno stessa L, stesso potenziale V, stessi numeri di massa (il primo speottrometro genera casualmente npar numeri di massa e gli stessi numeri di massa vengono assegnati anche agli altri spettrometri), stessa operazione di calcolo della risoluzione (arrotondamento/troncamento) ma diversa risoluzione del numero di massa delta_a. Ripeto il confronto sia per risoluzione dello numero di massa calcolata con l'arrotondamento sia per risoluzione dello numero di massa con il troncamento

# ARROTONDAMENTO
        
    Spett1= s.SpettrometroTOF(L, v, 1, npar, 'ar')
    Spett1.Metodi_disponibili_TOF()

# Immagazzino gli attributi degli oggetti in array per comodità

    aa=Spett1.a_in
    a1=Spett1.a
    m1=Spett1.array_masse
    t1=Spett1.array_tempi
    errt1=Spett1.delta_t
    erra1=Spett1.array_delta_a


    Spett2=s.SpettrometroTOF(L, v, 2, aa, 'ar')
    Spett3=s.SpettrometroTOF(L, v, 3, aa, 'ar')
    Spett4=s.SpettrometroTOF(L, v, 4, aa, 'ar')
    Spett5=s.SpettrometroTOF(L, v, 5, aa, 'ar')
    Spett10=s.SpettrometroTOF(L, v, 10, aa, 'ar')


    a2=Spett2.a
    t2=Spett2.array_tempi
    errt2=Spett2.delta_t
    erra2=Spett2.array_delta_a
    a3=Spett3.a
    t3=Spett3.array_tempi
    errt3=Spett3.delta_t
    erra3=Spett3.array_delta_a
    a4=Spett4.a
    t4=Spett4.array_tempi
    errt4=Spett4.delta_t
    erra4=Spett4.array_delta_a
    a5=Spett5.a
    t5=Spett5.array_tempi
    errt5=Spett5.delta_t
    erra5=Spett5.array_delta_a
    a10=Spett10.a
    t10=Spett10.array_tempi
    errt10=Spett10.delta_t
    erra10=Spett10.array_delta_a

# Grafico A-t di tutti gli spettrometri INSIEME con risoluzione diversa che utilizzano l'arrotondamento

    plt.errorbar(a1, t1, xerr=erra1,  yerr=errt1, fmt='o', color='red', label='ΔA=1')
    plt.errorbar(a2, t2, xerr=erra2, yerr=errt2, fmt='o', color='yellow', label='ΔA=2')
    plt.errorbar(a3, t3, xerr=erra3, yerr=errt3, fmt='o', color='limegreen', label='ΔA=3')
    plt.errorbar(a4, t4, xerr=erra4, yerr=errt4, fmt='o', color='skyblue', label='ΔA=4')
    plt.errorbar(a5, t5, xerr=erra5, yerr=errt5, fmt='o',  color='pink', label='ΔA=5')
    plt.errorbar(a10, t10, xerr=erra10, yerr=errt10, fmt='o', color='darkviolet', label='ΔA=10')
    tit='Spettrometri TOF '+Spett1.operazione+': A-t'
    plt.title(tit, fontsize=15)
    plt.xlabel('Numeri di massa', fontsize=12)
    plt.ylabel('Tempi di volo particelle [s]', fontsize=12)
    plt.legend(fontsize=14)
    plt.savefig('Plot-complessivo-A-t-con-ar.png')
    plt.show()
    
# Subplot A-t di spettrometri con risoluzione diversa che utilizzano l'arrotondamento

    ArSp=np.array([Spett1, Spett2, Spett3, Spett4, Spett5, Spett10])

    Spett1.SubplotsTOF_A_t(ArSp, "Spettrometri con arrotondamento e risoluzione diversa")

    #Spett1.SubplotsTOF_m_t(ArSp, "Spettrometri con arrotondamento e risoluzione diversa")



# TRONCAMENTO

    Spett01= s.SpettrometroTOF(L, v, 1, aa, 'tr')

# Immagazzino gli attributi degli oggetti in array per comodità

    a01=Spett01.a
    t01=Spett01.array_tempi
    errt01=Spett01.delta_t
    erra01=Spett01.array_delta_a


    Spett02=s.SpettrometroTOF(L, v, 2, aa, 'tr')
    Spett03=s.SpettrometroTOF(L, v, 3, aa, 'tr')
    Spett04=s.SpettrometroTOF(L, v, 4, aa, 'tr')
    Spett05=s.SpettrometroTOF(L, v, 5, aa, 'tr')
    Spett010=s.SpettrometroTOF(L, v, 10, aa, 'tr')

    a02=Spett02.a
    t02=Spett02.array_tempi
    errt02=Spett02.delta_t
    erra02=Spett02.array_delta_a
    a03=Spett03.a
    t03=Spett03.array_tempi
    errt03=Spett03.delta_t
    erra03=Spett03.array_delta_a
    a04=Spett04.a
    t04=Spett04.array_tempi
    errt04=Spett04.delta_t
    erra04=Spett04.array_delta_a
    a05=Spett05.a
    t05=Spett05.array_tempi
    errt05=Spett05.delta_t
    erra05=Spett05.array_delta_a
    a010=Spett010.a
    t010=Spett010.array_tempi
    errt010=Spett010.delta_t
    erra010=Spett010.array_delta_a

# Grafico A-t di tutti gli spettrometri INSIEME con risoluzione diversa che utilizzano il troncamento

    plt.errorbar(a01, t01, xerr=erra01,  yerr=errt01, fmt='o', color='red', label='ΔA=1')
    plt.errorbar(a02, t02, xerr=erra02, yerr=errt02, fmt='o', color='yellow', label='ΔA=2')
    plt.errorbar(a03, t03, xerr=erra03, yerr=errt03, fmt='o', color='limegreen', label='ΔA=3')
    plt.errorbar(a04, t04, xerr=erra04, yerr=errt04, fmt='o', color='skyblue', label='ΔA=4')
    plt.errorbar(a05, t05, xerr=erra05, yerr=errt05, fmt='o',  color='pink', label='ΔA=5')
    plt.errorbar(a010, t010, xerr=erra010, yerr=errt010, fmt='o', color='darkviolet', label='ΔA=10')
    tit0='Spettrometri TOF '+Spett01.operazione+': A-t'
    plt.title(tit0, fontsize=15)
    plt.xlabel('Numero di massa', fontsize=12)
    plt.ylabel('Tempi di volo particelle [s]', fontsize=12)
    plt.legend(fontsize=14)
    plt.savefig('Plot-complessivo-A-t-con-tr.png')
    plt.show()
    

# Subplot A-t di spettrometri con risoluzione diversa che utilizzano il troncamento

    ArSp0=np.array([Spett01, Spett02, Spett03, Spett04, Spett05, Spett010])

    Spett01.SubplotsTOF_A_t(ArSp0, "Spettrometri con troncamento e risoluzione diversa")
    
    #Spett01.SubplotsTOF_m_t(ArSp0, "Spettrometri con troncamento e risoluzione diversa")

    

# Confronto gli spettrometri che prendono in input gli stessi numeri di massa, hanno stessa risoluzione, ma operano con arrotondamento o troncamento. In particolare si evidenzia il confronto nel caso della risoluzione più piccola, ΔA=1, e nel caso della risoluzione più grande, ΔA=10

    ArSp00=np.array([Spett1, Spett01, Spett10, Spett010])

    Spett1.SubplotsTOF_A_t(ArSp00, "Spettrometri arrotondamento-troncamento a confronto")

    #Spett1.SubplotsTOF_m_t(ArSp00, "Spettrometri arrotondamento-troncamento a confronto")



# Per gli isotopi del carbonio e del cloro mostro i diversi risultati di spettrometria per risoluzioni diverse sia per arrotondamento che per troncamento
    C= el.Elemento('C', np.array([12, 13]), np.array([98.893, 1.107]))
    Cl= el.Elemento('Cl', np.array([35, 37]), np.array([75.77, 24.23]))

    SpettC1= s.SpettrometroTOF(L, v, 1, C.array_isotopi, 'ar')
    SpettC01= s.SpettrometroTOF(L, v, 1, C.array_isotopi , 'tr')
    SpettC10= s.SpettrometroTOF(L, v, 10, C.array_isotopi, 'ar')
    SpettC010= s.SpettrometroTOF(L, v, 10, C.array_isotopi, 'tr')


    ArSpC= np.array([SpettC1, SpettC01, SpettC10, SpettC010])

    SpettC1.SubplotsTOF_A_t(ArSpC, "Isotopi Carbonio visualizzati con spettrometri diversi")

    SpettCl1= s.SpettrometroTOF(L, v, 1, Cl.array_isotopi, 'ar')
    SpettCl01= s.SpettrometroTOF(L, v, 1, Cl.array_isotopi , 'tr')
    SpettCl10= s.SpettrometroTOF(L, v, 10, Cl.array_isotopi, 'ar')
    SpettCl010= s.SpettrometroTOF(L, v, 10, Cl.array_isotopi, 'tr')

    ArSpCl= np.array([SpettCl1, SpettCl01, SpettCl10, SpettCl010])
    SpettCl1.SubplotsTOF_A_t(ArSpCl, "Isotopi Cloro visualizzati con spettrometri diversi")





############### MAIN 2

# Definisco 2 oggetti SpettrometroTOF_Composti del modulo SpettC. Da console inserisco rispettivamente i seguenti dati:
#-K-39 93%; K-41 7%
#-Be-9 10%; O-16 62%; Al-27 7%; Si-28 19%; Si-29 1%; Si-30 0.6%; Cr-52 0.36%; Cr-53 0.04%
#Per ciascuno dei 2 oggetti chiamo i metodi:
#-Get_Abbondanze_Isotopiche: restituisce le abbondanze isotopiche dei numeri di massa degli elementi che hanno tutti gli isotopi presenti nel composto
#-Spettro_Di_Massa: realizza lo spettro di massa cioè un diagramma a barre A-Abbondanza %


if(False):
    
    Spet1=sc.SpettrometroTOF_Composti()
    Abb1=Spet1.Get_Abbondanze_Isotopiche()
    Spet1.Spettro_Di_Massa()

    Spet2=sc.SpettrometroTOF_Composti()
    Abb2=Spet2.Get_Abbondanze_Isotopiche()
    Spet2.Spettro_Di_Massa()




############### MAIN 3

# Definisco 2 oggetti SpettrometroTOF_C_H_O del modulo Spett_C_H_O. Da console inserisco rispettivamente i seguenti dati:
#-C6H8O6
#-C28H44O
# Per ciascuno dei 2 oggetti chiamo il metodo:
#-Get_Abbondanza_H: restituisce le probabilità di ogni combinazione possibile di isotopi di H nella molecola

if (False):
    
    Sp1=scho.SpettrometroTOF_C_H_O()
    Prob1=Sp1.Get_Abbondanza_H()

    Sp2=scho.SpettrometroTOF_C_H_O()
    Prob2=Sp2.Get_Abbondanza_H()
























