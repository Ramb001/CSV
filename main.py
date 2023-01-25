import csv


def openFile():
    fileName = str(input())
    with open(fileName, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


if __name__ == "__main__":
    openFile()
