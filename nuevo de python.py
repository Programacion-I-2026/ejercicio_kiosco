try:
    total_comida = int(input("Ingrese el total gastado en comida: "))
    total_bebidas_sin_alcohol = int(input("Ingrese el total de bebidas sin alcohol: "))
    total_bebidas_con_alcohol = int(input("Ingrese el total de bebidas con alcohol: "))
    cantidad_invitados = int(input("Ingrese la cantidad total de invitados: "))
    cantidad_beben_alcohol = int(input("Ingrese la cantidad de invitados que consumieron alcohol: "))

except ValueError:
    print("Error en los datos ingresados:") 

else:
    costo_base = (total_comida + total_bebidas_sin_alcohol) / cantidad_invitados
    
    if cantidad_beben_alcohol > 0:
        costo_extra_alcohol = total_bebidas_con_alcohol / cantidad_beben_alcohol
    else:
        costo_extra_alcohol = 0
    print("Cada invitado debe pagar (comida + bebida sin alcohol):", costo_base)
    print("Cada invitado que consumió alcohol debe pagar extra:", costo_extra_alcohol)

finally:
    print("Gracias por usar mi programa")