class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def inc(self):
        self.x += 1
        self.y += 1
        self.z += 1

    def dec(self):
        self.x -= 1
        self.y -= 1
        self.z -= 1

    def show(self):
        print(f"Point: ({self.x}, {self.y}, {self.z})")

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __lt__(self, other):
        return self.x < other.x

    def __gt__(self, other):
        return self.x > other.x

    def __eq__(self, other):
        return self.x == other.x

    def quadrant(self):
        if self.x > 0 and self.y > 0:
            print("Quadrant 1")
        elif self.x < 0 and self.y > 0:
            print("Quadrant 2")
        elif self.x < 0 and self.y < 0:
            print("Quadrant 3")
        elif self.x > 0 and self.y < 0:
            print("Quadrant 4")
        else:
            print("On an axis")

    def collinear(self, other):
        if self.x * other.y == self.y * other.x:
            print("Collinear Points")
        else:
            print("Not Collinear")

# Testing the class
p1 = Point(2, 3, 4)
p2 = Point(1, 2, 3)

p1.show()
p1.inc()
p1.show()
p1.dec()
p1.show()

p3 = p1 + p2
p3.show()

print(p1 < p2)
print(p1 > p2)
print(p1 == p2)

p1.quadrant()
p1.collinear(p2)