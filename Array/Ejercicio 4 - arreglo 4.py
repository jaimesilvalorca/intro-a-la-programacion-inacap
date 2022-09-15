import numpy as np 

 

arregloA = np.zeros(10, dtype=int) 

 

elem = 2 

for i in range(0, 10, 1): 

 

    if i % 2 == 0: 

        arregloA[i] = 1 

     

print("A -> ", arregloA) 
