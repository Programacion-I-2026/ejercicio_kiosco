try:
    comida = int(input("Ingrese los gastos en comida: "))
    sinAlcohol = int(input("Ingrese los gastos en bebidas sin alcohol: "))
    alcohol = int(input("Ingrese los gastos en bebidas con alcohol: "))
    invitados = int(input("Ingrese la cantidad de invitados: "))
    invAlcohol = int(input("Ingrese la cantidad de invitados que consumen alcohol: "))

except ValueError:
    print("error al ingresar los datos, ingrese un numero")

else:
    comyeb = (comida + sinAlcohol) / invitados
    borrachos = comyeb + (alcohol / invAlcohol)

    print("cada uno debera pagar:", comyeb)
    print("si toma alcohol debera pagar:", borrachos)

finally:
    print("gracias por usar nuestro servicio")