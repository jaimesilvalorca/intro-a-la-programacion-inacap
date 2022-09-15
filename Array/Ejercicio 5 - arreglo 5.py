import numpy as np 

 

arregloA = np.zeros(10, dtype=int) 

arregloB = np.zeros(10, dtype=int) 

 

for i in range(0, 10, 1): 

    arregloA[i] = 100 - i 

    print("Elemento posición[", i, "] ->", arregloA[i])

    arregloB[i] = 50 - i

    print("Elemento posición[", i, "] ->", arregloB[i])

    

    

 

 

print("A -> ", arregloA)
print("B -> ", arregloB)
