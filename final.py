# Создаем словарь для хранения информации о заметке
note = {}

# Запрашиваем информацию у пользователя
note["username"] = input("Введите имя пользователя: ")
note["content"] = input("Введите описание заметки: ")
note["status"] = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
note["created_date"] = input("Введите дату создания заметки в формате 'день.месяц.год': ")
note["issue_date"] = input("Введите дату истечения заметки в формате 'день.месяц.год': ")

#Запрашиваем несколько заголовков и добавляем их в список
title1 = input("Введите заголовок заметки 1: ")
title2 = input("Введите заголовок заметки 2: ")
title3 = input("Введите заголовок заметки 3: ")
note["titles"] = [title1, title2, title3]

# Формат вывода дат пользователю
note["temp_created_date"] = note["created_date"][0:5]
note["temp_issue_date"] = note["issue_date"][0:5]

# Выводим собранные данные
print("\nСобранная информация о заметке:")
print(note)




