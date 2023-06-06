def isSchaltjahr(jahr):
    return (jahr%4==0 and jahr%100!=0) or jahr%400==0


print(isSchaltjahr(2012))
print(isSchaltjahr(2000))
print(isSchaltjahr(1916))
print(isSchaltjahr(1896))

print(isSchaltjahr(2013))
print(isSchaltjahr(2003))
print(isSchaltjahr(1900))
print(isSchaltjahr(1881))