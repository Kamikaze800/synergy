import math
import sqlite3
import time


class FDataBase:
    def __init__(self, db):
        self.__db = db  # ссылка на связь с базой данных
        self.__cur = db.cursor()

    def getMenu(self):
        sql = '''SELECT * FROM  mainmenu'''
        try:  # пытаемся прочитать данные с таблицы
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print('ошибка чтения БД')
        return []

    def addPost(self, title, text):
        try:
            tm = math.floor(time.time())
            self.__cur.execute('INSERT INTO posts VALUES(NULL, ?, ?, ?)', (title, text, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления статиь в БД ' + str(e))
        return True

    def getPost(self, postId):
        try:
            self.__cur.execute(f'SELECT title, text FROM posts WHERE id = {postId} LIMIT 1')
            res = self.__cur.fetchone()  # взять только 1 запись
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка получения статьи из БД' + str(e))

        return (False, False)

    def getPostsAnonce(self):
        try:
            self.__cur.execute(f'SELECT id, title, text FROM posts ORDER BY time DESC')  # сначала свежие
            res = self.__cur.fetchall()
            if res: return res
        except sqlite3.Error as e:
            print('Ошибка получения статьи из БД ' + str(e))

        return []
