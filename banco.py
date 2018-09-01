import mysql.connector
import time


class Connection:
    def __init__(self):
        self.open_connection()

    def open_connection(self):
        self.connect = mysql.connector.connect(user='', password='', host='', database='')
        self.cursor = self.connect.cursor()

    def commit_close(self):
        self.connect.commit()
        self.cursor.close()
        self.connect.close()

    def add_log(self, user, time, data):
        self.open_connection()
        query = "insert into log(nome,horario,data) values (%s,%s,%s)"
        params = user, time, data
        self.cursor.execute(query, params)
        self.commit_close()

    def get_name(self, password):
        self.open_connection()
        query = "select senha from user where nome=%s"
        params = password
        self.cursor.execute(query, (params,))
        username, password = self.cursor.fetchall()
        return username

    def check_pass(self, password):
        self.open_connection()
        query = "select * from user where senha=%s"
        params = password
        self.cursor.execute(query, (params,))
        result = self.cursor.fetchall()
        self.cursor.close()
        self.connect.close()
        if (len(result) > 0):
            username, password = result[0]
            self.add_log(username, time.strftime('%H:%M'), time.strftime('%d-%m-%Y'))
            return 1
        else:
            return 0

    def create_user(self, username, password):
        self.open_connection()
        query = "insert into user(nome,senha) values(%s,%s)"
        params = username, password
        self.cursor.execute(query, params)
        self.commit_close()
