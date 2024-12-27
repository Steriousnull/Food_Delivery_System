from Models.User import User
from Models.UserManager import UserManager



class LoginSystem:
    def Login(self):

        mailid = input("Email id : ")
        password = input("Password : ")

        user = UserManager.Finduser(mailid,password)

        if user is not None:
            print("login successful")
            pass
        else:
            print("Invalid mailid or password")




    def Register(self):
        
        name = input("Name : ")               #add validation just strings
        mobile = int(input("Mobile No : "))   #add validation just 10 numbers
        mailid = input("Email id : ")         #add validation just email format with @ , . etc
        password = input("Password : ")       #add validation starting letter capital and mixed characters and numbers
        #in memory location instead of database // storing data in list

        user = User(name, mobile, mailid, password)

        UserManager.AddUser(user)

    def GuestLogin(self):
        pass

    def ValidateOption(self, option):
        if option == 1:
            self.Login()

        elif option == 2:
            self.Register()

        elif option == 3:
            self.GuestLogin()

        elif option == 4:
            print("Thanks for using our Food App")
            exit()

        else:
            print("Invalid choice. Please Retry")




class FoodApp:

    LoginOptions = {1:"Login",2:"Register",3:"Guest",4:"Exit"}

    @staticmethod
    def Init():
        print("<< Welcome to Online Food Ordering >>") 

        loginSystem = LoginSystem()

        while True:
       
            for option in FoodApp.LoginOptions:
                print(f"{option}.{FoodApp.LoginOptions[option]}",end="  ")

            print()


            try:
                choice = int(input("Please Enter Your Choice : "))
                loginSystem.ValidateOption(choice)

            except ValueError:
                print("Invalid Input... Please enter the valid choice")



