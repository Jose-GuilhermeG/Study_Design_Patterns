"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
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
        
        
class VeiculoFactory(
    ABC
):
    @staticmethod
    @abstractmethod
    def get_carro(tipo : str) -> Veiculo:
        pass
    
class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo):
        if tipo.lower() == "luxo":
            return CarroLuxo()
        elif tipo.lower() == "popular":
            return CarroPopular()
        elif tipo.lower() == "moto_luxo":
            return MotoLuxo()
        elif tipo.lower() == "moto_popular":
            return MotoPopular()
        
        raise Exception(f"Nenhum veiculo do tipo {tipo}")
    
class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo):
        if tipo.lower() == "popular":
            return CarroPopular()
        elif tipo.lower() == "moto_popular":
            return MotoPopular()
        
        raise Exception(f"Nenhum veiculo do tipo {tipo}")
    

if __name__ == "__main__" :
    while True:
        veiculos_disponiveis_zona_norte = ['luxo' , 'popular' , 'moto_luxo' , 'moto_popular']
        print("Escolha um carro:")
        for i in veiculos_disponiveis_zona_norte:
            print(" " + i.capitalize())
            
        carro_escolhido = input("Carro escolhido : ").lower()
        
        if carro_escolhido in veiculos_disponiveis_zona_norte:
            carro = ZonaNorteVeiculoFactory.get_carro(carro_escolhido)
            system("clear")
            carro.buscar_cliente()
            break
        
        system("clear")
        print("Digite uma escolha valida")