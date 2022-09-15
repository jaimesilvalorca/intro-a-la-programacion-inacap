#desarrolle un programa que permita ingresar 10 notas a un arreglo y al finalizar despliegue el promedio, la nota mas alta y la posicion donde fue ingresada
#Tambien si aprueba o reprueba la asignatura. Nota: Debe validar que la nota este entre 1 y 7 de lo contontrario ingreasar el mensaje de error y solicitar reingreso de la nota

import numpy as np 

b = np.zeros(10, dtype = float)


suma = 0
i = 0
alta = 0
pos = 0

while i < 10:
    b[i] = round(float(input("Ing. nota " + str(i+1) + " :")),2)

    if b[i] >= 1 and b[i] <= 7:

        suma = suma + b[i]
        i = i+1

    else:
        print("Nota invalida, ingrese nuevamente")

promedio = suma/10

if promedio <4:

    print("alumno reprueba la asignatura")
else:
    print("alumno aprueba la asignatura")
    

print("El promedio fue de: ", promedio)

for i in range(0,10,1):

    if b[i] > alta:
        alta = b[i]
        pos = i
        
print(alta,(pos+1), " -> es mayor de las notas") 
