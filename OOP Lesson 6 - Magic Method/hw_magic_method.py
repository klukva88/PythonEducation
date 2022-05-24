class Area:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def findArea(self):
        return self.height * self.width

    def __lt__(self, other):
        if isinstance(other, Area):
            return self.findArea() < other.findArea()

        return False

    def __gt__(self, other):
        if isinstance(other, Area):
            return self.findArea() > other.findArea()
        else:
            return False

    def __eq__(self, other):
        if isinstance(other, Area):
            return self.findArea() == other.findArea()
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Area):
            return self.findArea() <= other.findArea()
        else:
            return False


    def __ge__(self, other):
        if isinstance(other, Area):
            return self.findArea() >= other.findArea()
        else:
            return False

def main():
    area1 = Area(12,30) #360
    area2 = Area(15,20) #300

    print(area1 > area2)
    print(area1 < area2)
    print(area1 == area2)
    print(area1 >= area2)
    print(area1 <= area2)


if __name__ == '__main__':
    main()
