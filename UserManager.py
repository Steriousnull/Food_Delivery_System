from Models.User import User

class UserManager:
    __Users = []

    @classmethod
    def AddUser(cls, userObj):
        if isinstance(userObj, User):
            cls.__Users.append(userObj)
            print("You have been successfully registered")
        else:
            print('Invalid User')

    @classmethod
    def Finduser(cls, mailid, pwd):
        for user in cls.__Users:
            if user.Mail == mailid and user.Password == pwd:  # Ensure attributes match
                return user
        return None
