comida=int(input("Ingrese los gastos en comida: "))
invitados=int(input("Ingrese cuantos invitados van a la cena: "))
sinAlcohol=int(input("Ingrese los gastos en bebidas sin alcohol: "))
alcohol=int(input("Ingrese los gastos en bebidas con alcohol: "))
invAlcohol=int(input("Ingrese la cantidad de invitados que consumen alcohol: "))
comybeb= (comida + sinAlcohol) / invitados
try:
    borrachos= comybeb + (alcohol/invAlcohol)
except ZeroDivisionError:
    borrachos= 0
    print("No hay invitados que tomen alcohol")
else:
    print(f"si toma alcohol debera pagar: {borrachos}")
print(f"Cada uno debera pagar: {comybeb}")
print("gracias por usar nuestro servicio!")