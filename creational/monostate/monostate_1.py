"""
Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.
"""

class StringReprMixin:
    def __str__(self):
        params = "".join([f'{key} = {value} \n' for key , value in self.__dict__.items()])
        return f'{self.__class__.__name__}:\n{params}'
    
    def __repr__(self):
        return self.__str__()
    

class MonoStateSimple(
    StringReprMixin
):
    _state = {
        "x" : 10,
        "y" : 20
    }
    
    def __init__(self , nome = None):
        self.__dict__ = self._state
        
        if nome:
            self.nome = nome
        
        
if __name__ ==  "__main__":
    m1 = MonoStateSimple("teste")
    print(m1)