experience = float(input())
battles_count = int(input())
current_battle = 0
current_experience = 0

for i in range(0, battles_count):
    new_experience = float(input())
    current_experience += new_experience
    current_battle += 1
    if current_battle % 3 == 0:
        current_experience += new_experience * 15 / 100
    if current_battle % 5 == 0:
        current_experience -= new_experience * 10 / 100
    if current_battle % 15 == 0:
        current_experience += new_experience * 5 / 100
    if current_experience >= experience:
        break

difference = experience - current_experience

if current_experience >= experience:
    print(f"Player successfully collected his needed experience for {current_battle} battles.")
else:
    print(f"Player was not able to collect the needed experience, {difference:.2f} more needed.")