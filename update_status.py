note = {} # Создаем словарь для хранения информации о заметке
while True:
    print("\nВыберите статус заметки: \n- выполнено \n- в процессе \n- отложено")
    note["status"] = input("Ваш выбор: ")  # Запрашиваем статус
    if note["status"] == "выполнено" or note["status"] == "в процессе" or note["status"] == "отложено":  # Задаем условие на правильный ввод
        print(f"\nВаш статус: {note["status"]}")
        while True:
            print("\nХотите изменить:\n - да\n - нет")
            status_confirm = input("Ваш выбор: ")  # Запрашиваем подтверждение на изменение
            if status_confirm == "да":  # Задаем условие на подтверждение изменения
                print("\nВы дали согласие на изменение ...")
                while True:
                    print("\nВыберите новый статус(цифра или слово): \n1. выполнено \n2. в процессе \n3. отложено")
                    note["status"] = input("Ваш выбор: ")  # Запрашиваем новый статус
                    if note["status"] == "1" or note["status"] == "выполнено":  # Задаем условие на 1 вариант выбора
                        note["status"] = "выполнено"
                        break
                    elif note["status"] == "2" or note["status"] == "в процессе":  # Задаем условие на 2 вариант выбора
                        note["status"] = "в процессе"
                        break
                    elif note["status"] == "3" or note["status"] == "отложено":  # Задаем условие на 3 вариант выбора
                        note["status"] = "отложено"
                        break
                    else:
                        print("\nНеправильный ввод!Попробуйте еще раз!")
                print(f"\nСтатус заметки успешно обновлён на '{note["status"]}'")  # Выводим измененный статус
                break
            elif status_confirm == "нет":  # Задаем условие на отклонение изменения
                print(f"\nВаш текущий статус '{note["status"]}' не изменился") # Предупреждаем о неизменности статуса
                break
            else:
                print("\nНеправильный ввод!Попробуйте еще раз")
        break
    else:
        print("\nНеправильный ввод!Попробуйте еще раз")

# ДОРАБОТАТЬ

# 13. Рефакторинг:
# Если программа становится длинной, разбейте её на функции: например, отдельная функция для проверки корректности ввода или вывода текущего статуса.