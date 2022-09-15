import numpy as np 

a = np.zeros(10, dtype = float)
b=0
mayor=0
for x in range (10):
    y=0
    while y < 1:
        a[x]=round(float(input("ig nota " + str(x+1) + " : ")),2)
        if a[x]>=1 and a[x]<=7:
            b=b+a[x]
            y=y+1
            if a[x]>=mayor:
                mayor=a[x]      
        else:
            print("Error nota mala, reingrese porfavor")

b=b/10
b=round(b,1)
print(a)
print(mayor)
print(b)
if b>=4:
    print("Aprobado!")
else:
    print("Reprobado!")
