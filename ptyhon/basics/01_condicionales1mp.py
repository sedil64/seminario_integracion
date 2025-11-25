"""
Un jugador es elegible para fichaje si:
- Tiene >= 18 años y experiencia >= 2 años,
  O si tiene contrato universitario (semillero).
"""

edad = int(input("Edad del jugador: "))
exp = int(input("Años de experiencia en ligas menores: "))
tiene_contrato = input("¿Tiene contrato universitario/semillero? (s/n): ").lower() == "s"

if (edad >= 18 and exp >= 2) or tiene_contrato:
    print("El jugador es elegible para fichaje.")
else:
    print("El jugador NO es elegible.")
