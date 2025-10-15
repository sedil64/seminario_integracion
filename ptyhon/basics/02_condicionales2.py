"""
Sistema que poda pago por hora y horas trabajadas. las primeras 40h son normales, 
las horas extras se pagan al 150% 
cakcula y muestra el total semanal
"""


pago_hora = float(input("Ingrese el pago por hora: "))
horas_trabajadas = int(input("Ingrese las horas trabajadas en la semana:) "))

if horas_trabajadas <= 40:
    total_semanal = pago_hora * horas_trabajadas
else:
    horas_extras = horas_trabajadas - 40
    total_semanal = (pago_hora * 40) + (pago_hora * 1.5 * horas_extras)
