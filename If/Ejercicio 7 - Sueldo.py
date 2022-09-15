#desarrolle un programa en python que permite ingresar el sueldo de una persona, y aumentarlo segun la siguiente tabla:

#Sueldo mayor a 400000 y menor o igual a 500000 se aumenta el 20%

#mayor a 500000 y menor o giaul a 700000 se aumenta un 10%

#mayor a 700000 un 5%

#desplegar el sueldo y el aumento y el total.

Sueldo = 0

aumento = 0.0

total = 0.0


sueldo = int(input("Ingrese su sueldo :"))

if sueldo > 400000 and sueldo <= 500000:
    aumento = sueldo * 0.2

    total = sueldo+aumento

    print("Su sueldo es: ",sueldo, "Tiene un aumento de 20% que corresponde al: ", aumento, "y su total es: ", total)

elif sueldo > 500000 and sueldo <= 700000:

    aumento = sueldo * 0.10

    total = sueldo+aumento

    print("Su sueldo es: ",sueldo, "Tiene un aumento de 10% que corresponde al: ", aumento, "y su total es: ", total)

elif sueldo > 700000:

    aumento = sueldo * 0.05

    total = sueldo+aumento

    print("Su sueldo es: ",sueldo, "Tiene un aumento de 5% que corresponde al: ", aumento, "y su total es: ", total)

else:

    print("Sueldo invalido")

    

    

    
    




               
