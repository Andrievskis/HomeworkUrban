import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        x = self._cords[0] + self.speed * dx
        y = self._cords[1] + self.speed * dy
        z = self._cords[2] + self.speed * dz
        if z in self._cords < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords = [x, y, z]

    def get_cords(self):
        print(f"X:{self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]} ")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, I'm attacking you O_O")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} eggs for you.")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        z1 = abs(dz) * self.speed // 2
        z = self._cords[2] - z1
        if z < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[2] = z


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = 'Click-click-click'


db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
# print(Duckbill.mro())
