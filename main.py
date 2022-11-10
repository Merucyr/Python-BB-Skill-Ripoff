from background import Background
from skill import Skill
from skill_container import Skill_Container
from active_skill import Active_Skill
from character import Character


container = Skill_Container()

thief = Background(id="thief")
poacher = Background(id="light_archer")
skill = Skill(id="slash")
active = Active_Skill("hand_to_hand")

thief.statMods["Health"] = 200
print(hex(id(skill.statMods)))
print(hex(id(thief.statMods)))
print(hex(id(active.statMods)))
print(skill.statMods)
print(thief.statMods)
print(active.statMods)

# container.addSkill(thief)
# container.addSkill(skill)
# container.addSkill(active)

# print(container.statMods)
# print(hex(id(container.getActiveSkills())))
# print(container.getUsableSkills()[0].name)

# char1 = Character()
# char2 = Character()

# print(char1.skillContainer)
# print(char2.skillContainer)

