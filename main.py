pi = 3.1416
try:
    radio = int(input("ingrese el radio:"))
except ValueError:
    print("error en el ingreso de numeros")
else:
    area = pi*(radio*radio)
    print ("la superficie del circulo es: ",area)
finally:
    print ("Gracias por utlizar el programa")
