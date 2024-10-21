import os
import datetime
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if line != '':
                all_data.append(line)
            else:
                break

path = './Files/'
file_list = [path+f for f in os.listdir(path)]
"""
#       Линейный вызов
start = datetime.datetime.now()
for file in file_list:
    read_info(file)
end = datetime.datetime.now()
print('Линейный вызов:', end - start)

"""
#        Многопроцессный вызов
if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_list)
    end = datetime.datetime.now()
    print('Многопроцессный вызов:', end - start)

