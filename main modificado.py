precio = 50
cantidad = 4
total = precio * cantidad 
impuesto = total * 1.10 
total_final = total + impuesto
print(total_final)
#el error de esto es que suma el precio y la cantidad en vez de multiplicarla, tambien multiplica por 10 cuando debe dividir
# cambiamos la suma por la multipliacion 
#para sacar el 10%