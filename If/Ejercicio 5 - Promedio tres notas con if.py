#Desarrrolle un programa donde el usuario ingrese 3 notas y el sistema despliegue el promedio.

n1 = 0.0 

n2 = 0.0 

n3 = 0.0 

pro = 0.0 

 

n1 = float(input("Nota 1 :")) 

n2 = float(input("Nota 2 :")) 

n3 = float(input("Nota 3 :")) 

 

pro = (n1 + n2 + n3) / 3 

pro = round(pro, 1)




if pro >= 4: 
    print("Aprueba el semestre con un",pro)

else:
    print("Reprueba el semestre con un",pro)

print("Fin del programa")

 
