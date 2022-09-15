ipcM = 6
ipcF = 3
producto  = 0
diferencia = 0
marzo = 0
febrero = 0
x= 0

producto = int(input("Ingrese el monto del producto para calcular el ipc: "))

while x <= 1:
    
    if x == 0:
        marzo = producto * (ipcM/100)
        marzo = int(round(producto + marzo,0))
        print("El Valor del producto en marzo es:",marzo)

    else:
        febrero = producto * (ipcF/100)
        febrero = int(round(producto + febrero,0))
        print("El Valor del producto en febrero es:",febrero)

    diferencia = marzo - febrero
    
    x= x+1
print("La diferencia entre marzo y febrero es:",diferencia)
print("Fin del programa")
        
