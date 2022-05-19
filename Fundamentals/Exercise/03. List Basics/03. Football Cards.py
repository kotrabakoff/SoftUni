string = input().split(" ")
team_A = 11
team_B = 11
game_On = True

for i in string:
    if i[0] == "A":
        team_A -= 1
    elif i[0] == "B":
        team_B -= 1

    if team_A == 6 or team_B == 6:
        game_On = False
        break

print(f"Team A - {team_A}; Team B - {team_B}")

if game_On == False:
    print ("Game was terminated")
