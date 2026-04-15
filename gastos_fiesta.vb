# total de gastos de comida, bebida son alchol, bebidas con alchol
#cantidad de invitados
#cantidad de invitados que consumieron bebidas alcholicas
#cuanto deben pagar por comida y bebida sin alchol mas costo extra por tomar alchol 

total_de_comida = int(input("Ingrese el total de gastos en comida: "))
total_de_bebidas_sa = int(input("Ingrese el total de gastos en bebidas sin alcohol: "))
total_de_bebidas_ca = int(input("Ingrese el total de gastos en bebidas alcoholicas: "))
cantidad_de_invitados = int(input("Ingrese la cantidad de invitados: "))
cantidad_de_invitados_ca = int(input("Ingrese la cantidad de invitados que consumieron bebidas alcoholicas: "))

#entrada sin alchol y comida 
total = total_de_comida + total_de_bebidas_sa
costo_deT_Sa = total / cantidad_de_invitados
#entrada con alchol
costo_extra = total_de_bebidas_ca / cantidad_de_invitados_ca


print("El costo total de al entrada es: ", costo_deT_Sa , "el extra por beber achol es:", costo_extra)