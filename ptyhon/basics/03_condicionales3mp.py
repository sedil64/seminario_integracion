"""
Vacaciones según años en el club.
<1 año: 0 días
<3 años: 3 días
<5 años: 10 días
>=5 años: 15 días
"""

anios = int(input("Años del entrenador en el club: "))

if anios < 1:
    dias = 0
elif anios < 3:
    dias = 3
elif anios < 5:
    dias = 10
else:
    dias = 15

print(f"Días de descanso asignados: {dias}")
