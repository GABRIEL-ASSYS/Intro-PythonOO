import math

class Point:
    #defino os valores iniciais dos atributos
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    #defino um método para mover
    def move(self, x, y):
        self.x = x
        self.y = y

    #defino o nome do método "reset" e em quem ele é aplicado "self"
    def reset(self):
        self.x = 0
        self.y = 0

    #defino um método para calcular a distância entre dois pontos
    def calculate_distance(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

#criar dois objetos ponto
p1 = Point(5,4)
p2 = Point(3,6)

#imprimo os valores de cada atributo para os pontos
print(p1.x, p1.y)
print(p2.x, p2.y)

#chamo o método reset da classe Point
p1.reset()
p2.reset()

print(p1.x, p1.y)
print(p2.x, p2.y)

#mover o ponto p1 para a posição (10, 15)
p1.move(10, 15)

print(p1.x, p1.y)

#distância entre o ponto p1 e p2
print(p1.calculate_distance(p2))