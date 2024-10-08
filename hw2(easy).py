class Car:
    def __init__(self, max_speed, color, name):
        self.max_speed = max_speed
        self.color = color
        self.name = name
        self.is_police = False
        self.is_moving = False
        self.direction = None

    def go(self):
        if not self.is_moving:
            self.is_moving = True
            print(f"{self.name} поехала!")
        else:
            print(f"{self.name} уже в движении.")

    def stop(self):
        if self.is_moving:
            self.is_moving = False
            print(f"{self.name} остановилась.")
        else:
            print(f"{self.name} уже стоит на месте.")

    def set_direction(self, direction_code):
        direction_map = {
            1: "прямо",
            2: "назад",
            3: "влево",
            4: "вправо"
        }

        if self.is_moving:
            if direction_code in direction_map:
                self.direction = direction_map[direction_code]
                print(f"{self.name} поедет {self.direction}.")
            else:
                print("Некорректный код направления.")
        else:
            print(f"{self.name} не может изменить направление, пока стоит.")

class TownCar(Car):
    def __init__(self, max_speed, color, name):
        super().__init__(max_speed, color, name)

class SportCar(Car):
    def __init__(self, max_speed, color, name):
        super().__init__(max_speed, color, name)

class WorkCar(Car):
    def __init__(self, max_speed, color, name):
        super().__init__(max_speed, color, name)

class PoliceCar(Car):
    def __init__(self, max_speed, color, name):
        super().__init__(max_speed, color, name)
        self.is_police = True

town_car = TownCar(max_speed=140, color="white", name="Kia")
town_car.go()
town_car.set_direction(3)
town_car.stop()
