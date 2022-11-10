from background import Background
from skill import Skill
from skill_container import Skill_Container


container = Skill_Container()

thief = Background(id="thief_background")
skill = Skill(id="slash_skill")

print(skill.statMods)
print(thief.statMods)

container.addSkill(thief)
container.addSkill(skill)

print(container.statMods)

