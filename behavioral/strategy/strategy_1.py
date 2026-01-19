"""
Strategy é um padrão de projeto comportamental que tem
a intenção de definir uma família de algoritmos,
encapsular cada uma delas e torná-las intercambiáveis.
Strategy permite que o algorítmo varie independentemente
dos clientes que o utilizam.

Princípio do aberto/fechado (Open/closed principle)
Entidades devem ser abertas para extensão, mas fechadas para modificação
"""
from abc import ABC , abstractmethod

class Order:
    def __init__(self , total_price : float , discount : 'DiscountStrategy')->None:
        self._total = total_price
        self._discount = discount
        
    @property
    def total(self) -> float:
        return self._total        

    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)
    
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self , value : float)->float:
        pass
    
class TwentyPercent(DiscountStrategy):
    def calculate(self, value):
        return value - (value * 0.2)
    
class FiftyPercent(DiscountStrategy):
    def calculate(self, value):
        return value - (value * 0.5)
    
class NoDiscount(DiscountStrategy):
    def calculate(self, value):
        return value
    
class CustomDiscount(DiscountStrategy):
    def __init__(self,discount : int):
        self.discount = discount / 100
        
    def calculate(self, value):
        return value - (value * self.discount)
    
if __name__ == "__main__":
    twenty_percent = TwentyPercent()
    order = Order(1000,twenty_percent)
    
    print(order.total)
    print(order.total_with_discount)
    
    fifty_percent = FiftyPercent()
    order_2 = Order(1000 , fifty_percent)
    
    print(order_2.total)
    print(order_2.total_with_discount)
    
    zero_percent = NoDiscount()
    order_3 = Order(1000 , zero_percent)
    
    print(order_3.total)
    print(order_3.total_with_discount)
    
    five_percent = CustomDiscount(5)
    order_4 = Order(1000 , five_percent)
    
    print(order_4.total)
    print(order_4.total_with_discount)