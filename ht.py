import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    # print("Механики игры: (W) - Вперёд, (S) - Назад, (A) - Влево, (D) - Вправо")


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














