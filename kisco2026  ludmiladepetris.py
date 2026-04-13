precio = 50
cantidad = 4
# Esta parte esta mal porque deberia multiplicar el precio del chocolate por la cantidad de chocolates que lleva.
total = precio*cantidad 
# Luego, en esta parte debe sedr multiplicado 0.10, sino estaria multiplicando 10 veces el total.
impuesto = total *0.10 
total_final = total + impuesto
print(total_final)
