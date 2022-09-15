#Ingresar 5 elementos en la posición 0 y desplazar todos los elementos hacia la derecha

import numpy as np 

b = np.array([3,5,1,8,6], dtype = int)

print(b)

for n in range(5): 

    for x in range(0,4,1): 

        b[x] = b[x + 1] 

    b[0] = int(input("Ing. número :"))
    print(b)

 

print(b) 

 
