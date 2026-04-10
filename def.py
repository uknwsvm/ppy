import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficher_point(self):
        print(f"({self.x}, {self.y})")

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def milieu_segment(self, other):
        mx = (self.x + other.x) / 2
        my = (self.y + other.y) / 2
        return Point(mx, my)

    def translation(self, deplacement):
        return Point(self.x + deplacement.dx, self.y + deplacement.dy)

    def projection_x(self):
        return Point(self.x, 0)

    def projection_y(self):
        return Point(0, self.y)


class Deplacement:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy


# Programme principal
A = Point(1, 2)
B = Point(4, 6)

print("Point A:")
A.afficher_point()

print("Point B:")
B.afficher_point()

# Distance
print("Distance:", A.distance(B))

# Milieu
M = A.milieu_segment(B)
print("Milieu:")
M.afficher_point()

# Projection
print("Projection de A sur X:")
A.projection_x().afficher_point()

# Déplacement
d = Deplacement(2, 3)

A2 = A.translation(d)
B2 = B.translation(d)

print("A après déplacement:")
A2.afficher_point()

print("B après déplacement:")
B2.afficher_point()