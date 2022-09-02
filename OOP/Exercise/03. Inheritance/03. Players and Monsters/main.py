from project.elf import Elf
from project.hero import Hero

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)


# Output:
# H
# 4
# H of type Hero has level 4
# E of type Elf has level 4
# Hero
# E
# 4
