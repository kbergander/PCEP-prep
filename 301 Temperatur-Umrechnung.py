def convertToCelsius(temp,einheitIn):
    return temp-273.15 if einheitIn=="K" else (temp-32)*(5/9) if einheitIn=="F" else temp
def converToFahrenheit(temp,einheitIn):
    return (temp*(9/5))+32 if einheitIn=="C" else (temp-273.15)*(9/5)+32 if einheitIn=="K" else temp
def convertToKelvin(temp,einheitIn):
    return temp+273.15 if einheitIn=="C" else (temp-32)*(5/9)+273.15 if einheitIn=="F" else temp

def convertTemperatur(temp,einheitIn,einheitOut):
    return convertToCelsius(temp,einheitIn) if einheitOut=="C" else convertToKelvin(temp,einheitIn) if einheitOut=="K" else converToFahrenheit(temp,einheitIn)

temp=float(input("Geben sie eine Temperatur ein: "))
einheitIn=input("Welche Einheit hat der eingegebene Wert (C/F/K)? ")
einheitOut=input("Geben Sie die Einheit für die Umrechnung ein (C/F/K): ")
print(convertTemperatur(temp,einheitIn,einheitOut))
