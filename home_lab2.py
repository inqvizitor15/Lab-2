from csv import reader
import random
random.seed()
output3 = open('result.txt', 'w')
rez1 = 0

rw = 1
rnd3 =[]
kol = 0
while True: # выбираем 20 случайных строк для задания с библиографическими ссылками
    temp = random.randint(2, 9410)
    if temp not in rnd3 and kol < 20:
        rnd3.append(temp)
        kol += 1
    if kol >= 20:
        break

search_writer = input('Введите запрос: ') # 2 задание на поиск по автору

search_writer_lower = search_writer.lower()
with open('books.csv', 'r', encoding='windows-1251') as booksfile:
    table = reader(booksfile, delimiter=';')
    for row in table:
        rw += 1

        lower_case = row[1].lower()
        if len(lower_case) > 30: # 1 задание на 30 символов
            rez1 += 1


        if (search_writer_lower in row[4].lower()) and ('2014' in row[6] or '2016' in row[6] or '2017' in row[6]): # 2 задание
            print(row[1])

        if rw in rnd3: # 3 задание
            if len(row[4]) > 0:
                output3.write(f'{row[4]}. {row[1]} - {row[6]}\n')
            else:
                output3.write(f'Нет данных. {row[1]} - {row[6]}\n')

print()
print(f'Количество записей, у которых в поле <Название> строка длинее 30 символов: {rez1}')
output3.close()