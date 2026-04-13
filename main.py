precio = 50
cantidad = 4
total = precio + cantidad 
#El primer error es que el total debe calcularse multiplicando el precio por la cantidad, quedando de esta manera:
#total = precio * cantidad
impuesto = total * 10 
#El segundo error es que el impuesto debe calcularse sacando el 10% sobre el total.
#impuesto = total * 0.10
total_final = total + impuesto
print(total_final)
