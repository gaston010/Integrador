import mysql.connector as mysql


class Conexion:

    def __init__(self):
        try:
            self.conexion = mysql.connect(
                host="sql.freedb.tech",
                user="freedb_discordia",
                password="kn@QS6G3F2$WGtJ",
                database="freedb_discordia"
            )
            self.cursor = self.conexion.cursor()
        except Exception as e:
            print(e)
        finally:
            print("Conexion exitosa")

    def execute(self, sql, params=None):
        try:
            self.cursor.execute(sql, params)
            self.conexion.commit()
            return self.cursor
        except Exception as e:
            return Exception(e)

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conexion.close()

    def commit(self):
        self.conexion.commit()

    def rollback(self):
        self.conexion.rollback()

    def rowcount(self):
        return self.cursor.rowcount
