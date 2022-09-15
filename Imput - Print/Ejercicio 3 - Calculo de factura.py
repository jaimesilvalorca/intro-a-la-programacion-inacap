neto = 0
iva = 0
total = 0

neto = int(input("Ingrese el monto neto de la factura: "))

print(neto)
iva = int(round(neto * (19/100),0))
total = neto + iva
print(iva)
print(total)
