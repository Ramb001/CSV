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
        # for row in reader:
        #     x = row.pop(reader.fieldnames[0])
        #     for column, value in row.items():
        #         if column and value:
        #             y = column
        #             table[x,y] = value
    print(table)


def getValues(fitem, sitem):
    return str(int(table.get(fitem)) + int(table.get(sitem)))


def newValues():
    for k, v in table.items():
        if v[0] == "=":
            for i in range(len(v)):
                if v[i] == "+":
                    index = i
                    fitem = v[1:index]
                    sitem = v[index+1:]
                    table[k] = getValues(fitem, sitem)
                    
                    
def writeFile():
    pass


if __name__ == "__main__":
    openFile()
    newValues()
    print(table)
