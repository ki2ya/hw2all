
class Person:
    def __init__(self, name, race):
        self.name = name
        self.race = race


class Player(Person):
    def __init__(self, name, race, health, damage, armor):
        super().__init__(name, race)
        self.health = health
        self.damage = damage
        self.armor = armor

    def count_attack(self, enemy):
        count1 = self.damage - enemy.armor
        print("Вы нанесете:",count1,"урона")
        return count1

    def attack(self, enemy):
        count1 = self.count_attack(enemy)
        enemy.health = enemy.health - count1
        print("У противника осталось:", enemy.health, "здоровья")




class Enemy(Person):
    def __init__(self, name, race, health, damage, armor):
        super().__init__(name, race)
        self.health = health
        self.damage = damage
        self.armor = armor

    def count_attack(self, player):
        count1 = self.damage - player.armor
        print("Вам нанесут:", count1, "урона")
        return count1

    def attack(self, player):
        count1 = self.count_attack(player)
        player.health = player.health - count1
        print("У вас осталось:", player.health, "здоровья")


my_player = Player("Yagami", "Elf", 110, 10, 3)
my_enemy  = Enemy("L", "Dwarf", 100, 6, 8)

while my_player.health > 0 and my_enemy.health > 0:
    my_player.attack(my_enemy)
    if my_enemy.health <= 0:
        print(f"{my_enemy.name} повержен!")
        break
    my_enemy.attack(my_player)
    if my_player.health <= 0:
        print(f"{my_player.name} повержен!")
