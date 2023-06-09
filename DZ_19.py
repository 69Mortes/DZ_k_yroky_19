#Домашнее задание :)
print("Условия задач:\n1. Дано 2 множества, содержащих названия IT-компаний. "
      "Найти только те компании, которые содержатся в обоих множествах."
      "\n2. Сгенерировать n множеств. Вывести множества кратные трём "
      "и не входящие в первое множество.")
users1 = {"EPAM", "iTechArt Group", "IBA Group", "ISsoft", "Microsoft", "Dell", "IBM", "Yandex",
          "Adobe Inc", "overone", "LOVATA", "IQUADART"}
users2 = {"overone", "IBM", "Microsoft", "NewIT", "SKY INCOM", "Egorov Agency", "MEGA.BY",
          "VironIT", "ArtisMedia", "LOVATA", "Qmedia.by", "Yandex",}
# Для удобного отображения и разделения заданий, нарисуем линию
print("_________________________________1-e задание:_________________________________________________________")
print("1-е множество: ", users1) # Выводим первое множество
print("2-е множество: ", users2) # Выводим второе множество
users3 = users1.intersection(users2) # Сравниваем 1 и 2 множества, сохраняем компании, находящиеся в обоих множествах
print("Компании, которые содержатся в обоих множествах\n", users3)
users4 = users2.difference(users1) # Сравниваем 2 и 1 множества, сохраняем компании, не входящие в 1-е множество
print("Компании, не входящее в первое множество :\n", users4)
print("_________________________________2-e задание:_________________________________________________________")
import random # Импортируем библиотеку рандом, чтобы не вводить вручную элементы множеств
N = int(input("Введите количество множеств: ")) # Просим пользователя ввести число N
list1 = [] # Создаем пустой список
set1 = set() # Создаем пустое множество
for cikl_1 in range(N): # Создаем столько множеств, сколько указал пользователь
    set1 = {random.randint(1, 250) for j in range(5)} # создаем тело множества: 5 элементов (рандомные числа от 1 до 250)
    list1.append(set1) # сохраняем полученные множества в список для дальнейших действий
    # Тк цикл начинается с 0, добавим +1 для удобного отображения порядкового номера
    print(cikl_1 + 1, "-е множество:", set1) # Выводим полученное множество.
kratnie_3 = set() # Создаем пустое множество, позже будем сохранять числа, кратные 3-м
for cikl_2 in list1: # Перебираем множества из списка
    for cikl_3 in cikl_2: # Перебираем элементы внутри множества
        # создаем условие: нет остатка при делении на 3 и числа, не входящие в первое множество
        if cikl_3 % 3 == 0 and cikl_3 not in list1[0]:
            kratnie_3.add(cikl_3) # сохраняем отобранные числа
print("Множества кратные трём и не входящие в первое множество:\n", kratnie_3) # Выводим полученный результат