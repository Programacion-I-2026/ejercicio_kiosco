try:

 totalComida = int(input("ingrese el total de comida:"))
 totalBebidaSA = int(input("ingrese el total de bebida sin alcohol:"))
 totalBebidaCA = int(input("ingrese el total de bebida con alcohol:"))
 invitados = int(input("Ingrese cantidad de invitados:"))
 invitadosQueToman = int(input("¿Cuántos consumirán alcohol?:"))
 importeEntrada = (totalComida/invitados + totalBebidaSA/invitados)
 try: 
     extra = (totalBebidaCA/invitadosQueToman)
 except ZeroDivisionError:
     extra = 0
     print("No hay personas que consumen alcohol.")
 else:
     print("Extra a pagar por persona que consuma alcohol:", extra) 

 print("El valor de la entrada por persona será de:", importeEntrada)
except ValueError:
  print("error de datos ingresados")

