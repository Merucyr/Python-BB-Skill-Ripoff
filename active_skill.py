from skill import Skill
import skill_list
from defaults import zeroStatMods

# Mimics an active skill, these don't have any stat mods attatched to them
class Active_Skill(Skill):
    def __init__(self, id=None): 
        super().__init__(id)
        self._isActive = True

    @property
    def statMods(self): # We always return a zero'ed version of the stat mods
        return zeroStatMods.copy()

    def setStatMods(self):   # Don't have to store another table with zero-values so we can just make statmods = none on setting
        self._statMods = None
        
    def getDict(self):
        return skill_list.activeSkillDict
    
    def getIdPostfix(self):
        return "_active"