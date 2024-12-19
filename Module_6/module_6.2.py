class Vehicle:
    def __init__(self, owner, _model, _color, _engine_power):
        self.owner = owner
        self._model = _model
        self._engine_power = _engine_power
        self._color = _color
        self._COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self):
        return f'Модель: {self._model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self._engine_power}'

    def get_color(self):
        return f'Цвет: {self._color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        self.new_color = new_color
        if new_color.lower() in self._COLOR_VARIANTS:
            self._color = self.new_color
        else:
            print(f'Нельзя сменить цвет на {self.new_color}')


class Sedan(Vehicle):
    _PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
