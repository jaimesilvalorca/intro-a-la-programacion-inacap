#Crear un algoritmo en diagrama de flujo  que al leer un número entero positivo (asuma que el número cumple las condiciones), imprimir PAR si el número es par e IMPAR si es impar.

num = 0

num = int(input("Ingrese un numero para determinar si el numero es par o impar: "))

if num % 2 == 0:
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar")

