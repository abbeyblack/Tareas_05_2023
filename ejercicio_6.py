peso_payaso = 112
peso_muñeca = 75

num_payasos = input("¿Cuántos payasos fueron vendidos en el último pedido:")
num_muñecas = input("¿Cuántos muñecas fueron vendidas en el último pedido:")

peso_total = (peso_payaso*int(num_payasos))+(peso_muñeca*int(num_muñecas))

print(f"El peso total del paquete que será enviado es de {peso_total} gr.")