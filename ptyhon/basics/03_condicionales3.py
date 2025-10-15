"""
Vacaciones por antiguedad 
Pide años de antiguedad y muestra dias de vacaciones segun los años
<1=0
<3=3
<5=10
>=5=15

"""

anos_antiguedad = int(input("Ingrese sus años de antiguedad: "))
if anos_antiguedad < 1:
    dias_vacaciones = 0
elif anos_antiguedad < 3:
    dias_vacaciones = 3
elif anos_antiguedad < 5:
    dias_vacaciones = 10
else:
    dias_vacaciones = 15
print(f"El empleado tien {dias_vacaciones} días de vacaciones.")

