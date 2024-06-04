class Base:
    def __init__(self) -> None:
        self.a = "a"
        self.b = "b"
        self.c = "c"

    def A(self):
        print(self.a)

    def B(self):
        print(self.b)
    
    def C(self):
        print(self.c)

class Derived (Base):

    def __init__(self) -> None:
        self.a = "aa"
        super().__init__()
        self.c = "cc"

    def A(self):
        print(self.a)

    def B(self):
        self.b = "bb"
        super().B()
        print(self.b)

base = Base()
derived= Derived()

base.A()
derived.A()
print()
base.B() 
derived.B() 
base.C() 
derived.C() 
derived = base 
derived.C()

