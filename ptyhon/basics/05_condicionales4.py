"""
Pide el salario y clasifica el cargo
<1000 junior
1000-2000 semi junior
>2000 senior
"""

salario=int(input("Cuanto recibes de salario"))
if salario < 1000:
    puesto="junior"
elif salario <= 2000:
    puesto="Semi junior"
else:
    puesto="Senior"
    
print(f"{puesto}")
