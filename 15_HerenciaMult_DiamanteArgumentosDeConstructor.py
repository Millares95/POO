class A:
    def __init__(self,a) -> None:
        self.a = a 

class B(A):
    def __init__(self, a, b) -> None:
        super().__init__(self, a)
        self.b = b

class C (A):
    def __init__(self, a, c) -> None:
        super().__init__(self, a)
        self.c = c 

class D(B, C):
    def __init__(self, a, b, c) -> None:
        super().__init__(self, a, b)
        super(). __init__(self, a, c)

#-----otra--via-------------------------------------------------

class A :
    def __init__(self, a_param) -> None:
    # A esta clase "base" y no tiene antepasado para pasar
    #argumentos, por lo que no hay necesidad de **kwargs
        self.a = a_param

class B(A):
    def __init__(self, b_param,**kwargs) -> None:
        # Aqui solo se usa el parametro 'b_param'
        # y el resto se pasa al constructor de la clase 
        # devuelta por 'super()'
        super().__init__(**kwargs)
        self.b = b_param

class C(A):
    def __init__(self, _c_param, **kwargs) -> None:
        # Aquí, solo se usa el parámetro 'c_param', 
        # y el resto se pasa al constructor de la clase 
        # devuelta por 'super ()
        super().__init__(**kwargs)
        self.c = _c_param

class D(B,C):
    def __init__(self,a ,b ,c) -> None:
        # Los argumentos se nombran para poder usarlos de manera explícita 
        # en los constructores de las clases madre.
        super().__init__(a_param = a, b_param = b, c_param = c)
print(C.__mro__)