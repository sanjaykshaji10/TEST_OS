import os
from multiprocessing import Process, current_process
import setproctitle
# define all the functions here


def square(number):
    result = number ** 2

    process_name = current_process().name
    current_process().name = 'square_process'
    print(f'Process number: {process_name}')
    print(f'{number} squares to {result}')
    p_new = current_process().name
    print("Process : ", p_new)


def cube(number):
    result = number ** 2
    process_name = current_process().name
    current_process().name = 'cube_process'
    p_new = current_process().name
    print("Process : ", p_new)
    print(f'Process number: {process_name}')
    print(f'{number} cubes to {result}')


if __name__ == '__main__':

    processes = []
    # val = input('enter a value :')
    # print('value was ' + val)
    numbers = [1, 2, 5, 7]

    for number in numbers:
        process_square = Process(target=square, args=(number,))
        processes.append(process_square)
        process_cube = Process(target=cube, args=(number,))
        processes.append(process_cube)
        process_square.start()
