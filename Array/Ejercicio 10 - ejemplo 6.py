import numpy as np 

 
largo = 100

arregloA = np.zeros(largo, dtype=int) 

 

for i in range(0, largo, 1): 

    if i < largo / 2: 

        arregloA[i] = -1 

    else: 

        arregloA[i] = 1 

     

print("A -> ", arregloA) 
