try:
    comida=int(input("Ingrese los gastos en comida: "))
    invitados=int(input("Ingrese cuantos invitados van a la cena: "))
    sinAlcohol=int(input("Ingrese los gastos en bebidas sin alcohol: "))
    alcohol=int(input("Ingrese los gastos en bebidas con alcohol: "))
    invAlcohol=int(input("Ingrese la cantidad de invitados que consumen alcohol: "))
except ValueError:
    print("error al ingresar los datos, ingrese un numero")
else:
    comybeb= (comida + sinAlcohol) / invitados
    borrachos= comybeb + (alcohol/invAlcohol)
    print(f"Cada uno debera pagar: {comybeb}")
    print(f"si toma alcohol debera pagar: {borrachos}")
finally:
    print("gracias por usar nuestro servicio!")