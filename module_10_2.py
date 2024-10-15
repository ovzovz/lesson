from threading import Thread
from time import  sleep
class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f' {self.name}, на нас напали!')
        day_count=0
        enemy_count = 100
        while enemy_count>0:
            sleep(1)
            day_count += 1
            enemy_count -= self.power
            print(f'{self.name} сражается {day_count} день(дня),'
                  f' осталось {enemy_count} воинов.')
        print(f'{self.name} одержал победу спустя {day_count} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')
