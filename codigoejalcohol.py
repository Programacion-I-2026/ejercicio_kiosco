precioComida = int(input("ingrese total de la comida: "))
precioBebidaSA = int(input("ingrese total de la bebida sin alcohol: "))
precioBebidaCA = int(input("ingrese total de la bebida con alcohol: "))
totalInvitados = int(input("ingrese total de invitados: "))
totalBorrachos = int(input("ingrese total de invitados que beben alcohol: "))
cuotaInvitados = ((precioComida/totalInvitados)+(precioBebidaSA/totalInvitados))
extraCuotaBorrachos = precioBebidaCA/totalBorrachos
print("cada invitado debe pagar: ", cuotaInvitados)
print("cada invitado que tome alcohol debe pagar un extra de: ", extraCuotaBorrachos)