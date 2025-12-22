from funny import FunnyHeadline, SportHeadline, WeatherHeadline, RandomHeadline

from user_register import login_Registration

from history import History

fn = FunnyHeadline()
sp = SportHeadline()
wt = WeatherHeadline()
dm = RandomHeadline()
hs = History()

lr = login_Registration()

class FakeHead:
    def headline_generater(self, module, title, category_name):
        news = "yes"
        headline = ""

        while news == "yes":
            headline = module.generate(title)
            print(headline)
            news = input("\nWant more headlines (Yes/No): ").lower().strip()

        save = input("You want to save this headline? (Yes/No): ").lower().strip()
        if save == "yes" or save == "y":
            hs.save_headline(category_name, headline)

        saved_head = input("Want to read saved headline? (yes/no):").lower().strip()
        if saved_head == "yes" or saved_head == "y":
            print(hs.get_data(category_name))

    def showmenu(self):
        option = 0
        while True:
            print("\n\nWhat type of news do you want?")
            print("1. Funny News")
            print("2. Sports News")
            print("3. Weather News")
            print("4. Random News")
            try:
                option = int(input("Enter your choice: "))
            except ValueError:
                print("\nChoose option in number only(1 to 4)")
            

            if option == 1:
                self.headline_generater(fn, "Funny Headlines 😂", "Funny")

            elif option == 2:
                self.headline_generater(sp, "Sports Headlines 🔥", "Sport")

            elif option == 3:
                self.headline_generater(wt, "Weather Headlines 🌦️", "Weather")
            
            elif option == 4:
                self.headline_generater(dm, "Random Headline", "Random")

            else:
                print("\nPlease enter valid choice. Try again...!")

    def user(self):
        print("1. You don't have an account. Please register first. (Press 1)")
        print("2. Already registered? Please log in. (Press 2)")
        print("3. If you want to skip registration (Press 3)")
        user_input = int(input("What your choice: "))
        if user_input == 1:
            result = lr.registration()
            if result == True:
                login_result = lr.login()
                if login_result == True:
                    self.showmenu()

        elif user_input == 2:
            log_result = lr.login()
            if log_result == True:
                self.showmenu()

        elif user_input == 3:
            self.showmenu()

fk = FakeHead()

fk.user()


