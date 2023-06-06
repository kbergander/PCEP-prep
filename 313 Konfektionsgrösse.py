def computeGarmentSize(width,size,gender):
    return computeMaleGarmentSize(width) if gender=="M" else computeFemaleGarmentSize(width,size)

def computeMaleGarmentSize(width):
    return width/2

def computeFemaleGarmentSize(width,size):
    garmentSize = (width / 2)-6
    if size>170:
        garmentSize *= 2
    elif size<164:
        garmentSize /=2

    return garmentSize


print(computeGarmentSize(92,192,"M"))
print(computeGarmentSize(80,172,"M"))

print(computeGarmentSize(92,167,"F"))
print(computeGarmentSize(103,150,"F"))
print(computeGarmentSize(86,180,"F"))