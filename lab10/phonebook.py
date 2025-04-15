import psycopg2
import csv

# Настройки подключения
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "Kazakhstan2007"  
DB_HOST = "localhost"
DB_PORT = "5432"

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

# 1. Загрузка из CSV
def insert_from_csv(file_path):
    conn = get_connection()
    cur = conn.cursor()
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Пропускаем заголовок
        for row in reader:
            cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    cur.close()
    conn.close()
    print("CSV данные успешно загружены.")

# 2. Ввод с консоли
def insert_from_console():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Данные успешно добавлены.")

# 3. Обновление данных
def update_data():
    name = input("Введите существующее имя: ")
    new_name = input("Новое имя (Enter чтобы пропустить): ")
    new_phone = input("Новый телефон (Enter чтобы пропустить): ")

    conn = get_connection()
    cur = conn.cursor()

    if new_name:
        cur.execute("UPDATE PhoneBook SET name = %s WHERE name = %s", (new_name, name))
    if new_phone:
        cur.execute("UPDATE PhoneBook SET phone = %s WHERE name = %s", (new_phone, name))

    conn.commit()
    cur.close()
    conn.close()
    print("Данные обновлены.")

# 4. Поиск
def query_data():
    print("Фильтр: name / phone / all")
    filter_type = input("Введите тип фильтра: ")

    conn = get_connection()
    cur = conn.cursor()

    if filter_type == "name":
        value = input("Введите имя: ")
        cur.execute("SELECT * FROM PhoneBook WHERE name = %s", (value,))
    elif filter_type == "phone":
        value = input("Введите номер: ")
        cur.execute("SELECT * FROM PhoneBook WHERE phone = %s", (value,))
    else:
        cur.execute("SELECT * FROM PhoneBook")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

# 5. Удаление
def delete_user():
    value = input("Введите имя или номер телефона для удаления: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM PhoneBook WHERE name = %s OR phone = %s", (value, value))

    conn.commit()
    cur.close()
    conn.close()
    print("Пользователь удалён.")

# Меню
def main():
    while True:
        print("\n=== МЕНЮ ТЕЛЕФОННОЙ КНИГИ ===")
        print("1. Загрузить из CSV")
        print("2. Ввод вручную")
        print("3. Обновить данные")
        print("4. Поиск")
        print("5. Удалить")
        print("6. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            path = input("Введите путь к CSV файлу: ")
            insert_from_csv(path)
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_data()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_user()
        elif choice == "6":
            break
        else:
            print("Неверный выбор. Повторите.")

if __name__ == "__main__":
    main()
