comida = int(input("Ingrese el total de la comida: "))
bebida_sa = int(input("Ingrese el total de la bebida sin alcohol: "))
bebida_ca = int(input("Ingrese el total de la bebida con alcohol: "))
invitados = int(input( "Ingrese el total de invitados: "))
invitados_ca = int(input("Ingrese el total de invitados que toman alcohol: "))
importe = comida/invitados+bebida_sa/invitados
extra = bebida_ca/invitados_ca
print("El importe que cada invitado debe abonar es de : ", importe)
print("El importe extra por el consumo de alcohol es:", extra)
