"""
Pide cuantos dias registraras 
para cada dia ingresa T(tarde) O(ok) P(permiso)
cuenta y muyestra tardanzas totales
"""
dias=int(input("¿Cuantos dias vas a cargar"))
tardes=0
for i in range(dias):
    marca = input(f"Dia {i+1} (T=tarde, O=ok, P=permiso)").strip().upper()
    if marca=="T":
        tardes+=1
    print(f"Tardanzas totales: {tardes}")