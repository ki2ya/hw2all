class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def purchase_materials(self):
        print(f"Закупаем материалы для создания игрушки: {self.name}")

    def sew(self):
        print(f"Шьем игрушку: {self.name}")

    def paint(self):
        print(f"Окрашиваем игрушку: {self.name} в цвет {self.color}")

    def __str__(self):
        return f"Игрушка: {self.name}, цвет: {self.color}"


class AnimalToy(Toy):
    def __str__(self):
        return f"Игрушка-животное: {self.name}, цвет: {self.color}"


class CartoonCharacterToy(Toy):
    def __str__(self):
        return f"Игрушка-персонаж мультфильма: {self.name}, цвет: {self.color}"


class ToyFactory:
    def create_toy(self, name, color, toy_type):
        if toy_type == "animal":
            toy = AnimalToy(name, color)
        elif toy_type == "cartoon_character":
            toy = CartoonCharacterToy(name, color)
        else:
            raise ValueError(f"Неизвестный тип игрушки: {toy_type}")

        print(f"\nНачинаем производство игрушки: {name} ({toy_type})")
        toy.purchase_materials()
        toy.sew()
        toy.paint()

        print("Игрушка создана\n")
        return toy


def main():
    factory = ToyFactory()

    teddy_bear = factory.create_toy("Мишка", "Коричневый", "animal")
    print(teddy_bear)

    mickey_mouse = factory.create_toy("Микки Маус", "Чёрно-белый", "cartoon_character")
    print(mickey_mouse)


if __name__ == "__main__":
    main()
