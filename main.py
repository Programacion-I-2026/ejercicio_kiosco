precio = 50
cantidad = 4

#El total no es suma, es multiplicación (precio * cantidad).
total = precio * cantidad 

#El impuesto no se multiplica por 10, para sacar el 10% hay que usar (total * 10) / 100
impuesto = (total * 10) / 100

total_final = total + impuesto
print(total_final)