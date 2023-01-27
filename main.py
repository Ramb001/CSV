import csv


table = {}
ops = {'+': lambda x, y: x + y,
       '-': lambda x, y: x - y,
       '*': lambda x, y: x * y,
       '/': lambda x, y: x / y}


def isInt(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def openFile():
    fileName = str(input())
    with open(fileName, newline="") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            stroke = list(row.values())[0]
            
            try:
                int(stroke)
            except ValueError:
                print('Value Error!')
                quit()
                
            col = list(row.keys())[1:]
            values = list(row.values())[1:]
            
            for i in range(len(col)):
                cell = col[i] + stroke
                table[cell] = values[i]
                
    print(table)


def getNames(cell):
    for i in range(len(cell)):
        if cell[i] == "+" or cell[i] == "-" or cell[i] == "*" or cell[i] == "/":
            index = i
            operator = cell[i]
            fitem = cell[1:index]
            sitem = cell[index+1:]
    return fitem, sitem, operator


def getValue(cell, key):
    fitem, sitem, operator = getNames(cell)
    if table.get(fitem)[0] == '=':
        table[fitem] = getValue(table.get(fitem), fitem)
    try:
        res = ops[operator](float(table.get(fitem)), float(table.get(sitem)))
        if isInt(res): 
            res = int(res)
        table[key] = res
        
    except ZeroDivisionError:
        print('Division by 0!')
        quit()


def newValues():
    for k, v in table.items():
        if v[0] == "=":
            if "+" in v or "-" in v or "*" in v or "/" in v:
                getValue(v, k)
            else:
                print('Invalid format of cell!')
                quit()

          
def writeFile():
    pass


if __name__ == "__main__":
    openFile()
    newValues()
    print(table)