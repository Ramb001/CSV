import csv
import sys


table = {}


def openFile():
    with open(sys.argv[1], newline="") as file:
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
    
    
def getNames(cell):
    for i in range(len(cell)):
        if cell[i] in "+-*/":
            return cell[1:i], cell[i + 1 :], cell[i]
    else:
        print('Invalid table format!')
        quit()


def getValue(cell):
    ops = {'+': lambda x, y: x + y,
           '-': lambda x, y: x - y,
           '*': lambda x, y: x * y,
           '/': lambda x, y: x / y}
    
    fitem, sitem, operator = getNames(cell)
    
    checkValue(fitem)
    checkValue(sitem)
    
    try:
        res = ops[operator](float(table.get(fitem)), float(table.get(sitem)))
    except ZeroDivisionError:
        print('Division by 0!')
        quit()
        
    if int(res) == res: 
        res = int(res)
        
    return str(res)


def checkValue(value):
    if value not in table:
        print('Invalid table format!')
        quit()
        
    if table.get(value)[0] == '=':
        try:
            table[value] = getValue(table.get(value))
        except RecursionError:
            print('Invalid table format!')
            quit()

          
def writeFile():
    values = list(table.values())
    with open(sys.argv[1], newline="") as file:
        reader = csv.DictReader(file)
        m = 0
        names = reader.fieldnames
        print(*names, sep=',')
        
        for row in reader:
            stroke = list(row.values())
            for i in range(1, len(stroke)):
                stroke[i] = values[m]
                m += 1
            print(*stroke, sep=',')


if __name__ == "__main__":
    openFile()
    for k, v in table.items():
        if v[0] == "=":
            table[k] = getValue(v)
    writeFile()