#desarrolle un programa que permite ingresar 10 numeros al usuario y al finalizar despliegue el promedio

x= 1
num= 0
suma= 0


while x <= 10:
    num = int(input("Ingrese numero " + str(x) + " de 10 : "))
    if num > 0:
        suma = suma + num
        total= suma/10

        x = x+1
    else:
        print("Error, Ingresó un numero negativo, intente nuevamente")      
  
print(total)
