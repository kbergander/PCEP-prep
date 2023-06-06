tag=int(input("tag"))
monat=int(input("monat"))
jahr=int(input("jahr"))
anzahl=int(input("anzahl tage"))

while anzahl>0:
    anzahl-=1
    tag+=1
    if monat==12 and tag>31:
        jahr+=1
        monat=1
        tag=1
        continue

    if ((monat==2 and tag>28)
       or((monat==1 or monat==3 or monat==5 or monat==7 or monat==8 or monat==10 or monat==12) and tag>31)
       or ((monat==2 or monat==4 or monat==6 or monat==9 or monat==11) and tag>30)):
        monat+=1
        tag=1

print(tag,monat,jahr,sep=".")
