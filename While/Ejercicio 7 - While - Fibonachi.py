ciclos = 0
num = 0
x = 1
negativo = 0
positivo = 0
resultado = 0

ciclos = int(input("Ingrese cantidad de numeros a evaluar:" ))

if ciclos < 0:
    ciclos = ciclos *-1

while x <= ciclos:
    num = x

    if num % 2 != 0:
        num = num
        
        positivo = positivo + num
    else:
        num = num * - 1
        negativo = negativo - num


    resultado = positivo - negativo
    x= x +1
    print(num)
print("La suma de los numeros anteriores es: ",resultado)
   


    

