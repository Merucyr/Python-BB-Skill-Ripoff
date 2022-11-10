from skill import Skill
import background_list

# Mimic-ing Backgrounds from BB (Backgrounds should be treated like skills but with separate IDs)
class Background(Skill):
    def __init__(self, id=None): # If we don't pump in a background id it'll get something totally random
        
        # bg = None
        # if id != None:
        #     bg = background_list.getBackground(id)
            
        # if bg == None: # If getting a specific bg fails OR if it was none, we reach here
        #     bg = background_list.getRandomBackground()

        super().__init__(id)
        # self.setID(id)
        # self.setStatMods()

    def getDict(self):
        return background_list.backgroundDict

    def getIdPostfix(self):
        return "_background"