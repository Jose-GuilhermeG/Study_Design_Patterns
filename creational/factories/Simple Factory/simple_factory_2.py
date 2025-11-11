"""
Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método
que é responsável por criar objetos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory).

    Podem facilitar o processo de "cache" ou criação de "singletons" porque a
    fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no código

Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory

Nessa aula:
Simple Factory <- Uma espécie de Factory Method parametrizado
Simple Factory pode não ser considerado um padrão de projeto por si só
Simple Factory pode quebrar princípios do SOLID
"""
from abc import ABC, abstractmethod
from os import system


class Veiculo(
    ABC
):
    @abstractmethod
    def buscar_cliente(self) -> None :
        pass
    
class CarroLuxo(
    Veiculo
):
    def buscar_cliente(self)->None:
        print("Carro de luxo buscando cliente")
        
class CarroPopular(
    Veiculo
):
    def buscar_cliente(self):
        print("Carro popular buscando cliente")
        
class MotoLuxo(
    Veiculo
):
    def buscar_cliente(self)->None:
        print("Moto de luxo buscando cliente")
        
class MotoPopular(
    Veiculo
):
    def buscar_cliente(self):
        print("Moto popular buscando cliente")
        
        
class VeiculoFactory:
    
    def __init__(self , tipo:str) -> None:
        self.carro = self.get_carro(tipo)
        
    @staticmethod
    def get_carro(tipo : str) -> Veiculo:
        if tipo.lower() == "luxo":
            return CarroLuxo()
        elif tipo.lower() == "popular":
            return CarroPopular()
        elif tipo.lower() == "moto_luxo":
            return MotoLuxo()
        elif tipo.lower() == "moto_popular":
            return MotoPopular()
        
        raise Exception(f"Nenhum veiculo do tipo {tipo}")
    
    def buscar_cliente(self):
        self.carro.buscar_cliente()

if __name__ == "__main__" :
    while True:
        carros_disponiveis = ['luxo' , 'popular' , 'moto_luxo' , 'moto_popular']
        print("Escolha um carro:")
        for i in carros_disponiveis:
            print(" " + i.capitalize())
            
        carro_escolhido = input("Carro escolhido : ").lower()
        
        if carro_escolhido in carros_disponiveis:
            carro = VeiculoFactory(carro_escolhido)
            system("clear")
            carro.buscar_cliente()
            break
        
        system("clear")
        print("Digite uma escolha valida")