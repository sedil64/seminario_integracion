"""
Clasificación salarial:
< 10000 = Promesa
10000–30000 = Profesional
> 30000 = Estrella
"""

salario = float(input("Salario mensual del jugador: "))

if salario < 10000:
    categoria = "Promesa"
elif salario <= 30000:
    categoria = "Profesional"
else:
    categoria = "Estrella"

print(f"Categoría del jugador: {categoria}")
