import psycopg2

# Подключение к базе данных
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

# 1. Функция: поиск по шаблону
def create_function_search_by_pattern():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
    RETURNS TABLE(id INT, name TEXT, phone TEXT)
    AS $$
    BEGIN
        RETURN QUERY
        SELECT * FROM PhoneBook
        WHERE name ILIKE '%' || pattern || '%'
           OR phone ILIKE '%' || pattern || '%';
    END;
    $$ LANGUAGE plpgsql;
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Функция search_by_pattern создана.")

# 2. Процедура: вставка/обновление одного пользователя
def create_procedure_insert_or_update():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE OR REPLACE PROCEDURE insert_or_update_user(in_username TEXT, in_phone TEXT)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        IF EXISTS (SELECT 1 FROM PhoneBook WHERE name = in_username) THEN
            UPDATE PhoneBook SET phone = in_phone WHERE name = in_username;
        ELSE
            INSERT INTO PhoneBook(name, phone) VALUES (in_username, in_phone);
        END IF;
    END;
    $$;
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Процедура insert_or_update_user создана.")

# 3. Процедура: вставка списка пользователей с проверкой телефонов
def create_procedure_insert_many_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE OR REPLACE PROCEDURE insert_many_users(
        in_names TEXT[],
        in_phones TEXT[],
        OUT bad_entries TEXT[]
    )
    LANGUAGE plpgsql
    AS $$
    DECLARE
        i INT := 1;
        tmp_bad TEXT[] := '{}';
    BEGIN
        WHILE i <= array_length(in_names, 1) LOOP
            IF in_phones[i] ~ '^[0-9]{10,15}$' THEN
                CALL insert_or_update_user(in_names[i], in_phones[i]);
            ELSE
                tmp_bad := array_append(tmp_bad, in_names[i]);
            END IF;
            i := i + 1;
        END LOOP;
        bad_entries := tmp_bad;
    END;
    $$;
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Процедура insert_many_users создана.")

# Вызов всех функций и процедур
def setup_all():
    create_function_search_by_pattern()
    create_procedure_insert_or_update()
    create_procedure_insert_many_users()

if __name__ == "__main__":
    setup_all()
