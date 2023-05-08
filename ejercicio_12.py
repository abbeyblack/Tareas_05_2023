nombre = input("¿Cuál es su nombre? ")
género = input("¿Con qué género se identifica? (hombre o mujer) ")
grupo_abc_1 = ["ABCDEFGHIJKLMabcdefghijklm"]
grupo_abc_2 = ["NÑOPQRSTUVWXYZnñopqrstuvwxyz"]
primera_letra = nombre[0]

if género == "mujer":
    for x in grupo_abc_1:
        if primera_letra in x:
            print("Pertenece al grupo A")
        else:
            print("Pertenece al grupo B")
if género == "hombre":
    for y in grupo_abc_2:
        if primera_letra in y:
            print("Pertenece al grupo A")
        else:
            print("Pertenece al grupo B")
            