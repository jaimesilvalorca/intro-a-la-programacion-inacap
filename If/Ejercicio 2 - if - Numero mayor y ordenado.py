#INgresar 3 numeros y desplegar el mayor y ordenandolo de mayor a menor

n1 = 0

n2 = 0

n3 = 0

n1 = int(input("Ingrese primer numero"))
n2 = int(input("Ingrese segundo numero"))
n3 = int(input("Ingrese tercer numero"))

if n1 > n2 and n1 > n3:
       print("El primer numero es el mayor")
       print(n1)
       print(n2)
       print(n3)

else:
    if n2>n3:
        print("El segundo numero es el mayor")
    else:
        print("el tercer numero es el mayor")
