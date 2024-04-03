from flask_login import UserMixin
from flask import url_for


class UserLogin(UserMixin):
    def fromDB(self, user_id, db):
        self.__user = db.getUser(user_id)
        return self

    def create(self, user):
        self.__user = user
        return self

    def get_id(self):
        return str(self.__user['id'])

    def getName(self):
        return self.__user['name'] if self.__user else "Без имени на сайте"

    def getEmail(self):
        return self.__user['email'] if self.__user else "Без email"

    def get_gender(self):
        return self.__user['gender'] if self.__user else "Без пола, это как?"

    def getPlace(self):
        return self.__user['place']

    def get_fullname(self):
        return self.__user['fullname'] if self.__user else "Без имени"

    def getAvatar(self, app):
        img = None
        if not self.__user['avatar']:
            try:
                with app.open_resource(app.root_path + url_for('static', filename='img/default.png'), "rb") as f:
                    img = f.read()
            except FileNotFoundError as e:
                print("Не найден аватар по умолчанию: " + str(e))
        else:
            img = self.__user['avatar']

        return img

    def verifyExt(self, filename):
        ext = filename.rsplit('.', 1)[1]
        if ext == "png" or ext == "PNG":
            return True
        return False
