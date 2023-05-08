pizza_veg = ["pimiento", "tofu"]
pizza_nor = "peperoni", "jamón", "salmón"
base_pizza ="tomate", "mozarella"

tipo_pizza = input("¿Qué tipo de pizza desea? (vegetariana o normal) ")

if tipo_pizza == "vegetariana":
    print(f"Este es el menú vegetariano: {pizza_veg}")
    ingrediente = input ("Escoja uno de los ingredientes de la pizza ")
    print("La pizza seleccionada tendrá los siguientes ingredientes: ")
    print(f"{base_pizza} y {ingrediente}")
if tipo_pizza == "normal":
    print(f"Este es el menú normal: {pizza_nor}")
    ingrediente = input ("Escoja uno de los ingredientes de la pizza: ")
    print("La pizza seleccionada tendrá los siguientes ingredientes: ")
    print(f"{base_pizza} y {ingrediente}")
