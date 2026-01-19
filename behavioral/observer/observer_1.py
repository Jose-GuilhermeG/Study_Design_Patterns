"""
O padrão Observer tem a intenção de
definir uma dependência de um-para-muitos entre
objetos, de maneira que quando um objeto muda de
estado, todo os seus dependentes são notificados
e atualizados automaticamente.

Um observer é um objeto que gostaria de ser
informado, um observable (subject) é a entidade
que gera as informações.
"""
from abc import ABC , abstractmethod

class IObservable(ABC):
    @abstractmethod
    def add_observer(self , observer: "IObserver")->None:
        pass
    
    @abstractmethod
    def remove_observer(self , observer : "IObserver") -> None:
        pass
    
    @abstractmethod
    def notify_observers(self)->None:
        pass
    
class WeatherStation(IObservable):

    def __init__(self):
        self.observers : list["IObserver"] = []
        self._state : dict = {}
    
    @property 
    def state(self)->dict:
        return self._state
    
    @state.setter
    def state(self,state_update : dict)->None:
        new_state : dict = { ** self._state , **state_update }
        
        if new_state != self._state:
            self._state = new_state
            self.notify_observers()
    def reset_state(self)->None:
        
        self._state = {}
    
    def add_observer(self , observer: "IObserver")->None:
        self.observers.append(observer)
    
    def remove_observer(self , observer : "IObserver") -> None:
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify_observers(self)->None:
        for observer in self.observers:
            observer.update()
            

class IObserver(ABC):
    @abstractmethod
    def update(self)->None:
        pass
    

class Smartphone(IObserver):
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'{self.name} o objeto {observable_name} '
              f'acabou de ser atualizado => {self.observable.state}')
        
class Notebook(IObserver):
    def __init__(self, observable: IObservable) -> None:
        self.observable = observable

    def show(self) -> None:
        state = self.observable.state
        print('Sou o note e vou fazer outra coisa com esses dados', state)

    def update(self) -> None:
        self.show()
        
if __name__ == "__main__":
    weather_station = WeatherStation()

    smartphone = Smartphone('iPhone', weather_station)
    outro_smartphone = Smartphone('Outro Smartphone', weather_station)
    notebook = Notebook(weather_station)

    weather_station.add_observer(smartphone)
    weather_station.add_observer(outro_smartphone)
    weather_station.add_observer(notebook)

    weather_station.state = {'temperature': '30'}
    weather_station.state = {'temperature': '32'}
    weather_station.state = {'humidity': '90'}

    weather_station.remove_observer(outro_smartphone)
    weather_station.reset_state()
