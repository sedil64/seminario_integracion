"""
Se pide cuántos jugadores hay
y luego el sueldo de cada uno.
Calcula la nómina total del equipo.
"""

jugadores = int(input("Número de jugadores del equipo: "))
nomina = 0

for i in range(jugadores):
    sueldo = float(input(f"Sueldo del jugador {i+1}: "))
    nomina += sueldo

print(f"Nómina total del equipo: ${nomina:.2f}")
