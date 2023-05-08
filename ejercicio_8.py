interés = 0.04
monto_inicial = input("Monto inicial en la cuenta de ahorro:")

saldo_año_1 = (int(monto_inicial)*interés) + int(monto_inicial)
saldo_año_2 = (saldo_año_1*interés) + saldo_año_1
saldo_año_3 = (saldo_año_2*interés) + saldo_año_2

print("La cantidad de ahorros tras el primer año es:", round(saldo_año_1, 2))
print("La cantidad de ahorros tras el segundo año es:", round(saldo_año_2, 2))
print("La cantidad de ahorros tras el tercer año es:", round(saldo_año_3, 2))
