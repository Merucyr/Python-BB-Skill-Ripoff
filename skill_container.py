from defaults import dfStatMods

# All skills really had a function that gave you skill modifications, but here we're cheating and
# using just the dicts and assuming every skill can modify the base stats in some way
class Skill_Container:
    def __init__(self):
        self.resetSkills()
    
    @property
    def skills(self):
        return self._skills

    def addSkill(self, toAdd):
        self._skills.append(toAdd)

    def resetSkills(self): #On creation we want to just set the skills to nothing but maybe other times too?
        self._skills = []

    @property
    def statMods(self):
        sM = dfStatMods.copy() #Copy the base stat so we don't configs
        for s in self.skills:
            sM["Health"]         += s.statMods["Health"]
            sM["MeleeAttack"]    += s.statMods["MeleeAttack"]
            sM["MeleeDefense"]   += s.statMods["MeleeDefense"]
            sM["RangedAttack"]   += s.statMods["RangedAttack"]
            sM["RangedDefense"]  += s.statMods["RangedDefense"]
            sM["Bravery"]        += s.statMods["Bravery"]
        return sM #Because we copied we don't need to return a copy