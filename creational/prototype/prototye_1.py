"""
Especificar os tipos de objetos a serem criados
usando uma instância-protótipo e criar novos objetos
pela cópia desse protótipo
"""

from copy import deepcopy

class StringReprMixin:
    def __str__(self):
        params = "".join([f'{key} = {value} \n' for key , value in self.__dict__.items()])
        return f'{self.__class__.__name__}:\n{params}'
    
    def __repr__(self):
        return self.__str__()

class Person(StringReprMixin):
    def __init__(self , first_name : str , last_name : str)->None:
        self.first_name = first_name
        self.last_name = last_name
        self.addresses : list["Address"] = []
        
    def add_address(self , address : "Address") -> None:
        self.addresses.append(address)
        
    def copy(self) -> "Person":
        return deepcopy(self)
        
class Address(StringReprMixin):
    def __init__(self , street : str , number : int)->None:
        self.street = street
        self.number =number
        
if __name__ == "__main__" : 
    luiz = Person("Luiz","Miranda")
    endereco_luiz = Address("AV. Brasil",250)
    luiz.add_address(endereco_luiz)
    
    esposa_luiz = luiz.copy()
    esposa_luiz.first_name = "leticia"
    
    print(luiz)
    print(esposa_luiz)