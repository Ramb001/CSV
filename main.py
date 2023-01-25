import csv


table = {}


def openFile():
    fileName = str(input())
    with open(fileName, newline="") as file:
        reader = csv.DictReader(file)
        # {A1: 1,...} ключ - значени верха и левого бока, значение - значение ячейки
        for row in reader:
            stroke = list(row.values())[0]
            col = list(row.keys())[1:]
            values = list(row.values())[1:]
            for i in range(len(col)):
                cell = col[i] + stroke
                table[cell] = values[i]
    print(table)


if __name__ == "__main__":
    openFile()