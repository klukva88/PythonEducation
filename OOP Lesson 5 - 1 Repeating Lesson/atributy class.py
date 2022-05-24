class TriangleChecker:
    def __init__(self, sidesList):
        self.sidesList = sidesList


    def is_triangle(self):
        for side in self.sidesList:
            if isinstance(side, str):
                return print("Введите положительные числа!")
            elif side <= 0:
                return print("Нужно вводить числа")
        if self.sidesList[0]+self.sidesList[1] > self.sidesList[2] and self.sidesList[1]+self.sidesList[2] > self.sidesList[0] and self.sidesList[0]+self.sidesList[2] > self.sidesList[1]:
            return print(f"Ура можно построить треугольник!")
        else:
            return print(f"Построить треугольник нельзя!")


triangle1 = TriangleChecker([2, 3, 4])
triangle1.is_triangle()
triangle1 = TriangleChecker([77, 3, 4])
triangle1.is_triangle()
triangle1 = TriangleChecker([2, 3, "Side 4"])
triangle1.is_triangle()
triangle1 = TriangleChecker([2, -3, 4])
triangle1.is_triangle()