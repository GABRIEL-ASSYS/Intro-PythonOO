class Point:
    #defino o nome do método e em quem ele é aplicado, no caso "self"
    def reset(self):
        self.x = 0
        self.y = 0

#criar dois objetos ponto
p1 = Point()
p2 = Point()

#atribuo valores x e y para cada um dos pontos
p1.x = 5
p1.y = 4

p2.x = 3
p2.y = 6

#imprimo os valores de cada atributo para os pontos
print(p1.x, p1.y)
print(p2.x, p2.y)

#chamo o método reset da classe Point
p1.reset()
p2.reset()

print(p1.x, p1.y)
print(p2.x, p2.y)