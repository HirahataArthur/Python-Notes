from rich import print, inspect
from classes import Quadrado, Circulo

q1 = Quadrado(12)
print(f"Area do quadrado de lado {q1.lado}: {q1.area()}")
print(f"Perimetro do quadrado de lado {q1.lado}: {q1.perimetro()}")

c1 = Circulo(20)
print(f"Area do circulo de raio {c1.raio}: {c1.area():.1f}")
print(f"Perimetro do circulo de raio {c1.raio}: [yellow]{c1.perimetro():.1f}[/]\n\n")