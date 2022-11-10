from background import Background
from skill import Skill
from skill_container import Skill_Container
from active_skill import Active_Skill
from character import Character


container = Skill_Container()

thief = Background(id="thief_background")
poacher = Background(id="light_archer_background")
skill = Skill(id="slash_skill")
active = Active_Skill("hand_to_hand_active")

print(skill.statMods)
print(thief.statMods)
print(active.statMods)

container.addSkill(thief)
container.addSkill(skill)
container.addSkill(active)

print(container.statMods)
print(container.getActiveSkills()[0].name)
print(container.getUsableSkills()[0].name)

char1 = Character()
char2 = Character()

print(char1.skillContainer)
print(char2.skillContainer)

