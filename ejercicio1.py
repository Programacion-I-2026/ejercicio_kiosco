comida = int(input("Ingreso total de la comida: "))
bebida_sa = int(input("Ingrese el total de la bebida sin alcohol :"))
bebida_ca = int(input("Ingrese el total de la bebida con alcohol:"))
invitados = int(input("Ingrese la cantidad de invitados: "))
invitados_ca = int(input("Ingrese la cantidad de invitados con alcohol: "))
importe = comida/invitados+bebida_sa/invitados
extra = bebida_ca/invitados_ca
print("El importe que debe abonar es de: ",importe)
print("El importe que debe abonar las personas que van a tomar con alcohol es de : ",extra)