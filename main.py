import csv


table = {}


def openFile():
    fileName = str(input())
    with open(fileName, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            stroke = list(row.values())[0]
            try:
                int(stroke)
            except ValueError:
                print('Value Error')
                quit()
            col = list(row.keys())[1:]
            values = list(row.values())[1:]
            for i in range(len(col)):
                cell = col[i] + stroke
                table[cell] = values[i]
    print(table)


def getValue(fitem, sitem, operator):
    ops = {'+': lambda x, y: x + y,
           '-': lambda x, y: x - y,
           '*': lambda x, y: x * y,
           '/': lambda x, y: x / y}
    try:
        int(table.get(fitem)) or float(table.get(fitem))
        int(table.get(sitem)) or float(table.get(sitem))
    except ValueError:
        print("Error")
    return str(ops[operator](int(table.get(fitem)), int(table.get(sitem))))


def getNames(cell):
    for i in range(len(cell)):
        if cell[i] == "+" or cell[i] == "-" or cell[i] == "*" or cell[i] == "/":
            index = i
            operator = cell[i]
            fitem = cell[1:index]
            sitem = cell[index+1:]
    return fitem, sitem, operator


def newValues():
    for k, v in table.items():
        if v[0] == "=":
            if "+" in v or "-" in v or "*" in v or "/" in v:
                fitem, sitem, operator = getNames(v)
                table[k] = getValue(fitem, sitem, operator)
            else:
                print('Invalid format')
                quit()

          
def writeFile():
    pass


if __name__ == "__main__":
    openFile()
    newValues()
    print(table)
