comida= int(input("total de la comida:"))
bebida_sa=int(input("total de la bebida sin alchol:"))
bebida_ca=int(input("total de la bebida con alchol:"))
invitados=int(input("cuantos invitados son:"))
invitados_ca=int(input("cuantos invitados van a tomar alchol:"))
total=comida/invitados+ bebida_sa/invitados
try:
    extra=bebida_ca/invitados_ca
except ZeroDivisionError:
    extra=0
    print("no hay persona que consuma alchol")
else:
    print("el importe extra por alchol es de:",extra)
print("el total de los invitados es de ", total)