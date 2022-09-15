#Desarrolle un programa que permita ingresar tres notas y desplegar el promedio deba validar que la nota ingresada este entre 1 y 7 de lo contrario termina el programa
#De lo contrario enviar mensaje de nota invaldia si no esta drentro del rango

nota1 = 0.0

nota2 = 0.0

nota3 = 0.0

promedio= 0.0


nota1 = float(input("Ingrese primera nota : "))

if nota1 >= 1 and nota1 <= 7:
    print("")

else:
    print("Nota invalida, no está dentro del grupo")

nota2 = float(input("Ingrese segunda nota : "))

if nota2 >= 1 and nota2 <= 7:
    print("")
else:
    print("Nota invalida, no está dentro del grupo")

nota3 = float(input("Ingrese tercera nota : "))
    
if nota3 >= 1 and nota3 <= 7:
    print("")
else:
    print("Nota invalida, no está dentro del grupo")


promedio=(nota1 + nota2 + nota3)/3

round(promedio , 1)

print("Su promedio es:", promedio)




    
