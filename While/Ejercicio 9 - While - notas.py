promedio = 0
ciclos = 0
x= 0
suma = 0
nota = 0
menor = 0

ciclos = int(input("Ingrese la cantidad de calificaciones que tendrá: "))

if ciclos < 0:

    ciclos = ciclos * - 1
    

while x < ciclos:
    nota = int(input("Ingrese nota " + str(x+1) + " de " + str(ciclos) + " :"))

    if x==0:
        menor = nota

    if menor > nota:

        menor = nota

    if nota > 0 and nota <=7:

        suma = nota + suma
        print(suma)
        x = x + 1
        
    else:

        print("numero fuera de rango")


        


    
promedio = suma/ciclos


print(promedio)
print(menor)
    

        

        
