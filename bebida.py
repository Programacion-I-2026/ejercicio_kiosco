comida= int(input("total de la comida:"))
bebida_sa=int(input("total de la bebida sin alchol:"))
bebida_ca=int(input("total de la bebida con alchol:"))
invitados=int(input("cuantos invitados son:"))
invitados_ca=int(input("cuantos invitados van a tomar alchol:"))
total=comida/invitados+ bebida_sa/invitados
extra=bebida_ca/invitados_ca
print("el total de los invitados es de ", total)
print("el extra es de:", extra)