class A:
    def __init__(self, a_atribute):
        self.a_atr = a_atribute

    def display(self):
        print('Hello from A')

class B:
    def __init__(self, b_atribute):
        self.b_atr = b_atribute

    def countSmth(self):
        print('I am counting.. from class B')

class C(A):
    def display2(self):
        print('Hello2')

class D(A,B):
    def __init__(self, somed, a, b):
        super().__init__(a)
        B.__init__(self,b)

        self.somed = somed

    def display3(self):
        # super().display()
        # super().display2()
        # super().countSmth()
        super().display()
        super().countSmth()
        A.display(self)
        B.countSmth(self)
        print(f'Hello from C')

def main():
    a = A('sds')
    a.display()

    d = D('d1','a1','b1')
    d.display3()

    print(D.mro())


if __name__ == '__main__':
    main()



