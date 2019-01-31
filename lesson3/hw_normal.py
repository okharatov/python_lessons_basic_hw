# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

names = ['Vasy', 'Lena', 'Oleg', 'Ivan']
salary = [100000, 300000, 400000, 500000]

def parse_raw(s):
    row = s.replace('\n', '').split(' - ')
    return f'{row[0]} - {float(row[1]) * 0.87}'

salary_dict = dict(zip(names, salary))
#Не очень понял 500тыс. это до с налогом или без, сделал вместе с налогом
#Если наше приложение является фтльтром, то писать "сенситив" данные файл некорректно
filtered_list = filter(lambda x: x[1] < 500000, salary_dict.items()) 

with open('salary.txt', 'w', encoding='utf-8') as file:    
    file.writelines(map(lambda row: f'{row[0].upper()} - {row[1]}\n', filtered_list))

with open('salary.txt', 'r', encoding='utf-8') as file:
    result = map(parse_raw, file.readlines())

[print(r) for r in result]