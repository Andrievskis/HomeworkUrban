import threading
import time
from random import randint

lock = threading.Lock()


class Bank(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.balance = 0

    def deposit(self):
        for transaction in range(100):
            number_random = randint(50, 500)
            self.balance += number_random
            print(f'Пополнение {number_random}. Баланс: {self.balance}')
            if self.balance >= 500 and lock.locked():
                lock.release()
            time.sleep(0.001)

    def take(self):
        for transaction in range(100):
            number_random = randint(50, 500)
            print(f'Запрос на {number_random}.')
            if number_random <= self.balance:
                self.balance -= number_random
                print(f'Снятие: {number_random}.Баланс: {self.balance}')
            elif number_random > self.balance:
                print('Запрос отклонён, недостаточно средств.')
                lock.acquire()
            time.sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
