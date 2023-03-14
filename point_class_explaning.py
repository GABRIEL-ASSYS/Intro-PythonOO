import math

class Point:
    "Representa um ponto em coordenadas de duas dimensões"
    def __init__(self, x=0, y=0):
        """
        Inicializa a posição do ponto. As coordenadas x e y podem ser especificadas. 
        Se elas não forem especificadas, retornam a posição de origem.
        """
        self.x = x
        self.y = y

    "Move o ponto para uma nova localização no espaço"
    def move(self, x, y):
        self.x = x
        self.y = y

    "Reseto o ponto para a origem: 0,0"
    def reset(self):
        self.x = 0
        self.y = 0

    """
    Calcula a distância deste ponto para um segundo ponto passado como
    parâmetro. Essa função utiliza o Teorema de Pitágoras para calculo
    da distância. A distância é retornada como float.
    """
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