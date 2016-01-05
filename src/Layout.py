
tSize = input("Tile size: ").split()
gSize = input("Grout line thickness: ").split("/")
rSize = input("Length of room in feet: ")

coefficient = int(tSize[0])
numerator = int(tSize[1].split("/")[0])
denominator = int(tSize[1].split("/")[1])

print("Tile Size: {} {}/{}".format(coefficient, numerator, denominator))
print("Grout Size: {}/{}".format(gSize[0], gSize[1]))

def reduceFract(c, n, d) :
    while n >= d :
        n -= d
        c += 1
    while n % 2 == 0 :
        n = n / 2
        d = d / 2
    return int(c), int(n), int(d)

def addFract(f1n, f1d, f2n, f2d) :
    combinedNum = (f1n * f2d) + (f2n * f1d)
    combinedDen = f1d * f2d
    return int(combinedNum), int(combinedDen)
    
def calcLayout(interval, length) :
    length = length * 12
    i = 1
    marks = [0]
    curMark = [0,0,0]
    while curMark[0] < length :
        curMark = [interval[0]*i,interval[1]*i,interval[2]]
        curMark[0], curMark[1], curMark[2] = reduceFract(curMark[0], curMark[1], curMark[2])
        marks.append("{} {} {}/{}".format(i, curMark[0], curMark[1], curMark[2]))
        i += 1
        print(curMark[0], length)

numerator, denominator = addFract(numerator, denominator, int(gSize[0]), int(gSize[1]))
print("{}/{}".format(numerator, denominator))
coefficient, numerator, denominator = reduceFract(coefficient, numerator, denominator)

print("{} {}/{}". format(coefficient, numerator, denominator))

calcLayout([coefficient, numerator, denominator], int(rSize))
print(marks)
