import pyodbc

def handle_admin(dsn, conn):
    print("Просмотр:")
    try:
        conn_db = pyodbc.connect(dsn)
        cursor = conn_db.cursor()


        cursor.execute("SELECT [ID], [Time_log], [login] FROM [Users]")
        users = cursor.fetchall()

        users_str = "\nПользователи:\n\n"
        for row in users:
            users_str += f"ID: {row[0]} Был в сети: {row[1]} Логин: {row[2]}\n"



        full_result = users_str

        print("rez:")
        print(full_result)
        conn.send(full_result.encode())
    except Exception as e:
        print(f"Ошибка подключения: {e}")
        conn.send(f"Ошибка подключения: {e}".encode())