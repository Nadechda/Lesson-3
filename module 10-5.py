import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, encoding="utf-8") as f:
        s = f.readline()
        all_data.append(s)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start = datetime.now()
for name in filenames:
    read_info(name)

finish = datetime.now()
res = finish - start
res_msec = res * 1000
print(f'Время работы в миллисекундах(линейный):', res_msec)

# Многопроцессный


if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    finish = datetime.now()
    res = finish - start
    res_msec = res * 1000
    print('Время работы в миллисекундах(многопроцессорный): ', res_msec)
