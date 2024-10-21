from threading import Thread
from time import sleep
from random import randint
from queue import Queue

class Table():
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 11))

class Cafe():
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        for guest in guests:
            guest_done = 0
            for table in tables:
                if table.guest == None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    guest_done = 1
                    guest.join()
                    break
            if guest_done == 0:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')
    def discuss_guests(self):
        while not(self.queue.empty()) or len([table for
                            table in tables if table.guest != None]) > 0:
            for table in  tables:
                if table.guest != None:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None
                        if not(self.queue.empty()):
                            table.guest = self.queue.get()
                            print(f'{table.guest.name} вышел(-ла) из очереди '
                                f'и сел(-а) за стол номер {table.number}' )
                            table.guest.start()

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
