from datetime import datetime

from history import Userdata

ud = Userdata()

class login_Registration:
    def registration(self):
        print("-----WELCOME to Headline generator App!-----")
        
        self.name = input("Enter your name: ")

        while True:
            try:
                self.age = int(input("Enter you age: "))
            except ValueError:
                print("Enter your age in number...")
            
            try:
                date_of_birth = input("Enter you Date of Birth (DD-MM-YYYY): ")
                self.dob_input = datetime.strptime(date_of_birth, "%d-%m-%Y").date()

                ud.save_user_details(self.name, self.age, date_of_birth)

                return_age = ud.get_age()

                # Calculating age using date of year
                today = datetime.today()
                formated_age = datetime.strptime(date_of_birth, "%d-%m-%Y")
                calculate_age = today.year - formated_age.year

                if return_age == calculate_age:
                    print('Registration successfull...!')
                    return True
                else:
                    print("Registration Failed! Enter correct Age With your birth of year")
            
            except ValueError:
                print("Invalid date format! Use DD-MM-YYYY")


    def login(self):
        print("----WELCOME Again----")
        while True:
            entered_name = input("Enter your name: ")

            try:
                date_of_birth = input("Enter you Date of Birth (DD-MM-YYYY): ")
                
                # converting string format of date into date fromat
                DOB = datetime.strptime(date_of_birth, "%d-%m-%Y")

            except ValueError:
                print("Invalid date format! Use DD-MM-YYYY")
            
            u_name, u_dob = ud.get_user_details()
            
            # converting date int an String fromat
            formatted_dob = datetime.strptime(u_dob, "%d-%m-%Y")

            if entered_name == u_name and DOB == formatted_dob:
                print("Login Successfull!")
                return True
            
            else:
                print("Invalid Credential")


