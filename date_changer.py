# Определяем переменные
username = "Петр Петров"    # Имя пользователя
title = "Список дел"        # Заголовок заметки
content = "Выполнить ДЗ"    # Описание заметки
status = "Активна"          # Статус заметки
created_date = "22.01.2025" # Дата создания заметки
issue_date = "23.01.2025"   # Дата истечения заметки

# Формат вывода дат пользователю
temp_created_date = created_date[0:5]
temp_issue_date = issue_date[0:5]

# Выводим введенные данные
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", temp_created_date)
print("Дата истечения заметки:", temp_issue_date)
