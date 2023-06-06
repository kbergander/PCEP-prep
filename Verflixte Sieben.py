zahl = 0
check=0
while zahl <1000:
    zahl +=1
    if zahl%7 == 0:
        print(str(zahl)+": durch 7 teilbar")
    else:
        tmp = zahl // 10
        while tmp!=0:
            if tmp%10==7:
                print(str(zahl) + ": enthält eine 7")
            tmp = tmp //10


