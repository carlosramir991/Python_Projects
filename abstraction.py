
from abc import ABC, abstractmethod

class calories(ABC):

    def maint(self,calories):
        print("Your maintenance calories today will be {}!".format(calories))

    @abstractmethod
    def lose(self,calories):
        pass

class losingw(calories):

    
    def lose(self,calories):
        calories = (calories -250)
        print("In order to lose weight you need to eat {} calories!".format(calories))

        
obj = losingw()
obj.maint(2000)
obj.lose(2000)
