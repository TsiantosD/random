#Θέμα Δ
EP = []
ON = []
ALMA1 = []
ALMA2 = []
XWRA = []
SYN = []
bathmologia_germanias = 0
megalyterh_bathmologia = 0
thesh = -1
plhthos = 0 #Πλήθος ατόμων με καλήτερη επίδοση στο 2ο άλμα

#Δ1 - Δ2
for i in range(80): 
    eponymo = input("Επίθετο: ")
    onoma = input("Όνομα: ")
    alma1 = int(input("Βαθμολογία πρώτου άλματος: "))
    alma2 = int(input("Βαθμολογία δεύτερου άλματος: "))
    xwra = input("Χώρα: ")

#Δ3
    EP.append(eponymo)
    ON.append(onoma)
    ALMA1.append(alma1)
    ALMA2.append(alma2)
    XWRA.append(xwra)

#Δ4
    synolo = alma1 + alma2 
    SYN.append(synolo)

#Δ5
    if xwra == "ΓΕΡΜΑΝΙΑ":
        bathmologia_germanias = bathmologia_germanias + synolo
        
   
#Δ6        
    if megalyterh_bathmologia < synolo:
        megalyterh_bathmologia = synolo
        thesh = i

#Δ7
    if alma2 > alma1:
        plhthos += 1

print(EP, ON, ALMA1, ALMA2, XWRA, SYN)
print("Συνολική βαθμολογία της Γερμανίας: ", bathmologia_germanias)
print("Αθλητής με την μεγαλύτερη βαθμολογία: ", EP[thesh])
print("Νούμερο αθλητών με καλύτερη επίδοση στο 2ο άλμα: ", plhthos)
