"""Escriba un programa que pida edad,años de experiencia y 
si tiene titulo universitario
un candidato es elegible si tiene >= 21 años y experiencia >= 2 años o titulo
Muestra elegiblre o no elegible"""

edad = int(input("Ingrese su edad: "))
exp = int(input("Ingrese sus años de experiencia: "))

tiene_titulo = input("¿Tiene título universitario? s/n ").lower()=="s"


if (edad >= 21 and exp >= 2) or tiene_titulo=="s":
    print("Elegible")
else:
    print("No elegible")
