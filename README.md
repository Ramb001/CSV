# CSV
Данная программа написана для обработки CSV-файлов. В CSV-файле хранится таблица, в которую включены название стоблцов и строк, представленных в виде положительных целых чисел, а также ячейки, которые храянят в себе целые числа или выражения вида: <p><b>=ARG1 op ARG2.</b><p>В ходе выполнения программы вычисляются значения неизвестных ячеек (в случае необходимости), после чего выводится результат в CSV-представлении.\ Для проверки всех сценариев программы, готовые таблицы и результат выполнения можно найти в файле [Tables for tests](https://github.com/Ramb001/CSV/blob/203908edcb762a357552fa62553a9b3318e1276c/Tables%20for%20tests), с описанием определенного сценария. Тестовые таблицы нужно вносить в файл [table.csv](https://github.com/Ramb001/CSV/blob/203908edcb762a357552fa62553a9b3318e1276c/table.csv). 

Для запуска программы нужно написать в консоле следующее:
```
python3 main.py table.csv
```
