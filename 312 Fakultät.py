def fak(endzahl):
    zahl=1
    produkt=1
    while zahl<=endzahl:
        produkt *= zahl
        zahl+=1
    return produkt

print(fak(6))
print(fak(2))
print(fak(1))
print(fak(9))