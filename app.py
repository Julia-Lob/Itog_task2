#task_2
import psycopg2
from tkinter import messagebox
import pandas as pd


def create_table(conn):
    # Создание таблицы в базе данных.
    with conn.cursor() as cursor:
        create_table_query = """
        CREATE TABLE IF NOT EXISTS employees (
            ID SERIAL PRIMARY KEY,
            Name VARCHAR(100),
            Age INTEGER,
            Department VARCHAR(100)
        );
        """
        cursor.execute(create_table_query)
        conn.commit()
        print("Таблица создана.")

def insert_data(conn):
    # Наполнение таблицы данными.
    with conn.cursor() as cursor:
        insert_query = """
        INSERT INTO employees (Name, Age, Department) VALUES
        ('John Doe', 28, 'HR'),
        ('Jane Smith', 35, 'Engineering'),
        ('Alice Johnson', 42, 'Sales');
        """
        cursor.execute(insert_query)
        conn.commit()
        print("Данные добавлены в таблицу.")


def fetch_data(conn):
    select_query = "SELECT * FROM employees;"
    # Используем psycopg2 для выполнения запроса и получения данных
    with conn.cursor() as cursor:
        cursor.execute(select_query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
    # Создаем DataFrame вручную
    df = pd.DataFrame(rows, columns=columns)

    df.columns = ['ID' if col.lower() == 'id' else col.capitalize() for col in df.columns]

    print("Данные из таблицы:")
    for index, row in df.iterrows():
        row_data = ', '.join([f"{col}: {row[col]}" for col in df.columns])
        print(row_data)


def main():
    try:
        # Создание таблицы
        create_table(conn)

        # Наполнение таблицы данными
        insert_data(conn)

        # Вывод данных из таблицы
        fetch_data(conn)

    except psycopg2.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")


if __name__ == "__main__":
    db_user = "postgres"
    db_password = "999999"
    db_host = "db"
    db_port = "5432"
    db_name = "Attestation"
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )

    curses = conn.cursor()
    main()
    curses.close()
   # conn.close()


