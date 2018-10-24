class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self._tuple1 = (x1, y1)
        self._tuple2 = (x2, y2)
        self._lenX = abs(x2 - x1)
        self._lenY = abs(y2 - y1)
        self._lenHyp = (self._lenX ** 2 + self._lenY ** 2) ** 0.5

    def area(self):
        return (self._lenX * self._lenY) / 2

    def get_corners(self):
        return self._tuple1, self._tuple2

    def perimeter(self):
        return self._lenX + self._lenY + self._lenHyp

    def intersects(self, g):
        times_between_coordinates = 0
        for i in range(2):
            if min(g.get_corners()[0][i], g.get_corners()[1][i]) <= self._tuple1[i] <= max(g.get_corners()[0][i], g.get_corners()[1][i]):
                times_between_coordinates += 1
        if times_between_coordinates == 2:
            return print("Rectangles overlap")
        else:
            return print("Rectangles do not overlap")

    def __str__(self):
        in_text = "Right angle rectangle with corners at " + str(self._tuple1) + ", " + str(self._tuple2)
        in_text += "\n The area equals " + str(self.area()) + " cubic length units"
        in_text += "\n The perimeter equals " + str(self.perimeter()) + " length units"
        return in_text
