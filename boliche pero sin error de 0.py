comida = int(input("Ingrese el total de la comida: "))
bebida_sa = int(input("ingrese el total de la bebida sin alcohol: "))
bebida_ca = int(input("ingrese el total de la bebida con alcohol: "))
invitados = int(input("ingrese el total de invitados: "))
invitados_ca = int(input("ingrese el total de invitados que tomen alcohol: "))
importe = comida/invitados+bebida_sa/invitados
try :
    extra = bebida_ca/invitados_ca
except ZeroDivisionError:
    extra = 0
    print("no hay persona que consuman alcohol.")
else: 
    print("el importe extra poe el consumo de alcohol: ", extra)

print("el importe que debe abonar cada invitado es de: ", importe)
