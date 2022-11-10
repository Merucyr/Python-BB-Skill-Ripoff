from random import choice
# Actually a dict holding all of the backgrounds

backgroundDict = {
    "thief_background" : {      # background's ID
        "dispName" : "Thief",   # Display name (what user sees)
        "statMods" : {          # Any stat mods that occur 
            "Health" : -5, 
            "MeleeAttack" : 2, 
            "MeleeDefense" : 5, 
            "RangedAttack" : 0, 
            "RangedDefense" : 3, 
            "Bravery" : -2
        }
    },
    "warrior_background" : {
        "dispName" : "Warrior",
        "statMods" : {
            "Health" : 10, 
            "MeleeAttack" : 3, 
            "MeleeDefense" : 0, 
            "RangedAttack" : 0, 
            "RangedDefense" : 0, 
            "Bravery" : 0
        }
    },
    "light_archer_background" : { 
        "dispName" : "Poacher",
        "statMods" : {
            "Health" : -5, 
            "MeleeAttack" : -3, 
            "MeleeDefense" : -2, 
            "RangedAttack" : 7, 
            "RangedDefense" : 4, 
            "Bravery" : 0
        }
    }
}

# Kind of a hack, this would ideally be run when all backgrounds have been added to that backgroundDict
# Alternatively you could append to both, assuming you wanted multiple files to be able to add to dict/list
# Could trigger this in a function to be made, e.g. set allBackgrounds = None and do on load
allBackgrounds = list(backgroundDict)


# Takes in a list of dict keys we want to be able to pick from, e.g. ["light_archer"] would only pick that 1 bg
# No input uses all bgs, currently doesn't support weighting 
def getRandomBackground(bgList = allBackgrounds):
    idx = choice(bgList)
    try: 
        return backgroundDict[idx]
    except KeyError:
        print("Background Dict does not have a Key named:", idx)
        return None

def getBackground(id):
    try: 
        return backgroundDict[id]
    except KeyError:
        print("Background Dict does not have a Key named:", id)
        return None
