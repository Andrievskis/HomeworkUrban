import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# start = datetime.now()
# for file in filenames:
#     read_info(file)
# stop = datetime.now()
# print(f'{stop - start} (линейный)')


if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool(processes=len(filenames)) as p:
        p.map(read_info, filenames)
    stop = datetime.now()
    print(f'{stop - start} (многопроцессный)')
