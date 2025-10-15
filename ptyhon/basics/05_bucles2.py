"""
Pide el numero de empleados y luego el sueldo de cada uno
suma y muestra la nomina total
"""

num_empleados = int(input("Ingrese el número de empleados: "))
nomina_total = 0
for i in range(num_empleados):
    sueldo = float(input(f"Ingrese el sueldo del empleado {i+1}: "))
    nomina_total += sueldo

print(f"La nómina total es: {nomina_total}")
