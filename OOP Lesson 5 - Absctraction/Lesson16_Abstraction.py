from abc import ABC, abstractmethod
from math import pi, pow

class Figure(ABC):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @abstractmethod
    def findSquare(self):
        pass
    @abstractmethod
    def display(self):
        pass

class Triangle(Figure):
    def __init__(self, name, color, a, h):
        super().__init__(name, color)
        self.aSide = a
        self.height = h

    def findSquare(self):
        result = 0.5* self.aSide * self.height
        return result

    def display(self):
        print(f'Square of {self.name} with {self.color} color is {self.findSquare()}')

class Circle(Figure):
    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self.radius = radius

    def findSquare(self):
        result = pi * pow(self.radius, 2)

        return result

    def display(self):
        print(f'Square of {self.name} with {self.color} color is {self.findSquare():.2f} which Radius is {self.radius}')

class Square(Figure):
    def __init__(self, name, color, width, height):
        super().__init__(name, color)
        self.width = width
        self.height = height

    def findSquare(self):
        result = self.width * self.height

        return result

    def display(self):
        print(f'Square of {self.name} with {self.color} color is {self.findSquare()} and heigh {self.height} and '
              f'width is {self.width}')

def main():
    #figure1 = Figure('Some figure', 'Black')
    #Triangle
    figure2 = Triangle('Triangle', 'yellow', 5, 8)

    #Circle
    #153.93804002589985
    figure3 = Circle('Circle', 'pink', 7)

    #Square
    figure4 = Square('Square', 'red', 12, 15)


    print(figure2.findSquare())
    figure2.display()
    figure3.display()
    figure4.display()



if __name__ == '__main__':
    main()



