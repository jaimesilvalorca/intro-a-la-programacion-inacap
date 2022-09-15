import numpy as np 

b = np.zeros(3, dtype = float)

i = 0
promedio = 0
promedioFinal = 0
suma = 0

while i < 3:
    b[i] = float(input("Ingrese notas " + str(i + 1) + " de 3: "))

    if b[i] >= 1 and b[i] <=7:
        suma = suma + b[i]
        i = i + 1

    else:
        print("nota fuera de rango")

promedio = suma / 3

print("Su nota n°1 ",b[0]," equivale a un 15% del promedio final")
print("Su nota n°2 ",b[1]," equivale a un 20% del promedio final")
print("Su nota n°3 ",b[2]," equivale a un 35% del promedio final")
print("Su nota n°4 ",round(promedio,2)," equivale a un 30% del promedio final")

b[0] = b[0]*0.15
b[1] = b[1]*0.20
b[2] = b[2]*0.35
promedio  = promedio*0.30

promedioFinal = b[0] + b[1] + b[2] + promedio

print("Su promedio final es: ",round(promedioFinal,2))
