import numpy as np 
 
a = np.array ([0,1,2], dtype = int)
b = np.array([11,12,13], dtype = int)

sav = 0

print("Primer arreglo -->",a)
print("Segundo arreglo -->",b)


for i in range(3):
       
    sav = a[i] 

    a[i] = b[i]
    b[i] = sav

    print(a)
    print(b)
    
print("-----------")
print("Primer arreglo -->",a)
print("Segundo arreglo -->",b)
