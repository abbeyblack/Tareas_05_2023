cantidad_invertir = input("¿Cuánto desea invertir?")
interes_anual = input("¿Cuál es el interés anual porcentual de su inversión?")
numero_años = input("¿Por cuantos años quiere invertir su dinero?")

capital_obtenido = int(cantidad_invertir)*(int(interes_anual)/100)*int(numero_años)

print(f"El capital obtenido es {capital_obtenido}")