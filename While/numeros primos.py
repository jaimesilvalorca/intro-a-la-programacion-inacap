hasta = int(input("¿ Cúantos primos desea desplegar ? :")) 

 

contarPrimos = 1 

num = 1 

while contarPrimos <= hasta: 

    divisibles = 0 

    for x in range(1, num + 1, 1): 

        if num % x == 0: 

            divisibles = divisibles + 1 

 

    if divisibles == 2: 

        print(contarPrimos , "->", num) 

        contarPrimos = contarPrimos + 1 

 

    num = num + 1 
