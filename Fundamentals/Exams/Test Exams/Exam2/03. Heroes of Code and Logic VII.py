n = int(input())
hero_dict = {}

for i in range(0, n):
    hero = input().split(" ")
    hero_name = hero[0]
    hp = int(hero[1])
    mp = int(hero[2])
    if hp > 100:
        hp = 100
    if mp > 200:
        mp = 200
    value = [hp, mp]
    hero_dict[hero_name] = value

action = input()

while action != "End":
    action = action.split(" - ")
    command = action[0]
    name_command = action[1]

    if command == "CastSpell":
        mp_needed = int(action[2])
        spell_name = action[3]
        if name_command in hero_dict.keys():
            if hero_dict[name_command][1] > mp_needed:
                hero_dict[name_command][1] -= mp_needed
                print(f"{name_command} has successfully cast {spell_name} and now has {hero_dict[name_command][1]} MP!")
            else:
                print(f"{name_command} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        damage = int(action[2])
        attacker = action[3]
        if name_command in hero_dict.keys():
            hero_dict[name_command][0] -= damage
            if hero_dict[name_command][0] > 0:
                print(f"{name_command} was hit for {damage} HP by {attacker} and now has {hero_dict[name_command][0]} HP left!")
            else:
                hero_dict.pop(name_command)
                print(f"{name_command} has been killed by {attacker}!")

    elif command == "Recharge":
        amount_mp = int(action[2])
        if hero_dict[name_command][1] + amount_mp > 200:
            remainder = (hero_dict[name_command][1] + amount_mp) - 200
            amount_mp -= remainder
            hero_dict[name_command][1] = 200
        else:
            hero_dict[name_command][1] += amount_mp
        print(f"{name_command} recharged for {amount_mp} MP!")
    elif command == "Heal":
        amount_hp = int(action[2])
        if hero_dict[name_command][0] + amount_hp > 100:
            remainder = (hero_dict[name_command][0] + amount_hp) - 100
            amount_hp -= remainder
            hero_dict[name_command][0] = 100

        else:
            hero_dict[name_command][0] += amount_hp

        print(f"{name_command} healed for {amount_hp} HP!")
    action = input()

for key in hero_dict.keys():
    print(key)
    print(f"  HP: {hero_dict[key][0]}")
    print(f"  MP: {hero_dict[key][1]}")