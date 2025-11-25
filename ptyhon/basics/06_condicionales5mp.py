"""
Bono de rendimiento según puntuación del entrenador (1 a 5):
>4 = 15%
>3 = 10%
>2 = 5%
>1 = 2%
1 o menos = sin bono
"""

salario = float(input("Salario del jugador: "))
rendimiento = float(input("Calificación del rendimiento (1-5): "))

if rendimiento > 4:
    bono = 0.15
elif rendimiento > 3:
    bono = 0.10
elif rendimiento > 2:
    bono = 0.05
elif rendimiento > 1:
    bono = 0.02
else:
    bono = 0

salario_final = salario + (salario * bono)

print(f"Salario final con bono: ${salario_final:.2f}")
