import numpy as np 

 

arregloA = np.zeros(10, dtype=int) 

 

for i in range(0, 10, 1): 

    if i < 5: 

        arregloA[i] = -1 

    else: 

        arregloA[i] = 1 

     

print("A -> ", arregloA) 
