numA = int(input("Ing. 1er número :")) 

 

sumDivA = 0 

for x in range(1, numA, 1): 

    if numA % x == 0: 

        sumDivA = sumDivA + x 

        #print("divisor->" , x) 

 

sumDivB = 0 

numB = int(input("Ing. 2do número :")) 

for x in range(1, numB, 1): 

    if numB % x == 0: 

        sumDivB = sumDivB + x 

        #print("divisor->" , x) 

 

 

if numA == sumDivB and numB == sumDivA: 

    print("Amiguis") 

else: 

    print("Enemigos") 
