comida = int(input("ingrese total de la comida:"))
bebida_sa = int(input("ingrese total de la bebida sin alcohol:"))
bebida_ca = int(input("ingrese total de la bebida con alcohol:"))
invitados = int(input("ingrese total de invitados"))
invitados_ca = int(input("ingrese el total de invitados que beben alcohol: "))
importe = comida/invitados+bebida_sa/invitados
try :
    extra = bebida_ca/invitados_ca
except  ZeroDivisionError:
    extra = 0
    print("no hay personas que consuman alcohol: ")
else:
    print("el importe extra por el cosnumo de alcohol es de: ", extra)
print("el importe que debe abonar cada invitado es de :  ", importe)
