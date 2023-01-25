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
        # for row in reader:
        #     x = row.pop(reader.fieldnames[0])
        #     for column, value in row.items():
        #         if column and value:
        #             y = column
        #             table[x,y] = value
    print(table)


def getValues(fitem, sitem):
    return int(table.get(fitem)) + int(table.get(sitem))


def newValues():
    for k, v in table.items():
        if v[0] == '=':
            for i in range(len(v)):
                if v[i] == '+':
                    index = i
                    fitem = v[1:index]
                    sitem = v[index+1:]
                    table[k] = getValues(fitem, sitem)


if __name__ == "__main__":
    openFile()
    newValues()
    print(table)