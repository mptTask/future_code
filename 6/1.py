import sqlite3

conn = sqlite3.connect('shelter_database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        breed TEXT,
        status TEXT
    )
''')
conn.commit()

def add_cat():
    name = input("Введите имя кота: ")
    age = int(input("Введите возраст кота: "))
    breed = input("Введите породу кота: ")
    status = input("Введите статус кота (Available/Adopted): ")
    
    cursor.execute('''
        INSERT INTO cats (name, age, breed, status)
        VALUES (?, ?, ?, ?)
    ''', (name, age, breed, status))
    conn.commit()
    print(f"Кот {name} успешно добавлен в базу данных.")

def view_cats():
    cursor.execute('SELECT * FROM cats')
    cats = cursor.fetchall()
    if cats:
        for cat in cats:
            print(cat)
    else:
        print("База данных котов пуста.")

def update_cat():
    cat_id = int(input("Введите ID кота, данные которого нужно обновить: "))
    name = input("Введите новое имя кота: ")
    age = int(input("Введите новый возраст кота: "))
    breed = input("Введите новую породу кота: ")
    status = input("Введите новый статус кота (Available/Adopted): ")
    
    cursor.execute('''
        UPDATE cats
        SET name=?, age=?, breed=?, status=?
        WHERE id=?
    ''', (name, age, breed, status, cat_id))
    conn.commit()
    print(f"Данные по коту с ID {cat_id} успешно обновлены.")

def delete_cat():
    cat_id = int(input("Введите ID кота, который будет удален: "))
    cursor.execute('DELETE FROM cats WHERE id=?', (cat_id,))
    conn.commit()
    print(f"Кот с ID {cat_id} успешно удален из базы данных.")

def find_cat_by_name():
    name = input("Введите имя кота для поиска: ")
    cursor.execute('SELECT * FROM cats WHERE name LIKE ?', ('%' + name + '%',))
    cats = cursor.fetchall()
    if cats:
        for cat in cats:
            print(cat)
    else:
        print(f"Кот с именем {name} не найден.")

while True:
    print(" /\_/\  \n( o.o ) \n > ^ < ")
    print("\n===== Меню навигации =====")
    print("1. Добавить кота")
    print("2. Просмотреть всех котов")
    print("3. Обновить данные кота")
    print("4. Удалить кота")
    print("5. Найти кота по имени")
    print("0. Выйти из программы")

    choice = input("Введите номер действия: ")

    if choice == '1':
        add_cat()
    elif choice == '2':
        view_cats()
    elif choice == '3':
        update_cat()
    elif choice == '4':
        delete_cat()
    elif choice == '5':
        find_cat_by_name()
    elif choice == '0':
        print("Программа завершена.")
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите действие из меню.")
