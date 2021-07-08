import math

class Point:
    def __init__(self, x_ax, y_ax ):
        self.x_ax = x_ax
        self.y_ax = y_ax

    def show(self):
        print(f"coordinates are: x = {self.x_ax}; y = {self.y_ax}")

    def move(self, move_x, move_y):
        self.x_ax += move_x
        self.y_ax += move_y

    def distance(self, point2):
        dist = math.sqrt(((self.x_ax - point2.x_ax)**2) + ((self.y_ax - point2.y_ax)**2))
        print(dist)
if __name__ == "__main__":
    p1 = Point(1,3)
    p2 = Point(4,9)
    p1.show()
    p2.show()
    p1.move(-8, 12)
    p1.show()
    p1.distance(p2)