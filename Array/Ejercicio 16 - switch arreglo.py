
#0,1,2,3,4,5,6,7,8,9 - 11,12,13,14,15,16,17,18,19

import numpy as np 
 
a = np.array ([0,1,2], dtype = int)
b = np.array([11,12,13], dtype = int)

save1 = 0
save2 = 0

print("Primer arreglo -->",a)
print("Segundo arreglo -->",b)


for i in range(3):
       
    save1 = a[i] 
    save2 = b[i]

    b[i] = save1
    a[i] = save2
    print(a)
    print(b)

print("-----------")
print("Primer arreglo -->",a)
print("Segundo arreglo -->",b)
    
    
