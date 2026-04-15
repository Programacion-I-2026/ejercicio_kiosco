# total de gastos de comida, bebida son alchol, bebidas con alchol
#cantidad de invitados
#cantidad de invitados que consumieron bebidas alcholicas
#cuanto deben pagar por comida y bebida sin alchol mas costo extra por tomar alchol 

total_de_comida = int(input("Ingrese el total de gastos en comida: "))
total_de_bebidas_sa = int(input("Ingrese el total de gastos en bebidas sin alcohol: "))
total_de_bebidas_ca = int(input("Ingrese el total de gastos en bebidas alcoholicas: "))
cantidad_de_invitados = int(input("Ingrese la cantidad de invitados: "))
cantidad_de_invitados_ca = int(input("Ingrese la cantidad de invitados que consumieron bebidas alcoholicas: "))

#calculo del costo total por persona sin eel extra por tomar alchol

costo_t = (total_de_comida + total_de_bebidas_sa) / cantidad_de_invitados
print("El costo total de al entrada es: ", costo_t)

#costo extra por tomar alchol (try por si son 0 personas)
try:

    costo_extra = total_de_bebidas_ca / cantidad_de_invitados_ca
except ZeroDivisionError:
    costo_extra = 0
    print("No hay personas que tomen alchol")
else:
    print("el extra por beber achol es:", costo_extra)

