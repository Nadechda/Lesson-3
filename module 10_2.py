import threading
import time


class Knight(threading.Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)



    def run(self):
        print(f'{self.name}, на нас напали!"')
        counter = 100
        day = 0
        while counter > 0:
            time.sleep(1)
            counter -= self.power
            day += 1
            print(f"{self.name} сражается {day}..., осталось {counter} воинов.")
        print(f'{self.name}  одержал победу спустя {day} дней(дня)!')


# Создание класса
first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

print(f'\nВсе враги повержены, битвы закончены!')
