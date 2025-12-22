from datetime import datetime


class login_Registration:
    def registratin(self):
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
                print('Registration successfull...!')
                return True
            
            except ValueError:
                print("Invalid date format! Use DD-MM-YYYY")


    


