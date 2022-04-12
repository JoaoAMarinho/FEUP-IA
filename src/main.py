from model.DataCenter import DataCenter


def main():
    data_center = DataCenter('input_xl.txt')
    for x in data_center.solution: print(x.slots)


if __name__ == '__main__':
    main()
