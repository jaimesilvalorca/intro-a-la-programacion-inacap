 

import numpy as np 

 

b = np.zeros(5, dtype = int) 

 

suma = 0 

for i in range(0,10, 1): 

    b[i] = int(input("Ing. número en la posición " + str(i) + " :")) 

    suma = suma + b[i] 

 

promedio = suma / 5 

 

print("Usted ingresó los siguientes números -> ", b) 

print("El promedio de los números ingresados es -> ", promedio) 

 

#for i in range(0,5,1): 

    #if b[i] > promedio: 

  #      print(b[i], " -> es mayor al promedio") 

 

#print("Programa finalizado") 
