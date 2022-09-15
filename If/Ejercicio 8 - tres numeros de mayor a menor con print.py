n1 = 0

n2 = 0

n3 = 0 

 
n1 = int(input("Ingrese primer número : ")) 

n2 = int(input("Ingrese segundo número : ")) 

n3 = int(input("Ingrese tercer número : ")) 

 

if n1 > n2 and n1 > n3: 

    print("El mayor es: ", n1)
    print("")
    if n2> n3:
        print(n1)
        print(n2)
        print(n3)
    else:
        print(n1)
        print(n3)
        print(n2)

else: 

    if n2>n3 and n2>n1:

        print("El mayor es: ", n2)
        print("")
        if n1>n3:
            print(n2)
            print(n1)
            print(n3)
        else:
            print(n2)
            print(n3)
            print(n1)

    else:

        print("El mayor es: ", n3)
        print("")
        if n2>n1:
            print(n3)
            print(n2)
            print(n1)
        else:
            print(n3)
            print(n1)
            print(n2)


print("")
print("El programa ha terminado")



