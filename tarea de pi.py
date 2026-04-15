pi = 3.1415
try:
    radio = int(input("ingrese el radio: "))
except ValueError:
    print("error en el ingreso de numeros")
else:
    area = pi*(radio*radio)
    print("la superficie del circulo es: ", round(area, 2))
finally:
    print("gracias por utilizar el programa!!")
