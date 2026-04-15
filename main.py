print("\n🤩 Calculadora de todos los costos de la fiesta🤩\n")


#TOTAL DE INVITADOS
try:
    total_estudiantes=int(input("Ingrese la cantidad de invitados que asistiran: "))                 
    print("\n\tAsistiran", total_estudiantes,"a la fiesta\n\t")
    #Cantidad de estudiantes que NO tomaran alcohol
    estudiantes1=int(input("¿Cuantos invitados tomaran bebidas SIN alcohol?: "))

except ValueError:
    print("\n\tERROR. No se admiten caracteres\n\t")


if estudiantes1<=total_estudiantes:
    print("\n\tOkey, Comeran y beberan", estudiantes1,"estudiantes")
else:
    print("\t⚔️  Solo hay",total_estudiantes,"en total, no es posible ⚔️\t")



 #Cantidad de estudiantes que tomaran alcohol

estudiantes2=abs(estudiantes1-total_estudiantes)                                            




#¿Cuantos estudiantes comeran y beberan alcohol?

print("\nSignifica que comeran y beberan alcohol", estudiantes2, "estudiantes por que son los restantes\n")





#CANTIDAD DE CONSUMOS

cant_comida=int(input("Ingrese la cantidad de platos de comida que hay: "))

cant_bebidas=int(input("Ingrese la cantidad de bebidas que hay: "))

cant_bebidas_con_alcohol=int(input("Ingrese la cantidad de bebidas CON alcohol que hay: "))






#COSTOS DE CONSUMOS

comida=int(input("¿Costo de la comida?:"))

bebida=int(input("¿Costo de la bebida SIN alcohol?: "))

bebidas_con_alcohol=int(input("¿Costo de la bebida CON alcohol?: "))

print("\nEntonces\n")






#COSTOS * CANTIDAD
precio_por_cantidad_comida=(cant_comida*comida)
print("Poseemos", cant_comida, "platos de comida que en total son", precio_por_cantidad_comida, "pesos")

print("\n\n")
precio_por_cantidad_bebidas=(cant_bebidas*bebida)
print("Poseemos", cant_bebidas, "botellas de bebidas que en total son", precio_por_cantidad_bebidas, "pesos")

print("\n\n")
precio_por_cantidad_bebidas_con_alcohol=(cant_bebidas_con_alcohol*bebidas_con_alcohol)
print("Poseemos", cant_bebidas_con_alcohol, "botellas con alcohol que en total son", precio_por_cantidad_bebidas_con_alcohol, "pesos")
print("\n\n")



print("\n\t😎 ¿Cuanto deberan pagar en total cada grupo?😎\n\t")

#¿CUANTO DEBERAN PAGAR TODOS LOS QUE NO BEBEN ALCOHOL?

abono_total_1=(comida+bebida*estudiantes1)
print("\tEn total todos los estudiantes que NO beban Alcohol deberan pagar", abono_total_1, "pesos\t")                       


#¿CUANTO DEBERAN PAGAR TODOS LOS QUE SI BEBEN ALCOHOL?

abono_total_2=(comida+bebidas_con_alcohol*estudiantes2)
print("\tEn total todos los estudiantes que beban Alcohol deberan pagar", abono_total_2, "pesos\t")





#¿CUANTO DEBERA ABONAR CADA ESUDIANTE?
print("\n\t😎 ¿Cuanto debera abonar cada estudiante?😎\n\t")

abono_individual1=(precio_por_cantidad_bebidas+precio_por_cantidad_comida)//estudiantes1
print("Cada estudiante que quiera beber sin alcohol debera abonar", abono_individual1, "pesos cada uno")


abono_individual2=(precio_por_cantidad_bebidas_con_alcohol+precio_por_cantidad_comida)//estudiantes2 
print("Cada estudiante que quiera beber alcohol debera abonar", abono_individual2, "pesos cada uno")
print("\n\t\n\t")


#COSTO EXTRA QUE DEBERA PAGAR CADA INIVITADO QUE TOME ALCOHOL

extra=abs(abono_individual1-abono_individual2)
print("El extra que deberan abonar los que tomaran alcohol son", extra, "pesos")
print("\n\t\n\t")













