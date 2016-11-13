from random import randrange
from obesenec import obrazky

def vyber_slovo():

    cislo = randrange(0, 2)
    if cislo == 0:
        return 'filoména'
    elif cislo == 1:
        return 'mentolka'
    else:
        return 'estragon'

def ziskej_pismeno():
    while True:
        pismeno = input("Zadej pismeno: ")
        if len(pismeno) == 1:
            return pismeno
        else:
            print("Jenom 1 pismeno, potvoro.")
       
def hra():
    slovo = vyber_slovo()
    stav = len(slovo) * "_"
    chyb = 0
    while True:
        pismeno = ziskej_pismeno()
        try:
            pozice = slovo.index(pismeno)
            stav = zamen(stav, pozice, pismeno)
        except ValueError:
            chyb = chyb + 1
        print(stav)
        if vyhral(stav):
            print("Vyhrals")
            break
        print(obrazky[chyb])
        if len(obrazky) == chyb + 1:
            print("Prohrals")
            break
      
            
        
def zamen(retezec, pozice, znak):
    return (retezec[:pozice] + znak + retezec[pozice+1:])
    
def vyhral(retezec):
    if "_" not in retezec:
        return True
    else:
        return False
    
hra()
        

    
        


    

