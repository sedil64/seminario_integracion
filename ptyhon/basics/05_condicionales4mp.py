"""
Registrar asistencia de jugadores:
- T = tarde
- O = OK
- P = permiso

Cuenta cuántas tardanzas hubo.
"""

dias = int(input("¿Cuántos días de entrenamiento registrarás?: "))
tardanzas = 0

for i in range(dias):
    marca = input(f"Día {i+1} (T/O/P): ").strip().upper()
    if marca == "T":
        tardanzas += 1

print(f"Tardanzas totales del jugador: {tardanzas}")
