# Solicitar al usuario que ingrese el monto de la compra
monto_compra = float(input("Ingrese el monto de la compra: "))

# Inicializar el descuento en 0
descuento = 0

# Calcular el descuento según el rango de monto de la compra
if 500 <= monto_compra < 1000:
    descuento = 0.05 * monto_compra
elif 1000 <= monto_compra < 7000:
    descuento = 0.11 * monto_compra
elif 7000 <= monto_compra <= 15000:
    descuento = 0.18 * monto_compra
elif monto_compra > 15000:
    descuento = 0.25 * monto_compra

# Calcular el monto final a pagar
total_a_pagar = monto_compra - descuento

# Mostrar el descuento y el monto total a pagar
print(f"El descuento aplicado es de: {descuento}")
print(f"El monto total a pagar es: {total_a_pagar}")
