print("-------------------------------------")
print(" - - - - EJERCICIO DE PRUEBA - - - - ")
print("-------------------------------------")
print(" Ludmila Depetris, Comision 4 . . . .")

# INGRESO DE DATOS:
try:
    totalComida=int(input("Total gastado en comida: "))
    total_bebidas_sA=int(input("Total bebidas sin alcohol: "))
    total_bebida_cA=int(input("Total bebidas con alcohol: "))
    cantInvitados=int(input("Cantidad de invitados a asistir: "))
    cantInvitadosA=int(input("Cantidad de invitados que cosumieron bebidas alcoholicas: "))

    # ENTRADA GENERAL:
    entradaGeneral= totalComida+total_bebidas_sA / cantInvitados
    print("El total que debe pagar cada persona es de:",entradaGeneral)
    print("Costo sin consumision de alcohol.")

    try:
     extra= total_bebida_cA / cantInvitadosA
    except ZeroDivisionError:
        extra=0
        print("No hay personas que consuman alcohol.")
    else:
        # COSTO EXTRA POR ALCOHOL:
        extra= total_bebida_cA / cantInvitadosA
        entradaAlcohol= entradaGeneral+extra
except ValueError:
    print("Los datos son erroneos. No se puede ingresar letras.")
    print("\n Porfavor vuelva a internarlo.")

print("El costo a pagar es de:",entradaGeneral,"y agregando el alcohol es:",round(extra,2))
print("El costo de la entrada con alcohol es de:",round(entradaAlcohol,2))
