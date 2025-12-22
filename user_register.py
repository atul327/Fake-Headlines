from datetime import datetime

from history import Userdata

ud = Userdata()

class login_Registration:
    def registration(self):
        print("-----WELCOME to Headline generator App!-----")
        while True:
            self.name = input("Enter your name: ")
            try:
                self.age = int(input("Enter you age: "))
            except ValueError:
                print("Enter your age in number...")
            
            try:
                date_of_birth = input("Enter you Date of Birth (DD-MM-YYYY): ")
                self.dob_input = datetime.strptime(date_of_birth, "%d-%m-%Y").date()

                ud.save_user_details(self.name, self.age, date_of_birth)

                print('Registration successfull...!')
                return True
            
            except ValueError:
                print("Invalid date format! Use DD-MM-YYYY")


    def login(self):
        print("----WELCOME Again----")
        while True:
            entered_name = input("Enter your name: ")

            try:
                date_of_birth = input("Enter you Date of Birth (DD-MM-YYYY): ")
                DOB = datetime.strptime(date_of_birth, "%d-%m-%Y").date()
            except ValueError:
                print("Invalid date format! Use DD-MM-YYYY")
            
            if entered_name == self.name and DOB == self.dob_input:
                print("Login Successfull!")
                return True
            
            else:
                print("Invalid Credential")


