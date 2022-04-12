from pathlib import Path


def input_file_menu():
    while True:
        filename = input('Input filename: ')
        file = Path(f'./src/inputs/{filename}')
        if file.is_file():
            break
        else:
            print('File does not exist, try again!')


# TODO: validar inputs
def insert_data_menu():
    while True:
        file = open('./src/inputs/runtime_input.txt', 'x')

        print('IMPORTANT')
        print('In this menu, you will be prompted to provide some required information.')
        print('It is extremely important that you follow the format indicated.')

        print('First, provide the following data in the indicated format - <rows> <slots> <unavailable slots> <pools> <servers>')

        input = input()
        file.write(input)

        _, _, unavailable, _, servers = map(int, input.split())

        print(f'You indicated that there are {unavailable} slots.')
        print('Please provide the coordinates for each one.')
        print('[format: <row> <slot>]')

        for i in range(unavailable):
            input = input(f'Coordinates of slot no. {i}: ')
            file.write(input)

        print(f'You indicated that there are {servers} servers')
        print('Please provide the size (number of slots occupied by it) and capacity for each one.')
        print('[format: <size> <capacity>]')

        for i in range(servers):
            input = input(f'Size and capacity of slot no. {i}: ')
            file.write(input)


# TODO: mais opções??
def main_menu():
    print('1. Input file')
    print('2. Insert data')

    valid_op = False
    next_menu = None

    while not valid_op:
        op = input('Choose an option: ')

        if op == '1':
            next_menu = input_file_menu
            valid_op = True
        elif op == '2':
            next_menu = insert_data_menu
            valid_op = True
        else:
            print('Invalid option!')

    next_menu()
