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
                
    print(table)
    

def checkPrevValue(prevValue, curValue):
    return prevValue == curValue


def getValue(cell):
    # print(cell)
    ops = {'+': lambda x, y: x + y,
       '-': lambda x, y: x - y,
       '*': lambda x, y: x * y,
       '/': lambda x, y: x / y}
    
    for i in range(len(cell)):
        if cell[i] == "+" or cell[i] == "-" or cell[i] == "*" or cell[i] == "/":
            index = i
            operator = cell[i]
            fitem = cell[1:index]
            sitem = cell[index+1:]
            break
    else:
        print('Invalid format of cell!')
        quit()
    
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
    if table.get(value)[0] == '=':
        try:
            table[value] = getValue(table.get(value))
        except RecursionError:
            print('Invalid table format!')
            quit()


def newValues():
    for k, v in table.items():
        if v[0] == "=":
            table[k] = getValue(v)

          
def writeFile():
    pass


if __name__ == "__main__":
    openFile()
    newValues()
    print(table)