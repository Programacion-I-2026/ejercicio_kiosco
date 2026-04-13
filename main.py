precio = 50
cantidad = 4
total = precio * cantidad       #Aqui hay que multiplicar la cantidad con el precio de esas 4 NO sumar.
impuesto = total * 0.10    #Aca pide el 10% no tiene sentido la multiplicacion
total_final = total + impuesto
print(total_final)
