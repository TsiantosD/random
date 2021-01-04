#Θέμα Δ
EP = []
ON = []
ALMA1 = []
ALMA2 = []
XWRA = []
SYN = []
bathmologia_germanias = 0
KALYTERH_EPIDOSH = [] #atoma poy eixan megalyterh bathmologia sto 2o alma

for i in range(80):
    eponymo = raw_input("Επίθετο: ")
    onoma = raw_input("Όνομα: ")
    alma1 = input("Βαθμολογία πρώτου άλματος: "))
    alma2 = input("Βαθμολογία δεύτερου άλματος: "))
    xwra = raw_input("Χώρα: ")

    EP.append(eponymo)
    ON.append(onoma)
    ALMA1.append(alma1)
    ALMA2.append(alma2)
    XWRA.append(xwra)

    synolo = alma1 + alma2 
    SYN.append(synolo)

    if xwra == "ΓΕΡΜΑΝΙΑ":
        bathmologia_germanias = bathmologia_germanias + synolo
    
    if alma2 > alma1:
        KALYTERH_EPIDOSH.append(eponymo)

megalyterh_bathmologia = max(SYN)
megalyterh_bathmologia_index = SYN.index(megalyterh_bathmologia)

print(EP, ON, ALMA1, ALMA2, XWRA, SYN)
print("Συνολική βαθμολογία της Γερμανίας: ", bathmologia_germanias)
print("Αθλητής με την μεγαλύτερη βαθμολογία: ", EP[megalyterh_bathmologia_index])
print("Νούμερο αθλητών με καλύτερη επίδοση στο 2ο άλμα: ", len(KALYTERH_EPIDOSH))
