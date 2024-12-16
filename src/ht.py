import os

def clear_none():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear(player):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"HP - {player.health_points}   Defense - {player.defense_points}  Attack - {player.attack_points}  Ex - {player.ex}\n")

def clear_i(player):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"HP - {player.health_points}   Defense - {player.defense_points}  Attack - {player.attack_points}  Ex - {player.ex}\n")

def pr(text, val):
    while 1:
        print(text)
        inp = input()
        if inp in val:
            break
        else:
            print("Введите корректные значения")
            continue
    return inp
