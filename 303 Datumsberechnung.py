def datumsberechnung(tag,monat,jahr,anzahl):
    while anzahl>0:
        tag+=1
        anzahl-=1
        if tag>tageImMonat(monat,jahr):
            tag=1
            monat+=1
        if monat>12:
            monat =1
            tag=1
            jahr-=1

    return tag,monat,jahr
def isSchaltjahr(jahr):
    return(jahr % 4 == 0) and (jahr % 100 != 0) or (jahr % 400 == 0)

def tageImMonat(monat,jahr):
    if monat==2:
        return 29 if isSchaltjahr(jahr) else 28
    else:
        return 30 if monat==4 or monat==6 or monat==9 or monat==11 else 31



tag=int(input("tag"))
monat=int(input("monat"))
jahr=int(input("jahr"))
anzahl=int(input("anzahl tage"))
print(datumsberechnung(tag,monat,jahr,anzahl))