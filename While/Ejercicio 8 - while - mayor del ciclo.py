ciclos = 0
num = 0
x = 0
nmayor = 0


ciclos = int(input("Ingrese cantidad de numeros a evaluar:" ))

while x < ciclos:
    num = int(input(" Numero " + str(x+1) + " de " + str(ciclos) + ": "))
    if x == 0:
        nmayor = num

    if num > nmayor:
        nmayor = num
        
     print(nmayor)
     print(num)
    x = x + 1


print("El numero mayor es: ",nmayor)
