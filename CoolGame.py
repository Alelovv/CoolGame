import random
import time
import os
import keyboard
import ht
import threading

ht.clear()




class Player:
    def __init__(self):
        self.name = None

        self.choice = None

        self.attack_points = 0
        self.defense_points = 0
        self.health_points = 0

        self.character = {
            1: {'attack':random.randint(5, 8),
                'defense':random.randint(4, 7),
                'health':random.randint(30, 35),
                "item": None,
                 "name" : 'Силач'},

            2: {'attack':random.randint(7, 10),
                'defense':random.randint(3, 5),
                'health':random.randint(20, 28),
                "item": None,
                 "name" : "Странник"},

            3: {'attack':random.randint(2, 6),
                'defense':random.randint(8, 18),
                'health':random.randint(30, 50),
                "item": "зелье здоровья",
                 "name" : "Травник"}
        }

        self.ex = 0
        self.inv = {}

    def attack(self, value, enemy):
        enemy.health_points -= value

    def get_attack(self, value):
        self.health_points -= value

class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health_points = health
        self.attack_points = attack
        self.defense_points = defense

    def attack(self, value, player):
        player.health_points -= value

    def get_attack(self, value):
        self.health_points -= value




class Play:
    def __init__(self):
        self.player = Player()
        self.items = ["зелье здоровья", "зелье атаки", 'ключ']
        self.staff = {"зелье здоровья": lambda:self.player.health_points == self.player.health_points + 1}
        self.locations = []
        self.items_count = 0
        self.running = True

    def random_staff(self):
        self.items_count += 1
        self.player.inv[f"item{self.items_count}"] = random.choice(self.items)

    def open_inv(self):
        if not self.player.inv:
            print("Пусто")
        else:
            for item in self.player.inv.values():
                print(f'-{item}')

    def key_monitoring(self):
        while self.running == True:
            if keyboard.is_pressed('i'):
                self.open_inv()
                keyboard.wait('esc')
            elif keyboard.is_pressed('q'):
                print("\nВы завершили игру! До встречи.")
                self.running = False
                break


    def start(self):
        print('Добро пожаловать в CoolGame')

        while True:
            self.player.name = input("Введите никнейм:\n")
            ht.clear()
            print(f"{self.player.name}, cейчас тебе предстоит выбрать класс. В зависимости от выбора, твой персонаж с большей вероятностью будет "
                  "\nобладать соответстующими характеристиками, которые определяются рандомом в заданных диапазонах\n")
            input("Нажмите [Enter], чтобы продолжить.")
            ht.clear()

            i = None
            while i != 'y':
                self.player.choice = int(ht.pr("Выберите класс:\n  1 - Силач(Повышенная атака и защита, но проблемы с здоровьем),\n  2 - Странник(Повышеная ловкость и здоровье, но практически отсутствует защита),\n  3 - Травник(имеет в запасе зелье здоровья, усредненные характеристики)", ['1', '2', '3']))
                ht.clear()
                i = ht.pr(f"Вы уверены, что хотите выбрать класс {self.player.character[self.player.choice]["name"]}?\n (y) - Да , (n) - Нет\n", ['y', 'n'])
                ht.clear()
                if i == 'y':
                    break
                elif i == 'n':
                    continue


            ht.clear()
            self.player.attack_points = self.player.character[self.player.choice]['attack']
            self.player.defense_points = self.player.character[self.player.choice]['defense']
            self.player.health_points = self.player.character[self.player.choice]['health']

            print(f"{self.player.name}, ты очнулся в сырой траве, вокруг всё окутано густым туманом. Тепло земли под\n "
                  "тобой смешивается с холодным воздухом, от которого пробирает дрожь.\n Единственный звук — это шорох листвы где-то вдалеке\n")
            input("Нажмите [Enter], чтобы продолжить.")
            ht.clear()
            input_thread = threading.Thread(target=self.key_monitoring, daemon=True)
            input_thread.start()


            print('Начальная локация: Тропа\n')
            p = False
            while p == False:
                action = ht.pr("(b) - Исследовать, (h) - Продолжить путь:", ['b', 'h'])
                if action == "h":
                    print("Я настоятельно бы порекомендовал изменить выбор")
                    continue

                elif action == "b":
                    Play.random_staff(self)
                    print(f"Вы по случайным стечениям обстоятельств нашли сундук, в котором находится: {self.player.inv[f"item{self.items_count}"]}!\n"
                          f"Теперь у вас появляется шанс находить сундуки с вещами, шанс появления сундука напрямую зависит от вашего колличества опыта(не более 50)")
                    p = True


if __name__ == "__main__":
    test = Play()
    test.start()
