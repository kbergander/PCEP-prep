
def endlichesProdukt(startwert,endwert):
    if endwert<=0 or startwert<=0:
        return 0

    if endwert<startwert:
        startwert,endwert = vertausche(startwert,endwert)

    produkt=startwert
    aktWert=startwert

    while aktWert<endwert:
        produkt *= nextWert(aktWert)
        aktWert+=1
    return produkt

def nextWert(wert):
    return wert+1

def multipliziere(z1,z2):
    return z1*z2

def vertausche(v1,v2):
    return v2,v1


startwert=int(input("Startwert: "))
endwert=int(input("Endwert: "))
print(str(endlichesProdukt(startwert,endwert)))