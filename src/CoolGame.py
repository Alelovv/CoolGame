import random
import time
import os
import ht

ht.clear_none()

class Player:
    def __init__(self):
        self.name = None
        self.choice = None
        self.attack_points = 0
        self.defense_points = 0
        self.health_points = 0
        self.character = {
            1: {'attack': random.randint(5, 8),
                'defense': random.randint(4, 7),
                'health': random.randint(30, 35),
                "item": None,
                "name": 'Силач'},
            2: {'attack': random.randint(7, 10),
                'defense': random.randint(3, 5),
                'health': random.randint(20, 28),
                "item": None,
                "name": "Странник"},
            3: {'attack': random.randint(2, 6),
                'defense': random.randint(8, 18),
                'health': random.randint(30, 50),
                "item": "зелье здоровья",
                "name": "Травник"}
        }
        self.ex = 0
        self.inv = {}

    def attack(self, enemy, value):
        enemy.health_points -= value


    def get_attack(self, value):
        self.health_points -= value

    def dodge(self):
        chance = random.random()
        return chance < 0.4

    def use_item(self, item):
        if item == "зелье здоровья":
            self.health_points += 3
            print(f'Вы восстановили 3 очка здоровья!')
        elif item == "зелье атаки":
            self.attack_points += 1
            print(f'Вы увеличили атаку на 1 еденицу!')
        else:
            print("Предмет не найден!")
        a = input("Нажмите [Enter], чтобы продолжить...")
        ht.clear_i(self)

class Enemy:
    def __init__(self, name, attack, defense, health, exp_reward, loot):
        self.name = name
        self.attack_points = attack
        self.defense_points = defense
        self.health_points = health
        self.exp_reward = exp_reward
        self.loot = loot

    def attack(self, player):
        damage = max(0, self.attack_points - player.defense_points)
        print(f"{self.name} наносит {damage} урона!")
        player.health_points -= damage

    def dodge(self):
        chance = random.random()
        return chance < 0.2     


class Play:
    def __init__(self):
        self.player = Player()
        self.items = ["зелье здоровья", "зелье атаки", 'ключ']
        self.items_count = 0
        self.running = True
        self.enemies = [
            Enemy("Дикий волк", attack=5, defense=3, health=15, exp_reward=10, loot="зелье здоровья"),
            Enemy("Разбойник", attack=7, defense=4, health=20, exp_reward=15, loot="зелье атаки"),
            Enemy("Большой медведь", attack=10, defense=5, health=25, exp_reward=20, loot=None)
        ]

    def random_enemy(self):
        return random.choice(self.enemies)

    def random_staff(self):
        self.items_count += 1
        self.player.inv[f"item{self.items_count}"] = random.choice(self.items)

    def open_inv(self):
        ht.clear_i(self.player)
        while 1:
            print("Ваш инвентарь:                   (q) - Выйти")
            if not self.player.inv:
                print("Пусто")
            else:
                for index, item in enumerate(self.player.inv.values(), 1): 
                    print(f'{index} - {item}')

            itm = ht.pr("\nВыберите предмет или нажмите 'q' для выхода: ", list(self.player.inv.values()) + ['q'])
            if itm == 'q':
                ht.clear_i(self.player)
                break

            p = ht.pr(f"Вы уверены, что хотите использовать {itm}? (y) - Да , (n) - Нет", ['y', 'n', 'q'])
            if p == 'y':
                self.player.use_item(itm)

                for key, value in self.player.inv.items():
                    if value == itm:
                        del self.player.inv[key]
                        break
            elif p == 'n':
                ht.clear_i(self.player)
                continue
            elif p == 'q':
                ht.clear_i(self.player)
                break
            ht.clear_i(self.player)
            break

    def fight(self):
        ht.clear_i(self.player)
        enemy = self.random_enemy()
        print(f"Вы встретили врага: {enemy.name}!\n")

        while enemy.health_points > 0 and self.player.health_points > 0:
            print(f"{enemy.name}: HP = {enemy.health_points} | Атака = {enemy.attack_points} | Защита = {enemy.defense_points}\n")
            
            action = ht.pr("(a) - Атаковать, (d) - Увернуться, (i) - Открыть инвентарь", ['a', 'd', 'i'])
            l = False
            if action == 'a':
                ht.clear_i(self.player)
                if not enemy.dodge():  # Враг может увернуться от атаки
                    if enemy.defense_points > 0:
                        enemy.defense_points -= self.player.attack_points  # Уменьшаем защиту врага
                        if enemy.defense_points < 0:
                            enemy.health_points = enemy.health_points - self.player.attack_points + self.player.defense_points
                            enemy.defense_points = 0
                            ht.clear_i(self.player)
                            print(f"Вы атаковали {enemy.name}. Защита врага теперь: {enemy.defense_points} HP: {enemy.health_points}.")
                        else:
                            enemy.health_points = enemy.health_points - self.player.attack_points
                            ht.clear_i(self.player)
                            print(f"Вы атаковали {enemy.name}. Защита врага теперь: {enemy.defense_points} HP: {enemy.health_points}.")
                    elif self.enemy.defense_points == 0:
                        enemy.defense_points = 0  
                        enemy.health_points -= self.player.attack_points 
                        ht.clear_i(self.player)       
                        print(f"Вы атаковали {enemy.name}. Защита врага теперь: {enemy.defense_points} HP: {enemy.health_points}.")  
                    elif enemy.defense_points < 0:
                        enemy.health_points = enemy.health_points - self.player.attack_points + self.player.defense_points
                        enemy.defense_points = 0      
                        ht.clear_i(self.player)       
                        print(f"Вы атаковали {enemy.name}. Его здоровье: {enemy.health_points}")
                else:
                    print(f"{enemy.name} увернулся от вашей атаки!")

            
            elif action == 'd':
                ht.clear_i(self.player)
                if self.player.dodge():  # Игрок может увернуться только если выбрал "d"
                    print("Вы успешно увернулись от атаки врага!")
                    l = True
                    continue  # Пропускаем ход врага, если игрок увернулся
                else:
                    print("Вы не увернулись от атаки врага!")

            elif action == 'i':
                ht.clear_i(self.player)
                self.open_inv()
                continue

            print("Теперь ход врага...")
            input("Нажмите [Enter], чтобы враг совершил свой ход...")
            ht.clear_i(self.player)

            if enemy.health_points > 0:
                if l == False: 
                    if self.player.defense_points > 0:
                        self.player.defense_points -= enemy.attack_points 
                        if self.player.defense_points < 0: 
                            self.player.health_points = self.player.health_points - enemy.attack_points + self.player.defense_points
                            self.player.defense_points = 0
                            ht.clear_i(self.player)
                            print(f"Вас атаковал {enemy.name}. Вы получили {enemy.attack_points} урона!.")
                        else:
                            self.player.health_points = self.player.health_points - enemy.attack_points
                            ht.clear_i(self.player)
                            print(f"Вас атаковал {enemy.name}. Вы получили {enemy.attack_points} урона!.")
                    elif self.player.defense_points == 0:
                        self.player.defense_points = 0  
                        self.player.health_points -= enemy.attack_points
                        ht.clear_i(self.player)        
                        print(f"Вас атаковал {enemy.name}. Вы получили {enemy.attack_points} урона!.")   
                    elif self.player.defense_points < 0:
                        self.player.health_points -= enemy.attack_points - self.player.defense_points
                        self.player.defense_points = 0
                        ht.clear_i(self.player)
                        print(f"Вас атаковал {enemy.name}. Вы получили {enemy.attack_points} урона!.")


                else:
                    print(f"{enemy.name} пытался атаковать, но вы увернулись!")
            l == False

            time.sleep(2.5)
            ht.clear_i(self.player)

        if self.player.health_points > 0:
            print(f"Вы победили {enemy.name}! Получено опыта: {enemy.exp_reward}")
            self.player.ex += enemy.exp_reward
            if enemy.loot:
                self.items_count += 1
                self.player.inv[f"item{self.items_count}"] = enemy.loot
                print(f"Вы получили предмет: {enemy.loot}!")
        else:
            print("Вы проиграли! Игра окончена.")
            self.running = False

        input("Нажмите [Enter], чтобы продолжить...")










            

            


    def start(self):
        print('Добро пожаловать в =CoolGame=\n')

        while self.running:
            self.player.name = input("Введите никнейм:\n")
            ht.clear(self.player)
            print(f"{self.player.name}, cейчас тебе предстоит выбрать класс. В зависимости от выбора, твой персонаж с большей вероятностью будет "
                  "\nобладать соответстующими характеристиками, которые определяются рандомом в заданных диапазонах\n")
            input("Нажмите [Enter], чтобы продолжить...")
            ht.clear(self.player)

            i = None
            while i != 'y':
                ht.clear(self.player)
                self.player.choice = int(ht.pr("Выберите класс:\n  1 - Силач(Повышенная атака и защита, но проблемы с здоровьем),\n  2 - Странник(Повышеная ловкость и здоровье, но практически отсутствует защита),\n  3 - Травник(имеет в запасе зелье здоровья, усредненные характеристики)", ['1', '2', '3']))

                self.player.attack_points = self.player.character[self.player.choice]['attack']
                self.player.defense_points = self.player.character[self.player.choice]['defense']
                self.player.health_points = self.player.character[self.player.choice]['health']
                ht.clear(self.player)

                i = ht.pr(f"Вы уверены, что хотите выбрать класс {self.player.character[self.player.choice]['name']}?\n (y) - Да , (n) - Нет\n", ['y', 'n'])
                ht.clear(self.player)
                if i == 'y':
                    break
                elif i == 'n':
                    self.player.attack_points = 0
                    self.player.defense_points = 0
                    self.player.health_points = 0
                    continue

            ht.clear(self.player)

            print(f"{self.player.name}, ты очнулся в сырой траве, вокруг всё окутано густым туманом. Тепло земли под\n "
                  "тобой смешивается с холодным воздухом, от которого пробирает дрожь.\n Единственный звук — это шорох листвы где-то вдалеке\n")
            input("Нажмите [Enter], чтобы продолжить.")
            ht.clear(self.player)

            print('Начальная локация: Тропа\n')
            p = False
            while not p:
                action = ht.pr("(b) - Исследовать, (h) - Продолжить путь:", ['b', 'h'])
                if action == "h":
                    print("Ты не сможешь пройти дальше, пока не познакомишься с важной механикой")
                    continue
                elif action == "b":
                    self.random_staff()
                    print(f"Вы по случайным стечениям обстоятельств нашли сундук, в котором находится: {self.player.inv[f'item{self.items_count}']}! Вы время грядущих боев ты сможешь\n открыть инвентарь и воспользоваться предметом")
                    p = True
                    _ = input("Нажмите [Enter], чтобы продолжить...")
                    ht.clear_i(self.player)

            while self.running:
                action = ht.pr("(b) - Исследовать, (f) - Встретить врага", ['b', 'f'])
                if action == 'b':
                    print("Вы нашли ничего...")
                elif action == 'f':
                    self.fight()
            



if __name__ == "__main__":
    test = Play()
    test.start()
