import random
from threading import Thread
from time import sleep
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
        t = random.randint(3, 10)
        sleep(t)


class Cafe:
    list_th = []

    def __init__(self, *tables):
        self.tables = list(tables)
        self.q = Queue()

    def guest_arrival(self, *guests):
        list_guests = list(guests)
        list_tables=self.tables
        min_guests_t=min(len(list_guests),len(list_tables))

        for i in range(min_guests_t):
            list_tables[i].guests =guests[i]
            thread1 = guests[i]
            thread1.start()
            print(f'{list_guests[i].name} сел(-а) за стол номер {list_tables[i].number}')
            if len(list_guests) > min_guests_t:
                for i in range(min_guests_t,len(list_guests)):
                    self.q.put(guests[i])
                    print(f'{list_guests[i]} в очереди')

    def discuss_guests(self):
        while not self.q.empty() or table.guest is not None:
            if not(table.guest is None) and not(table.guest.is_alive()):
                print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                print(f"Стол номер {table.number} свободен")
                table.guest = None
            if not(self.q.empty()) and table.guest is None:
                table.guest = self.q.get()
                print(f"{self.table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                thread1 = table.guest
                thread1.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya',
                'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
