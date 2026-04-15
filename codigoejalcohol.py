try: 
    precioComida = int(input("ingrese total de la comida: "))
    precioBebidaSA = int(input("ingrese total de la bebida sin alcohol: "))
    precioBebidaCA = int(input("ingrese total de la bebida con alcohol: "))
    totalInvitados = int(input("ingrese total de invitados: "))
    totalBorrachos = int(input("ingrese total de invitados que beben alcohol: "))
    cuotaInvitados = ((precioComida/totalInvitados)+(precioBebidaSA/totalInvitados))
    try :
        extraCuotaBorrachos = precioBebidaCA/totalBorrachos
    except ZeroDivisionError:
        extraCuotaBorrachos = 0
        print("No hay personas que consuman alcohol")
    else:
        print("El importe extra por el consmo de alcohol: ", extraCuotaBorrachos)
    print("cada invitado debe pagar: ", cuotaInvitados)
except ValueError:
    print("los datos ingresados estan mal \n asegurese de ingresar UNICAMENTE NUMEROS")