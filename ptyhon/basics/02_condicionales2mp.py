"""
Sistema de pago para un árbitro.
– Las primeras 40 horas se pagan normal.
– Horas extra se pagan al 150%.
"""

pago_hora = float(input("Tarifa por hora del árbitro: "))
horas = int(input("Horas trabajadas esta semana: "))

if horas <= 40:
    total = pago_hora * horas
else:
    extras = horas - 40
    total = (pago_hora * 40) + (pago_hora * 1.5 * extras)

print(f"Pago semanal total: ${total:.2f}")
