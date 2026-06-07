import Pyro5.api
import sqlite3
from datetime import datetime


@Pyro5.api.expose
class Calculator:

    def tinh_tong(self, n):

        print("\n==============================")
        print(f"Nhan yeu cau tinh tong n = {n}")
        print("==============================")

        tong = 0

        for i in range(1, n + 1):
            tong += i

            print(
                f"Buoc {i}: "
                f"tong = {tong - i} + {i} = {tong}"
            )

        print("------------------------------")
        print(f"Ket qua cuoi cung = {tong}")

        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS ketqua(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                n INTEGER,
                result INTEGER,
                time TEXT
            )
            """)

            cursor.execute(
                """
                INSERT INTO ketqua(n, result, time)
                VALUES (?, ?, ?)
                """,
                (
                    n,
                    tong,
                    datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                )
            )

            conn.commit()
            conn.close()

            print("Da luu vao database")

        except Exception as e:
            print("Loi database:", e)

        return {
            "n": n,
            "tong": tong
        }


daemon = Pyro5.api.Daemon(
    host="localhost",
    port=40101
)

calculator = Calculator()

uri = daemon.register(calculator)

print("===== SERVER DANG CHAY =====")
print("URI:")
print(uri)

daemon.requestLoop()