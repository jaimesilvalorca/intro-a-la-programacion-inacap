inicio = int(input("Indique N° de inicio: ")) 
hasta = int(input("Indique N° final: ")) 


contarPrimos = 1 

num = 1 

while True: 

    divisibles = 0 

    for x in range(1, num + 1, 1): 

        if num % x == 0: 

            divisibles = divisibles + 1 

 

    if divisibles == 2: 

        contarPrimos = contarPrimos + 1

    while contarPrimos >= inicio and contarPrimos <= hasta:
        
        print(contarPrimos , "->", num)

        inicio = inicio + 1
        
    num = num + 1 
