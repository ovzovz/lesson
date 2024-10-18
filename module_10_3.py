from threading import Thread, Lock
from random import randint
from time import sleep
class Bank():
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            plus = randint(50,501)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += plus
            print(f'Пополнение: {plus}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            minus = randint(50, 501)
            print('Запрос на ', minus)
            if minus <= self.balance:
                self.balance -= minus
                print(f'Снятие: {minus}.  Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')


