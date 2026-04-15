comida = float(input("Ingrese el total de la comida: "))
bebida_sa = float(input("Ingrese el total de la bebida sin alcohol: "))
bebida_ca = float(input("Ingrese el total de la bebida con alcohol: "))
invitados = int(input("Ingrese la cantidad de invitados: "))
invitados_ca = int(input("Ingrese la cantidad de invitados que beben alcohol: "))
importe = comida / invitados + bebida_sa / invitados
extra = bebida_ca / invitados_ca
print("Total a abonar por comida y bebida cada invitado:", importe)
print("Extra a abonar quien tomó alcohol:", extra)