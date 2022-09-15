import numpy as np 

 

arregloA = np.zeros(10, dtype=int) 

arregloB = np.zeros(10, dtype=int) 

 

for i in range(0,10,1): 

    arregloA[i] = i + 1 

 

i = 0 

while i <= 9: 

    arregloB[i] = i + 2 

 

    i = i + 1 

 

print("A -> ", arregloA) 

print("B -> ", arregloB) 
