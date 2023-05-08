numerador = input("Ingrese el numerador:")
denominador = input("Ingrese el denominador:")

while int(denominador) == 0:
    print("El denominador no puede ser cero.")
    denominador = input("Ingrese el denominador nuevamente:")

resultado = int(numerador) / int(denominador)
print(f"El resultado es: {resultado}")

