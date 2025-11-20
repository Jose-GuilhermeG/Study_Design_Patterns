"""
Builder é um padrão de criação que tem a intenção
de separar a construção de um objeto complexo
da sua representação, de modo que o mesmo processo
de construção possa criar diferentes representações.

Builder te da a possibilidade de criar objetos passo-a-passo
e isso já é possível no Python sem este padrão.

Geralmente o builder aceita o encadeamento de métodos
(method chaining).
"""

from abc import ABC , abstractmethod

class StringReprMixin:
    def __str__(self):
        params = "".join([f'{key} = {value} \n' for key , value in self.__dict__.items()])
        return f'{self.__class__.__name__}:\n{params}'
    
    def __repr__(self):
        return self.__str__()

class User(
    StringReprMixin
):
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone_numbers = []
        self.addresses = []
        
    
class IUserBuilder(
    ABC
):
    @property
    @abstractmethod
    def result(self) -> None:
        pass
    
    @abstractmethod
    def add_firstname(self , firstname : str) -> None:
        pass
    
    @abstractmethod
    def add_lastname(self , lastname : str) -> None:
        pass
    
    @abstractmethod
    def add_age(self , age : int) -> None:
        pass
    
    @abstractmethod
    def add_phone_numbers(self , phones : list ) -> None:
        pass
    
    @abstractmethod
    def add_addresses(self , addresses : list ) -> None:
        pass
    
class UserBuilder(
    IUserBuilder
):
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.__result = User()
        
    @property
    def result(self) -> None:
        result_data = self.__result
        self.reset()
        return result_data
    
    def add_firstname(self , firstname : str):
        self.__result.firstname = firstname
        return self
    
    def add_lastname(self , lastname : str):
        self.__result.lastname = lastname
        return self
    
    def add_age(self , age : int):
        self.__result.age = age
        return self
    
    def add_phone_numbers(self , phones : list ):
        self.__result.phone_numbers = phones
        return self
    
    def add_addresses(self , addresses : list ):
        self.__result.addresses = addresses
        return self
        
class UserDirector:
    def __init__(self , builder : UserBuilder) ->None:
        self.__builder = builder
        
    def create_with_age(self , firstname : str , lastname : str , age : int):
        self.__builder.add_firstname(firstname).add_lastname(lastname).add_age(age)
        return self.__builder.result
    
    def create_with_addresses(self , fistname : str , lastname : str , address : list):
        self.__builder.add_firstname(fistname).add_lastname(lastname).add_addresses(address)
        return self.__builder.result
    
    
if __name__ == '__main__':
    builder = UserBuilder()
    director = UserDirector(builder)
    user_1 = director.create_with_age("José" , "Guilherme" , 18)
    user_2 = director.create_with_addresses("João" , "Felipe" , [
        "Avenida Brasil "
    ])
    print(user_1)
    print(user_2)