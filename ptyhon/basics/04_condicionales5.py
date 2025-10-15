"""
pide salario y desempeño(1-5)
si el desempeño es
>4=15%
>3=10%
>2=5%
>1=2%
"""

salario=int(input("Coloque su salario"))
desempeno=int(input("Cual fue su desempeño"))

if desempeno > 4:
    bono = 0.15
    sueldo = salario * bono
    sueldo_final = salario + sueldo
    print(sueldo_final)
elif desempeno > 3:
    bono = 0.10
    sueldo = salario * bono
    sueldo_final = salario + sueldo
    print(sueldo_final)
elif desempeno > 2:
    bono = 0.05
    sueldo = salario * bono
    sueldo_final = salario + sueldo
    print(sueldo_final)    
elif desempeno > 1:
    bono = 0.02
    sueldo = salario * bono
    sueldo_final = salario + sueldo
    print(sueldo_final)

else:
    print(salario, "este es su salario sin bonificacion")
