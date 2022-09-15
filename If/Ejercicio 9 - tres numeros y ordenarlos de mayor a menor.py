n1 = 0

n2 = 0

n3 = 0

mayor = 0
segundo = 0
tecero = 0


 
n1 = int(input("Ingrese primer número : ")) 

n2 = int(input("Ingrese segundo número : ")) 

n3 = int(input("Ingrese tercer número : ")) 


if n1 > n2 and n1 > n3:
    mayor= n1
    if n2 > n3:
        segundo= n2
        tercero= n3
    else:
        segundo= n3
        tercero= n2
elif n2 > n1 and n2 > n3:
    mayor = n2
    if n1 > n3:
        segundo= n1
        tecero= n3
    else:
        segundo=n3
        tercero=n1
else:
    mayor=n3
    if n1 > n2:
        segundo= n1
        tercero= n2
    else:
        segundo= n2
        tercero= n1

print(mayor)
print(segundo)
print(tercero)
        
