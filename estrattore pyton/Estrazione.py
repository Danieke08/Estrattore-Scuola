import time
import random
imputati = []
risposta = False
lista_estratti = []
j = 1
imputati_file = open("imputati.txt", "a")

l_materie = ["matematica", "fisica","geostoria","inglese","italiano","scienze","latino"]          #Scrivi tutte le materie

for i in l_materie:
    file_scelto = open( i + ".txt", "r")                                                 #mette i contenuti di tutti i file in un array
    for k in file_scelto:
        imputati.append(k)
    file_scelto.close()

    
print("Per quale materia vuoi estrarre tra: 'matematica','fisica','gestoria','inglese','latino','italiano'e'scienze'")       #inserisci la materia per cui vuoi estrarre
materia = input("materia: ")
file = open( materia + ".txt", "r")


numero_estratti = int(input("quante persone vuoi estrarre? \n"))                            #quante persone vuoi estrarre

lista = []
for i in file:
    lista.append(i)    
        
while j <= numero_estratti:
    
    b = False
    
   
    while b == False:  
        n = random.randrange(0 , len(imputati))                             #esegue finchè il nome non si trova nella materia scelta
        
        
        for i in lista:                                                        #controlla che il nome estratto sia nell'array lista
            if i == imputati[n]:
                b = True        
                                                
    if imputati[n] not in lista_estratti:
        lista_estratti.append(imputati[n])
        j += 1
        print(imputati[n])
        imputati_file.write(imputati[n])
    time.sleep(random.random())
             
print(lista_estratti)
imputati_file.close()
file.close()


p = (len(lista_estratti)-1)
u = 0
while u <= p:
    rimuovi = input("Vuoi togliere lo/a sfigato/a "+ lista_estratti[u] +" dal file?\n")
    if rimuovi == "si":                                                                              
        lista.remove(lista_estratti[u])
        print("ok")
        risposta = True
        u += 1
    elif rimuovi == "no":
        print("ok")
        risposta = True
        u += 1
    else:
        print("scrivi 'si' o 'no' la prossima volta")



'''''''''''''''
while risposta == False:
    rimuovi = input("Vuoi togliere lo/a sfigato/a "+ imputati[n] +" dal file?\n")                    #puoi decidere di rimuovere la persona estratta dal file
    if rimuovi == "si":                                                                              #non ancora finito
        lista.remove(imputati[n])
        print("ok")
        risposta = True
    elif rimuovi == "no":
        print("ok")
        risposta = True
    else:
        print("scrivi 'si' o 'no' la prossima volta")


'''''




    
"""
if b == True:
    lista.remove(imputati[n])
    print(lista)
    open("Estrattore/" + i + ".txt", "w")
"""