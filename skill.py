from defaults import dfStatMods
import skill_list

# Mimic-ing skills, essentially player modifiers in some way
class Skill:
    def __init__(self, id=None):
        self.id = id           # ID was useful for event checks, etc
        self.setStatMods()     # Technically all skills have stat mods
        self.setDefaultName()  # All skills have a display name, whether it's a background's name or etc


    # .id get/set
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id


    # .statMods get, the set shouldn't be called unless forcing an override ideally
    @property
    def statMods(self): #Returns actual dict not a copy
        return self._statMods

    def setStatMods(self, override=None):
        if override != None:
            self._statMods = override.copy()
        else:
            try:
                self._statMods = self.getDict()[self.id]["statMods"].copy()
            except KeyError:
                self._statMods = dfStatMods.copy()
                print("ID not found in dictionary: ", self.id, "of object: ", self, "in dict: ", self.getDict())


    # .name get/set 
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, val):
        self._name = val


    # sDN used for setting the actual display name relative to the dict, could override this by using the name setter
    def setDefaultName(self):
        self.name = self.getDict()[self.id]["dispName"]

    # getDict convenient, we use dicts to hold our keyID : skillInformation
    # using this we can generalize all of our dict calls instead of having to pass it in etc
    # because all backgrounds would come from the backgroundDict, all skills from skillDict, etc
    def getDict(self):
        return skill_list.skillDict