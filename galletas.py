precio_paquete = 10

paquetes = int(input("¿Cuántos paquetes de galletas desea comprar? "))

subtotal = paquetes * precio_paquete

descuento = subtotal * 0.60

total = subtotal - descuento

print("Subtotal: $", subtotal)
print("Descuento: $", descuento)
print("Total a pagar: $", total)
