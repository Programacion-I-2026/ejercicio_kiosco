try :
    comida = int(input("Ingreso total de la comida: "))
    bebida_sa = int(input("Ingrese el total de la bebida sin alcohol :"))
    bebida_ca = int(input("Ingrese el total de la bebida con alcohol:"))
    invitados = int(input("Ingrese la cantidad de invitados: "))
    invitados_ca = int(input("Ingrese la cantidad de invitados con alcohol: "))
    importe = comida/invitados+bebida_sa/invitados
    try : 
        extra = bebida_ca/invitados_ca
    except:
        extra = 0
        print("No hay personas que consuman alcohol")
    else:
        print("El importo total de las personas que toman alcohol: ", extra)
    
    print("El importe que debe abonar es de: ",importe)
except ValueError:
    print("Valor ingresado incorrecto"
          "\nIngresar un valor numerico")

