num = 0
x = 0
a = 0
b = 0
mayor = 0

while x <= 1:
    num = int(input("Ingrese numeros: "))

    if x == 0:
        a = num

    if x == 1:
        b = num
        if a > b:
            print(a, "es mayor")
        if b < a:
            print(b,"es menor")
        if a == b:
            print("son iguales")
                 
    x = x +1

