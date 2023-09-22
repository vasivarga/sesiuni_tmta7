class User:
    __username = ""
    __password = ""
    _has_full_rights = False

    @property
    def username(self):
        pass

    @username.setter
    def username(self, username_ext):
        if "@" in username_ext and ".com" in username_ext:
            print("Numele de utilizator a fost setat cu succes")
            self.__username = username_ext
        else:
            print(f"Numele de utilizator {username_ext} nu a fost setat, trebuie sa contina @ si .com ")

    @username.getter
    def username(self):
        return self.__username

    @property
    def password(self):
        pass

    @password.getter
    def password(self):
        if self._has_full_rights:
            return self.__password
        else:
            print("Acces refuzat, nu aveti drepul sa vedeti parola")
            return ""

    @password.setter
    def password(self, pass_ext):
        self.__password = pass_ext

    # def get_username(self):
    #     return self.__username
    #
    # def set_username(self, username_ext):
    #     self.__username = username_ext
    #
    # def get_password(self):
    #     return self.__password
    #
    # def set_password(self, pass_ext):
    #     self.__password = pass_ext


user1 = User()
user1._has_full_rights = True

# user1.set_username("tmta7")
# print(user1.get_username())
user1.username = "tmta7@itfactory.com"

user2 = User()
user2.username = "pop.ion@itfactory.com"
# user2.set_username("pop.ion")
# print(user2.get_username())

user1.password = "Alabala"
user2.password = "Portocala"

user1._has_full_rights = True
user2._has_full_rights = False


print(user1.password)
print(user2.password)




