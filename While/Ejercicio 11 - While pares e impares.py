#desarrolle un programa en python que permite ingresar 10 numeros y al finalizar despliegue por pantalla cuantos numeros fueron pares

num = 0
x = 1
pares = 0
impares = 0

while x <= 10:
    num = int(input("Ingrese numero " + str(x) + " de 10 : "))

    x = x+1

    if num % 2 == 0:

        pares = pares + 1

    else:
        impares= impares+1


print("Hay ",pares,"Ingresados")

print("Hay ",impares,"Ingresados")
    

    



 







