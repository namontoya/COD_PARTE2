import math

class Circulo:
  def __init__(self, radio):
    self.radio = radio

  def calcular_area(self):
    area = math.pi * self.radio ** 2
    return area

  def calcular_perimetro(self):
    perimetro = 2 * math.pi * self.radio
    return perimetro


class Rectangulo:
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def calcular_area(self):
    area = self.base * self.altura
    return area

  def calcular_perimetro(self):
    perimetro = 2 * self.base + 2 * self.altura
    return perimetro


class Cuadrado:
  def __init__(self, longitud):
    self.longitud = longitud

  def calcular_area(self):
    area = self.longitud ** 2
    return area

  def calcular_perimetro(self):
    perimetro = self.longitud * 4
    return perimetro


class TrianguloRectangulo:
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def calcular_area(self):
    area = (self.base * self.altura) / 2
    return area

  def calcular_hipotenusa(self):
    hipotenusa = math.sqrt((self.base) ** 2 + (self.base) ** 2)
    return hipotenusa

  def calcular_perimetro(self):
    perimetro = self.base + self.altura + self.calcular_hipotenusa()
    return perimetro

  def calcular_tipo_triangulo(self):
    if self.base == self.altura and self.altura == self.calcular_hipotenusa():
      return "equilatero"
    elif self.base == self.altura or self.altura == self.calcular_hipotenusa() or self.base == self.calcular_hipotenusa():
      return "isosceles"
    else:
       return "escaleno"


circulo = Circulo(5)
rectangulo = Rectangulo(2, 6)
cuadrado = Cuadrado (4)
triangulo_rectangulo = TrianguloRectangulo(7, 4)
print(f"El área del círculo es: {circulo.calcular_area()}")
print(f"El perímetro del círculo es: {circulo.calcular_perimetro()}")
print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
print(f"El perímetro del rectángulo es: {rectangulo.calcular_perimetro()}")
print(f"El área del cuadrado es: {cuadrado.calcular_area()}")
print(f"El perímetro del cuadrado es: {cuadrado.calcular_perimetro()}")
print(f"El área del triángulo rectángulo es: {triangulo_rectangulo.calcular_area()}")
print(f"El perímetro del triángulo rectángulo es: {triangulo_rectangulo.calcular_perimetro()}")
print(f"El tipo de triángulo es: {triangulo_rectangulo.calcular_tipo_triangulo()}")
