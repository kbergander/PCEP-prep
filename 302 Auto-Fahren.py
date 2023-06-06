def showMenu():
    print ("(T)anken")
    print ("(F)ahren")
    print ("(R)eichweite anzeigen")
    print ("")
    print ("(B)eenden")
    print ("")
    return input ("Ihre Wahl: ")

def showInfo():
    print ("Tacho: "+str(tacho),"Tank: "+str(tank))

def showTanken():
    liter = float(input ("Wie viele Liter? "))
    return liter

def showFahren():
    km = float(input ("Wie viele Kilometer? "))
    return km

def showReichweite():
    print ((tank/verbrauch)*100)

tacho = 0
tank = 60
verbrauch=5

while True:
    option=showMenu()
    if option=="T":
        tank += showTanken()
    elif option=="F":
        km=showFahren()
        tacho += km
        tank -= (verbrauch/km)*100
    elif option=="R":
        showReichweite()
    elif option=="B":
        break
    showInfo()