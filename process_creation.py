import os
from multiprocessing import Process, current_process
import setproctitle

# define all the functions here
def square(number):
    result = number ** 2

    process_name = current_process().name
    current_process().name = 'sid'
    print(f'Process name: {process_name}')
    print(f'{number} squares to {result}')
    p_new = current_process().name
    print(p_new)

if __name__ == '__main__':

    processes = []
    # val = input('enter a value :')
    # print('value was ' + val)
    numbers = [1, 2, 5, 7]

    for number in numbers:
        process = Process(target=square, args=(number,))
        processes.append(process)

        process.start()
