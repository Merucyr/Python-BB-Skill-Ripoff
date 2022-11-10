from defaults import character_names
from random import choice
from skill_container import Skill_Container

class Character:
    def __init__(self):
        self.name = choice(character_names)
        self.skillContainer = Skill_Container()

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, val):
        self._name = val

    @property
    def skillContainer(self):
        return self._skillContainer
    
    @skillContainer.setter
    def skillContainer(self, val):
        self._skillContainer = val
