class Point2D:
    def __init__(self, x, y) -> None:
        self.x = x 
        self.y = y

    def translation (self, a, b):
        self.x += a
        self.y += b

    def __str__(self):
        return "X : {}; Y: {}".format(self.x, self.y)

a = Point2D(1, 2)
print(f"A = {a}")

a.translation(-1, -2)
print(f'A = {a}')

b = Point2D(-3, 0)
b.translation(5, -1)
print(f'B = {b}')

class Point3D(Point2D):
    def __init__(self, x, y, z) -> None:
        super().__init__(x, y)
        self.z = z

    def translation(self, a, b, c):
        super().translation(a, b)
        self.z += c
        
    def __str__(self):
        return f'{super().__str__()},Z:{self.z}'



c = Point3D(1,5,-3)
c.translation(0, -2, 1)
print("C = {}".format(c))