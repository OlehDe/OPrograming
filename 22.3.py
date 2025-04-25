class Point:
    def __init__(self, coordinate_x: int, coordinate_y: int, color: str = 'black'):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.color = color

points = [Point(0, 0, 'red') for _ in range(1000)]

print("Кількість точок у списку:", len(points))

points[2].coordinate_x = 10

print("Нова координата x третьої точки:", points[2].coordinate_x)
