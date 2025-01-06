class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_numbers(self.__numbers)
        self.__is_valid_vin(self.__vin)

    def __is_valid_vin(self, vin_number):
        self.vin_number = vin_number
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif vin_number not in range(1000000, 10000000):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        self.__numbers = numbers
        if not isinstance(numbers, str):
            raise IncorrectCarNumber('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumber('Неверная длина номера')
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.massage = message


class IncorrectCarNumber(Exception):
    def __init__(self, message):
        self.massage = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.massage)
except IncorrectCarNumber as exc:
    print(exc.massage)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 't001tp')
except IncorrectVinNumber as exc:
    print(exc.massage)
except IncorrectCarNumber as exc:
    print(exc.massage)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.massage)
except IncorrectCarNumber as exc:
    print(exc.massage)
else:
    print(f'{third.model} успешно создан')
