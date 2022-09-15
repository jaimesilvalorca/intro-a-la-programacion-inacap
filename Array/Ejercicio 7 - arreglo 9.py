import numpy as np 

 

arregloA = np.zeros(10, dtype=int) 

elemento = 1 

for i in range(0, 5, 1): 

    arregloA[i] = elemento 

    elemento = elemento + 1

    print(arregloA)

    arregloA[9 - i] = elemento 

    elemento = elemento + 1

    print(arregloA)

 

     

print("A -> ", arregloA) 
