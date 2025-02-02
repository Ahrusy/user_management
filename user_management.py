class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

    def __str__(self):
        return f"User(ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level})"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self._users = []

    def add_user(self, user):
        if isinstance(user, User):
            self._users.append(user)
            print(f"Пользователь {user.get_name()} успешно добавлен.")
        else:
            print("Некорректный объект пользователя.")

    def remove_user(self, user_id):
        for user in self._users:
            if user.get_user_id() == user_id:
                self._users.remove(user)
                print(f"Пользователь с ID {user_id} успешно удален.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    def list_users(self):
        if not self._users:
            print("В системе нет пользователей.")
        else:
            for user in self._users:
                print(user)


# Пример использования
if __name__ == "__main__":
    admin = Admin(1, "Администратор")

    user1 = User(2, "Руслан")
    user2 = User(3, "Вадим")

    admin.add_user(user1)
    admin.add_user(user2)

    admin.list_users()

    admin.remove_user(2)

    admin.list_users()